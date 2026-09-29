"""Offline tests. Fixtures are the page text GameTora showed for Special Week
(versions and profile), so they check the parser against the layout we have seen."""
import datetime
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import generate_character_profiles as g  # noqa: E402

VERSION_LINES = """Special Week (Original)
▼ Character versions ▼
[Special Dreamer]
Special Week
⭐⭐⭐
Japanese name
スペシャルウィーク
Voice actor
Release date
2025-06-26
Birthday
???
Height
cm
Three sizes
???
Base stats
⭐⭐⭐
Speed
83
Stamina
88
Power
98
Guts
90
Wit
91
⭐⭐⭐⭐⭐
Speed
102
Stamina
108
Power
120
Guts
110
Wit
110
Stat bonuses
Speed
-
Stamina
20%
Power
-
Guts
-
Wit
10%
Aptitude
Surface
Turf
A
Dirt
G
Distance
Short
F
Mile
C
Medium
A
Long
A
Strategy
Front
G
Pace
A
Late
A
End
C
Objectives
1. Participate in the Junior Make Debut
Turn
12
Junior Class, Late June
Turf – 2000m – Medium
2. Place 5th or better in the Kisaragi Sho
Turn 27 (previous + 14)
Classic Class, Early February
G3 – Turf – 1800m – Mile""".split("\n")

PROFILE_LINES = """Special Week
Special Week
Rar'n to go! A pure-hearted girl focused on her dream.
Japanese name
スペシャルウィーク
Voice actor
Azumi Waki
Birthday
May 2
School
Junior Division
Dorm
Ritto Dormitory
My name's Special Week! My dream is to be the top Umamusume in all of Japan!
Measurements
Height
158 cm
Weight
Slight decrease (pre-race nerves)
Three sizes
81 - 56 - 81
Shoe size
Left: 23.5cm Right: 23.0cm
Profile
Strong points
Detailed food reports
Weak points
Using her train pass
Ears
Perks up and teleports to the kitchen when she hears the sounds of cooking
Tail
Moves along with her emotions, making her a terrible poker player
Family
She gets her eye color from her birth mother
Did you know? She can tell different brands of milk apart from taste alone.
Did you know?
She is great at piggyback rides.""".split("\n")

SUPPORT_MD = """# SSR Support Cards

## Power

| Support Card Name | Friendship Bonus | Mood Effect | Speed Bonus | Training Effectiveness | Initial Friendship Gauge | Specialty Priority | EN Release |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Wild Rider] Vodka | 35 (+10) | 40 | - | - | 25 | 65 (+20) | 2025-06-26 |
| [Ballroom Tempest] Vodka | 30 | 60 | - | 15 | 30 | 65 | JP only |
| [時に交わる海と空] Mr. C.B. | 35 | 80 | - | 20 | 30 | 120 | JP only |
"""


class ParserTests(unittest.TestCase):
    def test_html_to_lines(self):
        html = "<h1>Vodka (Original)</h1><script>x=1</script><div>Speed</div><div>96</div><em>Cool line</em>"
        lines, h1, em = g.html_to_lines(html)
        self.assertEqual(lines, ["Vodka (Original)", "Speed", "96", "Cool line"])
        self.assertEqual((h1, em), ("Vodka (Original)", "Cool line"))

    def test_version(self):
        v = g.parse_version(VERSION_LINES, "Special Week (Original)")
        self.assertEqual(v["epithet"], "Special Dreamer")
        self.assertEqual(v["label"], "Original")
        self.assertEqual(v["release"], "2025-06-26")
        self.assertEqual([x["stars"] for x in v["stat_groups"]], [3, 5])
        self.assertEqual(v["stat_groups"][1]["Stamina"], 108)
        self.assertEqual(v["bonuses"]["Stamina"], "20%")
        self.assertIsNone(v["bonuses"]["Speed"])
        self.assertEqual(v["aptitudes"]["End"], "C")
        self.assertEqual(len(v["aptitudes"]), 10)
        self.assertEqual(g.best_fits(v["aptitudes"]), "Best fits: Medium and Long turf, as a Pace Chaser or Late Surger.")
        o = v["objectives"]
        self.assertEqual((o[0]["turn"], o[0]["timing"], o[0]["race"]), ("12", "Junior Class, Late June", "Turf, 2000m, Medium"))
        self.assertEqual((o[1]["turn"], o[1]["race"]), ("27", "G3, Turf, 1800m, Mile"))

    def test_profile(self):
        p = g.parse_profile(PROFILE_LINES, "Rar'n to go! A pure-hearted girl focused on her dream.")
        self.assertEqual((p["jp"], p["va"], p["birthday"]), ("スペシャルウィーク", "Azumi Waki", "May 2"))
        self.assertEqual(p["height"], "158 cm")
        self.assertTrue(p["intro"].startswith("My name's Special Week"))
        self.assertEqual(len(p["trivia"]), 2)
        self.assertTrue(p["trivia"][0].startswith("She can tell different brands"))

    def test_support_cards(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / "SSR.md").write_text(SUPPORT_MD, encoding="utf-8")
            cards = g.load_support_cards(Path(d))
        self.assertEqual(len(cards["vodka"]), 2)
        self.assertIn("mrcb", cards)  # "Mr. C.B." matches the Mr_CB file name
        rows = g.support_table(cards["vodka"])
        self.assertIn("Friendship Bonus 35 (+10)", rows[2])
        self.assertNotIn("Speed Bonus", rows[2])

    def test_render_and_helpers(self):
        v = g.parse_version(VERSION_LINES, "Special Week (Original)")
        v.update(vid="100101", url="https://gametora.com/umamusume/characters/100101-special-week")
        p = g.parse_profile(PROFILE_LINES, "Rar'n to go!")
        md = g.render("Special Week", "special-week", "1001", p, [v], [], datetime.date(2026, 9, 29))
        self.assertTrue(md.startswith("# Special Week\n\n" + g.MARKER))
        for needle in ["| Voice actor | Azumi Waki |", "### Shared aptitudes (all versions)", "| 3 star | 83 | 88 | 98 | 90 | 91 |",
                       "chara_stand_1001_100101.png", "Stamina 20%, Wit 10%", "## Gaps"]:
            self.assertIn(needle, md)

    def test_stub_and_slugs(self):
        self.assertTrue(g.is_stub("# Admire Groove\n"))
        self.assertFalse(g.is_stub("# Vodka\n\n**Japanese name:**"))
        self.assertIn("mr-cb", g.slug_candidates("Mr_CB"))
        self.assertIn("ks-miracle", g.slug_candidates("KS_Miracle"))
        self.assertEqual(g.display_name("Air_Groove"), "Air Groove")

    def test_missing_fields_do_not_crash(self):
        md = g.render("X", "x", None, g.parse_profile([], None),
                      [dict(title="X (Original)", epithet=None, label="Original", release=None, stat_groups=[], bonuses={},
                            aptitudes={}, objectives=[], vid="100001", url="u")], [], datetime.date(2026, 9, 29))
        self.assertIn("Not listed", md)


if __name__ == "__main__":
    unittest.main()
