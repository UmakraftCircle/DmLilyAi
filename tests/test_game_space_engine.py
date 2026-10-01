"""Umamusume docs engine: name resolution, section reads, search, chat pre-lookup.

Run:  python -m unittest discover -s tests -v
"""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from LilyAiGameSpace.UmamusumeGameSpaceEngine import UmamusumeGameSpaceEngine  # noqa: E402

SPECIAL_WEEK = """# Special Week

**Japanese name:** スペシャルウィーク (Supesharu Wīku)

## Overview

Bright country girl from Hokkaido. ![art](https://x/y.png)

## Game data: versions

### Version 1: Special Week [Special Dreamer] (Original)

**Unique skill:** late-race speed boost after overtaking.

### Version 3: Special Week (Commander) [Ruler of Japan]

**Unique skill:** velocity boost at Nakayama Racecourse.

## Sources

| Source | URL |
|---|---|
| GameTora | https://gametora.com/umamusume/characters/special-week |

## Images

| d | u |
|---|---|
| art | https://gametora.com/images/a.png |
"""

RACE_LIST = "# Race List\n\n## Senior Year\n\n| Slot | Race |\n|---|---|\n| Late December | Arima Kinen |\n"


class GameSpaceEngineTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        (root / "Character").mkdir()
        (root / "Guide" / "RaceList").mkdir(parents=True)
        (root / "Character" / "Special_Week.md").write_text(SPECIAL_WEEK, encoding="utf-8")
        (root / "Guide" / "RaceList" / "Racelist.md").write_text(RACE_LIST, encoding="utf-8")
        self.engine = UmamusumeGameSpaceEngine(root, refresh_interval=0)

    def tearDown(self):
        self.tmp.cleanup()

    def test_resolve_by_name_alias_japanese_and_typo(self):
        for ref in ("Special Week", "special_week", "Character/Special_Week", "スペシャルウィーク",
                    "special week commander", "specal week"):
            self.assertEqual(self.engine.resolve(ref).id, "Character/Special_Week", ref)
        self.assertEqual(self.engine.resolve("race list").id, "Guide/RaceList/Racelist")
        self.assertIsNone(self.engine.resolve("nonexistent thing"))

    def test_read_section_hides_images_and_returns_sources(self):
        r = self.engine.read("Special Week", "Version 3")
        self.assertIn("Nakayama", r.text)
        self.assertNotIn("late-race", r.text)
        self.assertEqual(r.sources, ["https://gametora.com/umamusume/characters/special-week"])
        whole = self.engine.read("Special Week").text
        self.assertNotIn("gametora.com/images", whole)
        self.assertIn("art", whole)  # image reduced to its alt text
        self.assertIsNone(self.engine.read("Special Week", "images").section)

    def test_search_ranks_sections(self):
        hit = self.engine.search("special week unique skill nakayama")[0]
        self.assertIn("Version 3", hit.section)
        self.assertEqual(self.engine.search("arima kinen")[0].doc_id, "Guide/RaceList/Racelist")
        self.assertEqual(self.engine.search("the of"), [])

    def test_context_for_only_when_a_doc_is_named(self):
        self.assertEqual(self.engine.context_for("thanks!"), [])
        self.assertEqual(self.engine.context_for("special weekly report please"), [])
        snippets = self.engine.context_for("how good is Special Week's Commander version at Nakayama?")
        self.assertTrue(snippets and "Nakayama" in snippets[0] and "(game docs)" in snippets[0])
        self.assertLessEqual(sum(len(s) for s in self.engine.context_for("tell me about special week")), 1500)
        self.assertTrue(self.engine.context_for("スペシャルウィークの強さは?"))

    def test_picks_up_changed_and_removed_files(self):
        path = Path(self.tmp.name) / "Character" / "Silence_Suzuka.md"
        path.write_text("# Silence Suzuka\n\nSenior of Special Week.\n", encoding="utf-8")
        self.assertEqual(self.engine.resolve("silence suzuka").id, "Character/Silence_Suzuka")
        path.unlink()
        self.assertIsNone(self.engine.resolve("silence suzuka"))


if __name__ == "__main__":
    unittest.main()
