"""Actuator interface: lets other domains send an unsolicited Discord DM, without depending on discord.py.

The Discord client is only constructed after the rest of the app (tools included) is built - see
LilyAiMain/main.py - so tools can't close over the real client at registration time. NotifierBox is a
small mutable seam: tools hold the box and read `.notifier` at call time, and main.py swaps in the real
client once Discord connects. Until then (or if Discord is disabled), NullNotifier just logs and no-ops.

Scheduled reminders are persisted via an optional ReminderStore (SQLite) so a restart/redeploy before
one fires doesn't lose it - main.py calls resume_pending() once the real client is wired in, which
replays anything still outstanding (overdue ones fire immediately instead of being dropped).
"""
import asyncio
import time
from typing import Optional, Protocol

from LilyAiCore.ExternalServices.Discord.reminder_store import ReminderStore
from LilyAiCore.Logging.logger import get_logger

log = get_logger("notifier")


class Notifier(Protocol):
    async def send_dm(self, user_id: str, text: str) -> bool: ...


class NullNotifier:
    async def send_dm(self, user_id: str, text: str) -> bool:
        log.warning("no Discord connection: dropped notification to %s: %s", user_id, text[:80])
        return False


class NotifierBox:
    def __init__(self, store: Optional[ReminderStore] = None):
        self.notifier: Notifier = NullNotifier()
        self.store = store
        self._tasks: set[asyncio.Task] = set()

    def schedule_dm(self, user_id: str, text: str, delay_s: float) -> None:
        """Fire-and-forget a DM after delay_s. Persisted via the store (if configured) until
        it actually sends, so it survives a restart in between - see resume_pending()."""
        due_at = time.time() + delay_s
        reminder_id = self.store.add(user_id, text, due_at) if self.store else None
        self._spawn(user_id, text, delay_s, reminder_id)

    def resume_pending(self) -> None:
        """Reschedule reminders left over from before a restart/redeploy. Call once after the
        real Discord client is wired in (self.notifier is no longer the NullNotifier).
        Overdue reminders fire immediately rather than being silently dropped."""
        if not self.store:
            return
        now = time.time()
        pending = self.store.all_pending()
        if pending:
            log.info("resuming %d pending reminder(s)", len(pending))
        for row in pending:
            delay_s = max(0.0, row["due_at"] - now)
            self._spawn(row["user_id"], row["message"], delay_s, row["id"])

    def _spawn(self, user_id: str, text: str, delay_s: float, reminder_id: int | None) -> None:
        async def _job():
            await asyncio.sleep(delay_s)
            try:
                await self.notifier.send_dm(user_id, text)
            finally:
                if reminder_id is not None and self.store:
                    self.store.remove(reminder_id)

        task = asyncio.create_task(_job())
        self._tasks.add(task)
        task.add_done_callback(self._tasks.discard)
