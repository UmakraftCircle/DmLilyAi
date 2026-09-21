"""Keyword-overlap retrieval over user facts and knowledge notes (fast, no embeddings)."""
from LilyAiCore.Helpers.text import tokenize

_STOP = frozenset(
    "the a an and or of to in on for with is are was were be i you it my me your this that at as by from do does did "
    "what how when where why can could should would will about".split()
)


def _terms(text: str) -> set[str]:
    return {t for t in tokenize(text) if t not in _STOP and len(t) > 1}


def rank_by_overlap(query: str, items: list[str], limit: int = 5, min_score: float = 0.0) -> list[str]:
    q = _terms(query)
    if not q:
        return []
    scored = []
    for item in items:
        t = _terms(item)
        if not t:
            continue
        score = len(q & t) / (len(q) ** 0.5 * len(t) ** 0.5)
        if score > min_score:
            scored.append((score, item))
    scored.sort(key=lambda x: -x[0])
    return [i for _, i in scored[:limit]]
