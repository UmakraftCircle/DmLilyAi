"""Composition root: the only place that wires domains to infrastructure."""
import time
from dataclasses import dataclass

from LilyAiContext.service import ContextBuilder
from LilyAiCore.Config.models import ModelPool
from LilyAiCore.Config.settings import Settings
from LilyAiCore.ExternalServices.Database.sqlite import Database
from LilyAiCore.ExternalServices.Discord.notifier import NotifierBox
from LilyAiCore.ExternalServices.Discord.reminder_store import ReminderStore
from LilyAiCore.ExternalServices.Search.base import SearchProvider
from LilyAiCore.Logging.logger import get_logger
from LilyAiCore.Providers.base import LLMProvider
from LilyAiCore.Providers.offline import OfflineProvider
from LilyAiLearning.Evaluation.model_scan import ModelScanner
from LilyAiLearning.service import LearningService
from LilyAiMain.MainService.Discord.Events.bus import EventBus
from LilyAiMain.MainService.Discord.Events.handlers import DiscordEventHandlers
from LilyAiMain.MainService.Discord.Middleware.middleware import AccessControl, RateLimiter
from LilyAiMain.MainService.Discord.Router.router import DMRouter
from LilyAiMain.MainService.Discord.Session.manager import SessionManager
from LilyAiMain.MainService.Interaction.Feedback.feedback import FeedbackHandler, ReplyLog
from LilyAiMain.MainService.Interaction.Forms.forms import FormManager
from LilyAiMain.MainService.Interaction.Onboarding.onboarding import OnboardingFlow
from LilyAiMain.MainService.Interaction.Polls.polls import PollManager
from LilyAiMain.MainService.Interaction.Workflows.chat_workflow import ChatWorkflow
from LilyAiMain.MainService.Interaction.Workflows.model_scan_job import make_model_scan_job
from LilyAiMain.MainService.Interaction.Workflows.scheduler import Scheduler
from LilyAiMemory.service import MemoryService
from LilyAiRag.service import RagService
from LilyAiTool.service import ToolContextData, ToolService, ToolSpec
from LilyAiWeb.service import WebService

log = get_logger("bootstrap")


@dataclass
class App:
    settings: Settings
    pool: ModelPool
    db: Database
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
    started_at: float

    async def aclose(self) -> None:
        await self.scheduler.stop()
        await self.provider.aclose()
        self.db.close()


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


def build_app(
    settings: Settings,
    provider: LLMProvider | None = None,
    search_provider: SearchProvider | None = None,
    db: Database | None = None,
) -> App:
    pool = ModelPool()
    db = db or Database(settings.db_path)

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
    tools = ToolService(notifier_box)
    for spec in _web_tools(web):
        tools.register(spec)

    chat = ChatWorkflow(settings, provider, memory, rag, tools, ContextBuilder(settings.token_budget), learning)
    replies, bus = ReplyLog(), EventBus()
    forms, polls = FormManager(), PollManager()
    router = DMRouter(
        memory, chat, replies, bus, SessionManager(), RateLimiter(), AccessControl(settings.allowed_user_ids),
        forms, polls, OnboardingFlow(memory, forms, polls),
    )
    scheduler = Scheduler()
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
    return App(
        settings, pool, db, provider, memory, rag, web, tools, learning, chat, router,
        FeedbackHandler(replies, learning, rag), bus, DiscordEventHandlers(bus), scanner, scheduler,
        notifier_box, time.time(),
    )
