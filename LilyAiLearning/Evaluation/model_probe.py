"""Probe a candidate model before it joins the pool, and decide whether it is a chat model at all."""
import asyncio
import re
import time
from dataclasses import dataclass, field
from typing import Any

from LilyAiCore.Exceptions.errors import ProviderError, RateLimitError
from LilyAiCore.Providers.base import LLMProvider

_NOT_CHAT = re.compile(r"whisper|tts|orpheus|playai|guard|safeguard|embed|rerank|moderation|transcri|speech", re.I)

_TOOL = {
    "type": "function",
    "function": {
        "name": "calculate",
        "description": "Evaluate an arithmetic expression exactly.",
        "parameters": {"type": "object", "properties": {"expression": {"type": "string"}}, "required": ["expression"]},
    },
}


def classify(info: dict[str, Any]) -> tuple[str, str]:
    """Return (kind, reason). kind: chat | agent | excluded | inactive."""
    mid = info.get("id", "")
    if info.get("active") is False:
        return "inactive", "reported inactive by Groq"
    if _NOT_CHAT.search(mid):
        return "excluded", "not a general chat model (speech, guard, embedding or similar)"
    if mid.startswith("groq/compound"):
        return "agent", "agent system; register manually if wanted"
    return "chat", ""


@dataclass
class ProbeResult:
    status: str  # passed | failed | deferred
    tools: bool = False
    latency_ms: int = 0
    checks: dict[str, bool] = field(default_factory=dict)
    error: str = ""

    def to_dict(self) -> dict:
        return {"status": self.status, "tools": self.tools, "latency_ms": self.latency_ms, "checks": self.checks, "error": self.error}


async def probe_model(provider: LLMProvider, model_id: str, timeout: float = 45.0) -> ProbeResult:
    """Three cheap calls against the exact model (no fallback): plain reply, exact arithmetic, tool calling.

    Passing needs the first two. Tool support is recorded, not required. A rate limit defers the model
    to the next scan instead of rejecting it.
    """
    checks: dict[str, bool] = {}
    start = time.perf_counter()
    try:
        r = await asyncio.wait_for(
            provider.chat(
                [{"role": "user", "content": "What is 17 * 23? Reply with only the number."}],
                model=model_id, temperature=0.0, max_tokens=600, fallback=False,
            ),
            timeout,
        )
        latency = int((time.perf_counter() - start) * 1000)
        checks["responds"] = bool(r.content.strip())
        checks["arithmetic"] = "391" in r.content

        try:
            t = await asyncio.wait_for(
                provider.chat(
                    [{"role": "user", "content": "Use the calculate tool to compute 1234 * 5678."}],
                    model=model_id, tools=[_TOOL], temperature=0.0, max_tokens=600, fallback=False,
                ),
                timeout,
            )
            checks["tool_call"] = any(c.name == "calculate" for c in t.tool_calls)
        except RateLimitError:
            raise
        except (ProviderError, asyncio.TimeoutError):
            checks["tool_call"] = False
    except RateLimitError:
        return ProbeResult("deferred", error="rate limited")
    except asyncio.TimeoutError:
        return ProbeResult("failed", error=f"timed out after {timeout:.0f}s", checks=checks)
    except ProviderError as e:
        return ProbeResult("failed", error=str(e)[:200], checks=checks)

    ok = checks["responds"] and checks["arithmetic"]
    return ProbeResult("passed" if ok else "failed", tools=checks.get("tool_call", False), latency_ms=latency, checks=checks,
                       error="" if ok else "did not answer the arithmetic check")
