"""Runs fixed table operations on Umamusume docs inside a PandaStack sandbox.

Flow: the chat model picks a doc + operation -> this module pulls the RAW section text from the
engine (not the 2,000-char clipped passages the guide builder uses) -> uploads it with a fixed script
(sandbox_scripts/docs_table_ops.py) to a throwaway microVM -> returns the printed result.
Calculators work the same way with sandbox_scripts/game_calcs.py, but need no doc text: the rules are in the script.

The model only supplies parameters. It never supplies code. Everything blocking is wrapped by
run_table_op_async() so the bot's event loop is never stalled.

Env:
    PANDASTACK_API_KEY             one key, or up to 6 comma-separated (e.g. psk_a,psk_b,psk_c), like GROQ_API_KEY.
                                   Runs are spread evenly across the keys; a key that is rate limited, out of credit
                                   or rejected is skipped for a while and the next key is tried automatically.
    PANDASTACK_TEMPLATE            default "code-interpreter"
    PANDASTACK_MAX_RUNS_PER_HOUR   default 30 PER KEY (cost guard for each key's free-tier credit)
"""
from __future__ import annotations

import asyncio
import hashlib
import json
import os
import threading
import time
from collections import OrderedDict, deque
from pathlib import Path
from typing import Any, Callable

from LilyAiCore.Logging.logger import get_logger
from LilyAiGameSpace.UmamusumeGameSpaceEngine import UmamusumeGameSpaceEngine, get_engine

log = get_logger("gamespace.sandbox")

SCRIPT_DIR = Path(__file__).resolve().parent / "sandbox_scripts"
TABLE_SCRIPT, CALC_SCRIPT = "docs_table_ops.py", "game_calcs.py"
MAX_RAW_CHARS = 400_000          # far below the engine's 2 MB file cap; keeps the upload small
EXEC_TIMEOUT_S = 30
SANDBOX_TTL_S = 120              # backstop: the VM reaps itself if we crash before kill()
CACHE_TTL_S = 600
CACHE_MAX = 64
MAX_KEYS = 6
COOLDOWN_RATE_LIMIT_S = 60        # key hit a rate limit: rest it briefly
COOLDOWN_BAD_KEY_S = 3600         # key rejected or out of credit: rest it for an hour


class SandboxError(Exception):
    """A user-presentable failure (never includes keys or stack traces)."""


def load_keys() -> list[str]:
    """PANDASTACK_API_KEY split on commas, de-duplicated, at most MAX_KEYS (extra keys are ignored)."""
    keys: list[str] = []
    for k in os.getenv("PANDASTACK_API_KEY", "").split(","):
        k = k.strip()
        if k and k not in keys:
            keys.append(k)
    if len(keys) > MAX_KEYS:
        log.warning("PANDASTACK_API_KEY has %d keys; only the first %d are used", len(keys), MAX_KEYS)
    return keys[:MAX_KEYS]


def api_key_set() -> bool:
    return bool(load_keys())


def sdk_installed() -> bool:
    try:
        import pandastack  # noqa: F401
        return True
    except Exception:
        return False


def is_configured() -> bool:
    return api_key_set() and sdk_installed()


# ------------------------------------------------------------------ raw doc text
def raw_section_text(ref: str, section: str | None = None, category: str | None = None,
                     engine: UmamusumeGameSpaceEngine | None = None) -> tuple[str, str, str, str]:
    """Return (doc_id, title, section_path, full_text) with NO clipping. Raises SandboxError if not found."""
    eng = engine or get_engine()
    doc = eng.resolve(ref, category)
    if doc is None:
        similar = eng.suggest(ref)
        hint = f" Did you mean: {', '.join(similar)}?" if similar else ""
        raise SandboxError(f"No doc found for {ref!r}.{hint}")
    secs = doc.visible()

    def render(items) -> str:
        return "\n\n".join(f"{'#' * s.level} {s.heading}\n{s.text}".rstrip() for s in items)

    if section:
        idx = eng._find_section(secs, section)
        if idx is None:
            names = ", ".join(s.path for s in secs if s.level > 1)[:300]
            raise SandboxError(f"No section matching {section!r} in {doc.title}. Sections: {names}")
        text, path = render(eng._subtree(secs, idx)), secs[idx].path
    else:
        text, path = render(secs), ""
    if len(text) > MAX_RAW_CHARS:
        raise SandboxError(f"{doc.title} is too large to process in one go ({len(text):,} chars). Name a section.")
    if not text.strip():
        raise SandboxError(f"That part of {doc.title} is empty.")
    return doc.id, doc.title, path, text


