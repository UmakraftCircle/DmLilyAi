"""Discord-facing helpers that don't need the discord library."""
from LilyAiCore.Helpers.text import chunk_for_discord


def split_reply(text: str, limit: int = 2000) -> list[str]:
    return chunk_for_discord(text, limit) or ["..."]
