"""Fixed game calculators. Runs INSIDE a PandaStack sandbox, never in the bot. Standard library only.

LilyAi uploads /workspace/params.json = {"calculator": "...", "inputs": {...}} and runs this file.
It prints one JSON object: {"ok": true, "text": "..."} or {"ok": false, "error": "..."}.
The model only supplies inputs. It never supplies code.

Every rule below is copied from the guide docs in LilyAiGameSpace/Umamusume/Guide and tagged with its source.
Where a doc is ambiguous the calculator says which assumption it made. Where the docs give no number
(e.g. the compatibility formula) there is deliberately NO calculator: nothing is guessed.

    Legacy:   Guide/Uma Musume Legacies/Legacy.md            -> legacy_blue_bonus, blue_spark_odds, white_spark_odds
    PvP:      Guide/Team Trials PvP Scoring System/PvpTeamTrials.md   -> pvp_score, start_delay, rush_duration
    Race:     Guide/Race Mechanics Handbook/RaceMechanicHandBook.md   -> stat_effective, wit_effectiveness,
                                                      race_phases, length_convert, speed_boost, acceleration_gain
"""
from __future__ import annotations

import json
import math
import re
import sys
from fractions import Fraction
from pathlib import Path

PARAMS = Path("/workspace/params.json")


class CalcError(Exception):
    pass


# ----------------------------------------------------------------------------- helpers
def n(x, name, lo=None, hi=None, integer=False, default=None):
    """Coerce an input to a number and range-check it."""
    if x is None or x == "":
        if default is not None:
            return default
        raise CalcError(f"{name} is required")
    if isinstance(x, bool):
        raise CalcError(f"{name} must be a number")
    try:
        v = float(str(x).replace(",", "").strip().rstrip("%"))
    except ValueError:
        raise CalcError(f"{name} must be a number, got {x!r}")
    if integer:
        if v != int(v):
            raise CalcError(f"{name} must be a whole number")
        v = int(v)
    if lo is not None and v < lo:
        raise CalcError(f"{name} must be at least {lo}")
    if hi is not None and v > hi:
        raise CalcError(f"{name} must be at most {hi}")
    return v


def truthy(x) -> bool:
    if isinstance(x, str):
        return x.strip().lower() in ("1", "true", "yes", "y", "on")
    return bool(x)


def num(v: float) -> str:
    v = round(v, 2)
    if v == int(v):
        return f"{int(v):,}"
    return f"{v:,.2f}".rstrip("0").rstrip(".")


def pct(p: float) -> str:
    return f"{p * 100:.2f}".rstrip("0").rstrip(".") + "%"


def need_list(x, name):
    if not isinstance(x, list) or not x:
        raise CalcError(f"{name} must be a non-empty list")
    return x


# ----------------------------------------------------------------------------- legacy (Legacy.md)
BLUE_BONUS = {1: 5, 2: 12, 3: 21}                      # "Blue spark" stat bonus table
STATS = {"speed": "Speed", "stamina": "Stamina", "power": "Power", "guts": "Guts", "wit": "Wit"}


def _stat(name) -> str:
    key = str(name).strip().lower()
    if key not in STATS:
        raise CalcError(f"stat must be one of {', '.join(STATS.values())}, got {name!r}")
    return STATS[key]


def calc_legacy_blue_bonus(i: dict) -> str:
    """Start-of-Career stat bonus from blue sparks. Additive over the legacies and sub-legacies."""
    sparks = need_list(i.get("sparks"), "sparks (list of {stat, stars})")
    if len(sparks) > 6:
        raise CalcError("a trainee has 2 legacies + 4 sub-legacies = at most 6 blue sparks")
    totals: dict[str, list[int]] = {}
    for s in sparks:
        if not isinstance(s, dict):
            raise CalcError("each spark must look like {\"stat\": \"Speed\", \"stars\": 3}")
        stars = n(s.get("stars"), "stars", 1, 3, integer=True)
        totals.setdefault(_stat(s.get("stat")), []).append(BLUE_BONUS[stars])
    lines = [f"- {st}: {' + '.join(str(b) for b in bs)} = {sum(bs)}" for st, bs in totals.items()]
    return ("Blue spark start bonus (+5 / +12 / +21 for 1/2/3 stars, added together):\n" + "\n".join(lines)
            + f"\nTotal across stats: {sum(sum(b) for b in totals.values())}")


