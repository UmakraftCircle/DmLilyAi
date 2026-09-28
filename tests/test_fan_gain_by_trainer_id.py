"""Lily can look a trainer up by Trainer ID (not just name) - check_fan_gain's trainer_id filter.

Run:  python -m unittest discover -s tests -v
"""
import asyncio
import sys
import types
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

try:  # allow running the tests without httpx installed
    import httpx  # noqa: F401
except ImportError:
    sys.modules["httpx"] = types.SimpleNamespace(AsyncClient=object, HTTPError=Exception)

from LilyAiMain.MainService.bootstrap import _trainer_link_tools, _umamoe_tools  # noqa: E402
from LilyAiTool.Models.tool_models import ToolContextData  # noqa: E402
from LilyAiTool.Validator import validate_args  # noqa: E402


class FakeUmamoe:
    async def get_circle(self, circle_id=None):
        return {
            "circle": {"name": "Test Circle"},
            "members": [
                {"viewer_id": 612856830731, "trainer_name": "Sam", "daily_fans": [100, 250, 400, 0]},
                {"viewer_id": 111111111, "trainer_name": "Alex", "daily_fans": [500, 900, 1300, 0]},
                {"viewer_id": 222222222, "trainer_name": None, "daily_fans": [10, 20, 30, 0]},
            ],
        }


class FakeLinks:
    def __init__(self, link=None):
        self.link = link

    def by_discord_id(self, discord_id):
        return self.link


def _fan_gain_spec():
    return next(s for s in _umamoe_tools(FakeUmamoe(), (1,)) if s.name == "check_fan_gain")


def run(spec, args):
    ctx = ToolContextData("u", "Tester", {})
    return asyncio.new_event_loop().run_until_complete(spec.handler(ctx, args))


class FanGainByTrainerIdTests(unittest.TestCase):
    def test_filters_by_trainer_id_string(self):
        out = run(_fan_gain_spec(), {"trainer_id": "612856830731"})
        self.assertIn("Sam", out)
        self.assertIn("612856830731", out)
        self.assertNotIn("Alex", out)

    def test_accepts_int_and_formatted_ids(self):
        for value in (612856830731, "612,856,830,731", " 612856830731 "):
            out = run(_fan_gain_spec(), {"trainer_id": value})
            self.assertIn("Sam", out, value)
            self.assertNotIn("Alex", out, value)

    def test_finds_a_member_with_no_name_by_id(self):
        out = run(_fan_gain_spec(), {"trainer_id": "222222222"})
        self.assertIn("222222222", out)
        self.assertNotIn("Sam", out)

    def test_unknown_id_says_so(self):
        out = run(_fan_gain_spec(), {"trainer_id": "999999999"})
        self.assertIn("No member with Trainer ID 999999999", out)

    def test_name_filter_and_default_listing_still_work(self):
        self.assertIn("Alex", run(_fan_gain_spec(), {"trainer_name": "ale"}))
        out = run(_fan_gain_spec(), {})
        self.assertTrue("Sam" in out and "Alex" in out)

    def test_schema_accepts_id_as_string_int_or_null(self):
        schema = _fan_gain_spec().parameters
        for value in ("612856830731", 612856830731, None):
            self.assertEqual(validate_args(schema, {"trainer_id": value})["trainer_id"], value)


class LinkedTrainerToolTests(unittest.TestCase):
    def test_result_hands_the_id_to_check_fan_gain(self):
        link = types.SimpleNamespace(trainer_id="612856830731", trainer_name=None)
        spec = _trainer_link_tools(FakeLinks(link))[0]
        out = spec.handler(ToolContextData("u", "Tester", {}), {})
        self.assertIn("612856830731", out)
        self.assertIn("trainer_id", out)

    def test_not_linked(self):
        spec = _trainer_link_tools(FakeLinks(None))[0]
        self.assertIn("isn't linked", spec.handler(ToolContextData("u", "Tester", {}), {}))


if __name__ == "__main__":
    unittest.main()
