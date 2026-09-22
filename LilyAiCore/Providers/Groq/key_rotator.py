"""Even distribution across multiple Groq API keys.

Draws keys from a shuffled bag (no replacement) so every key is used exactly once per
cycle, then reshuffles - this is fairer than plain random.choice(), which can repeat
the same key several times before touching the others.

Also tracks per-key cooldowns so a key that just hit a 429 is skipped until it recovers,
letting the caller switch to a working key immediately instead of only sleeping it out.
"""
import random
import time
from asyncio import Lock


class KeyRotator:
    def __init__(self, keys: list[str], default_cooldown_s: float = 30.0):
        if not keys:
            raise ValueError("KeyRotator needs at least one key")
        self._keys = list(dict.fromkeys(keys))  # de-dupe, preserve order
        self._bag: list[str] = []
        self._default_cooldown_s = default_cooldown_s
        self._cooling_until: dict[str, float] = {}
        self._lock = Lock()

    def _refill(self) -> None:
        self._bag = list(self._keys)
        random.shuffle(self._bag)

    def _usable(self, key: str, exclude: set[str], now: float) -> bool:
        return key not in exclude and self._cooling_until.get(key, 0.0) <= now

    async def next(self, exclude: set[str] | None = None) -> str:
        """Draw the next key. Skips cooling-down and excluded keys where possible;
        falls back to the soonest-to-recover key if everything is currently excluded/cooling."""
        exclude = exclude or set()
        async with self._lock:
            now = time.monotonic()
            for _ in range(2):  # at most one reshuffle needed to find a usable key
                while self._bag:
                    key = self._bag.pop()
                    if self._usable(key, exclude, now):
                        return key
                self._refill()
            # Nothing usable (all keys cooling and/or excluded) - use whichever recovers soonest.
            candidates = [k for k in self._keys if k not in exclude] or self._keys
            return min(candidates, key=lambda k: self._cooling_until.get(k, 0.0))

    async def mark_rate_limited(self, key: str, retry_after_s: float = 0.0) -> None:
        async with self._lock:
            self._cooling_until[key] = time.monotonic() + max(retry_after_s, self._default_cooldown_s)

    @property
    def key_count(self) -> int:
        return len(self._keys)
