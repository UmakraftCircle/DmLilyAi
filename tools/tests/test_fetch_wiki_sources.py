import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

import fetch_wiki_sources as f  # noqa: E402

STUB = """# Air Shakur

## Overview

Not filled in yet.

## Background

Not filled in yet.

## Profile details (game)

| a | b |

## Appearances

Not filled in yet.

---

## Game data
"""

PARTLY = """# Some Uma

## Overview

She is a student at Tracen Academy.

## Background

Not filled in yet.

## Appearances

- Anime cameo.

---
"""

FILLED = PARTLY.replace("Not filled in yet.", "Kind and calm.")

WIKITEXT = """{{Infobox|name=Air Shakur}}
'''Air Shakur''' is a character.

== Biography ==
She is [[logical|logical]] and eccentric.<ref>note</ref>

== Appearance ==
Silver hair.

== Relationships ==
=== Friends ===
* [[Air Messiah]] - underclassman

== Media Appearances ==
* [[Beginning of a New Era]] (Cameo)

== Trivia ==
* Likes soccer.

== External Links ==
x
"""


class BlankCheck(unittest.TestCase):
    def test_all_blank(self):
        self.assertEqual(f.blank_sections(STUB), ["Overview", "Background", "Appearances"])

    def test_only_blank_ones_are_reported(self):
        self.assertEqual(f.blank_sections(PARTLY), ["Background"])

    def test_all_filled_is_skipped(self):
        self.assertEqual(f.blank_sections(FILLED), [])

    def test_missing_heading_counts_as_blank(self):
        self.assertEqual(f.blank_sections("# X\n\n## Overview\n\nText.\n"), ["Background", "Appearances"])

    def test_other_sections_do_not_leak_in(self):
        # The stub's profile table must not be read as part of Overview or Background.
        self.assertEqual(f.section_body(STUB, "Background").strip(), "Not filled in yet.")

    def test_title_candidates(self):
        self.assertEqual(f.wiki_title(STUB, "Air_Shakur"), ["Air_Shakur"])
        self.assertEqual(f.wiki_title("# K.S.Miracle\n", "KS_Miracle"), ["K.S.Miracle", "KS_Miracle"])

    def test_only_names_are_normalised(self):
        for typed in ("Air_Shakur", "Air Shakur", "air shakur", " air_shakur.md ", "Air-Shakur"):
            self.assertEqual(f.norm_name(typed), "air_shakur")


class WikitextParsing(unittest.TestCase):
    def test_split_keeps_subsections_in_parent(self):
        lead, secs = f.split_sections(WIKITEXT)
        titles = [t for t, _ in secs]
        self.assertEqual(titles, ["Biography", "Appearance", "Relationships", "Media Appearances", "Trivia", "External Links"])
        rel = dict(secs)["Relationships"]
        self.assertIn("=== Friends ===", rel)
        self.assertIn("Infobox", lead)

    def test_pick_by_target(self):
        _, secs = f.split_sections(WIKITEXT)
        self.assertEqual([t for t, _ in f.pick_sections(secs, ["Appearances"])],
                         ["Appearance", "Media Appearances", "Trivia"])
        self.assertEqual([t for t, _ in f.pick_sections(secs, ["Overview"])], ["Biography"])
        self.assertEqual([t for t, _ in f.pick_sections(secs, ["Background"])],
                         ["Biography", "Relationships", "Trivia"])

    def test_clean_text(self):
        self.assertEqual(f.clean_text("She is [[logical|logical]] and [[Vivlos]].<ref>n</ref> '''Bold'''"),
                         "She is logical and Vivlos. Bold")
        self.assertNotIn("{{", f.clean_text("{{Infobox|a={{x}}}} text", strip_templates=True))

    def test_staged_file_lists_only_needed_sections(self):
        text = f.build_staged("Air_Shakur", "path.md", ["Appearances"], "Air_Shakur", WIKITEXT, "IRL:Air_Shakur", None)
        self.assertIn("## Media Appearances", text)
        self.assertNotIn("## Lead", text)
        self.assertNotIn("## Biography", text)


if __name__ == "__main__":
    unittest.main()
