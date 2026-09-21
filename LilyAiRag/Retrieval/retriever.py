from LilyAiRag.Embedding.embedder import Embedder
from LilyAiRag.Models.rag_models import ScoredChunk
from LilyAiRag.Ranking.ranker import rerank
from LilyAiRag.VectorStore.store import InMemoryVectorStore


class Retriever:
    def __init__(self, embedder: Embedder, store: InMemoryVectorStore, min_score: float = 0.12):
        self.embedder, self.store, self.min_score = embedder, store, min_score

    def retrieve(self, query: str, k: int = 4) -> list[ScoredChunk]:
        if len(self.store) == 0 or not query.strip():
            return []
        candidates = self.store.search(self.embedder.embed(query), k=k * 4)
        return [h for h in rerank(query, candidates, k=k) if h.score >= self.min_score]
