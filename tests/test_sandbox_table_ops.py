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

CALC_SCRIPT = ROOT / "LilyAiGameSpace" / "sandbox_scripts" / "game_calcs.py"
cspec = importlib.util.spec_from_file_location("game_calcs", CALC_SCRIPT)
calcs = importlib.util.module_from_spec(cspec)
cspec.loader.exec_module(calcs)

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
        params = json.loads(self.files["/workspace/params.json"])
        if "game_calcs.py" in cmd:
            return _Res(json.dumps(calcs.run(params)))
        return _Res(json.dumps(ops.run(self.files["/workspace/input.md"], params)))

    def kill(self):
        type(self).killed += 1


def test_runner_uses_sandbox_and_always_kills():
    pytest.importorskip("LilyAiCore.Logging.logger")
    from LilyAiGameSpace import sandbox_runner as sr

    sr._cache.clear()
    out = sr.run_table_op(DOC, {"op": "top", "column": "Friendship", "n": 1},
                          sandbox_factory=lambda template, ttl, key: _FakeSandbox())
    assert "Kitasan Black" in out
    assert _FakeSandbox.killed >= 1
    with pytest.raises(sr.SandboxError):
        sr.run_table_op(DOC, {"op": "stat", "agg": "sum", "column": "Nope"},
                        sandbox_factory=lambda template, ttl, key: _FakeSandbox())


class _RateLimited(Exception):
    status_code = 429


def test_multiple_keys_rotate_and_skip_a_limited_key(monkeypatch):
    pytest.importorskip("LilyAiCore.Logging.logger")
    from LilyAiGameSpace import sandbox_runner as sr

    monkeypatch.setenv("PANDASTACK_API_KEY", " k1, k2 ,k2,k3,k4,k5,k6,k7 ")
    assert sr.load_keys() == ["k1", "k2", "k3", "k4", "k5", "k6"]   # trimmed, de-duplicated, max 6

    monkeypatch.setenv("PANDASTACK_API_KEY", "k1,k2")
    sr._pool = sr._KeyPool()
    used = []

    def factory(template, ttl, key):
        used.append(key)
        if key == "k1":
            raise _RateLimited("too many requests")
        return _FakeSandbox()

    sr._cache.clear()
    assert "Kitasan Black" in sr.run_table_op(DOC, {"op": "top", "column": "Friendship", "n": 1}, sandbox_factory=factory)
    assert used == ["k1", "k2"]                 # k1 failed, k2 answered in the same call
    used.clear()
    sr._cache.clear()
    sr.run_table_op(DOC, {"op": "top", "column": "Friendship", "n": 2}, sandbox_factory=factory)
    assert used == ["k2"]                       # k1 is resting, so it is not tried again


# ---- calculators: every expected number below is a worked example printed in the guide docs ----
def _calc(name, **inputs):
    r = calcs.run({"calculator": name, "inputs": inputs})
    assert r["ok"], r.get("error")
    return r["text"]


def test_legacy_blue_bonus_matches_doc_example():
    sparks = [{"stat": "Speed", "stars": 3}, {"stat": "Speed", "stars": 2}] + [{"stat": "Speed", "stars": 1}] * 4
    assert "= 53" in _calc("legacy_blue_bonus", sparks=sparks)          # Legacy.md: 21+12+5+5+5+5 = 53


def test_pvp_score_matches_doc_examples():
    # PvpTeamTrials.md: 10,000 base + 20% opponent + 5% support = 12,500
    assert "12,500" in _calc("pvp_score", opponent_bonus_pct=20, support_bonus_pct=5, characters=[{"position": 1}])
    # 60% opponent bonus and a won match = 16,000 for the victory
    wins = [{"won": True, "characters": [{"position": 4}]}] * 3
    assert "16,000" in _calc("pvp_score", opponent_bonus_pct=60, races=wins)


def test_pvp_rush_penalty_ignores_modifiers():
    text = _calc("pvp_score", opponent_bonus_pct=50, characters=[{"position": 2, "rush_seconds": 4}])
    assert "x1.50 = 12,000 - 900 rush = 11,100" in text


def test_race_mechanics_examples():
    assert "1,350" in _calc("stat_effective", stat=1500, which="speed")        # 1500 counts as 1350
    assert "+2.25%" in _calc("speed_boost", bonus_ms=0.45)                     # 0.45 m/s on 20 m/s
    assert "400m - 1,600m" in _calc("race_phases", distance=2400)              # the doc's 2400m table
    assert "167m - 667m" in _calc("race_phases", distance=1000)                # the doc's 1000m table
    assert "0%" in _calc("start_delay", multiplier=0.4).split("Late start")[1][:30]   # Concentration: no late starts


def test_unknown_things_are_refused_not_guessed():
    assert calcs.run({"calculator": "compatibility", "inputs": {}})["ok"] is False
    assert calcs.run({"calculator": "wit_effectiveness", "inputs": {"wit": 500, "strategy_aptitude": "B"}})["ok"] is False
    assert calcs.run({"calculator": "pvp_score", "inputs": {"characters": [{"position": 1, "margin": "4.5"}]}})["ok"] is False


def test_run_calc_goes_through_the_sandbox_and_kills_it():
    pytest.importorskip("LilyAiCore.Logging.logger")
    from LilyAiGameSpace import sandbox_runner as sr

    sr._cache.clear()
    before = _FakeSandbox.killed
    out = sr.run_calc("blue_spark_odds", {"final_stat": 700}, sandbox_factory=lambda template, ttl, key: _FakeSandbox())
    assert "50%" in out and _FakeSandbox.killed == before + 1
    with pytest.raises(sr.SandboxError):
        sr.run_calc("compatibility", {}, sandbox_factory=lambda template, ttl, key: _FakeSandbox())
