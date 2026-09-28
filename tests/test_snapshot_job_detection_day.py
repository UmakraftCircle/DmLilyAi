"""run_daily_fan_gain(): a trainer's first_tracked_day (see gains.py) must not be charged
a quota deficit - there's no earlier day of data for "today" to be measured against yet.

Run:  python -m unittest discover -s tests -v
"""
import asyncio
import sys
import types
import unittest
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# discord.py isn't installed in this environment; snapshot_job.py and Deficit.py only use
# it for type hints (deferred via `from __future__ import annotations`) and as a runtime
# client object, so a minimal stub is enough to import and exercise both modules.
sys.modules.setdefault("discord", types.SimpleNamespace(Client=object))

from LilyAiTask.DailyTask.DeficitTask.snapshot_job import run_daily_fan_gain  # noqa: E402


class FakeUmamoe:
    def __init__(self, members):
        self._members = members

    async def get_circle(self, circle_id=None):
        return {"circle": {"name": "Test Circle"}, "members": self._members}


class FakeTrainerLinkStore:
    def __init__(self, links):
        self._links = links

    def all_linked(self):
        return self._links


class FakeFanSnapshotStore:
    def __init__(self):
        self.recorded = []

    def record(self, club, trainer_id, fan_total):
        self.recorded.append((club, trainer_id, fan_total))


class FakeDeficitState:
    def __init__(self, carry, total_gained):
        self.carry = carry
        self.total_gained = total_gained


class FakeDeficitStateStore:
    def __init__(self):
        self._saved = {}
        self.set_calls = []
        self.reset_calls = []

    def get(self, club, trainer_id):
        return self._saved.get((club, trainer_id))

    def set(self, club, trainer_id, carry, total_gained):
        self._saved[(club, trainer_id)] = FakeDeficitState(carry, total_gained)
        self.set_calls.append((club, trainer_id, carry, total_gained))

    def reset(self, club, trainer_id):
        self._saved[(club, trainer_id)] = FakeDeficitState(0, 0)
        self.reset_calls.append((club, trainer_id))


class FakeUser:
    def __init__(self, sink, discord_id):
        self.sink = sink
        self.discord_id = discord_id

    async def send(self, message):
        self.sink.append((self.discord_id, message))


class FakeDiscordClient:
    def __init__(self):
        self.sent = []

    def get_user(self, discord_id):
        return FakeUser(self.sent, discord_id)

    async def fetch_user(self, discord_id):
        return FakeUser(self.sent, discord_id)


def _link(discord_id, trainer_id, trainer_name):
    return types.SimpleNamespace(discord_id=discord_id, trainer_id=trainer_id, trainer_name=trainer_name)


class DetectionDayTests(unittest.TestCase):
    def _run(self, members, links, now=None):
        umamoe = FakeUmamoe(members)
        trainer_link_store = FakeTrainerLinkStore(links)
        fan_store = FakeFanSnapshotStore()
        tracker_store = FakeDeficitStateStore()
        client = FakeDiscordClient()
        asyncio.new_event_loop().run_until_complete(
            run_daily_fan_gain(
                client, trainer_link_store, fan_store, tracker_store, umamoe,
                circle_id=1, club="Umakraft", now=now or datetime(2026, 9, 15),
            )
        )
        return fan_store, tracker_store, client

    def test_new_joiner_gets_no_dm_and_no_deficit(self):
        # Detected today with 500m fans already on the books.
        members = [{"viewer_id": 1, "trainer_name": "Newbie",
                    "daily_fans": [0] * 14 + [500_000_000] + [0] * 16}]
        links = [_link(discord_id=111, trainer_id="1", trainer_name="Newbie")]

        fan_store, tracker_store, client = self._run(members, links)

        # Historical snapshot is still written...
        self.assertEqual(fan_store.recorded, [("Umakraft", "1", 500_000_000)])
        # ...but no quota state and no DM went out for the detection day itself.
        self.assertEqual(tracker_store.set_calls, [])
        self.assertEqual(client.sent, [])

    def test_established_member_still_gets_normal_quota_tracking(self):
        members = [{"viewer_id": 2, "trainer_name": "Veteran",
                    "daily_fans": [10_000_000, 16_000_000] + [0] * 29}]
        links = [_link(discord_id=222, trainer_id="2", trainer_name="Veteran")]

        fan_store, tracker_store, client = self._run(members, links)

        self.assertEqual(len(tracker_store.set_calls), 1)
        club, trainer_id, carry, total_gained = tracker_store.set_calls[0]
        self.assertEqual((club, trainer_id), ("Umakraft", "2"))
        # gained 6,000,000 today against a 5,000,000 quota -> 1,000,000 surplus (carry < 0)
        self.assertEqual(carry, -1_000_000)
        self.assertEqual(len(client.sent), 1)
        discord_id, message = client.sent[0]
        self.assertEqual(discord_id, 222)
        self.assertIn("Surplus", message)

    def test_month_rollover_day_one_also_skips_everyone(self):
        # First poll of a new month: every linked member has exactly one data point.
        members = [
            {"viewer_id": 3, "trainer_name": "A", "daily_fans": [10_000_000] + [0] * 30},
            {"viewer_id": 4, "trainer_name": "B", "daily_fans": [999_000_000] + [0] * 30},
        ]
        links = [
            _link(discord_id=333, trainer_id="3", trainer_name="A"),
            _link(discord_id=444, trainer_id="4", trainer_name="B"),
        ]

        fan_store, tracker_store, client = self._run(members, links, now=datetime(2026, 10, 1))

        self.assertEqual(tracker_store.set_calls, [])
        self.assertEqual(client.sent, [])
        self.assertEqual(len(fan_store.recorded), 2)  # still logged historically

    def test_joiner_gets_normal_tracking_the_day_after_detection(self):
        members = [{"viewer_id": 5, "trainer_name": "Newbie",
                    "daily_fans": [0] * 13 + [500_000_000, 507_000_000] + [0] * 16}]
        links = [_link(discord_id=555, trainer_id="5", trainer_name="Newbie")]

        fan_store, tracker_store, client = self._run(members, links)

        self.assertEqual(len(tracker_store.set_calls), 1)
        _, _, carry, _ = tracker_store.set_calls[0]
        # gained 7,000,000 vs 5,000,000 quota -> 2,000,000 surplus
        self.assertEqual(carry, -2_000_000)
        self.assertEqual(len(client.sent), 1)

    def test_unlinked_roster_member_is_ignored(self):
        members = [{"viewer_id": 6, "trainer_name": "Ghost", "daily_fans": [1, 2, 3] + [0] * 28}]
        links = []  # nobody linked
        fan_store, tracker_store, client = self._run(members, links)
        self.assertEqual(fan_store.recorded, [])
        self.assertEqual(client.sent, [])

    def test_linked_trainer_missing_from_live_roster_is_skipped(self):
        members = []  # left the club
        links = [_link(discord_id=777, trainer_id="7", trainer_name="Gone")]
        fan_store, tracker_store, client = self._run(members, links)
        self.assertEqual(fan_store.recorded, [])
        self.assertEqual(tracker_store.set_calls, [])
        self.assertEqual(client.sent, [])


if __name__ == "__main__":
    unittest.main()