# ------------------------------------------------------------------ guards
class _RateGuard:
    def __init__(self, per_hour: int):
        self.per_hour = per_hour
        self._stamps: deque[float] = deque()
        self._lock = threading.Lock()

    def allow(self) -> bool:
        now = time.monotonic()
        with self._lock:
            while self._stamps and now - self._stamps[0] > 3600:
                self._stamps.popleft()
            if len(self._stamps) >= self.per_hour:
                return False
            self._stamps.append(now)
            return True


def _max_runs() -> int:
    try:
        return max(1, int(os.getenv("PANDASTACK_MAX_RUNS_PER_HOUR", "30")))
    except ValueError:
        return 30


def _kid(key: str) -> str:
    """Short non-reversible id for a key, safe to log. The key itself is never logged."""
    return hashlib.sha1(key.encode("utf-8")).hexdigest()[:6]


class _KeyPool:
    """Round-robin over the keys, with a per-key cooldown and a per-key hourly cap."""

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._next = 0
        self._cool: dict[str, float] = {}
        self._guards: dict[str, _RateGuard] = {}

    def order(self, keys: list[str]) -> list[str]:
        """Keys in the order to try: next in rotation first, keys that are cooling down last-resort only."""
        with self._lock:
            n = len(keys)
            start = self._next % n
            self._next += 1
            ordered = [keys[(start + i) % n] for i in range(n)]
            now = time.monotonic()
            ready = [k for k in ordered if self._cool.get(_kid(k), 0.0) <= now]
            return ready or ordered      # all resting: still try, a credit top-up may have landed

    def cool(self, key: str, seconds: float) -> None:
        with self._lock:
            self._cool[_kid(key)] = time.monotonic() + seconds

    def allow(self, key: str) -> bool:
        with self._lock:
            guard = self._guards.setdefault(_kid(key), _RateGuard(_max_runs()))
        return guard.allow()


_pool = _KeyPool()
_cache: "OrderedDict[str, tuple[float, str]]" = OrderedDict()
_cache_lock = threading.Lock()
_slots = threading.BoundedSemaphore(2)   # at most two sandboxes at once


def _cache_get(key: str) -> str | None:
    with _cache_lock:
        hit = _cache.get(key)
        if hit and time.monotonic() - hit[0] < CACHE_TTL_S:
            _cache.move_to_end(key)
            return hit[1]
        _cache.pop(key, None)
    return None


def _cache_put(key: str, value: str) -> None:
    with _cache_lock:
        _cache[key] = (time.monotonic(), value)
        while len(_cache) > CACHE_MAX:
            _cache.popitem(last=False)


def _classify(exc: Exception) -> float | None:
    """Seconds to rest the key if `exc` is about the KEY (rate limit, bad key, no credit); None otherwise."""
    status = None
    for obj in (exc, getattr(exc, "response", None)):
        for attr in ("status_code", "status"):
            v = getattr(obj, attr, None)
            if isinstance(v, int):
                status = v
                break
        if status is not None:
            break
    name, msg = type(exc).__name__.lower(), str(exc).lower()
    if status == 429 or "ratelimit" in name or "rate limit" in msg or "too many requests" in msg:
        return COOLDOWN_RATE_LIMIT_S
    if (status in (401, 402, 403)
            or any(w in name for w in ("auth", "permission", "quota", "payment"))
            or any(w in msg for w in ("unauthorized", "invalid api key", "invalid token", "forbidden",
                                      "quota", "insufficient", "credit", "payment required"))):
        return COOLDOWN_BAD_KEY_S
    return None


# ------------------------------------------------------------------ the run
def _default_factory(template: str, ttl: int, api_key: str):
    from pandastack import Client   # imported lazily: the bot must start without the SDK
    client = Client(api_key=api_key)
    try:
        return client.sandboxes.create(template=template, ttl_seconds=ttl)
    except TypeError:               # an SDK version without ttl_seconds on this call
        return client.sandboxes.create(template=template)


