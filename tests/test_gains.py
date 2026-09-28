"""member_gains(): monthly gain is a DIFFERENCE of cumulative totals, never a sum of them,
and the anomaly finder flags data that can't be a real running total.

Run:  python -m unittest discover -s tests -v
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from LilyAiCore.ExternalServices.Umamoe.gains import find_anomalies, member_gains  # noqa: E402


class MemberGainsTests(unittest.TestCase):
    def test_monthly_is_latest_minus_day_one_not_a_sum(self):
        # Day 1 = 10m, day 2 = 12m, day 3 = 15m  ->  +5m this month (NOT 10+12+15).
        daily = [10_000_000, 12_000_000, 15_000_000] + [0] * 28
        g = member_gains(daily)
        self.assertEqual(g["total_fans"], 15_000_000)
        self.assertEqual(g["monthly_gain"], 5_000_000)
        self.assertEqual(g["today_gain"], 3_000_000)
        self.assertEqual(g["daily_gain"], 2_000_000)
        self.assertLess(g["monthly_gain"], sum(daily))

    def test_month_end_stays_bounded_by_total(self):
        daily = [900_000_000 + i * 3_000_000 for i in range(28)] + [0, 0, 0]
        g = member_gains(daily)
        self.assertEqual(g["monthly_gain"], 27 * 3_000_000)
        self.assertLessEqual(g["monthly_gain"], g["total_fans"])

    def test_mid_month_joiner_detection_day_counts_as_zero(self):
        # Detected on day 10 with 500m fans already: that influx must not count as a gain.
        detected = [0] * 9 + [500_000_000] + [0] * 21
        g = member_gains(detected)
        self.assertEqual(g["total_fans"], 500_000_000)
        self.assertEqual((g["monthly_gain"], g["today_gain"], g["daily_gain"]), (0, 0, 0))

        # Two days later only the fans earned since detection count.
        later = [0] * 9 + [500_000_000, 510_000_000, 530_000_000] + [0] * 19
        g = member_gains(later)
        self.assertEqual(g["monthly_gain"], 30_000_000)
        self.assertEqual(g["today_gain"], 20_000_000)
        self.assertEqual(g["daily_gain"], 10_000_000)

    def test_club_total_excludes_a_new_members_influx(self):
        veteran = [100_000_000 + i * 2_000_000 for i in range(10)] + [0] * 21          # +18m
        joiner = [0] * 6 + [700_000_000 + i * 1_000_000 for i in range(4)] + [0] * 21  # +3m
        club = sum(member_gains(d)["monthly_gain"] for d in (veteran, joiner))
        self.assertEqual(club, 18_000_000 + 3_000_000)

    def test_established_member_baseline_is_still_day_one(self):
        daily = [50, 60, 0, 90, 0]
        self.assertEqual(member_gains(daily)["monthly_gain"], 40)

    def test_label_only_affects_logging(self):
        daily = [10, 20, 35, 0]
        self.assertEqual(member_gains(daily), member_gains(daily, label="Sam (1)"))
        self.assertEqual(member_gains(None, label="x"), member_gains([]))


class AnomalyTests(unittest.TestCase):
    def test_clean_data_has_no_anomalies(self):
        daily = [10, 12, 15, 0, 0]
        self.assertEqual(find_anomalies(daily, member_gains(daily)), [])

    def test_reproduces_the_reported_impossible_numbers(self):
        # monthly 1,755,029,179 vs total 927,874,437 (the screenshot) needs a day-1 value of
        # -827,154,742 - a corrupt/wrapped entry, not a real fan count.
        daily = [-827_154_742, 100, 927_874_437, 0]
        g = member_gains(daily)
        self.assertEqual(g["total_fans"], 927_874_437)
        self.assertEqual(g["monthly_gain"], 1_755_029_179)
        problems = find_anomalies(daily, g)
        self.assertIn("negative entry in daily_fans", problems)
        self.assertIn("monthly_gain exceeds total_fans", problems)

    def test_flags_totals_that_go_down(self):
        daily = [10, 20, 15, 0]
        self.assertIn("cumulative total decreases between days", find_anomalies(daily, member_gains(daily)))

    def test_tolerates_missing_entries(self):
        daily = [10, None, 15, 0]
        find_anomalies(daily, {"total_fans": 15, "monthly_gain": 5, "today_gain": 0, "daily_gain": 0, "week_avg": None})


if __name__ == "__main__":
    unittest.main()
