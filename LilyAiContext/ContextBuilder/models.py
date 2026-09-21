from dataclasses import dataclass, field
from typing import Any


@dataclass
class HistoryMessage:
    role: str
    content: str


@dataclass
class ContextInput:
    """Everything the Context domain needs. Gathered by the caller so Context stays decoupled."""

    user_message: str
    user_id: str = ""
    display_name: str = ""
    history: list[HistoryMessage] = field(default_factory=list)
    user_facts: list[str] = field(default_factory=list)
    knowledge_snippets: list[str] = field(default_factory=list)
    web_snippets: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    tool_schemas: list[dict[str, Any]] = field(default_factory=list)


@dataclass
class BuiltContext:
    messages: list[dict[str, Any]]
    tools: list[dict[str, Any]]
    token_estimate: int
    dropped_history: int = 0
    sections: dict[str, int] = field(default_factory=dict)
