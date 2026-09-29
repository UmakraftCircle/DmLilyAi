"""Composition root: the only place that wires domains to infrastructure."""
import json
import time
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Any

from LilyAiContext.service import ContextBuilder
from LilyAiCore.Config.models import ModelPool
from LilyAiCore.Config.settings import Settings
from LilyAiCore.ExternalServices.Database.sqlite import Database
from LilyAiCore.ExternalServices.Database.turso import TursoDatabase
from LilyAiCore.ExternalServices.Discord.notifier import NotifierBox
from LilyAiCore.ExternalServices.Discord.reconnect_state import ReconnectState
from LilyAiCore.ExternalServices.Discord.relay_channel_store import RelayChannelStore
from LilyAiCore.ExternalServices.Discord.reminder_store import ReminderStore
from LilyAiCore.ExternalServices.Search.base import SearchProvider
from LilyAiCore.ExternalServices.Umamoe.client import UmamoeClient
from LilyAiCore.ExternalServices.Umamoe.gains import member_gains
from LilyAiCore.ExternalServices.Umamoe.store import UmamoeStore
from LilyAiCore.ExternalServices.Umapyoi.client import UmapyoiClient
from LilyAiCore.Logging.logger import get_logger
from LilyAiCore.Providers.base import LLMProvider
from LilyAiCore.Providers.offline import OfflineProvider
from LilyAiLearning.Evaluation.model_scan import ModelScanner
from LilyAiLearning.service import LearningService
from LilyAiMain.MainService.Discord.Events.bus import EventBus
from LilyAiMain.MainService.Discord.Events.channel_watch import ChannelWatch
from LilyAiMain.MainService.Discord.Events.handlers import DiscordEventHandlers
from LilyAiMain.MainService.Discord.Middleware.middleware import AccessControl, RateLimiter
from LilyAiMain.MainService.Discord.Router.router import DMRouter
from LilyAiMain.MainService.Discord.Session.manager import SessionManager
from LilyAiMain.MainService.Interaction.Feedback.feedback import FeedbackHandler, ReplyLog
from LilyAiMain.MainService.Interaction.Forms.forms import FormManager
from LilyAiMain.MainService.Interaction.Forms.link_trainer import LinkTrainerFlow
from LilyAiMain.MainService.Interaction.Onboarding.onboarding import OnboardingFlow
from LilyAiMain.MainService.Interaction.Polls.polls import PollManager
from LilyAiMain.MainService.Interaction.Workflows.chat_workflow import ChatWorkflow
from LilyAiMain.MainService.Interaction.Workflows.model_scan_job import make_model_scan_job
from LilyAiMain.MainService.Interaction.Workflows.scheduler import Scheduler
from LilyAiMain.MainService.Interaction.Workflows.self_ping_job import make_self_ping_job
from LilyAiMain.MainService.Interaction.Workflows.umamoe_job import make_umamoe_job
from LilyAiMemory.DeficitState.deficit_state_store import DeficitStateStore
from LilyAiMemory.FanGain.fan_gain import FanSnapshotStore
from LilyAiMemory.JobRuns.job_run_store import JobRunStore
from LilyAiMemory.service import MemoryService
from LilyAiRag.service import RagService
from LilyAiTask.DailyTask.DeficitTask.snapshot_job import run_daily_fan_gain
from LilyAiTool.service import ToolContextData, ToolService, ToolSpec
from LilyAiWeb.service import WebService

log = get_logger("bootstrap")


@dataclass
class App:
    settings: Settings
    pool: ModelPool
    db: Database | TursoDatabase
    provider: LLMProvider
    memory: MemoryService
    rag: RagService
    web: WebService
    tools: ToolService
    learning: LearningService
    chat: ChatWorkflow
    router: DMRouter
    feedback: FeedbackHandler
    bus: EventBus
    discord_state: DiscordEventHandlers
    scanner: ModelScanner
    scheduler: Scheduler
    notifier_box: NotifierBox
    umamoe: UmamoeClient | None
    umamoe_store: UmamoeStore | None
    discord_reconnect: ReconnectState
    channel_watch: ChannelWatch
    relay_channel_store: RelayChannelStore
    started_at: float
    # Set from main.py once LilyDiscordClient exists (built after the API/App, so it can't be
    # wired in here). None whenever Discord is disabled or hasn't connected yet - callers using
    # it (the /api/relay/channel* endpoints) check for that.
    discord_client: Any = None

    async def aclose(self) -> None:
        await self.scheduler.stop()
        await self.provider.aclose()
        self.db.close()


