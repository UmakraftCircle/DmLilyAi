import time
from collections import defaultdict, deque

MAX_INPUT_CHARS = 4000


class RateLimiter:
    """Sliding window per user. Keeps us inside Groq free-tier limits."""

    def __init__(self, max_events: int = 8, per_seconds: int = 60):
        self.max_events, self.per_seconds = max_events, per_seconds
        self._hits: dict[str, deque[float]] = defaultdict(deque)

    def check(self, user_id: str) -> float:
        """Return 0 if allowed, else seconds to wait."""
        now = time.time()
        q = self._hits[user_id]
        while q and now - q[0] > self.per_seconds:
            q.popleft()
        if len(q) >= self.max_events:
            return self.per_seconds - (now - q[0])
        q.append(now)
        return 0.0


class AccessControl:
    def __init__(self, allowed_ids: frozenset[int]):
        self.allowed = {str(i) for i in allowed_ids}

    def permits(self, user_id: str, source: str) -> bool:
        return source != "discord" or not self.allowed or user_id in self.allowed


def clean_input(text: str) -> str:
    return text.strip()[:MAX_INPUT_CHARS]
