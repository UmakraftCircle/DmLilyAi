from dataclasses import dataclass, field
from typing import Any, Awaitable, Callable


@dataclass
class ToolContextData:
    """Who/where a tool is being run for. Passed to every tool handler."""

    user_id: str = ""
    display_name: str = ""
    extra: dict[str, Any] = field(default_factory=dict)


ToolHandler = Callable[[ToolContextData, dict[str, Any]], Awaitable[str] | str]


@dataclass
class ToolSpec:
    name: str
    description: str
    parameters: dict[str, Any]
    handler: ToolHandler
    category: str = "utility"
    timeout: float = 20.0

    def schema(self) -> dict[str, Any]:
        return {
            "type": "function",
            "function": {"name": self.name, "description": self.description, "parameters": self.parameters},
        }


@dataclass
class ToolResult:
    name: str
    ok: bool
    output: str
    duration_ms: float = 0.0
