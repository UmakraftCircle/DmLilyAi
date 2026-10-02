"""Tests for the sandbox table tool. No network: the sandbox is faked and runs the real script locally."""
import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "LilyAiGameSpace" / "sandbox_scripts" / "docs_table_ops.py"

spec = importlib.util.spec_from_file_location("docs_table_ops", SCRIPT)
ops = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ops)

DOC = """## Cards
| Card | Rarity | Friendship | Race Bonus |
| --- | --- | --- | --- |
| Kitasan Black | SSR | 1,200 | 10 |
| Super Creek | SSR | 900 | 5 |
| Ines Fujin | R | 100 | n/a |
"""


def test_top_and_stat():
    assert "Kitasan Black" in ops.run(DOC, {"op": "top", "column": "Friendship", "n": 1})["text"]
    assert "= 15" in ops.run(DOC, {"op": "stat", "agg": "sum", "column": "Race Bonus"})["text"]
    r = ops.run(DOC, {"op": "stat", "agg": "avg", "column": "Friendship", "where_column": "Rarity", "where_value": "SSR"})
    assert "= 1050" in r["text"]


def test_compare_shows_difference():
    r = ops.run(DOC, {"op": "compare", "names": "Kitasan Black, Super Creek", "columns": "Card,Friendship"})
    assert "= -300" in r["text"]


def test_errors_are_reported_not_raised():
    assert ops.run(DOC, {"op": "stat", "agg": "sum", "column": "Nope"})["ok"] is False
    assert ops.run("no tables here", {"op": "table"})["ok"] is False
    assert ops.run(DOC, {"op": "rm -rf"})["ok"] is False


class _FakeFS:
    def __init__(self, files):
        self.files = files

    def write(self, path, content):
        self.files[path] = content


class _Res:
    def __init__(self, stdout, exit_code=0, stderr=""):
        self.stdout, self.exit_code, self.stderr = stdout, exit_code, stderr


class _FakeSandbox:
    """Runs the real script against the uploaded files, like the microVM would."""

    killed = 0

    def __init__(self):
        self.files = {}
        self.filesystem = _FakeFS(self.files)

    def exec(self, cmd, timeout_seconds=30):
        text, params = self.files["/workspace/input.md"], json.loads(self.files["/workspace/params.json"])
        return _Res(json.dumps(ops.run(text, params)))

    def kill(self):
        type(self).killed += 1


def test_runner_uses_sandbox_and_always_kills():
    pytest.importorskip("LilyAiCore.Logging.logger")
    from LilyAiGameSpace import sandbox_runner as sr

    sr._cache.clear()
    out = sr.run_table_op(DOC, {"op": "top", "column": "Friendship", "n": 1},
                          sandbox_factory=lambda template, ttl: _FakeSandbox())
    assert "Kitasan Black" in out
    assert _FakeSandbox.killed >= 1
    with pytest.raises(sr.SandboxError):
        sr.run_table_op(DOC, {"op": "stat", "agg": "sum", "column": "Nope"},
                        sandbox_factory=lambda template, ttl: _FakeSandbox())
