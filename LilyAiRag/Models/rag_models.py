from dataclasses import dataclass, field


@dataclass
class Document:
    id: str
    source: str
    text: str
    metadata: dict = field(default_factory=dict)


@dataclass
class Chunk:
    id: str
    doc_id: str
    source: str
    index: int
    text: str


@dataclass
class ScoredChunk:
    chunk: Chunk
    score: float

    def as_snippet(self, max_chars: int = 700) -> str:
        return f"{self.chunk.source}: {self.chunk.text[:max_chars]}"
