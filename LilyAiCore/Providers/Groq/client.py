"""Groq chat provider (OpenAI-compatible endpoint). Pure transport: no business logic."""
import asyncio
import json
from typing import Any

import httpx

from LilyAiCore.Config.models import ModelPool
from LilyAiCore.Exceptions.errors import ConfigError, ProviderError, RateLimitError
from LilyAiCore.Logging.logger import get_logger
from LilyAiCore.Providers.base import LLMProvider, LLMResponse, ToolCallRequest

log = get_logger("provider.groq")


class GroqProvider(LLMProvider):
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.groq.com/openai/v1",
        default_model: str = "openai/gpt-oss-20b",
        pool: ModelPool | None = None,
        timeout: float = 60.0,
        max_retries: int = 2,
    ):
        if not api_key:
            raise ConfigError("GROQ_API_KEY is not set")
        self.default_model = default_model
        self.pool = pool or ModelPool()
        self.max_retries = max_retries
        self._http = httpx.AsyncClient(
            base_url=base_url.rstrip("/"),
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=timeout,
        )

    async def aclose(self) -> None:
        await self._http.aclose()

    async def describe_models(self) -> list[dict[str, Any]]:
        r = await self._http.get("/models")
        if r.status_code != 200:
            raise ProviderError(f"Groq /models failed: {r.status_code} {r.text[:200]}")
        return sorted(r.json().get("data", []), key=lambda m: m.get("id", ""))

    async def list_models(self) -> list[str]:
        return [m["id"] for m in await self.describe_models()]

    async def chat(self, messages, *, model=None, tools=None, temperature=0.6, max_tokens=None, json_mode=False, fallback=True):
        primary = model or self.default_model
        if not fallback:  # exact model only (used by model probes)
            return await self._call(primary, messages, tools, temperature, max_tokens, json_mode)
        candidates = [primary] + self.pool.fallbacks(primary, need_tools=bool(tools))
        last_err: Exception | None = None
        for candidate in candidates:
            try:
                return await self._call(candidate, messages, tools, temperature, max_tokens, json_mode)
            except ProviderError as e:  # includes RateLimitError
                log.warning("model %s failed: %s", candidate, e)
                last_err = e
        raise ProviderError(f"All models failed: {last_err}")

    async def _call(self, model, messages, tools, temperature, max_tokens, json_mode) -> LLMResponse:
        body: dict[str, Any] = {"model": model, "messages": messages, "temperature": temperature}
        if max_tokens:
            body["max_completion_tokens"] = max_tokens
        if tools:
            body["tools"] = tools
            body["tool_choice"] = "auto"
        if json_mode:
            body["response_format"] = {"type": "json_object"}

        for attempt in range(self.max_retries + 1):
            try:
                r = await self._http.post("/chat/completions", json=body)
            except httpx.HTTPError as e:
                if attempt == self.max_retries:
                    raise ProviderError(f"network error: {e}") from e
                await asyncio.sleep(1.5 * (attempt + 1))
                continue
            if r.status_code == 429:
                retry = float(r.headers.get("retry-after", "0") or 0)
                if attempt == self.max_retries or retry > 8:
                    raise RateLimitError(retry_after=retry)
                await asyncio.sleep(max(retry, 1.0))
                continue
            if r.status_code >= 500 and attempt < self.max_retries:
                await asyncio.sleep(1.5 * (attempt + 1))
                continue
            if r.status_code != 200:
                raise ProviderError(f"{r.status_code}: {r.text[:300]}")
            return self._parse(r.json(), model)
        raise ProviderError("exhausted retries")

    @staticmethod
    def _parse(data: dict, model: str) -> LLMResponse:
        msg = data["choices"][0]["message"]
        calls: list[ToolCallRequest] = []
        for tc in msg.get("tool_calls") or []:
            try:
                args = json.loads(tc["function"].get("arguments") or "{}")
            except json.JSONDecodeError:
                args = {}
            calls.append(ToolCallRequest(id=tc["id"], name=tc["function"]["name"], arguments=args))
        raw: dict[str, Any] = {"role": "assistant", "content": msg.get("content") or ""}
        if msg.get("tool_calls"):
            raw["tool_calls"] = msg["tool_calls"]
        return LLMResponse(
            content=(msg.get("content") or "").strip(),
            tool_calls=calls,
            model=data.get("model", model),
            usage=data.get("usage", {}),
            raw_message=raw,
        )
