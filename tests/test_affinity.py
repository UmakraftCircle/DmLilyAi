"""Affinity tests. No network. The data-layout checks run on the real file when it is in the repo, and are skipped otherwise."""
import importlib.util
import itertools
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("affinity_calc", ROOT / "LilyAiGameSpace" / "sandbox_scripts" / "affinity_calc.py")
ac = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ac)

NAMES = {1: "Alpha", 2: "Beta", 3: "Gamma", 4: "Delta", 5: "Echo"}


def make_data():
    """5 characters. Pair ratings are a made-up symmetric table; each triple is min(pairs) - 1 (never above a pair)."""
    chars = [1, 2, 3, 4, 5]
    n = len(chars)
    pair = {(a, b): 10 + (a * 7 + b * 7 + a * b) % 25 for a in chars for b in chars if a < b}
    p = lambda a, b: 0 if a == b else pair[(min(a, b), max(a, b))]
    aff2 = [p(a, b) for a in chars for b in chars]

    def t(a, b, c):
        if len({a, b, c}) < 3:
            return 0
        return max(0, min(p(a, b), p(a, c), p(b, c)) - 1)

    aff3 = [t(a, b, c) for a in chars for b in chars for c in chars]
    return {"chars": chars, "aff2": aff2, "aff3": aff3}, p, t


def test_total_follows_the_formula_and_tiers():
    raw, p, t = make_data()
    out = ac.run({"op": "total", "main": 1, "legacy1": 2, "legacy2": 3, "sub11": 4, "sub21": 5, "names": NAMES}, raw)
    assert out["ok"], out
    expected = p(1, 2) + p(1, 3) + p(2, 3) + t(1, 2, 4) + t(1, 3, 5)
    assert f"Base total: {expected}" in out["text"]
    low = ac.run({"op": "total", "main": 1, "legacy1": 2, "names": NAMES}, raw)["text"]
    assert "triangle" in low                                   # 50 or less
    assert "double circle" in ac.run({"op": "total", "main": 1, "legacy1": 2, "bonus": 140, "names": NAMES}, raw)["text"]
    assert ac.tier(50) != ac.tier(51) and ac.tier(150) != ac.tier(151)


def test_rejects_bad_setups():
    raw, _, _ = make_data()
    assert ac.run({"op": "total", "main": 1, "legacy1": 1}, raw)["ok"] is False          # her own legacy
    assert ac.run({"op": "total", "main": 1, "sub11": 2}, raw)["ok"] is False             # no legacy at all
    assert ac.run({"op": "total", "main": 1, "legacy1": 99}, raw)["ok"] is False          # not in the data


def test_best_is_a_true_maximum():
    raw, p, t = make_data()
    out = ac.run({"op": "best", "main": 1, "top": 1, "names": NAMES}, raw)
    assert out["ok"], out
    others = [2, 3, 4, 5]

    def best2(leg):
        return sum(sorted((t(1, leg, s) for s in others if s != leg), reverse=True)[:2])

    brute = max(p(1, a) + p(1, b) + p(a, b) + best2(a) + best2(b) for a, b in itertools.combinations(others, 2))
    assert out["text"].splitlines()[1].startswith(f"1. {brute} ")


def real_file():
    path = ROOT / "LilyAiGameSpace" / "affinity_data" / "affinity.json"
    if not path.is_file():
        pytest.skip("affinity.json is not in the repo yet")
    return json.loads(path.read_text(encoding="utf-8"))


def test_real_file_layout():
    raw = real_file()
    n = len(raw["chars"])
    assert len(raw["aff2"]) == n * n and len(raw["aff3"]) == n ** 3
    a2, a3 = raw["aff2"], raw["aff3"]
    assert all(a2[i * n + i] == 0 for i in range(n))
    assert all(a2[i * n + j] == a2[j * n + i] for i in range(n) for j in range(n))
    for i, j, k in itertools.combinations(range(n), 3):
        triple = a3[(i * n + j) * n + k]
        assert triple == a3[(k * n + j) * n + i] == a3[(j * n + i) * n + k]               # symmetric
        assert triple <= min(a2[i * n + j], a2[i * n + k], a2[j * n + k])                 # a group holding all three holds each pair


def test_names_cover_the_real_file():
    raw = real_file()
    names = json.loads((ROOT / "LilyAiGameSpace" / "affinity_data" / "affinity_names.json").read_text(encoding="utf-8"))
    assert {str(c) for c in raw["chars"]} == set(names)
