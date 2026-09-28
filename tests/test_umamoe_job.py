"""The uma.moe poll job must not block the asyncio event loop.

Regression: its store writes (a Turso network round trip each) ran directly on the loop, so the
Discord gateway logged "heartbeat blocked for more than 10 seconds" and reconnected - replies to
DMs were delayed by minutes.

Run:  python -m unittest discover -s tests -v
"""
import asyncio
import sys
import time
import types
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

try:  # allow running the tests without httpx installed
    import httpx  # noqa: F401
except ImportError:
    sys.modules["httpx"] = types.SimpleNamespace(AsyncClient=object, HTTPError=Exception)

from LilyAiMain.MainService.Interaction.Workflows.umamoe_job import make_umamoe_job  # noqa: E402


class FakeClient:
    def __init__(self, members):
        self.members = members

    async def get_circle(self, circle_id=None):
        return {"circle": {"name": "Test", "monthly_rank": 5, "monthly_point": 100, "member_count": len(self.members)},
                "members": self.members}


class SlowStore:
    """Stands in for a Turso-backed store: every write takes a while."""

    def __init__(self, prev_fans=None, delay=0.05):
        self.prev_fans, self.delay, self.writes = prev_fans, delay, 0

    def get_circle_state(self, circle_id):
        return None

    def set_circle_state(self, *args):
        pass

    def get_member_fans(self, circle_id, viewer_id):
        return self.prev_fans

    def set_member_fans(self, *args):
        time.sleep(self.delay)
        self.writes += 1


class FakeBus:
    def __init__(self):
        self.published = []

    def publish(self, kind, source, **kw):
        self.published.append((kind, source, kw))


def _members(n):
    return [{"viewer_id": 1000 + i, "trainer_name": f"T{i}", "daily_fans": [100, 200, 350, 0]} for i in range(n)]


class UmamoeJobTests(unittest.IsolatedAsyncioTestCase):
    async def test_store_writes_do_not_block_the_event_loop(self):
        store = SlowStore()  # 6 members x 50ms of blocking writes = 0.3s
        job = make_umamoe_job(FakeClient(_members(6)), store, None, (1,), "", FakeBus())
        ticks, done = 0, False

        async def ticker():
            nonlocal ticks
            while not done:
                await asyncio.sleep(0.01)
                ticks += 1

        t = asyncio.create_task(ticker())
        await job()
        done = True
        await t
        self.assertEqual(store.writes, 6)
        # If the loop had been blocked for the writes, the ticker would have barely run.
        self.assertGreaterEqual(ticks, 10)

    async def test_still_reports_fan_changes(self):
        bus = FakeBus()
        store = SlowStore(prev_fans=300, delay=0)  # was 300, now 350
        job = make_umamoe_job(FakeClient(_members(1)), store, None, (1,), "", bus)
        await job()
        self.assertEqual(len(bus.published), 1)
        self.assertIn("T0 +50 fans", bus.published[0][2]["text"])

    async def test_no_change_publishes_nothing_and_second_run_works(self):
        bus = FakeBus()
        job = make_umamoe_job(FakeClient(_members(2)), SlowStore(prev_fans=350, delay=0), None, (1,), "", bus)
        await job()
        await job()
        self.assertEqual(bus.published, [])


if __name__ == "__main__":
    unittest.main()