def _build_db(settings: Settings) -> Database | TursoDatabase:
    if settings.turso_database_url:
        log.info("Turso database configured: using embedded replica synced against %s", settings.turso_database_url)
        return TursoDatabase(
            settings.db_path, settings.turso_database_url, settings.turso_auth_token,
            sync_interval_s=settings.turso_sync_interval_s,
        )
    return Database(settings.db_path)


def _seconds_until_utc(hour: int, minute: int = 0) -> float:
    """Seconds from now until the next hour:minute UTC (today if that time hasn't
    happened yet today, otherwise tomorrow).

    Used to align a daily scheduler job to a fixed time of day. Recomputed fresh
    on every process start (build_app() calls this, it's not itself persisted),
    so a restart just re-targets the next occurrence rather than drifting - and
    since the moment a day's target time has passed, "next occurrence" is always
    tomorrow, a same-day restart can never compute a delay that lands on today
    again. That still leaves a narrow race if two processes are briefly alive at
    once (e.g. a rolling Render redeploy) with both about to fire close together;
    JobRunStore (see _fan_gain_job) is the actual guarantee against a double send,
    this is just what makes it happen at 19:00 UTC instead of at process-start-
    plus-N in the first place.
    """
    now = datetime.now(timezone.utc)
    target = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if target <= now:
        target += timedelta(days=1)
    return (target - now).total_seconds()


def _web_tools(web: WebService) -> list[ToolSpec]:
    async def web_search(ctx: ToolContextData, args: dict) -> str:
        docs = await web.research(args["query"], limit=3, read_top=2)
        if not docs:
            return "No results found."
        ctx.extra.setdefault("domains", []).extend(d.domain for d in docs)
        return "\n\n".join(f"[{i}] {d.as_snippet(1200)}" for i, d in enumerate(docs, 1))

    async def read_webpage(ctx: ToolContextData, args: dict) -> str:
        doc = await web.read(args["url"], 5000)
        ctx.extra.setdefault("domains", []).append(doc.domain)
        return doc.as_snippet(5000)

    return [
        ToolSpec(
            "web_search",
            "Search the web for current or factual information and read the top pages. Use for news, prices, "
            "recent events, or anything you're unsure about. Never use this (or read_webpage) to look up uma.moe "
            "fan gain, circle standing, or leaderboard data - use check_umamoe / check_fan_gain instead, even for "
            "this bot's own site.",
            {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]},
            web_search, category="web", timeout=30,
        ),
        ToolSpec(
            "read_webpage",
            "Fetch and read the text of a specific web page URL.",
            {"type": "object", "properties": {"url": {"type": "string"}}, "required": ["url"]},
            read_webpage, category="web", timeout=30,
        ),
    ]


