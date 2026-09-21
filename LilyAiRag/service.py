"""Facade for the RAG domain: ingest -> chunk -> embed -> store -> retrieve."""
from pathlib import Path

from LilyAiRag.Chunking.chunker import chunk_document
from LilyAiRag.Document.loader import load_directory, load_file, make_document
from LilyAiRag.Embedding.embedder import Embedder, HashingEmbedder
from LilyAiRag.Models.rag_models import Document, ScoredChunk
from LilyAiRag.Retrieval.retriever import Retriever
from LilyAiRag.VectorStore.store import InMemoryVectorStore


class RagService:
    def __init__(self, index_path: str | Path | None = None, embedder: Embedder | None = None):
        self.embedder = embedder or HashingEmbedder()
        self.store = InMemoryVectorStore(index_path)
        self.store.load()
        self.retriever = Retriever(self.embedder, self.store)

    def ingest_document(self, doc: Document) -> int:
        if not doc.text or self.store.has_doc(doc.id):
            return 0
        chunks = chunk_document(doc)
        self.store.add(chunks, self.embedder.embed_many([c.text for c in chunks]))
        return len(chunks)

    def ingest_text(self, source: str, text: str) -> int:
        n = self.ingest_document(make_document(source, text))
        if n:
            self.store.save()
        return n

    def ingest_path(self, path: str | Path) -> int:
        p = Path(path)
        docs = load_directory(p) if p.is_dir() else [load_file(p)]
        n = sum(self.ingest_document(d) for d in docs)
        if n:
            self.store.save()
        return n

    def retrieve(self, query: str, k: int = 4) -> list[ScoredChunk]:
        return self.retriever.retrieve(query, k)

    def delete_source(self, source: str) -> int:
        n = self.store.delete_source(source)
        self.store.save()
        return n

    def stats(self) -> dict:
        return {"chunks": len(self.store), "sources": self.store.sources()}