def calc_blue_spark_odds(i: dict) -> str:
    """Star odds of the blue spark a finished Career generates, by the final value of the rolled stat."""
    stat = n(i.get("final_stat"), "final_stat", 0)
    if stat < 600:
        odds = {1: 0.90, 2: 0.10, 3: 0.0}
    elif stat <= 1100:
        odds = {1: 0.50, 2: 0.45, 3: 0.05}
    else:
        odds = {1: 0.20, 2: 0.70, 3: 0.10}
    exp_bonus = sum(p * BLUE_BONUS[s] for s, p in odds.items())
    return (f"Blue spark star odds at final stat {num(stat)}: 1\u2605 {pct(odds[1])}, 2\u2605 {pct(odds[2])}, "
            f"3\u2605 {pct(odds[3])}.\nExpected start bonus if used as a legacy: {num(exp_bonus)} "
            f"(1\u2605 +5, 2\u2605 +12, 3\u2605 +21). Bands: under 600, 600-1100, over 1100.")


WHITE_RATES = [("normal_skills", "normal skill", 0.20), ("double_circle_skills", "\u25ce skill", 0.25),
               ("gold_skills", "gold (rare) skill", 0.40), ("g1_wins", "G1 race win", 0.20)]
WHITE_STARS = {1: 0.50, 2: 0.45, 3: 0.05}


def calc_white_spark_odds(i: dict) -> str:
    """Chance of white sparks at the end of a Career: per skill / G1 win / the Career itself."""
    chances: list[tuple[str, int, float]] = []
    for key, label, p in WHITE_RATES:
        count = n(i.get(key), key, 0, integer=True, default=0)
        if count:
            chances.append((label, count, p))
    if truthy(i.get("career", True)):
        chances.append(("Career itself", 1, 0.20))
    if not chances:
        raise CalcError("give at least one of normal_skills, double_circle_skills, gold_skills, g1_wins")
    expected = sum(c * p for _, c, p in chances)
    p_none = math.prod((1 - p) ** c for _, c, p in chances)
    lines = [f"- {c} x {label} at {pct(p)} each" for label, c, p in chances]
    star_line = ", ".join(f"{s}\u2605 {num(expected * q)}" for s, q in WHITE_STARS.items())
    return ("White spark odds (base rates; SS rank or higher raises the 2\u2605/3\u2605 odds but the docs give no numbers):\n"
            + "\n".join(lines) + f"\nExpected white sparks: {num(expected)}  ({star_line})"
            f"\nChance of at least one: {pct(1 - p_none)}  |  none: {pct(p_none)}"
            f"\nStar split per spark: 1\u2605 50%, 2\u2605 45%, 3\u2605 5%.")


# ----------------------------------------------------------------------------- PvP (PvpTeamTrials.md)
POSITION_PTS = {1: 10000, 2: 8000, 3: 7000, 4: 6000, 5: 5000, 6: 4000, 7: 4000, 8: 3000, 9: 3000, 10: 2000, 11: 2000, 12: 2000}
MARGIN_PTS = {"distance": 3000, "nose": 5000, "head": 3000, "neck": 2000,
              Fraction(1, 2): 1000, Fraction(3, 4): 1100, Fraction(1): 1200, Fraction(5, 4): 1300, Fraction(3, 2): 1400,
              Fraction(7, 4): 1500, Fraction(2): 1600, Fraction(5, 2): 1700, Fraction(3): 1800, Fraction(7, 2): 1900,
              Fraction(4): 2000, Fraction(5): 2100, Fraction(6): 2200, Fraction(7): 2300, Fraction(8): 2400,
              Fraction(9): 2500, Fraction(10): 2600}