def _umamoe_tools(client: UmamoeClient, default_circle_ids: tuple[int, ...]) -> list[ToolSpec]:
    async def check_umamoe(ctx: ToolContextData, args: dict) -> str:
        circle_id = args.get("circle_id")
        ids = (circle_id,) if circle_id else default_circle_ids
        if not ids:
            return "No uma.moe circle configured. Set UMAMOE_CIRCLE_IDS or pass a circle_id."
        lines = []
        for cid in ids:
            data = await client.get_circle(circle_id=cid)
            c = data.get("circle") or {}
            lines.append(
                f"{c.get('name', cid)}: rank {c.get('monthly_rank', '?')}, "
                f"{c.get('monthly_point', '?')} pts, {c.get('member_count', '?')} members"
            )
        return "\n".join(lines)

    _SORT_KEYS = {"today": "today_gain", "monthly": "monthly_gain", "total": "total_fans"}

    async def check_fan_gain(ctx: ToolContextData, args: dict) -> str:
        circle_id = args.get("circle_id")
        name_filter = (args.get("trainer_name") or "").strip().lower()
        # Trainer IDs are numeric uma.moe viewer_ids. Accept an int or a string like "123,456,789" and
        # compare digits only, so a linked user can be found by ID even if their name isn't on file.
        id_filter = "".join(ch for ch in str(args.get("trainer_id") or "") if ch.isdigit())
        # "total" (current total fans) matches how a fan-gain LEADERBOARD is normally ranked -
        # same as /api/leaderboard and uma.moe's own site - so it's the default rather than
        # today_gain, which only makes sense when the user specifically asks about today.
        sort_by = args.get("sort_by") or "total"
        sort_key = _SORT_KEYS.get(sort_by, "total_fans")
        ids = (circle_id,) if circle_id else default_circle_ids
        if not ids:
            return "No uma.moe circle configured. Set UMAMOE_CIRCLE_IDS or pass a circle_id."
        sections = []
        for cid in ids:
            data = await client.get_circle(circle_id=cid)
            circle_name = (data.get("circle") or {}).get("name", str(cid))
            rows = []
            for m in data.get("members", []):
                viewer_id = str(m.get("viewer_id") or "")
                trainer_name = m.get("trainer_name") or viewer_id
                if id_filter and viewer_id != id_filter:
                    continue
                if name_filter and name_filter not in trainer_name.lower():
                    continue
                rows.append((trainer_name, viewer_id, member_gains(m.get("daily_fans"))))
            if not rows:
                continue
            rows.sort(key=lambda r: r[2][sort_key], reverse=True)
            total_members = len(rows)
            shown = rows[:25]  # keep replies readable for a full-roster query
            section = [f"**{circle_name}** (ranked by {sort_by} fan gain)"]
            # Numbered so the model relays the rank instead of counting bullets itself.
            for rank, (trainer_name, viewer_id, g) in enumerate(shown, start=1):
                id_part = f" (Trainer ID {viewer_id})" if viewer_id else ""
                section.append(
                    f"{rank}. {trainer_name}{id_part}: {g['today_gain']:,} today, {g['monthly_gain']:,} this month "
                    f"(total {g['total_fans']:,})"
                )
            if total_members > len(shown):
                # Told explicitly, not left implicit - otherwise a >25-member circle silently gets
                # presented as a complete leaderboard when it's actually been cut off.
                section.append(
                    f"...(showing top {len(shown)} of {total_members} members - filter by trainer_name "
                    "or trainer_id for anyone not shown)"
                )
            sections.append("\n".join(section))
        if not sections:
            if id_filter:
                return (
                    f"No member with Trainer ID {id_filter} found in the tracked club(s) - "
                    "they may not be in the circle, or the ID may be wrong."
                )
            return f"No trainer matching '{args.get('trainer_name')}' found." if name_filter else "No members found."
        return "\n\n".join(sections)

    return [
        ToolSpec(
            "check_umamoe",
            "Check current uma.moe CIRCLE-level standing (overall rank, points, member count) for the tracked "
            "club(s), or a specific circle_id if given. Does NOT include individual members' fan numbers - use "
            "check_fan_gain for that.",
            {"type": "object", "properties": {
                "circle_id": {"type": ["integer", "null"], "description": "Omit or pass null for the default club(s)"},
            }, "required": []},
            check_umamoe, category="umamoe", timeout=15,
        ),
        ToolSpec(
            "check_fan_gain",
            "Look up today's and this month's fan gain, plus current total fans, per trainer in the tracked "
            "uma.moe club(s), returned as a numbered, ranked list. Optionally filter to one trainer by trainer_id "
            "(the numeric uma.moe Trainer ID - most exact, use it whenever you have one, e.g. from "
            "get_linked_trainer) or by trainer_name. Use this for any request about fan gain, fan numbers, or a "
            "fan leaderboard - never try to fetch or scrape this bot's own web pages for it. IMPORTANT: pass "
            "sort_by matching what was actually asked (e.g. 'today's leaderboard' -> sort_by='today') rather "
            "than re-sorting the returned list yourself.",
            {"type": "object", "properties": {
                "circle_id": {"type": ["integer", "null"], "description": "Omit or pass null for the default club(s)"},
                "trainer_id": {
                    "type": ["string", "integer", "null"],
                    "description": "Numeric uma.moe Trainer ID to look up exactly; omit or pass null to not filter by ID",
                },
                "trainer_name": {
                    "type": ["string", "null"],
                    "description": "Filter to trainers whose name contains this; omit or pass null for everyone",
                },
                "sort_by": {
                    "type": ["string", "null"],
                    "enum": ["today", "monthly", "total", None],
                    "description": (
                        "Rank by 'today' (today's gain), 'monthly' (this month's gain), or 'total' (current "
                        "total fans - the standard leaderboard ranking, and the default if omitted)."
                    ),
                },
            }, "required": []},
            check_fan_gain, category="umamoe", timeout=15,
        ),
    ]


