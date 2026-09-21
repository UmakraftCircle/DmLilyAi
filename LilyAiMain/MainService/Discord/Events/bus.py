"""In-process event bus feeding the frontend Relay (monitoring/debugging)."""
import itertools
import time
from collections import deque
from typing import Any


class EventBus:
    def __init__(self, maxlen: int = 500):
        self._events: deque[dict[str, Any]] = deque(maxlen=maxlen)
        self._ids = itertools.count(1)

    def publish(self, kind: str, source: str, user_id: str = "", name: str = "", text: str = "", **meta) -> dict:
        ev = {
            "id": next(self._ids), "ts": time.time(), "kind": kind, "source": source,
            "user_id": user_id, "name": name, "text": text, "meta": meta,
        }
        self._events.append(ev)
        return ev

    def since(self, after: int = 0, source: str | None = None, limit: int = 200) -> list[dict]:
        out = [e for e in self._events if e["id"] > after and (source in (None, "", "all") or e["source"] == source)]
        return out[-limit:]
