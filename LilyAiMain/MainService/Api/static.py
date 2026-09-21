"""Serves the web client (LilyAiFrontend) from the same process as the API, so one URL is the whole site."""
from pathlib import Path

# The only client folders that may be served. Nothing else in the repo is reachable over HTTP.
SERVED_DIRS = frozenset({"Public", "Assets", "Shared", "Home", "Chat", "Dashboard", "Settings", "Admin"})


def default_frontend_dir() -> Path:
    return Path(__file__).resolve().parents[3] / "LilyAiFrontend"


def resolve_static(root: Path, url_path: str) -> Path | None:
    """Map a URL path to a file inside an allowed client folder, or None. Blocks traversal."""
    rel = url_path.strip("/")
    if rel in {"", "index.html"}:
        rel = "Public/index.html"
    if rel.split("/", 1)[0] not in SERVED_DIRS:
        return None
    root = root.resolve()
    target = (root / rel).resolve()
    try:
        parts = target.relative_to(root).parts
    except ValueError:
        return None
    if not parts or parts[0] not in SERVED_DIRS:  # e.g. Assets/../server.py
        return None
    return target if target.is_file() else None
