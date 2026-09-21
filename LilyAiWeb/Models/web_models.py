from dataclasses import dataclass


@dataclass
class SearchResult:
    title: str
    url: str
    snippet: str
    domain: str = ""
    score: float = 0.0


@dataclass
class WebDocument:
    url: str
    title: str
    text: str
    domain: str = ""

    def as_snippet(self, max_chars: int = 900) -> str:
        body = self.text[:max_chars].strip()
        return f"{self.title} ({self.domain}) - {self.url}\n{body}"
