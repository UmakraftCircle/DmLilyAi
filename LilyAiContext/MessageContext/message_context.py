from LilyAiContext.ContextBuilder.models import HistoryMessage


def history_to_messages(history: list[HistoryMessage]) -> list[dict]:
    return [{"role": h.role, "content": h.content} for h in history if h.role in {"user", "assistant"}]
