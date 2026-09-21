"""The web client is served by the API; make sure only client files are reachable."""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from LilyAiMain.MainService.Api.static import SERVED_DIRS, default_frontend_dir, resolve_static  # noqa: E402


class StaticTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp())
        for rel in ["Public/index.html", "Shared/app.js", "Admin/Relay/relay.js", "Assets/styles/tokens.css", "server.py", "secrets.txt", "data/db.sqlite3"]:
            f = self.root / rel
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_text("x")

    def test_serves_client_files(self):
        for url, rel in [("/", "Public/index.html"), ("", "Public/index.html"), ("/index.html", "Public/index.html"),
                         ("/Shared/app.js", "Shared/app.js"), ("Admin/Relay/relay.js", "Admin/Relay/relay.js"),
                         ("/Assets/styles/tokens.css", "Assets/styles/tokens.css")]:
            self.assertEqual(resolve_static(self.root, url), (self.root / rel).resolve(), url)

    def test_blocks_everything_else(self):
        for url in ["/server.py", "/secrets.txt", "/data/db.sqlite3", "/Assets/../secrets.txt", "/Assets/../../etc/passwd",
                    "/../secrets.txt", "/Shared/../server.py", "/Shared/nope.js", "/Shared", "/Admin/"]:
            self.assertIsNone(resolve_static(self.root, url), url)

    def test_real_frontend_folder_is_complete(self):
        root = default_frontend_dir()
        self.assertIsNotNone(resolve_static(root, "/"))
        self.assertIsNotNone(resolve_static(root, "/Shared/app.js"))
        # every module the router imports must resolve
        import re
        routes = (root / "Shared" / "routes.js").read_text()
        for path in re.findall(r'import\("(/[^"]+)"\)', routes):
            self.assertIsNotNone(resolve_static(root, path), path)
        # no non-client files at the top level of the frontend folder besides the README
        extras = {p.name for p in root.iterdir()} - SERVED_DIRS - {"README.md"}
        self.assertEqual(extras, set())


if __name__ == "__main__":
    unittest.main()
