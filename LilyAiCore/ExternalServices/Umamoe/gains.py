"""Shared fan-gain math for uma.moe's daily-fan array.

Pulled out of LilyAiMain/MainService/Api/server.py so it has exactly one
implementation: /api/leaderboard and the daily quota DM (LilyAiTask/DailyTask/
DeficitTask/snapshot_job.py) both call member_gains() and can never disagree
about a trainer's numbers.
"""
from __future__ import annotations

from datetime import datetime, timezone


def member_gains(daily_fans: list[int] | None) -> dict:
    """Fan-gain breakdown from uma.moe's daily-fan array (one cumulative-total entry per
    day of the currently-tracked month; days that haven't happened yet come back as 0
    padding, since get_circle() hands back a full calendar month of snapshots rather than
    "up to today").

    Returns:
      total_fans   - current cumulative fan count (last day with real data)
      today_gain   - fans gained so far on the current (possibly still in-progress) day
      daily_gain   - fans gained on the last FULL completed day (i.e. "yesterday")
      monthly_gain - fans gained since day 1 of the tracked month
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

    monthly_gain = current - daily[0]

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
