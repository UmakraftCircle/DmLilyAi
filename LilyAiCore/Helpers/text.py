import re


def estimate_tokens(text: str) -> int:
    """Cheap token estimate (~4 chars/token). Good enough for budgeting."""
    return max(1, len(text) // 4)


def truncate(text: str, limit: int, suffix: str = "...") -> str:
    return text if len(text) <= limit else text[: max(0, limit - len(suffix))] + suffix


_FENCE = re.compile(r"```([^\n`]*)\n?")


def _open_fence_lang(piece: str) -> str | None:
    """Return the language tag of the ``` fence still open at the end of `piece`, or None if
    every fence in it is already closed (an even number of ``` markers)."""
    fences = _FENCE.findall(piece)
    return fences[-1] if len(fences) % 2 == 1 else None


def chunk_for_discord(text: str, limit: int = 2000) -> list[str]:
    """Split text into <=limit pieces, preferring paragraph, then line, then space boundaries.

    Keeps ``` code fences balanced across the split: if a cut would land inside an open fence,
    the piece is closed with a trailing ``` and the next piece reopens with the same language
    tag, so Discord doesn't render the rest of the reply as one giant unterminated code block.
    """
    text = text.strip()
    if not text:
        return []
    parts: list[str] = []
    reopen = ""  # a ``` fence (with language) to prepend to the next piece, if we're mid-fence
    slack = 8  # headroom for a closing ``` we might append, so pieces still fit under `limit`
    while len(text) > limit:
        budget = max(1, limit - len(reopen) - slack)
        cut = max(text.rfind("\n\n", 0, budget), text.rfind("\n", 0, budget), text.rfind(" ", 0, budget))
        if cut < budget // 2:
            cut = budget
        piece = reopen + text[:cut].rstrip()
        lang = _open_fence_lang(piece)
        if lang is not None:
            piece += "\n```"
            reopen = f"```{lang}\n"
        else:
            reopen = ""
        parts.append(piece)
        text = text[cut:].lstrip()
    if text:
        parts.append(reopen + text)
    return parts


_WORD = re.compile(r"[A-Za-z0-9_']+")


def tokenize(text: str) -> list[str]:
    return [w.lower() for w in _WORD.findall(text)]
