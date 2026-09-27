"""Tavily Search API - LLM-oriented web search. Requires TAVILY_API_KEY.

Preferred over DuckDuckGoSearch (see duckduckgo.py) when a key is configured: Tavily is a real
API built for this use case, rather than scraping an HTML results page that can change shape or
start blocking the request out from under us at any time (see the uma.moe extractor lesson -
same class of problem). See bootstrap.py's build_app() for the selection logic.
"""
import httpx

from LilyAiCore.Exceptions.errors import WebError
from .base import RawSearchHit, SearchProvider

_URL = "https://api.tavily.com/search"


class TavilySearch(SearchProvider):
    def __init__(self, api_key: str):
        self._api_key = api_key

    async def search(self, query: str, limit: int = 5) -> list[RawSearchHit]:
        payload = {
            "api_key": self._api_key,
            "query": query,
            "max_results": limit,
            "search_depth": "basic",
        }
        try:
            async with httpx.AsyncClient(timeout=15) as http:
                r = await http.post(_URL, json=payload)
        except httpx.HTTPError as e:
            raise WebError(f"search failed: {e}") from e
        if r.status_code != 200:
            raise WebError(f"search failed: HTTP {r.status_code}")
        data = r.json()
        hits = [
            RawSearchHit(item.get("title", ""), item.get("url", ""), item.get("content", ""))
            for item in data.get("results", [])
        ]
        return hits[:limit]
