"""Composition root: the only place that wires domains to infrastructure."""
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
    this is just what makes it happen at 11:00 UTC instead of at process-start-
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

    async def check_fan_gain(ctx: ToolContextData, args: dict) -> str:
        circle_id = args.get("circle_id")
        name_filter = (args.get("trainer_name") or "").strip().lower()
        ids = (circle_id,) if circle_id else default_circle_ids
        if not ids:
            return "No uma.moe circle configured. Set UMAMOE_CIRCLE_IDS or pass a circle_id."
        sections = []
        for cid in ids:
            data = await client.get_circle(circle_id=cid)
            circle_name = (data.get("circle") or {}).get("name", str(cid))
            rows = []
            for m in data.get("members", []):
                trainer_name = m.get("trainer_name") or str(m.get("viewer_id"))
                if name_filter and name_filter not in trainer_name.lower():
                    continue
                rows.append((trainer_name, member_gains(m.get("daily_fans"))))
            if not rows:
                continue
            rows.sort(key=lambda r: r[1]["today_gain"], reverse=True)
            section = [f"**{circle_name}**"]
            for trainer_name, g in rows[:25]:  # keep replies readable for a full-roster query
                section.append(
                    f"- {trainer_name}: {g['today_gain']:,} today, {g['monthly_gain']:,} this month "
                    f"(total {g['total_fans']:,})"
                )
            sections.append("\n".join(section))
        if not sections:
            return f"No trainer matching '{args.get('trainer_name')}' found." if name_filter else "No members found."
        return "\n\n".join(sections)

    return [
        ToolSpec(
            "check_umamoe",
            "Check current uma.moe CIRCLE-level standing (overall rank, points, member count) for the tracked "
            "club(s), or a specific circle_id if given. Does NOT include individual members' fan numbers - use "
            "check_fan_gain for that.",
            {"type": "object", "properties": {"circle_id": {"type": "integer"}}, "required": []},
            check_umamoe, category="umamoe", timeout=15,
        ),
        ToolSpec(
            "check_fan_gain",
            "Look up today's and this month's fan gain, plus current total fans, per trainer in the tracked "
            "uma.moe club(s). Optionally filter to one trainer_name. Use this for any request about fan gain, "
            "fan numbers, or a fan leaderboard - never try to fetch or scrape this bot's own web pages for it.",
            {"type": "object", "properties": {
                "circle_id": {"type": "integer"},
                "trainer_name": {"type": "string", "description": "Filter to trainers whose name contains this"},
            }, "required": []},
            check_fan_gain, category="umamoe", timeout=15,
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
        from LilyAiCore.ExternalServices.Search.duckduckgo import DuckDuckGoSearch

        search_provider = DuckDuckGoSearch()

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

    umamoe = UmamoeClient(settings.umamoe_api_key) if settings.umamoe_api_key else None
    umamoe_store = UmamoeStore(db) if umamoe else None
    if umamoe:
        for spec in _umamoe_tools(umamoe, settings.umamoe_circle_ids):
            tools.register(spec)
    else:
        log.info("UMAMOE_API_KEY not set: uma.moe circle tracking (Leaderboard, check_umamoe) is disabled")

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
        # fired at 11:00 UTC. _seconds_until_utc(11, 0) recomputes the delay to the
        # next 11:00 UTC fresh on every process start, so a restart just re-targets
        # the next occurrence instead of drifting off schedule. job_run_store guards
        # against sending the same UTC day's DM twice if a restart happens to land
        # right around 11:00 (e.g. old/new processes briefly overlapping during a
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
                initial_delay_s=_seconds_until_utc(11, 0),
            )

    return app
