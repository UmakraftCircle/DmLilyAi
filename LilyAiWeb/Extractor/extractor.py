"""Fetch a page and extract readable text."""
import re

import httpx

from LilyAiCore.Exceptions.errors import WebError
from LilyAiWeb.Models.web_models import WebDocument
from LilyAiWeb.Sources.sources import domain_of, is_safe_url

_UA = "Mozilla/5.0 (compatible; LilyAi/1.0)"
MAX_BYTES = 1_500_000


def html_to_text(html: str) -> tuple[str, str]:
    """Return (title, text). Uses BeautifulSoup when installed, regex otherwise."""
    try:
        from bs4 import BeautifulSoup

        soup = BeautifulSoup(html, "html.parser")
        title = (soup.title.string or "").strip() if soup.title and soup.title.string else ""
        for tag in soup(["script", "style", "nav", "footer", "header", "aside", "form", "noscript", "svg"]):
            tag.decompose()
        node = soup.find("article") or soup.find("main") or soup.body or soup
        text = node.get_text("\n")
    except ImportError:
        m = re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I)
        title = m.group(1).strip() if m else ""
        text = re.sub(r"(?is)<(script|style|nav|footer|header|aside)[^>]*>.*?</\1>", " ", html)
        text = re.sub(r"<[^>]+>", "\n", text)
    lines = [re.sub(r"\s+", " ", ln).strip() for ln in text.splitlines()]
    return title, "\n".join(ln for ln in lines if len(ln) > 30 or (ln and len(ln.split()) > 4))


async def fetch_document(url: str, max_chars: int = 6000) -> WebDocument:
    if not is_safe_url(url):
        raise WebError("URL not allowed")
    try:
        async with httpx.AsyncClient(timeout=15, headers={"User-Agent": _UA}, follow_redirects=True) as http:
            r = await http.get(url)
    except httpx.HTTPError as e:
        raise WebError(f"fetch failed: {e}") from e
    if r.status_code != 200:
        raise WebError(f"fetch failed: HTTP {r.status_code}")
    if "html" not in r.headers.get("content-type", "html"):
        raise WebError("not an HTML page")
    if not is_safe_url(str(r.url)):
        raise WebError("redirected to a disallowed URL")
    title, text = html_to_text(r.text[:MAX_BYTES])
    return WebDocument(url=str(r.url), title=title or domain_of(url), text=text[:max_chars], domain=domain_of(str(r.url)))
