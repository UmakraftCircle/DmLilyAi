from LilyAiCore.Exceptions.errors import ToolError
from LilyAiTool.Models.tool_models import ToolSpec


class ToolRegistry:
    def __init__(self):
        self._tools: dict[str, ToolSpec] = {}

    def register(self, spec: ToolSpec) -> None:
        self._tools[spec.name] = spec

    def get(self, name: str) -> ToolSpec:
        if name not in self._tools:
            raise ToolError(f"Unknown tool: {name}")
        return self._tools[name]

    def names(self) -> list[str]:
        return sorted(self._tools)

    def schemas(self, categories: set[str] | None = None) -> list[dict]:
        return [t.schema() for t in self._tools.values() if categories is None or t.category in categories]