def _execute(script_name: str, input_text: str, payload: str, sandbox_factory: Callable[..., Any] | None) -> str:
    """Blocking. Upload a fixed script (+ optional input text and a params.json) to a fresh sandbox, run it,
    return its text result.

    Tries the configured keys in rotation; a key-level failure (rate limit, rejected key, no credit)
    rests that key and moves to the next one. Script/operation errors are returned as-is, never retried.
    """
    script = (SCRIPT_DIR / script_name).read_text(encoding="utf-8")
    cache_key = hashlib.sha1((script_name + "\0" + payload + "\0" + input_text).encode("utf-8")).hexdigest()
    if (cached := _cache_get(cache_key)) is not None:
        return cached

    keys = load_keys()
    if sandbox_factory is None:
        if not (keys and sdk_installed()):
            raise SandboxError("The sandbox isn't set up (PANDASTACK_API_KEY or the pandastack package is missing).")
        sandbox_factory = _default_factory
    elif not keys:
        keys = ["test-key"]          # injected factories (tests) don't need a real key
    if not _slots.acquire(timeout=10):
        raise SandboxError("The sandbox is busy right now. Try again in a moment.")

    template = os.getenv("PANDASTACK_TEMPLATE", "code-interpreter")
    key_failed = 0
    try:
        for key in _pool.order(keys):
            if not _pool.allow(key):
                continue
            sbx = None
            try:
                sbx = sandbox_factory(template, SANDBOX_TTL_S, key)
                if input_text:
                    sbx.filesystem.write("/workspace/input.md", input_text)
                sbx.filesystem.write("/workspace/params.json", payload)
                sbx.filesystem.write(f"/workspace/{script_name}", script)
                res = sbx.exec(f"python3 /workspace/{script_name}", timeout_seconds=EXEC_TIMEOUT_S)
                stdout = (getattr(res, "stdout", "") or "").strip()
                code = getattr(res, "exit_code", 0)
                if code not in (0, None) and not stdout:
                    log.warning("sandbox script exited %s: %s", code, (getattr(res, "stderr", "") or "")[:300])
                    raise SandboxError("The sandbox script failed.")
                try:
                    data = json.loads(stdout)
                except json.JSONDecodeError:
                    log.warning("sandbox returned non-JSON output: %r", stdout[:200])
                    raise SandboxError("The sandbox returned an unreadable result.")
                if not data.get("ok"):
                    raise SandboxError(str(data.get("error") or "The operation failed."))
                result = str(data.get("text") or "")
                _cache_put(cache_key, result)
                return result
            except SandboxError:
                raise
            except Exception as e:
                rest = _classify(e)
                if rest is None:
                    log.warning("sandbox call failed: %s: %s", type(e).__name__, str(e)[:200])
                    raise SandboxError("Couldn't reach the sandbox service. Try again in a minute.")
                key_failed += 1
                _pool.cool(key, rest)
                log.warning("pandastack key %s resting %ds (%s); trying the next key", _kid(key), rest, type(e).__name__)
            finally:
                if sbx is not None:
                    try:
                        sbx.kill()
                    except Exception:
                        pass   # TTL reaps it
        if key_failed:
            raise SandboxError("Every PandaStack key is rate limited or out of credit right now. Try again later.")
        raise SandboxError("Sandbox limit reached for this hour. Try again later.")
    finally:
        _slots.release()


def run_table_op(text: str, params: dict[str, Any], *, sandbox_factory: Callable[..., Any] | None = None) -> str:
    """Table operations (top, stat, filter, compare...) on raw doc text. See sandbox_scripts/docs_table_ops.py."""
    payload = json.dumps(params, sort_keys=True, ensure_ascii=False)
    return _execute(TABLE_SCRIPT, text, payload, sandbox_factory)


def run_calc(calculator: str, inputs: dict[str, Any], *, sandbox_factory: Callable[..., Any] | None = None) -> str:
    """Rule-based game calculators (PvP score, sparks, race maths...). See sandbox_scripts/game_calcs.py."""
    payload = json.dumps({"calculator": calculator, "inputs": inputs}, sort_keys=True, ensure_ascii=False)
    return _execute(CALC_SCRIPT, "", payload, sandbox_factory)


async def run_table_op_async(text: str, params: dict[str, Any], **kw: Any) -> str:
    return await asyncio.to_thread(run_table_op, text, params, **kw)


async def run_calc_async(calculator: str, inputs: dict[str, Any], **kw: Any) -> str:
    return await asyncio.to_thread(run_calc, calculator, inputs, **kw)
