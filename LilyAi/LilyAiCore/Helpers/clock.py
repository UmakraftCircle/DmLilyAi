import time
from datetime import datetime, timezone


def now_ts() -> float:
    return time.time()


def utcnow_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")
