from LilyAiTool.DiscordTools import discord_tools
from LilyAiTool.Executor import ToolExecutor
from LilyAiTool.Models import ToolContextData, ToolResult, ToolSpec  # noqa: F401
from LilyAiTool.Registry import ToolRegistry
from LilyAiTool.UtilityTools import utility_tools


class ToolService:
    def __init__(self):
        self.registry = ToolRegistry()
        self.executor = ToolExecutor(self.registry)
        for spec in [*utility_tools(), *discord_tools()]:
            self.registry.register(spec)

    def register(self, spec: ToolSpec) -> None:
        self.registry.register(spec)

    def schemas(self) -> list[dict]:
        return self.registry.schemas()

    async def run(self, name: str, arguments: dict, ctx: ToolContextData) -> ToolResult:
        return await self.executor.execute(name, arguments, ctx)