UNIQUE_LOW = {1: 1500, 2: 1700, 3: 1800, 4: 1900, 5: 2000, 6: 2100, 7: 2200, 8: 2300, 9: 2400, 10: 2500}   # 1-2 star umas
UNIQUE_HIGH_EXTRA = 500                                                                                      # 3 star and up
NORMAL_SKILL, GOLD_SKILL = 500, 1200
ACE_PCT, POSITIONING_PTS, STRONG_START_PTS, DARK_HORSE_PTS = 10.0, 1000, 1000, 4000
RUSH_FLAT, RUSH_PER_SEC = 500, 100
VICTORY_PTS, TRIO_PTS, QUINELLA_PTS, ALL_PLACED_PTS = 10000, 5000, 3000, 4000


def parse_margin(m):
    if m is None or m == "":
        return None
    if isinstance(m, (int, float)) and not isinstance(m, bool):
        x = Fraction(str(m))
    else:
        s = re.sub(r"(?i)\blengths?\b", "", str(m)).strip().lower()
        named = {"nose": "nose", "head": "head", "neck": "neck", "distance": "distance", "dist": "distance",
                 "long shot": "distance", "longshot": "distance"}
        if s in named:
            return named[s]
        try:
            x = sum((Fraction(p) for p in s.split()), Fraction(0))
        except (ValueError, ZeroDivisionError):
            raise CalcError(f"margin {m!r} not understood. Use a number of lengths (e.g. 2.5 or '1 3/4') or neck/head/nose/distance")
    if x > 10:
        return "distance"            # "Long Shot" = more than ten lengths
    return x


def margin_points(m) -> tuple[int, str]:
    key = parse_margin(m)
    if key is None:
        return 0, ""
    if key not in MARGIN_PTS:
        raise CalcError(f"margin {m!r} isn't a listed value. Listed: 1/2, 3/4, 1, 1 1/4, 1 1/2, 1 3/4, 2, 2 1/2, 3, 3 1/2, 4-10 lengths, neck, head, nose, distance")
    return MARGIN_PTS[key], str(m)


def _character_score(c: dict, mods: dict, race_no: int) -> dict:
    pos = n(c.get("position"), "position", 1, 12, integer=True)
    parts: list[tuple[str, int]] = [(f"{pos}{'st' if pos == 1 else 'nd' if pos == 2 else 'rd' if pos == 3 else 'th'} place", POSITION_PTS[pos])]
    if pos == 1:
        mp, label = margin_points(c.get("margin"))
        if mp:
            parts.append((f"margin {label}", mp))
    ns, gs = n(c.get("normal_skills"), "normal_skills", 0, integer=True, default=0), n(c.get("gold_skills"), "gold_skills", 0, integer=True, default=0)
    if ns:
        parts.append((f"{ns} normal skill{'s' if ns > 1 else ''}", ns * NORMAL_SKILL))
    if gs:
        parts.append((f"{gs} gold skill{'s' if gs > 1 else ''}", gs * GOLD_SKILL))
    if c.get("unique_level") not in (None, "", 0):
        lvl = n(c.get("unique_level"), "unique_level", 1, 10, integer=True)
        stars = n(c.get("stars"), "stars", 1, 5, integer=True, default=1)
        acts = n(c.get("unique_activations"), "unique_activations", 0, integer=True, default=1)
        per = UNIQUE_LOW[lvl] + (UNIQUE_HIGH_EXTRA if stars >= 3 else 0)
        if acts:
            parts.append((f"unique Lv{lvl} ({stars}\u2605)" + (f" x{acts}" if acts > 1 else ""), per * acts))
    ph = n(c.get("positioning"), "positioning", 0, 2, integer=True, default=0)
    if ph:
        parts.append(("good positioning" + (" x2" if ph == 2 else ""), ph * POSITIONING_PTS))
    bt = n(c.get("beat_time_s"), "beat_time_s", 0, default=0)
    if bt >= 0.1:
        parts.append((f"beat standard time by {bt:g}s", min(20, int(bt * 10 + 1e-9)) * 100))
    if truthy(c.get("strong_start")):
        parts.append(("strong start", STRONG_START_PTS))
    dark = truthy(c.get("dark_horse"))
    if c.get("popularity") not in (None, ""):
        dark = n(c.get("popularity"), "popularity", 1, integer=True) >= 8 and pos <= 3
    if dark:
        parts.append(("dark horse", DARK_HORSE_PTS))
    base = sum(p for _, p in parts)
    ace = truthy(c.get("ace"))
    mod_pct = (ACE_PCT if ace else 0) + mods["opp"] + mods["support"] + mods["streak"]
    positive = base * (1 + mod_pct / 100)
    penalty = 0
    rs = c.get("rush_seconds")
    if truthy(c.get("rushed")) or (rs not in (None, "") and n(rs, "rush_seconds", 0) > 0):
        penalty = RUSH_FLAT + RUSH_PER_SEC * n(rs, "rush_seconds", 0, default=0)
    return {"name": c.get("name") or f"R{race_no} #{pos}", "pos": pos, "parts": parts, "base": base, "mod_pct": mod_pct,
            "positive": positive, "penalty": penalty, "total": positive - penalty, "ace": ace}


