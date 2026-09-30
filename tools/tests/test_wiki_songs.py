import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

import fetch_wiki_sources as f  # noqa: E402

RENDERED = (
    '<h2><span class="mw-headline" id="Media_Appearances">Media Appearances</span></h2><ul><li>Anime</li></ul>'
    '<h2><span class="mw-headline" id="Song_Discography">Song Discography</span></h2>'
    '<table class="wikitable"><tr><th>Song</th><th>Album</th><th>Type</th></tr>'
    '<tr><td><a href="/Gift">Gift (Game Size)</a></td><td><a href="/x">Solo Vocal &amp; Talk</a></td><td><b>Ver.</b></td></tr>'
    '<tr><td>Unite!!</td><td>WINNING LIVE 19</td><td>Group</td></tr></table>'
    '<h2><span class="mw-headline" id="Trivia">Trivia</span></h2><ul><li>x</li></ul>'
)

PAGE = "'''X''' is a character.\n\n== Song Discography ==\n{{Character_Discography}}\n\n== Trivia ==\n* Likes soccer.\n"


class Songs(unittest.TestCase):
    def test_extract_section_only(self):
        text = f.extract_rendered_section(RENDERED, "Song_Discography")
        self.assertEqual(text.splitlines(), [
            "Song | Album | Type",
            "Gift (Game Size) | Solo Vocal & Talk | Ver.",
            "Unite!! | WINNING LIVE 19 | Group",
        ])
        self.assertNotIn("Anime", text)
        self.assertNotIn("Likes", text)

    def test_missing_section_returns_none(self):
        self.assertIsNone(f.extract_rendered_section(RENDERED, "Nope"))

    def test_template_detected_with_space_or_underscore(self):
        self.assertTrue(f.DISCO_TEMPLATE.search("{{Character_Discography}}"))
        self.assertTrue(f.DISCO_TEMPLATE.search("{{ Character Discography|x=1}}"))

    def test_staged_uses_expanded_songs(self):
        text = f.build_staged("X", "p.md", ["Appearances"], "X", PAGE, "IRL:X", None, "Song | Album | Type\nUnite!! | WL19 | Group")
        self.assertIn("Unite!! | WL19 | Group", text)
        self.assertNotIn("{{Character_Discography}}", text)

    def test_staged_notes_missing_songs(self):
        text = f.build_staged("X", "p.md", ["Appearances"], "X", PAGE, "IRL:X", None, None)
        self.assertIn("songs are missing", text)
        self.assertNotIn("{{Character_Discography}}", text)

    def test_section_sizes(self):
        text = f.build_staged("X", "p.md", ["Appearances"], "X", PAGE, "IRL:X", None, "a | b")
        self.assertIn("Song Discography (", f.section_sizes(text))


if __name__ == "__main__":
    unittest.main()
