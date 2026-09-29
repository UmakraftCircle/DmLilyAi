"""to_epoch_seconds(): converts uma.moe's ISO 8601 last_updated field (see the
CircleMemberFansMonthly.last_updated / Circle.last_updated schema in uma.moe's OpenAPI
spec) into the epoch seconds the frontend's fmtAgo() expects. Handing fmtAgo() the raw
ISO string produced "NaNd ago" on the leaderboard.

Run:  python -m unittest discover -s tests -v
"""
import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from LilyAiCore.ExternalServices.Umamoe.timestamps import to_epoch_seconds  # noqa: E402


class ToEpochSecondsTests(unittest.TestCase):
    def test_none_and_blank(self):
        for v in (None, "", "   ", True, False):
            self.assertIsNone(to_epoch_seconds(v))

    def test_iso_with_z_suffix(self):
        # uma.moe's actual format per its OpenAPI spec (date-time / ISO 8601).
        expected = datetime(2026, 9, 28, 11, 50, 0, tzinfo=timezone.utc).timestamp()
        self.assertEqual(to_epoch_seconds("2026-09-28T11:50:00Z"), expected)

    def test_iso_with_explicit_offset(self):
        expected = datetime(2026, 9, 28, 11, 50, 0, tzinfo=timezone.utc).timestamp()
        self.assertEqual(to_epoch_seconds("2026-09-28T11:50:00+00:00"), expected)

    def test_naive_iso_treated_as_utc(self):
        expected = datetime(2026, 9, 28, 11, 50, 0, tzinfo=timezone.utc).timestamp()
        self.assertEqual(to_epoch_seconds("2026-09-28T11:50:00"), expected)

    def test_fractional_seconds_of_various_precision(self):
        for frac in ("5", "50", "500", "500000", "500000000"):
            ts = to_epoch_seconds(f"2026-09-28T11:50:00.{frac}Z")
            self.assertIsNotNone(ts)
            self.assertAlmostEqual(ts, datetime(2026, 9, 28, 11, 50, 0, tzinfo=timezone.utc).timestamp(), delta=1.0)

    def test_numeric_seconds_and_milliseconds(self):
        self.assertEqual(to_epoch_seconds(1790596200), 1790596200.0)
        self.assertEqual(to_epoch_seconds(1790596200.5), 1790596200.5)
        self.assertEqual(to_epoch_seconds(1790596200000), 1790596200.0)  # ms -> s

    def test_numeric_string(self):
        self.assertEqual(to_epoch_seconds("1790596200"), 1790596200.0)

    def test_garbage_and_nan_return_none(self):
        for v in ("not a date", "NaN", "Infinity", float("nan"), float("inf")):
            self.assertIsNone(to_epoch_seconds(v))

    def test_unsupported_types_return_none(self):
        for v in ([1, 2, 3], {"a": 1}, object()):
            self.assertIsNone(to_epoch_seconds(v))


if __name__ == "__main__":
    unittest.main()
