import json
from pathlib import Path

from LilyAiRag.Models.rag_models import Chunk, ScoredChunk


class InMemoryVectorStore:
    """Cosine search over normalised vectors, persisted as JSON."""

    def __init__(self, path: str | Path | None = None):
        self.path = Path(path) if path else None
        self._chunks: dict[str, Chunk] = {}
        self._vectors: dict[str, list[float]] = {}

    def add(self, chunks: list[Chunk], vectors: list[list[float]]) -> None:
        for c, v in zip(chunks, vectors):
            self._chunks[c.id] = c
            self._vectors[c.id] = v

    def search(self, query_vec: list[float], k: int = 5) -> list[ScoredChunk]:
        scored = [
            ScoredChunk(self._chunks[cid], sum(a * b for a, b in zip(query_vec, vec)))
            for cid, vec in self._vectors.items()
        ]
        scored.sort(key=lambda s: -s.score)
        return scored[:k]

    def has_doc(self, doc_id: str) -> bool:
        return any(c.doc_id == doc_id for c in self._chunks.values())

    def delete_source(self, source: str) -> int:
        ids = [cid for cid, c in self._chunks.items() if c.source == source]
        for cid in ids:
            self._chunks.pop(cid, None)
            self._vectors.pop(cid, None)
        return len(ids)

    def sources(self) -> dict[str, int]:
        out: dict[str, int] = {}
        for c in self._chunks.values():
            out[c.source] = out.get(c.source, 0) + 1
        return out

    def __len__(self) -> int:
        return len(self._chunks)

    def save(self) -> None:
        if not self.path:
            return
        payload = [
            {"chunk": vars(self._chunks[cid]), "vec": [round(x, 5) for x in self._vectors[cid]]}
            for cid in self._chunks
        ]
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(json.dumps(payload), encoding="utf-8")
        tmp.replace(self.path)

    def load(self) -> None:
        if not self.path or not self.path.exists():
            return
        for row in json.loads(self.path.read_text(encoding="utf-8")):
            c = Chunk(**row["chunk"])
            self._chunks[c.id] = c
            self._vectors[c.id] = row["vec"]