def calc_pvp_score(i: dict) -> str:
    races = i.get("races")
    if races is None and i.get("characters") is not None:
        races = [{"characters": i["characters"], "won": i.get("won")}]
    races = need_list(races, "races (list of {won, characters:[...]})")
    if len(races) > 5:
        raise CalcError("a Team Trials match has 5 races")
    opp, sup = n(i.get("opponent_bonus_pct"), "opponent_bonus_pct", 0, default=0), n(i.get("support_bonus_pct"), "support_bonus_pct", 0, default=0)
    out: list[str] = []
    grand, wins, streak = 0.0, 0, 0
    notes: list[str] = []
    for r_no, race in enumerate(races, 1):
        chars = need_list(race.get("characters"), f"race {r_no} characters")
        if len(chars) > 3:
            raise CalcError("a team fields at most 3 characters per race")
        won = race.get("won")
        if won is not None:
            if truthy(won):
                wins += 1
                streak += 1
            else:
                streak = 0
        streak_pct = n(race.get("win_streak"), "win_streak", 0, default=streak if truthy(won) else 0)
        mods = {"opp": opp, "support": sup, "streak": streak_pct}
        scored = [_character_score(c, mods, r_no) for c in chars]
        race_total = 0.0
        out.append(f"Race {r_no}" + ("" if won is None else (" (won)" if truthy(won) else " (lost)")) + f" - modifiers +{num(opp + sup + streak_pct)}% (+10% more for the ace):")
        for s in scored:
            m = s["mod_pct"]
            line = f"  {s['name']}: " + " + ".join(f"{num(p)} {lbl}" for lbl, p in s["parts"]) + f" = {num(s['base'])}"
            if m:
                line += f" x{1 + m / 100:.2f} = {num(s['positive'])}"
            if s["penalty"]:
                line += f" - {num(s['penalty'])} rush = {num(s['total'])}"
            out.append(line)
            race_total += s["total"]
        poss = sorted(s["pos"] for s in scored)
        team = 0
        if len(scored) == 3 and poss == [1, 2, 3]:
            team, label = TRIO_PTS, "1-2-3 sweep (Trio)"
        elif len(scored) == 2 and poss == [1, 2]:
            team, label = QUINELLA_PTS, "1st & 2nd (Quinella)"
        elif len(scored) == 3 and all(p <= 5 for p in poss):
            team, label = ALL_PLACED_PTS, "all members in the top 5"
        if team:
            out.append(f"  team bonus: {label} +{num(team)}")
            race_total += team
        out.append(f"  race total: {num(race_total)}")
        grand += race_total
    if wins >= 3:
        victory = VICTORY_PTS * (1 + opp / 100)
        out.append(f"Victory ({wins} races won): {num(VICTORY_PTS)} x{1 + opp / 100:.2f} (opponent bonus only) = {num(victory)}")
        grand += victory
    elif any(r.get("won") is not None for r in races):
        out.append(f"No victory bonus ({wins} races won, 3 needed).")
    out.append(f"MATCH TOTAL: {num(grand)}")
    notes.append("Assumed: Trio/Quinella/All-placed bonuses are flat (docs only say the opponent bonus applies to Victory); "
                 "win streak = N% on the Nth win in a row; rush penalties ignore modifiers.")
    return "\n".join(out) + "\n" + " ".join(notes)


