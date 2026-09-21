from LilyAiCore.ExternalServices.Search.base import SearchProvider
from LilyAiWeb.Models.web_models import SearchResult


async def run_search(provider: SearchProvider, query: str, limit: int) -> list[SearchResult]:
    hits = await provider.search(query, limit=limit)
    return [SearchResult(h.title, h.url, h.snippet) for h in hits]
