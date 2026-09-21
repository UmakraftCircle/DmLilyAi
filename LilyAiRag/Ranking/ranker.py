"""Rerank: blend vector score with keyword coverage, then drop near-duplicates."""
from LilyAiCore.Helpers.text import tokenize
from LilyAiRag.Models.rag_models import ScoredChunk


def _coverage(query_terms: set[str], text: str) -> float:
    if not query_terms:
        return 0.0
    return len(query_terms & set(tokenize(text))) / len(query_terms)


def rerank(query: str, hits: list[ScoredChunk], k: int = 4, keyword_weight: float = 0.35) -> list[ScoredChunk]:
    q = {t for t in tokenize(query) if len(t) > 2}
    rescored = [ScoredChunk(h.chunk, (1 - keyword_weight) * h.score + keyword_weight * _coverage(q, h.chunk.text)) for h in hits]
    rescored.sort(key=lambda s: -s.score)
    picked: list[ScoredChunk] = []
    for h in rescored:
        words = set(tokenize(h.chunk.text))
        if any(len(words & set(tokenize(p.chunk.text))) / max(1, len(words)) > 0.85 for p in picked):
            continue
        picked.append(h)
        if len(picked) >= k:
            break
    return picked
