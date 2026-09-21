"""Token-budget trimming: oldest history goes first, system + latest message are never dropped."""
from LilyAiCore.Helpers.text import estimate_tokens


def trim_history(history: list[dict], budget_tokens: int) -> tuple[list[dict], int]:
    kept: list[dict] = []
    used = 0
    for msg in reversed(history):
        cost = estimate_tokens(msg["content"]) + 4
        if used + cost > budget_tokens:
            break
        kept.append(msg)
        used += cost
    kept.reverse()
    # never start history on an assistant turn
    while kept and kept[0]["role"] != "user":
        kept.pop(0)
    return kept, len(history) - len(kept)
