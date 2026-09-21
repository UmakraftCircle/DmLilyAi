"""Source processing: normalise, dedupe, block unsafe hosts, rank."""
import ipaddress
from urllib.parse import urlparse

from LilyAiWeb.Models.web_models import SearchResult

_BLOCKED_HOST_PARTS = ("localhost", ".local", ".internal")


def domain_of(url: str) -> str:
    host = (urlparse(url).hostname or "").lower()
    return host[4:] if host.startswith("www.") else host


def is_safe_url(url: str) -> bool:
    """Block non-http(s) and private-network targets (SSRF guard for the extractor)."""
    p = urlparse(url)
    if p.scheme not in {"http", "https"} or not p.hostname:
        return False
    host = p.hostname.lower()
    if any(part in host for part in _BLOCKED_HOST_PARTS):
        return False
    try:
        ip = ipaddress.ip_address(host)
        return not (ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved)
    except ValueError:
        return True


def process_results(results: list[SearchResult], preferred: dict[str, float] | None = None) -> list[SearchResult]:
    preferred = preferred or {}
    seen: set[str] = set()
    out: list[SearchResult] = []
    for i, r in enumerate(results):
        if not is_safe_url(r.url):
            continue
        r.domain = domain_of(r.url)
        key = r.url.split("#")[0].rstrip("/")
        if key in seen:
            continue
        seen.add(key)
        r.score = 1.0 / (i + 1) + preferred.get(r.domain, 0.0)
        out.append(r)
    out.sort(key=lambda r: -r.score)
    return out