def _trainer_link_tools(trainer_link_store) -> list[ToolSpec]:
    """Expose the Discord<->uma.moe Trainer ID link (see LilyAiMemory/TrainerLink) to the chat model.

    The link itself is created out-of-band via the "link me" DM flow (LinkTrainerFlow) and stored
    in TrainerLinkStore, but until now nothing in the tool registry could read it back, so the model
    had no way to answer "what's my trainer ID" and could only look trainers up by an ID/name the
    user typed in fresh - even for a user who had already linked one.
    """

    def get_linked_trainer(ctx: ToolContextData, args: dict) -> str:
        if not ctx.user_id:
            return "No Discord user in this context to look up."
        link = trainer_link_store.by_discord_id(ctx.user_id)
        if not link:
            return (
                "This Discord account isn't linked to a uma.moe Trainer ID yet. "
                "They can link one by saying \"link me\"."
            )
        name_part = f" ({link.trainer_name})" if link.trainer_name else ""
        return (
            f"This Discord account is linked to uma.moe Trainer ID `{link.trainer_id}`{name_part}. "
            f"For their fan numbers, call check_fan_gain with trainer_id=\"{link.trainer_id}\" (if that tool is available)."
        )

    return [
        ToolSpec(
            "get_linked_trainer",
            "Look up the uma.moe Trainer ID linked to the CURRENT Discord user (the person you're chatting "
            "with right now). Call this whenever the user refers to \"my\" trainer/stats/fan gain without "
            "giving an explicit Trainer ID or name - resolve it here first, then pass the returned Trainer ID "
            "as trainer_id into check_fan_gain. Takes no arguments; it always looks up the current user and "
            "never anyone else's account.",
            {"type": "object", "properties": {}, "required": []},
            get_linked_trainer, category="umamoe",
        ),
    ]


def _umapyoi_tools(client: UmapyoiClient) -> list[ToolSpec]:
    """Supplementary Uma Musume game-trivia tools (umapyoi.net - keyless, no rotation needed).

    These are secondary/flavor tools, not core features - check_umamoe/check_fan_gain (circle
    and fan tracking) and web_search (everything else current/factual) remain the bot's primary
    tools. Every tool description below says so explicitly so the model doesn't reach for these
    over the primary two, and each just returns compact JSON straight from the API rather than
    a hand-formatted string, since the response schema isn't pinned down anywhere - the model
    can read and summarize the JSON fine, and this avoids silently-wrong formatting if a field
    name turns out different than expected.
    """

    def _json(data, limit: int = 3000) -> str:
        return json.dumps(data, ensure_ascii=False)[:limit]

    async def check_gacha_banner(ctx: ToolContextData, args: dict) -> str:
        return _json(await client.gacha_current())

    async def check_umamusume_news(ctx: ToolContextData, args: dict) -> str:
        count = args.get("count") or 5
        return _json(await client.news_latest(count=count, english=True))

    async def check_character_birthdays(ctx: ToolContextData, args: dict) -> str:
        return _json(await client.character_birthdays())

    async def check_character(ctx: ToolContextData, args: dict) -> str:
        entry = await client.find_character(args["name"])
        if not entry:
            return f"No character found matching '{args['name']}'."
        return _json(entry, limit=2000)

    _note = (
        "This is a secondary game-trivia tool, not a primary one - check_umamoe/check_fan_gain "
        "(circle and fan tracking) and web_search (everything else current) come first; only "
        "reach for this when the request is specifically "
    )
    return [
        ToolSpec(
            "check_gacha_banner",
            _note + "about the current in-game gacha banner (what outfits/support cards are featured right now).",
            {"type": "object", "properties": {}, "required": []},
            check_gacha_banner, category="umapyoi", timeout=15,
        ),
        ToolSpec(
            "check_umamusume_news",
            _note + "for recent official Uma Musume game news/announcements.",
            {"type": "object", "properties": {
                "count": {"type": ["integer", "null"], "description": "How many posts, max 32; omit for 5"},
            }, "required": []},
            check_umamusume_news, category="umapyoi", timeout=15,
        ),
        ToolSpec(
            "check_character_birthdays",
            _note + "about which character(s) have a birthday today or next.",
            {"type": "object", "properties": {}, "required": []},
            check_character_birthdays, category="umapyoi", timeout=15,
        ),
        ToolSpec(
            "check_character",
            _note + "asking for a specific character's game info/profile by name.",
            {"type": "object", "properties": {"name": {"type": "string"}}, "required": ["name"]},
            check_character, category="umapyoi", timeout=15,
        ),
    ]


