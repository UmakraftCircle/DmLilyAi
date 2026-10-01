from LilyAiCore.ExternalServices.Discord.notifier import NotifierBox
from LilyAiCore.Logging.logger import get_logger
from LilyAiGameSpace.UmamusumeGameSpaceEngine import get_engine
from LilyAiTool.DiscordTools import discord_tools
from LilyAiTool.Executor import ToolExecutor
from LilyAiTool.GameSpaceTools import game_space_tools
from LilyAiTool.Models import ToolContextData, ToolResult, ToolSpec  # noqa: F401
from LilyAiTool.Registry import ToolRegistry
from LilyAiTool.UtilityTools import utility_tools

log = get_logger("tool.service")


class ToolService:
    def __init__(self, notifier_box: NotifierBox | None = None):
        self.registry = ToolRegistry()
        self.executor = ToolExecutor(self.registry)
        self.notifier_box = notifier_box or NotifierBox()
        for spec in [*utility_tools(), *discord_tools(self.notifier_box), *game_space_tools()]:
            self.registry.register(spec)

    def register(self, spec: ToolSpec) -> None:
        self.registry.register(spec)

    def schemas(self) -> list[dict]:
        return self.registry.schemas()

    def game_context(self, text: str) -> list[str]:
        """Game-doc snippets for a chat message that names a known Umamusume doc, else [].

        No model call: a plain lookup, so the chat model can answer from the docs without first
        having to decide to call a tool. Never raises - a docs problem must not break a chat turn.
        """
        try:
            return get_engine().context_for(text)
        except Exception:
            log.exception("game docs context lookup failed")
            return []

    async def run(self, name: str, arguments: dict, ctx: ToolContextData) -> ToolResult:
        return await self.executor.execute(name, arguments, ctx)
