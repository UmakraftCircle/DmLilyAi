"""Tests for the JSON-based parser. The text lines are the real ones GameTora returned for
Special Week (Original) to the GitHub runner; the JSON numbers are the real itemData values."""
import datetime
import html
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import generate_character_profiles as g  # noqa: E402
import generate_character_profiles_v2 as v2  # noqa: E402

TEXT = """Special Week (Original) | Uma Musume | GameTora
8|Special Week (Original)
▼ Character versions ▼
[Special Dreamer]
Special Week
⭐⭐⭐
Base stats
Stat bonuses
Aptitude
Objectives
Junior
1. Participate in the Junior Make Debut
Turn 12
Junior Class
,
Late June
Turf – 2000m – Medium
Classic
2. Place 5th or better in the Kisaragi Sho
Turn 27 (previous + 14)
Classic Class
,
Early February
G3 – Turf – 1800m – Mile
3. Place 5th or better in the Tokyo Yushun (Japanese Derby)
Turn 34 (previous + 6)
Classic Class
,
Late May
G1 – Turf – 2400m – Medium
4. Place 3rd or better in the Kikuka Sho
Turn 44 (previous + 9)
Classic Class
,
Late October
1. Some other numbered list further down the page""".split("\n")[1:]

ITEM = {
    "url_name": "100101-special-week", "char_id": 1001, "card_id": 100101, "name_en": "Special Week",
    "title": "Special Dreamer", "title_en_gl": "[Special Dreamer]", "rarity": 3, "release": "2021-02-24",
    "release_en": "2025-06-26", "stat_bonus": [0, 20, 0, 0, 10], "base_stats": [83, 88, 98, 90, 91],
    "aptitude": ["A", "G", "F", "C", "A", "A", "G", "A", "A", "C"],
    "four_star_stats": [92, 98, 109, 100, 101], "five_star_stats": [102, 108, 120, 110, 110],
}


def make_html(item=ITEM):
    data = {"props": {"pageProps": {"itemData": item}}}
    body = "".join(f"<div>{html.escape(l)}</div>" for l in TEXT)
    return (f'<html><h1>Special Week (Original)</h1>{body}'
            f'<script id="__NEXT_DATA__" type="application/json">{json.dumps(data)}</script></html>')


class V2Tests(unittest.TestCase):
    def test_version_from_json(self):
        v = v2.parse_version_page(make_html(), "100101", "https://x/100101-special-week", print)
        self.assertEqual(v["epithet"], "Special Dreamer")
        self.assertEqual(v["label"], "Original")
        self.assertEqual(v["release"], "2025-06-26")
        self.assertEqual([x["stars"] for x in v["stat_groups"]], [3, 4, 5])
        self.assertEqual(v["stat_groups"][2]["Wit"], 110)
        self.assertEqual(v["bonuses"], {"Speed": None, "Stamina": "20%", "Power": None, "Guts": None, "Wit": "10%"})
        self.assertEqual(v["aptitudes"]["Turf"], "A")
        self.assertEqual(v["aptitudes"]["Dirt"], "G")
        self.assertEqual(v["aptitudes"]["Late"], "A")
        self.assertEqual(v["aptitudes"]["End"], "C")
        self.assertEqual(g.best_fits(v["aptitudes"]), "Best fits: Medium and Long turf, as a Pace Chaser or Late Surger.")

    def test_objectives_from_split_text_nodes(self):
        o = v2.parse_objectives(TEXT)
        self.assertEqual(len(o), 4)  # the stray "1. ..." further down must be ignored
        self.assertEqual((o[0]["turn"], o[0]["timing"], o[0]["race"]),
                         ("12", "Junior Class, Late June", "Turf, 2000m, Medium"))
        self.assertEqual((o[1]["turn"], o[1]["timing"], o[1]["race"]),
                         ("27", "Classic Class, Early February", "G3, Turf, 1800m, Mile"))
        self.assertEqual(o[2]["race"], "G1, Turf, 2400m, Medium")
        self.assertEqual((o[3]["turn"], o[3]["timing"], o[3]["race"]), ("44", "Classic Class, Late October", None))

    def test_missing_json_is_reported_not_crashing(self):
        msgs = []
        self.assertIsNone(v2.parse_version_page("<html><h1>x</h1></html>", "1", "u", msgs.append))
        self.assertTrue(msgs and "no usable itemData" in msgs[0])

    def test_render_with_json_version(self):
        v = v2.parse_version_page(make_html(), "100101", "https://x/100101-special-week", print)
        md = g.render("Special Week", "special-week", "1001", g.parse_profile([], None), [v], [], datetime.date(2026, 9, 30))
        for needle in ["| 5 star | 102 | 108 | 120 | 110 | 110 |", "Stamina 20%, Wit 10%", "| Turf | A |",
                       "| 1 | Participate in the Junior Make Debut | 12 | Junior Class, Late June | Turf, 2000m, Medium |"]:
            self.assertIn(needle, md)


if __name__ == "__main__":
    unittest.main()
