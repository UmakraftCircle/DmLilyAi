"""Tavily Search API - LLM-oriented web search. Requires TAVILY_API_KEY.

Preferred over DuckDuckGoSearch (see duckduckgo.py) when a key is configured: Tavily is a real
API built for this use case, rather than scraping an HTML results page that can change shape or
start blocking the request out from under us at any time (see the uma.moe extractor lesson -
same class of problem). See bootstrap.py's build_app() for the selection logic.

Supports multiple comma-separated keys (TAVILY_API_KEY=key_a,key_b,key_c) via the same
KeyRotator used for GROQ_API_KEY: keys are drawn from a shuffled bag so load spreads evenly
across them, and a key that comes back rate-limited (429) is put on cooldown so the next
call automatically picks a different one instead of retrying the same key.
"""
import httpx

from LilyAiCore.Exceptions.errors import WebError
from LilyAiCore.Providers.Groq.key_rotator import KeyRotator
from .base import RawSearchHit, SearchProvider

_URL = "https://api.tavily.com/search"


class TavilySearch(SearchProvider):
    def __init__(self, api_keys: list[str] | str, max_retries: int = 2):
        keys = [api_keys] if isinstance(api_keys, str) else list(api_keys)
        if not keys:
            raise ValueError("TavilySearch needs at least one API key")
        self._rotator = KeyRotator(keys)
        self._max_retries = max_retries

    async def search(self, query: str, limit: int = 5) -> list[RawSearchHit]:
        tried: set[str] = set()  # keys already rate-limited within this call
        last_err: Exception | None = None
        for attempt in range(self._max_retries + 1):
            key = await self._rotator.next(exclude=tried)
            payload = {
                "api_key": key,
                "query": query,
                "max_results": limit,
                "search_depth": "basic",
            }
            try:
                async with httpx.AsyncClient(timeout=15) as http:
                    r = await http.post(_URL, json=payload)
            except httpx.HTTPError as e:
                last_err = WebError(f"search failed: {e}")
                if attempt == self._max_retries:
                    raise last_err from e
                continue
            if r.status_code == 429:
                retry = float(r.headers.get("retry-after", "0") or 0)
                await self._rotator.mark_rate_limited(key, retry)
                tried.add(key)
                last_err = WebError(f"search failed: HTTP 429 (rate-limited, {len(tried)}/{self._rotator.key_count} keys tried)")
                if attempt == self._max_retries:
                    raise last_err
                continue  # retry immediately with a different key
            if r.status_code != 200:
                raise WebError(f"search failed: HTTP {r.status_code}")
            data = r.json()
            hits = [
                RawSearchHit(item.get("title", ""), item.get("url", ""), item.get("content", ""))
                for item in data.get("results", [])
            ]
            return hits[:limit]
        raise last_err or WebError("search failed: exhausted retries")
