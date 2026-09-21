"""Paragraph-aware chunking with character overlap."""
from LilyAiRag.Models.rag_models import Chunk, Document


def chunk_text(text: str, size: int = 800, overlap: int = 120) -> list[str]:
    paragraphs = [p.strip() for p in text.replace("\r\n", "\n").split("\n\n") if p.strip()]
    chunks: list[str] = []
    current = ""
    for para in paragraphs:
        while len(para) > size:  # hard-split very long paragraphs
            cut = para.rfind(" ", 0, size)
            cut = cut if cut > size // 2 else size
            if current:
                chunks.append(current)
                current = ""
            chunks.append(para[:cut].strip())
            para = para[max(0, cut - overlap):].strip()
            if len(para) <= overlap:
                para = ""
        if not para:
            continue
        if current and len(current) + len(para) + 2 > size:
            chunks.append(current)
            tail = current[-overlap:] if overlap else ""
            current = (tail + "\n\n" + para).strip() if tail else para
        else:
            current = f"{current}\n\n{para}".strip() if current else para
    if current:
        chunks.append(current)
    return chunks


def chunk_document(doc: Document, size: int = 800, overlap: int = 120) -> list[Chunk]:
    return [
        Chunk(f"{doc.id}:{i}", doc.id, doc.source, i, t) for i, t in enumerate(chunk_text(doc.text, size, overlap))
    ]