def _uniform_late(mult: float, threshold: float, max_delay: float) -> float:
    return max(0.0, min(1.0, 1 - threshold / (max_delay * mult))) if mult > 0 else 0.0


def calc_start_delay(i: dict) -> str:
    """Start delay odds. Doc: a roll up to 0.1 s, uniform assumed; skills multiply the roll."""
    mult = n(i.get("multiplier"), "multiplier", 0, default=1.0)
    hi = 0.1 * mult
    p_strong = 1.0 if hi <= 0.02 else 0.02 / hi
    p_late = _uniform_late(mult, 0.066, 0.1)
    p_notice = _uniform_late(mult, 0.08, 0.1)
    return (f"Start delay odds with the roll multiplied by {mult:g} (max delay {hi:.3f}s, uniform roll assumed):\n"
            f"- Strong start (under 0.02s): {pct(p_strong)}  -> Team Trials +1,000 points, expected {num(1000 * p_strong)}\n"
            f"- Late start (0.066s or more): {pct(p_late)}\n- 'Late Start' indicator shown (0.08s or more): {pct(p_notice)}\n"
            f"Docs: Focus multiplies the delay by 0.9, golden Concentration by 0.4 (late starts become impossible).")


def calc_rush_duration(i: dict) -> str:
    """Rush length: every 3 s a 60% roll ends it; it ends by itself at 12 s (+ debuff extensions)."""
    ext = n(i.get("extension_s"), "extension_s", 0, default=0)
    cap = 12 + ext
    alive, exp, lines = 1.0, 0.0, []
    t = 3.0
    while t < cap:
        end = alive * 0.6
        exp += end * t
        lines.append(f"ends at {t:g}s: {pct(end)}")
        alive -= end
        t += 3
    exp += alive * cap
    lines.append(f"lasts the full {cap:g}s (roll or automatic end): {pct(alive)}")
    return (f"Rush duration (60% end roll every 3s, hard cap {cap:g}s; first roll assumed at 3s):\n- " + "\n- ".join(lines)
            + f"\nExpected duration {exp:.2f}s -> expected Team Trials penalty {num(RUSH_FLAT + RUSH_PER_SEC * exp)} points "
              f"(-500 flat, -100 per second, if a rush happens). Rushing uses 1.6x stamina.")


# ----------------------------------------------------------------------------- race mechanics
def _threshold_pct(excess: float) -> float:
    return 0.0 if excess <= 0 else min(20.0, 5.0 * math.ceil(excess / 300))


