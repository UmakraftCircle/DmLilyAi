"""Composition root: the only place that wires domains to infrastructure."""
import time
from dataclasses import dataclass
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
from LilyAiMemory.FanGain.fan_gain import FanSnapshotStore
from LilyAiMemory.service import MemoryService
from LilyAiRag.service import RagService
from LilyAiTask.DailyTask.DeficitTask.Deficit import DeficitTracker
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
            "recent events, or anything you're unsure about.",
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

    return [
        ToolSpec(
            "check_umamoe",
            "Check current uma.moe circle standing (rank, points, member count) for the tracked club(s), "
            "or a specific circle_id if given.",
            {"type": "object", "properties": {"circle_id": {"type": "integer"}}, "required": []},
            check_umamoe, category="umamoe", timeout=15,
        ),
    ]


def _fan_gain_job(app: App, trainer_link_store, fan_store: FanSnapshotStore,
                   umamoe: UmamoeClient, circle_id: int, club: str):
    """Build one scheduler job: snapshot every linked trainer's current fan total for
    `club`/`circle_id` (via the real UmamoeClient - see snapshot_job.py) and send the
    daily quota DM.

    `trackers` is created once here and closed over, so DeficitTracker state (carry,
    total_gained) persists across runs for the life of the process, per club, exactly
    as run_daily_fan_gain's docstring expects.

    app.discord_client isn't set yet when jobs are registered below (Discord connects
    after build_app() returns - see main.py), so it's read lazily on every run instead,
    the same way LilyAiMain/MainService/Api/server.py's _discord_or_400() does.
    """
    trackers: dict[str, DeficitTracker] = {}

    async def run() -> None:
        client = app.discord_client
        if not client or not client.is_ready():
            log.info("daily-fan-gain (%s): Discord not connected yet, skipping this run", club)
            return
        await run_daily_fan_gain(client, trainer_link_store, fan_store, umamoe, circle_id, club, trackers)

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
        # One daily fan-snapshot + quota job per tracked circle (see snapshot_job.py).
        # Club names follow the convention already used there and in .env.example's
        # "your 2 clubs" comment: the first tracked circle is "Umakraft", any further
        # ones are numbered. Re-map UMAMOE_CIRCLE_IDS's order if that's ever not right.
        #
        # The in-process Scheduler only supports fixed intervals, not a fixed time of
        # day, so this runs once every 24h from process start rather than at a specific
        # UTC hour - close enough for a daily quota reminder, but worth revisiting if
        # the DM needs to land at a particular time.
        for i, circle_id in enumerate(settings.umamoe_circle_ids, start=1):
            club = "Umakraft" if i == 1 else f"Umakraft {i}"
            scheduler.every(
                f"daily-fan-gain-{i}",
                24 * 3600,
                _fan_gain_job(app, memory.trainer_link, memory.fan_gain, umamoe, circle_id, club),
                initial_delay_s=120.0,
            )

    return app
