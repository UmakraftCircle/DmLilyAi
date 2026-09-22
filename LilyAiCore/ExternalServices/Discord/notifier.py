"""Actuator interface: lets other domains send an unsolicited Discord DM, without depending on discord.py.

The Discord client is only constructed after the rest of the app (tools included) is built - see
LilyAiMain/main.py - so tools can't close over the real client at registration time. NotifierBox is a
small mutable seam: tools hold the box and read `.notifier` at call time, and main.py swaps in the real
client once Discord connects. Until then (or if Discord is disabled), NullNotifier just logs and no-ops.
"""
import asyncio
from typing import Protocol

from LilyAiCore.Logging.logger import get_logger

log = get_logger("notifier")


class Notifier(Protocol):
    async def send_dm(self, user_id: str, text: str) -> bool: ...


class NullNotifier:
    async def send_dm(self, user_id: str, text: str) -> bool:
        log.warning("no Discord connection: dropped notification to %s: %s", user_id, text[:80])
        return False


class NotifierBox:
    def __init__(self):
        self.notifier: Notifier = NullNotifier()
        self._tasks: set[asyncio.Task] = set()

    def schedule_dm(self, user_id: str, text: str, delay_s: float) -> None:
        """Fire-and-forget a DM after delay_s. In-memory only: lost on restart/redeploy."""

        async def _job():
            await asyncio.sleep(delay_s)
            await self.notifier.send_dm(user_id, text)

        task = asyncio.create_task(_job())
        self._tasks.add(task)
        task.add_done_callback(self._tasks.discard)
