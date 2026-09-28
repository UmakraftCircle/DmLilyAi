"""Shared fan-gain math for uma.moe's daily-fan array.

Pulled out of LilyAiMain/MainService/Api/server.py so it has exactly one
implementation: /api/leaderboard and the daily quota DM (LilyAiTask/DailyTask/
DeficitTask/snapshot_job.py) both call member_gains() and can never disagree
about a trainer's numbers.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone

from LilyAiCore.Logging.logger import get_logger

log = get_logger("umamoe_gains")


def find_anomalies(daily_fans: list[int] | None, gains: dict) -> list[str]:
    """Reasons a member's numbers can't be right, given cumulative daily totals.

    daily_fans is a running total, so real data is never negative, never goes down
    from one day to the next, and a month's gain can never exceed the current total.
    Any hit means uma.moe's array (or how we read it) is off - see the diagnostics
    in LilyAiMain/MainService/Interaction/Workflows/umamoe_job.py.
    """
    daily = daily_fans or []
    problems: list[str] = []
    numbers = [v for v in daily if isinstance(v, (int, float))]
    if any(v < 0 for v in numbers):
        problems.append("negative entry in daily_fans")
    seen = [v for v in numbers if v]
    if any(b < a for a, b in zip(seen, seen[1:])):
        problems.append("cumulative total decreases between days")
    if gains["monthly_gain"] < 0:
        problems.append("monthly_gain is negative")
    if gains["monthly_gain"] > gains["total_fans"]:
        problems.append("monthly_gain exceeds total_fans")
    return problems


def member_gains(daily_fans: list[int] | None, label: str | None = None) -> dict:
    """Fan-gain breakdown - see _compute_gains().

    label is optional and only affects logging: when given (e.g. "Nero (316112867285)"),
    a warning with the raw array is logged if the numbers fail find_anomalies(). The
    returned values are identical with or without it.
    """
    gains = _compute_gains(daily_fans)
    if label is not None:
        try:
            problems = find_anomalies(daily_fans, gains)
            if problems:
                log.warning(
                    "fan-gain anomaly for %s: %s | gains=%s | daily_fans=%s",
                    label, "; ".join(problems), gains, json.dumps(daily_fans)[:1000],
                )
        except Exception as e:  # diagnostics must never break a poll
            log.warning("fan-gain anomaly check failed for %s: %s", label, e)
    return gains


def _compute_gains(daily_fans: list[int] | None) -> dict:
    """Fan-gain breakdown from uma.moe's daily-fan array (one cumulative-total entry per
    day of the currently-tracked month; days that haven't happened yet come back as 0
    padding, since get_circle() hands back a full calendar month of snapshots rather than
    "up to today").

    Returns:
      total_fans   - current cumulative fan count (last day with real data)
      today_gain   - fans gained so far on the current (possibly still in-progress) day
      daily_gain   - fans gained on the last FULL completed day (i.e. "yesterday")
      monthly_gain - fans gained since the first day this trainer has data in the tracked month
                     (day 1 for an established member; for someone who joined mid-month, the day
                     uma.moe first detected them - see the join note below)
      week_avg     - average daily gain since this week's Monday, resetting every Monday;
                     None when Monday falls before day 1 of the fetched month (edge of month)

    "Today" is the LAST NON-ZERO entry, not simply the last slot in the array - blindly
    using daily[-1] would pick up an unfilled future day (0) and produce a wildly negative
    gain. Same logic walks backward again to find the last full day, and again for Monday.

    Deliberately stateless: everything comes from this one daily_fans array, so callers
    never need their own day-to-day snapshot history to get correct today/monthly figures
    - not on a trainer's very first tracked day, and not after a process restart wipes
    any local snapshot store (e.g. Render's free-plan ephemeral filesystem).
    """
    daily = daily_fans or []
    empty = {"total_fans": 0, "today_gain": 0, "daily_gain": 0, "monthly_gain": 0, "week_avg": None}
    if not daily:
        return empty

    def last_nonzero(upto: int) -> int | None:
        for i in range(upto, -1, -1):
            if daily[i]:
                return i
        return None

    latest_idx = last_nonzero(len(daily) - 1)
    if latest_idx is None:
        return empty
    current = daily[latest_idx]

    prev_idx = last_nonzero(latest_idx - 1)
    today_gain = current - daily[prev_idx] if prev_idx is not None else 0

    day_before_idx = last_nonzero(prev_idx - 1) if prev_idx is not None else None
    daily_gain = (daily[prev_idx] - daily[day_before_idx]
                  if prev_idx is not None and day_before_idx is not None else 0)

    # Join note: a trainer who joined the club mid-month has 0 padding before the day uma.moe
    # first detected them, and on that day their whole pre-existing total appears at once.
    # Measuring from daily[0] (a 0) would book all of it as a gain and inflate the club's fan
    # gain. Baselining on the FIRST day with data makes the detection day's gain 0 (today_gain
    # and daily_gain already come out 0 there because there is no earlier day to diff against),
    # so only fans earned after being detected count. Established members (data on day 1) are
    # unaffected: their baseline is still daily[0].
    first_idx = next(i for i, v in enumerate(daily) if v)  # exists: latest_idx is not None
    monthly_gain = current - daily[first_idx]

    # Resolve "this Monday" as a day-of-month against the same array. Assumes the array's
    # month matches the server's current UTC month (true unless this poll happens right at
    # a month boundary); a Monday that falls in the previous month reports week_avg=None.
    today = datetime.now(timezone.utc)
    monday_day = today.day - today.weekday()  # Monday == 0
    week_avg = None
    if monday_day >= 1:
        monday_idx = monday_day - 1
        if monday_idx <= latest_idx and daily[monday_idx]:
            elapsed = max(1, latest_idx - monday_idx + 1)
            week_avg = round((current - daily[monday_idx]) / elapsed)

    return {
        "total_fans": current, "today_gain": today_gain, "daily_gain": daily_gain,
        "monthly_gain": monthly_gain, "week_avg": week_avg,
    }
