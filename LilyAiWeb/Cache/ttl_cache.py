import time
from typing import Any


class TTLCache:
    def __init__(self, ttl: float = 900, max_items: int = 256):
        self.ttl, self.max_items = ttl, max_items
        self._data: dict[str, tuple[float, Any]] = {}

    def get(self, key: str) -> Any | None:
        item = self._data.get(key)
        if not item:
            return None
        if time.time() - item[0] > self.ttl:
            self._data.pop(key, None)
            return None
        return item[1]

    def set(self, key: str, value: Any) -> None:
        if len(self._data) >= self.max_items:
            oldest = min(self._data, key=lambda k: self._data[k][0])
            self._data.pop(oldest, None)
        self._data[key] = (time.time(), value)

    def __len__(self) -> int:
        return len(self._data)