def calc_stat_effective(i: dict) -> str:
    stat_name = str(i.get("which") or "speed").strip().lower()
    if stat_name not in STATS:
        raise CalcError(f"which must be one of {', '.join(STATS)}")
    raw = n(i.get("stat"), "stat", 1, 2000)
    mood = n(i.get("mood"), "mood", -2, 2, integer=True, default=0)
    steps = [f"base {num(raw)}"]
    v = raw
    if truthy(i.get("career_run")):
        v += 400
        steps.append(f"+400 during a Career run = {num(v)}")
    if v > 1200:
        v = 1200 + (v - 1200) / 2
        steps.append(f"over 1200 counts half = {num(v)}")
    if mood:
        v *= 1 + 0.02 * mood
        steps.append(f"mood {mood:+d} ({mood * 2:+d}%) = {num(v)}")
    terrain, cond = str(i.get("terrain") or "").strip().lower(), str(i.get("condition") or "").strip().lower()
    flat = 0
    if cond and cond not in ("firm", "good", "soft", "heavy"):
        raise CalcError("condition must be firm, good, soft or heavy")
    if stat_name == "speed" and cond == "heavy":
        flat = -50
    if stat_name == "power" and terrain == "turf" and cond and cond != "firm":
        flat = -50
    if stat_name == "power" and terrain == "dirt" and cond:
        flat = -50 if cond == "good" else -100
    if flat:
        v += flat
        steps.append(f"{terrain or 'terrain'} {cond}: {flat} = {num(v)}")
    if stat_name == "speed" and i.get("threshold_excess") not in (None, ""):
        bonus = _threshold_pct(n(i.get("threshold_excess"), "threshold_excess", 0))
        if bonus:
            v *= 1 + bonus / 100
            steps.append(f"course threshold exceeded by {num(n(i.get('threshold_excess'), 'x'))}: +{bonus:g}% = {num(v)}")
    extra = "\nSoft/heavy ground also adds 2% HP use per second." if cond in ("soft", "heavy") else ""
    return (f"Effective {STATS[stat_name]} used by race mechanics: {num(v)}\n" + "\n".join(f"- {s}" for s in steps)
            + extra + "\nAssumed order: +400, halve above 1200, mood, terrain, threshold (the docs don't state the order). "
              "Threshold: +5% per started 300 over, max 20% (the docs' wording is ambiguous).")


WIT_APT = {"s": 1.10, "a": 1.0, "d": 0.60, "g": 0.10}


def calc_wit_effectiveness(i: dict) -> str:
    wit = n(i.get("wit"), "wit", 1)
    apt = str(i.get("strategy_aptitude") or "").strip().lower()
    if apt not in WIT_APT:
        raise CalcError("the docs only give S (+10%), A (unchanged), D (-40%) and G (-90%); B, C, E and F are not documented")
    return f"Wit {num(wit)} at {apt.upper()} strategy aptitude counts as {num(wit * WIT_APT[apt])} ({(WIT_APT[apt] - 1) * 100:+.0f}%)."


def calc_race_phases(i: dict) -> str:
    d = n(i.get("distance"), "distance", 1)
    s = d / 6
    rows = [("Early-Race", 0, s), ("Mid-Race", s, 4 * s), ("Late-Race", 4 * s, 5 * s), ("Last Spurt phase", 5 * s, d)]
    lines = [f"- {name}: {num(round(a))}m - {num(round(b))}m" for name, a, b in rows]
    return (f"Phases for a {num(d)}m race (one sixth = {s:.1f}m):\n" + "\n".join(lines)
            + f"\nMax distance in a non-normal Position Keep mode: {d / 24:.1f}m (Runaway {d / 8:.1f}m).")


def calc_length_convert(i: dict) -> str:
    if i.get("lengths") not in (None, ""):
        L = n(i.get("lengths"), "lengths", 0)
        tag = " (counts as 'Long Shot'/distance: over 10 lengths)" if L > 10 else ""
        return f"{L:g} horse lengths = {L * 2.5:g} m (1 length = 2.5 m in the game){tag}."
    m = n(i.get("meters"), "meters (or lengths)", 0)
    return f"{m:g} m = {m / 2.5:g} horse lengths (1 length = 2.5 m). Nose ~0.2m, Head ~0.4m, Neck ~0.8m."


def calc_speed_boost(i: dict) -> str:
    base = n(i.get("base_ms"), "base_ms", 0.1, default=20.0)
    bonus = n(i.get("bonus_ms"), "bonus_ms")
    return (f"+{bonus:g} m/s on a base of {base:g} m/s = +{bonus / base * 100:.2f}% ({base * 3.6:.1f} -> {(base + bonus) * 3.6:.1f} km/h). "
            "Docs baselines: 20 m/s early/mid race, 25 m/s last spurt.")


