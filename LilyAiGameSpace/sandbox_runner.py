"""Runs fixed table operations on Umamusume docs inside a PandaStack sandbox.

Flow: the chat model picks a doc + operation -> this module pulls the RAW section text from the
engine (not the 2,000-char clipped passages the guide builder uses) -> uploads it with a fixed script
(sandbox_scripts/docs_table_ops.py) to a throwaway microVM -> returns the printed result.

The model only supplies parameters. It never supplies code. Everything blocking is wrapped by
run_table_op_async() so the bot's event loop is never stalled.

Env:
    PANDASTACK_API_KEY             required (the SDK reads it itself)
    PANDASTACK_TEMPLATE            default "code-interpreter"
    PANDASTACK_MAX_RUNS_PER_HOUR   default 30 (cost guard for the free tier credit)
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

SCRIPT_PATH = Path(__file__).resolve().parent / "sandbox_scripts" / "docs_table_ops.py"
MAX_RAW_CHARS = 400_000          # far below the engine's 2 MB file cap; keeps the upload small
EXEC_TIMEOUT_S = 30
SANDBOX_TTL_S = 120              # backstop: the VM reaps itself if we crash before kill()
CACHE_TTL_S = 600
CACHE_MAX = 64


class SandboxError(Exception):
    """A user-presentable failure (never includes keys or stack traces)."""


def api_key_set() -> bool:
    return bool(os.getenv("PANDASTACK_API_KEY", "").strip())


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


_guard = _RateGuard(_max_runs())
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


# ------------------------------------------------------------------ the run
def _default_factory(template: str, ttl: int):
    from pandastack import Sandbox   # imported lazily: the bot must start without the SDK
    return Sandbox.create(template=template, ttl_seconds=ttl)


def run_table_op(text: str, params: dict[str, Any], *, sandbox_factory: Callable[..., Any] | None = None) -> str:
    """Blocking. Upload `text` + a fixed script to a fresh sandbox, run it, return its text result."""
    script = SCRIPT_PATH.read_text(encoding="utf-8")
    payload = json.dumps(params, sort_keys=True, ensure_ascii=False)
    key = hashlib.sha1((payload + "\0" + text).encode("utf-8")).hexdigest()
    if (cached := _cache_get(key)) is not None:
        return cached

    if sandbox_factory is None:
        if not is_configured():
            raise SandboxError("The sandbox isn't set up (PANDASTACK_API_KEY or the pandastack package is missing).")
        sandbox_factory = _default_factory
    if not _guard.allow():
        raise SandboxError("Sandbox limit reached for this hour. Try again later.")
    if not _slots.acquire(timeout=10):
        raise SandboxError("The sandbox is busy right now. Try again in a moment.")

    template = os.getenv("PANDASTACK_TEMPLATE", "code-interpreter")
    sbx = None
    try:
        sbx = sandbox_factory(template, SANDBOX_TTL_S)
        sbx.filesystem.write("/workspace/input.md", text)
        sbx.filesystem.write("/workspace/params.json", payload)
        sbx.filesystem.write("/workspace/docs_table_ops.py", script)
        res = sbx.exec("python3 /workspace/docs_table_ops.py", timeout_seconds=EXEC_TIMEOUT_S)
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
        _cache_put(key, result)
        return result
    except SandboxError:
        raise
    except Exception as e:
        log.warning("sandbox call failed: %s: %s", type(e).__name__, str(e)[:200])
        raise SandboxError("Couldn't reach the sandbox service. Try again in a minute.")
    finally:
        _slots.release()
        if sbx is not None:
            try:
                sbx.kill()
            except Exception:
                pass   # TTL reaps it


async def run_table_op_async(text: str, params: dict[str, Any], **kw: Any) -> str:
    return await asyncio.to_thread(run_table_op, text, params, **kw)
