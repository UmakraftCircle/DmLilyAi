import asyncio
from collections import OrderedDict


class SessionManager:
    """Serialises processing per user so replies stay in order and state isn't raced."""

    def __init__(self, max_users: int = 2000):
        self.max_users = max_users
        self._locks: OrderedDict[str, asyncio.Lock] = OrderedDict()

    def lock(self, user_id: str) -> asyncio.Lock:
        lk = self._locks.get(user_id)
        if lk is None:
            lk = self._locks[user_id] = asyncio.Lock()
        else:
            self._locks.move_to_end(user_id)  # LRU: most-recently-active users survive eviction
        self._evict_idle()
        return lk

    def _evict_idle(self) -> None:
        """Drop the oldest, currently-unheld locks once over the cap. A held lock is never evicted -
        that would let two calls for the same user run concurrently. An evicted user just gets a
        fresh Lock() next time, which is safe since locks carry no state of their own."""
        if len(self._locks) <= self.max_users:
            return
        for uid in list(self._locks):
            if len(self._locks) <= self.max_users:
                break
            if not self._locks[uid].locked():
                del self._locks[uid]
