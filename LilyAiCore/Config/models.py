"""Free-tier Groq model pool. LilyAi only uses free-tier models."""
from dataclasses import dataclass

from LilyAiCore.Constants.constants import ROLE_AGENT, ROLE_ALTERNATE, ROLE_CHAT, ROLE_REASONING


@dataclass(frozen=True)
class ModelSpec:
    id: str
    role: str
    supports_tools: bool = True
    note: str = ""


DEFAULT_POOL: tuple[ModelSpec, ...] = (
    ModelSpec("openai/gpt-oss-20b", ROLE_CHAT, True, "Fast, high-volume chat"),
    ModelSpec("openai/gpt-oss-120b", ROLE_REASONING, True, "Strongest general-purpose"),
    ModelSpec("qwen/qwen3.6-27b", ROLE_ALTERNATE, True, "General alternative"),
    ModelSpec("groq/compound-mini", ROLE_AGENT, False, "Agent / tool workflows (server-side tools)"),
)


class ModelPool:
    def __init__(self, models: tuple[ModelSpec, ...] = DEFAULT_POOL):
        self._models = list(models)

    def all(self) -> list[ModelSpec]:
        return list(self._models)

    def for_role(self, role: str) -> ModelSpec:
        for m in self._models:
            if m.role == role:
                return m
        return self._models[0]

    def fallbacks(self, primary_id: str, need_tools: bool = False) -> list[str]:
        """Chat fallbacks. Agent-role models are excluded: they're for dedicated workflows."""
        return [
            m.id
            for m in self._models
            if m.id != primary_id and m.role != ROLE_AGENT and (m.supports_tools or not need_tools)
        ]

    def ids(self) -> list[str]:
        return [m.id for m in self._models]

    def has(self, model_id: str) -> bool:
        return any(m.id == model_id for m in self._models)

    def add(self, spec: ModelSpec) -> None:
        if not self.has(spec.id):
            self._models.append(spec)

    def remove(self, model_id: str) -> bool:
        before = len(self._models)
        self._models = [m for m in self._models if m.id != model_id]
        return len(self._models) < before
