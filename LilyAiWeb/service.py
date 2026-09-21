"""Facade for the Web domain: search -> process -> extract."""
import asyncio

from LilyAiCore.ExternalServices.Search.base import SearchProvider
from LilyAiCore.Exceptions.errors import WebError
from LilyAiCore.Logging.logger import get_logger
from LilyAiWeb.Cache.ttl_cache import TTLCache
from LilyAiWeb.Extractor.extractor import fetch_document
from LilyAiWeb.Models.web_models import SearchResult, WebDocument
from LilyAiWeb.Search.search import run_search
from LilyAiWeb.Sources.sources import process_results

log = get_logger("web")


class WebService:
    def __init__(self, provider: SearchProvider, preferred_domains: dict[str, float] | None = None):
        self.provider = provider
        self.preferred = preferred_domains or {}
        self._search_cache = TTLCache(ttl=900)
        self._doc_cache = TTLCache(ttl=1800)

    async def search(self, query: str, limit: int = 5) -> list[SearchResult]:
        key = f"{query.lower().strip()}|{limit}"
        cached = self._search_cache.get(key)
        if cached is not None:
            return cached
        results = process_results(await run_search(self.provider, query, limit * 2), self.preferred)[:limit]
        self._search_cache.set(key, results)
        return results

    async def read(self, url: str, max_chars: int = 6000) -> WebDocument:
        cached = self._doc_cache.get(url)
        if cached is not None:
            return cached
        doc = await fetch_document(url, max_chars)
        self._doc_cache.set(url, doc)
        return doc

    async def research(self, query: str, limit: int = 3, read_top: int = 2) -> list[WebDocument]:
        """Search, then read the top pages; fall back to the search snippet if a page can't be read."""
        results = await self.search(query, limit)

        async def load(r: SearchResult) -> WebDocument:
            try:
                return await self.read(r.url, 3000)
            except WebError as e:
                log.info("read failed %s: %s", r.url, e)
                return WebDocument(r.url, r.title, r.snippet, r.domain)

        top = await asyncio.gather(*(load(r) for r in results[:read_top]))
        rest = [WebDocument(r.url, r.title, r.snippet, r.domain) for r in results[read_top:]]
        return [*top, *rest]
