import time
from collections import OrderedDict, deque

MAX_INPUT_CHARS = 4000


class RateLimiter:
    """Sliding window per user. Keeps us inside Groq free-tier limits."""

    def __init__(self, max_events: int = 8, per_seconds: int = 60, max_users: int = 2000):
        self.max_events, self.per_seconds, self.max_users = max_events, per_seconds, max_users
        self._hits: OrderedDict[str, deque[float]] = OrderedDict()

    def check(self, user_id: str) -> float:
        """Return 0 if allowed, else seconds to wait."""
        now = time.time()
        q = self._hits.setdefault(user_id, deque())
        self._hits.move_to_end(user_id)  # LRU: most-recently-active users survive eviction
        while q and now - q[0] > self.per_seconds:
            q.popleft()
        if len(q) >= self.max_events:
            wait = self.per_seconds - (now - q[0])
        else:
            q.append(now)
            wait = 0.0
        while len(self._hits) > self.max_users:
            self._hits.popitem(last=False)
        return wait


class AccessControl:
    def __init__(self, allowed_ids: frozenset[int]):
        self.allowed = {str(i) for i in allowed_ids}

    def permits(self, user_id: str, source: str) -> bool:
        return source != "discord" or not self.allowed or user_id in self.allowed


def clean_input(text: str) -> str:
    return text.strip()[:MAX_INPUT_CHARS]
