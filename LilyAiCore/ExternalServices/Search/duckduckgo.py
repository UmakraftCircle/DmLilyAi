"""Keyless default search provider (DuckDuckGo HTML endpoint). Swap for any SearchProvider."""
import html as _html
import re
from urllib.parse import parse_qs, unquote, urlparse

import httpx

from LilyAiCore.Exceptions.errors import WebError
from .base import RawSearchHit, SearchProvider

_UA = "Mozilla/5.0 (compatible; LilyAi/1.0)"
_RESULT = re.compile(
    r'<a[^>]+class="result__a"[^>]+href="(?P<url>[^"]+)"[^>]*>(?P<title>.*?)</a>.*?'
    r'class="result__snippet"[^>]*>(?P<snippet>.*?)</a>',
    re.S,
)
_TAGS = re.compile(r"<[^>]+>")


def _clean(fragment: str) -> str:
    return _html.unescape(_TAGS.sub("", fragment)).strip()


def _real_url(href: str) -> str:
    if href.startswith("//"):
        href = "https:" + href
    parsed = urlparse(href)
    if "duckduckgo.com" in parsed.netloc and parsed.path.startswith("/l/"):
        return unquote(parse_qs(parsed.query).get("uddg", [""])[0])
    return href


class DuckDuckGoSearch(SearchProvider):
    async def search(self, query: str, limit: int = 5) -> list[RawSearchHit]:
        try:
            async with httpx.AsyncClient(timeout=15, headers={"User-Agent": _UA}, follow_redirects=True) as http:
                r = await http.post("https://html.duckduckgo.com/html/", data={"q": query})
        except httpx.HTTPError as e:
            raise WebError(f"search failed: {e}") from e
        if r.status_code != 200:
            raise WebError(f"search failed: HTTP {r.status_code}")
        hits: list[RawSearchHit] = []
        for m in _RESULT.finditer(r.text):
            url = _real_url(m.group("url"))
            if url.startswith("http"):
                hits.append(RawSearchHit(_clean(m.group("title")), url, _clean(m.group("snippet"))))
            if len(hits) >= limit:
                break
        return hits
