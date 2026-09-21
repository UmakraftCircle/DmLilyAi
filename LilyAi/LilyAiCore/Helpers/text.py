import re


def estimate_tokens(text: str) -> int:
    """Cheap token estimate (~4 chars/token). Good enough for budgeting."""
    return max(1, len(text) // 4)


def truncate(text: str, limit: int, suffix: str = "...") -> str:
    return text if len(text) <= limit else text[: max(0, limit - len(suffix))] + suffix


def chunk_for_discord(text: str, limit: int = 2000) -> list[str]:
    """Split text into <=limit pieces, preferring paragraph, then line, then space boundaries."""
    text = text.strip()
    if not text:
        return []
    parts: list[str] = []
    while len(text) > limit:
        cut = max(text.rfind("\n\n", 0, limit), text.rfind("\n", 0, limit), text.rfind(" ", 0, limit))
        if cut < limit // 2:
            cut = limit
        parts.append(text[:cut].rstrip())
        text = text[cut:].lstrip()
    if text:
        parts.append(text)
    return parts


_WORD = re.compile(r"[A-Za-z0-9_']+")


def tokenize(text: str) -> list[str]:
    return [w.lower() for w in _WORD.findall(text)]