def _fan_gain_job(app: App, trainer_link_store, fan_store: FanSnapshotStore, tracker_store: DeficitStateStore,
                   job_run_store: JobRunStore, job_name: str, umamoe: UmamoeClient, circle_id: int, club: str):
    """Build one scheduler job: snapshot every linked trainer's current fan total for
    `club`/`circle_id` (via the real UmamoeClient - see snapshot_job.py) and send the
    daily quota DM.

    No in-memory tracker state is kept here: run_daily_fan_gain loads and saves each
    trainer's DeficitTracker carry/total_gained through tracker_store on every call, so
    it's correct on the very first run and survives process restarts/redeploys.

    job_run_store/job_name guard against sending the same UTC day's DM twice if the
    process restarts right around the scheduled time - see JobRunStore's docstring.
    Checked (and claimed via mark_run) BEFORE calling run_daily_fan_gain, so even a
    process that started moments after another one already ran today skips instead
    of re-sending every linked trainer's DM.

    app.discord_client isn't set yet when jobs are registered below (Discord connects
    after build_app() returns - see main.py), so it's read lazily on every run instead,
    the same way LilyAiMain/MainService/Api/server.py's _discord_or_400() does.
    """

    async def run() -> None:
        client = app.discord_client
        if not client or not client.is_ready():
            log.info("daily-fan-gain (%s): Discord not connected yet, skipping this run", club)
            return
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        if job_run_store.has_run(job_name, today):
            log.info("daily-fan-gain (%s): already ran today (%s), skipping", club, today)
            return
        job_run_store.mark_run(job_name, today)
        await run_daily_fan_gain(client, trainer_link_store, fan_store, tracker_store, umamoe, circle_id, club)

    return run


