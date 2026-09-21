import asyncio
from collections import defaultdict


class SessionManager:
    """Serialises processing per user so replies stay in order and state isn't raced."""

    def __init__(self):
        self._locks: dict[str, asyncio.Lock] = defaultdict(asyncio.Lock)

    def lock(self, user_id: str) -> asyncio.Lock:
        return self._locks[user_id]
