import hashlib
from pathlib import Path

from LilyAiRag.Models.rag_models import Document

TEXT_SUFFIXES = {".txt", ".md", ".markdown", ".rst", ".csv", ".json"}


def make_document(source: str, text: str, metadata: dict | None = None) -> Document:
    doc_id = hashlib.sha1(f"{source}\n{text}".encode("utf-8")).hexdigest()[:16]
    return Document(doc_id, source, text.strip(), metadata or {})


def load_file(path: str | Path) -> Document:
    p = Path(path)
    return make_document(p.name, p.read_text(encoding="utf-8", errors="ignore"), {"path": str(p)})


def load_directory(path: str | Path) -> list[Document]:
    root = Path(path)
    return [load_file(f) for f in sorted(root.rglob("*")) if f.is_file() and f.suffix.lower() in TEXT_SUFFIXES]