def build_app(
    settings: Settings,
    provider: LLMProvider | None = None,
    search_provider: SearchProvider | None = None,
    db: Database | TursoDatabase | None = None,
) -> App:
    pool = ModelPool()
    db = db or _build_db(settings)

    if provider is None:
        if settings.groq_api_keys:
            from LilyAiCore.Providers.Groq.client import GroqProvider

            provider = GroqProvider(list(settings.groq_api_keys), settings.groq_base_url, settings.chat_model, pool)
            log.info("Groq provider ready with %d API key(s)", len(settings.groq_api_keys))
        else:
            log.warning("GROQ_API_KEY not set: running with the offline provider")
            provider = OfflineProvider()

    if search_provider is None:
        if settings.tavily_api_keys:
            from LilyAiCore.ExternalServices.Search.tavily import TavilySearch

            search_provider = TavilySearch(list(settings.tavily_api_keys))
            log.info("Tavily search provider ready with %d API key(s)", len(settings.tavily_api_keys))
        else:
            from LilyAiCore.ExternalServices.Search.duckduckgo import DuckDuckGoSearch

            search_provider = DuckDuckGoSearch()
            log.info("TAVILY_API_KEY not set: web_search/read_webpage fall back to the DuckDuckGo HTML scraper")

    scanner = ModelScanner(
        provider, pool, settings.model_scan_state_path, settings.model_scan_docs_dir,
        fallback_docs_dir=settings.data_dir, max_auto=settings.model_scan_max_auto,
    )
    restored = scanner.load_into_pool()
    if restored:
        log.info("restored %d auto-added model(s) into the pool", restored)

    memory = MemoryService(db)
    learning = LearningService(db)
    rag = RagService(settings.rag_path)
    web = WebService(search_provider, learning.web.preferred_domains())
    notifier_box = NotifierBox(ReminderStore(db))
    discord_reconnect = ReconnectState(db)
    tools = ToolService(notifier_box)
    for spec in _web_tools(web):
        tools.register(spec)
    for spec in _trainer_link_tools(memory.trainer_link):
        tools.register(spec)

    umamoe = UmamoeClient(settings.umamoe_api_key) if settings.umamoe_api_key else None
    umamoe_store = UmamoeStore(db) if umamoe else None
    if umamoe:
        for spec in _umamoe_tools(umamoe, settings.umamoe_circle_ids):
            tools.register(spec)
    else:
        log.info("UMAMOE_API_KEY not set: uma.moe circle tracking (Leaderboard, check_umamoe) is disabled")

    if settings.umapyoi_enabled:
        for spec in _umapyoi_tools(UmapyoiClient()):
            tools.register(spec)
        log.info("umapyoi.net game-data tools ready (secondary to check_umamoe/check_fan_gain/web_search)")
    else:
        log.info("UMAPYOI_ENABLED=false: umapyoi.net game-data tools (banners/news/birthdays/character) are disabled")

    chat = ChatWorkflow(settings, provider, memory, rag, tools, ContextBuilder(settings.token_budget), learning)
    replies, bus = ReplyLog(), EventBus()
    forms, polls = FormManager(), PollManager()
    router = DMRouter(
        memory, chat, replies, bus, SessionManager(), RateLimiter(), AccessControl(settings.allowed_user_ids),
        forms, polls, OnboardingFlow(memory, forms, polls), LinkTrainerFlow(memory, forms),
    )
    if not settings.webhook_url:
        log.info("WEBHOOK_URL not set: ops alerts (task crashes, job failures) are logged only")
    scheduler = Scheduler(settings.webhook_url)
    if settings.model_scan_enabled and not isinstance(provider, OfflineProvider):
        if settings.model_scan_interval_s is not None:
            # Explicit seconds override (e.g. MODEL_SCAN_INTERVAL_SECONDS=600). 60s floor guards
            # against a mistyped tiny value hammering the Groq API.
            interval = max(60.0, settings.model_scan_interval_s)
        else:
            interval = max(1.0, settings.model_scan_interval_hours) * 3600
        # first run waits out whatever is left of the interval since the last scan (min 60s after start)
        scheduler.every("model-scan", interval, make_model_scan_job(scanner, bus),
                        initial_delay_s=max(60.0, scanner.seconds_until_due(interval)))
    if umamoe and settings.umamoe_circle_ids:
        if settings.umamoe_poll_interval_s is not None:
            # Explicit seconds override (e.g. UMAMOE_POLL_INTERVAL_SECONDS=300 = every 5 minutes).
            # 60s floor guards against a mistyped tiny value hammering the uma.moe API.
            umamoe_interval = max(60.0, settings.umamoe_poll_interval_s)
        else:
            umamoe_interval = max(1.0, settings.umamoe_poll_interval_hours) * 3600
        scheduler.every("umamoe-poll", umamoe_interval,
                        make_umamoe_job(umamoe, umamoe_store, notifier_box, settings.umamoe_circle_ids,
                                        settings.umamoe_notify_user_id, bus),
                        initial_delay_s=10.0)
    elif umamoe:
        log.info("UMAMOE_CIRCLE_IDS not set: check_umamoe works on demand but background polling is off")
    if settings.enable_api and settings.self_ping_enabled:
        if settings.self_ping_url:
            ping_url = settings.self_ping_url.rstrip("/") + "/api/health"
            # 60s floor guards against a mistyped tiny value hammering the service's own API.
            ping_interval = max(60.0, settings.self_ping_interval_s)
            scheduler.every("self-ping", ping_interval, make_self_ping_job(ping_url), initial_delay_s=ping_interval)
        else:
            log.info("SELF_PING_ENABLED but no SELF_PING_URL/RENDER_EXTERNAL_URL set: self-ping is off")

    app = App(
        settings, pool, db, provider, memory, rag, web, tools, learning, chat, router,
        FeedbackHandler(replies, learning, rag), bus, DiscordEventHandlers(bus), scanner, scheduler,
        notifier_box, umamoe, umamoe_store, discord_reconnect, ChannelWatch(), RelayChannelStore(db), time.time(),
    )

    if umamoe and settings.umamoe_circle_ids:
        # One daily fan-snapshot + quota job per tracked circle (see snapshot_job.py),
        # fired at 19:00 UTC. _seconds_until_utc(19, 0) recomputes the delay to the
        # next 19:00 UTC fresh on every process start, so a restart just re-targets
        # the next occurrence instead of drifting off schedule. job_run_store guards
        # against sending the same UTC day's DM twice if a restart happens to land
        # right around 19:00 (e.g. old/new processes briefly overlapping during a
        # Render redeploy) - see JobRunStore's docstring.
        #
        # Club names follow the convention already used in snapshot_job.py and
        # .env.example's "your 2 clubs" comment: the first tracked circle is
        # "Umakraft", any further ones are numbered. Re-map UMAMOE_CIRCLE_IDS's
        # order if that's ever not right.
        for i, circle_id in enumerate(settings.umamoe_circle_ids, start=1):
            club = "Umakraft" if i == 1 else f"Umakraft {i}"
            job_name = f"daily-fan-gain-{i}"
            scheduler.every(
                job_name,
                24 * 3600,
                _fan_gain_job(app, memory.trainer_link, memory.fan_gain, memory.deficit_state,
                              memory.job_runs, job_name, umamoe, circle_id, club),
                initial_delay_s=_seconds_until_utc(19, 0),
            )

    return app
