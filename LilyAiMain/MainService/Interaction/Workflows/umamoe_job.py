"""Scheduled job: poll tracked uma.moe circles for rank/points/fan changes and alert on anything new."""
import asyncio
import json

from LilyAiCore.ExternalServices.Discord.notifier import NotifierBox
from LilyAiCore.ExternalServices.Umamoe.client import UmamoeClient
from LilyAiCore.ExternalServices.Umamoe.gains import member_gains
from LilyAiCore.ExternalServices.Umamoe.store import UmamoeStore
from LilyAiCore.Logging.logger import get_logger
from LilyAiMain.MainService.Discord.Events.bus import EventBus

log = get_logger("umamoe_job")

# How many top-gaining members get their raw daily_fans array logged on the first poll.
_DIAG_TOP_N = 3


def _log_raw_diag(circle_id: int, members: list[dict]) -> None:
    """Diagnostic: log the raw daily_fans of the biggest monthly gainers once per process.

    Lets us see exactly what uma.moe sends (cumulative totals? negative/wrapped entries?)
    when a leaderboard number looks wrong. Never raises.
    """
    try:
        ranked = []
        for m in members:
            daily = m.get("daily_fans") or []
            if daily:
                ranked.append((member_gains(daily)["monthly_gain"], m, daily))
        ranked.sort(key=lambda r: r[0], reverse=True)
        for monthly, m, daily in ranked[:_DIAG_TOP_N]:
            log.info(
                "fan-gain diag circle=%s %s (%s) monthly_gain=%s daily_fans=%s",
                circle_id, m.get("trainer_name"), m.get("viewer_id"), monthly, json.dumps(daily)[:1000],
            )
    except Exception as e:
        log.warning("fan-gain diag failed: %s", e)


def make_umamoe_job(client: UmamoeClient, store: UmamoeStore, notifier_box: NotifierBox,
                     circle_ids: tuple[int, ...], notify_user_id: str, bus: EventBus):
    diag_logged = False

    def _apply_circle(circle_id: int, name: str, rank, points, member_count, members: list[dict]) -> list[str]:
        """Every blocking store call for one circle, in one place.

        The store talks to SQLite/Turso synchronously (Turso = a network round trip per call), so
        running this directly on the event loop froze the whole bot - the Discord gateway logged
        "heartbeat blocked for more than 10 seconds" and reconnected, delaying replies. run() hands
        this to a worker thread instead (both Database backends are lock-guarded and thread-safe).
        """
        prev = store.get_circle_state(circle_id)
        store.set_circle_state(circle_id, name, rank, points, member_count)

        changes: list[str] = []
        if prev and prev["monthly_rank"] is not None and rank is not None and prev["monthly_rank"] != rank:
            changes.append(f"rank {prev['monthly_rank']} -> {rank}")
        if prev and prev["monthly_point"] is not None and points is not None and points != prev["monthly_point"]:
            changes.append(f"{points - prev['monthly_point']:+d} points ({points} total)")

        for member in members:
            viewer_id = member.get("viewer_id")
            if viewer_id is None:
                continue
            trainer_name = member.get("trainer_name") or str(viewer_id)
            daily = member.get("daily_fans") or []
            if not daily:
                continue
            # member_gains() is the one shared calc (see its docstring) - using it here
            # too means this poller's "current total fans" can never disagree with what
            # check_fan_gain, /api/leaderboard, or the daily quota job report for the
            # same trainer. The previous max(daily) could diverge from that on a data
            # blip (e.g. a stray inflated value from an uma.moe hiccup). Passing a label
            # makes it log a warning (with the raw array) if the data looks impossible.
            total = member_gains(daily, label=f"{trainer_name} ({viewer_id})")["total_fans"]
            prev_fans = store.get_member_fans(circle_id, viewer_id)
            store.set_member_fans(circle_id, viewer_id, trainer_name, total)
            if prev_fans is not None and total > prev_fans:
                changes.append(f"{trainer_name} +{total - prev_fans} fans")
        return changes

    async def run() -> None:
        nonlocal diag_logged
        for circle_id in circle_ids:
            data = await client.get_circle(circle_id=circle_id)
            circle = data.get("circle") or {}
            name = circle.get("name") or str(circle_id)
            members = data.get("members", [])

            if not diag_logged:
                _log_raw_diag(circle_id, members)

            changes = await asyncio.to_thread(
                _apply_circle, circle_id, name, circle.get("monthly_rank"),
                circle.get("monthly_point"), circle.get("member_count"), members,
            )

            if not changes:
                continue
            text = f"📊 {name}: " + "; ".join(changes)
            bus.publish("system", "umamoe", text=text)
            log.info(text)
            if notify_user_id:
                await notifier_box.notifier.send_dm(notify_user_id, text)
        diag_logged = True

    return run
