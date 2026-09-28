"""Timestamp parsing for uma.moe payloads.

uma.moe's OpenAPI spec documents CircleMemberFansMonthly.last_updated (and Circle.last_updated)
as an ISO 8601 date-time string. LilyAiFrontend/Shared/ui.js's fmtAgo() does
`Date.now() / 1000 - ts` and expects ts to already be epoch seconds - handed the raw ISO
string instead, that subtraction is string-minus-number, so it silently produces NaN and
the leaderboard shows "NaNd ago" for every member.
"""
from __future__ import annotations

import math
import re
from datetime import datetime, timezone

_FRACTION = re.compile(r"\.(\d+)")


def to_epoch_seconds(value) -> float | None:
    """Epoch seconds from an ISO 8601 string, a number of seconds, or a number of milliseconds.

    Returns None for None / empty / unparseable input (including NaN/Infinity, which
    float() happily accepts but which are not valid timestamps) so callers can fall back
    to something else. A naive datetime with no offset is read as UTC.
    """
    if value is None or isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        seconds = float(value)
        if not math.isfinite(seconds):  # float("nan") / float("inf") are valid floats
            return None
        return seconds / 1000 if seconds > 1e11 else seconds  # > 1e11 can only be milliseconds
    if not isinstance(value, str):
        return None
    text = value.strip()
    if not text:
        return None
    try:
        numeric = float(text)  # numeric string - also accepts "nan"/"inf", filtered above
    except ValueError:
        pass
    else:
        return to_epoch_seconds(numeric)
    if text[-1] in "Zz":
        text = text[:-1] + "+00:00"
    # datetime.fromisoformat (py<3.11) only accepts exactly 3 or 6 fractional digits; uma.moe
    # (and ISO 8601 generally) can send anywhere from 1-9. Pad/trim to 6 so parsing doesn't
    # depend on how many digits happen to be present.
    text = _FRACTION.sub(lambda m: "." + m.group(1)[:6].ljust(6, "0"), text, count=1)
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.timestamp()
