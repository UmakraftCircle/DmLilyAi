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


class SignFlipNormalizationTests(unittest.TestCase):
    """A run of negative entries in daily_fans (real uma.moe data, not a data-entry error
    on our side) used to be read literally, producing a monthly gain bigger than the
    trainer's total fan count. See _normalize_daily()'s docstring."""

    def test_the_xth_2026_09_28_report(self):
        # Reported live: theXth (viewer_id 460640859804) showed +1,757,291,827 monthly
        # against a 930,137,085 total. Exact array from the Render log.
        daily = [-827154742, -830021721, -832205736, -834098050, -835530231, -837425967,
                 -838932122, -840383441, -844066426, -847557628, -851576808, -855214530,
                 -856880251, -862279944, -865202752, -868542377, -870893111, -875357509,
                 -879452431, -881502420, -885758619, -887429121, -889953219, -894521021,
                 -897698168, 905921468, 918152062, 930137085, 0, 0, 0, 0]
        g = member_gains(daily)
        self.assertEqual(g["total_fans"], 930137085)
        self.assertEqual(g["today_gain"], 930137085 - 918152062)
        self.assertEqual(g["daily_gain"], 918152062 - 905921468)
        # Baseline is abs(first entry), so the flip itself isn't read as a 1.7b jump.
        self.assertEqual(g["monthly_gain"], 930137085 - 827154742)
        self.assertLessEqual(g["monthly_gain"], g["total_fans"])
        self.assertGreater(g["monthly_gain"], 0)

    def test_short_negative_run_still_normalizes(self):
        daily = [-100, -150, -180, 200, 230] + [0] * 26
        g = member_gains(daily)
        self.assertEqual(g["monthly_gain"], 230 - 100)
        self.assertGreater(g["monthly_gain"], 0)

    def test_raw_array_still_flagged_for_logging_even_though_result_is_now_sane(self):
        # find_anomalies() looks at what uma.moe actually sent, not the corrected output -
        # keeps the sign-flip visible in logs after member_gains() fixes the math.
        daily = [-827154742, -830021721, 905921468, 918152062, 930137085] + [0] * 27
        g = member_gains(daily)
        problems = find_anomalies(daily, g)
        self.assertIn("negative entry in daily_fans", problems)
        # and the corrected gains dict no longer trips the "exceeds total" check itself
        self.assertNotIn("monthly_gain exceeds total_fans", problems)


class AnomalyTests(unittest.TestCase):
    def test_clean_data_has_no_anomalies(self):
        daily = [10, 12, 15, 0, 0]
        self.assertEqual(find_anomalies(daily, member_gains(daily)), [])

    def test_flags_totals_that_go_down(self):
        daily = [10, 20, 15, 0]
        self.assertIn("cumulative total decreases between days", find_anomalies(daily, member_gains(daily)))

    def test_tolerates_missing_entries(self):
        daily = [10, None, 15, 0]
        find_anomalies(daily, {"total_fans": 15, "monthly_gain": 5, "today_gain": 0, "daily_gain": 0, "week_avg": None})


if __name__ == "__main__":
    unittest.main()