def calc_acceleration_gain(i: dict) -> str:
    v0, v1 = n(i.get("from_ms"), "from_ms", 0, default=20.0), n(i.get("to_ms"), "to_ms", 0, default=25.0)
    a0 = n(i.get("accel"), "accel (base m/s^2)", 0.01)
    bonus = n(i.get("accel_bonus"), "accel_bonus", 0)
    if v1 <= v0:
        raise CalcError("to_ms must be higher than from_ms")
    t0, t1 = (v1 - v0) / a0, (v1 - v0) / (a0 + bonus)
    gain = 0.5 * (v1 - v0) * (t0 - t1)
    return (f"Reaching {v1:g} m/s from {v0:g}: {t0:.2f}s at {a0:g} m/s^2, {t1:.2f}s at {a0 + bonus:g} m/s^2.\n"
            f"Gain on a runner without the bonus: {gain:.2f}m = {gain / 2.5:.2f} lengths (gain = half the speed step x time saved).\n"
            "The docs' own example rounds to 11s vs 7.5s and quotes 8.75m (3.5 lengths).")


CALCS = {
    "legacy_blue_bonus": (calc_legacy_blue_bonus, "sparks: [{stat, stars}] (up to 6) -> start stat bonus"),
    "blue_spark_odds": (calc_blue_spark_odds, "final_stat -> star odds of the blue spark"),
    "white_spark_odds": (calc_white_spark_odds, "normal_skills, double_circle_skills, gold_skills, g1_wins, career -> white spark odds"),
    "pvp_score": (calc_pvp_score, "races:[{won, characters:[{position, margin, ace, stars, unique_level, normal_skills, gold_skills, positioning, beat_time_s, strong_start, popularity, rush_seconds}]}], opponent_bonus_pct, support_bonus_pct"),
    "start_delay": (calc_start_delay, "multiplier (Focus 0.9, Concentration 0.4) -> strong/late start odds"),
    "rush_duration": (calc_rush_duration, "extension_s -> expected rush length and PvP penalty"),
    "stat_effective": (calc_stat_effective, "stat, which, mood(-2..2), career_run, terrain, condition, threshold_excess -> stat used in races"),
    "wit_effectiveness": (calc_wit_effectiveness, "wit, strategy_aptitude (S/A/D/G) -> effective wit"),
    "race_phases": (calc_race_phases, "distance -> phase boundaries in metres"),
    "length_convert": (calc_length_convert, "lengths or meters -> the other"),
    "speed_boost": (calc_speed_boost, "bonus_ms, base_ms -> % and km/h"),
    "acceleration_gain": (calc_acceleration_gain, "accel, accel_bonus, from_ms, to_ms -> time and metres gained"),
}


def calc_help(i: dict) -> str:
    return "Calculators:\n" + "\n".join(f"- {k}: {d}" for k, (_, d) in CALCS.items()) + \
           "\nNot available: compatibility (triangle/circle/double circle) - the formula isn't in the docs."


def run(params: dict) -> dict:
    name = str(params.get("calculator") or "").strip().lower()
    inputs = params.get("inputs")
    if isinstance(inputs, str):
        try:
            inputs = json.loads(inputs)
        except json.JSONDecodeError:
            return {"ok": False, "error": "inputs must be a JSON object"}
    inputs = inputs if isinstance(inputs, dict) else {}
    if name == "help":
        return {"ok": True, "text": calc_help(inputs)}
    if name == "compatibility":
        return {"ok": False, "error": "Compatibility can't be calculated: the formula and thresholds aren't in the docs yet."}
    if name not in CALCS:
        return {"ok": False, "error": f"calculator must be one of: {', '.join(CALCS)} (or 'help')"}
    try:
        return {"ok": True, "text": CALCS[name][0](inputs)}
    except CalcError as e:
        return {"ok": False, "error": str(e)}


def main() -> None:
    try:
        params = json.loads(PARAMS.read_text(encoding="utf-8"))
        result = run(params if isinstance(params, dict) else {})
    except Exception as e:
        result = {"ok": False, "error": f"{type(e).__name__}: {e}"}
    sys.stdout.write(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
