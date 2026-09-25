"""Scheduled job: poll tracked uma.moe circles for rank/points/fan changes and alert on anything new."""
from LilyAiCore.ExternalServices.Discord.notifier import NotifierBox
from LilyAiCore.ExternalServices.Umamoe.client import UmamoeClient
from LilyAiCore.ExternalServices.Umamoe.store import UmamoeStore
from LilyAiCore.Logging.logger import get_logger
from LilyAiMain.MainService.Discord.Events.bus import EventBus

log = get_logger("umamoe_job")


def make_umamoe_job(client: UmamoeClient, store: UmamoeStore, notifier_box: NotifierBox,
                     circle_ids: tuple[int, ...], notify_user_id: str, bus: EventBus):
    async def run() -> None:
        for circle_id in circle_ids:
            data = await client.get_circle(circle_id=circle_id)
            circle = data.get("circle") or {}
            name = circle.get("name") or str(circle_id)
            rank = circle.get("monthly_rank")
            points = circle.get("monthly_point")
            member_count = circle.get("member_count")

            prev = store.get_circle_state(circle_id)
            store.set_circle_state(circle_id, name, rank, points, member_count)

            changes: list[str] = []
            if prev and prev["monthly_rank"] is not None and rank is not None and prev["monthly_rank"] != rank:
                changes.append(f"rank {prev['monthly_rank']} -> {rank}")
            if prev and prev["monthly_point"] is not None and points is not None and points != prev["monthly_point"]:
                changes.append(f"{points - prev['monthly_point']:+d} points ({points} total)")

            for member in data.get("members", []):
                viewer_id = member.get("viewer_id")
                if viewer_id is None:
                    continue
                trainer_name = member.get("trainer_name") or str(viewer_id)
                daily = member.get("daily_fans") or []
                total = max(daily) if daily else None
                if total is None:
                    continue
                prev_fans = store.get_member_fans(circle_id, viewer_id)
                store.set_member_fans(circle_id, viewer_id, trainer_name, total)
                if prev_fans is not None and total > prev_fans:
                    changes.append(f"{trainer_name} +{total - prev_fans} fans")

            if not changes:
                continue
            text = f"📊 {name}: " + "; ".join(changes)
            bus.publish("system", "umamoe", text=text)
            log.info(text)
            if notify_user_id:
                await notifier_box.notifier.send_dm(notify_user_id, text)

    return run
