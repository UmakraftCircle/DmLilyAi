"""Daily fan snapshot + quota job.

Wires the Deficit flow up to real uma.moe data: for every linked trainer in a
club, reads today's and this month's fan gain straight from uma.moe's own
daily_fans array (via LilyAiCore.ExternalServices.Umamoe.gains.member_gains -
the exact same calculation /api/leaderboard uses) and feeds today's gain into
the DeficitTracker that drives the quota DM.

Gains used to be computed by diffing our own LilyAiMemory.FanGain.FanSnapshotStore
snapshots day over day. That was broken: a trainer's very first tracked day (no
previous local snapshot to diff against) and any run right after a Render
redeploy (the free-plan filesystem is ephemeral, so "yesterday's" row is gone -
see .env.example's TURSO note) both silently came back as "0 gained, 0 /
150,000,000 monthly" regardless of the trainer's real activity, because there
was nothing to diff against. uma.moe's daily_fans array already hands back a
full calendar month of cumulative snapshots in one get_circle() call, so
reading gains from it directly needs no local history and can't cold-start to
zero.

FanSnapshotStore is still written here as a historical record of each day's
total_fans (harmless, and useful if that log is ever wanted later), but it no
longer participates in the gain math.

There is no scraper here: fan data comes from the existing UmamoeClient (the
same client that already powers check_umamoe and /api/leaderboard, configured
via UMAMOE_API_KEY / UMAMOE_CIRCLE_IDS - see render.yaml and .env.example).
One get_circle(circle_id) call per run returns every tracked member's
daily_fans in one shot, the same call umamoe_job.py already makes for the
rank/points poll.
"""
from __future__ import annotations

from datetime import datetime

import discord

from LilyAiCore.ExternalServices.Umamoe.client import UmamoeClient
from LilyAiCore.ExternalServices.Umamoe.gains import member_gains
from LilyAiMemory.FanGain.fan_gain import FanSnapshotStore
from LilyAiMemory.TrainerLink.trainer_link import TrainerLinkStore
from LilyAiTask.DailyTask.DeficitTask.Deficit import (
    DeficitTracker,
    linked_members,
    send_daily_dm,
)


def _is_first_of_month(now: datetime) -> bool:
    return now.day == 1


async def _fetch_member_gains(umamoe: UmamoeClient, circle_id: int) -> dict[str, dict]:
    """trainer_id (uma.moe viewer_id, as str) -> member_gains() breakdown
    (total_fans/today_gain/daily_gain/monthly_gain/week_avg) for every member
    currently on this circle's live roster.
    """
    data = await umamoe.get_circle(circle_id=circle_id)
    out: dict[str, dict] = {}
    for member in data.get("members", []):
        viewer_id = member.get("viewer_id")
        if viewer_id is None:
            continue
        out[str(viewer_id)] = member_gains(member.get("daily_fans"))
    return out


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
    """Run one day's quota cycle for every linked trainer in `club`.

    Args:
        client: logged-in discord.Client/Bot, passed through to send_daily_dm.
        trainer_link_store: source of linked Discord<->trainer pairs.
        fan_store: FanSnapshotStore - written here purely as a historical log
            of each day's total_fans; today_gain/monthly_gain both come from
            member_gains() below, not from diffing these snapshots.
        umamoe: the shared UmamoeClient (app.umamoe - None means
            UMAMOE_API_KEY isn't set, in which case this job shouldn't be
            scheduled; see bootstrap.py).
        circle_id: the uma.moe circle id this club maps to (one of
            settings.umamoe_circle_ids).
        club: which club this run is for ("Umakraft" / "Umakraft 2").
        trackers: trainer_id -> DeficitTracker, kept alive by the caller
            across days (e.g. held on the bot/app instance) so carry persists
            between runs. A trainer's tracker is replaced with a fresh one on
            the 1st of the month.
        now: override for testing; defaults to current UTC time.
    """
    now = now or datetime.utcnow()
    members = linked_members(trainer_link_store)
    if not members:
        return

    member_gain_data = await _fetch_member_gains(umamoe, circle_id)

    for member in members:
        gains = member_gain_data.get(member.trainer_id)
        if gains is None:
            # Linked trainer isn't on this circle's live roster right now
            # (e.g. dropped from the club) - nothing to report today.
            continue

        fan_store.record(club, member.trainer_id, gains["total_fans"])

        if member.trainer_id not in trackers or _is_first_of_month(now):
            trackers[member.trainer_id] = DeficitTracker()

        result = trackers[member.trainer_id].record_day(gains["today_gain"])

        await send_daily_dm(client, member, result, monthly_gain=gains["monthly_gain"])
