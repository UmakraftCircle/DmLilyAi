"""Provider-agnostic LLM interface. Domains depend on this, never on Groq directly."""
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


@dataclass
class ToolCallRequest:
    id: str
    name: str
    arguments: dict[str, Any]


@dataclass
class LLMResponse:
    content: str
    tool_calls: list[ToolCallRequest] = field(default_factory=list)
    model: str = ""
    usage: dict[str, int] = field(default_factory=dict)
    raw_message: dict[str, Any] = field(default_factory=dict)


class LLMProvider(ABC):
    @abstractmethod
    async def chat(
        self,
        messages: list[dict[str, Any]],
        *,
        model: str | None = None,
        tools: list[dict[str, Any]] | None = None,
        temperature: float = 0.6,
        max_tokens: int | None = None,
        json_mode: bool = False,
        fallback: bool = True,
    ) -> LLMResponse: ...

    @abstractmethod
    async def list_models(self) -> list[str]: ...

    async def describe_models(self) -> list[dict[str, Any]]:
        """Model metadata (id plus whatever the provider reports). Default: ids only."""
        return [{"id": m} for m in await self.list_models()]

    async def aclose(self) -> None:
        return None
