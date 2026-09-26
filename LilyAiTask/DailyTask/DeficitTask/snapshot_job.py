"""Daily fan snapshot + quota job.

Wires LilyAiMemory.FanGain.FanSnapshotStore into the existing Deficit
flow: records each linked trainer's current fan_total once a day, derives
that day's gain from the previous snapshot, and feeds it into the same
DeficitTracker used for the quota DM.

No separate "weekly reset" step is needed: LilyAiMemory.FanGain's
today/weekly/monthly figures are always computed as a delta from the
relevant boundary snapshot (today's 00:00, this week's Monday 00:00,
this month's 1st 00:00) - once this job has written a Monday's snapshot,
every gain figure for that club automatically re-baselines against it.

Monthly reconciliation: the monthly figure sent in the DM is computed
here from FanSnapshotStore (fan_total - snapshot at this month's 1st),
the same source the fan gain embed reads via get_fan_gain_rows(). It is
passed into send_daily_dm as an override so the DM never disagrees with
the embed, even if DeficitTracker.total_gained drifts (e.g. after a
restart resets an in-memory tracker mid-month).

Fan totals come from the existing LilyAiCore.ExternalServices.Umamoe.
UmamoeClient (the same uma.moe API client that already powers
check_umamoe and /api/leaderboard, configured via UMAMOE_API_KEY /
UMAMOE_CIRCLE_IDS - see render.yaml and .env.example). There is no
scraper here and none is needed: one get_circle(circle_id) call per run
returns every tracked member's fan total in one shot, the same call
umamoe_job.py already makes for the rank/points poll.
"""
from __future__ import annotations

from datetime import datetime

import discord

from LilyAiCore.ExternalServices.Umamoe.client import UmamoeClient
from LilyAiMemory.FanGain.fan_gain import FanSnapshotStore
from LilyAiMemory.TrainerLink.trainer_link import TrainerLinkStore
from LilyAiTask.DailyTask.DeficitTask.Deficit import (
    DeficitTracker,
    linked_members,
    send_daily_dm,
)


def _is_first_of_month(now: datetime) -> bool:
    return now.day == 1


def _month_start_total(
    fan_store: FanSnapshotStore, club: str, trainer_id: str, now: datetime, fallback: int
) -> int:
    """The trainer's fan_total as of this month's 1st, or `fallback` if
    there's no snapshot that far back yet (new trainer / new club)."""
    month_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    base = fan_store.at_or_before(club, month_start).get(trainer_id)
    return base.fan_total if base else fallback


async def _fetch_fan_totals(umamoe: UmamoeClient, circle_id: int) -> dict[str, int]:
    """trainer_id (uma.moe viewer_id, as str) -> current fan_total for every
    member currently on this circle's roster.

    Same call and same "current total = max(daily_fans)" reading that
    umamoe_job.py's poll job uses, so this and the rank/points poll never
    disagree about a member's fan count.
    """
    data = await umamoe.get_circle(circle_id=circle_id)
    totals: dict[str, int] = {}
    for member in data.get("members", []):
        viewer_id = member.get("viewer_id")
        if viewer_id is None:
            continue
        daily = member.get("daily_fans") or []
        if not daily:
            continue
        totals[str(viewer_id)] = max(daily)
    return totals


async def run_daily_fan_gain(
    client: discord.Client,
    trainer_link_store: TrainerLinkStore,
    fan_store: FanSnapshotStore,
    umamoe: UmamoeClient,
    circle_id: int,
    club: str,
    trackers: dict[str, DeficitTracker],
    now: datetime | None = None,
) -> None:
    """Run one day's snapshot + quota cycle for every linked trainer in `club`.

    Args:
        client: logged-in discord.Client/Bot, passed through to send_daily_dm.
        trainer_link_store: source of linked Discord<->trainer pairs.
        fan_store: FanSnapshotStore for this club's snapshot history.
        umamoe: the shared UmamoeClient (app.umamoe - None means
            UMAMOE_API_KEY isn't set, in which case this job shouldn't be
            scheduled; see bootstrap.py).
        circle_id: the uma.moe circle id this club maps to (one of
            settings.umamoe_circle_ids).
        club: which club this run is for ("Umakraft" / "Umakraft 2").
        trackers: trainer_id -> DeficitTracker, kept alive by the caller
            across days (e.g. held on the bot/app instance) so carry and
            total_gained persist between runs. A trainer's tracker is
            replaced with a fresh one on the 1st of the month so its own
            total_gained restarts at the same boundary the snapshot-based
            monthly figure uses.
        now: override for testing; defaults to current UTC time.
    """
    now = now or datetime.utcnow()
    members = linked_members(trainer_link_store)
    if not members:
        return

    previous_totals = fan_store.latest(club)
    current_totals = await _fetch_fan_totals(umamoe, circle_id)

    for member in members:
        fan_total = current_totals.get(member.trainer_id)
        if fan_total is None:
            # Linked trainer isn't on this circle's live roster right now
            # (e.g. dropped from the club) - nothing to snapshot today.
            continue
        fan_store.record(club, member.trainer_id, fan_total)

        prev = previous_totals.get(member.trainer_id)
        today_gain = fan_total - prev.fan_total if prev else 0

        if member.trainer_id not in trackers or _is_first_of_month(now):
            trackers[member.trainer_id] = DeficitTracker()

        result = trackers[member.trainer_id].record_day(today_gain)

        base_total = _month_start_total(fan_store, club, member.trainer_id, now, fallback=fan_total)
        monthly_gain = fan_total - base_total

        await send_daily_dm(client, member, result, monthly_gain=monthly_gain)
