# Uma Musume: Advance Gameplay Guide

One reference that combines three community spreadsheets: the **Skills Spreadsheet**, the **Spark Procs calculator**, and **Luh's Support Card Encyclopedia**. The guide is text only, and the spreadsheets' tables are kept as Markdown tables.

> **What is and is not included.** Everything a reader would use is here: every skill table and tier list, the spark and affinity tables, the calculator instructions, and all 13 scenario card tables. Three kinds of tabs are left out on purpose. They are the deprecated "(old)" skill tabs, the raw lookup and helper tabs the sheets use internally (for example `alldata`, `_affinity`, `_relations`), and the 2,000-row *Complete Distribution Table*. Section 6 lists them. Card images and column art are not carried over because this is a text-only file.

> **A note on wording.** The introductions, explanations and how-to sections were rewritten for clarity. Game data, per-skill notes and per-card notes are kept as the authors wrote them, apart from obvious typo fixes and tidied spacing, so the numbers and advice stay exactly as published.

---

## Table of Contents

1. [Skills Reference](#1-skills-reference)
2. [Spark Procs and Lineage Planning](#2-spark-procs-and-lineage-planning)
3. [Support Card Encyclopedia](#3-support-card-encyclopedia)
4. [Quick Cross-Guide Workflow](#4-quick-cross-guide-workflow)
5. [Sources and Credits](#5-sources-and-credits)
6. [What Was Left Out](#6-what-was-left-out)

---

## 1. Skills Reference

**Source:** Uma Musume Skills Spreadsheet by @dylank0 (info) and @sayaduck (formatting).

### 1.1 Credits and Updates

| Item | Detail |
|---|---|
| Skill information | @dylank0 |
| Formatting | @sayaduck |
| Companion site | [uma.guide](https://uma.guide/) |
| Latest update | December 12th, 2025: added Manhattan Cafe's unique skill |
| Previous update | November 23rd, 2025: updated the filter for the additional category |

### 1.2 Skill Rank Legend

Every skill is given a rank for each game mode. Use it to judge how much a skill is worth buying.

| Rank | Label | Meaning |
|---|---|---|
| ⍟ | Essential | Absolutely necessary for the given distance or running style. |
| ◎ | Top tier | Generally the best skills available for that distance or style. |
| ◯ | Good | Solid, but falls short of ◎, usually because of lower potency or stricter conditions. |
| ▲ | Situational | Can range anywhere from ⍟ to ✕ depending on the circumstances. |
| △ | Low priority | Take only with spare Skill Points (SP) or when there are no better options. |
| ✕ | Avoid | Useless or too inconsistent. Never take these. |

Ranks are given separately for **Team Trials** and for the latest Champions Meeting (**CM**). The per-style and per-distance lists use **PvP** as the second mode. The column header shows the CM number the rank was set for (for example CM9 for speed skills, CM6 for acceleration).

### 1.3 Glossary

| Symbol | Meaning |
|---|---|
| m/s | Target Speed |
| m꜀/s | Current Speed |
| mₗ/s | Lateral Speed |
| m/s² | Acceleration |
| HP | HP / Stamina |
| FoV | Vision (field of view) |

### 1.4 How to Read the Tables

- **Score/SP** is the skill's score value divided by its cost, so higher means more score per Skill Point.
- **Base Cost** lists the cost in SP. A value such as `130+140` means the base skill costs 130 and its upgraded (gold) version costs 140 more.
- **Placeholders** such as `[Run Style]`, `[Distance]` and `[Rotation]` stand for the value that matches your Uma (for example Front Runner, Mile or Right-Handed).
- A `/` in a cell means "not applicable".
- In the source, one row of a skill's base and upgraded versions often shares merged cells. In this guide the shared values are repeated on both rows so every row can be read on its own.

### 1.5 Usage Tips and Disclaimer

- Use **Ctrl+F** (or *Find & Replace* on mobile) to find a specific skill quickly.
- Most skills depend on the track, and this is especially true of ▲ skills.
- If you are unsure whether a skill is effective on a given track, ask @dylank0 or an experienced JP player.

### 1.6 Skill Tables by Category

#### Speed Skills

Skills that raise target speed (m/s). 111 skills are listed.

| Skill Name | Rank (Team Trials) | Rank (CM9) | Score/SP | Base Cost | Ground/Distance/Style | Base Duration(s) | Effect (Self) | Effect (Target) | Effect Target(s) | Precondition(s) | Condition(s) | Why? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [Run Style] Corners ◯ | ◎ | ⍟ | 3.85 | 130 | [Run Style] | 3 | 0.15m/s | / | / | / | Random Point on Random Corner | Cheap and consistent, they are must-haves |
| [Run Style] Corners ◎ | △ | ⍟ | 1.85 | 130+140 | [Run Style] | 3 | 0.25m/s | / | / | / | Random Point on Random Corner | Cheap and consistent, they are must-haves |
| [Run Style] Straightaways ◯ | ◎ | ⍟ | 3.85 | 130 | [Run Style] | 3 | 0.15m/s | / | / | / | Random Point on Random Straight | Cheap and consistent, they are must-haves |
| [Run Style] Straightaways ◎ | △ | ⍟ | 1.85 | 130+140 | [Run Style] | 3 | 0.25m/s | / | / | / | Random Point on Random Straight | Cheap and consistent, they are must-haves |
| [Distance] Corners ◯ | ◎ | ⍟ | 5 | 100 | [Distance] | 3 | 0.15m/s | / | / | / | Random Point on Random Corner | Cheap and consistent, they are must-haves |
| [Distance] Corners ◎ | △ | ⍟ | 2.38 | 100+110 | [Distance] | 3 | 0.25m/s | / | / | / | Random Point on Random Corner | Cheap and consistent, they are must-haves |
| [Distance] Straightaways ◯ | ◎ | ⍟ | 5 | 100 | [Distance] | 3 | 0.15m/s | / | / | / | Random Point on Random Straight | Cheap and consistent, they are must-haves |
| [Distance] Straightaways ◎ | △ | ⍟ | 2.38 | 100+110 | [Distance] | 3 | 0.25m/s | / | / | / | Random Point on Random Straight | Cheap and consistent, they are must-haves |
| Corner Adept ◯ | △ | △ | 2.78 | 180 | / | 2.4 (30s CD) | 0.15m/s | / | / | / | Random Point on Random Corner | Consistent, but expensive<br>Rare ver. has greater speed boost making it more worth to acquire |
| Professor of Curvature | ◯ | ◯ | 3.33 | 180+180 | / | 2.4 (30s CD) | 0.35m/s | / | / | / | Random Point on Random Corner | Consistent, but expensive<br>Rare ver. has greater speed boost making it more worth to acquire |
| Straightaway Adept | △ | △ | 2.94 | 170 | / | 2.4 (30s CD) | 0.15m/s | / | / | / | Random Point on any Straight | Consistent |
| Beeline Burst | ◯ | ◯ | 3.53 | 170+170 | / | 2.4 (30s CD) | 0.35m/s | / | / | / | Random Point on any Straight | Consistent |
| Ramp Up | △ | △ | 2.94 | 170 | / | 1.8 (30s CD) | 0.15m/s | / | / | / | Overtake, during Mid-Race | Consistent. Even better when used in tandem with Tail Held High, Slipstream, and Playtime's Over! |
| It's On! | ◯ | ◯ | 3.53 | 170+170 | / | 1.8 (30s CD) | 0.35m/s | / | / | / | Overtake, during Mid-Race | Consistent. Even better when used in tandem with Tail Held High, Slipstream, and Playtime's Over! |
| Homestretch Haste | △ | △ | 2.94 | 170 | / | 2.4 | 0.15m/s | / | / | / | In Last Spurt Mode, at Random Point during Last Spurt | Useful and (fairly) consistent Last Spurt speed boost, falls short of ◎ because it could activate at the very end of a race |
| In Body and Mind | ◯ | ◯ | 3.53 | 170+170 | / | 2.4 | 0.35m/s | / | / | / | In Last Spurt Mode, at Random Point during Last Spurt | Useful and (fairly) consistent Last Spurt speed boost, falls short of ◎ because it could activate at the very end of a race |
| Uma Stan | ◎ | ◎ | 3.12 | 160 | / | 3 | 0.15m/s | / | / | / | ≥3 Nearby Uma(s), ≥5s after Race Start | Best speed skill on longer tracks for non-Front-Runners, can help to release PDM on some longer tracks |
| Super Stan | ◎ | ◎ | 3.75 | 160+160 | / | 3 | 0.35m/s | / | / | / | ≥3 Nearby Uma(s), ≥5s after Race Start | Best speed skill on longer tracks for non-Front-Runners, can help to release PDM on some longer tracks |
| Tail Held High | ◎ | ◎ | 5 | 100 | / | 3 | 0.15m/s | / | / | / | ≥3 Skill Activations, during Mid-Race | Cheap and consistent, though note the condition of requiring 3 skill activations before acquiring it |
| Slipstream | ◎ | ◎ | 3.12 | 160 | / | 3 (30s CD) | 0.15m/s | / | / | / | ≤2.5m behind Uma infront for ≥3s, ≥10s after Race Start | Consistent and facilitates overtaking when activated |
| Playtime's Over! | ◎ | ◎ | 3.12 | 160 | / | 3 (30s CD) | 0.15m/s | / | / | / | ≤2.5m ahead of Uma behind for ≥3s, ≥10s after Race Start | Consistent and improves Uma's capacity to maintain her placement |
| Ignited Spirit SPD | △ | △ | 2.5 | 200 | / | 1.8 | 0.15m/s | / | / | / | Random Point during Mid-Race | 1.8s isn't very long and it costs 200 base SP |
| Burning Spirit SPD | △ | △ | 3 | 200+200 | / | 1.8 | 0.35m/s | / | / | / | Random Point during Mid-Race | 1.8s isn't very long and it costs 200 base SP |
| Ignited Spirit GUTS | ◯ | ◎ | 2.5 | 200 | / | 1.8 | 0.05m/s & 0.1m/s² | / | / | / | Random Point during Late-Race | Good random Late-Race accel but in the game's current state,<br>this skill's effect is likely 80% (when Total Guts ≤ 1200) or 90% (when 1200 < Total Guts ≤ 1600) |
| Burning Spirit GUTS | ◎ | ◎ | 3 | 200+200 | / | 1.8 | 0.25m/s & 0.3m/s² | / | / | / | Random Point during Late-Race | Good random Late-Race accel but in the game's current state,<br>this skill's effect is likely 80% (when Total Guts ≤ 1200) or 90% (when 1200 < Total Guts ≤ 1600) |
| Risky Business | ✕ | ✕ | 4.17 | 120 | / | 1.8 | 0.25m/s & -[Random]% HP | / | / | / | Random Point in Second Half of Race | This skill can completely kill your stamina, it's definitely not worth it unless you're trying to do some niche strat |
| Fast-Paced | ◎ | ◎ | 2.78 | 180 | Front Runner | 3 | 0.15m/s | / | / | / | First Half of the Pack, at Random Point during Mid-Race | Consistent with easy conditions. Helps Front Runners maintain/regain their lead during the Mid-Race |
| Escape Artist | ◎ | ◎ | 3.33 | 180+180 | Front Runner | 3 | 0.35m/s | / | / | / | First Half of the Pack, at Random Point during Mid-Race | Consistent with easy conditions. Helps Front Runners maintain/regain their lead during the Mid-Race |
| Leader's Pride | △ | ◎ | 2.78 | 180 | Front Runner | 3 | 0.15m/s | / | / | / | Be overtaken OR Blocked from the Side(s),<br>during Early-Race or Mid-Race, ≥5s after Race Start | Inconsistent activation during Early-Race where overtaking doesn't happen frequently or consistently, consistency is directly proportional to track distance |
| Prepared to Pass | △ | △ | 2.78 | 180 | Pace Chaser | 1.8 | 0.15m/s | / | / | / | First Half of the Pack, at Random Point on Final Corner | Consistent but Target Speed boost during Final Corners are only useful if Uma will enter Last Spurt Mode in a few seconds/has already entered Last Spurt Mode.<br>Otherwise, boosting Target Speed right when Uma enters Last Spurt Mode renders it useless (doesn't actually increase speed since Uma's Current Speed hasn't reached Target Speed) |
| Speed Star | △ | △ | 3.33 | 180+180 | Pace Chaser | 1.8 | 0.35m/s | / | / | / | First Half of the Pack, at Random Point on Final Corner | Consistent but Target Speed boost during Final Corners are only useful if Uma will enter Last Spurt Mode in a few seconds/has already entered Last Spurt Mode.<br>Otherwise, boosting Target Speed right when Uma enters Last Spurt Mode renders it useless (doesn't actually increase speed since Uma's Current Speed hasn't reached Target Speed) |
| Position Pilfer | ◯ | ◯ | 2.78 | 180 | Late Surger | 2.4 | 0.15m/s | / | / | / | 6th-9th/7th-12th Place, at Random Point during Mid-Race | Consistent |
| Fast & Furious | ◯ | ◎ | 3.33 | 180+180 | Late Surger | 2.4 | 0.35m/s | / | / | / | 6th-9th/7th-12th Place, at Random Point during Mid-Race | Consistent |
| Outer Swell | ◯ | ◎ | 2.78 | 180 | Late Surger | 3 | 0.15m/s | / | / | / | Overtake Uma closer to the Inner Fence than you, on Final Corner | Somewhat consistent but Target Speed boost during Final Corners are only useful if Uma will enter Last Spurt Mode in a few seconds/has already entered Last Spurt Mode.<br>Otherwise, boosting Target Speed right when Uma enters Last Spurt Mode renders it useless (doesn't actually increase speed since Uma's Current Speed hasn't reached Target Speed) |
| Rising Dragon | ◯ | ◎ | 3.33 | 180+180 | Late Surger | 3 | 0.35m/s | / | / | / | Overtake Uma closer to the Inner Fence than you, on Final Corner | Somewhat consistent but Target Speed boost during Final Corners are only useful if Uma will enter Last Spurt Mode in a few seconds/has already entered Last Spurt Mode.<br>Otherwise, boosting Target Speed right when Uma enters Last Spurt Mode renders it useless (doesn't actually increase speed since Uma's Current Speed hasn't reached Target Speed) |
| 1,500,000 CC | ◎ | ◎ | 4.17 | 120 | Late Surger | 2.4 | 0.15m/s | / | / | / | Random Point on Random Uphill | Cheap and consistent |
| 15,000,000 CC | ◎ | ◎ | 5 | 120+120 | Late Surger | 2.4 | 0.35m/s | / | / | / | Random Point on Random Uphill | Cheap and consistent |
| Masterful Gambit | ✕ | ✕ | 2.78 | 180 | End Closer | 3 | 0.15m/s | / | / | / | Last Half of the Pack (by Distance), at Random Point during Late-Race | Extremely inconsistent, borderline impossible to activate as your Uma should already be at least within top 75% (by distance) of the pack by the time the Mid-Race ends |
| Sturm und Drang | ✕ | ✕ | 3.33 | 180+180 | End Closer | 3 | 0.35m/s | / | / | / | Last Half of the Pack (by Distance), at Random Point during Late-Race | Extremely inconsistent, borderline impossible to activate as your Uma should already be at least within top 75% (by distance) of the pack by the time the Mid-Race ends |
| Early Start | △ | △ | 2.78 | 180 | End Closer | 4 | 0.05m/s | / | / | / | 5th-9th/6th-12th Place, at Random Point during Mid-Race | Very small speed boost, but it can unlock Pace-down Mode for a good amount of time so it isn't totally useless |
| Gap Closer | ▲ | ▲ | 3.12 | 160 | Sprint | 3 | 0.15m/s & 0.05m/s² | / | / | / | 6th-9th/7th-12th Place, at Random Point during Late-Race | Decent for Sprint Late Surgers/End Closers (only King Halo for now) |
| Blinding Flash | ▲ | ▲ | 3.75 | 160+160 | Sprint | 3 | 0.35m/s & 0.1m/s² | / | / | / | 6th-9th/7th-12th Place, at Random Point during Late-Race | Decent for Sprint Late Surgers/End Closers (only King Halo for now) |
| Huge Lead | ✕ | ✕ | 2.94 | 170 | Sprint | 3 | 0.15m/s | / | / | / | 1st Place, during Mid-Race, ≥7.5m ahead of Uma behind | 12.5m lead is highly unfeasible, this skill will almost never activate |
| Staggering Lead | ✕ | ✕ | 3.53 | 170+170 | Sprint | 3 | 0.35m/s | / | / | / | 1st Place, during Mid-Race, ≥7.5m ahead of Uma behind | 12.5m lead is highly unfeasible, this skill will almost never activate |
| Productive Plan | ◯ | ✕ | 3.12 | 160 | Mile | 3 | 0.15m/s | / | / | / | First Half of the Pack, at Random Point during Early-Race, ≥5s After Race Start | Mostly consistent but activation occurs during Early-Race where Uma may not have hit top speed, making target speed boosts obsolete (doesn't actually increase speed<br>since Uma's Current Speed hasn't reached Target Speed). Additionally, the skill may pick a point prior to the 5 seconds needed after the race starts to activate, making it proc inconsistently too |
| Mile Maven | ◎ | ✕ | 3.75 | 160+160 | Mile | 3 | 0.35m/s | / | / | / | First Half of the Pack, at Random Point during Early-Race, ≥5s After Race Start | Mostly consistent but activation occurs during Early-Race where Uma may not have hit top speed, making target speed boosts obsolete (doesn't actually increase speed<br>since Uma's Current Speed hasn't reached Target Speed). Additionally, the skill may pick a point prior to the 5 seconds needed after the race starts to activate, making it proc inconsistently too |
| Shifting Gears | ◯ | ✕ | 3.12 | 160 | Mile | 2.4 | 0.15m/s | / | / | / | First Half of the Pack, at Random Point during Mid-Race | Consistent |
| Changing Gears | ◯ | ✕ | 3.75 | 160+160 | Mile | 2.4 | 0.35m/s | / | / | / | First Half of the Pack, at Random Point during Mid-Race | Consistent |
| Unyielding Spirit | ◎ | ✕ | 4.17 | 120 | Mile | 2.4 | 0.15m/s | / | / | / | Have Overtake Target, ≥5s after Race Start | Cheap and consistent |
| Big-Sisterly | ◎ | ✕ | 5 | 120+120 | Mile | 2.4 | 0.35m/s | / | / | / | Have Overtake Target, ≥5s after Race Start | Cheap and consistent |
| Up-Tempo | ◯ | ✕ | 3.12 | 160 | Medium | 2.4 | 0.15m/s | / | / | / | First Half of the Pack, at Random Point during Mid-Race | Consistent |
| Killer Tunes | ◯ | ✕ | 3.75 | 160+160 | Medium | 2.4 | 0.35m/s | / | / | / | First Half of the Pack, at Random Point during Mid-Race | Consistent |
| Steadfast | △ | ✕ | 3.12 | 160 | Medium | 3 | 0.15m/s & 0.05m/s² | / | / | / | Be overtaken, on Final Corner | Essentially a band-aid protective measure against losing the lead on the Final Corner, could be good but it's very situational |
| Unyielding | △ | ✕ | 3.75 | 160+160 | Medium | 3 | 0.35m/s & 0.1m/s² | / | / | / | Be overtaken, on Final Corner | Essentially a band-aid protective measure against losing the lead on the Final Corner, could be good but it's very situational |
| All I've Got | △ | ✕ | 3.12 | 160 | Medium | 2.4 | 0.15m/s | / | / | / | 2nd-5th/7th Place, in Last Spurt Mode, on a Straight | Other than a few 2400m tracks, most Medium tracks have their Last Spurt Modes activate on a Corner, so this skill acts as a better Homestretch Haste/In Body and Mind |
| Come What May | △ | ✕ | 3.75 | 160+160 | Medium | 2.4 | 0.35m/s | / | / | / | 2nd-5th/7th Place, in Last Spurt Mode, on a Straight | Other than a few 2400m tracks, most Medium tracks have their Last Spurt Modes activate on a Corner, so this skill acts as a better Homestretch Haste/In Body and Mind |
| Inside Scoop | △ | ✕ | 3.12 | 160 | Long | 3 | 0.15m/s | / | / | / | Right Beside Inner Fence, on Final Corner | Somewhat consistent but Target Speed boost during Final Corners are only useful if Uma will enter Last Spurt Mode in a few seconds/has already entered Last Spurt Mode.<br>Otherwise, boosting Target Speed right when Uma enters Last Spurt Mode renders it useless (doesn't actually increase speed since Uma's Current Speed hasn't reached Target Speed) |
| Innate Experience | △ | ✕ | 3.75 | 160+160 | Long | 3 | 0.35m/s | / | / | / | Right Beside Inner Fence, on Final Corner | Somewhat consistent but Target Speed boost during Final Corners are only useful if Uma will enter Last Spurt Mode in a few seconds/has already entered Last Spurt Mode.<br>Otherwise, boosting Target Speed right when Uma enters Last Spurt Mode renders it useless (doesn't actually increase speed since Uma's Current Speed hasn't reached Target Speed) |
| Keeping the Lead | △ | △ | 3.12 | 160 | Long | 3 | 0.15m/s | / | / | / | 1st Place, at Random Point during Mid-Race, ≥2.5m ahead of Uma behind | 2.5m lead is somewhat possible in a Long race but still not the most consistent |
| Vanguard Spirit | △ | △ | 3.75 | 160+160 | Long | 3 | 0.35m/s | / | / | / | 1st Place, at Random Point during Mid-Race, ≥2.5m ahead of Uma behind | 2.5m lead is somewhat possible in a Long race but still not the most consistent |
| Pressure | △ | ✕ | 3.12 | 160 | Long | 3 | 0.15m/s | / | / | / | Overtake, during Late-Race | Overtakes and consequently, Target Speed boost is likely to occur toward the beginning of Last Spurt Mode,<br>rendering it useless (doesn't actually increase speed since Uma's Current Speed hasn't reached Target Speed) |
| Overwhelming Pressure | △ | ✕ | 3.75 | 160+160 | Long | 3 | 0.35m/s | / | / | / | Overtake, during Late-Race | Overtakes and consequently, Target Speed boost is likely to occur toward the beginning of Last Spurt Mode,<br>rendering it useless (doesn't actually increase speed since Uma's Current Speed hasn't reached Target Speed) |
| Top Pick | △ | ✕ | 2.78 | 180 | Dirt | 2.4 | 0.15m/s | / | / | / | Blocked from the Side(s) for ≥2s, during Mid-Race | Should have a consistent activation and is helpful for maintaining/securing/fighting for the lead |
| Trending in the Charts! | △ | ✕ | 3.33 | 180+180 | Dirt | 2.4 | 0.35m/s | / | / | / | Blocked from the Side(s) for ≥2s, during Mid-Race | Should have a consistent activation and is helpful for maintaining/securing/fighting for the lead |
| Certain Victory | △ | ◎ | 2.5 | 200 | / | 3 | 0.25m/s | / | / | 1st-5th Place,<br>Have Overtake Target for ≥2s,<br>on Final Corner or beyond | On Last Straight | Identical to OG Teio's unique with slightly looser conditions |
| Legacy of the Strong | △ | △ | 2.5 | 200 | / | 3.6 | 0.15m/s | / | / | / | Be Overtake Target for ≥1s, at 1st-3rd Place, on Final Corner or beyond,<br>≤2.5m ahead of Uma behind, ≤45% HP remaining | Effects aren't bad but inconsistent activation |
| Shooting Star | △ | ◯ | 2.5 | 200 | / | 3 | 0.15m/s & 0.05m/s² | / | / | / | Overtake, at 2nd-5th/6th Place, during Late-Race or beyond | Consistent activation, but weak effect |
| The View from the Lead is Mine! | △ | △ | 2.5 | 200 | / | 3 | 0.15m/s | / | / | / | 1st Place, in Second Half of Race, ≥2.5m ahead of Uma behind | Somewhat consistent activation for Front Runners, but weak effect |
| Sky-High Teio Step | △ | ◎ | 2.5 | 200 | / | 3 | 0.25m/s | / | / | 1st-3rd Place,<br>Have Overtake Target,<br>≤2.5m behind Uma infront | On Last Straight | Mostly consistent for non-Front-Runners, with strong effect |
| Triumphant Pulse | △ | ◎ | 2.5 | 200 | / | 3 | 0.25m/s | / | / | / | 2nd-5th Place, 200m before Race End | Consistent for non-Front-Runners, with strong effect |
| Anchors Aweigh! | △ | ✕ | 2.5 | 200 | / | 3.6 | 0.05m/s | / | / | / | 6th-9th/7th-12th Place, at 50-60% of Race | Consistent for Late Surgers/End Closers but minimal effect |
| Cut and Drive! | ✕ | ✕ | 2.5 | 200 | / | 3 | 0.15m/s | / | / | / | First Half of the Pack but not 1st-2nd Place,<br>≤200m before Race End, ≤2.5m ahead/behind another Uma | Not the most consistent, and also a weak effect, not worth taking |
| Resplendent Red Ace | △ | ▲ | 2.5 | 200 | / | 3 | 0.05m/s & 0.1m/s² | / | / | / | 1st Place, in Second Half of Race, ≤2.5m ahead of Uma behind<br>OR<br>Have Overtake Target, at 2nd Place, in Second Half of Race | Accel can come in handy occasionally but still very situational and slightly unreliable |
| Where There's a Will, There's a Way | △ | △ | 2.5 | 200 | / | 3 | 0.15m/s | / | / | / | Overtake, at 3rd-9th/12th Place, on Last Straight | Decent speed skill option for non-Front-Runners |
| The Duty of Dignity Calls | △ | ◯ | 2.5 | 200 | / | 3 | 0.15m/s | / | / | / | First 30% of the Pack (by Distance), on Final Corner | Final Corner Target Speed boost is inconsistent (especially in Med race), but it can be situationally good for Front Runners/Pace Chasers |
| Victoria por plancha ☆ | △ | ◎ | 2.5 | 200 | / | 3 | 0.05m/s & 0.1m/s² | / | / | / | 1st-2nd Place, with ≥30% HP remaining, on Last Straight | Activation is mostly consistent, some tracks benefit from a Last Straight accel |
| This Dance Is for Vittoria! | △ | ◯ | 2.5 | 200 | / | 3 | 0.15m/s | / | / | / | 1st-4th Place, ≤2.5m ahead/behind another Uma, on Final Corner or beyond | Fairly consistent activation but Final Corner Target Speed boost could be inconsistent |
| Behold Thine Emperor's Divine Might | △ | ◎ | 2.5 | 200 | / | 3 | 0.25m/s | / | / | Overtook ≥3 Umas<br>since Late-Race Start | On Last Straight | Consistent for non-Front-Runners, with strong effect |
| Blazing Pride | △ | ◯ | 2.5 | 200 | / | 3 | 0.15m/s | / | / | / | Overtake, at 3rd-9th/12th Place, on Final Corner | Final Corner Target Speed boost is inconsistent (especially in Med race), but it can be situationally good for Late Surgers |
| ∴win Q.E.D. | △ | ◯ | 2.5 | 200 | / | 3 | 0.15m/s | / | / | / | Overtake, at 1st-4th Place, on Final Corner | Final Corner Target Speed boost is inconsistent (especially in Med race), but it can be situationally good for Front Runners |
| Flashy☆Landing | △ | ◯ | 2.5 | 200 | / | 3 | 0.05m/s & 0.1m/s² | / | / | / | 1st-3rd Place, Blocked from the Side(s) for ≥2s, on Final Corner or beyond | Acceleration on and beyond Final Corner is decent, conditions to activate may not be consistent unless you're Front Runner or Pace Chaser |
| G00 1st. F∞; | ✕ | △ | 2.5 | 200 | / | 3 | 0.15m/s | / | / | / | 1st-3rd Place, No Late Start, no Rushed, on Last Straight | 0.15m/s but has two additional checks (for Start Delay and Rushed) |
| Blue Rose Closer | △ | △ | 2.5 | 200 | / | 3 | 0.15m/s | / | / | Overtake, at 1st-4th Place,<br>on Final Corner or beyond | On Last Straight | Consistent, but weak effect |
| Our Ticket to Win! | △ | △ | 2.5 | 200 | / | 3 | 0.15m/s | / | / | Blocked from the Side(s) for ≥2s,<br>on Final Corner or beyond | 1st-5th Place, on Last Straight | Side block on Last Straight is rare, weak effect as well makes it not worth getting |
| Genius x Bakushin = Victory | ✕ | △ | 2.5 | 200 | / | 3 | 0.15m/s | / | / | / | 1st-3rd Place, in Second Half of Race, Blocked from the Side(s) for ≥2s | Fairly consistent, but also weak |
| I See Victory in My Future! | ✕ | ✕ | 2.5 | 200 | / | 3 | 0.15m/s & 0.05m/s² | / | / | / | ≥3rd Place, Blocked in Front, during Late-Race or beyond | Front Block condition is downright horrible |
| Just a Little Farther! | △ | ✕ | 2.5 | 200 | / | 3 | 0.15m/s | / | / | / | 3rd Place, ≤2.5m ahead of Uma behind, during Late-Race or beyond | Fairly consistent, but also weak |
| Prideful King | ✕ | ✕ | 2.5 | 200 | / | 3 | 0.25m/s | / | / | / | 4th-6th/8th Place, no Rushed, 200m before Race End | Extremely inconsistent, if not totally impossible to even activate in any distance but Sprint |
| #LookatCurren | △ | △ | 2.5 | 200 | / | 3 | 0.05m/s & 0.1m/s² | / | / | / | Overtake, at 2nd-5th/6th Place, at 50-65% of Race | Slightly consistent but effect is really weak since it usually activates at Mid-Race |
| Nemesis | △ | ◯ | 2.5 | 200 | / | 3 | 0.15m/s | / | / | / | Have Overtake Target, at 4th-7th/5th-9th Place, on Final Corner or beyond | Consistent for Late Surgers/End Closers but effect is weak |
| SPARKLY☆STARDOM | △ | ▲ | 2.5 | 200 | / | 3 | 0.05m/s & 0.1m/s² | / | / | / | 1st-2nd Place, ≤2.5m ahead of Uma behind, on a Straight, during Mid-Race | Mostly consistent for most Front Runners and helps them maintain their lead |
| Shadow Break | △ | ◯ | 2.5 | 200 | / | 3 | ① 0.25m/s<br>② 0.15m/s | / | / | ① Blocked from the Side(s) for ≥2s<br>during Mid-Race | Overtake Uma closer to Inner Fence than you,<br>at 2nd-7th/9th, on Final Corner or beyond | Should be consistent but effect isn't great enough to be used over other similar uniques |
| Eternal Moments | △ | △ | 2.5 | 200 | / | 3 | 0.15m/s | / | / | / | First Half of the Pack but not 1st-3rd Place, have Overtake Target, during Mid-Race | Fairly consistent for non-Front-Runners, but the effect is weak |
| Flowery☆Maneuver | △ | ▲ | 2.5 | 200 | / | ① 3<br>② 2.4 | ① 0.15m/s<br>② 0.2m/s² | / | / | / | ① Overtake, at first ⅖ of the Pack, on Final Corner<br>② Overtake, at ½-⅘ of the Pack, on Final Corner | ① Strong for Front/Pace on some tracks to carry over speed on final corner<br>② Strong for Late/End on tracks that start the Last Spurt on final corner |
| You and Me! One-on-One! | △ | △ | 2.5 | 200 | / | 3 | 0.15m/s | / | / | Overtake Uma, who's Closer to<br>the Inner Fence than you,<br>at last 60% of the pack,<br>on Final Corner or beyond | On Last Straight | Decent Last Straight speed skill for Late Surgers or End Closers |
| Lights of Vaudeville | △ | ◯ | 2.5 | 200 | / | 3 | 0.25m/s | / | / | / | ≤5m ahead of Uma behind for ≥1s, at First 30% of the Pack, on Last Straight | Consistent activation but effectiveness depends on track |
| A Kiss for Courage | △ | △ | 2.5 | 200 | / | 3 | 0.15m/s | / | / | / | Activate ≥1 Recovery Skills, at 1st-3rd Place, in Second Half of Race | Varying effectiveness depending on track but can be strong with Triple 7s activation |
| I Never Goof Up! | △ | ◯ | 2.5 | 200 | / | 3 | 0.05m/s & 0.1m/s² | / | / | / | Overtake, at 3rd-9th/12th Place, on a Corner, during Late-Race | Good effect but rng and track dependent |
| Schwarzes Schwert | ✕ | △ | 2.5 | 200 | / | 3 | 0.15m/s | / | / | No Late Start,<br>no Rushed | 3rd-9th/12th Place, on Last Straight | 0.15m/s but requires two additional checks (for Start Delay and Rushed) |
| Bountiful Harvest | △ | △ | 2.5 | 200 | / | 3 | 0.15m/s | / | / | / | Be an Overtake Target for ≥2s, at 4th-9th/5th-12th Place, in Second Half of Race | Consistent but relatively weak |
| YUMMY☆SPEED! | △ | ✕ | 2.5 | 200 | / | 3 | 0.05m/s & 0.1m/s² | / | / | / | ≤70% HP Remaining, at 3rd-5th/6th Place, at 45-60% of Race | Unfortunate timing at 60% of the Race makes this skill's acceleration practically useless |
| OMG! (ﾟ∀ﾟ) The Final Sprint! ☆ | △ | △ | 2.5 | 200 | / | 3 | 0.15m/s & 0.015mₗ/s | / | / | Late-Race or beyond | Overtake ≥2 Umas | Generally, when you overtake in Late-Race, you're still accelerating, so a Target Speed skill wouldn't be effective |
| Give Mummy a Hug ♡ | △ | ◯ | 2.5 | 200 | / | 3 | 0.05m/s & 0.1m/s² | / | / | / | 1st-4th Place, ≤2.5m behind Uma infront, on Last Straight | Good accel for tracks that have their Last Spurt Mode begin on/near a Last Straight |
| A Princess Must Seize Victory! | ✕ | ✕ | 2.5 | 200 | / | 3 | 0.15m/s | / | / | / | Blocked from the Side(s) for ≥2s, on Last Straight | Side block condition on the Last Straight is quite strict and difficult to proc |
| Chasing After You | △ | △ | 2.5 | 200 | / | 3.6 | 0.05m/s | -0.025m꜀/s | 5 closest Umas ahead | / | 4th-6th/5th-8th Place, in Second Half of Race | Very weak effect but can be used as a debuff |
| Dancing in the Leaves | ✕ | ✕ | 2.5 | 200 | / | 3 | 0.05m/s & 0.1m/s² | / | / | / | 3rd-6th/4th-8th Place, Blocked from the Side(s) for ≥2s, on Final Corner | Side Block isn't consistent, effect isn't outstanding either |
| Arrows Whistle, Shadows Disperse | △ | ◯ | 2.5 | 200 | / | 3 | 0.15m/s | / | / | / | Be Overtake Target for ≥2s, at 1st-4th/5th Place, on Final Corner or beyond | Consistent, but weak effect |
| Pop & Polish | △ | ◯ | 2.5 | 200 | / | 3 | 0.15m/s | / | / | / | Overtake, at 2nd Place, on Last Straight<br>OR<br>Have Overtake Target for ≥2s, at 2nd-3rd/4th Place, on Last Straight | Consistent, but weak effect |
| Presents from X | △ | △ | 2.5 | 200 | / | 3 | 0.15m/s | / | / | 1st-4th/5th Place, ≥5s after Race Start | 2nd-4th/5th Place, in Second Half of Race, during Mid-Race |  |
| Festive Miracle | △ | ◯ | 2.5 | 200 | / | 3 | 0.05m/s & 0.1m/s² & 0.5% HP | / | / | Activate ≥3 Recovery Skills | In Second Half of Race | Strong on some tracks where Triple 7s can proc before the Last Spurt |
| Fairy Tale | △ | △ | 2.5 | 200 | / | 3 | 0.15m/s | / | / | / | Blocked from the Side(s) for ≥2s, at 2nd-4th/5th Place, in Second Half of Race |  |

#### Acceleration Skills

Skills that raise acceleration (m/s²). 43 skills are listed.

| Skill Name | Rank (Team Trials) | Rank (CM6) | Score/SP | Base Cost | Ground/Distance/Style | Base Duration(s) | Effect | Precondition(s) | Condition(s) | Why? |
|---|---|---|---|---|---|---|---|---|---|---|
| Corner Acceleration ◯ | △ | ✕ | 2.78 | 180 | / | 3 | 0.2m/s² | / | Random Point on Random Corner | Acceleration on the Corner 1/First Corner of any track is useless |
| Corner Connoisseur | △ | ✕ | 3.33 | 180+180 | / | 3 | 0.4m/s² | / | Random Point on Random Corner | Acceleration on the Corner 1/First Corner of any track is useless |
| Straightaway Acceleration | △ | ✕ | 2.94 | 170 | / | 3 | 0.2m/s² | / | Random Point on Random Straight | Random straight activations are too inconsistent to be effective |
| Rushing Gale! | △ | ✕ | 3.53 | 170+170 | / | 3 | 0.4m/s² | / | Random Point on Random Straight | Random straight activations are too inconsistent to be effective |
| Nimble Navigator | ◯ | ◎ | 3.33 | 150 | / | 3 | 0.2m/s² & 0.005mₗ/s | / | In Last Spurt Mode, with ≥1% HP remaining, ≤2.5m behind Uma infront for ≥1s | Strong accel but rng-dependent |
| No Stopping Me! | ◯ | ◎ | 4 | 150+150 | / | 3 | 0.4m/s² & 0.025mₗ/s | / | In Last Spurt Mode, with ≥1% HP remaining, ≤2.5m behind Uma infront for ≥1s | Strong accel but rng-dependent |
| Highlander | △ | ◎ | 3.12 | 160 | / | 3 | 0.2m/s² | / | Random Point on Random Uphill | Very powerful on tracks with Uphills right before/as Last Spurt Mode begins |
| Groundwork | △ | ▲ | 5 | 100 | / | 3 | 0.2m/s² | / | ≥3 Skill Activations, during Early-Race | For Front Runners only, use with 3 Early-Race skills like Focus/Concentration+Green Skills |
| Ignited Spirit PWR | ◎ | ◎ | 2.5 | 200 | / | 1.2 | 0.2m/s² | / | Random Point during Late-Race | It's like a weaker but universal Slick Surge/On Your Left! |
| Burning Spirit PWR | ◎ | ◎ | 3 | 200+200 | / | 1.2 | 0.4m/s² | / | Random Point during Late-Race | It's like a weaker but universal Slick Surge/On Your Left! |
| Early Lead | ◎ | ⍟ | 4.17 | 120 | Front Runner | 1.2 | 0.2m/s² | / | During Early-Race | Necessary skill for all Front Runners |
| Taking the Lead | ◎ | ⍟ | 5 | 120+120 | Front Runner | 1.2 | 0.4m/s² | / | During Early-Race | Necessary skill for all Front Runners |
| Final Push | △ | ✕ | 2.78 | 180 | Front Runner | 3 | 0.2m/s² | / | 1st Place, at Random Point on Final Corner | Being in 1st isn't completely consistent, but it's a rare skill that can be useful on tracks where<br>your Uma enters Last Spurt Mode slightly after where the Final Corner begins/right at where the Final Corner is |
| Unrestrained | △ | ✕ | 3.33 | 180+180 | Front Runner | 3 | 0.4m/s² | / | 1st Place, at Random Point on Final Corner | Being in 1st isn't completely consistent, but it's a rare skill that can be useful on tracks where<br>your Uma enters Last Spurt Mode slightly after where the Final Corner begins/right at where the Final Corner is |
| Second Wind | ✕ | ✕ | 2.78 | 180 | Front Runner | 3 | 0.2m/s² | / | 2nd-9th/12th Place, at Random Point in Mid-Race | Expensive and impossible to activate on Front Runners, plus, Mid-Race acceleration is useless |
| Shrewd Step | △ | ✕ | 4.17 | 120 | Pace Chaser | 3 | 0.2m/s² | / | Change Lanes | Cheap and consistent activation, but useless Mid-Race accel |
| Technician | △ | ✕ | 5 | 120+120 | Pace Chaser | 3 | 0.3m/s² | / | Change Lanes | Cheap and consistent activation, but useless Mid-Race accel |
| Straight Descent | △ | ⍟ | 4.17 | 120 | Pace Chaser | 3 | 0.2m/s² | / | Random Point on Random Downhill | Very powerful on tracks with Downhills right before/as Last Spurt Mode begins |
| Determined Descent | △ | ⍟ | 5 | 120+120 | Pace Chaser | 3 | 0.3m/s² | / | Random Point on Random Downhill | Very powerful on tracks with Downhills right before/as Last Spurt Mode begins |
| Tactical Tweak | △ | ✕ | 4.17 | 120 | Pace Chaser | 3 | 0.2m/s² | / | 5th-9th/6th-12th Place, at Random Point in Mid-Race | Cheap and consistent activation, but useless Mid-Race accel |
| Shatterproof | △ | ✕ | 5 | 120+120 | Pace Chaser | 3 | 0.3m/s² | / | 5th-9th/6th-12th Place, at Random Point in Mid-Race | Cheap and consistent activation, but useless Mid-Race accel |
| Head-On | ◯ | ⍟ | 2.78 | 180 | Pace Chaser | 1.8 | 0.2m/s² | / | First Half of the Pack, at Random Point during Late-Race | Pace Chaser ver. of Slick Surge |
| Slick Surge | ◯ | ⍟ | 2.78 | 180 | Late Surger | 1.8 | 0.2m/s² | / | 6th-9th/7th-12th Place, at Random Point in Late-Race | Good but inconsistently effective accel |
| On Your Left! | ◯ | ⍟ | 3.33 | 180+180 | Late Surger | 1.8 | 0.4m/s² | / | 6th-9th/7th-12th Place, at Random Point in Late-Race | Good but inconsistently effective accel |
| Fighter | △ | ✕ | 4.17 | 120 | Late Surger | 4 | 0.2m/s² | / | Have Overtake Target, ≥5s after Race Start | Cheap and consistent activation but useless Mid-Race accel |
| Hard Worker | △ | ✕ | 5 | 120+120 | Late Surger | 4 | 0.3m/s² | / | Have Overtake Target, ≥5s after Race Start | Cheap and consistent activation but useless Mid-Race accel |
| Straightaway Spurt | △ | ⍟ | 2.78 | 180 | End Closer | 0.9 | 0.2m/s² | / | In Last Spurt Mode, on a Straight | Very powerful End Closer acceleration that works on tracks where Last Spurt Mode begins on a Straight |
| Encroaching Shadow | △ | ⍟ | 3.33 | 180+180 | End Closer | 0.9 | 0.4m/s² | / | In Last Spurt Mode, on a Straight | Very powerful End Closer acceleration that works on tracks where Last Spurt Mode begins on a Straight |
| Sprinting Gear | △ | ✕ | 3.12 | 160 | Sprint | 3 | 0.2m/s² | / | Random Point on Any Straight | Random straight activations are almost always useless |
| Turbo Sprint | △ | ✕ | 3.75 | 160+160 | Sprint | 3 | 0.4m/s² | / | Random Point on Any Straight | Random straight activations are almost always useless |
| Countermeasure | △ | ✕ | 3.12 | 160 | Sprint | 3 | 0.2m/s² | / | First Half of the Pack but not 1st, at Random Point during Second Half of Mid-Race | Gamble accel, if it procs right before Mid-Race ends it'll be effective |
| Plan X | △ | ✕ | 3.75 | 160+160 | Sprint | 3 | 0.4m/s² | / | First Half of the Pack but not 1st, at Random Point during Second Half of Mid-Race | Gamble accel, if it procs right before Mid-Race ends it'll be effective |
| Updrafters | ◯ | ✕ | 3.12 | 160 | Mile | 3 | 0.2m/s² | / | 6th-9th/7th-12th Place, at Random Point during Late-Race | Good but inconsistently effective accel for Lates/Ends in Mile |
| Furious Feat | ◯ | ✕ | 3.75 | 160+160 | Mile | 3 | 0.4m/s² | / | 6th-9th/7th-12th Place, at Random Point during Late-Race | Good but inconsistently effective accel for Lates/Ends in Mile |
| Acceleration | △ | ✕ | 3.12 | 160 | Mile | 3 | 0.2m/s² | / | Overtake, during Mid-Race | Fairly consistent but Mid-Race accel is useless |
| Step on the Gas! | △ | ✕ | 3.75 | 160+160 | Mile | 3 | 0.4m/s² | / | Overtake, during Mid-Race | Fairly consistent but Mid-Race accel is useless |
| Red Shift/LP1211-M | ▲ | ✕ | 2.5 | 200 | / | 2.4 | 0.2m/s² | / | 1st-5th Place, on Final Corner | Powerful accel for Fronts/Paces, especially on tracks where Last Spurt Mode begins slightly before or on the Final Corner |
| Shooting for Victory! | ▲ | ◎ | 2.5 | 200 | / | 2.4 | 0.2m/s² | / | First Half of the Pack but not 1st-2nd Place, on Second Half of Final Corner | Powerful accel for Paces/Lates, especially on tracks where Last Spurt Mode begins slightly before or on the Second Half of the Final Corner |
| Let's Pump Some Iron! | ▲ | ◎ | 2.5 | 200 | / | 2.4 | 0.2m/s² | / | 6th (for CM)/8th (for TT) Place, on a Corner, during Late-Race or beyond | Strongest but most inconsistent accel for Lates/Ends on tracks where Last Spurt Mode begins slightly before or on the Final Corner |
| Angling and Scheming | ▲ | ◎ | 2.5 | 200 | / | 2.4 | 0.2m/s² | / | 1st Place, on a Corner, during Late-Race or beyond | Strongest accel for Fronts on tracks where Last Spurt Mode begins on a Corner |
| Condor's Fury | ▲ | ✕ | 2.5 | 200 | / | 2.4 | 0.2m/s² | / | Have Overtake Target, at First ¾ of the Pack but not 1st-3rd Place, on Final Corner | Powerful accel for Lates/Ends, especially on tracks where Last Spurt Mode begins slightly before or on the Final Corner |
| KEEP IT REAL. | △ | ✕ | 2.5 | 200 | / | 3.6 | 0.1m/s² | / | Have Overtake Target, at 40%-70% of the Pack, in Second Half of Race | Mostly useless accel but consistent activation |
| Moving Past, and Beyond | △ | ✕ | 2.5 | 200 | / | 2.4 | 0.2m/s² | No Rushed | 5th-6th/6th-8th Place, on Final Corner, during Mid-Race<br>OR<br>5th-6th/6th-8th Place, on Any Corner, during Late-Race or beyond |  |

#### Stamina Recovery Skills

Skills that restore HP (stamina) during the race. 49 skills are listed.

| Skill Name | Rank (Team Trials) | Rank (CM6) | Score/SP | Base Cost | Ground/Distance/Style | Base Duration (s) | Effect (Self) | Effect (Target) | Effect Target(s) | Precondition(s) | Condition(s) | Why? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Corner Recovery ◯ | ◎ | ◎ | 2.94 | 170 | / | Instant | 1.5% HP | / | / | / | Random Point on Corner 1<br>If Corner 1 does not exist, then First Corner (2/3/4) instead | Consistent and effective recovery |
| Swinging Maestro | ◎ | ◎ | 3.53 | 170+170 | / | Instant | 5.5% HP | / | / | / | Random Point on Corner 1<br>If Corner 1 does not exist, then First Corner (2/3/4) instead | Consistent and effective recovery |
| Straightaway Recovery | △ | △ | 2.94 | 170 | / | Instant | 1.5% HP | / | / | / | Random Point on Any Straight | Inconsistent, it might be wasted on an early or late activation |
| Breath of Fresh Air | △ | △ | 3.53 | 170+170 | / | Instant | 5.5% HP | / | / | / | Random Point on Any Straight | Inconsistent, it might be wasted on an early or late activation |
| Lay Low | △ | ✕ | 3.12 | 160 | / | Instant | 1.5% HP | / | / | / | Blocked in Front for ≥1s, during Early-Race or Mid-Race, ≥5s after Race Start | Might proc in Early-Race which might overflow HP |
| Iron Will | △ | ✕ | 3.75 | 160+160 | / | Instant | 5.5% HP | / | / | / | Blocked in Front for ≥1s, during Early-Race or Mid-Race, ≥5s after Race Start | Might proc in Early-Race which might overflow HP |
| Pace Strategy | △ | ✕ | 2.94 | 170 | / | Instant | 1.5% HP | / | / | / | Be overtaken, during Mid-Race | Being overtaken is an inconsistent condition<br>More suitable on long, backline Run Styles |
| Indomitable | △ | ✕ | 3.53 | 170+170 | / | Instant | 5.5% HP | / | / | / | Be overtaken, during Mid-Race | Being overtaken is an inconsistent condition<br>More suitable on long, backline Run Styles |
| Calm in a Crowd | ✕ | ✕ | 2.94 | 170 | / | Instant | 1.5% HP | / | / | / | Surrounded, during Mid-Race | Almost impossible to be boxed in on all sides in CM |
| Unruffled | ✕ | ✕ | 3.53 | 170+170 | / | Instant | 5.5% HP | / | / | / | Surrounded, during Mid-Race | Almost impossible to be boxed in on all sides in CM |
| Triple 7s | △ | ▲ | 3.12 | 160 | / | Instant | 1.5% HP | / | / | / | Activates 777m before Race End | Consistent, but only effective on <2400m tracks, useful for some Uma that rely on Stamina skill procs |
| Shake It Out | △ | ✕ | 5 | 100 | / | Instant | 1.5% HP | / | / | / | ≥3 Skill Activations during Late-Race and beyond | Late-Race recovery is ineffective<br>consider acquiring it only for Team Trials because it's very cheap |
| Ignited Spirit STA | △ | △ | 2.5 | 200 | / | Instant | 1.5% HP | / | / | / | Random Point during Mid-Race | Definitely an option but it costs more than a usual skill (at 200 base SP) |
| Burning Spirit STA | △ | △ | 3 | 200+200 | / | Instant | 5.5% HP | / | / | / | Random Point during Mid-Race | Definitely an option but it costs more than a usual skill (at 200 base SP) |
| Moxie | △ | ◯ | 2.78 | 180 | Front Runner | Instant | 1.5% HP | / | / | / | Uphill, ≥10s after Race Start | Consistent activation but recovery can be useless when<br>the uphill is located at anywhere other than Mid-Race |
| Restless | △ | △ | 3.33 | 180+180 | Front Runner | Instant | 5.5% HP | / | / | / | Uphill, ≥10s after Race Start | Consistent activation but recovery can be useless when<br>the uphill is located at anywhere other than Mid-Race |
| Stamina to Spare | △ | ◯ | 2.78 | 180 | Pace Chaser | Instant | 1.5% HP | / | / | / | First Half of the Pack, at a Random Point during Second Half of Early-Race | Stamina to Spare is okay as its recovery is unlikely to overflow (making it a decent choice),<br>but Calm and Collected may recover too much in a few situations (making it less consistent) |
| Calm and Collected | △ | ◎ | 3.33 | 180+180 | Pace Chaser | Instant | 5.5% HP | / | / | / | First Half of the Pack, at a Random Point during Second Half of Early-Race | Stamina to Spare is okay as its recovery is unlikely to overflow (making it a decent choice),<br>but Calm and Collected may recover too much in a few situations (making it less consistent) |
| Preferred Position | ◎ | ◯ | 2.78 | 180 | Pace Chaser | Instant | 1.5% HP | / | / | / | First Half of the Pack, at a Random Point during Mid-Race | Consistent and effective recovery |
| Race Planner | ◎ | ◎ | 3.33 | 180+180 | Pace Chaser | Instant | 5.5% HP | / | / | / | First Half of the Pack, at a Random Point during Mid-Race | Consistent and effective recovery |
| Hydrate | ◎ | ◯ | 2.78 | 180 | Pace Chaser | Instant | 1.5% HP | / | / | / | Random Point during Mid-Race | Consistent and effective recovery |
| Gourmand | ◎ | ◎ | 3.33 | 180+180 | Pace Chaser | Instant | 5.5% HP | / | / | / | Random Point during Mid-Race | Consistent and effective recovery |
| A Small Breather | △ | ✕ | 2.78 | 180 | Late Surger | Instant | 1.5% HP | / | / | / | Random Point during Late-Race | Late-Race recovery is ineffective, Last Spurt recalculation isn't added until 1st Year Anniversary |
| Relax | △ | ✕ | 3.33 | 180+180 | Late Surger | Instant | 5.5% HP | / | / | / | Random Point during Late-Race | Late-Race recovery is ineffective, Last Spurt recalculation isn't added until 1st Year Anniversary |
| Be Still | △ | ◯ | 2.78 | 180 | Late Surger | Instant | 1.5% HP | / | / | / | 5th-9th/6th-12th Place, at Random Point during Second Half of Mid-Race |  |
| Lie in Wait | △ | ◎ | 3.33 | 180+180 | Late Surger | Instant | 5.5% HP | / | / | / | 5th-9th/6th-12th Place, at Random Point during Second Half of Mid-Race |  |
| Standing By | △ | ✕ | 2.78 | 180 | End Closer | Instant | 1.5% HP | / | / | / | Last 25% of the Pack (by Distance), at Random Point during Mid-Race | Somewhat consistent, but may be undesirable for well-built End Closers<br>since they can probably reach positions above 75% by distance and hence, not activate this skill |
| Sleeping Lion | △ | ✕ | 3.33 | 180+180 | End Closer | Instant | 5.5% HP | / | / | / | Last 25% of the Pack (by Distance), at Random Point during Mid-Race | Somewhat consistent, but may be undesirable for well-built End Closers<br>since they can probably reach positions above 75% by distance and hence, not activate this skill |
| After-School Stroll | △ | ✕ | 2.94 | 170 | End Closer | Instant | 1.5% HP | / | / | / | Downhill, ≥10s after Race Start | Consistent activation but recovery can be useless when<br>the downhill is located at anywhere other than Mid-Race |
| Go-Home Specialist | △ | ✕ | 3.53 | 170+170 | End Closer | Instant | 5.5% HP | / | / | / | Downhill, ≥10s after Race Start | Consistent activation but recovery can be useless when<br>the downhill is located at anywhere other than Mid-Race |
| Levelheaded | △ | △ | 2.78 | 180 | End Closer | Instant | 1.5% HP | / | / | / | Blocked in Front for ≥1s, ≥10s after Race Start | Getting blocked is a decently consistent condition for End Closers |
| Wait-and-See | ▲ | ✕ | 3.12 | 160 | Sprint | 3 | 1.5% HP & 0.1m/s² | / | / | / | 6th-9th/7th-12th Place, at Random Point during Mid-Race | Only for Late Surgers/End Closers (only King Halo for now), the extra acceleration effect is useless |
| Watchful Eye | ▲ | ✕ | 3.12 | 160 | Mile | Instant | 1.5% HP | -0.05m꜀/s | All Umas ahead | / | 6th-9th/7th-12th Place, at Random Point during Second Half of Early-Race | Most effective Mile debuff skill, must-have for all Mile debuffers |
| Keen Eye | ▲ | ✕ | 3.75 | 160+160 | Mile | Instant | 5.5% HP | -0.2m꜀/s | All Umas ahead | / | 6th-9th/7th-12th Place, at Random Point during Second Half of Early-Race | Most effective Mile debuff skill, must-have for all Mile debuffers |
| Rosy Outlook | △ | ✕ | 3.12 | 160 | Medium | Instant | 1.5% HP | / | / | / | 1st-3rd Place, at Random Point in Mid-Race | Consistent recovery for Front Runners and perhaps even Pace Chasers |
| Trackblazer | △ | ✕ | 3.75 | 160+160 | Medium | Instant | 5.5% HP | / | / | / | 1st-3rd Place, at Random Point in Mid-Race | Consistent recovery for Front Runners and perhaps even Pace Chasers |
| Soft Step | △ | ✕ | 3.12 | 160 | Medium | Instant | 1.5% HP | / | / | / | Change Lanes, ≥10s after Race Start | Consistent but effect isn't that strong<br>Rare ver. is actually worse as this tends to activate early on and the 5.5% recovery could overflow |
| Miraculous Step | △ | ✕ | 3.75 | 160+160 | Medium | Instant | 5.5% HP | / | / | / | Change Lanes, ≥10s after Race Start | Consistent but effect isn't that strong<br>Rare ver. is actually worse as this tends to activate early on and the 5.5% recovery could overflow |
| Deep Breaths | △ | △ | 3.12 | 160 | Long | Instant | 1.5% HP | / | / | / | Random Point on Any Straight | Inconsistent, it might be wasted on an early or late activation |
| Cooldown | △ | △ | 3.75 | 160+160 | Long | Instant | 5.5% HP | / | / | / | Random Point on Any Straight | Inconsistent, it might be wasted on an early or late activation |
| Extra Tank | △ | △ | 3.12 | 160 | Long | Instant | 1.5% HP | / | / | / | ≤30% HP Remaining | If your HP drops to zero, you're cooked anyway, no recovery can save you |
| Adrenaline Rush | △ | △ | 3.75 | 160+160 | Long | Instant | 5.5% HP | / | / | / | ≤30% HP Remaining | If your HP drops to zero, you're cooked anyway, no recovery can save you |
| Passing Pro | △ | △ | 3.12 | 160 | Long | Instant | 1.5% HP | / | / | / | Have Overtake Target, ≥5s after Race Start | Mostly consistent but activation can occur on Early-Race, diminishing its value |
| U=ma2 | △ | ✕ | 2.5 | 200 | / | 2.4 | 1.5% HP & 0.05m/s | / | / | / | First ⅖ of the Pack but ≥3rd Place, on Any Corner, during Second Half of the Race | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Pure Heart | △ | △ | 2.5 | 200 | / | Instant | 3.5% HP | / | / | / | First ⅖ of the Pack but ≥2nd Place, at Random Point during Mid-Race | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Super-Duper Climax | △ | ✕ | 2.5 | 200 | / | Instant | 1.5% HP | / | / | / | 6th-9th/7th-12th Place, ≥1 Nearby Uma(s), on Final Corner | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Superior Heal | △ | △ | 2.5 | 200 | / | Instant | 1.5% HP | / | / | / | Overtake, at Last ⅗ of the Pack, during Mid-Race | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Dazzl'n ♪ Diver | △ | ✕ | 2.5 | 200 | / | Instant | 1.5% HP | / | / | / | Activate ≥2 Skills, at First 70% of the Pack but not 1st Place, during Mid-Race | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Every Rose Has Its Fangs | △ | ✕ | 2.5 | 200 | / | Instant | 1.5% HP | -0.25% HP | All Umas ahead | / | Be an Overtake Target for ≥1s, at First Half of the Pack but not 1st Place, during Mid-Race | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |

#### Other (Orange) Skills

Skills that do not fit the other groups, such as lateral movement and positioning. 25 skills are listed.

| Skill Name | Rank (Team Trials) | Rank (CM6) | Score/SP | Base Cost | Ground/Distance/Style | Base Duration(s) | Effect | Condition(s) | Why? |
|---|---|---|---|---|---|---|---|---|---|
| Prudent Positioning | △ | ▲ | 4.17 | 120 | / | 3 | 0.035mₗ/s | Random Point during Early-Race | Use with Dodging Danger for a very powerful Early-Race burst of speed (Front Runner only) |
| Center Stage | △ | ✕ | 5 | 120+120 | / | 3 | 0.045mₗ/s | Random Point during Early-Race | Never use for Front-Runners that want to run the Dodging Danger tech |
| Go with the Flow | △ | ✕ | 4.17 | 120 | / | 3 | 0.025mₗ/s | Random Point during Late-Race | Random non-Early-Race Lane Movement Speed for non-Front-Runners are useless<br>Take only because they are very cheap and if you have no other options |
| Lane Legerdemain | △ | ✕ | 5 | 120+120 | / | 3 | 0.035mₗ/s | Random Point during Late-Race | Random non-Early-Race Lane Movement Speed for non-Front-Runners are useless<br>Take only because they are very cheap and if you have no other options |
| Ignited Spirit WIT | △ | ▲ | 2.5 | 200 | / | 3 | 0.015mₗ/s & 5 FoV | Random Point during Early-Race | Use with Dodging Danger for a very powerful Early-Race burst of speed (Front Runner only) |
| Burning Spirit WIT | △ | ✕ | 3 | 200+200 | / | 3 | 0.035mₗ/s & 15 FoV | Random Point during Early-Race | Never use for Front-Runners that want to run the Dodging Danger tech |
| Dodging Danger | △ | ⍟ | 4.55 | 110 | Front Runner | 3 | 0.025mₗ/s | Blocked in any direction for ≥1s, during Early-Race | Use with Prudent Positioning/Ignition Spirit WIT for a very powerful Early-Race burst of speed (Front Runner only) |
| Sixth Sense | △ | ✕ | 5.45 | 110+110 | Front Runner | 3 | 0.035mₗ/s | Blocked in any direction for ≥1s, during Early-Race | Never use for Front-Runners that want to run the "Prudent Positioning" + "Dodging Danger" combo |
| Meticulous Measures | △ | ✕ | 3.57 | 140 | Sprint | 4 | 0.025mₗ/s & 0.2m/s² | Random Point during Mid-Race | Random non-Early-Race Lane Movement Speed for non-Front-Runners are useless<br>There is no need for any additional acceleration (unless it's toward the very end which is very RNG-dependent)<br>Take only because they are very cheap and if you have no other options |
| Perfect Prep! | △ | ✕ | 4.29 | 140+140 | Sprint | 4 | 0.035mₗ/s & 0.3m/s² | Random Point during Mid-Race | Random non-Early-Race Lane Movement Speed for non-Front-Runners are useless<br>There is no need for any additional acceleration (unless it's toward the very end which is very RNG-dependent)<br>Take only because they are very cheap and if you have no other options |
| Thunderbolt Step | △ | ✕ | 3.57 | 140 | Medium | 4 | 0.025mₗ/s & 0.2m/s² | 6th-9th/7th-12th Place, at Random Point during Mid-Race | Random non-Early-Race Lane Movement Speed for non-Front-Runners are useless<br>There is no need for any additional acceleration (unless it's toward the very end which is very RNG-dependent)<br>Take only because they are very cheap and if you have no other options |
| Lightning Step | △ | ✕ | 4.29 | 140+140 | Medium | 4 | 0.035mₗ/s & 0.3m/s² | 6th-9th/7th-12th Place, at Random Point during Mid-Race | Random non-Early-Race Lane Movement Speed for non-Front-Runners are useless<br>There is no need for any additional acceleration (unless it's toward the very end which is very RNG-dependent)<br>Take only because they are very cheap and if you have no other options |
| Forward, March! | △ | ✕ | 3.57 | 140 | Dirt | 3 | 0.025mₗ/s & 0.2m/s² | Random Point during Late-Race | Very good Dirt accel skill disguised as a lane movement speed skill |
| Lead the Charge! | △ | ✕ | 4.29 | 140+140 | Dirt | 3 | 0.035mₗ/s & 0.3m/s² | Random Point during Late-Race | Very good Dirt accel skill disguised as a lane movement speed skill |
| Focus | ◎ | ▲ | 3.57 | 140 | / | Instant | 0.9× Start Time | / | Only take for Front Runners, Focus reduces the chance of a Late Start, while Concentration makes it impossible<br>You also get score for "strong starts" in Team Trials, so Concentration is always good there |
| Concentration | ◎ | ▲ | 4.29 | 140+140 | / | Instant | 0.4× Start Time | / | Only take for Front Runners, Focus reduces the chance of a Late Start, while Concentration makes it impossible<br>You also get score for "strong starts" in Team Trials, so Concentration is always good there |
| Studious | △ | ✕ | 4.17 | 120 | Late Surger | 3 | 5 FoV | Random Point during Mid-Race | Extra FoV is mostly useless<br>Take only because they are very cheap and if you have no other options |
| The Bigger Picture | △ | ✕ | 5 | 120+120 | Late Surger | 3 | 15 FoV | Random Point during Mid-Race | Extra FoV is mostly useless<br>Take only because they are very cheap and if you have no other options |
| I Can See Right Through You | △ | ✕ | 4.55 | 110 | End Closer | 3 | 5 FoV | Change Lanes | Extra FoV is mostly useless<br>Take only because they are very cheap and if you have no other options |
| The Coast Is Clear! | △ | ✕ | 5.45 | 110+110 | End Closer | 3 | 10 FoV | Change Lanes | Extra FoV is mostly useless<br>Take only because they are very cheap and if you have no other options |
| Strategist | △ | ✕ | 4.55 | 110 | End Closer | 3 | 5 FoV | 6th-9th/7th-12th Place, at Random Point during Late-Race | Extra FoV is mostly useless<br>Take only because they are very cheap and if you have no other options |
| Crusader | △ | ✕ | 5.45 | 110+110 | End Closer | 3 | 15 FoV | 6th-9th/7th-12th Place, at Random Point during Late-Race | Extra FoV is mostly useless<br>Take only because they are very cheap and if you have no other options |
| Hawkeye | △ | ✕ | 4.55 | 110 | Medium | 3 | 10 FoV | Random Point during Early-Race | Extra FoV is mostly useless<br>Take only because they are very cheap and if you have no other options |
| Clairvoyance | △ | ✕ | 5.45 | 110+110 | Medium | 3 | 15 FoV | Random Point during Early-Race | Extra FoV is mostly useless<br>Take only because they are very cheap and if you have no other options |
| Runaway | ▲ | ▲ | 6 | 200 | Front Runner | Infinite | Change "Front Runner"<br>to "Great Escape" | / | Dependent on what you want/need |

#### Debuff Skills

Skills that slow, disrupt or otherwise hinder opposing Umas. 27 skills are listed.

| Skill Name | Rank (Team Trials) | Rank (CM4) | Score/SP | Base Cost | Ground/Distance/Style | Base Duration(s) | Effect (Self) | Effect (Target) | Effect Target(s) | Precondition(s) | Condition(s) | Why? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hesitant [Run Style]s | ◎ | ◎ | 3.85 | 130 | / | 3 | / | -0.15m꜀/s | All [Run Style]s | / | Random Point in Late-Race | Cheap and consistent, speed debuff is generally always good |
| Frenzied [Run Style]s | ◯ | ◎ | 3.85 | 130 | / | 5 | / | Increase Rush Time | "Rushed" [RS]s | / | [Run Style] is "Rushed" | Usually only hits one Uma, but the 5s longer "Rushed" will decimate her HP |
| Subdued [Run Style]s | ◎ | ◎ | 3.85 | 130 | / | Instant | / | -1% HP | All [Run Style]s | / | Random Point in Early-Race, ≥5 after Race Start | Cheap and consistent |
| Flustered [Run Style]s | ◎ | ◎ | 3.85 | 130 | / | Instant | / | -1% HP | All [Run Style]s | / | Random Point in Mid-Race | Cheap and consistent |
| Trick (Front) | ◎ | ◎ | 3.57 | 140 | / | Instant | / | -1% HP | Rushed Uma(s) behind | / | First Half of the Pack, ≥1 "Rushed" Uma behind | Helps to nail the coffin on Rushed Umas |
| Tantalizing Trick | ◎ | ◎ | 4.29 | 140+140 | / | Instant | / | -3% HP | Rushed Uma(s) behind | / | First Half of the Pack, ≥1 "Rushed" Uma behind | Helps to nail the coffin on Rushed Umas |
| Trick (Rear) | ◎ | ◎ | 3.57 | 140 | / | Instant | / | -1% HP | Rushed Uma(s) ahead | / | 2nd-9th/12th Place, ≥1 "Rushed" Uma ahead | Helps to nail the coffin on Rushed Umas |
| Restart | ✕ | ✕ | 3.85 | 130 | Front Runner | 3 | / | -0.1m/s² | All Umas ahead | / | Last Half of the Pack, at Random Point during Early-Race, ≥5s after Race Start | Accel debuff is great but occuring at a Random Point can cause it to try proc'ing before 5s is up, preventing activation |
| Disorient | △ | △ | 4.55 | 110 | Pace Chaser | 3 | / | -3 FoV | All Umas behind | / | First Half of the Pack, at Random Point during Late-Race | FoV is an almost entirely useless stat |
| Dazzling Disorientation | △ | △ | 5.45 | 110+110 | Pace Chaser | 3 | / | -5 FoV | All Umas behind | / | First Half of the Pack, at Random Point during Late-Race | FoV is an almost entirely useless stat |
| Sharp Gaze | ◎ | ◎ | 2.78 | 180 | Late Surger | Instant | / | -1% HP | All Umas within Fov | / | Last Half of the Pack, at Random Point during Late-Race | Consistent and strong stamina debuff |
| All-Seeing Eyes | ◎ | ◎ | 3.33 | 180+180 | Late Surger | Instant | / | -3% HP | All Umas within Fov | / | Last Half of the Pack, at Random Point during Late-Race | Consistent and strong stamina debuff |
| Intense Gaze | △ | ◯ | 2.78 | 180 | End Closer | 3 | / | -0.15m꜀/s | All Umas within FoV | / | Not 1st Place, at Random Point during Late-Race | Good speed debuff, but since only Umas in FoV are affected, it's not that strong |
| Intimidate | △ | ✕ | 2.94 | 170 | Sprint | 3 | / | -0.2m꜀/s | All Umas behind | / | First Half of the Pack, at Random Point in Early-Race, ≥5s after Race Start | Very strong speed debuff but activates inconsistently due to accumulatetime≥5 + at a Random Point,<br>still worth taking if you have the SP to spare |
| Adored by All | △ | ✕ | 3.53 | 170+170 | Sprint | 3 | / | -0.25m꜀/s | All Umas behind | / | First Half of the Pack, at Random Point in Early-Race, ≥5s after Race Start | Very strong speed debuff but activates inconsistently due to accumulatetime≥5 + at a Random Point,<br>still worth taking if you have the SP to spare |
| Stop Right There! | ✕ | ✕ | 2.94 | 170 | Sprint | Instant | / | -1% HP & 0.05m/s² | All Umas ahead | / | Last Half of the Pack, at Random Point during Early-Race, ≥5s after Race Start | Only for Sprint Late Surgers/End Closers (only King Halo for now), Random Point also causes inconsistent activation |
| Speed Eater | △ | ✕ | 3.12 | 160 | Mile | 3 | 0.15m/s | -0.15m꜀/s | 5 closest Umas behind | / | 1st-3rd Place, at Random Point during Mid-Race | Very good if Uma can take the lead early but not always consistent |
| Opening Gambit | ✕ | ✕ | 3.12 | 160 | Mile | 3 | / | -0.1m/s² | All Umas ahead | / | Last Half of the Pack, at Random Point during Early-Race, ≥3s after Race Start | Accel debuff is great but occuring at a Random Point can cause it to try proc'ing before 3s is up, preventing activation |
| Battle Formation | ✕ | ✕ | 3.75 | 160+160 |  | 3 | / | -0.3m/s² | All Umas ahead | / | Last Half of the Pack, at Random Point during Early-Race, ≥3s after Race Start | Accel debuff is great but occuring at a Random Point can cause it to try proc'ing before 3s is up, preventing activation |
| Tether | ◎ | ✕ | 3.12 | 160 | Medium | 3 | / | -0.15m꜀/s | All Umas ahead | / | Last Half of the Pack, at Random Point during Late-Race | Devastating speed debuff for Medium Late Surgers/End Closers (especially Dominator) |
| Dominator | ◎ | ✕ | 3.75 | 160+160 | Medium | 3 | / | 0.25m꜀/s | All Umas ahead | / | Last Half of the Pack, at Random Point during Late-Race | Devastating speed debuff for Medium Late Surgers/End Closers (especially Dominator) |
| Murmur | ◎ | ✕ | 3.12 | 160 | Medium | Instant | / | -1% HP | All Umas ahead | / | Blocked in Front for ≥1s, during Mid-Race | Consistent and strong stamina debuff |
| Mystifying Murmur | ◎ | ✕ | 3.75 | 160+160 | Medium | Instant | / | -3% HP | All Umas ahead | / | Blocked in Front for ≥1s, during Mid-Race | Consistent and strong stamina debuff |
| Stamina Eater | ◯ | ◎ | 3.12 | 160 | Long | Instant | 1.5% HP | -0.5% HP | 5 closest Umas ahead | / | ≥5th Place, at Random Point in Mid-Race | Acts as a cheaper HP recovery skill that simultaneously marginally drains HP |
| Stamina Siphon | ◎ | ◎ | 3.75 | 160+160 | Long | Instant | 3.5% HP | -1% HP | 5 closest Umas ahead | / | ≥5th Place, at Random Point in Mid-Race | Acts as a cheaper HP recovery skill that simultaneously marginally drains HP |
| Smoke Screen | △ | △ | 4.55 | 110 | Long | 3 | / | -5 FoV | All Umas ahead | / | Random Point in Late-Race | FoV is an almost entirely useless stat |
| Illusionist | △ | △ | 5.45 | 110+110 | Long | 3 | / | -10 FoV | All Umas ahead | / | Random Point in Late-Race | FoV is an almost entirely useless stat |

#### Green (Passive) Skills

Passive skills that grant stat boosts or other permanent effects. 34 skills are listed.

| Skill Name | Rank (Team Trials) | Rank (CM) | Score/SP | Base Cost | Ground/Distance/Style | Base Duration(s) | Effect | Precondition(s) | Condition(s) | Why? |
|---|---|---|---|---|---|---|---|---|---|---|
| [Rotation]-Handed ◯ | ◯ | ◎ | 5.56 | 90 | / | Infinite | 40 Speed | / | Race is [Rotation] | Speed stat increase is significant |
| [Rotation]-Handed ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Infinite | 60 Speed | / | Race is [Rotation] | Speed stat increase is significant |
| [Season] Runner ◯ | ◯ | ◎ | 5.56 | 90 | / | Infinite | 40 Speed | / | Race is in [Season] | Speed stat increase is significant |
| [Season] Runner ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Infinite | 60 Speed | / | Race is in [Season] | Speed stat increase is significant |
| Fall Frenzy | ✕ | ✕ | 3.64 | 90+110+130 | / | Infinite | 60 Speed & 60 Power | / | Race is in Autumn | Take only on Autumn CMs |
| Outer Post Proficiency ◯ | ✕ | ✕ | 5.56 | 90 | / | Infinite | 40 Speed | / | Uma is at Post Numbers 6-8 | Post Numbers 6-8 is inconsistent |
| Outer Post Proficiency ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Infinite | 60 Speed | / | Uma is at Post Numbers 6-8 | Post Numbers 6-8 is inconsistent |
| Maverick ◯ | ✕ | ✕ | 5.56 | 90 | / | Infinite | 60 Speed | / | No other Umas use [Run Style] | Very rare to have no Umas use your run style |
| Maverick ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Infinite | 80 Speed | / | No other Umas use [Run Style] | Very rare to have no Umas use your run style |
| Long Shot ◯ | ✕ | ✕ | 5.56 | 90 | / | Infinite | 40 Speed | / | Popularity/Favourite ≥4th | Popularity-dependent skills are inconsistent |
| Long Shot ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Infinite | 60 Speed | / | Popularity/Favourite ≥4th | Popularity-dependent skills are inconsistent |
| Sympathy | ✕ | ▲ | 7.14 | 70 | / | Infinite | 40 Speed | / | ≥4 other Umas share this skill with you | Practically impossible to proc |
| Lone Wolf | ◎ | ◎ | 7.14 | 70 | / | Infinite | 40 Speed | / | No other Umas share this skill with you | Easy to proc, you either benefit (you proc) or make it even (you prevent someone else's from proc'ing) |
| [Location] Racecourse ◯ | △ | ◎ | 5.56 | 90 | / | Infinite | 40 Stamina | / | Race is at [Location] | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| [Location] Racecourse ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Infinite | 60 Stamina | / | Race is at [Location] | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Yodo Invicta | ✕ | ✕ | 3.64 | 90+110+130 | / | Infinite | 60 Stamina & 60 Wit | / | Race is at Kyoto | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Standard Distance ◯ | ◯ | ◎ | 5.56 | 90 | / | Infinite | 40 Stamina | / | Race Distance is a multiplie of 400m | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Standard Distance ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Infinite | 60 Stamina | / | Race Distance is a multiplie of 400m | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Non-Standard Distance ◯ | ◯ | ◎ | 5.56 | 90 | / | Infinite | 40 Stamina | / | Race Distance is not a multiple of 400m | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Non-Standard Distance ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Infinite | 60 Stamina | / | Race Distance is not a multiple of 400m | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| [Ground Condition] Conditions ◯ | △ | ◎ | 5.56 | 90 | / | Infinite | 40 Power | / | Race ground condition is [Ground Condition] | Power Stat increase is decent but low priority |
| [Ground Condition] Conditions ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Infinite | 60 Power | / | Race ground condition is [Ground Condition] | Power Stat increase is decent but low priority |
| Competitive Spirit ◯ | ✕ | ✕ | 5.56 | 90 | / | Infinite | 40 Power | / | ≥40% other Umas use [Run Style] | It's unlikely for 40% of the lobby to use the same run style as you |
| Competitive Spirit ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Infinite | 60 Power | / | ≥40% other Umas use [Run Style] | It's unlikely for 40% of the lobby to use the same run style as you |
| [Weather] Days ◯ | △ | △ | 5.56 | 90 | / | Infinite | 40 Guts | / | Race weather is [Weather] | Guts is extremely unimportant, only take it you really need to |
| [Weather] Days ◎ | ✕ | △ | 2.5 | 90+110 | / | Infinite | 60 Guts | / | Race weather is [Weather] | Guts is extremely unimportant, only take it you really need to |
| Target in Sight ◯ | ✕ | ✕ | 5.56 | 90 | / | Infinite | 40 Guts | / | 1st Fav. uses the same [Run Style] as you | Guts is extremely unimportant, only take it you really need to |
| Target in Sight ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Infinite | 60 Guts | / | 1st Fav. uses the same [Run Style] as you | Guts is extremely unimportant, only take it you really need to |
| Inner Post Proficiency ◯ | ✕ | ✕ | 5.56 | 90 | / | Infinite | 40 Wit | / | Uma is at Post Numbers 1-3 | Post Numbers 1-3 is inconsistent |
| Inner Post Proficiency ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Infinite | 60 Wit | / | Uma is at Post Numbers 1-3 | Post Numbers 1-3 is inconsistent |
| [Run Style] Savvy ◯ | ◎ | ◯ | 4.55 | 110 | [Run Style] | Infinite | 40 Wit & 5 FoV | / | Uma uses [Run Style] | Consistent activation, FoV buff is useful for Nice Nature's All-Seeing Eyes |
| [Run Style] Savvy ◎ | △ | ▲ | 2.08 | 110+130 | [Run Style] | Infinite | 60 Wit & 10 FoV | / | Uma uses [Run Style] | Consistent activation, FoV buff is useful for Nice Nature's All-Seeing Eyes |
| Lucky Seven | ✕ | ✕ | 4.55 | 110 | / | Infinite | 40 Speed, Stamina, Power | / | Uma is at Post Number 7, 50% chance of activating | Inconsistent, even more so than the Post Proficiency skills |
| Super Lucky Seven | ✕ | ✕ | 5.45 | 110+110 | / | Infinite | 60 Speed, Stamina, Power | / | Uma is at Post Number 7, 50% chance of activating | Inconsistent, even more so than the Post Proficiency skills |


### 1.7 Tier Lists

Each list below ranks every skill, grouped by its **Team Trials** tier. Skills are **unordered within a tier**, so the lists are mainly for quick searching. The second mode (CM or PvP) appears in its own column, and a short "quick view" under each list groups skill names by that second ranking.

The master list covers all skills. The other eight lists are filtered for one running style (Front Runner, Pace Chaser, Late Surger, End Closer) or one distance (Sprint, Mile, Medium, Long).

> **Data note.** The source's tier lists occasionally show a Score/SP value that differs from the category table (for example, a few skills such as *Trick (Front)* and *15,000,000 CC* show two different values). Where they disagree, this guide uses the value from the skill's own category table.


#### Master Tier List (All Skills)

Skills are unordered within each tier; the list is mainly meant for quick searching (Ctrl+F). It covers 289 skills, grouped by their **Team Trials** tier. The CM rank of each skill is shown in its own column.

##### ◎ Top tier (Team Trials): 44 skills

| Skill | Team Trials | CM | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| [Run Style] Corners ◯ | ◎ | ⍟ | 3.85 | 130 | [Run Style] | Cheap and consistent, they are must-haves |
| [Run Style] Straightaways ◯ | ◎ | ⍟ | 3.85 | 130 | [Run Style] | Cheap and consistent, they are must-haves |
| [Distance] Corners ◯ | ◎ | ⍟ | 5 | 100 | [Distance] | Cheap and consistent, they are must-haves |
| [Distance] Straightaways ◯ | ◎ | ⍟ | 5 | 100 | [Distance] | Cheap and consistent, they are must-haves |
| Uma Stan | ◎ | ◎ | 3.12 | 160 | / | Best speed skill on longer tracks for non-Front-Runners, can help to release PDM on some longer tracks |
| Super Stan | ◎ | ◎ | 3.75 | 160+160 | / | Best speed skill on longer tracks for non-Front-Runners, can help to release PDM on some longer tracks |
| Tail Held High | ◎ | ◎ | 5 | 100 | / | Cheap and consistent, though note the condition of requiring 3 skill activations before acquiring it |
| Slipstream | ◎ | ◎ | 3.12 | 160 | / | Consistent and facilitates overtaking when activated |
| Playtime's Over! | ◎ | ◎ | 3.12 | 160 | / | Consistent and improves Uma's capacity to maintain her placement |
| Burning Spirit GUTS | ◎ | ◎ | 3 | 200+200 | / | Good random Late-Race accel but in the game's current state,<br>this skill's effect is likely 80% (when Total Guts ≤ 1200) or 90% (when 1200 < Total Guts ≤ 1600) |
| Fast-Paced | ◎ | ◎ | 2.78 | 180 | Front Runner | Consistent with easy conditions. Helps Front Runners maintain/regain their lead during the Mid-Race |
| Escape Artist | ◎ | ◎ | 3.33 | 180+180 | Front Runner | Consistent with easy conditions. Helps Front Runners maintain/regain their lead during the Mid-Race |
| 1,500,000 CC | ◎ | ◎ | 4.17 | 120 | Late Surger | Cheap and consistent |
| 15,000,000 CC | ◎ | ◎ | 5 | 120+120 | Late Surger | Cheap and consistent |
| Mile Maven | ◎ | ✕ | 3.75 | 160+160 | Mile | Mostly consistent but activation occurs during Early-Race where Uma may not have hit top speed, making target speed boosts obsolete (doesn't actually increase speed<br>since Uma's Current Speed hasn't reached Target Speed). Additionally, the skill may pick a point prior to the 5 seconds needed after the race starts to activate, making it proc inconsistently too |
| Unyielding Spirit | ◎ | ✕ | 4.17 | 120 | Mile | Cheap and consistent |
| Big-Sisterly | ◎ | ✕ | 5 | 120+120 | Mile | Cheap and consistent |
| Corner Recovery ◯ | ◎ | ◎ | 2.94 | 170 | / | Consistent and effective recovery |
| Swinging Maestro | ◎ | ◎ | 3.53 | 170+170 | / | Consistent and effective recovery |
| Preferred Position | ◎ | ◯ | 2.78 | 180 | Pace Chaser | Consistent and effective recovery |
| Race Planner | ◎ | ◎ | 3.33 | 180+180 | Pace Chaser | Consistent and effective recovery |
| Hydrate | ◎ | ◯ | 2.78 | 180 | Pace Chaser | Consistent and effective recovery |
| Gourmand | ◎ | ◎ | 3.33 | 180+180 | Pace Chaser | Consistent and effective recovery |
| Ignited Spirit PWR | ◎ | ◎ | 2.5 | 200 | / | It's like a weaker but universal Slick Surge/On Your Left! |
| Burning Spirit PWR | ◎ | ◎ | 3 | 200+200 | / | It's like a weaker but universal Slick Surge/On Your Left! |
| Early Lead | ◎ | ⍟ | 4.17 | 120 | Front Runner | Necessary skill for all Front Runners |
| Taking the Lead | ◎ | ⍟ | 5 | 120+120 | Front Runner | Necessary skill for all Front Runners |
| Focus | ◎ | ▲ | 3.57 | 140 | / | Only take for Front Runners, Focus reduces the chance of a Late Start, while Concentration makes it impossible<br>You also get score for "strong starts" in Team Trials, so Concentration is always good there |
| Concentration | ◎ | ▲ | 4.29 | 140+140 | / | Only take for Front Runners, Focus reduces the chance of a Late Start, while Concentration makes it impossible<br>You also get score for "strong starts" in Team Trials, so Concentration is always good there |
| Hesitant [Run Style]s | ◎ | ◎ | 3.85 | 130 | / | Random Point in Late-Race |
| Subdued [Run Style]s | ◎ | ◎ | 3.85 | 130 | / | Random Point in Early-Race, ≥5 after Race Start |
| Flustered [Run Style]s | ◎ | ◎ | 3.85 | 130 | / | Random Point in Mid-Race |
| Trick (Front) | ◎ | ◎ | 3.57 | 140 | / | First Half of the Pack, ≥1 "Rushed" Uma behind |
| Tantalizing Trick | ◎ | ◎ | 4.29 | 140+140 | / | First Half of the Pack, ≥1 "Rushed" Uma behind |
| Trick (Rear) | ◎ | ◎ | 3.57 | 140 | / | 2nd-9th/12th Place, ≥1 "Rushed" Uma ahead |
| Sharp Gaze | ◎ | ◎ | 2.78 | 180 | Late Surger | Last Half of the Pack, at Random Point during Late-Race |
| All-Seeing Eyes | ◎ | ◎ | 3.33 | 180+180 | Late Surger | Last Half of the Pack, at Random Point during Late-Race |
| Tether | ◎ | ✕ | 3.12 | 160 | Medium | Last Half of the Pack, at Random Point during Late-Race |
| Dominator | ◎ | ✕ | 3.75 | 160+160 | Medium | Last Half of the Pack, at Random Point during Late-Race |
| Murmur | ◎ | ✕ | 3.12 | 160 | Medium | Blocked in Front for ≥1s, during Mid-Race |
| Mystifying Murmur | ◎ | ✕ | 3.75 | 160+160 | Medium | Blocked in Front for ≥1s, during Mid-Race |
| Stamina Siphon | ◎ | ◎ | 3.75 | 160+160 | Long | ≥5th Place, at Random Point in Mid-Race |
| Lone Wolf | ◎ | ◎ | 7.14 | 70 | / | Easy to proc, you either benefit (you proc) or make it even (you prevent someone else's from proc'ing) |
| [Run Style] Savvy ◯ | ◎ | ◯ | 4.55 | 110 | [Run Style] | Consistent activation, FoV buff is useful for Nice Nature's All-Seeing Eyes |

##### ◯ Good (Team Trials): 27 skills

| Skill | Team Trials | CM | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| Professor of Curvature | ◯ | ◯ | 3.33 | 180+180 | / | Consistent, but expensive<br>Rare ver. has greater speed boost making it more worth to acquire |
| Beeline Burst | ◯ | ◯ | 3.53 | 170+170 | / | Consistent |
| It's On! | ◯ | ◯ | 3.53 | 170+170 | / | Consistent. Even better when used in tandem with Tail Held High, Slipstream, and Playtime's Over! |
| In Body and Mind | ◯ | ◯ | 3.53 | 170+170 | / | Useful and (fairly) consistent Last Spurt speed boost, falls short of ◎ because it could activate at the very end of a race |
| Ignited Spirit GUTS | ◯ | ◎ | 2.5 | 200 | / | Good random Late-Race accel but in the game's current state,<br>this skill's effect is likely 80% (when Total Guts ≤ 1200) or 90% (when 1200 < Total Guts ≤ 1600) |
| Position Pilfer | ◯ | ◯ | 2.78 | 180 | Late Surger | Consistent |
| Fast & Furious | ◯ | ◎ | 3.33 | 180+180 | Late Surger | Consistent |
| Outer Swell | ◯ | ◎ | 2.78 | 180 | Late Surger | Somewhat consistent but Target Speed boost during Final Corners are only useful if Uma will enter Last Spurt Mode in a few seconds/has already entered Last Spurt Mode.<br>Otherwise, boosting Target Speed right when Uma enters Last Spurt Mode renders it useless (doesn't actually increase speed since Uma's Current Speed hasn't reached Target Speed) |
| Rising Dragon | ◯ | ◎ | 3.33 | 180+180 | Late Surger | Somewhat consistent but Target Speed boost during Final Corners are only useful if Uma will enter Last Spurt Mode in a few seconds/has already entered Last Spurt Mode.<br>Otherwise, boosting Target Speed right when Uma enters Last Spurt Mode renders it useless (doesn't actually increase speed since Uma's Current Speed hasn't reached Target Speed) |
| Productive Plan | ◯ | ✕ | 3.12 | 160 | Mile | Mostly consistent but activation occurs during Early-Race where Uma may not have hit top speed, making target speed boosts obsolete (doesn't actually increase speed<br>since Uma's Current Speed hasn't reached Target Speed). Additionally, the skill may pick a point prior to the 5 seconds needed after the race starts to activate, making it proc inconsistently too |
| Shifting Gears | ◯ | ✕ | 3.12 | 160 | Mile | Consistent |
| Changing Gears | ◯ | ✕ | 3.75 | 160+160 | Mile | Consistent |
| Up-Tempo | ◯ | ✕ | 3.12 | 160 | Medium | Consistent |
| Killer Tunes | ◯ | ✕ | 3.75 | 160+160 | Medium | Consistent |
| Nimble Navigator | ◯ | ◎ | 3.33 | 150 | / | Strong accel but rng-dependent |
| No Stopping Me! | ◯ | ◎ | 4 | 150+150 | / | Strong accel but rng-dependent |
| Head-On | ◯ | ⍟ | 2.78 | 180 | Pace Chaser | Pace Chaser ver. of Slick Surge |
| Slick Surge | ◯ | ⍟ | 2.78 | 180 | Late Surger | Good but inconsistently effective accel |
| On Your Left! | ◯ | ⍟ | 3.33 | 180+180 | Late Surger | Good but inconsistently effective accel |
| Updrafters | ◯ | ✕ | 3.12 | 160 | Mile | Good but inconsistently effective accel for Lates/Ends in Mile |
| Furious Feat | ◯ | ✕ | 3.75 | 160+160 | Mile | Good but inconsistently effective accel for Lates/Ends in Mile |
| Frenzied [Run Style]s | ◯ | ◎ | 3.85 | 130 | / | [Run Style] is "Rushed" |
| Stamina Eater | ◯ | ◎ | 3.12 | 160 | Long | ≥5th Place, at Random Point in Mid-Race |
| [Rotation]-Handed ◯ | ◯ | ◎ | 5.56 | 90 | / | Speed stat increase is significant |
| [Season] Runner ◯ | ◯ | ◎ | 5.56 | 90 | / | Speed stat increase is significant |
| Standard Distance ◯ | ◯ | ◎ | 5.56 | 90 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Non-Standard Distance ◯ | ◯ | ◎ | 5.56 | 90 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |

##### ▲ Situational (Team Trials): 11 skills

| Skill | Team Trials | CM | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| Gap Closer | ▲ | ▲ | 3.12 | 160 | Sprint | Decent for Sprint Late Surgers/End Closers (only King Halo for now) |
| Blinding Flash | ▲ | ▲ | 3.75 | 160+160 | Sprint | Decent for Sprint Late Surgers/End Closers (only King Halo for now) |
| Wait-and-See | ▲ | ✕ | 3.12 | 160 | Sprint | Only for Late Surgers/End Closers (only King Halo for now), the extra acceleration effect is useless |
| Watchful Eye | ▲ | ✕ | 3.12 | 160 | Mile | Most effective Mile debuff skill, must-have for all Mile debuffers |
| Keen Eye | ▲ | ✕ | 3.75 | 160+160 | Mile | Most effective Mile debuff skill, must-have for all Mile debuffers |
| Red Shift/LP1211-M | ▲ | ✕ | 2.5 | 200 | / | Powerful accel for Fronts/Paces, especially on tracks where Last Spurt Mode begins slightly before or on the Final Corner |
| Shooting for Victory! | ▲ | ◎ | 2.5 | 200 | / | Powerful accel for Paces/Lates, especially on tracks where Last Spurt Mode begins slightly before or on the Second Half of the Final Corner |
| Let's Pump Some Iron! | ▲ | ◎ | 2.5 | 200 | / | Strongest but most inconsistent accel for Lates/Ends on tracks where Last Spurt Mode begins slightly before or on the Final Corner |
| Angling and Scheming | ▲ | ◎ | 2.5 | 200 | / | Strongest accel for Fronts on tracks where Last Spurt Mode begins on a Corner |
| Condor's Fury | ▲ | ✕ | 2.5 | 200 | / | Powerful accel for Lates/Ends, especially on tracks where Last Spurt Mode begins slightly before or on the Final Corner |
| Runaway | ▲ | ▲ | 6 | 200 | Front Runner | Dependent on what you want/need |

##### △ Low priority (Team Trials): 163 skills

| Skill | Team Trials | CM | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| [Run Style] Corners ◎ | △ | ⍟ | 1.85 | 130+140 | [Run Style] | Cheap and consistent, they are must-haves |
| [Run Style] Straightaways ◎ | △ | ⍟ | 1.85 | 130+140 | [Run Style] | Cheap and consistent, they are must-haves |
| [Distance] Corners ◎ | △ | ⍟ | 2.38 | 100+110 | [Distance] | Cheap and consistent, they are must-haves |
| [Distance] Straightaways ◎ | △ | ⍟ | 2.38 | 100+110 | [Distance] | Cheap and consistent, they are must-haves |
| Corner Adept ◯ | △ | △ | 2.78 | 180 | / | Consistent, but expensive<br>Rare ver. has greater speed boost making it more worth to acquire |
| Straightaway Adept | △ | △ | 2.94 | 170 | / | Consistent |
| Ramp Up | △ | △ | 2.94 | 170 | / | Consistent. Even better when used in tandem with Tail Held High, Slipstream, and Playtime's Over! |
| Homestretch Haste | △ | △ | 2.94 | 170 | / | Useful and (fairly) consistent Last Spurt speed boost, falls short of ◎ because it could activate at the very end of a race |
| Ignited Spirit SPD | △ | △ | 2.5 | 200 | / | 1.8s isn't very long and it costs 200 base SP |
| Burning Spirit SPD | △ | △ | 3 | 200+200 | / | 1.8s isn't very long and it costs 200 base SP |
| Leader's Pride | △ | ◎ | 2.78 | 180 | Front Runner | Inconsistent activation during Early-Race where overtaking doesn't happen frequently or consistently, consistency is directly proportional to track distance |
| Prepared to Pass | △ | △ | 2.78 | 180 | Pace Chaser | Consistent but Target Speed boost during Final Corners are only useful if Uma will enter Last Spurt Mode in a few seconds/has already entered Last Spurt Mode.<br>Otherwise, boosting Target Speed right when Uma enters Last Spurt Mode renders it useless (doesn't actually increase speed since Uma's Current Speed hasn't reached Target Speed) |
| Speed Star | △ | △ | 3.33 | 180+180 | Pace Chaser | Consistent but Target Speed boost during Final Corners are only useful if Uma will enter Last Spurt Mode in a few seconds/has already entered Last Spurt Mode.<br>Otherwise, boosting Target Speed right when Uma enters Last Spurt Mode renders it useless (doesn't actually increase speed since Uma's Current Speed hasn't reached Target Speed) |
| Early Start | △ | △ | 2.78 | 180 | End Closer | Very small speed boost, but it can unlock Pace-down Mode for a good amount of time so it isn't totally useless |
| Steadfast | △ | ✕ | 3.12 | 160 | Medium | Essentially a band-aid protective measure against losing the lead on the Final Corner, could be good but it's very situational |
| Unyielding | △ | ✕ | 3.75 | 160+160 | Medium | Essentially a band-aid protective measure against losing the lead on the Final Corner, could be good but it's very situational |
| All I've Got | △ | ✕ | 3.12 | 160 | Medium | Other than a few 2400m tracks, most Medium tracks have their Last Spurt Modes activate on a Corner, so this skill acts as a better Homestretch Haste/In Body and Mind |
| Come What May | △ | ✕ | 3.75 | 160+160 | Medium | Other than a few 2400m tracks, most Medium tracks have their Last Spurt Modes activate on a Corner, so this skill acts as a better Homestretch Haste/In Body and Mind |
| Inside Scoop | △ | ✕ | 3.12 | 160 | Long | Somewhat consistent but Target Speed boost during Final Corners are only useful if Uma will enter Last Spurt Mode in a few seconds/has already entered Last Spurt Mode.<br>Otherwise, boosting Target Speed right when Uma enters Last Spurt Mode renders it useless (doesn't actually increase speed since Uma's Current Speed hasn't reached Target Speed) |
| Innate Experience | △ | ✕ | 3.75 | 160+160 | Long | Somewhat consistent but Target Speed boost during Final Corners are only useful if Uma will enter Last Spurt Mode in a few seconds/has already entered Last Spurt Mode.<br>Otherwise, boosting Target Speed right when Uma enters Last Spurt Mode renders it useless (doesn't actually increase speed since Uma's Current Speed hasn't reached Target Speed) |
| Keeping the Lead | △ | △ | 3.12 | 160 | Long | 2.5m lead is somewhat possible in a Long race but still not the most consistent |
| Vanguard Spirit | △ | △ | 3.75 | 160+160 | Long | 2.5m lead is somewhat possible in a Long race but still not the most consistent |
| Pressure | △ | ✕ | 3.12 | 160 | Long | Overtakes and consequently, Target Speed boost is likely to occur toward the beginning of Last Spurt Mode,<br>rendering it useless (doesn't actually increase speed since Uma's Current Speed hasn't reached Target Speed) |
| Overwhelming Pressure | △ | ✕ | 3.75 | 160+160 | Long | Overtakes and consequently, Target Speed boost is likely to occur toward the beginning of Last Spurt Mode,<br>rendering it useless (doesn't actually increase speed since Uma's Current Speed hasn't reached Target Speed) |
| Top Pick | △ | ✕ | 2.78 | 180 | Dirt | Should have a consistent activation and is helpful for maintaining/securing/fighting for the lead |
| Trending in the Charts! | △ | ✕ | 3.33 | 180+180 | Dirt | Should have a consistent activation and is helpful for maintaining/securing/fighting for the lead |
| Certain Victory | △ | ◎ | 2.5 | 200 | / | Identical to OG Teio's unique with slightly looser conditions |
| Legacy of the Strong | △ | △ | 2.5 | 200 | / | Effects aren't bad but inconsistent activation |
| Shooting Star | △ | ◯ | 2.5 | 200 | / | Consistent activation, but weak effect |
| The View from the Lead is Mine! | △ | △ | 2.5 | 200 | / | Somewhat consistent activation for Front Runners, but weak effect |
| Sky-High Teio Step | △ | ◎ | 2.5 | 200 | / | Mostly consistent for non-Front-Runners, with strong effect |
| Triumphant Pulse | △ | ◎ | 2.5 | 200 | / | Consistent for non-Front-Runners, with strong effect |
| Anchors Aweigh! | △ | ✕ | 2.5 | 200 | / | Consistent for Late Surgers/End Closers but minimal effect |
| Resplendent Red Ace | △ | ▲ | 2.5 | 200 | / | Accel can come in handy occasionally but still very situational and slightly unreliable |
| Where There's a Will, There's a Way | △ | △ | 2.5 | 200 | / | Decent speed skill option for non-Front-Runners |
| The Duty of Dignity Calls | △ | ◯ | 2.5 | 200 | / | Final Corner Target Speed boost is inconsistent (especially in Med race), but it can be situationally good for Front Runners/Pace Chasers |
| Victoria por plancha ☆ | △ | ◎ | 2.5 | 200 | / | Activation is mostly consistent, some tracks benefit from a Last Straight accel |
| This Dance Is for Vittoria! | △ | ◯ | 2.5 | 200 | / | Fairly consistent activation but Final Corner Target Speed boost could be inconsistent |
| Behold Thine Emperor's Divine Might | △ | ◎ | 2.5 | 200 | / | Consistent for non-Front-Runners, with strong effect |
| Blazing Pride | △ | ◯ | 2.5 | 200 | / | Final Corner Target Speed boost is inconsistent (especially in Med race), but it can be situationally good for Late Surgers |
| ∴win Q.E.D. | △ | ◯ | 2.5 | 200 | / | Final Corner Target Speed boost is inconsistent (especially in Med race), but it can be situationally good for Front Runners |
| Flashy☆Landing | △ | ◯ | 2.5 | 200 | / | Acceleration on and beyond Final Corner is decent, conditions to activate may not be consistent unless you're Front Runner or Pace Chaser |
| Blue Rose Closer | △ | △ | 2.5 | 200 | / | Consistent, but weak effect |
| Our Ticket to Win! | △ | △ | 2.5 | 200 | / | Side block on Last Straight is rare, weak effect as well makes it not worth getting |
| Just a Little Farther! | △ | ✕ | 2.5 | 200 | / | Fairly consistent, but also weak |
| #LookatCurren | △ | △ | 2.5 | 200 | / | Slightly consistent but effect is really weak since it usually activates at Mid-Race |
| Nemesis | △ | ◯ | 2.5 | 200 | / | Consistent for Late Surgers/End Closers but effect is weak |
| SPARKLY☆STARDOM | △ | ▲ | 2.5 | 200 | / | Mostly consistent for most Front Runners and helps them maintain their lead |
| Shadow Break | △ | ◯ | 2.5 | 200 | / | Should be consistent but effect isn't great enough to be used over other similar uniques |
| Eternal Moments | △ | △ | 2.5 | 200 | / | Fairly consistent for non-Front-Runners, but the effect is weak |
| Flowery☆Maneuver | △ | ▲ | 2.5 | 200 | / | ① Strong for Front/Pace on some tracks to carry over speed on final corner<br>② Strong for Late/End on tracks that start the Last Spurt on final corner |
| You and Me! One-on-One! | △ | △ | 2.5 | 200 | / | Decent Last Straight speed skill for Late Surgers or End Closers |
| Lights of Vaudeville | △ | ◯ | 2.5 | 200 | / | Consistent activation but effectiveness depends on track |
| A Kiss for Courage | △ | △ | 2.5 | 200 | / | Varying effectiveness depending on track but can be strong with Triple 7s activation |
| I Never Goof Up! | △ | ◯ | 2.5 | 200 | / | Good effect but rng and track dependent |
| Bountiful Harvest | △ | △ | 2.5 | 200 | / | Consistent but relatively weak |
| YUMMY☆SPEED! | △ | ✕ | 2.5 | 200 | / | Unfortunate timing at 60% of the Race makes this skill's acceleration practically useless |
| OMG! (ﾟ∀ﾟ) The Final Sprint! ☆ | △ | △ | 2.5 | 200 | / | Generally, when you overtake in Late-Race, you're still accelerating, so a Target Speed skill wouldn't be effective |
| Give Mummy a Hug ♡ | △ | ◯ | 2.5 | 200 | / | Good accel for tracks that have their Last Spurt Mode begin on/near a Last Straight |
| Chasing After You | △ | △ | 2.5 | 200 | / | Very weak effect but can be used as a debuff |
| Arrows Whistle, Shadows Disperse | △ | ◯ | 2.5 | 200 | / | Consistent, but weak effect |
| Pop & Polish | △ | ◯ | 2.5 | 200 | / | Consistent, but weak effect |
| Presents from X | △ | △ | 2.5 | 200 | / | Consistent, but weak effect |
| Festive Miracle | △ | ◯ | 2.5 | 200 | / | Strong on some tracks where Triple 7s can proc before the Last Spurt |
| Fairy Tale | △ | △ | 2.5 | 200 | / | Strong on some tracks where Triple 7s can proc before the Last Spurt |
| Straightaway Recovery | △ | △ | 2.94 | 170 | / | Inconsistent, it might be wasted on an early or late activation |
| Breath of Fresh Air | △ | △ | 3.53 | 170+170 | / | Inconsistent, it might be wasted on an early or late activation |
| Lay Low | △ | ✕ | 3.12 | 160 | / | Might proc in Early-Race which might overflow HP |
| Iron Will | △ | ✕ | 3.75 | 160+160 | / | Might proc in Early-Race which might overflow HP |
| Pace Strategy | △ | ✕ | 2.94 | 170 | / | Being overtaken is an inconsistent condition<br>More suitable on long, backline Run Styles |
| Indomitable | △ | ✕ | 3.53 | 170+170 | / | Being overtaken is an inconsistent condition<br>More suitable on long, backline Run Styles |
| Triple 7s | △ | ▲ | 3.12 | 160 | / | Consistent, but only effective on <2400m tracks, useful for some Uma that rely on Stamina skill procs |
| Shake It Out | △ | ✕ | 5 | 100 | / | Late-Race recovery is ineffective<br>consider acquiring it only for Team Trials because it's very cheap |
| Ignited Spirit STA | △ | △ | 2.5 | 200 | / | Definitely an option but it costs more than a usual skill (at 200 base SP) |
| Burning Spirit STA | △ | △ | 3 | 200+200 | / | Definitely an option but it costs more than a usual skill (at 200 base SP) |
| Moxie | △ | ◯ | 2.78 | 180 | Front Runner | Consistent activation but recovery can be useless when<br>the uphill is located at anywhere other than Mid-Race |
| Restless | △ | △ | 3.33 | 180+180 | Front Runner | Consistent activation but recovery can be useless when<br>the uphill is located at anywhere other than Mid-Race |
| Stamina to Spare | △ | ◯ | 2.78 | 180 | Pace Chaser | Stamina to Spare is okay as its recovery is unlikely to overflow (making it a decent choice),<br>but Calm and Collected may recover too much in a few situations (making it less consistent) |
| Calm and Collected | △ | ◎ | 3.33 | 180+180 | Pace Chaser | Stamina to Spare is okay as its recovery is unlikely to overflow (making it a decent choice),<br>but Calm and Collected may recover too much in a few situations (making it less consistent) |
| A Small Breather | △ | ✕ | 2.78 | 180 | Late Surger | Late-Race recovery is ineffective, Last Spurt recalculation isn't added until 1st Year Anniversary |
| Relax | △ | ✕ | 3.33 | 180+180 | Late Surger | Late-Race recovery is ineffective, Last Spurt recalculation isn't added until 1st Year Anniversary |
| Be Still | △ | ◯ | 2.78 | 180 | Late Surger | Late-Race recovery is ineffective, Last Spurt recalculation isn't added until 1st Year Anniversary |
| Lie in Wait | △ | ◎ | 3.33 | 180+180 | Late Surger | Late-Race recovery is ineffective, Last Spurt recalculation isn't added until 1st Year Anniversary |
| Standing By | △ | ✕ | 2.78 | 180 | End Closer | Somewhat consistent, but may be undesirable for well-built End Closers<br>since they can probably reach positions above 75% by distance and hence, not activate this skill |
| Sleeping Lion | △ | ✕ | 3.33 | 180+180 | End Closer | Somewhat consistent, but may be undesirable for well-built End Closers<br>since they can probably reach positions above 75% by distance and hence, not activate this skill |
| After-School Stroll | △ | ✕ | 2.94 | 170 | End Closer | Consistent activation but recovery can be useless when<br>the downhill is located at anywhere other than Mid-Race |
| Go-Home Specialist | △ | ✕ | 3.53 | 170+170 | End Closer | Consistent activation but recovery can be useless when<br>the downhill is located at anywhere other than Mid-Race |
| Levelheaded | △ | △ | 2.78 | 180 | End Closer | Getting blocked is a decently consistent condition for End Closers |
| Rosy Outlook | △ | ✕ | 3.12 | 160 | Medium | Consistent recovery for Front Runners and perhaps even Pace Chasers |
| Trackblazer | △ | ✕ | 3.75 | 160+160 | Medium | Consistent recovery for Front Runners and perhaps even Pace Chasers |
| Soft Step | △ | ✕ | 3.12 | 160 | Medium | Consistent but effect isn't that strong<br>Rare ver. is actually worse as this tends to activate early on and the 5.5% recovery could overflow |
| Miraculous Step | △ | ✕ | 3.75 | 160+160 | Medium | Consistent but effect isn't that strong<br>Rare ver. is actually worse as this tends to activate early on and the 5.5% recovery could overflow |
| Deep Breaths | △ | △ | 3.12 | 160 | Long | Inconsistent, it might be wasted on an early or late activation |
| Cooldown | △ | △ | 3.75 | 160+160 | Long | Inconsistent, it might be wasted on an early or late activation |
| Extra Tank | △ | △ | 3.12 | 160 | Long | If your HP drops to zero, you're cooked anyway, no recovery can save you |
| Adrenaline Rush | △ | △ | 3.75 | 160+160 | Long | If your HP drops to zero, you're cooked anyway, no recovery can save you |
| Passing Pro | △ | △ | 3.12 | 160 | Long | Mostly consistent but activation can occur on Early-Race, diminishing its value |
| U=ma2 | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Pure Heart | △ | △ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Super-Duper Climax | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Superior Heal | △ | △ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Dazzl'n ♪ Diver | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Every Rose Has Its Fangs | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Corner Acceleration ◯ | △ | ✕ | 2.78 | 180 | / | Acceleration on the Corner 1/First Corner of any track is useless |
| Corner Connoisseur | △ | ✕ | 3.33 | 180+180 | / | Acceleration on the Corner 1/First Corner of any track is useless |
| Straightaway Acceleration | △ | ✕ | 2.94 | 170 | / | Random straight activations are too inconsistent to be effective |
| Rushing Gale! | △ | ✕ | 3.53 | 170+170 | / | Random straight activations are too inconsistent to be effective |
| Highlander | △ | ◎ | 3.12 | 160 | / | Very powerful on tracks with Uphills right before/as Last Spurt Mode begins |
| Groundwork | △ | ▲ | 5 | 100 | / | For Front Runners only, use with 3 Early-Race skills like Focus/Concentration+Green Skills |
| Final Push | △ | ✕ | 2.78 | 180 | Front Runner | Being in 1st isn't completely consistent, but it's a rare skill that can be useful on tracks where<br>your Uma enters Last Spurt Mode slightly after where the Final Corner begins/right at where the Final Corner is |
| Unrestrained | △ | ✕ | 3.33 | 180+180 | Front Runner | Being in 1st isn't completely consistent, but it's a rare skill that can be useful on tracks where<br>your Uma enters Last Spurt Mode slightly after where the Final Corner begins/right at where the Final Corner is |
| Shrewd Step | △ | ✕ | 4.17 | 120 | Pace Chaser | Cheap and consistent activation, but useless Mid-Race accel |
| Technician | △ | ✕ | 5 | 120+120 | Pace Chaser | Cheap and consistent activation, but useless Mid-Race accel |
| Straight Descent | △ | ⍟ | 4.17 | 120 | Pace Chaser | Very powerful on tracks with Downhills right before/as Last Spurt Mode begins |
| Determined Descent | △ | ⍟ | 5 | 120+120 | Pace Chaser | Very powerful on tracks with Downhills right before/as Last Spurt Mode begins |
| Tactical Tweak | △ | ✕ | 4.17 | 120 | Pace Chaser | Cheap and consistent activation, but useless Mid-Race accel |
| Shatterproof | △ | ✕ | 5 | 120+120 | Pace Chaser | Cheap and consistent activation, but useless Mid-Race accel |
| Fighter | △ | ✕ | 4.17 | 120 | Late Surger | Cheap and consistent activation but useless Mid-Race accel |
| Hard Worker | △ | ✕ | 5 | 120+120 | Late Surger | Cheap and consistent activation but useless Mid-Race accel |
| Straightaway Spurt | △ | ⍟ | 2.78 | 180 | End Closer | Very powerful End Closer acceleration that works on tracks where Last Spurt Mode begins on a Straight |
| Encroaching Shadow | △ | ⍟ | 3.33 | 180+180 | End Closer | Very powerful End Closer acceleration that works on tracks where Last Spurt Mode begins on a Straight |
| Sprinting Gear | △ | ✕ | 3.12 | 160 | Sprint | Random straight activations are almost always useless |
| Turbo Sprint | △ | ✕ | 3.75 | 160+160 | Sprint | Random straight activations are almost always useless |
| Countermeasure | △ | ✕ | 3.12 | 160 | Sprint | Gamble accel, if it procs right before Mid-Race ends it'll be effective |
| Plan X | △ | ✕ | 3.75 | 160+160 | Sprint | Gamble accel, if it procs right before Mid-Race ends it'll be effective |
| Acceleration | △ | ✕ | 3.12 | 160 | Mile | Fairly consistent but Mid-Race accel is useless |
| Step on the Gas! | △ | ✕ | 3.75 | 160+160 | Mile | Fairly consistent but Mid-Race accel is useless |
| KEEP IT REAL. | △ | ✕ | 2.5 | 200 | / | Mostly useless accel but consistent activation |
| Moving Past, and Beyond | △ | ✕ | 2.5 | 200 | / | Mostly useless accel but consistent activation |
| Prudent Positioning | △ | ▲ | 4.17 | 120 | / | Use with Dodging Danger for a very powerful Early-Race burst of speed (Front Runner only) |
| Center Stage | △ | ✕ | 5 | 120+120 | / | Never use for Front-Runners that want to run the Dodging Danger tech |
| Go with the Flow | △ | ✕ | 4.17 | 120 | / | Random non-Early-Race Lane Movement Speed for non-Front-Runners are useless<br>Take only because they are very cheap and if you have no other options |
| Lane Legerdemain | △ | ✕ | 5 | 120+120 | / | Random non-Early-Race Lane Movement Speed for non-Front-Runners are useless<br>Take only because they are very cheap and if you have no other options |
| Ignited Spirit WIT | △ | ▲ | 2.5 | 200 | / | Use with Dodging Danger for a very powerful Early-Race burst of speed (Front Runner only) |
| Burning Spirit WIT | △ | ✕ | 3 | 200+200 | / | Never use for Front-Runners that want to run the Dodging Danger tech |
| Dodging Danger | △ | ⍟ | 4.55 | 110 | Front Runner | Use with Prudent Positioning/Ignition Spirit WIT for a very powerful Early-Race burst of speed (Front Runner only) |
| Sixth Sense | △ | ✕ | 5.45 | 110+110 | Front Runner | Never use for Front-Runners that want to run the "Prudent Positioning" + "Dodging Danger" combo |
| Meticulous Measures | △ | ✕ | 3.57 | 140 | Sprint | Random non-Early-Race Lane Movement Speed for non-Front-Runners are useless<br>There is no need for any additional acceleration (unless it's toward the very end which is very RNG-dependent)<br>Take only because they are very cheap and if you have no other options |
| Perfect Prep! | △ | ✕ | 4.29 | 140+140 | Sprint | Random non-Early-Race Lane Movement Speed for non-Front-Runners are useless<br>There is no need for any additional acceleration (unless it's toward the very end which is very RNG-dependent)<br>Take only because they are very cheap and if you have no other options |
| Thunderbolt Step | △ | ✕ | 3.57 | 140 | Medium | Random non-Early-Race Lane Movement Speed for non-Front-Runners are useless<br>There is no need for any additional acceleration (unless it's toward the very end which is very RNG-dependent)<br>Take only because they are very cheap and if you have no other options |
| Lightning Step | △ | ✕ | 4.29 | 140+140 | Medium | Random non-Early-Race Lane Movement Speed for non-Front-Runners are useless<br>There is no need for any additional acceleration (unless it's toward the very end which is very RNG-dependent)<br>Take only because they are very cheap and if you have no other options |
| Forward, March! | △ | ✕ | 3.57 | 140 | Dirt | Very good Dirt accel skill disguised as a lane movement speed skill |
| Lead the Charge! | △ | ✕ | 4.29 | 140+140 | Dirt | Very good Dirt accel skill disguised as a lane movement speed skill |
| Studious | △ | ✕ | 4.17 | 120 | Late Surger | Extra FoV is mostly useless<br>Take only because they are very cheap and if you have no other options |
| The Bigger Picture | △ | ✕ | 5 | 120+120 | Late Surger | Extra FoV is mostly useless<br>Take only because they are very cheap and if you have no other options |
| I Can See Right Through You | △ | ✕ | 4.55 | 110 | End Closer | Extra FoV is mostly useless<br>Take only because they are very cheap and if you have no other options |
| The Coast Is Clear! | △ | ✕ | 5.45 | 110+110 | End Closer | Extra FoV is mostly useless<br>Take only because they are very cheap and if you have no other options |
| Strategist | △ | ✕ | 4.55 | 110 | End Closer | Extra FoV is mostly useless<br>Take only because they are very cheap and if you have no other options |
| Crusader | △ | ✕ | 5.45 | 110+110 | End Closer | Extra FoV is mostly useless<br>Take only because they are very cheap and if you have no other options |
| Hawkeye | △ | ✕ | 4.55 | 110 | Medium | Extra FoV is mostly useless<br>Take only because they are very cheap and if you have no other options |
| Clairvoyance | △ | ✕ | 5.45 | 110+110 | Medium | Extra FoV is mostly useless<br>Take only because they are very cheap and if you have no other options |
| Disorient | △ | △ | 4.55 | 110 | Pace Chaser | First Half of the Pack, at Random Point during Late-Race |
| Dazzling Disorientation | △ | △ | 5.45 | 110+110 | Pace Chaser | First Half of the Pack, at Random Point during Late-Race |
| Intense Gaze | △ | ◯ | 2.78 | 180 | End Closer | Not 1st Place, at Random Point during Late-Race |
| Intimidate | △ | ✕ | 2.94 | 170 | Sprint | First Half of the Pack, at Random Point in Early-Race, ≥5s after Race Start |
| Adored by All | △ | ✕ | 3.53 | 170+170 | Sprint | First Half of the Pack, at Random Point in Early-Race, ≥5s after Race Start |
| Speed Eater | △ | ✕ | 3.12 | 160 | Mile | 1st-3rd Place, at Random Point during Mid-Race |
| Smoke Screen | △ | △ | 4.55 | 110 | Long | Random Point in Late-Race |
| Illusionist | △ | △ | 5.45 | 110+110 | Long | Random Point in Late-Race |
| [Location] Racecourse ◯ | △ | ◎ | 5.56 | 90 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| [Ground Condition] Conditions ◯ | △ | ◎ | 5.56 | 90 | / | Power Stat increase is decent but low priority |
| [Weather] Days ◯ | △ | △ | 5.56 | 90 | / | Guts is extremely unimportant, only take it you really need to |
| [Run Style] Savvy ◎ | △ | ▲ | 2.08 | 110+130 | [Run Style] | Consistent activation, FoV buff is useful for Nice Nature's All-Seeing Eyes |

##### ✕ Avoid (Team Trials): 44 skills

| Skill | Team Trials | CM | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| Risky Business | ✕ | ✕ | 4.17 | 120 | / | This skill can completely kill your stamina, it's definitely not worth it unless you're trying to do some niche strat |
| Masterful Gambit | ✕ | ✕ | 2.78 | 180 | End Closer | Extremely inconsistent, borderline impossible to activate as your Uma should already be at least within top 75% (by distance) of the pack by the time the Mid-Race ends |
| Sturm und Drang | ✕ | ✕ | 3.33 | 180+180 | End Closer | Extremely inconsistent, borderline impossible to activate as your Uma should already be at least within top 75% (by distance) of the pack by the time the Mid-Race ends |
| Huge Lead | ✕ | ✕ | 2.94 | 170 | Sprint | 12.5m lead is highly unfeasible, this skill will almost never activate |
| Staggering Lead | ✕ | ✕ | 3.53 | 170+170 | Sprint | 12.5m lead is highly unfeasible, this skill will almost never activate |
| Cut and Drive! | ✕ | ✕ | 2.5 | 200 | / | Not the most consistent, and also a weak effect, not worth taking |
| G00 1st. F∞; | ✕ | △ | 2.5 | 200 | / | 0.15m/s but has two additional checks (for Start Delay and Rushed) |
| Genius x Bakushin = Victory | ✕ | △ | 2.5 | 200 | / | Fairly consistent, but also weak |
| I See Victory in My Future! | ✕ | ✕ | 2.5 | 200 | / | Front Block condition is downright horrible |
| Prideful King | ✕ | ✕ | 2.5 | 200 | / | Extremely inconsistent, if not totally impossible to even activate in any distance but Sprint |
| Schwarzes Schwert | ✕ | △ | 2.5 | 200 | / | 0.15m/s but requires two additional checks (for Start Delay and Rushed) |
| A Princess Must Seize Victory! | ✕ | ✕ | 2.5 | 200 | / | Side block condition on the Last Straight is quite strict and difficult to proc |
| Dancing in the Leaves | ✕ | ✕ | 2.5 | 200 | / | Side Block isn't consistent, effect isn't outstanding either |
| Calm in a Crowd | ✕ | ✕ | 2.94 | 170 | / | Almost impossible to be boxed in on all sides in CM |
| Unruffled | ✕ | ✕ | 3.53 | 170+170 | / | Almost impossible to be boxed in on all sides in CM |
| Second Wind | ✕ | ✕ | 2.78 | 180 | Front Runner | Expensive and impossible to activate on Front Runners, plus, Mid-Race acceleration is useless |
| Restart | ✕ | ✕ | 3.85 | 130 | Front Runner | Last Half of the Pack, at Random Point during Early-Race, ≥5s after Race Start |
| Stop Right There! | ✕ | ✕ | 2.94 | 170 | Sprint | Last Half of the Pack, at Random Point during Early-Race, ≥5s after Race Start |
| Opening Gambit | ✕ | ✕ | 3.12 | 160 | Mile | Last Half of the Pack, at Random Point during Early-Race, ≥3s after Race Start |
| Battle Formation | ✕ | ✕ | 3.75 | 160+160 | Mile | Last Half of the Pack, at Random Point during Early-Race, ≥3s after Race Start |
| [Rotation]-Handed ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Speed stat increase is significant |
| [Season] Runner ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Speed stat increase is significant |
| Fall Frenzy | ✕ | ✕ | 3.64 | 90+110+130 | / | Take only on Autumn CMs |
| Outer Post Proficiency ◯ | ✕ | ✕ | 5.56 | 90 | / | Post Numbers 6-8 is inconsistent |
| Outer Post Proficiency ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Post Numbers 6-8 is inconsistent |
| Maverick ◯ | ✕ | ✕ | 5.56 | 90 | / | Very rare to have no Umas use your run style |
| Maverick ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Very rare to have no Umas use your run style |
| Long Shot ◯ | ✕ | ✕ | 5.56 | 90 | / | Popularity-dependent skills are inconsistent |
| Long Shot ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Popularity-dependent skills are inconsistent |
| Sympathy | ✕ | ▲ | 7.14 | 70 | / | Practically impossible to proc |
| [Location] Racecourse ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Yodo Invicta | ✕ | ✕ | 3.64 | 90+110+130 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Standard Distance ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Non-Standard Distance ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| [Ground Condition] Conditions ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Power Stat increase is decent but low priority |
| Competitive Spirit ◯ | ✕ | ✕ | 5.56 | 90 | / | It's unlikely for 40% of the lobby to use the same run style as you |
| Competitive Spirit ◎ | ✕ | ✕ | 2.5 | 90+110 | / | It's unlikely for 40% of the lobby to use the same run style as you |
| [Weather] Days ◎ | ✕ | △ | 2.5 | 90+110 | / | Guts is extremely unimportant, only take it you really need to |
| Target in Sight ◯ | ✕ | ✕ | 5.56 | 90 | / | Guts is extremely unimportant, only take it you really need to |
| Target in Sight ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Guts is extremely unimportant, only take it you really need to |
| Inner Post Proficiency ◯ | ✕ | ✕ | 5.56 | 90 | / | Post Numbers 1-3 is inconsistent |
| Inner Post Proficiency ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Post Numbers 1-3 is inconsistent |
| Lucky Seven | ✕ | ✕ | 4.55 | 110 | / | Inconsistent, even more so than the Post Proficiency skills |
| Super Lucky Seven | ✕ | ✕ | 5.45 | 110+110 | / | Inconsistent, even more so than the Post Proficiency skills |

##### Quick view: skills grouped by CM tier

- **⍟ Essential (18):** [Run Style] Corners ◯; [Run Style] Straightaways ◯; [Distance] Corners ◯; [Distance] Straightaways ◯; Early Lead; Taking the Lead; Head-On; Slick Surge; On Your Left!; [Run Style] Corners ◎; [Run Style] Straightaways ◎; [Distance] Corners ◎; [Distance] Straightaways ◎; Straight Descent; Determined Descent; Straightaway Spurt; Encroaching Shadow; Dodging Danger
- **◎ Top tier (58):** Uma Stan; Super Stan; Tail Held High; Slipstream; Playtime's Over!; Burning Spirit GUTS; Fast-Paced; Escape Artist; 1,500,000 CC; 15,000,000 CC; Corner Recovery ◯; Swinging Maestro; Race Planner; Gourmand; Ignited Spirit PWR; Burning Spirit PWR; Hesitant [Run Style]s; Subdued [Run Style]s; Flustered [Run Style]s; Trick (Front); Tantalizing Trick; Trick (Rear); Sharp Gaze; All-Seeing Eyes; Stamina Siphon; Lone Wolf; Ignited Spirit GUTS; Fast & Furious; Outer Swell; Rising Dragon; Nimble Navigator; No Stopping Me!; Frenzied [Run Style]s; Stamina Eater; [Rotation]-Handed ◯; [Season] Runner ◯; Standard Distance ◯; Non-Standard Distance ◯; Shooting for Victory!; Let's Pump Some Iron!; Angling and Scheming; Leader's Pride; Certain Victory; Sky-High Teio Step; Triumphant Pulse; Victoria por plancha ☆; Behold Thine Emperor's Divine Might; Calm and Collected; Lie in Wait; Highlander; [Location] Racecourse ◯; [Ground Condition] Conditions ◯; [Rotation]-Handed ◎; [Season] Runner ◎; [Location] Racecourse ◎; Standard Distance ◎; Non-Standard Distance ◎; [Ground Condition] Conditions ◎
- **◯ Good (26):** Preferred Position; Hydrate; [Run Style] Savvy ◯; Professor of Curvature; Beeline Burst; It's On!; In Body and Mind; Position Pilfer; Shooting Star; The Duty of Dignity Calls; This Dance Is for Vittoria!; Blazing Pride; ∴win Q.E.D.; Flashy☆Landing; Nemesis; Shadow Break; Lights of Vaudeville; I Never Goof Up!; Give Mummy a Hug ♡; Arrows Whistle, Shadows Disperse; Pop & Polish; Festive Miracle; Moxie; Stamina to Spare; Be Still; Intense Gaze
- **▲ Situational (14):** Focus; Concentration; Gap Closer; Blinding Flash; Runaway; Resplendent Red Ace; SPARKLY☆STARDOM; Flowery☆Maneuver; Triple 7s; Groundwork; Prudent Positioning; Ignited Spirit WIT; [Run Style] Savvy ◎; Sympathy
- **△ Low priority (47):** Corner Adept ◯; Straightaway Adept; Ramp Up; Homestretch Haste; Ignited Spirit SPD; Burning Spirit SPD; Prepared to Pass; Speed Star; Early Start; Keeping the Lead; Vanguard Spirit; Legacy of the Strong; The View from the Lead is Mine!; Where There's a Will, There's a Way; Blue Rose Closer; Our Ticket to Win!; #LookatCurren; Eternal Moments; You and Me! One-on-One!; A Kiss for Courage; Bountiful Harvest; OMG! (ﾟ∀ﾟ) The Final Sprint! ☆; Chasing After You; Presents from X; Fairy Tale; Straightaway Recovery; Breath of Fresh Air; Ignited Spirit STA; Burning Spirit STA; Restless; Levelheaded; Deep Breaths; Cooldown; Extra Tank; Adrenaline Rush; Passing Pro; Pure Heart; Superior Heal; Disorient; Dazzling Disorientation; Smoke Screen; Illusionist; [Weather] Days ◯; G00 1st. F∞;; Genius x Bakushin = Victory; Schwarzes Schwert; [Weather] Days ◎
- **✕ Avoid (126):** Mile Maven; Unyielding Spirit; Big-Sisterly; Tether; Dominator; Murmur; Mystifying Murmur; Productive Plan; Shifting Gears; Changing Gears; Up-Tempo; Killer Tunes; Updrafters; Furious Feat; Wait-and-See; Watchful Eye; Keen Eye; Red Shift/LP1211-M; Condor's Fury; Steadfast; Unyielding; All I've Got; Come What May; Inside Scoop; Innate Experience; Pressure; Overwhelming Pressure; Top Pick; Trending in the Charts!; Anchors Aweigh!; Just a Little Farther!; YUMMY☆SPEED!; Lay Low; Iron Will; Pace Strategy; Indomitable; Shake It Out; A Small Breather; Relax; Standing By; Sleeping Lion; After-School Stroll; Go-Home Specialist; Rosy Outlook; Trackblazer; Soft Step; Miraculous Step; U=ma2; Super-Duper Climax; Dazzl'n ♪ Diver; Every Rose Has Its Fangs; Corner Acceleration ◯; Corner Connoisseur; Straightaway Acceleration; Rushing Gale!; Final Push; Unrestrained; Shrewd Step; Technician; Tactical Tweak; Shatterproof; Fighter; Hard Worker; Sprinting Gear; Turbo Sprint; Countermeasure; Plan X; Acceleration; Step on the Gas!; KEEP IT REAL.; Moving Past, and Beyond; Center Stage; Go with the Flow; Lane Legerdemain; Burning Spirit WIT; Sixth Sense; Meticulous Measures; Perfect Prep!; Thunderbolt Step; Lightning Step; Forward, March!; Lead the Charge!; Studious; The Bigger Picture; I Can See Right Through You; The Coast Is Clear!; Strategist; Crusader; Hawkeye; Clairvoyance; Intimidate; Adored by All; Speed Eater; Risky Business; Masterful Gambit; Sturm und Drang; Huge Lead; Staggering Lead; Cut and Drive!; I See Victory in My Future!; Prideful King; A Princess Must Seize Victory!; Dancing in the Leaves; Calm in a Crowd; Unruffled; Second Wind; Restart; Stop Right There!; Opening Gambit; Battle Formation; Fall Frenzy; Outer Post Proficiency ◯; Outer Post Proficiency ◎; Maverick ◯; Maverick ◎; Long Shot ◯; Long Shot ◎; Yodo Invicta; Competitive Spirit ◯; Competitive Spirit ◎; Target in Sight ◯; Target in Sight ◎; Inner Post Proficiency ◯; Inner Post Proficiency ◎; Lucky Seven; Super Lucky Seven

#### Front Runner

173 skills ranked for this build, grouped by their **Team Trials** tier. The PvP rank of each skill is shown in its own column.

##### ◎ Top tier (Team Trials): 28 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| [Run Style] Corners ◯ | ◎ | ⍟ | 3.85 | 130 | [Run Style] | Cheap and consistent, they are must-haves |
| [Run Style] Straightaways ◯ | ◎ | ⍟ | 3.85 | 130 | [Run Style] | Cheap and consistent, they are must-haves |
| [Distance] Corners ◯ | ◎ | ⍟ | 5 | 100 | [Distance] | Cheap and consistent, they are must-haves |
| [Distance] Straightaways ◯ | ◎ | ⍟ | 5 | 100 | [Distance] | Cheap and consistent, they are must-haves |
| Uma Stan | ◎ | ◎ | 3.12 | 160 | / | Best speed skill on longer tracks for non-Front-Runners, can help to release PDM on some longer tracks |
| Super Stan | ◎ | ◎ | 3.75 | 160+160 | / | Best speed skill on longer tracks for non-Front-Runners, can help to release PDM on some longer tracks |
| Tail Held High | ◎ | ◎ | 5 | 100 | / | Cheap and consistent, though note the condition of requiring 3 skill activations before acquiring it |
| Slipstream | ◎ | ◎ | 3.12 | 160 | / | Consistent and facilitates overtaking when activated |
| Playtime's Over! | ◎ | ◎ | 3.12 | 160 | / | Consistent and improves Uma's capacity to maintain her placement |
| Burning Spirit GUTS | ◎ | ◎ | 3 | 200+200 | / | Good random Late-Race accel but in the game's current state,<br>this skill's effect is likely 80% (when Total Guts ≤ 1200) or 90% (when 1200 < Total Guts ≤ 1600) |
| Fast-Paced | ◎ | ◎ | 2.78 | 180 | Front Runner | Consistent with easy conditions. Helps Front Runners maintain/regain their lead during the Mid-Race |
| Escape Artist | ◎ | ◎ | 3.33 | 180+180 | Front Runner | Consistent with easy conditions. Helps Front Runners maintain/regain their lead during the Mid-Race |
| Corner Recovery ◯ | ◎ | ◎ | 2.94 | 170 | / | Consistent and effective recovery |
| Swinging Maestro | ◎ | ◎ | 3.53 | 170+170 | / | Consistent and effective recovery |
| Ignited Spirit PWR | ◎ | ◎ | 2.5 | 200 | / | It's like a weaker but universal Slick Surge/On Your Left! |
| Burning Spirit PWR | ◎ | ◎ | 3 | 200+200 | / | It's like a weaker but universal Slick Surge/On Your Left! |
| Early Lead | ◎ | ⍟ | 4.17 | 120 | Front Runner | Necessary skill for all Front Runners |
| Taking the Lead | ◎ | ⍟ | 5 | 120+120 | Front Runner | Necessary skill for all Front Runners |
| Focus | ◎ | ▲ | 3.57 | 140 | / | Only take for Front Runners, Focus reduces the chance of a Late Start, while Concentration makes it impossible<br>You also get score for "strong starts" in Team Trials, so Concentration is always good there |
| Concentration | ◎ | ▲ | 4.29 | 140+140 | / | Only take for Front Runners, Focus reduces the chance of a Late Start, while Concentration makes it impossible<br>You also get score for "strong starts" in Team Trials, so Concentration is always good there |
| Hesitant [Run Style]s | ◎ | ◎ | 3.85 | 130 | / | Random Point in Late-Race |
| Subdued [Run Style]s | ◎ | ◎ | 3.85 | 130 | / | Random Point in Early-Race, ≥5 after Race Start |
| Flustered [Run Style]s | ◎ | ◎ | 3.85 | 130 | / | Random Point in Mid-Race |
| Trick (Front) | ◎ | ◎ | 3.57 | 140 | / | First Half of the Pack, ≥1 "Rushed" Uma behind |
| Tantalizing Trick | ◎ | ◎ | 4.29 | 140+140 | / | First Half of the Pack, ≥1 "Rushed" Uma behind |
| Trick (Rear) | ◎ | ◎ | 3.57 | 140 | / | 2nd-9th/12th Place, ≥1 "Rushed" Uma ahead |
| Lone Wolf | ◎ | ◎ | 7.14 | 70 | / | Easy to proc, you either benefit (you proc) or make it even (you prevent someone else's from proc'ing) |
| [Run Style] Savvy ◯ | ◎ | ◯ | 4.55 | 110 | [Run Style] | Consistent activation, FoV buff is useful for Nice Nature's All-Seeing Eyes |

##### ◯ Good (Team Trials): 12 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| Professor of Curvature | ◯ | ◯ | 3.33 | 180+180 | / | Consistent, but expensive<br>Rare ver. has greater speed boost making it more worth to acquire |
| Beeline Burst | ◯ | ◯ | 3.53 | 170+170 | / | Consistent |
| It's On! | ◯ | ◯ | 3.53 | 170+170 | / | Consistent. Even better when used in tandem with Tail Held High, Slipstream, and Playtime's Over! |
| In Body and Mind | ◯ | ◯ | 3.53 | 170+170 | / | Useful and (fairly) consistent Last Spurt speed boost, falls short of ◎ because it could activate at the very end of a race |
| Ignited Spirit GUTS | ◯ | ◎ | 2.5 | 200 | / | Good random Late-Race accel but in the game's current state,<br>this skill's effect is likely 80% (when Total Guts ≤ 1200) or 90% (when 1200 < Total Guts ≤ 1600) |
| Nimble Navigator | ◯ | ◎ | 3.33 | 150 | / | Strong accel but rng-dependent |
| No Stopping Me! | ◯ | ◎ | 4 | 150+150 | / | Strong accel but rng-dependent |
| Frenzied [Run Style]s | ◯ | ◎ | 3.85 | 130 | / | [Run Style] is "Rushed" |
| [Rotation]-Handed ◯ | ◯ | ◎ | 5.56 | 90 | / | Speed stat increase is significant |
| [Season] Runner ◯ | ◯ | ◎ | 5.56 | 90 | / | Speed stat increase is significant |
| Standard Distance ◯ | ◯ | ◎ | 5.56 | 90 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Non-Standard Distance ◯ | ◯ | ◎ | 5.56 | 90 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |

##### ▲ Situational (Team Trials): 6 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| Red Shift/LP1211-M | ▲ | ✕ | 2.5 | 200 | / | Powerful accel for Fronts/Paces, especially on tracks where Last Spurt Mode begins slightly before or on the Final Corner |
| Shooting for Victory! | ▲ | ◎ | 2.5 | 200 | / | Powerful accel for Paces/Lates, especially on tracks where Last Spurt Mode begins slightly before or on the Second Half of the Final Corner |
| Let's Pump Some Iron! | ▲ | ◎ | 2.5 | 200 | / | Strongest but most inconsistent accel for Lates/Ends on tracks where Last Spurt Mode begins slightly before or on the Final Corner |
| Angling and Scheming | ▲ | ◎ | 2.5 | 200 | / | Strongest accel for Fronts on tracks where Last Spurt Mode begins on a Corner |
| Condor's Fury | ▲ | ✕ | 2.5 | 200 | / | Powerful accel for Lates/Ends, especially on tracks where Last Spurt Mode begins slightly before or on the Final Corner |
| Runaway | ▲ | ▲ | 6 | 200 | Front Runner | Dependent on what you want/need |

##### △ Low priority (Team Trials): 90 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| [Run Style] Corners ◎ | △ | ⍟ | 1.85 | 130+140 | [Run Style] | Cheap and consistent, they are must-haves |
| [Run Style] Straightaways ◎ | △ | ⍟ | 1.85 | 130+140 | [Run Style] | Cheap and consistent, they are must-haves |
| [Distance] Corners ◎ | △ | ⍟ | 2.38 | 100+110 | [Distance] | Cheap and consistent, they are must-haves |
| [Distance] Straightaways ◎ | △ | ⍟ | 2.38 | 100+110 | [Distance] | Cheap and consistent, they are must-haves |
| Corner Adept ◯ | △ | △ | 2.78 | 180 | / | Consistent, but expensive<br>Rare ver. has greater speed boost making it more worth to acquire |
| Straightaway Adept | △ | △ | 2.94 | 170 | / | Consistent |
| Ramp Up | △ | △ | 2.94 | 170 | / | Consistent. Even better when used in tandem with Tail Held High, Slipstream, and Playtime's Over! |
| Homestretch Haste | △ | △ | 2.94 | 170 | / | Useful and (fairly) consistent Last Spurt speed boost, falls short of ◎ because it could activate at the very end of a race |
| Ignited Spirit SPD | △ | △ | 2.5 | 200 | / | 1.8s isn't very long and it costs 200 base SP |
| Burning Spirit SPD | △ | △ | 3 | 200+200 | / | 1.8s isn't very long and it costs 200 base SP |
| Leader's Pride | △ | ◎ | 2.78 | 180 | Front Runner | Inconsistent activation during Early-Race where overtaking doesn't happen frequently or consistently, consistency is directly proportional to track distance |
| Certain Victory | △ | ◎ | 2.5 | 200 | / | Identical to OG Teio's unique with slightly looser conditions |
| Legacy of the Strong | △ | △ | 2.5 | 200 | / | Effects aren't bad but inconsistent activation |
| Shooting Star | △ | ◯ | 2.5 | 200 | / | Consistent activation, but weak effect |
| The View from the Lead is Mine! | △ | △ | 2.5 | 200 | / | Somewhat consistent activation for Front Runners, but weak effect |
| Sky-High Teio Step | △ | ◎ | 2.5 | 200 | / | Mostly consistent for non-Front-Runners, with strong effect |
| Triumphant Pulse | △ | ◎ | 2.5 | 200 | / | Consistent for non-Front-Runners, with strong effect |
| Anchors Aweigh! | △ | ✕ | 2.5 | 200 | / | Consistent for Late Surgers/End Closers but minimal effect |
| Resplendent Red Ace | △ | ▲ | 2.5 | 200 | / | Accel can come in handy occasionally but still very situational and slightly unreliable |
| Where There's a Will, There's a Way | △ | △ | 2.5 | 200 | / | Decent speed skill option for non-Front-Runners |
| The Duty of Dignity Calls | △ | ◯ | 2.5 | 200 | / | Final Corner Target Speed boost is inconsistent (especially in Med race), but it can be situationally good for Front Runners/Pace Chasers |
| Victoria por plancha ☆ | △ | ◎ | 2.5 | 200 | / | Activation is mostly consistent, some tracks benefit from a Last Straight accel |
| This Dance Is for Vittoria! | △ | ◯ | 2.5 | 200 | / | Fairly consistent activation but Final Corner Target Speed boost could be inconsistent |
| Behold Thine Emperor's Divine Might | △ | ◎ | 2.5 | 200 | / | Consistent for non-Front-Runners, with strong effect |
| Blazing Pride | △ | ◯ | 2.5 | 200 | / | Final Corner Target Speed boost is inconsistent (especially in Med race), but it can be situationally good for Late Surgers |
| ∴win Q.E.D. | △ | ◯ | 2.5 | 200 | / | Final Corner Target Speed boost is inconsistent (especially in Med race), but it can be situationally good for Front Runners |
| Flashy☆Landing | △ | ◯ | 2.5 | 200 | / | Acceleration on and beyond Final Corner is decent, conditions to activate may not be consistent unless you're Front Runner or Pace Chaser |
| Blue Rose Closer | △ | △ | 2.5 | 200 | / | Consistent, but weak effect |
| Our Ticket to Win! | △ | △ | 2.5 | 200 | / | Side block on Last Straight is rare, weak effect as well makes it not worth getting |
| Just a Little Farther! | △ | ✕ | 2.5 | 200 | / | Fairly consistent, but also weak |
| #LookatCurren | △ | △ | 2.5 | 200 | / | Slightly consistent but effect is really weak since it usually activates at Mid-Race |
| Nemesis | △ | ◯ | 2.5 | 200 | / | Consistent for Late Surgers/End Closers but effect is weak |
| SPARKLY☆STARDOM | △ | ▲ | 2.5 | 200 | / | Mostly consistent for most Front Runners and helps them maintain their lead |
| Shadow Break | △ | ◯ | 2.5 | 200 | / | Should be consistent but effect isn't great enough to be used over other similar uniques |
| Eternal Moments | △ | △ | 2.5 | 200 | / | Fairly consistent for non-Front-Runners, but the effect is weak |
| Flowery☆Maneuver | △ | ▲ | 2.5 | 200 | / | ① Strong for Front/Pace on some tracks to carry over speed on final corner<br>② Strong for Late/End on tracks that start the Last Spurt on final corner |
| You and Me! One-on-One! | △ | △ | 2.5 | 200 | / | Decent Last Straight speed skill for Late Surgers or End Closers |
| Lights of Vaudeville | △ | ◯ | 2.5 | 200 | / | Consistent activation but effectiveness depends on track |
| A Kiss for Courage | △ | △ | 2.5 | 200 | / | Varying effectiveness depending on track but can be strong with Triple 7s activation |
| I Never Goof Up! | △ | ◯ | 2.5 | 200 | / | Good effect but rng and track dependent |
| Bountiful Harvest | △ | △ | 2.5 | 200 | / | Consistent but relatively weak |
| YUMMY☆SPEED! | △ | ✕ | 2.5 | 200 | / | Unfortunate timing at 60% of the Race makes this skill's acceleration practically useless |
| OMG! (ﾟ∀ﾟ) The Final Sprint! ☆ | △ | △ | 2.5 | 200 | / | Generally, when you overtake in Late-Race, you're still accelerating, so a Target Speed skill wouldn't be effective |
| Give Mummy a Hug ♡ | △ | ◯ | 2.5 | 200 | / | Good accel for tracks that have their Last Spurt Mode begin on/near a Last Straight |
| Chasing After You | △ | △ | 2.5 | 200 | / | Very weak effect but can be used as a debuff |
| Arrows Whistle, Shadows Disperse | △ | ◯ | 2.5 | 200 | / | Consistent, but weak effect |
| Pop & Polish | △ | ◯ | 2.5 | 200 | / | Consistent, but weak effect |
| Presents from X | △ | △ | 2.5 | 200 | / | Consistent, but weak effect |
| Festive Miracle | △ | ◯ | 2.5 | 200 | / | Strong on some tracks where Triple 7s can proc before the Last Spurt |
| Fairy Tale | △ | △ | 2.5 | 200 | / | Strong on some tracks where Triple 7s can proc before the Last Spurt |
| Straightaway Recovery | △ | △ | 2.94 | 170 | / | Inconsistent, it might be wasted on an early or late activation |
| Breath of Fresh Air | △ | △ | 3.53 | 170+170 | / | Inconsistent, it might be wasted on an early or late activation |
| Lay Low | △ | ✕ | 3.12 | 160 | / | Might proc in Early-Race which might overflow HP |
| Iron Will | △ | ✕ | 3.75 | 160+160 | / | Might proc in Early-Race which might overflow HP |
| Pace Strategy | △ | ✕ | 2.94 | 170 | / | Being overtaken is an inconsistent condition<br>More suitable on long, backline Run Styles |
| Indomitable | △ | ✕ | 3.53 | 170+170 | / | Being overtaken is an inconsistent condition<br>More suitable on long, backline Run Styles |
| Triple 7s | △ | ▲ | 3.12 | 160 | / | Consistent, but only effective on <2400m tracks, useful for some Uma that rely on Stamina skill procs |
| Shake It Out | △ | ✕ | 5 | 100 | / | Late-Race recovery is ineffective<br>consider acquiring it only for Team Trials because it's very cheap |
| Ignited Spirit STA | △ | △ | 2.5 | 200 | / | Definitely an option but it costs more than a usual skill (at 200 base SP) |
| Burning Spirit STA | △ | △ | 3 | 200+200 | / | Definitely an option but it costs more than a usual skill (at 200 base SP) |
| Moxie | △ | ◯ | 2.78 | 180 | Front Runner | Consistent activation but recovery can be useless when<br>the uphill is located at anywhere other than Mid-Race |
| Restless | △ | △ | 3.33 | 180+180 | Front Runner | Consistent activation but recovery can be useless when<br>the uphill is located at anywhere other than Mid-Race |
| U=ma2 | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Pure Heart | △ | △ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Super-Duper Climax | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Superior Heal | △ | △ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Dazzl'n ♪ Diver | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Every Rose Has Its Fangs | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Corner Acceleration ◯ | △ | ✕ | 2.78 | 180 | / | Acceleration on the Corner 1/First Corner of any track is useless |
| Corner Connoisseur | △ | ✕ | 3.33 | 180+180 | / | Acceleration on the Corner 1/First Corner of any track is useless |
| Straightaway Acceleration | △ | ✕ | 2.94 | 170 | / | Random straight activations are too inconsistent to be effective |
| Rushing Gale! | △ | ✕ | 3.53 | 170+170 | / | Random straight activations are too inconsistent to be effective |
| Highlander | △ | ◎ | 3.12 | 160 | / | Very powerful on tracks with Uphills right before/as Last Spurt Mode begins |
| Groundwork | △ | ▲ | 5 | 100 | / | For Front Runners only, use with 3 Early-Race skills like Focus/Concentration+Green Skills |
| Final Push | △ | ✕ | 2.78 | 180 | Front Runner | Being in 1st isn't completely consistent, but it's a rare skill that can be useful on tracks where<br>your Uma enters Last Spurt Mode slightly after where the Final Corner begins/right at where the Final Corner is |
| Unrestrained | △ | ✕ | 3.33 | 180+180 | Front Runner | Being in 1st isn't completely consistent, but it's a rare skill that can be useful on tracks where<br>your Uma enters Last Spurt Mode slightly after where the Final Corner begins/right at where the Final Corner is |
| KEEP IT REAL. | △ | ✕ | 2.5 | 200 | / | Mostly useless accel but consistent activation |
| Moving Past, and Beyond | △ | ✕ | 2.5 | 200 | / | Mostly useless accel but consistent activation |
| Prudent Positioning | △ | ▲ | 4.17 | 120 | / | Use with Dodging Danger for a very powerful Early-Race burst of speed (Front Runner only) |
| Center Stage | △ | ✕ | 5 | 120+120 | / | Never use for Front-Runners that want to run the Dodging Danger tech |
| Go with the Flow | △ | ✕ | 4.17 | 120 | / | Random non-Early-Race Lane Movement Speed for non-Front-Runners are useless<br>Take only because they are very cheap and if you have no other options |
| Lane Legerdemain | △ | ✕ | 5 | 120+120 | / | Random non-Early-Race Lane Movement Speed for non-Front-Runners are useless<br>Take only because they are very cheap and if you have no other options |
| Ignited Spirit WIT | △ | ▲ | 2.5 | 200 | / | Use with Dodging Danger for a very powerful Early-Race burst of speed (Front Runner only) |
| Burning Spirit WIT | △ | ✕ | 3 | 200+200 | / | Never use for Front-Runners that want to run the Dodging Danger tech |
| Dodging Danger | △ | ⍟ | 4.55 | 110 | Front Runner | Use with Prudent Positioning/Ignition Spirit WIT for a very powerful Early-Race burst of speed (Front Runner only) |
| Sixth Sense | △ | ✕ | 5.45 | 110+110 | Front Runner | Never use for Front-Runners that want to run the "Prudent Positioning" + "Dodging Danger" combo |
| [Location] Racecourse ◯ | △ | ◎ | 5.56 | 90 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| [Ground Condition] Conditions ◯ | △ | ◎ | 5.56 | 90 | / | Power Stat increase is decent but low priority |
| [Weather] Days ◯ | △ | △ | 5.56 | 90 | / | Guts is extremely unimportant, only take it you really need to |
| [Run Style] Savvy ◎ | △ | ▲ | 2.08 | 110+130 | [Run Style] | Consistent activation, FoV buff is useful for Nice Nature's All-Seeing Eyes |

##### ✕ Avoid (Team Trials): 37 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| Risky Business | ✕ | ✕ | 4.17 | 120 | / | This skill can completely kill your stamina, it's definitely not worth it unless you're trying to do some niche strat |
| Cut and Drive! | ✕ | ✕ | 2.5 | 200 | / | Not the most consistent, and also a weak effect, not worth taking |
| G00 1st. F∞; | ✕ | △ | 2.5 | 200 | / | 0.15m/s but has two additional checks (for Start Delay and Rushed) |
| Genius x Bakushin = Victory | ✕ | △ | 2.5 | 200 | / | Fairly consistent, but also weak |
| I See Victory in My Future! | ✕ | ✕ | 2.5 | 200 | / | Front Block condition is downright horrible |
| Prideful King | ✕ | ✕ | 2.5 | 200 | / | Extremely inconsistent, if not totally impossible to even activate in any distance but Sprint |
| Schwarzes Schwert | ✕ | △ | 2.5 | 200 | / | 0.15m/s but requires two additional checks (for Start Delay and Rushed) |
| A Princess Must Seize Victory! | ✕ | ✕ | 2.5 | 200 | / | Side block condition on the Last Straight is quite strict and difficult to proc |
| Dancing in the Leaves | ✕ | ✕ | 2.5 | 200 | / | Side Block isn't consistent, effect isn't outstanding either |
| Calm in a Crowd | ✕ | ✕ | 2.94 | 170 | / | Almost impossible to be boxed in on all sides in CM |
| Unruffled | ✕ | ✕ | 3.53 | 170+170 | / | Almost impossible to be boxed in on all sides in CM |
| Second Wind | ✕ | ✕ | 2.78 | 180 | Front Runner | Expensive and impossible to activate on Front Runners, plus, Mid-Race acceleration is useless |
| Restart | ✕ | ✕ | 3.85 | 130 | Front Runner | Last Half of the Pack, at Random Point during Early-Race, ≥5s after Race Start |
| [Rotation]-Handed ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Speed stat increase is significant |
| [Season] Runner ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Speed stat increase is significant |
| Fall Frenzy | ✕ | ✕ | 3.64 | 90+110+130 | / | Take only on Autumn CMs |
| Outer Post Proficiency ◯ | ✕ | ✕ | 5.56 | 90 | / | Post Numbers 6-8 is inconsistent |
| Outer Post Proficiency ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Post Numbers 6-8 is inconsistent |
| Maverick ◯ | ✕ | ✕ | 5.56 | 90 | / | Very rare to have no Umas use your run style |
| Maverick ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Very rare to have no Umas use your run style |
| Long Shot ◯ | ✕ | ✕ | 5.56 | 90 | / | Popularity-dependent skills are inconsistent |
| Long Shot ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Popularity-dependent skills are inconsistent |
| Sympathy | ✕ | ▲ | 7.14 | 70 | / | Practically impossible to proc |
| [Location] Racecourse ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Yodo Invicta | ✕ | ✕ | 3.64 | 90+110+130 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Standard Distance ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Non-Standard Distance ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| [Ground Condition] Conditions ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Power Stat increase is decent but low priority |
| Competitive Spirit ◯ | ✕ | ✕ | 5.56 | 90 | / | It's unlikely for 40% of the lobby to use the same run style as you |
| Competitive Spirit ◎ | ✕ | ✕ | 2.5 | 90+110 | / | It's unlikely for 40% of the lobby to use the same run style as you |
| [Weather] Days ◎ | ✕ | △ | 2.5 | 90+110 | / | Guts is extremely unimportant, only take it you really need to |
| Target in Sight ◯ | ✕ | ✕ | 5.56 | 90 | / | Guts is extremely unimportant, only take it you really need to |
| Target in Sight ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Guts is extremely unimportant, only take it you really need to |
| Inner Post Proficiency ◯ | ✕ | ✕ | 5.56 | 90 | / | Post Numbers 1-3 is inconsistent |
| Inner Post Proficiency ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Post Numbers 1-3 is inconsistent |
| Lucky Seven | ✕ | ✕ | 4.55 | 110 | / | Inconsistent, even more so than the Post Proficiency skills |
| Super Lucky Seven | ✕ | ✕ | 5.45 | 110+110 | / | Inconsistent, even more so than the Post Proficiency skills |

##### Quick view: skills grouped by PvP tier

- **⍟ Essential (11):** [Run Style] Corners ◯; [Run Style] Straightaways ◯; [Distance] Corners ◯; [Distance] Straightaways ◯; Early Lead; Taking the Lead; [Run Style] Corners ◎; [Run Style] Straightaways ◎; [Distance] Corners ◎; [Distance] Straightaways ◎; Dodging Danger
- **◎ Top tier (45):** Uma Stan; Super Stan; Tail Held High; Slipstream; Playtime's Over!; Burning Spirit GUTS; Fast-Paced; Escape Artist; Corner Recovery ◯; Swinging Maestro; Ignited Spirit PWR; Burning Spirit PWR; Hesitant [Run Style]s; Subdued [Run Style]s; Flustered [Run Style]s; Trick (Front); Tantalizing Trick; Trick (Rear); Lone Wolf; Ignited Spirit GUTS; Nimble Navigator; No Stopping Me!; Frenzied [Run Style]s; [Rotation]-Handed ◯; [Season] Runner ◯; Standard Distance ◯; Non-Standard Distance ◯; Shooting for Victory!; Let's Pump Some Iron!; Angling and Scheming; Leader's Pride; Certain Victory; Sky-High Teio Step; Triumphant Pulse; Victoria por plancha ☆; Behold Thine Emperor's Divine Might; Highlander; [Location] Racecourse ◯; [Ground Condition] Conditions ◯; [Rotation]-Handed ◎; [Season] Runner ◎; [Location] Racecourse ◎; Standard Distance ◎; Non-Standard Distance ◎; [Ground Condition] Conditions ◎
- **◯ Good (20):** [Run Style] Savvy ◯; Professor of Curvature; Beeline Burst; It's On!; In Body and Mind; Shooting Star; The Duty of Dignity Calls; This Dance Is for Vittoria!; Blazing Pride; ∴win Q.E.D.; Flashy☆Landing; Nemesis; Shadow Break; Lights of Vaudeville; I Never Goof Up!; Give Mummy a Hug ♡; Arrows Whistle, Shadows Disperse; Pop & Polish; Festive Miracle; Moxie
- **▲ Situational (12):** Focus; Concentration; Runaway; Resplendent Red Ace; SPARKLY☆STARDOM; Flowery☆Maneuver; Triple 7s; Groundwork; Prudent Positioning; Ignited Spirit WIT; [Run Style] Savvy ◎; Sympathy
- **△ Low priority (32):** Corner Adept ◯; Straightaway Adept; Ramp Up; Homestretch Haste; Ignited Spirit SPD; Burning Spirit SPD; Legacy of the Strong; The View from the Lead is Mine!; Where There's a Will, There's a Way; Blue Rose Closer; Our Ticket to Win!; #LookatCurren; Eternal Moments; You and Me! One-on-One!; A Kiss for Courage; Bountiful Harvest; OMG! (ﾟ∀ﾟ) The Final Sprint! ☆; Chasing After You; Presents from X; Fairy Tale; Straightaway Recovery; Breath of Fresh Air; Ignited Spirit STA; Burning Spirit STA; Restless; Pure Heart; Superior Heal; [Weather] Days ◯; G00 1st. F∞;; Genius x Bakushin = Victory; Schwarzes Schwert; [Weather] Days ◎
- **✕ Avoid (53):** Red Shift/LP1211-M; Condor's Fury; Anchors Aweigh!; Just a Little Farther!; YUMMY☆SPEED!; Lay Low; Iron Will; Pace Strategy; Indomitable; Shake It Out; U=ma2; Super-Duper Climax; Dazzl'n ♪ Diver; Every Rose Has Its Fangs; Corner Acceleration ◯; Corner Connoisseur; Straightaway Acceleration; Rushing Gale!; Final Push; Unrestrained; KEEP IT REAL.; Moving Past, and Beyond; Center Stage; Go with the Flow; Lane Legerdemain; Burning Spirit WIT; Sixth Sense; Risky Business; Cut and Drive!; I See Victory in My Future!; Prideful King; A Princess Must Seize Victory!; Dancing in the Leaves; Calm in a Crowd; Unruffled; Second Wind; Restart; Fall Frenzy; Outer Post Proficiency ◯; Outer Post Proficiency ◎; Maverick ◯; Maverick ◎; Long Shot ◯; Long Shot ◎; Yodo Invicta; Competitive Spirit ◯; Competitive Spirit ◎; Target in Sight ◯; Target in Sight ◎; Inner Post Proficiency ◯; Inner Post Proficiency ◎; Lucky Seven; Super Lucky Seven

#### Pace Chaser

176 skills ranked for this build, grouped by their **Team Trials** tier. The PvP rank of each skill is shown in its own column.

##### ◎ Top tier (Team Trials): 28 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| [Run Style] Corners ◯ | ◎ | ⍟ | 3.85 | 130 | [Run Style] | Cheap and consistent, they are must-haves |
| [Run Style] Straightaways ◯ | ◎ | ⍟ | 3.85 | 130 | [Run Style] | Cheap and consistent, they are must-haves |
| [Distance] Corners ◯ | ◎ | ⍟ | 5 | 100 | [Distance] | Cheap and consistent, they are must-haves |
| [Distance] Straightaways ◯ | ◎ | ⍟ | 5 | 100 | [Distance] | Cheap and consistent, they are must-haves |
| Uma Stan | ◎ | ◎ | 3.12 | 160 | / | Best speed skill on longer tracks for non-Front-Runners, can help to release PDM on some longer tracks |
| Super Stan | ◎ | ◎ | 3.75 | 160+160 | / | Best speed skill on longer tracks for non-Front-Runners, can help to release PDM on some longer tracks |
| Tail Held High | ◎ | ◎ | 5 | 100 | / | Cheap and consistent, though note the condition of requiring 3 skill activations before acquiring it |
| Slipstream | ◎ | ◎ | 3.12 | 160 | / | Consistent and facilitates overtaking when activated |
| Playtime's Over! | ◎ | ◎ | 3.12 | 160 | / | Consistent and improves Uma's capacity to maintain her placement |
| Burning Spirit GUTS | ◎ | ◎ | 3 | 200+200 | / | Good random Late-Race accel but in the game's current state,<br>this skill's effect is likely 80% (when Total Guts ≤ 1200) or 90% (when 1200 < Total Guts ≤ 1600) |
| Corner Recovery ◯ | ◎ | ◎ | 2.94 | 170 | / | Consistent and effective recovery |
| Swinging Maestro | ◎ | ◎ | 3.53 | 170+170 | / | Consistent and effective recovery |
| Preferred Position | ◎ | ◯ | 2.78 | 180 | Pace Chaser | Consistent and effective recovery |
| Race Planner | ◎ | ◎ | 3.33 | 180+180 | Pace Chaser | Consistent and effective recovery |
| Hydrate | ◎ | ◯ | 2.78 | 180 | Pace Chaser | Consistent and effective recovery |
| Gourmand | ◎ | ◎ | 3.33 | 180+180 | Pace Chaser | Consistent and effective recovery |
| Ignited Spirit PWR | ◎ | ◎ | 2.5 | 200 | / | It's like a weaker but universal Slick Surge/On Your Left! |
| Burning Spirit PWR | ◎ | ◎ | 3 | 200+200 | / | It's like a weaker but universal Slick Surge/On Your Left! |
| Focus | ◎ | ▲ | 3.57 | 140 | / | Only take for Front Runners, Focus reduces the chance of a Late Start, while Concentration makes it impossible<br>You also get score for "strong starts" in Team Trials, so Concentration is always good there |
| Concentration | ◎ | ▲ | 4.29 | 140+140 | / | Only take for Front Runners, Focus reduces the chance of a Late Start, while Concentration makes it impossible<br>You also get score for "strong starts" in Team Trials, so Concentration is always good there |
| Hesitant [Run Style]s | ◎ | ◎ | 3.85 | 130 | / | Random Point in Late-Race |
| Subdued [Run Style]s | ◎ | ◎ | 3.85 | 130 | / | Random Point in Early-Race, ≥5 after Race Start |
| Flustered [Run Style]s | ◎ | ◎ | 3.85 | 130 | / | Random Point in Mid-Race |
| Trick (Front) | ◎ | ◎ | 3.57 | 140 | / | First Half of the Pack, ≥1 "Rushed" Uma behind |
| Tantalizing Trick | ◎ | ◎ | 4.29 | 140+140 | / | First Half of the Pack, ≥1 "Rushed" Uma behind |
| Trick (Rear) | ◎ | ◎ | 3.57 | 140 | / | 2nd-9th/12th Place, ≥1 "Rushed" Uma ahead |
| Lone Wolf | ◎ | ◎ | 7.14 | 70 | / | Easy to proc, you either benefit (you proc) or make it even (you prevent someone else's from proc'ing) |
| [Run Style] Savvy ◯ | ◎ | ◯ | 4.55 | 110 | [Run Style] | Consistent activation, FoV buff is useful for Nice Nature's All-Seeing Eyes |

##### ◯ Good (Team Trials): 13 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| Professor of Curvature | ◯ | ◯ | 3.33 | 180+180 | / | Consistent, but expensive<br>Rare ver. has greater speed boost making it more worth to acquire |
| Beeline Burst | ◯ | ◯ | 3.53 | 170+170 | / | Consistent |
| It's On! | ◯ | ◯ | 3.53 | 170+170 | / | Consistent. Even better when used in tandem with Tail Held High, Slipstream, and Playtime's Over! |
| In Body and Mind | ◯ | ◯ | 3.53 | 170+170 | / | Useful and (fairly) consistent Last Spurt speed boost, falls short of ◎ because it could activate at the very end of a race |
| Ignited Spirit GUTS | ◯ | ◎ | 2.5 | 200 | / | Good random Late-Race accel but in the game's current state,<br>this skill's effect is likely 80% (when Total Guts ≤ 1200) or 90% (when 1200 < Total Guts ≤ 1600) |
| Nimble Navigator | ◯ | ◎ | 3.33 | 150 | / | Strong accel but rng-dependent |
| No Stopping Me! | ◯ | ◎ | 4 | 150+150 | / | Strong accel but rng-dependent |
| Head-On | ◯ | ⍟ | 2.78 | 180 | Pace Chaser | Pace Chaser ver. of Slick Surge |
| Frenzied [Run Style]s | ◯ | ◎ | 3.85 | 130 | / | [Run Style] is "Rushed" |
| [Rotation]-Handed ◯ | ◯ | ◎ | 5.56 | 90 | / | Speed stat increase is significant |
| [Season] Runner ◯ | ◯ | ◎ | 5.56 | 90 | / | Speed stat increase is significant |
| Standard Distance ◯ | ◯ | ◎ | 5.56 | 90 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Non-Standard Distance ◯ | ◯ | ◎ | 5.56 | 90 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |

##### ▲ Situational (Team Trials): 5 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| Red Shift/LP1211-M | ▲ | ✕ | 2.5 | 200 | / | Powerful accel for Fronts/Paces, especially on tracks where Last Spurt Mode begins slightly before or on the Final Corner |
| Shooting for Victory! | ▲ | ◎ | 2.5 | 200 | / | Powerful accel for Paces/Lates, especially on tracks where Last Spurt Mode begins slightly before or on the Second Half of the Final Corner |
| Let's Pump Some Iron! | ▲ | ◎ | 2.5 | 200 | / | Strongest but most inconsistent accel for Lates/Ends on tracks where Last Spurt Mode begins slightly before or on the Final Corner |
| Angling and Scheming | ▲ | ◎ | 2.5 | 200 | / | Strongest accel for Fronts on tracks where Last Spurt Mode begins on a Corner |
| Condor's Fury | ▲ | ✕ | 2.5 | 200 | / | Powerful accel for Lates/Ends, especially on tracks where Last Spurt Mode begins slightly before or on the Final Corner |

##### △ Low priority (Team Trials): 95 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| [Run Style] Corners ◎ | △ | ⍟ | 1.85 | 130+140 | [Run Style] | Cheap and consistent, they are must-haves |
| [Run Style] Straightaways ◎ | △ | ⍟ | 1.85 | 130+140 | [Run Style] | Cheap and consistent, they are must-haves |
| [Distance] Corners ◎ | △ | ⍟ | 2.38 | 100+110 | [Distance] | Cheap and consistent, they are must-haves |
| [Distance] Straightaways ◎ | △ | ⍟ | 2.38 | 100+110 | [Distance] | Cheap and consistent, they are must-haves |
| Corner Adept ◯ | △ | △ | 2.78 | 180 | / | Consistent, but expensive<br>Rare ver. has greater speed boost making it more worth to acquire |
| Straightaway Adept | △ | △ | 2.94 | 170 | / | Consistent |
| Ramp Up | △ | △ | 2.94 | 170 | / | Consistent. Even better when used in tandem with Tail Held High, Slipstream, and Playtime's Over! |
| Homestretch Haste | △ | △ | 2.94 | 170 | / | Useful and (fairly) consistent Last Spurt speed boost, falls short of ◎ because it could activate at the very end of a race |
| Ignited Spirit SPD | △ | △ | 2.5 | 200 | / | 1.8s isn't very long and it costs 200 base SP |
| Burning Spirit SPD | △ | △ | 3 | 200+200 | / | 1.8s isn't very long and it costs 200 base SP |
| Prepared to Pass | △ | △ | 2.78 | 180 | Pace Chaser | Consistent but Target Speed boost during Final Corners are only useful if Uma will enter Last Spurt Mode in a few seconds/has already entered Last Spurt Mode.<br>Otherwise, boosting Target Speed right when Uma enters Last Spurt Mode renders it useless (doesn't actually increase speed since Uma's Current Speed hasn't reached Target Speed) |
| Speed Star | △ | △ | 3.33 | 180+180 | Pace Chaser | Consistent but Target Speed boost during Final Corners are only useful if Uma will enter Last Spurt Mode in a few seconds/has already entered Last Spurt Mode.<br>Otherwise, boosting Target Speed right when Uma enters Last Spurt Mode renders it useless (doesn't actually increase speed since Uma's Current Speed hasn't reached Target Speed) |
| Certain Victory | △ | ◎ | 2.5 | 200 | / | Identical to OG Teio's unique with slightly looser conditions |
| Legacy of the Strong | △ | △ | 2.5 | 200 | / | Effects aren't bad but inconsistent activation |
| Shooting Star | △ | ◯ | 2.5 | 200 | / | Consistent activation, but weak effect |
| The View from the Lead is Mine! | △ | △ | 2.5 | 200 | / | Somewhat consistent activation for Front Runners, but weak effect |
| Sky-High Teio Step | △ | ◎ | 2.5 | 200 | / | Mostly consistent for non-Front-Runners, with strong effect |
| Triumphant Pulse | △ | ◎ | 2.5 | 200 | / | Consistent for non-Front-Runners, with strong effect |
| Anchors Aweigh! | △ | ✕ | 2.5 | 200 | / | Consistent for Late Surgers/End Closers but minimal effect |
| Resplendent Red Ace | △ | ▲ | 2.5 | 200 | / | Accel can come in handy occasionally but still very situational and slightly unreliable |
| Where There's a Will, There's a Way | △ | △ | 2.5 | 200 | / | Decent speed skill option for non-Front-Runners |
| The Duty of Dignity Calls | △ | ◯ | 2.5 | 200 | / | Final Corner Target Speed boost is inconsistent (especially in Med race), but it can be situationally good for Front Runners/Pace Chasers |
| Victoria por plancha ☆ | △ | ◎ | 2.5 | 200 | / | Activation is mostly consistent, some tracks benefit from a Last Straight accel |
| This Dance Is for Vittoria! | △ | ◯ | 2.5 | 200 | / | Fairly consistent activation but Final Corner Target Speed boost could be inconsistent |
| Behold Thine Emperor's Divine Might | △ | ◎ | 2.5 | 200 | / | Consistent for non-Front-Runners, with strong effect |
| Blazing Pride | △ | ◯ | 2.5 | 200 | / | Final Corner Target Speed boost is inconsistent (especially in Med race), but it can be situationally good for Late Surgers |
| ∴win Q.E.D. | △ | ◯ | 2.5 | 200 | / | Final Corner Target Speed boost is inconsistent (especially in Med race), but it can be situationally good for Front Runners |
| Flashy☆Landing | △ | ◯ | 2.5 | 200 | / | Acceleration on and beyond Final Corner is decent, conditions to activate may not be consistent unless you're Front Runner or Pace Chaser |
| Blue Rose Closer | △ | △ | 2.5 | 200 | / | Consistent, but weak effect |
| Our Ticket to Win! | △ | △ | 2.5 | 200 | / | Side block on Last Straight is rare, weak effect as well makes it not worth getting |
| Just a Little Farther! | △ | ✕ | 2.5 | 200 | / | Fairly consistent, but also weak |
| #LookatCurren | △ | △ | 2.5 | 200 | / | Slightly consistent but effect is really weak since it usually activates at Mid-Race |
| Nemesis | △ | ◯ | 2.5 | 200 | / | Consistent for Late Surgers/End Closers but effect is weak |
| SPARKLY☆STARDOM | △ | ▲ | 2.5 | 200 | / | Mostly consistent for most Front Runners and helps them maintain their lead |
| Shadow Break | △ | ◯ | 2.5 | 200 | / | Should be consistent but effect isn't great enough to be used over other similar uniques |
| Eternal Moments | △ | △ | 2.5 | 200 | / | Fairly consistent for non-Front-Runners, but the effect is weak |
| Flowery☆Maneuver | △ | ▲ | 2.5 | 200 | / | ① Strong for Front/Pace on some tracks to carry over speed on final corner<br>② Strong for Late/End on tracks that start the Last Spurt on final corner |
| You and Me! One-on-One! | △ | △ | 2.5 | 200 | / | Decent Last Straight speed skill for Late Surgers or End Closers |
| Lights of Vaudeville | △ | ◯ | 2.5 | 200 | / | Consistent activation but effectiveness depends on track |
| A Kiss for Courage | △ | △ | 2.5 | 200 | / | Varying effectiveness depending on track but can be strong with Triple 7s activation |
| I Never Goof Up! | △ | ◯ | 2.5 | 200 | / | Good effect but rng and track dependent |
| Bountiful Harvest | △ | △ | 2.5 | 200 | / | Consistent but relatively weak |
| YUMMY☆SPEED! | △ | ✕ | 2.5 | 200 | / | Unfortunate timing at 60% of the Race makes this skill's acceleration practically useless |
| OMG! (ﾟ∀ﾟ) The Final Sprint! ☆ | △ | △ | 2.5 | 200 | / | Generally, when you overtake in Late-Race, you're still accelerating, so a Target Speed skill wouldn't be effective |
| Give Mummy a Hug ♡ | △ | ◯ | 2.5 | 200 | / | Good accel for tracks that have their Last Spurt Mode begin on/near a Last Straight |
| Chasing After You | △ | △ | 2.5 | 200 | / | Very weak effect but can be used as a debuff |
| Arrows Whistle, Shadows Disperse | △ | ◯ | 2.5 | 200 | / | Consistent, but weak effect |
| Pop & Polish | △ | ◯ | 2.5 | 200 | / | Consistent, but weak effect |
| Presents from X | △ | △ | 2.5 | 200 | / | Consistent, but weak effect |
| Festive Miracle | △ | ◯ | 2.5 | 200 | / | Strong on some tracks where Triple 7s can proc before the Last Spurt |
| Fairy Tale | △ | △ | 2.5 | 200 | / | Strong on some tracks where Triple 7s can proc before the Last Spurt |
| Straightaway Recovery | △ | △ | 2.94 | 170 | / | Inconsistent, it might be wasted on an early or late activation |
| Breath of Fresh Air | △ | △ | 3.53 | 170+170 | / | Inconsistent, it might be wasted on an early or late activation |
| Lay Low | △ | ✕ | 3.12 | 160 | / | Might proc in Early-Race which might overflow HP |
| Iron Will | △ | ✕ | 3.75 | 160+160 | / | Might proc in Early-Race which might overflow HP |
| Pace Strategy | △ | ✕ | 2.94 | 170 | / | Being overtaken is an inconsistent condition<br>More suitable on long, backline Run Styles |
| Indomitable | △ | ✕ | 3.53 | 170+170 | / | Being overtaken is an inconsistent condition<br>More suitable on long, backline Run Styles |
| Triple 7s | △ | ▲ | 3.12 | 160 | / | Consistent, but only effective on <2400m tracks, useful for some Uma that rely on Stamina skill procs |
| Shake It Out | △ | ✕ | 5 | 100 | / | Late-Race recovery is ineffective<br>consider acquiring it only for Team Trials because it's very cheap |
| Ignited Spirit STA | △ | △ | 2.5 | 200 | / | Definitely an option but it costs more than a usual skill (at 200 base SP) |
| Burning Spirit STA | △ | △ | 3 | 200+200 | / | Definitely an option but it costs more than a usual skill (at 200 base SP) |
| Stamina to Spare | △ | ◯ | 2.78 | 180 | Pace Chaser | Stamina to Spare is okay as its recovery is unlikely to overflow (making it a decent choice),<br>but Calm and Collected may recover too much in a few situations (making it less consistent) |
| Calm and Collected | △ | ◎ | 3.33 | 180+180 | Pace Chaser | Stamina to Spare is okay as its recovery is unlikely to overflow (making it a decent choice),<br>but Calm and Collected may recover too much in a few situations (making it less consistent) |
| U=ma2 | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Pure Heart | △ | △ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Super-Duper Climax | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Superior Heal | △ | △ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Dazzl'n ♪ Diver | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Every Rose Has Its Fangs | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Corner Acceleration ◯ | △ | ✕ | 2.78 | 180 | / | Acceleration on the Corner 1/First Corner of any track is useless |
| Corner Connoisseur | △ | ✕ | 3.33 | 180+180 | / | Acceleration on the Corner 1/First Corner of any track is useless |
| Straightaway Acceleration | △ | ✕ | 2.94 | 170 | / | Random straight activations are too inconsistent to be effective |
| Rushing Gale! | △ | ✕ | 3.53 | 170+170 | / | Random straight activations are too inconsistent to be effective |
| Highlander | △ | ◎ | 3.12 | 160 | / | Very powerful on tracks with Uphills right before/as Last Spurt Mode begins |
| Groundwork | △ | ▲ | 5 | 100 | / | For Front Runners only, use with 3 Early-Race skills like Focus/Concentration+Green Skills |
| Shrewd Step | △ | ✕ | 4.17 | 120 | Pace Chaser | Cheap and consistent activation, but useless Mid-Race accel |
| Technician | △ | ✕ | 5 | 120+120 | Pace Chaser | Cheap and consistent activation, but useless Mid-Race accel |
| Straight Descent | △ | ⍟ | 4.17 | 120 | Pace Chaser | Very powerful on tracks with Downhills right before/as Last Spurt Mode begins |
| Determined Descent | △ | ⍟ | 5 | 120+120 | Pace Chaser | Very powerful on tracks with Downhills right before/as Last Spurt Mode begins |
| Tactical Tweak | △ | ✕ | 4.17 | 120 | Pace Chaser | Cheap and consistent activation, but useless Mid-Race accel |
| Shatterproof | △ | ✕ | 5 | 120+120 | Pace Chaser | Cheap and consistent activation, but useless Mid-Race accel |
| KEEP IT REAL. | △ | ✕ | 2.5 | 200 | / | Mostly useless accel but consistent activation |
| Moving Past, and Beyond | △ | ✕ | 2.5 | 200 | / | Mostly useless accel but consistent activation |
| Prudent Positioning | △ | ▲ | 4.17 | 120 | / | Use with Dodging Danger for a very powerful Early-Race burst of speed (Front Runner only) |
| Center Stage | △ | ✕ | 5 | 120+120 | / | Never use for Front-Runners that want to run the Dodging Danger tech |
| Go with the Flow | △ | ✕ | 4.17 | 120 | / | Random non-Early-Race Lane Movement Speed for non-Front-Runners are useless<br>Take only because they are very cheap and if you have no other options |
| Lane Legerdemain | △ | ✕ | 5 | 120+120 | / | Random non-Early-Race Lane Movement Speed for non-Front-Runners are useless<br>Take only because they are very cheap and if you have no other options |
| Ignited Spirit WIT | △ | ▲ | 2.5 | 200 | / | Use with Dodging Danger for a very powerful Early-Race burst of speed (Front Runner only) |
| Burning Spirit WIT | △ | ✕ | 3 | 200+200 | / | Never use for Front-Runners that want to run the Dodging Danger tech |
| Disorient | △ | △ | 4.55 | 110 | Pace Chaser | First Half of the Pack, at Random Point during Late-Race |
| Dazzling Disorientation | △ | △ | 5.45 | 110+110 | Pace Chaser | First Half of the Pack, at Random Point during Late-Race |
| [Location] Racecourse ◯ | △ | ◎ | 5.56 | 90 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| [Ground Condition] Conditions ◯ | △ | ◎ | 5.56 | 90 | / | Power Stat increase is decent but low priority |
| [Weather] Days ◯ | △ | △ | 5.56 | 90 | / | Guts is extremely unimportant, only take it you really need to |
| [Run Style] Savvy ◎ | △ | ▲ | 2.08 | 110+130 | [Run Style] | Consistent activation, FoV buff is useful for Nice Nature's All-Seeing Eyes |

##### ✕ Avoid (Team Trials): 35 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| Risky Business | ✕ | ✕ | 4.17 | 120 | / | This skill can completely kill your stamina, it's definitely not worth it unless you're trying to do some niche strat |
| Cut and Drive! | ✕ | ✕ | 2.5 | 200 | / | Not the most consistent, and also a weak effect, not worth taking |
| G00 1st. F∞; | ✕ | △ | 2.5 | 200 | / | 0.15m/s but has two additional checks (for Start Delay and Rushed) |
| Genius x Bakushin = Victory | ✕ | △ | 2.5 | 200 | / | Fairly consistent, but also weak |
| I See Victory in My Future! | ✕ | ✕ | 2.5 | 200 | / | Front Block condition is downright horrible |
| Prideful King | ✕ | ✕ | 2.5 | 200 | / | Extremely inconsistent, if not totally impossible to even activate in any distance but Sprint |
| Schwarzes Schwert | ✕ | △ | 2.5 | 200 | / | 0.15m/s but requires two additional checks (for Start Delay and Rushed) |
| A Princess Must Seize Victory! | ✕ | ✕ | 2.5 | 200 | / | Side block condition on the Last Straight is quite strict and difficult to proc |
| Dancing in the Leaves | ✕ | ✕ | 2.5 | 200 | / | Side Block isn't consistent, effect isn't outstanding either |
| Calm in a Crowd | ✕ | ✕ | 2.94 | 170 | / | Almost impossible to be boxed in on all sides in CM |
| Unruffled | ✕ | ✕ | 3.53 | 170+170 | / | Almost impossible to be boxed in on all sides in CM |
| [Rotation]-Handed ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Speed stat increase is significant |
| [Season] Runner ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Speed stat increase is significant |
| Fall Frenzy | ✕ | ✕ | 3.64 | 90+110+130 | / | Take only on Autumn CMs |
| Outer Post Proficiency ◯ | ✕ | ✕ | 5.56 | 90 | / | Post Numbers 6-8 is inconsistent |
| Outer Post Proficiency ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Post Numbers 6-8 is inconsistent |
| Maverick ◯ | ✕ | ✕ | 5.56 | 90 | / | Very rare to have no Umas use your run style |
| Maverick ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Very rare to have no Umas use your run style |
| Long Shot ◯ | ✕ | ✕ | 5.56 | 90 | / | Popularity-dependent skills are inconsistent |
| Long Shot ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Popularity-dependent skills are inconsistent |
| Sympathy | ✕ | ▲ | 7.14 | 70 | / | Practically impossible to proc |
| [Location] Racecourse ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Yodo Invicta | ✕ | ✕ | 3.64 | 90+110+130 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Standard Distance ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Non-Standard Distance ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| [Ground Condition] Conditions ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Power Stat increase is decent but low priority |
| Competitive Spirit ◯ | ✕ | ✕ | 5.56 | 90 | / | It's unlikely for 40% of the lobby to use the same run style as you |
| Competitive Spirit ◎ | ✕ | ✕ | 2.5 | 90+110 | / | It's unlikely for 40% of the lobby to use the same run style as you |
| [Weather] Days ◎ | ✕ | △ | 2.5 | 90+110 | / | Guts is extremely unimportant, only take it you really need to |
| Target in Sight ◯ | ✕ | ✕ | 5.56 | 90 | / | Guts is extremely unimportant, only take it you really need to |
| Target in Sight ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Guts is extremely unimportant, only take it you really need to |
| Inner Post Proficiency ◯ | ✕ | ✕ | 5.56 | 90 | / | Post Numbers 1-3 is inconsistent |
| Inner Post Proficiency ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Post Numbers 1-3 is inconsistent |
| Lucky Seven | ✕ | ✕ | 4.55 | 110 | / | Inconsistent, even more so than the Post Proficiency skills |
| Super Lucky Seven | ✕ | ✕ | 5.45 | 110+110 | / | Inconsistent, even more so than the Post Proficiency skills |

##### Quick view: skills grouped by PvP tier

- **⍟ Essential (11):** [Run Style] Corners ◯; [Run Style] Straightaways ◯; [Distance] Corners ◯; [Distance] Straightaways ◯; Head-On; [Run Style] Corners ◎; [Run Style] Straightaways ◎; [Distance] Corners ◎; [Distance] Straightaways ◎; Straight Descent; Determined Descent
- **◎ Top tier (45):** Uma Stan; Super Stan; Tail Held High; Slipstream; Playtime's Over!; Burning Spirit GUTS; Corner Recovery ◯; Swinging Maestro; Race Planner; Gourmand; Ignited Spirit PWR; Burning Spirit PWR; Hesitant [Run Style]s; Subdued [Run Style]s; Flustered [Run Style]s; Trick (Front); Tantalizing Trick; Trick (Rear); Lone Wolf; Ignited Spirit GUTS; Nimble Navigator; No Stopping Me!; Frenzied [Run Style]s; [Rotation]-Handed ◯; [Season] Runner ◯; Standard Distance ◯; Non-Standard Distance ◯; Shooting for Victory!; Let's Pump Some Iron!; Angling and Scheming; Certain Victory; Sky-High Teio Step; Triumphant Pulse; Victoria por plancha ☆; Behold Thine Emperor's Divine Might; Calm and Collected; Highlander; [Location] Racecourse ◯; [Ground Condition] Conditions ◯; [Rotation]-Handed ◎; [Season] Runner ◎; [Location] Racecourse ◎; Standard Distance ◎; Non-Standard Distance ◎; [Ground Condition] Conditions ◎
- **◯ Good (22):** Preferred Position; Hydrate; [Run Style] Savvy ◯; Professor of Curvature; Beeline Burst; It's On!; In Body and Mind; Shooting Star; The Duty of Dignity Calls; This Dance Is for Vittoria!; Blazing Pride; ∴win Q.E.D.; Flashy☆Landing; Nemesis; Shadow Break; Lights of Vaudeville; I Never Goof Up!; Give Mummy a Hug ♡; Arrows Whistle, Shadows Disperse; Pop & Polish; Festive Miracle; Stamina to Spare
- **▲ Situational (11):** Focus; Concentration; Resplendent Red Ace; SPARKLY☆STARDOM; Flowery☆Maneuver; Triple 7s; Groundwork; Prudent Positioning; Ignited Spirit WIT; [Run Style] Savvy ◎; Sympathy
- **△ Low priority (35):** Corner Adept ◯; Straightaway Adept; Ramp Up; Homestretch Haste; Ignited Spirit SPD; Burning Spirit SPD; Prepared to Pass; Speed Star; Legacy of the Strong; The View from the Lead is Mine!; Where There's a Will, There's a Way; Blue Rose Closer; Our Ticket to Win!; #LookatCurren; Eternal Moments; You and Me! One-on-One!; A Kiss for Courage; Bountiful Harvest; OMG! (ﾟ∀ﾟ) The Final Sprint! ☆; Chasing After You; Presents from X; Fairy Tale; Straightaway Recovery; Breath of Fresh Air; Ignited Spirit STA; Burning Spirit STA; Pure Heart; Superior Heal; Disorient; Dazzling Disorientation; [Weather] Days ◯; G00 1st. F∞;; Genius x Bakushin = Victory; Schwarzes Schwert; [Weather] Days ◎
- **✕ Avoid (52):** Red Shift/LP1211-M; Condor's Fury; Anchors Aweigh!; Just a Little Farther!; YUMMY☆SPEED!; Lay Low; Iron Will; Pace Strategy; Indomitable; Shake It Out; U=ma2; Super-Duper Climax; Dazzl'n ♪ Diver; Every Rose Has Its Fangs; Corner Acceleration ◯; Corner Connoisseur; Straightaway Acceleration; Rushing Gale!; Shrewd Step; Technician; Tactical Tweak; Shatterproof; KEEP IT REAL.; Moving Past, and Beyond; Center Stage; Go with the Flow; Lane Legerdemain; Burning Spirit WIT; Risky Business; Cut and Drive!; I See Victory in My Future!; Prideful King; A Princess Must Seize Victory!; Dancing in the Leaves; Calm in a Crowd; Unruffled; Fall Frenzy; Outer Post Proficiency ◯; Outer Post Proficiency ◎; Maverick ◯; Maverick ◎; Long Shot ◯; Long Shot ◎; Yodo Invicta; Competitive Spirit ◯; Competitive Spirit ◎; Target in Sight ◯; Target in Sight ◎; Inner Post Proficiency ◯; Inner Post Proficiency ◎; Lucky Seven; Super Lucky Seven

#### Late Surger

177 skills ranked for this build, grouped by their **Team Trials** tier. The PvP rank of each skill is shown in its own column.

##### ◎ Top tier (Team Trials): 28 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| [Run Style] Corners ◯ | ◎ | ⍟ | 3.85 | 130 | [Run Style] | Cheap and consistent, they are must-haves |
| [Run Style] Straightaways ◯ | ◎ | ⍟ | 3.85 | 130 | [Run Style] | Cheap and consistent, they are must-haves |
| [Distance] Corners ◯ | ◎ | ⍟ | 5 | 100 | [Distance] | Cheap and consistent, they are must-haves |
| [Distance] Straightaways ◯ | ◎ | ⍟ | 5 | 100 | [Distance] | Cheap and consistent, they are must-haves |
| Uma Stan | ◎ | ◎ | 3.12 | 160 | / | Best speed skill on longer tracks for non-Front-Runners, can help to release PDM on some longer tracks |
| Super Stan | ◎ | ◎ | 3.75 | 160+160 | / | Best speed skill on longer tracks for non-Front-Runners, can help to release PDM on some longer tracks |
| Tail Held High | ◎ | ◎ | 5 | 100 | / | Cheap and consistent, though note the condition of requiring 3 skill activations before acquiring it |
| Slipstream | ◎ | ◎ | 3.12 | 160 | / | Consistent and facilitates overtaking when activated |
| Playtime's Over! | ◎ | ◎ | 3.12 | 160 | / | Consistent and improves Uma's capacity to maintain her placement |
| Burning Spirit GUTS | ◎ | ◎ | 3 | 200+200 | / | Good random Late-Race accel but in the game's current state,<br>this skill's effect is likely 80% (when Total Guts ≤ 1200) or 90% (when 1200 < Total Guts ≤ 1600) |
| 1,500,000 CC | ◎ | ◎ | 4.17 | 120 | Late Surger | Cheap and consistent |
| 15,000,000 CC | ◎ | ◎ | 5 | 120+120 | Late Surger | Cheap and consistent |
| Corner Recovery ◯ | ◎ | ◎ | 2.94 | 170 | / | Consistent and effective recovery |
| Swinging Maestro | ◎ | ◎ | 3.53 | 170+170 | / | Consistent and effective recovery |
| Ignited Spirit PWR | ◎ | ◎ | 2.5 | 200 | / | It's like a weaker but universal Slick Surge/On Your Left! |
| Burning Spirit PWR | ◎ | ◎ | 3 | 200+200 | / | It's like a weaker but universal Slick Surge/On Your Left! |
| Focus | ◎ | ▲ | 3.57 | 140 | / | Only take for Front Runners, Focus reduces the chance of a Late Start, while Concentration makes it impossible<br>You also get score for "strong starts" in Team Trials, so Concentration is always good there |
| Concentration | ◎ | ▲ | 4.29 | 140+140 | / | Only take for Front Runners, Focus reduces the chance of a Late Start, while Concentration makes it impossible<br>You also get score for "strong starts" in Team Trials, so Concentration is always good there |
| Hesitant [Run Style]s | ◎ | ◎ | 3.85 | 130 | / | Random Point in Late-Race |
| Subdued [Run Style]s | ◎ | ◎ | 3.85 | 130 | / | Random Point in Early-Race, ≥5 after Race Start |
| Flustered [Run Style]s | ◎ | ◎ | 3.85 | 130 | / | Random Point in Mid-Race |
| Trick (Front) | ◎ | ◎ | 3.57 | 140 | / | First Half of the Pack, ≥1 "Rushed" Uma behind |
| Tantalizing Trick | ◎ | ◎ | 4.29 | 140+140 | / | First Half of the Pack, ≥1 "Rushed" Uma behind |
| Trick (Rear) | ◎ | ◎ | 3.57 | 140 | / | 2nd-9th/12th Place, ≥1 "Rushed" Uma ahead |
| Sharp Gaze | ◎ | ◎ | 2.78 | 180 | Late Surger | Last Half of the Pack, at Random Point during Late-Race |
| All-Seeing Eyes | ◎ | ◎ | 3.33 | 180+180 | Late Surger | Last Half of the Pack, at Random Point during Late-Race |
| Lone Wolf | ◎ | ◎ | 7.14 | 70 | / | Easy to proc, you either benefit (you proc) or make it even (you prevent someone else's from proc'ing) |
| [Run Style] Savvy ◯ | ◎ | ◯ | 4.55 | 110 | [Run Style] | Consistent activation, FoV buff is useful for Nice Nature's All-Seeing Eyes |

##### ◯ Good (Team Trials): 18 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| Professor of Curvature | ◯ | ◯ | 3.33 | 180+180 | / | Consistent, but expensive<br>Rare ver. has greater speed boost making it more worth to acquire |
| Beeline Burst | ◯ | ◯ | 3.53 | 170+170 | / | Consistent |
| It's On! | ◯ | ◯ | 3.53 | 170+170 | / | Consistent. Even better when used in tandem with Tail Held High, Slipstream, and Playtime's Over! |
| In Body and Mind | ◯ | ◯ | 3.53 | 170+170 | / | Useful and (fairly) consistent Last Spurt speed boost, falls short of ◎ because it could activate at the very end of a race |
| Ignited Spirit GUTS | ◯ | ◎ | 2.5 | 200 | / | Good random Late-Race accel but in the game's current state,<br>this skill's effect is likely 80% (when Total Guts ≤ 1200) or 90% (when 1200 < Total Guts ≤ 1600) |
| Position Pilfer | ◯ | ◯ | 2.78 | 180 | Late Surger | Consistent |
| Fast & Furious | ◯ | ◎ | 3.33 | 180+180 | Late Surger | Consistent |
| Outer Swell | ◯ | ◎ | 2.78 | 180 | Late Surger | Somewhat consistent but Target Speed boost during Final Corners are only useful if Uma will enter Last Spurt Mode in a few seconds/has already entered Last Spurt Mode.<br>Otherwise, boosting Target Speed right when Uma enters Last Spurt Mode renders it useless (doesn't actually increase speed since Uma's Current Speed hasn't reached Target Speed) |
| Rising Dragon | ◯ | ◎ | 3.33 | 180+180 | Late Surger | Somewhat consistent but Target Speed boost during Final Corners are only useful if Uma will enter Last Spurt Mode in a few seconds/has already entered Last Spurt Mode.<br>Otherwise, boosting Target Speed right when Uma enters Last Spurt Mode renders it useless (doesn't actually increase speed since Uma's Current Speed hasn't reached Target Speed) |
| Nimble Navigator | ◯ | ◎ | 3.33 | 150 | / | Strong accel but rng-dependent |
| No Stopping Me! | ◯ | ◎ | 4 | 150+150 | / | Strong accel but rng-dependent |
| Slick Surge | ◯ | ⍟ | 2.78 | 180 | Late Surger | Good but inconsistently effective accel |
| On Your Left! | ◯ | ⍟ | 3.33 | 180+180 | Late Surger | Good but inconsistently effective accel |
| Frenzied [Run Style]s | ◯ | ◎ | 3.85 | 130 | / | [Run Style] is "Rushed" |
| [Rotation]-Handed ◯ | ◯ | ◎ | 5.56 | 90 | / | Speed stat increase is significant |
| [Season] Runner ◯ | ◯ | ◎ | 5.56 | 90 | / | Speed stat increase is significant |
| Standard Distance ◯ | ◯ | ◎ | 5.56 | 90 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Non-Standard Distance ◯ | ◯ | ◎ | 5.56 | 90 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |

##### ▲ Situational (Team Trials): 5 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| Red Shift/LP1211-M | ▲ | ✕ | 2.5 | 200 | / | Powerful accel for Fronts/Paces, especially on tracks where Last Spurt Mode begins slightly before or on the Final Corner |
| Shooting for Victory! | ▲ | ◎ | 2.5 | 200 | / | Powerful accel for Paces/Lates, especially on tracks where Last Spurt Mode begins slightly before or on the Second Half of the Final Corner |
| Let's Pump Some Iron! | ▲ | ◎ | 2.5 | 200 | / | Strongest but most inconsistent accel for Lates/Ends on tracks where Last Spurt Mode begins slightly before or on the Final Corner |
| Angling and Scheming | ▲ | ◎ | 2.5 | 200 | / | Strongest accel for Fronts on tracks where Last Spurt Mode begins on a Corner |
| Condor's Fury | ▲ | ✕ | 2.5 | 200 | / | Powerful accel for Lates/Ends, especially on tracks where Last Spurt Mode begins slightly before or on the Final Corner |

##### △ Low priority (Team Trials): 91 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| [Run Style] Corners ◎ | △ | ⍟ | 1.85 | 130+140 | [Run Style] | Cheap and consistent, they are must-haves |
| [Run Style] Straightaways ◎ | △ | ⍟ | 1.85 | 130+140 | [Run Style] | Cheap and consistent, they are must-haves |
| [Distance] Corners ◎ | △ | ⍟ | 2.38 | 100+110 | [Distance] | Cheap and consistent, they are must-haves |
| [Distance] Straightaways ◎ | △ | ⍟ | 2.38 | 100+110 | [Distance] | Cheap and consistent, they are must-haves |
| Corner Adept ◯ | △ | △ | 2.78 | 180 | / | Consistent, but expensive<br>Rare ver. has greater speed boost making it more worth to acquire |
| Straightaway Adept | △ | △ | 2.94 | 170 | / | Consistent |
| Ramp Up | △ | △ | 2.94 | 170 | / | Consistent. Even better when used in tandem with Tail Held High, Slipstream, and Playtime's Over! |
| Homestretch Haste | △ | △ | 2.94 | 170 | / | Useful and (fairly) consistent Last Spurt speed boost, falls short of ◎ because it could activate at the very end of a race |
| Ignited Spirit SPD | △ | △ | 2.5 | 200 | / | 1.8s isn't very long and it costs 200 base SP |
| Burning Spirit SPD | △ | △ | 3 | 200+200 | / | 1.8s isn't very long and it costs 200 base SP |
| Certain Victory | △ | ◎ | 2.5 | 200 | / | Identical to OG Teio's unique with slightly looser conditions |
| Legacy of the Strong | △ | △ | 2.5 | 200 | / | Effects aren't bad but inconsistent activation |
| Shooting Star | △ | ◯ | 2.5 | 200 | / | Consistent activation, but weak effect |
| The View from the Lead is Mine! | △ | △ | 2.5 | 200 | / | Somewhat consistent activation for Front Runners, but weak effect |
| Sky-High Teio Step | △ | ◎ | 2.5 | 200 | / | Mostly consistent for non-Front-Runners, with strong effect |
| Triumphant Pulse | △ | ◎ | 2.5 | 200 | / | Consistent for non-Front-Runners, with strong effect |
| Anchors Aweigh! | △ | ✕ | 2.5 | 200 | / | Consistent for Late Surgers/End Closers but minimal effect |
| Resplendent Red Ace | △ | ▲ | 2.5 | 200 | / | Accel can come in handy occasionally but still very situational and slightly unreliable |
| Where There's a Will, There's a Way | △ | △ | 2.5 | 200 | / | Decent speed skill option for non-Front-Runners |
| The Duty of Dignity Calls | △ | ◯ | 2.5 | 200 | / | Final Corner Target Speed boost is inconsistent (especially in Med race), but it can be situationally good for Front Runners/Pace Chasers |
| Victoria por plancha ☆ | △ | ◎ | 2.5 | 200 | / | Activation is mostly consistent, some tracks benefit from a Last Straight accel |
| This Dance Is for Vittoria! | △ | ◯ | 2.5 | 200 | / | Fairly consistent activation but Final Corner Target Speed boost could be inconsistent |
| Behold Thine Emperor's Divine Might | △ | ◎ | 2.5 | 200 | / | Consistent for non-Front-Runners, with strong effect |
| Blazing Pride | △ | ◯ | 2.5 | 200 | / | Final Corner Target Speed boost is inconsistent (especially in Med race), but it can be situationally good for Late Surgers |
| ∴win Q.E.D. | △ | ◯ | 2.5 | 200 | / | Final Corner Target Speed boost is inconsistent (especially in Med race), but it can be situationally good for Front Runners |
| Flashy☆Landing | △ | ◯ | 2.5 | 200 | / | Acceleration on and beyond Final Corner is decent, conditions to activate may not be consistent unless you're Front Runner or Pace Chaser |
| Blue Rose Closer | △ | △ | 2.5 | 200 | / | Consistent, but weak effect |
| Our Ticket to Win! | △ | △ | 2.5 | 200 | / | Side block on Last Straight is rare, weak effect as well makes it not worth getting |
| Just a Little Farther! | △ | ✕ | 2.5 | 200 | / | Fairly consistent, but also weak |
| #LookatCurren | △ | △ | 2.5 | 200 | / | Slightly consistent but effect is really weak since it usually activates at Mid-Race |
| Nemesis | △ | ◯ | 2.5 | 200 | / | Consistent for Late Surgers/End Closers but effect is weak |
| SPARKLY☆STARDOM | △ | ▲ | 2.5 | 200 | / | Mostly consistent for most Front Runners and helps them maintain their lead |
| Shadow Break | △ | ◯ | 2.5 | 200 | / | Should be consistent but effect isn't great enough to be used over other similar uniques |
| Eternal Moments | △ | △ | 2.5 | 200 | / | Fairly consistent for non-Front-Runners, but the effect is weak |
| Flowery☆Maneuver | △ | ▲ | 2.5 | 200 | / | ① Strong for Front/Pace on some tracks to carry over speed on final corner<br>② Strong for Late/End on tracks that start the Last Spurt on final corner |
| You and Me! One-on-One! | △ | △ | 2.5 | 200 | / | Decent Last Straight speed skill for Late Surgers or End Closers |
| Lights of Vaudeville | △ | ◯ | 2.5 | 200 | / | Consistent activation but effectiveness depends on track |
| A Kiss for Courage | △ | △ | 2.5 | 200 | / | Varying effectiveness depending on track but can be strong with Triple 7s activation |
| I Never Goof Up! | △ | ◯ | 2.5 | 200 | / | Good effect but rng and track dependent |
| Bountiful Harvest | △ | △ | 2.5 | 200 | / | Consistent but relatively weak |
| YUMMY☆SPEED! | △ | ✕ | 2.5 | 200 | / | Unfortunate timing at 60% of the Race makes this skill's acceleration practically useless |
| OMG! (ﾟ∀ﾟ) The Final Sprint! ☆ | △ | △ | 2.5 | 200 | / | Generally, when you overtake in Late-Race, you're still accelerating, so a Target Speed skill wouldn't be effective |
| Give Mummy a Hug ♡ | △ | ◯ | 2.5 | 200 | / | Good accel for tracks that have their Last Spurt Mode begin on/near a Last Straight |
| Chasing After You | △ | △ | 2.5 | 200 | / | Very weak effect but can be used as a debuff |
| Arrows Whistle, Shadows Disperse | △ | ◯ | 2.5 | 200 | / | Consistent, but weak effect |
| Pop & Polish | △ | ◯ | 2.5 | 200 | / | Consistent, but weak effect |
| Presents from X | △ | △ | 2.5 | 200 | / | Consistent, but weak effect |
| Festive Miracle | △ | ◯ | 2.5 | 200 | / | Strong on some tracks where Triple 7s can proc before the Last Spurt |
| Fairy Tale | △ | △ | 2.5 | 200 | / | Strong on some tracks where Triple 7s can proc before the Last Spurt |
| Straightaway Recovery | △ | △ | 2.94 | 170 | / | Inconsistent, it might be wasted on an early or late activation |
| Breath of Fresh Air | △ | △ | 3.53 | 170+170 | / | Inconsistent, it might be wasted on an early or late activation |
| Lay Low | △ | ✕ | 3.12 | 160 | / | Might proc in Early-Race which might overflow HP |
| Iron Will | △ | ✕ | 3.75 | 160+160 | / | Might proc in Early-Race which might overflow HP |
| Pace Strategy | △ | ✕ | 2.94 | 170 | / | Being overtaken is an inconsistent condition<br>More suitable on long, backline Run Styles |
| Indomitable | △ | ✕ | 3.53 | 170+170 | / | Being overtaken is an inconsistent condition<br>More suitable on long, backline Run Styles |
| Triple 7s | △ | ▲ | 3.12 | 160 | / | Consistent, but only effective on <2400m tracks, useful for some Uma that rely on Stamina skill procs |
| Shake It Out | △ | ✕ | 5 | 100 | / | Late-Race recovery is ineffective<br>consider acquiring it only for Team Trials because it's very cheap |
| Ignited Spirit STA | △ | △ | 2.5 | 200 | / | Definitely an option but it costs more than a usual skill (at 200 base SP) |
| Burning Spirit STA | △ | △ | 3 | 200+200 | / | Definitely an option but it costs more than a usual skill (at 200 base SP) |
| A Small Breather | △ | ✕ | 2.78 | 180 | Late Surger | Late-Race recovery is ineffective, Last Spurt recalculation isn't added until 1st Year Anniversary |
| Relax | △ | ✕ | 3.33 | 180+180 | Late Surger | Late-Race recovery is ineffective, Last Spurt recalculation isn't added until 1st Year Anniversary |
| Be Still | △ | ◯ | 2.78 | 180 | Late Surger | Late-Race recovery is ineffective, Last Spurt recalculation isn't added until 1st Year Anniversary |
| Lie in Wait | △ | ◎ | 3.33 | 180+180 | Late Surger | Late-Race recovery is ineffective, Last Spurt recalculation isn't added until 1st Year Anniversary |
| U=ma2 | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Pure Heart | △ | △ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Super-Duper Climax | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Superior Heal | △ | △ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Dazzl'n ♪ Diver | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Every Rose Has Its Fangs | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Corner Acceleration ◯ | △ | ✕ | 2.78 | 180 | / | Acceleration on the Corner 1/First Corner of any track is useless |
| Corner Connoisseur | △ | ✕ | 3.33 | 180+180 | / | Acceleration on the Corner 1/First Corner of any track is useless |
| Straightaway Acceleration | △ | ✕ | 2.94 | 170 | / | Random straight activations are too inconsistent to be effective |
| Rushing Gale! | △ | ✕ | 3.53 | 170+170 | / | Random straight activations are too inconsistent to be effective |
| Highlander | △ | ◎ | 3.12 | 160 | / | Very powerful on tracks with Uphills right before/as Last Spurt Mode begins |
| Groundwork | △ | ▲ | 5 | 100 | / | For Front Runners only, use with 3 Early-Race skills like Focus/Concentration+Green Skills |
| Fighter | △ | ✕ | 4.17 | 120 | Late Surger | Cheap and consistent activation but useless Mid-Race accel |
| Hard Worker | △ | ✕ | 5 | 120+120 | Late Surger | Cheap and consistent activation but useless Mid-Race accel |
| KEEP IT REAL. | △ | ✕ | 2.5 | 200 | / | Mostly useless accel but consistent activation |
| Moving Past, and Beyond | △ | ✕ | 2.5 | 200 | / | Mostly useless accel but consistent activation |
| Prudent Positioning | △ | ▲ | 4.17 | 120 | / | Use with Dodging Danger for a very powerful Early-Race burst of speed (Front Runner only) |
| Center Stage | △ | ✕ | 5 | 120+120 | / | Never use for Front-Runners that want to run the Dodging Danger tech |
| Go with the Flow | △ | ✕ | 4.17 | 120 | / | Random non-Early-Race Lane Movement Speed for non-Front-Runners are useless<br>Take only because they are very cheap and if you have no other options |
| Lane Legerdemain | △ | ✕ | 5 | 120+120 | / | Random non-Early-Race Lane Movement Speed for non-Front-Runners are useless<br>Take only because they are very cheap and if you have no other options |
| Ignited Spirit WIT | △ | ▲ | 2.5 | 200 | / | Use with Dodging Danger for a very powerful Early-Race burst of speed (Front Runner only) |
| Burning Spirit WIT | △ | ✕ | 3 | 200+200 | / | Never use for Front-Runners that want to run the Dodging Danger tech |
| Studious | △ | ✕ | 4.17 | 120 | Late Surger | Extra FoV is mostly useless<br>Take only because they are very cheap and if you have no other options |
| The Bigger Picture | △ | ✕ | 5 | 120+120 | Late Surger | Extra FoV is mostly useless<br>Take only because they are very cheap and if you have no other options |
| [Location] Racecourse ◯ | △ | ◎ | 5.56 | 90 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| [Ground Condition] Conditions ◯ | △ | ◎ | 5.56 | 90 | / | Power Stat increase is decent but low priority |
| [Weather] Days ◯ | △ | △ | 5.56 | 90 | / | Guts is extremely unimportant, only take it you really need to |
| [Run Style] Savvy ◎ | △ | ▲ | 2.08 | 110+130 | [Run Style] | Consistent activation, FoV buff is useful for Nice Nature's All-Seeing Eyes |

##### ✕ Avoid (Team Trials): 35 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| Risky Business | ✕ | ✕ | 4.17 | 120 | / | This skill can completely kill your stamina, it's definitely not worth it unless you're trying to do some niche strat |
| Cut and Drive! | ✕ | ✕ | 2.5 | 200 | / | Not the most consistent, and also a weak effect, not worth taking |
| G00 1st. F∞; | ✕ | △ | 2.5 | 200 | / | 0.15m/s but has two additional checks (for Start Delay and Rushed) |
| Genius x Bakushin = Victory | ✕ | △ | 2.5 | 200 | / | Fairly consistent, but also weak |
| I See Victory in My Future! | ✕ | ✕ | 2.5 | 200 | / | Front Block condition is downright horrible |
| Prideful King | ✕ | ✕ | 2.5 | 200 | / | Extremely inconsistent, if not totally impossible to even activate in any distance but Sprint |
| Schwarzes Schwert | ✕ | △ | 2.5 | 200 | / | 0.15m/s but requires two additional checks (for Start Delay and Rushed) |
| A Princess Must Seize Victory! | ✕ | ✕ | 2.5 | 200 | / | Side block condition on the Last Straight is quite strict and difficult to proc |
| Dancing in the Leaves | ✕ | ✕ | 2.5 | 200 | / | Side Block isn't consistent, effect isn't outstanding either |
| Calm in a Crowd | ✕ | ✕ | 2.94 | 170 | / | Almost impossible to be boxed in on all sides in CM |
| Unruffled | ✕ | ✕ | 3.53 | 170+170 | / | Almost impossible to be boxed in on all sides in CM |
| [Rotation]-Handed ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Speed stat increase is significant |
| [Season] Runner ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Speed stat increase is significant |
| Fall Frenzy | ✕ | ✕ | 3.64 | 90+110+130 | / | Take only on Autumn CMs |
| Outer Post Proficiency ◯ | ✕ | ✕ | 5.56 | 90 | / | Post Numbers 6-8 is inconsistent |
| Outer Post Proficiency ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Post Numbers 6-8 is inconsistent |
| Maverick ◯ | ✕ | ✕ | 5.56 | 90 | / | Very rare to have no Umas use your run style |
| Maverick ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Very rare to have no Umas use your run style |
| Long Shot ◯ | ✕ | ✕ | 5.56 | 90 | / | Popularity-dependent skills are inconsistent |
| Long Shot ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Popularity-dependent skills are inconsistent |
| Sympathy | ✕ | ▲ | 7.14 | 70 | / | Practically impossible to proc |
| [Location] Racecourse ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Yodo Invicta | ✕ | ✕ | 3.64 | 90+110+130 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Standard Distance ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Non-Standard Distance ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| [Ground Condition] Conditions ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Power Stat increase is decent but low priority |
| Competitive Spirit ◯ | ✕ | ✕ | 5.56 | 90 | / | It's unlikely for 40% of the lobby to use the same run style as you |
| Competitive Spirit ◎ | ✕ | ✕ | 2.5 | 90+110 | / | It's unlikely for 40% of the lobby to use the same run style as you |
| [Weather] Days ◎ | ✕ | △ | 2.5 | 90+110 | / | Guts is extremely unimportant, only take it you really need to |
| Target in Sight ◯ | ✕ | ✕ | 5.56 | 90 | / | Guts is extremely unimportant, only take it you really need to |
| Target in Sight ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Guts is extremely unimportant, only take it you really need to |
| Inner Post Proficiency ◯ | ✕ | ✕ | 5.56 | 90 | / | Post Numbers 1-3 is inconsistent |
| Inner Post Proficiency ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Post Numbers 1-3 is inconsistent |
| Lucky Seven | ✕ | ✕ | 4.55 | 110 | / | Inconsistent, even more so than the Post Proficiency skills |
| Super Lucky Seven | ✕ | ✕ | 5.45 | 110+110 | / | Inconsistent, even more so than the Post Proficiency skills |

##### Quick view: skills grouped by PvP tier

- **⍟ Essential (10):** [Run Style] Corners ◯; [Run Style] Straightaways ◯; [Distance] Corners ◯; [Distance] Straightaways ◯; Slick Surge; On Your Left!; [Run Style] Corners ◎; [Run Style] Straightaways ◎; [Distance] Corners ◎; [Distance] Straightaways ◎
- **◎ Top tier (50):** Uma Stan; Super Stan; Tail Held High; Slipstream; Playtime's Over!; Burning Spirit GUTS; 1,500,000 CC; 15,000,000 CC; Corner Recovery ◯; Swinging Maestro; Ignited Spirit PWR; Burning Spirit PWR; Hesitant [Run Style]s; Subdued [Run Style]s; Flustered [Run Style]s; Trick (Front); Tantalizing Trick; Trick (Rear); Sharp Gaze; All-Seeing Eyes; Lone Wolf; Ignited Spirit GUTS; Fast & Furious; Outer Swell; Rising Dragon; Nimble Navigator; No Stopping Me!; Frenzied [Run Style]s; [Rotation]-Handed ◯; [Season] Runner ◯; Standard Distance ◯; Non-Standard Distance ◯; Shooting for Victory!; Let's Pump Some Iron!; Angling and Scheming; Certain Victory; Sky-High Teio Step; Triumphant Pulse; Victoria por plancha ☆; Behold Thine Emperor's Divine Might; Lie in Wait; Highlander; [Location] Racecourse ◯; [Ground Condition] Conditions ◯; [Rotation]-Handed ◎; [Season] Runner ◎; [Location] Racecourse ◎; Standard Distance ◎; Non-Standard Distance ◎; [Ground Condition] Conditions ◎
- **◯ Good (21):** [Run Style] Savvy ◯; Professor of Curvature; Beeline Burst; It's On!; In Body and Mind; Position Pilfer; Shooting Star; The Duty of Dignity Calls; This Dance Is for Vittoria!; Blazing Pride; ∴win Q.E.D.; Flashy☆Landing; Nemesis; Shadow Break; Lights of Vaudeville; I Never Goof Up!; Give Mummy a Hug ♡; Arrows Whistle, Shadows Disperse; Pop & Polish; Festive Miracle; Be Still
- **▲ Situational (11):** Focus; Concentration; Resplendent Red Ace; SPARKLY☆STARDOM; Flowery☆Maneuver; Triple 7s; Groundwork; Prudent Positioning; Ignited Spirit WIT; [Run Style] Savvy ◎; Sympathy
- **△ Low priority (31):** Corner Adept ◯; Straightaway Adept; Ramp Up; Homestretch Haste; Ignited Spirit SPD; Burning Spirit SPD; Legacy of the Strong; The View from the Lead is Mine!; Where There's a Will, There's a Way; Blue Rose Closer; Our Ticket to Win!; #LookatCurren; Eternal Moments; You and Me! One-on-One!; A Kiss for Courage; Bountiful Harvest; OMG! (ﾟ∀ﾟ) The Final Sprint! ☆; Chasing After You; Presents from X; Fairy Tale; Straightaway Recovery; Breath of Fresh Air; Ignited Spirit STA; Burning Spirit STA; Pure Heart; Superior Heal; [Weather] Days ◯; G00 1st. F∞;; Genius x Bakushin = Victory; Schwarzes Schwert; [Weather] Days ◎
- **✕ Avoid (54):** Red Shift/LP1211-M; Condor's Fury; Anchors Aweigh!; Just a Little Farther!; YUMMY☆SPEED!; Lay Low; Iron Will; Pace Strategy; Indomitable; Shake It Out; A Small Breather; Relax; U=ma2; Super-Duper Climax; Dazzl'n ♪ Diver; Every Rose Has Its Fangs; Corner Acceleration ◯; Corner Connoisseur; Straightaway Acceleration; Rushing Gale!; Fighter; Hard Worker; KEEP IT REAL.; Moving Past, and Beyond; Center Stage; Go with the Flow; Lane Legerdemain; Burning Spirit WIT; Studious; The Bigger Picture; Risky Business; Cut and Drive!; I See Victory in My Future!; Prideful King; A Princess Must Seize Victory!; Dancing in the Leaves; Calm in a Crowd; Unruffled; Fall Frenzy; Outer Post Proficiency ◯; Outer Post Proficiency ◎; Maverick ◯; Maverick ◎; Long Shot ◯; Long Shot ◎; Yodo Invicta; Competitive Spirit ◯; Competitive Spirit ◎; Target in Sight ◯; Target in Sight ◎; Inner Post Proficiency ◯; Inner Post Proficiency ◎; Lucky Seven; Super Lucky Seven

#### End Closer

174 skills ranked for this build, grouped by their **Team Trials** tier. The PvP rank of each skill is shown in its own column.

##### ◎ Top tier (Team Trials): 24 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| [Run Style] Corners ◯ | ◎ | ⍟ | 3.85 | 130 | [Run Style] | Cheap and consistent, they are must-haves |
| [Run Style] Straightaways ◯ | ◎ | ⍟ | 3.85 | 130 | [Run Style] | Cheap and consistent, they are must-haves |
| [Distance] Corners ◯ | ◎ | ⍟ | 5 | 100 | [Distance] | Cheap and consistent, they are must-haves |
| [Distance] Straightaways ◯ | ◎ | ⍟ | 5 | 100 | [Distance] | Cheap and consistent, they are must-haves |
| Uma Stan | ◎ | ◎ | 3.12 | 160 | / | Best speed skill on longer tracks for non-Front-Runners, can help to release PDM on some longer tracks |
| Super Stan | ◎ | ◎ | 3.75 | 160+160 | / | Best speed skill on longer tracks for non-Front-Runners, can help to release PDM on some longer tracks |
| Tail Held High | ◎ | ◎ | 5 | 100 | / | Cheap and consistent, though note the condition of requiring 3 skill activations before acquiring it |
| Slipstream | ◎ | ◎ | 3.12 | 160 | / | Consistent and facilitates overtaking when activated |
| Playtime's Over! | ◎ | ◎ | 3.12 | 160 | / | Consistent and improves Uma's capacity to maintain her placement |
| Burning Spirit GUTS | ◎ | ◎ | 3 | 200+200 | / | Good random Late-Race accel but in the game's current state,<br>this skill's effect is likely 80% (when Total Guts ≤ 1200) or 90% (when 1200 < Total Guts ≤ 1600) |
| Corner Recovery ◯ | ◎ | ◎ | 2.94 | 170 | / | Consistent and effective recovery |
| Swinging Maestro | ◎ | ◎ | 3.53 | 170+170 | / | Consistent and effective recovery |
| Ignited Spirit PWR | ◎ | ◎ | 2.5 | 200 | / | It's like a weaker but universal Slick Surge/On Your Left! |
| Burning Spirit PWR | ◎ | ◎ | 3 | 200+200 | / | It's like a weaker but universal Slick Surge/On Your Left! |
| Focus | ◎ | ▲ | 3.57 | 140 | / | Only take for Front Runners, Focus reduces the chance of a Late Start, while Concentration makes it impossible<br>You also get score for "strong starts" in Team Trials, so Concentration is always good there |
| Concentration | ◎ | ▲ | 4.29 | 140+140 | / | Only take for Front Runners, Focus reduces the chance of a Late Start, while Concentration makes it impossible<br>You also get score for "strong starts" in Team Trials, so Concentration is always good there |
| Hesitant [Run Style]s | ◎ | ◎ | 3.85 | 130 | / | Random Point in Late-Race |
| Subdued [Run Style]s | ◎ | ◎ | 3.85 | 130 | / | Random Point in Early-Race, ≥5 after Race Start |
| Flustered [Run Style]s | ◎ | ◎ | 3.85 | 130 | / | Random Point in Mid-Race |
| Trick (Front) | ◎ | ◎ | 3.57 | 140 | / | First Half of the Pack, ≥1 "Rushed" Uma behind |
| Tantalizing Trick | ◎ | ◎ | 4.29 | 140+140 | / | First Half of the Pack, ≥1 "Rushed" Uma behind |
| Trick (Rear) | ◎ | ◎ | 3.57 | 140 | / | 2nd-9th/12th Place, ≥1 "Rushed" Uma ahead |
| Lone Wolf | ◎ | ◎ | 7.14 | 70 | / | Easy to proc, you either benefit (you proc) or make it even (you prevent someone else's from proc'ing) |
| [Run Style] Savvy ◯ | ◎ | ◯ | 4.55 | 110 | [Run Style] | Consistent activation, FoV buff is useful for Nice Nature's All-Seeing Eyes |

##### ◯ Good (Team Trials): 12 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| Professor of Curvature | ◯ | ◯ | 3.33 | 180+180 | / | Consistent, but expensive<br>Rare ver. has greater speed boost making it more worth to acquire |
| Beeline Burst | ◯ | ◯ | 3.53 | 170+170 | / | Consistent |
| It's On! | ◯ | ◯ | 3.53 | 170+170 | / | Consistent. Even better when used in tandem with Tail Held High, Slipstream, and Playtime's Over! |
| In Body and Mind | ◯ | ◯ | 3.53 | 170+170 | / | Useful and (fairly) consistent Last Spurt speed boost, falls short of ◎ because it could activate at the very end of a race |
| Ignited Spirit GUTS | ◯ | ◎ | 2.5 | 200 | / | Good random Late-Race accel but in the game's current state,<br>this skill's effect is likely 80% (when Total Guts ≤ 1200) or 90% (when 1200 < Total Guts ≤ 1600) |
| Nimble Navigator | ◯ | ◎ | 3.33 | 150 | / | Strong accel but rng-dependent |
| No Stopping Me! | ◯ | ◎ | 4 | 150+150 | / | Strong accel but rng-dependent |
| Frenzied [Run Style]s | ◯ | ◎ | 3.85 | 130 | / | [Run Style] is "Rushed" |
| [Rotation]-Handed ◯ | ◯ | ◎ | 5.56 | 90 | / | Speed stat increase is significant |
| [Season] Runner ◯ | ◯ | ◎ | 5.56 | 90 | / | Speed stat increase is significant |
| Standard Distance ◯ | ◯ | ◎ | 5.56 | 90 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Non-Standard Distance ◯ | ◯ | ◎ | 5.56 | 90 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |

##### ▲ Situational (Team Trials): 5 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| Red Shift/LP1211-M | ▲ | ✕ | 2.5 | 200 | / | Powerful accel for Fronts/Paces, especially on tracks where Last Spurt Mode begins slightly before or on the Final Corner |
| Shooting for Victory! | ▲ | ◎ | 2.5 | 200 | / | Powerful accel for Paces/Lates, especially on tracks where Last Spurt Mode begins slightly before or on the Second Half of the Final Corner |
| Let's Pump Some Iron! | ▲ | ◎ | 2.5 | 200 | / | Strongest but most inconsistent accel for Lates/Ends on tracks where Last Spurt Mode begins slightly before or on the Final Corner |
| Angling and Scheming | ▲ | ◎ | 2.5 | 200 | / | Strongest accel for Fronts on tracks where Last Spurt Mode begins on a Corner |
| Condor's Fury | ▲ | ✕ | 2.5 | 200 | / | Powerful accel for Lates/Ends, especially on tracks where Last Spurt Mode begins slightly before or on the Final Corner |

##### △ Low priority (Team Trials): 96 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| [Run Style] Corners ◎ | △ | ⍟ | 1.85 | 130+140 | [Run Style] | Cheap and consistent, they are must-haves |
| [Run Style] Straightaways ◎ | △ | ⍟ | 1.85 | 130+140 | [Run Style] | Cheap and consistent, they are must-haves |
| [Distance] Corners ◎ | △ | ⍟ | 2.38 | 100+110 | [Distance] | Cheap and consistent, they are must-haves |
| [Distance] Straightaways ◎ | △ | ⍟ | 2.38 | 100+110 | [Distance] | Cheap and consistent, they are must-haves |
| Corner Adept ◯ | △ | △ | 2.78 | 180 | / | Consistent, but expensive<br>Rare ver. has greater speed boost making it more worth to acquire |
| Straightaway Adept | △ | △ | 2.94 | 170 | / | Consistent |
| Ramp Up | △ | △ | 2.94 | 170 | / | Consistent. Even better when used in tandem with Tail Held High, Slipstream, and Playtime's Over! |
| Homestretch Haste | △ | △ | 2.94 | 170 | / | Useful and (fairly) consistent Last Spurt speed boost, falls short of ◎ because it could activate at the very end of a race |
| Ignited Spirit SPD | △ | △ | 2.5 | 200 | / | 1.8s isn't very long and it costs 200 base SP |
| Burning Spirit SPD | △ | △ | 3 | 200+200 | / | 1.8s isn't very long and it costs 200 base SP |
| Early Start | △ | △ | 2.78 | 180 | End Closer | Very small speed boost, but it can unlock Pace-down Mode for a good amount of time so it isn't totally useless |
| Certain Victory | △ | ◎ | 2.5 | 200 | / | Identical to OG Teio's unique with slightly looser conditions |
| Legacy of the Strong | △ | △ | 2.5 | 200 | / | Effects aren't bad but inconsistent activation |
| Shooting Star | △ | ◯ | 2.5 | 200 | / | Consistent activation, but weak effect |
| The View from the Lead is Mine! | △ | △ | 2.5 | 200 | / | Somewhat consistent activation for Front Runners, but weak effect |
| Sky-High Teio Step | △ | ◎ | 2.5 | 200 | / | Mostly consistent for non-Front-Runners, with strong effect |
| Triumphant Pulse | △ | ◎ | 2.5 | 200 | / | Consistent for non-Front-Runners, with strong effect |
| Anchors Aweigh! | △ | ✕ | 2.5 | 200 | / | Consistent for Late Surgers/End Closers but minimal effect |
| Resplendent Red Ace | △ | ▲ | 2.5 | 200 | / | Accel can come in handy occasionally but still very situational and slightly unreliable |
| Where There's a Will, There's a Way | △ | △ | 2.5 | 200 | / | Decent speed skill option for non-Front-Runners |
| The Duty of Dignity Calls | △ | ◯ | 2.5 | 200 | / | Final Corner Target Speed boost is inconsistent (especially in Med race), but it can be situationally good for Front Runners/Pace Chasers |
| Victoria por plancha ☆ | △ | ◎ | 2.5 | 200 | / | Activation is mostly consistent, some tracks benefit from a Last Straight accel |
| This Dance Is for Vittoria! | △ | ◯ | 2.5 | 200 | / | Fairly consistent activation but Final Corner Target Speed boost could be inconsistent |
| Behold Thine Emperor's Divine Might | △ | ◎ | 2.5 | 200 | / | Consistent for non-Front-Runners, with strong effect |
| Blazing Pride | △ | ◯ | 2.5 | 200 | / | Final Corner Target Speed boost is inconsistent (especially in Med race), but it can be situationally good for Late Surgers |
| ∴win Q.E.D. | △ | ◯ | 2.5 | 200 | / | Final Corner Target Speed boost is inconsistent (especially in Med race), but it can be situationally good for Front Runners |
| Flashy☆Landing | △ | ◯ | 2.5 | 200 | / | Acceleration on and beyond Final Corner is decent, conditions to activate may not be consistent unless you're Front Runner or Pace Chaser |
| Blue Rose Closer | △ | △ | 2.5 | 200 | / | Consistent, but weak effect |
| Our Ticket to Win! | △ | △ | 2.5 | 200 | / | Side block on Last Straight is rare, weak effect as well makes it not worth getting |
| Just a Little Farther! | △ | ✕ | 2.5 | 200 | / | Fairly consistent, but also weak |
| #LookatCurren | △ | △ | 2.5 | 200 | / | Slightly consistent but effect is really weak since it usually activates at Mid-Race |
| Nemesis | △ | ◯ | 2.5 | 200 | / | Consistent for Late Surgers/End Closers but effect is weak |
| SPARKLY☆STARDOM | △ | ▲ | 2.5 | 200 | / | Mostly consistent for most Front Runners and helps them maintain their lead |
| Shadow Break | △ | ◯ | 2.5 | 200 | / | Should be consistent but effect isn't great enough to be used over other similar uniques |
| Eternal Moments | △ | △ | 2.5 | 200 | / | Fairly consistent for non-Front-Runners, but the effect is weak |
| Flowery☆Maneuver | △ | ▲ | 2.5 | 200 | / | ① Strong for Front/Pace on some tracks to carry over speed on final corner<br>② Strong for Late/End on tracks that start the Last Spurt on final corner |
| You and Me! One-on-One! | △ | △ | 2.5 | 200 | / | Decent Last Straight speed skill for Late Surgers or End Closers |
| Lights of Vaudeville | △ | ◯ | 2.5 | 200 | / | Consistent activation but effectiveness depends on track |
| A Kiss for Courage | △ | △ | 2.5 | 200 | / | Varying effectiveness depending on track but can be strong with Triple 7s activation |
| I Never Goof Up! | △ | ◯ | 2.5 | 200 | / | Good effect but rng and track dependent |
| Bountiful Harvest | △ | △ | 2.5 | 200 | / | Consistent but relatively weak |
| YUMMY☆SPEED! | △ | ✕ | 2.5 | 200 | / | Unfortunate timing at 60% of the Race makes this skill's acceleration practically useless |
| OMG! (ﾟ∀ﾟ) The Final Sprint! ☆ | △ | △ | 2.5 | 200 | / | Generally, when you overtake in Late-Race, you're still accelerating, so a Target Speed skill wouldn't be effective |
| Give Mummy a Hug ♡ | △ | ◯ | 2.5 | 200 | / | Good accel for tracks that have their Last Spurt Mode begin on/near a Last Straight |
| Chasing After You | △ | △ | 2.5 | 200 | / | Very weak effect but can be used as a debuff |
| Arrows Whistle, Shadows Disperse | △ | ◯ | 2.5 | 200 | / | Consistent, but weak effect |
| Pop & Polish | △ | ◯ | 2.5 | 200 | / | Consistent, but weak effect |
| Presents from X | △ | △ | 2.5 | 200 | / | Consistent, but weak effect |
| Festive Miracle | △ | ◯ | 2.5 | 200 | / | Strong on some tracks where Triple 7s can proc before the Last Spurt |
| Fairy Tale | △ | △ | 2.5 | 200 | / | Strong on some tracks where Triple 7s can proc before the Last Spurt |
| Straightaway Recovery | △ | △ | 2.94 | 170 | / | Inconsistent, it might be wasted on an early or late activation |
| Breath of Fresh Air | △ | △ | 3.53 | 170+170 | / | Inconsistent, it might be wasted on an early or late activation |
| Lay Low | △ | ✕ | 3.12 | 160 | / | Might proc in Early-Race which might overflow HP |
| Iron Will | △ | ✕ | 3.75 | 160+160 | / | Might proc in Early-Race which might overflow HP |
| Pace Strategy | △ | ✕ | 2.94 | 170 | / | Being overtaken is an inconsistent condition<br>More suitable on long, backline Run Styles |
| Indomitable | △ | ✕ | 3.53 | 170+170 | / | Being overtaken is an inconsistent condition<br>More suitable on long, backline Run Styles |
| Triple 7s | △ | ▲ | 3.12 | 160 | / | Consistent, but only effective on <2400m tracks, useful for some Uma that rely on Stamina skill procs |
| Shake It Out | △ | ✕ | 5 | 100 | / | Late-Race recovery is ineffective<br>consider acquiring it only for Team Trials because it's very cheap |
| Ignited Spirit STA | △ | △ | 2.5 | 200 | / | Definitely an option but it costs more than a usual skill (at 200 base SP) |
| Burning Spirit STA | △ | △ | 3 | 200+200 | / | Definitely an option but it costs more than a usual skill (at 200 base SP) |
| Standing By | △ | ✕ | 2.78 | 180 | End Closer | Somewhat consistent, but may be undesirable for well-built End Closers<br>since they can probably reach positions above 75% by distance and hence, not activate this skill |
| Sleeping Lion | △ | ✕ | 3.33 | 180+180 | End Closer | Somewhat consistent, but may be undesirable for well-built End Closers<br>since they can probably reach positions above 75% by distance and hence, not activate this skill |
| After-School Stroll | △ | ✕ | 2.94 | 170 | End Closer | Consistent activation but recovery can be useless when<br>the downhill is located at anywhere other than Mid-Race |
| Go-Home Specialist | △ | ✕ | 3.53 | 170+170 | End Closer | Consistent activation but recovery can be useless when<br>the downhill is located at anywhere other than Mid-Race |
| Levelheaded | △ | △ | 2.78 | 180 | End Closer | Getting blocked is a decently consistent condition for End Closers |
| U=ma2 | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Pure Heart | △ | △ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Super-Duper Climax | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Superior Heal | △ | △ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Dazzl'n ♪ Diver | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Every Rose Has Its Fangs | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Corner Acceleration ◯ | △ | ✕ | 2.78 | 180 | / | Acceleration on the Corner 1/First Corner of any track is useless |
| Corner Connoisseur | △ | ✕ | 3.33 | 180+180 | / | Acceleration on the Corner 1/First Corner of any track is useless |
| Straightaway Acceleration | △ | ✕ | 2.94 | 170 | / | Random straight activations are too inconsistent to be effective |
| Rushing Gale! | △ | ✕ | 3.53 | 170+170 | / | Random straight activations are too inconsistent to be effective |
| Highlander | △ | ◎ | 3.12 | 160 | / | Very powerful on tracks with Uphills right before/as Last Spurt Mode begins |
| Groundwork | △ | ▲ | 5 | 100 | / | For Front Runners only, use with 3 Early-Race skills like Focus/Concentration+Green Skills |
| Straightaway Spurt | △ | ⍟ | 2.78 | 180 | End Closer | Very powerful End Closer acceleration that works on tracks where Last Spurt Mode begins on a Straight |
| Encroaching Shadow | △ | ⍟ | 3.33 | 180+180 | End Closer | Very powerful End Closer acceleration that works on tracks where Last Spurt Mode begins on a Straight |
| KEEP IT REAL. | △ | ✕ | 2.5 | 200 | / | Mostly useless accel but consistent activation |
| Moving Past, and Beyond | △ | ✕ | 2.5 | 200 | / | Mostly useless accel but consistent activation |
| Prudent Positioning | △ | ▲ | 4.17 | 120 | / | Use with Dodging Danger for a very powerful Early-Race burst of speed (Front Runner only) |
| Center Stage | △ | ✕ | 5 | 120+120 | / | Never use for Front-Runners that want to run the Dodging Danger tech |
| Go with the Flow | △ | ✕ | 4.17 | 120 | / | Random non-Early-Race Lane Movement Speed for non-Front-Runners are useless<br>Take only because they are very cheap and if you have no other options |
| Lane Legerdemain | △ | ✕ | 5 | 120+120 | / | Random non-Early-Race Lane Movement Speed for non-Front-Runners are useless<br>Take only because they are very cheap and if you have no other options |
| Ignited Spirit WIT | △ | ▲ | 2.5 | 200 | / | Use with Dodging Danger for a very powerful Early-Race burst of speed (Front Runner only) |
| Burning Spirit WIT | △ | ✕ | 3 | 200+200 | / | Never use for Front-Runners that want to run the Dodging Danger tech |
| I Can See Right Through You | △ | ✕ | 4.55 | 110 | End Closer | Extra FoV is mostly useless<br>Take only because they are very cheap and if you have no other options |
| The Coast Is Clear! | △ | ✕ | 5.45 | 110+110 | End Closer | Extra FoV is mostly useless<br>Take only because they are very cheap and if you have no other options |
| Strategist | △ | ✕ | 4.55 | 110 | End Closer | Extra FoV is mostly useless<br>Take only because they are very cheap and if you have no other options |
| Crusader | △ | ✕ | 5.45 | 110+110 | End Closer | Extra FoV is mostly useless<br>Take only because they are very cheap and if you have no other options |
| Intense Gaze | △ | ◯ | 2.78 | 180 | End Closer | Not 1st Place, at Random Point during Late-Race |
| [Location] Racecourse ◯ | △ | ◎ | 5.56 | 90 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| [Ground Condition] Conditions ◯ | △ | ◎ | 5.56 | 90 | / | Power Stat increase is decent but low priority |
| [Weather] Days ◯ | △ | △ | 5.56 | 90 | / | Guts is extremely unimportant, only take it you really need to |
| [Run Style] Savvy ◎ | △ | ▲ | 2.08 | 110+130 | [Run Style] | Consistent activation, FoV buff is useful for Nice Nature's All-Seeing Eyes |

##### ✕ Avoid (Team Trials): 37 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| Risky Business | ✕ | ✕ | 4.17 | 120 | / | This skill can completely kill your stamina, it's definitely not worth it unless you're trying to do some niche strat |
| Masterful Gambit | ✕ | ✕ | 2.78 | 180 | End Closer | Extremely inconsistent, borderline impossible to activate as your Uma should already be at least within top 75% (by distance) of the pack by the time the Mid-Race ends |
| Sturm und Drang | ✕ | ✕ | 3.33 | 180+180 | End Closer | Extremely inconsistent, borderline impossible to activate as your Uma should already be at least within top 75% (by distance) of the pack by the time the Mid-Race ends |
| Cut and Drive! | ✕ | ✕ | 2.5 | 200 | / | Not the most consistent, and also a weak effect, not worth taking |
| G00 1st. F∞; | ✕ | △ | 2.5 | 200 | / | 0.15m/s but has two additional checks (for Start Delay and Rushed) |
| Genius x Bakushin = Victory | ✕ | △ | 2.5 | 200 | / | Fairly consistent, but also weak |
| I See Victory in My Future! | ✕ | ✕ | 2.5 | 200 | / | Front Block condition is downright horrible |
| Prideful King | ✕ | ✕ | 2.5 | 200 | / | Extremely inconsistent, if not totally impossible to even activate in any distance but Sprint |
| Schwarzes Schwert | ✕ | △ | 2.5 | 200 | / | 0.15m/s but requires two additional checks (for Start Delay and Rushed) |
| A Princess Must Seize Victory! | ✕ | ✕ | 2.5 | 200 | / | Side block condition on the Last Straight is quite strict and difficult to proc |
| Dancing in the Leaves | ✕ | ✕ | 2.5 | 200 | / | Side Block isn't consistent, effect isn't outstanding either |
| Calm in a Crowd | ✕ | ✕ | 2.94 | 170 | / | Almost impossible to be boxed in on all sides in CM |
| Unruffled | ✕ | ✕ | 3.53 | 170+170 | / | Almost impossible to be boxed in on all sides in CM |
| [Rotation]-Handed ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Speed stat increase is significant |
| [Season] Runner ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Speed stat increase is significant |
| Fall Frenzy | ✕ | ✕ | 3.64 | 90+110+130 | / | Take only on Autumn CMs |
| Outer Post Proficiency ◯ | ✕ | ✕ | 5.56 | 90 | / | Post Numbers 6-8 is inconsistent |
| Outer Post Proficiency ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Post Numbers 6-8 is inconsistent |
| Maverick ◯ | ✕ | ✕ | 5.56 | 90 | / | Very rare to have no Umas use your run style |
| Maverick ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Very rare to have no Umas use your run style |
| Long Shot ◯ | ✕ | ✕ | 5.56 | 90 | / | Popularity-dependent skills are inconsistent |
| Long Shot ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Popularity-dependent skills are inconsistent |
| Sympathy | ✕ | ▲ | 7.14 | 70 | / | Practically impossible to proc |
| [Location] Racecourse ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Yodo Invicta | ✕ | ✕ | 3.64 | 90+110+130 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Standard Distance ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Non-Standard Distance ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| [Ground Condition] Conditions ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Power Stat increase is decent but low priority |
| Competitive Spirit ◯ | ✕ | ✕ | 5.56 | 90 | / | It's unlikely for 40% of the lobby to use the same run style as you |
| Competitive Spirit ◎ | ✕ | ✕ | 2.5 | 90+110 | / | It's unlikely for 40% of the lobby to use the same run style as you |
| [Weather] Days ◎ | ✕ | △ | 2.5 | 90+110 | / | Guts is extremely unimportant, only take it you really need to |
| Target in Sight ◯ | ✕ | ✕ | 5.56 | 90 | / | Guts is extremely unimportant, only take it you really need to |
| Target in Sight ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Guts is extremely unimportant, only take it you really need to |
| Inner Post Proficiency ◯ | ✕ | ✕ | 5.56 | 90 | / | Post Numbers 1-3 is inconsistent |
| Inner Post Proficiency ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Post Numbers 1-3 is inconsistent |
| Lucky Seven | ✕ | ✕ | 4.55 | 110 | / | Inconsistent, even more so than the Post Proficiency skills |
| Super Lucky Seven | ✕ | ✕ | 5.45 | 110+110 | / | Inconsistent, even more so than the Post Proficiency skills |

##### Quick view: skills grouped by PvP tier

- **⍟ Essential (10):** [Run Style] Corners ◯; [Run Style] Straightaways ◯; [Distance] Corners ◯; [Distance] Straightaways ◯; [Run Style] Corners ◎; [Run Style] Straightaways ◎; [Distance] Corners ◎; [Distance] Straightaways ◎; Straightaway Spurt; Encroaching Shadow
- **◎ Top tier (42):** Uma Stan; Super Stan; Tail Held High; Slipstream; Playtime's Over!; Burning Spirit GUTS; Corner Recovery ◯; Swinging Maestro; Ignited Spirit PWR; Burning Spirit PWR; Hesitant [Run Style]s; Subdued [Run Style]s; Flustered [Run Style]s; Trick (Front); Tantalizing Trick; Trick (Rear); Lone Wolf; Ignited Spirit GUTS; Nimble Navigator; No Stopping Me!; Frenzied [Run Style]s; [Rotation]-Handed ◯; [Season] Runner ◯; Standard Distance ◯; Non-Standard Distance ◯; Shooting for Victory!; Let's Pump Some Iron!; Angling and Scheming; Certain Victory; Sky-High Teio Step; Triumphant Pulse; Victoria por plancha ☆; Behold Thine Emperor's Divine Might; Highlander; [Location] Racecourse ◯; [Ground Condition] Conditions ◯; [Rotation]-Handed ◎; [Season] Runner ◎; [Location] Racecourse ◎; Standard Distance ◎; Non-Standard Distance ◎; [Ground Condition] Conditions ◎
- **◯ Good (20):** [Run Style] Savvy ◯; Professor of Curvature; Beeline Burst; It's On!; In Body and Mind; Shooting Star; The Duty of Dignity Calls; This Dance Is for Vittoria!; Blazing Pride; ∴win Q.E.D.; Flashy☆Landing; Nemesis; Shadow Break; Lights of Vaudeville; I Never Goof Up!; Give Mummy a Hug ♡; Arrows Whistle, Shadows Disperse; Pop & Polish; Festive Miracle; Intense Gaze
- **▲ Situational (11):** Focus; Concentration; Resplendent Red Ace; SPARKLY☆STARDOM; Flowery☆Maneuver; Triple 7s; Groundwork; Prudent Positioning; Ignited Spirit WIT; [Run Style] Savvy ◎; Sympathy
- **△ Low priority (33):** Corner Adept ◯; Straightaway Adept; Ramp Up; Homestretch Haste; Ignited Spirit SPD; Burning Spirit SPD; Early Start; Legacy of the Strong; The View from the Lead is Mine!; Where There's a Will, There's a Way; Blue Rose Closer; Our Ticket to Win!; #LookatCurren; Eternal Moments; You and Me! One-on-One!; A Kiss for Courage; Bountiful Harvest; OMG! (ﾟ∀ﾟ) The Final Sprint! ☆; Chasing After You; Presents from X; Fairy Tale; Straightaway Recovery; Breath of Fresh Air; Ignited Spirit STA; Burning Spirit STA; Levelheaded; Pure Heart; Superior Heal; [Weather] Days ◯; G00 1st. F∞;; Genius x Bakushin = Victory; Schwarzes Schwert; [Weather] Days ◎
- **✕ Avoid (58):** Red Shift/LP1211-M; Condor's Fury; Anchors Aweigh!; Just a Little Farther!; YUMMY☆SPEED!; Lay Low; Iron Will; Pace Strategy; Indomitable; Shake It Out; Standing By; Sleeping Lion; After-School Stroll; Go-Home Specialist; U=ma2; Super-Duper Climax; Dazzl'n ♪ Diver; Every Rose Has Its Fangs; Corner Acceleration ◯; Corner Connoisseur; Straightaway Acceleration; Rushing Gale!; KEEP IT REAL.; Moving Past, and Beyond; Center Stage; Go with the Flow; Lane Legerdemain; Burning Spirit WIT; I Can See Right Through You; The Coast Is Clear!; Strategist; Crusader; Risky Business; Masterful Gambit; Sturm und Drang; Cut and Drive!; I See Victory in My Future!; Prideful King; A Princess Must Seize Victory!; Dancing in the Leaves; Calm in a Crowd; Unruffled; Fall Frenzy; Outer Post Proficiency ◯; Outer Post Proficiency ◎; Maverick ◯; Maverick ◎; Long Shot ◯; Long Shot ◎; Yodo Invicta; Competitive Spirit ◯; Competitive Spirit ◎; Target in Sight ◯; Target in Sight ◎; Inner Post Proficiency ◯; Inner Post Proficiency ◎; Lucky Seven; Super Lucky Seven

#### Sprint

173 skills ranked for this build, grouped by their **Team Trials** tier. The PvP rank of each skill is shown in its own column.

##### ◎ Top tier (Team Trials): 24 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| [Run Style] Corners ◯ | ◎ | ⍟ | 3.85 | 130 | [Run Style] | Cheap and consistent, they are must-haves |
| [Run Style] Straightaways ◯ | ◎ | ⍟ | 3.85 | 130 | [Run Style] | Cheap and consistent, they are must-haves |
| [Distance] Corners ◯ | ◎ | ⍟ | 5 | 100 | [Distance] | Cheap and consistent, they are must-haves |
| [Distance] Straightaways ◯ | ◎ | ⍟ | 5 | 100 | [Distance] | Cheap and consistent, they are must-haves |
| Uma Stan | ◎ | ◎ | 3.12 | 160 | / | Best speed skill on longer tracks for non-Front-Runners, can help to release PDM on some longer tracks |
| Super Stan | ◎ | ◎ | 3.75 | 160+160 | / | Best speed skill on longer tracks for non-Front-Runners, can help to release PDM on some longer tracks |
| Tail Held High | ◎ | ◎ | 5 | 100 | / | Cheap and consistent, though note the condition of requiring 3 skill activations before acquiring it |
| Slipstream | ◎ | ◎ | 3.12 | 160 | / | Consistent and facilitates overtaking when activated |
| Playtime's Over! | ◎ | ◎ | 3.12 | 160 | / | Consistent and improves Uma's capacity to maintain her placement |
| Burning Spirit GUTS | ◎ | ◎ | 3 | 200+200 | / | Good random Late-Race accel but in the game's current state,<br>this skill's effect is likely 80% (when Total Guts ≤ 1200) or 90% (when 1200 < Total Guts ≤ 1600) |
| Corner Recovery ◯ | ◎ | ◎ | 2.94 | 170 | / | Consistent and effective recovery |
| Swinging Maestro | ◎ | ◎ | 3.53 | 170+170 | / | Consistent and effective recovery |
| Ignited Spirit PWR | ◎ | ◎ | 2.5 | 200 | / | It's like a weaker but universal Slick Surge/On Your Left! |
| Burning Spirit PWR | ◎ | ◎ | 3 | 200+200 | / | It's like a weaker but universal Slick Surge/On Your Left! |
| Focus | ◎ | ▲ | 3.57 | 140 | / | Only take for Front Runners, Focus reduces the chance of a Late Start, while Concentration makes it impossible<br>You also get score for "strong starts" in Team Trials, so Concentration is always good there |
| Concentration | ◎ | ▲ | 4.29 | 140+140 | / | Only take for Front Runners, Focus reduces the chance of a Late Start, while Concentration makes it impossible<br>You also get score for "strong starts" in Team Trials, so Concentration is always good there |
| Hesitant [Run Style]s | ◎ | ◎ | 3.85 | 130 | / | Random Point in Late-Race |
| Subdued [Run Style]s | ◎ | ◎ | 3.85 | 130 | / | Random Point in Early-Race, ≥5 after Race Start |
| Flustered [Run Style]s | ◎ | ◎ | 3.85 | 130 | / | Random Point in Mid-Race |
| Trick (Front) | ◎ | ◎ | 3.57 | 140 | / | First Half of the Pack, ≥1 "Rushed" Uma behind |
| Tantalizing Trick | ◎ | ◎ | 4.29 | 140+140 | / | First Half of the Pack, ≥1 "Rushed" Uma behind |
| Trick (Rear) | ◎ | ◎ | 3.57 | 140 | / | 2nd-9th/12th Place, ≥1 "Rushed" Uma ahead |
| Lone Wolf | ◎ | ◎ | 7.14 | 70 | / | Easy to proc, you either benefit (you proc) or make it even (you prevent someone else's from proc'ing) |
| [Run Style] Savvy ◯ | ◎ | ◯ | 4.55 | 110 | [Run Style] | Consistent activation, FoV buff is useful for Nice Nature's All-Seeing Eyes |

##### ◯ Good (Team Trials): 12 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| Professor of Curvature | ◯ | ◯ | 3.33 | 180+180 | / | Consistent, but expensive<br>Rare ver. has greater speed boost making it more worth to acquire |
| Beeline Burst | ◯ | ◯ | 3.53 | 170+170 | / | Consistent |
| It's On! | ◯ | ◯ | 3.53 | 170+170 | / | Consistent. Even better when used in tandem with Tail Held High, Slipstream, and Playtime's Over! |
| In Body and Mind | ◯ | ◯ | 3.53 | 170+170 | / | Useful and (fairly) consistent Last Spurt speed boost, falls short of ◎ because it could activate at the very end of a race |
| Ignited Spirit GUTS | ◯ | ◎ | 2.5 | 200 | / | Good random Late-Race accel but in the game's current state,<br>this skill's effect is likely 80% (when Total Guts ≤ 1200) or 90% (when 1200 < Total Guts ≤ 1600) |
| Nimble Navigator | ◯ | ◎ | 3.33 | 150 | / | Strong accel but rng-dependent |
| No Stopping Me! | ◯ | ◎ | 4 | 150+150 | / | Strong accel but rng-dependent |
| Frenzied [Run Style]s | ◯ | ◎ | 3.85 | 130 | / | [Run Style] is "Rushed" |
| [Rotation]-Handed ◯ | ◯ | ◎ | 5.56 | 90 | / | Speed stat increase is significant |
| [Season] Runner ◯ | ◯ | ◎ | 5.56 | 90 | / | Speed stat increase is significant |
| Standard Distance ◯ | ◯ | ◎ | 5.56 | 90 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Non-Standard Distance ◯ | ◯ | ◎ | 5.56 | 90 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |

##### ▲ Situational (Team Trials): 8 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| Gap Closer | ▲ | ▲ | 3.12 | 160 | Sprint | Decent for Sprint Late Surgers/End Closers (only King Halo for now) |
| Blinding Flash | ▲ | ▲ | 3.75 | 160+160 | Sprint | Decent for Sprint Late Surgers/End Closers (only King Halo for now) |
| Wait-and-See | ▲ | ✕ | 3.12 | 160 | Sprint | Only for Late Surgers/End Closers (only King Halo for now), the extra acceleration effect is useless |
| Red Shift/LP1211-M | ▲ | ✕ | 2.5 | 200 | / | Powerful accel for Fronts/Paces, especially on tracks where Last Spurt Mode begins slightly before or on the Final Corner |
| Shooting for Victory! | ▲ | ◎ | 2.5 | 200 | / | Powerful accel for Paces/Lates, especially on tracks where Last Spurt Mode begins slightly before or on the Second Half of the Final Corner |
| Let's Pump Some Iron! | ▲ | ◎ | 2.5 | 200 | / | Strongest but most inconsistent accel for Lates/Ends on tracks where Last Spurt Mode begins slightly before or on the Final Corner |
| Angling and Scheming | ▲ | ◎ | 2.5 | 200 | / | Strongest accel for Fronts on tracks where Last Spurt Mode begins on a Corner |
| Condor's Fury | ▲ | ✕ | 2.5 | 200 | / | Powerful accel for Lates/Ends, especially on tracks where Last Spurt Mode begins slightly before or on the Final Corner |

##### △ Low priority (Team Trials): 91 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| [Run Style] Corners ◎ | △ | ⍟ | 1.85 | 130+140 | [Run Style] | Cheap and consistent, they are must-haves |
| [Run Style] Straightaways ◎ | △ | ⍟ | 1.85 | 130+140 | [Run Style] | Cheap and consistent, they are must-haves |
| [Distance] Corners ◎ | △ | ⍟ | 2.38 | 100+110 | [Distance] | Cheap and consistent, they are must-haves |
| [Distance] Straightaways ◎ | △ | ⍟ | 2.38 | 100+110 | [Distance] | Cheap and consistent, they are must-haves |
| Corner Adept ◯ | △ | △ | 2.78 | 180 | / | Consistent, but expensive<br>Rare ver. has greater speed boost making it more worth to acquire |
| Straightaway Adept | △ | △ | 2.94 | 170 | / | Consistent |
| Ramp Up | △ | △ | 2.94 | 170 | / | Consistent. Even better when used in tandem with Tail Held High, Slipstream, and Playtime's Over! |
| Homestretch Haste | △ | △ | 2.94 | 170 | / | Useful and (fairly) consistent Last Spurt speed boost, falls short of ◎ because it could activate at the very end of a race |
| Ignited Spirit SPD | △ | △ | 2.5 | 200 | / | 1.8s isn't very long and it costs 200 base SP |
| Burning Spirit SPD | △ | △ | 3 | 200+200 | / | 1.8s isn't very long and it costs 200 base SP |
| Certain Victory | △ | ◎ | 2.5 | 200 | / | Identical to OG Teio's unique with slightly looser conditions |
| Legacy of the Strong | △ | △ | 2.5 | 200 | / | Effects aren't bad but inconsistent activation |
| Shooting Star | △ | ◯ | 2.5 | 200 | / | Consistent activation, but weak effect |
| The View from the Lead is Mine! | △ | △ | 2.5 | 200 | / | Somewhat consistent activation for Front Runners, but weak effect |
| Sky-High Teio Step | △ | ◎ | 2.5 | 200 | / | Mostly consistent for non-Front-Runners, with strong effect |
| Triumphant Pulse | △ | ◎ | 2.5 | 200 | / | Consistent for non-Front-Runners, with strong effect |
| Anchors Aweigh! | △ | ✕ | 2.5 | 200 | / | Consistent for Late Surgers/End Closers but minimal effect |
| Resplendent Red Ace | △ | ▲ | 2.5 | 200 | / | Accel can come in handy occasionally but still very situational and slightly unreliable |
| Where There's a Will, There's a Way | △ | △ | 2.5 | 200 | / | Decent speed skill option for non-Front-Runners |
| The Duty of Dignity Calls | △ | ◯ | 2.5 | 200 | / | Final Corner Target Speed boost is inconsistent (especially in Med race), but it can be situationally good for Front Runners/Pace Chasers |
| Victoria por plancha ☆ | △ | ◎ | 2.5 | 200 | / | Activation is mostly consistent, some tracks benefit from a Last Straight accel |
| This Dance Is for Vittoria! | △ | ◯ | 2.5 | 200 | / | Fairly consistent activation but Final Corner Target Speed boost could be inconsistent |
| Behold Thine Emperor's Divine Might | △ | ◎ | 2.5 | 200 | / | Consistent for non-Front-Runners, with strong effect |
| Blazing Pride | △ | ◯ | 2.5 | 200 | / | Final Corner Target Speed boost is inconsistent (especially in Med race), but it can be situationally good for Late Surgers |
| ∴win Q.E.D. | △ | ◯ | 2.5 | 200 | / | Final Corner Target Speed boost is inconsistent (especially in Med race), but it can be situationally good for Front Runners |
| Flashy☆Landing | △ | ◯ | 2.5 | 200 | / | Acceleration on and beyond Final Corner is decent, conditions to activate may not be consistent unless you're Front Runner or Pace Chaser |
| Blue Rose Closer | △ | △ | 2.5 | 200 | / | Consistent, but weak effect |
| Our Ticket to Win! | △ | △ | 2.5 | 200 | / | Side block on Last Straight is rare, weak effect as well makes it not worth getting |
| Just a Little Farther! | △ | ✕ | 2.5 | 200 | / | Fairly consistent, but also weak |
| #LookatCurren | △ | △ | 2.5 | 200 | / | Slightly consistent but effect is really weak since it usually activates at Mid-Race |
| Nemesis | △ | ◯ | 2.5 | 200 | / | Consistent for Late Surgers/End Closers but effect is weak |
| SPARKLY☆STARDOM | △ | ▲ | 2.5 | 200 | / | Mostly consistent for most Front Runners and helps them maintain their lead |
| Shadow Break | △ | ◯ | 2.5 | 200 | / | Should be consistent but effect isn't great enough to be used over other similar uniques |
| Eternal Moments | △ | △ | 2.5 | 200 | / | Fairly consistent for non-Front-Runners, but the effect is weak |
| Flowery☆Maneuver | △ | ▲ | 2.5 | 200 | / | ① Strong for Front/Pace on some tracks to carry over speed on final corner<br>② Strong for Late/End on tracks that start the Last Spurt on final corner |
| You and Me! One-on-One! | △ | △ | 2.5 | 200 | / | Decent Last Straight speed skill for Late Surgers or End Closers |
| Lights of Vaudeville | △ | ◯ | 2.5 | 200 | / | Consistent activation but effectiveness depends on track |
| A Kiss for Courage | △ | △ | 2.5 | 200 | / | Varying effectiveness depending on track but can be strong with Triple 7s activation |
| I Never Goof Up! | △ | ◯ | 2.5 | 200 | / | Good effect but rng and track dependent |
| Bountiful Harvest | △ | △ | 2.5 | 200 | / | Consistent but relatively weak |
| YUMMY☆SPEED! | △ | ✕ | 2.5 | 200 | / | Unfortunate timing at 60% of the Race makes this skill's acceleration practically useless |
| OMG! (ﾟ∀ﾟ) The Final Sprint! ☆ | △ | △ | 2.5 | 200 | / | Generally, when you overtake in Late-Race, you're still accelerating, so a Target Speed skill wouldn't be effective |
| Give Mummy a Hug ♡ | △ | ◯ | 2.5 | 200 | / | Good accel for tracks that have their Last Spurt Mode begin on/near a Last Straight |
| Chasing After You | △ | △ | 2.5 | 200 | / | Very weak effect but can be used as a debuff |
| Arrows Whistle, Shadows Disperse | △ | ◯ | 2.5 | 200 | / | Consistent, but weak effect |
| Pop & Polish | △ | ◯ | 2.5 | 200 | / | Consistent, but weak effect |
| Presents from X | △ | △ | 2.5 | 200 | / | Consistent, but weak effect |
| Festive Miracle | △ | ◯ | 2.5 | 200 | / | Strong on some tracks where Triple 7s can proc before the Last Spurt |
| Fairy Tale | △ | △ | 2.5 | 200 | / | Strong on some tracks where Triple 7s can proc before the Last Spurt |
| Straightaway Recovery | △ | △ | 2.94 | 170 | / | Inconsistent, it might be wasted on an early or late activation |
| Breath of Fresh Air | △ | △ | 3.53 | 170+170 | / | Inconsistent, it might be wasted on an early or late activation |
| Lay Low | △ | ✕ | 3.12 | 160 | / | Might proc in Early-Race which might overflow HP |
| Iron Will | △ | ✕ | 3.75 | 160+160 | / | Might proc in Early-Race which might overflow HP |
| Pace Strategy | △ | ✕ | 2.94 | 170 | / | Being overtaken is an inconsistent condition<br>More suitable on long, backline Run Styles |
| Indomitable | △ | ✕ | 3.53 | 170+170 | / | Being overtaken is an inconsistent condition<br>More suitable on long, backline Run Styles |
| Triple 7s | △ | ▲ | 3.12 | 160 | / | Consistent, but only effective on <2400m tracks, useful for some Uma that rely on Stamina skill procs |
| Shake It Out | △ | ✕ | 5 | 100 | / | Late-Race recovery is ineffective<br>consider acquiring it only for Team Trials because it's very cheap |
| Ignited Spirit STA | △ | △ | 2.5 | 200 | / | Definitely an option but it costs more than a usual skill (at 200 base SP) |
| Burning Spirit STA | △ | △ | 3 | 200+200 | / | Definitely an option but it costs more than a usual skill (at 200 base SP) |
| U=ma2 | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Pure Heart | △ | △ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Super-Duper Climax | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Superior Heal | △ | △ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Dazzl'n ♪ Diver | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Every Rose Has Its Fangs | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Corner Acceleration ◯ | △ | ✕ | 2.78 | 180 | / | Acceleration on the Corner 1/First Corner of any track is useless |
| Corner Connoisseur | △ | ✕ | 3.33 | 180+180 | / | Acceleration on the Corner 1/First Corner of any track is useless |
| Straightaway Acceleration | △ | ✕ | 2.94 | 170 | / | Random straight activations are too inconsistent to be effective |
| Rushing Gale! | △ | ✕ | 3.53 | 170+170 | / | Random straight activations are too inconsistent to be effective |
| Highlander | △ | ◎ | 3.12 | 160 | / | Very powerful on tracks with Uphills right before/as Last Spurt Mode begins |
| Groundwork | △ | ▲ | 5 | 100 | / | For Front Runners only, use with 3 Early-Race skills like Focus/Concentration+Green Skills |
| Sprinting Gear | △ | ✕ | 3.12 | 160 | Sprint | Random straight activations are almost always useless |
| Turbo Sprint | △ | ✕ | 3.75 | 160+160 | Sprint | Random straight activations are almost always useless |
| Countermeasure | △ | ✕ | 3.12 | 160 | Sprint | Gamble accel, if it procs right before Mid-Race ends it'll be effective |
| Plan X | △ | ✕ | 3.75 | 160+160 | Sprint | Gamble accel, if it procs right before Mid-Race ends it'll be effective |
| KEEP IT REAL. | △ | ✕ | 2.5 | 200 | / | Mostly useless accel but consistent activation |
| Moving Past, and Beyond | △ | ✕ | 2.5 | 200 | / | Mostly useless accel but consistent activation |
| Prudent Positioning | △ | ▲ | 4.17 | 120 | / | Use with Dodging Danger for a very powerful Early-Race burst of speed (Front Runner only) |
| Center Stage | △ | ✕ | 5 | 120+120 | / | Never use for Front-Runners that want to run the Dodging Danger tech |
| Go with the Flow | △ | ✕ | 4.17 | 120 | / | Random non-Early-Race Lane Movement Speed for non-Front-Runners are useless<br>Take only because they are very cheap and if you have no other options |
| Lane Legerdemain | △ | ✕ | 5 | 120+120 | / | Random non-Early-Race Lane Movement Speed for non-Front-Runners are useless<br>Take only because they are very cheap and if you have no other options |
| Ignited Spirit WIT | △ | ▲ | 2.5 | 200 | / | Use with Dodging Danger for a very powerful Early-Race burst of speed (Front Runner only) |
| Burning Spirit WIT | △ | ✕ | 3 | 200+200 | / | Never use for Front-Runners that want to run the Dodging Danger tech |
| Meticulous Measures | △ | ✕ | 3.57 | 140 | Sprint | Random non-Early-Race Lane Movement Speed for non-Front-Runners are useless<br>There is no need for any additional acceleration (unless it's toward the very end which is very RNG-dependent)<br>Take only because they are very cheap and if you have no other options |
| Perfect Prep! | △ | ✕ | 4.29 | 140+140 | Sprint | Random non-Early-Race Lane Movement Speed for non-Front-Runners are useless<br>There is no need for any additional acceleration (unless it's toward the very end which is very RNG-dependent)<br>Take only because they are very cheap and if you have no other options |
| Intimidate | △ | ✕ | 2.94 | 170 | Sprint | First Half of the Pack, at Random Point in Early-Race, ≥5s after Race Start |
| Adored by All | △ | ✕ | 3.53 | 170+170 | Sprint | First Half of the Pack, at Random Point in Early-Race, ≥5s after Race Start |
| [Location] Racecourse ◯ | △ | ◎ | 5.56 | 90 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| [Ground Condition] Conditions ◯ | △ | ◎ | 5.56 | 90 | / | Power Stat increase is decent but low priority |
| [Weather] Days ◯ | △ | △ | 5.56 | 90 | / | Guts is extremely unimportant, only take it you really need to |
| [Run Style] Savvy ◎ | △ | ▲ | 2.08 | 110+130 | [Run Style] | Consistent activation, FoV buff is useful for Nice Nature's All-Seeing Eyes |

##### ✕ Avoid (Team Trials): 38 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| Risky Business | ✕ | ✕ | 4.17 | 120 | / | This skill can completely kill your stamina, it's definitely not worth it unless you're trying to do some niche strat |
| Huge Lead | ✕ | ✕ | 2.94 | 170 | Sprint | 12.5m lead is highly unfeasible, this skill will almost never activate |
| Staggering Lead | ✕ | ✕ | 3.53 | 170+170 | Sprint | 12.5m lead is highly unfeasible, this skill will almost never activate |
| Cut and Drive! | ✕ | ✕ | 2.5 | 200 | / | Not the most consistent, and also a weak effect, not worth taking |
| G00 1st. F∞; | ✕ | △ | 2.5 | 200 | / | 0.15m/s but has two additional checks (for Start Delay and Rushed) |
| Genius x Bakushin = Victory | ✕ | △ | 2.5 | 200 | / | Fairly consistent, but also weak |
| I See Victory in My Future! | ✕ | ✕ | 2.5 | 200 | / | Front Block condition is downright horrible |
| Prideful King | ✕ | ✕ | 2.5 | 200 | / | Extremely inconsistent, if not totally impossible to even activate in any distance but Sprint |
| Schwarzes Schwert | ✕ | △ | 2.5 | 200 | / | 0.15m/s but requires two additional checks (for Start Delay and Rushed) |
| A Princess Must Seize Victory! | ✕ | ✕ | 2.5 | 200 | / | Side block condition on the Last Straight is quite strict and difficult to proc |
| Dancing in the Leaves | ✕ | ✕ | 2.5 | 200 | / | Side Block isn't consistent, effect isn't outstanding either |
| Calm in a Crowd | ✕ | ✕ | 2.94 | 170 | / | Almost impossible to be boxed in on all sides in CM |
| Unruffled | ✕ | ✕ | 3.53 | 170+170 | / | Almost impossible to be boxed in on all sides in CM |
| Stop Right There! | ✕ | ✕ | 2.94 | 170 | Sprint | Last Half of the Pack, at Random Point during Early-Race, ≥5s after Race Start |
| [Rotation]-Handed ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Speed stat increase is significant |
| [Season] Runner ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Speed stat increase is significant |
| Fall Frenzy | ✕ | ✕ | 3.64 | 90+110+130 | / | Take only on Autumn CMs |
| Outer Post Proficiency ◯ | ✕ | ✕ | 5.56 | 90 | / | Post Numbers 6-8 is inconsistent |
| Outer Post Proficiency ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Post Numbers 6-8 is inconsistent |
| Maverick ◯ | ✕ | ✕ | 5.56 | 90 | / | Very rare to have no Umas use your run style |
| Maverick ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Very rare to have no Umas use your run style |
| Long Shot ◯ | ✕ | ✕ | 5.56 | 90 | / | Popularity-dependent skills are inconsistent |
| Long Shot ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Popularity-dependent skills are inconsistent |
| Sympathy | ✕ | ▲ | 7.14 | 70 | / | Practically impossible to proc |
| [Location] Racecourse ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Yodo Invicta | ✕ | ✕ | 3.64 | 90+110+130 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Standard Distance ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Non-Standard Distance ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| [Ground Condition] Conditions ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Power Stat increase is decent but low priority |
| Competitive Spirit ◯ | ✕ | ✕ | 5.56 | 90 | / | It's unlikely for 40% of the lobby to use the same run style as you |
| Competitive Spirit ◎ | ✕ | ✕ | 2.5 | 90+110 | / | It's unlikely for 40% of the lobby to use the same run style as you |
| [Weather] Days ◎ | ✕ | △ | 2.5 | 90+110 | / | Guts is extremely unimportant, only take it you really need to |
| Target in Sight ◯ | ✕ | ✕ | 5.56 | 90 | / | Guts is extremely unimportant, only take it you really need to |
| Target in Sight ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Guts is extremely unimportant, only take it you really need to |
| Inner Post Proficiency ◯ | ✕ | ✕ | 5.56 | 90 | / | Post Numbers 1-3 is inconsistent |
| Inner Post Proficiency ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Post Numbers 1-3 is inconsistent |
| Lucky Seven | ✕ | ✕ | 4.55 | 110 | / | Inconsistent, even more so than the Post Proficiency skills |
| Super Lucky Seven | ✕ | ✕ | 5.45 | 110+110 | / | Inconsistent, even more so than the Post Proficiency skills |

##### Quick view: skills grouped by PvP tier

- **⍟ Essential (8):** [Run Style] Corners ◯; [Run Style] Straightaways ◯; [Distance] Corners ◯; [Distance] Straightaways ◯; [Run Style] Corners ◎; [Run Style] Straightaways ◎; [Distance] Corners ◎; [Distance] Straightaways ◎
- **◎ Top tier (42):** Uma Stan; Super Stan; Tail Held High; Slipstream; Playtime's Over!; Burning Spirit GUTS; Corner Recovery ◯; Swinging Maestro; Ignited Spirit PWR; Burning Spirit PWR; Hesitant [Run Style]s; Subdued [Run Style]s; Flustered [Run Style]s; Trick (Front); Tantalizing Trick; Trick (Rear); Lone Wolf; Ignited Spirit GUTS; Nimble Navigator; No Stopping Me!; Frenzied [Run Style]s; [Rotation]-Handed ◯; [Season] Runner ◯; Standard Distance ◯; Non-Standard Distance ◯; Shooting for Victory!; Let's Pump Some Iron!; Angling and Scheming; Certain Victory; Sky-High Teio Step; Triumphant Pulse; Victoria por plancha ☆; Behold Thine Emperor's Divine Might; Highlander; [Location] Racecourse ◯; [Ground Condition] Conditions ◯; [Rotation]-Handed ◎; [Season] Runner ◎; [Location] Racecourse ◎; Standard Distance ◎; Non-Standard Distance ◎; [Ground Condition] Conditions ◎
- **◯ Good (19):** [Run Style] Savvy ◯; Professor of Curvature; Beeline Burst; It's On!; In Body and Mind; Shooting Star; The Duty of Dignity Calls; This Dance Is for Vittoria!; Blazing Pride; ∴win Q.E.D.; Flashy☆Landing; Nemesis; Shadow Break; Lights of Vaudeville; I Never Goof Up!; Give Mummy a Hug ♡; Arrows Whistle, Shadows Disperse; Pop & Polish; Festive Miracle
- **▲ Situational (13):** Focus; Concentration; Gap Closer; Blinding Flash; Resplendent Red Ace; SPARKLY☆STARDOM; Flowery☆Maneuver; Triple 7s; Groundwork; Prudent Positioning; Ignited Spirit WIT; [Run Style] Savvy ◎; Sympathy
- **△ Low priority (31):** Corner Adept ◯; Straightaway Adept; Ramp Up; Homestretch Haste; Ignited Spirit SPD; Burning Spirit SPD; Legacy of the Strong; The View from the Lead is Mine!; Where There's a Will, There's a Way; Blue Rose Closer; Our Ticket to Win!; #LookatCurren; Eternal Moments; You and Me! One-on-One!; A Kiss for Courage; Bountiful Harvest; OMG! (ﾟ∀ﾟ) The Final Sprint! ☆; Chasing After You; Presents from X; Fairy Tale; Straightaway Recovery; Breath of Fresh Air; Ignited Spirit STA; Burning Spirit STA; Pure Heart; Superior Heal; [Weather] Days ◯; G00 1st. F∞;; Genius x Bakushin = Victory; Schwarzes Schwert; [Weather] Days ◎
- **✕ Avoid (60):** Wait-and-See; Red Shift/LP1211-M; Condor's Fury; Anchors Aweigh!; Just a Little Farther!; YUMMY☆SPEED!; Lay Low; Iron Will; Pace Strategy; Indomitable; Shake It Out; U=ma2; Super-Duper Climax; Dazzl'n ♪ Diver; Every Rose Has Its Fangs; Corner Acceleration ◯; Corner Connoisseur; Straightaway Acceleration; Rushing Gale!; Sprinting Gear; Turbo Sprint; Countermeasure; Plan X; KEEP IT REAL.; Moving Past, and Beyond; Center Stage; Go with the Flow; Lane Legerdemain; Burning Spirit WIT; Meticulous Measures; Perfect Prep!; Intimidate; Adored by All; Risky Business; Huge Lead; Staggering Lead; Cut and Drive!; I See Victory in My Future!; Prideful King; A Princess Must Seize Victory!; Dancing in the Leaves; Calm in a Crowd; Unruffled; Stop Right There!; Fall Frenzy; Outer Post Proficiency ◯; Outer Post Proficiency ◎; Maverick ◯; Maverick ◎; Long Shot ◯; Long Shot ◎; Yodo Invicta; Competitive Spirit ◯; Competitive Spirit ◎; Target in Sight ◯; Target in Sight ◎; Inner Post Proficiency ◯; Inner Post Proficiency ◎; Lucky Seven; Super Lucky Seven

#### Mile

174 skills ranked for this build, grouped by their **Team Trials** tier. The PvP rank of each skill is shown in its own column.

##### ◎ Top tier (Team Trials): 27 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| [Run Style] Corners ◯ | ◎ | ⍟ | 3.85 | 130 | [Run Style] | Cheap and consistent, they are must-haves |
| [Run Style] Straightaways ◯ | ◎ | ⍟ | 3.85 | 130 | [Run Style] | Cheap and consistent, they are must-haves |
| [Distance] Corners ◯ | ◎ | ⍟ | 5 | 100 | [Distance] | Cheap and consistent, they are must-haves |
| [Distance] Straightaways ◯ | ◎ | ⍟ | 5 | 100 | [Distance] | Cheap and consistent, they are must-haves |
| Uma Stan | ◎ | ◎ | 3.12 | 160 | / | Best speed skill on longer tracks for non-Front-Runners, can help to release PDM on some longer tracks |
| Super Stan | ◎ | ◎ | 3.75 | 160+160 | / | Best speed skill on longer tracks for non-Front-Runners, can help to release PDM on some longer tracks |
| Tail Held High | ◎ | ◎ | 5 | 100 | / | Cheap and consistent, though note the condition of requiring 3 skill activations before acquiring it |
| Slipstream | ◎ | ◎ | 3.12 | 160 | / | Consistent and facilitates overtaking when activated |
| Playtime's Over! | ◎ | ◎ | 3.12 | 160 | / | Consistent and improves Uma's capacity to maintain her placement |
| Burning Spirit GUTS | ◎ | ◎ | 3 | 200+200 | / | Good random Late-Race accel but in the game's current state,<br>this skill's effect is likely 80% (when Total Guts ≤ 1200) or 90% (when 1200 < Total Guts ≤ 1600) |
| Mile Maven | ◎ | ✕ | 3.75 | 160+160 | Mile | Mostly consistent but activation occurs during Early-Race where Uma may not have hit top speed, making target speed boosts obsolete (doesn't actually increase speed<br>since Uma's Current Speed hasn't reached Target Speed). Additionally, the skill may pick a point prior to the 5 seconds needed after the race starts to activate, making it proc inconsistently too |
| Unyielding Spirit | ◎ | ✕ | 4.17 | 120 | Mile | Cheap and consistent |
| Big-Sisterly | ◎ | ✕ | 5 | 120+120 | Mile | Cheap and consistent |
| Corner Recovery ◯ | ◎ | ◎ | 2.94 | 170 | / | Consistent and effective recovery |
| Swinging Maestro | ◎ | ◎ | 3.53 | 170+170 | / | Consistent and effective recovery |
| Ignited Spirit PWR | ◎ | ◎ | 2.5 | 200 | / | It's like a weaker but universal Slick Surge/On Your Left! |
| Burning Spirit PWR | ◎ | ◎ | 3 | 200+200 | / | It's like a weaker but universal Slick Surge/On Your Left! |
| Focus | ◎ | ▲ | 3.57 | 140 | / | Only take for Front Runners, Focus reduces the chance of a Late Start, while Concentration makes it impossible<br>You also get score for "strong starts" in Team Trials, so Concentration is always good there |
| Concentration | ◎ | ▲ | 4.29 | 140+140 | / | Only take for Front Runners, Focus reduces the chance of a Late Start, while Concentration makes it impossible<br>You also get score for "strong starts" in Team Trials, so Concentration is always good there |
| Hesitant [Run Style]s | ◎ | ◎ | 3.85 | 130 | / | Random Point in Late-Race |
| Subdued [Run Style]s | ◎ | ◎ | 3.85 | 130 | / | Random Point in Early-Race, ≥5 after Race Start |
| Flustered [Run Style]s | ◎ | ◎ | 3.85 | 130 | / | Random Point in Mid-Race |
| Trick (Front) | ◎ | ◎ | 3.57 | 140 | / | First Half of the Pack, ≥1 "Rushed" Uma behind |
| Tantalizing Trick | ◎ | ◎ | 4.29 | 140+140 | / | First Half of the Pack, ≥1 "Rushed" Uma behind |
| Trick (Rear) | ◎ | ◎ | 3.57 | 140 | / | 2nd-9th/12th Place, ≥1 "Rushed" Uma ahead |
| Lone Wolf | ◎ | ◎ | 7.14 | 70 | / | Easy to proc, you either benefit (you proc) or make it even (you prevent someone else's from proc'ing) |
| [Run Style] Savvy ◯ | ◎ | ◯ | 4.55 | 110 | [Run Style] | Consistent activation, FoV buff is useful for Nice Nature's All-Seeing Eyes |

##### ◯ Good (Team Trials): 17 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| Professor of Curvature | ◯ | ◯ | 3.33 | 180+180 | / | Consistent, but expensive<br>Rare ver. has greater speed boost making it more worth to acquire |
| Beeline Burst | ◯ | ◯ | 3.53 | 170+170 | / | Consistent |
| It's On! | ◯ | ◯ | 3.53 | 170+170 | / | Consistent. Even better when used in tandem with Tail Held High, Slipstream, and Playtime's Over! |
| In Body and Mind | ◯ | ◯ | 3.53 | 170+170 | / | Useful and (fairly) consistent Last Spurt speed boost, falls short of ◎ because it could activate at the very end of a race |
| Ignited Spirit GUTS | ◯ | ◎ | 2.5 | 200 | / | Good random Late-Race accel but in the game's current state,<br>this skill's effect is likely 80% (when Total Guts ≤ 1200) or 90% (when 1200 < Total Guts ≤ 1600) |
| Productive Plan | ◯ | ✕ | 3.12 | 160 | Mile | Mostly consistent but activation occurs during Early-Race where Uma may not have hit top speed, making target speed boosts obsolete (doesn't actually increase speed<br>since Uma's Current Speed hasn't reached Target Speed). Additionally, the skill may pick a point prior to the 5 seconds needed after the race starts to activate, making it proc inconsistently too |
| Shifting Gears | ◯ | ✕ | 3.12 | 160 | Mile | Consistent |
| Changing Gears | ◯ | ✕ | 3.75 | 160+160 | Mile | Consistent |
| Nimble Navigator | ◯ | ◎ | 3.33 | 150 | / | Strong accel but rng-dependent |
| No Stopping Me! | ◯ | ◎ | 4 | 150+150 | / | Strong accel but rng-dependent |
| Updrafters | ◯ | ✕ | 3.12 | 160 | Mile | Good but inconsistently effective accel for Lates/Ends in Mile |
| Furious Feat | ◯ | ✕ | 3.75 | 160+160 | Mile | Good but inconsistently effective accel for Lates/Ends in Mile |
| Frenzied [Run Style]s | ◯ | ◎ | 3.85 | 130 | / | [Run Style] is "Rushed" |
| [Rotation]-Handed ◯ | ◯ | ◎ | 5.56 | 90 | / | Speed stat increase is significant |
| [Season] Runner ◯ | ◯ | ◎ | 5.56 | 90 | / | Speed stat increase is significant |
| Standard Distance ◯ | ◯ | ◎ | 5.56 | 90 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Non-Standard Distance ◯ | ◯ | ◎ | 5.56 | 90 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |

##### ▲ Situational (Team Trials): 7 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| Watchful Eye | ▲ | ✕ | 3.12 | 160 | Mile | Most effective Mile debuff skill, must-have for all Mile debuffers |
| Keen Eye | ▲ | ✕ | 3.75 | 160+160 | Mile | Most effective Mile debuff skill, must-have for all Mile debuffers |
| Red Shift/LP1211-M | ▲ | ✕ | 2.5 | 200 | / | Powerful accel for Fronts/Paces, especially on tracks where Last Spurt Mode begins slightly before or on the Final Corner |
| Shooting for Victory! | ▲ | ◎ | 2.5 | 200 | / | Powerful accel for Paces/Lates, especially on tracks where Last Spurt Mode begins slightly before or on the Second Half of the Final Corner |
| Let's Pump Some Iron! | ▲ | ◎ | 2.5 | 200 | / | Strongest but most inconsistent accel for Lates/Ends on tracks where Last Spurt Mode begins slightly before or on the Final Corner |
| Angling and Scheming | ▲ | ◎ | 2.5 | 200 | / | Strongest accel for Fronts on tracks where Last Spurt Mode begins on a Corner |
| Condor's Fury | ▲ | ✕ | 2.5 | 200 | / | Powerful accel for Lates/Ends, especially on tracks where Last Spurt Mode begins slightly before or on the Final Corner |

##### △ Low priority (Team Trials): 86 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| [Run Style] Corners ◎ | △ | ⍟ | 1.85 | 130+140 | [Run Style] | Cheap and consistent, they are must-haves |
| [Run Style] Straightaways ◎ | △ | ⍟ | 1.85 | 130+140 | [Run Style] | Cheap and consistent, they are must-haves |
| [Distance] Corners ◎ | △ | ⍟ | 2.38 | 100+110 | [Distance] | Cheap and consistent, they are must-haves |
| [Distance] Straightaways ◎ | △ | ⍟ | 2.38 | 100+110 | [Distance] | Cheap and consistent, they are must-haves |
| Corner Adept ◯ | △ | △ | 2.78 | 180 | / | Consistent, but expensive<br>Rare ver. has greater speed boost making it more worth to acquire |
| Straightaway Adept | △ | △ | 2.94 | 170 | / | Consistent |
| Ramp Up | △ | △ | 2.94 | 170 | / | Consistent. Even better when used in tandem with Tail Held High, Slipstream, and Playtime's Over! |
| Homestretch Haste | △ | △ | 2.94 | 170 | / | Useful and (fairly) consistent Last Spurt speed boost, falls short of ◎ because it could activate at the very end of a race |
| Ignited Spirit SPD | △ | △ | 2.5 | 200 | / | 1.8s isn't very long and it costs 200 base SP |
| Burning Spirit SPD | △ | △ | 3 | 200+200 | / | 1.8s isn't very long and it costs 200 base SP |
| Certain Victory | △ | ◎ | 2.5 | 200 | / | Identical to OG Teio's unique with slightly looser conditions |
| Legacy of the Strong | △ | △ | 2.5 | 200 | / | Effects aren't bad but inconsistent activation |
| Shooting Star | △ | ◯ | 2.5 | 200 | / | Consistent activation, but weak effect |
| The View from the Lead is Mine! | △ | △ | 2.5 | 200 | / | Somewhat consistent activation for Front Runners, but weak effect |
| Sky-High Teio Step | △ | ◎ | 2.5 | 200 | / | Mostly consistent for non-Front-Runners, with strong effect |
| Triumphant Pulse | △ | ◎ | 2.5 | 200 | / | Consistent for non-Front-Runners, with strong effect |
| Anchors Aweigh! | △ | ✕ | 2.5 | 200 | / | Consistent for Late Surgers/End Closers but minimal effect |
| Resplendent Red Ace | △ | ▲ | 2.5 | 200 | / | Accel can come in handy occasionally but still very situational and slightly unreliable |
| Where There's a Will, There's a Way | △ | △ | 2.5 | 200 | / | Decent speed skill option for non-Front-Runners |
| The Duty of Dignity Calls | △ | ◯ | 2.5 | 200 | / | Final Corner Target Speed boost is inconsistent (especially in Med race), but it can be situationally good for Front Runners/Pace Chasers |
| Victoria por plancha ☆ | △ | ◎ | 2.5 | 200 | / | Activation is mostly consistent, some tracks benefit from a Last Straight accel |
| This Dance Is for Vittoria! | △ | ◯ | 2.5 | 200 | / | Fairly consistent activation but Final Corner Target Speed boost could be inconsistent |
| Behold Thine Emperor's Divine Might | △ | ◎ | 2.5 | 200 | / | Consistent for non-Front-Runners, with strong effect |
| Blazing Pride | △ | ◯ | 2.5 | 200 | / | Final Corner Target Speed boost is inconsistent (especially in Med race), but it can be situationally good for Late Surgers |
| ∴win Q.E.D. | △ | ◯ | 2.5 | 200 | / | Final Corner Target Speed boost is inconsistent (especially in Med race), but it can be situationally good for Front Runners |
| Flashy☆Landing | △ | ◯ | 2.5 | 200 | / | Acceleration on and beyond Final Corner is decent, conditions to activate may not be consistent unless you're Front Runner or Pace Chaser |
| Blue Rose Closer | △ | △ | 2.5 | 200 | / | Consistent, but weak effect |
| Our Ticket to Win! | △ | △ | 2.5 | 200 | / | Side block on Last Straight is rare, weak effect as well makes it not worth getting |
| Just a Little Farther! | △ | ✕ | 2.5 | 200 | / | Fairly consistent, but also weak |
| #LookatCurren | △ | △ | 2.5 | 200 | / | Slightly consistent but effect is really weak since it usually activates at Mid-Race |
| Nemesis | △ | ◯ | 2.5 | 200 | / | Consistent for Late Surgers/End Closers but effect is weak |
| SPARKLY☆STARDOM | △ | ▲ | 2.5 | 200 | / | Mostly consistent for most Front Runners and helps them maintain their lead |
| Shadow Break | △ | ◯ | 2.5 | 200 | / | Should be consistent but effect isn't great enough to be used over other similar uniques |
| Eternal Moments | △ | △ | 2.5 | 200 | / | Fairly consistent for non-Front-Runners, but the effect is weak |
| Flowery☆Maneuver | △ | ▲ | 2.5 | 200 | / | ① Strong for Front/Pace on some tracks to carry over speed on final corner<br>② Strong for Late/End on tracks that start the Last Spurt on final corner |
| You and Me! One-on-One! | △ | △ | 2.5 | 200 | / | Decent Last Straight speed skill for Late Surgers or End Closers |
| Lights of Vaudeville | △ | ◯ | 2.5 | 200 | / | Consistent activation but effectiveness depends on track |
| A Kiss for Courage | △ | △ | 2.5 | 200 | / | Varying effectiveness depending on track but can be strong with Triple 7s activation |
| I Never Goof Up! | △ | ◯ | 2.5 | 200 | / | Good effect but rng and track dependent |
| Bountiful Harvest | △ | △ | 2.5 | 200 | / | Consistent but relatively weak |
| YUMMY☆SPEED! | △ | ✕ | 2.5 | 200 | / | Unfortunate timing at 60% of the Race makes this skill's acceleration practically useless |
| OMG! (ﾟ∀ﾟ) The Final Sprint! ☆ | △ | △ | 2.5 | 200 | / | Generally, when you overtake in Late-Race, you're still accelerating, so a Target Speed skill wouldn't be effective |
| Give Mummy a Hug ♡ | △ | ◯ | 2.5 | 200 | / | Good accel for tracks that have their Last Spurt Mode begin on/near a Last Straight |
| Chasing After You | △ | △ | 2.5 | 200 | / | Very weak effect but can be used as a debuff |
| Arrows Whistle, Shadows Disperse | △ | ◯ | 2.5 | 200 | / | Consistent, but weak effect |
| Pop & Polish | △ | ◯ | 2.5 | 200 | / | Consistent, but weak effect |
| Presents from X | △ | △ | 2.5 | 200 | / | Consistent, but weak effect |
| Festive Miracle | △ | ◯ | 2.5 | 200 | / | Strong on some tracks where Triple 7s can proc before the Last Spurt |
| Fairy Tale | △ | △ | 2.5 | 200 | / | Strong on some tracks where Triple 7s can proc before the Last Spurt |
| Straightaway Recovery | △ | △ | 2.94 | 170 | / | Inconsistent, it might be wasted on an early or late activation |
| Breath of Fresh Air | △ | △ | 3.53 | 170+170 | / | Inconsistent, it might be wasted on an early or late activation |
| Lay Low | △ | ✕ | 3.12 | 160 | / | Might proc in Early-Race which might overflow HP |
| Iron Will | △ | ✕ | 3.75 | 160+160 | / | Might proc in Early-Race which might overflow HP |
| Pace Strategy | △ | ✕ | 2.94 | 170 | / | Being overtaken is an inconsistent condition<br>More suitable on long, backline Run Styles |
| Indomitable | △ | ✕ | 3.53 | 170+170 | / | Being overtaken is an inconsistent condition<br>More suitable on long, backline Run Styles |
| Triple 7s | △ | ▲ | 3.12 | 160 | / | Consistent, but only effective on <2400m tracks, useful for some Uma that rely on Stamina skill procs |
| Shake It Out | △ | ✕ | 5 | 100 | / | Late-Race recovery is ineffective<br>consider acquiring it only for Team Trials because it's very cheap |
| Ignited Spirit STA | △ | △ | 2.5 | 200 | / | Definitely an option but it costs more than a usual skill (at 200 base SP) |
| Burning Spirit STA | △ | △ | 3 | 200+200 | / | Definitely an option but it costs more than a usual skill (at 200 base SP) |
| U=ma2 | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Pure Heart | △ | △ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Super-Duper Climax | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Superior Heal | △ | △ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Dazzl'n ♪ Diver | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Every Rose Has Its Fangs | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Corner Acceleration ◯ | △ | ✕ | 2.78 | 180 | / | Acceleration on the Corner 1/First Corner of any track is useless |
| Corner Connoisseur | △ | ✕ | 3.33 | 180+180 | / | Acceleration on the Corner 1/First Corner of any track is useless |
| Straightaway Acceleration | △ | ✕ | 2.94 | 170 | / | Random straight activations are too inconsistent to be effective |
| Rushing Gale! | △ | ✕ | 3.53 | 170+170 | / | Random straight activations are too inconsistent to be effective |
| Highlander | △ | ◎ | 3.12 | 160 | / | Very powerful on tracks with Uphills right before/as Last Spurt Mode begins |
| Groundwork | △ | ▲ | 5 | 100 | / | For Front Runners only, use with 3 Early-Race skills like Focus/Concentration+Green Skills |
| Acceleration | △ | ✕ | 3.12 | 160 | Mile | Fairly consistent but Mid-Race accel is useless |
| Step on the Gas! | △ | ✕ | 3.75 | 160+160 | Mile | Fairly consistent but Mid-Race accel is useless |
| KEEP IT REAL. | △ | ✕ | 2.5 | 200 | / | Mostly useless accel but consistent activation |
| Moving Past, and Beyond | △ | ✕ | 2.5 | 200 | / | Mostly useless accel but consistent activation |
| Prudent Positioning | △ | ▲ | 4.17 | 120 | / | Use with Dodging Danger for a very powerful Early-Race burst of speed (Front Runner only) |
| Center Stage | △ | ✕ | 5 | 120+120 | / | Never use for Front-Runners that want to run the Dodging Danger tech |
| Go with the Flow | △ | ✕ | 4.17 | 120 | / | Random non-Early-Race Lane Movement Speed for non-Front-Runners are useless<br>Take only because they are very cheap and if you have no other options |
| Lane Legerdemain | △ | ✕ | 5 | 120+120 | / | Random non-Early-Race Lane Movement Speed for non-Front-Runners are useless<br>Take only because they are very cheap and if you have no other options |
| Ignited Spirit WIT | △ | ▲ | 2.5 | 200 | / | Use with Dodging Danger for a very powerful Early-Race burst of speed (Front Runner only) |
| Burning Spirit WIT | △ | ✕ | 3 | 200+200 | / | Never use for Front-Runners that want to run the Dodging Danger tech |
| Speed Eater | △ | ✕ | 3.12 | 160 | Mile | 1st-3rd Place, at Random Point during Mid-Race |
| [Location] Racecourse ◯ | △ | ◎ | 5.56 | 90 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| [Ground Condition] Conditions ◯ | △ | ◎ | 5.56 | 90 | / | Power Stat increase is decent but low priority |
| [Weather] Days ◯ | △ | △ | 5.56 | 90 | / | Guts is extremely unimportant, only take it you really need to |
| [Run Style] Savvy ◎ | △ | ▲ | 2.08 | 110+130 | [Run Style] | Consistent activation, FoV buff is useful for Nice Nature's All-Seeing Eyes |

##### ✕ Avoid (Team Trials): 37 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| Risky Business | ✕ | ✕ | 4.17 | 120 | / | This skill can completely kill your stamina, it's definitely not worth it unless you're trying to do some niche strat |
| Cut and Drive! | ✕ | ✕ | 2.5 | 200 | / | Not the most consistent, and also a weak effect, not worth taking |
| G00 1st. F∞; | ✕ | △ | 2.5 | 200 | / | 0.15m/s but has two additional checks (for Start Delay and Rushed) |
| Genius x Bakushin = Victory | ✕ | △ | 2.5 | 200 | / | Fairly consistent, but also weak |
| I See Victory in My Future! | ✕ | ✕ | 2.5 | 200 | / | Front Block condition is downright horrible |
| Prideful King | ✕ | ✕ | 2.5 | 200 | / | Extremely inconsistent, if not totally impossible to even activate in any distance but Sprint |
| Schwarzes Schwert | ✕ | △ | 2.5 | 200 | / | 0.15m/s but requires two additional checks (for Start Delay and Rushed) |
| A Princess Must Seize Victory! | ✕ | ✕ | 2.5 | 200 | / | Side block condition on the Last Straight is quite strict and difficult to proc |
| Dancing in the Leaves | ✕ | ✕ | 2.5 | 200 | / | Side Block isn't consistent, effect isn't outstanding either |
| Calm in a Crowd | ✕ | ✕ | 2.94 | 170 | / | Almost impossible to be boxed in on all sides in CM |
| Unruffled | ✕ | ✕ | 3.53 | 170+170 | / | Almost impossible to be boxed in on all sides in CM |
| Opening Gambit | ✕ | ✕ | 3.12 | 160 | Mile | Last Half of the Pack, at Random Point during Early-Race, ≥3s after Race Start |
| Battle Formation | ✕ | ✕ | 3.75 | 160+160 | Mile | Last Half of the Pack, at Random Point during Early-Race, ≥3s after Race Start |
| [Rotation]-Handed ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Speed stat increase is significant |
| [Season] Runner ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Speed stat increase is significant |
| Fall Frenzy | ✕ | ✕ | 3.64 | 90+110+130 | / | Take only on Autumn CMs |
| Outer Post Proficiency ◯ | ✕ | ✕ | 5.56 | 90 | / | Post Numbers 6-8 is inconsistent |
| Outer Post Proficiency ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Post Numbers 6-8 is inconsistent |
| Maverick ◯ | ✕ | ✕ | 5.56 | 90 | / | Very rare to have no Umas use your run style |
| Maverick ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Very rare to have no Umas use your run style |
| Long Shot ◯ | ✕ | ✕ | 5.56 | 90 | / | Popularity-dependent skills are inconsistent |
| Long Shot ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Popularity-dependent skills are inconsistent |
| Sympathy | ✕ | ▲ | 7.14 | 70 | / | Practically impossible to proc |
| [Location] Racecourse ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Yodo Invicta | ✕ | ✕ | 3.64 | 90+110+130 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Standard Distance ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Non-Standard Distance ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| [Ground Condition] Conditions ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Power Stat increase is decent but low priority |
| Competitive Spirit ◯ | ✕ | ✕ | 5.56 | 90 | / | It's unlikely for 40% of the lobby to use the same run style as you |
| Competitive Spirit ◎ | ✕ | ✕ | 2.5 | 90+110 | / | It's unlikely for 40% of the lobby to use the same run style as you |
| [Weather] Days ◎ | ✕ | △ | 2.5 | 90+110 | / | Guts is extremely unimportant, only take it you really need to |
| Target in Sight ◯ | ✕ | ✕ | 5.56 | 90 | / | Guts is extremely unimportant, only take it you really need to |
| Target in Sight ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Guts is extremely unimportant, only take it you really need to |
| Inner Post Proficiency ◯ | ✕ | ✕ | 5.56 | 90 | / | Post Numbers 1-3 is inconsistent |
| Inner Post Proficiency ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Post Numbers 1-3 is inconsistent |
| Lucky Seven | ✕ | ✕ | 4.55 | 110 | / | Inconsistent, even more so than the Post Proficiency skills |
| Super Lucky Seven | ✕ | ✕ | 5.45 | 110+110 | / | Inconsistent, even more so than the Post Proficiency skills |

##### Quick view: skills grouped by PvP tier

- **⍟ Essential (8):** [Run Style] Corners ◯; [Run Style] Straightaways ◯; [Distance] Corners ◯; [Distance] Straightaways ◯; [Run Style] Corners ◎; [Run Style] Straightaways ◎; [Distance] Corners ◎; [Distance] Straightaways ◎
- **◎ Top tier (42):** Uma Stan; Super Stan; Tail Held High; Slipstream; Playtime's Over!; Burning Spirit GUTS; Corner Recovery ◯; Swinging Maestro; Ignited Spirit PWR; Burning Spirit PWR; Hesitant [Run Style]s; Subdued [Run Style]s; Flustered [Run Style]s; Trick (Front); Tantalizing Trick; Trick (Rear); Lone Wolf; Ignited Spirit GUTS; Nimble Navigator; No Stopping Me!; Frenzied [Run Style]s; [Rotation]-Handed ◯; [Season] Runner ◯; Standard Distance ◯; Non-Standard Distance ◯; Shooting for Victory!; Let's Pump Some Iron!; Angling and Scheming; Certain Victory; Sky-High Teio Step; Triumphant Pulse; Victoria por plancha ☆; Behold Thine Emperor's Divine Might; Highlander; [Location] Racecourse ◯; [Ground Condition] Conditions ◯; [Rotation]-Handed ◎; [Season] Runner ◎; [Location] Racecourse ◎; Standard Distance ◎; Non-Standard Distance ◎; [Ground Condition] Conditions ◎
- **◯ Good (19):** [Run Style] Savvy ◯; Professor of Curvature; Beeline Burst; It's On!; In Body and Mind; Shooting Star; The Duty of Dignity Calls; This Dance Is for Vittoria!; Blazing Pride; ∴win Q.E.D.; Flashy☆Landing; Nemesis; Shadow Break; Lights of Vaudeville; I Never Goof Up!; Give Mummy a Hug ♡; Arrows Whistle, Shadows Disperse; Pop & Polish; Festive Miracle
- **▲ Situational (11):** Focus; Concentration; Resplendent Red Ace; SPARKLY☆STARDOM; Flowery☆Maneuver; Triple 7s; Groundwork; Prudent Positioning; Ignited Spirit WIT; [Run Style] Savvy ◎; Sympathy
- **△ Low priority (31):** Corner Adept ◯; Straightaway Adept; Ramp Up; Homestretch Haste; Ignited Spirit SPD; Burning Spirit SPD; Legacy of the Strong; The View from the Lead is Mine!; Where There's a Will, There's a Way; Blue Rose Closer; Our Ticket to Win!; #LookatCurren; Eternal Moments; You and Me! One-on-One!; A Kiss for Courage; Bountiful Harvest; OMG! (ﾟ∀ﾟ) The Final Sprint! ☆; Chasing After You; Presents from X; Fairy Tale; Straightaway Recovery; Breath of Fresh Air; Ignited Spirit STA; Burning Spirit STA; Pure Heart; Superior Heal; [Weather] Days ◯; G00 1st. F∞;; Genius x Bakushin = Victory; Schwarzes Schwert; [Weather] Days ◎
- **✕ Avoid (63):** Mile Maven; Unyielding Spirit; Big-Sisterly; Productive Plan; Shifting Gears; Changing Gears; Updrafters; Furious Feat; Watchful Eye; Keen Eye; Red Shift/LP1211-M; Condor's Fury; Anchors Aweigh!; Just a Little Farther!; YUMMY☆SPEED!; Lay Low; Iron Will; Pace Strategy; Indomitable; Shake It Out; U=ma2; Super-Duper Climax; Dazzl'n ♪ Diver; Every Rose Has Its Fangs; Corner Acceleration ◯; Corner Connoisseur; Straightaway Acceleration; Rushing Gale!; Acceleration; Step on the Gas!; KEEP IT REAL.; Moving Past, and Beyond; Center Stage; Go with the Flow; Lane Legerdemain; Burning Spirit WIT; Speed Eater; Risky Business; Cut and Drive!; I See Victory in My Future!; Prideful King; A Princess Must Seize Victory!; Dancing in the Leaves; Calm in a Crowd; Unruffled; Opening Gambit; Battle Formation; Fall Frenzy; Outer Post Proficiency ◯; Outer Post Proficiency ◎; Maverick ◯; Maverick ◎; Long Shot ◯; Long Shot ◎; Yodo Invicta; Competitive Spirit ◯; Competitive Spirit ◎; Target in Sight ◯; Target in Sight ◎; Inner Post Proficiency ◯; Inner Post Proficiency ◎; Lucky Seven; Super Lucky Seven

#### Medium

177 skills ranked for this build, grouped by their **Team Trials** tier. The PvP rank of each skill is shown in its own column.

##### ◎ Top tier (Team Trials): 28 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| [Run Style] Corners ◯ | ◎ | ⍟ | 3.85 | 130 | [Run Style] | Cheap and consistent, they are must-haves |
| [Run Style] Straightaways ◯ | ◎ | ⍟ | 3.85 | 130 | [Run Style] | Cheap and consistent, they are must-haves |
| [Distance] Corners ◯ | ◎ | ⍟ | 5 | 100 | [Distance] | Cheap and consistent, they are must-haves |
| [Distance] Straightaways ◯ | ◎ | ⍟ | 5 | 100 | [Distance] | Cheap and consistent, they are must-haves |
| Uma Stan | ◎ | ◎ | 3.12 | 160 | / | Best speed skill on longer tracks for non-Front-Runners, can help to release PDM on some longer tracks |
| Super Stan | ◎ | ◎ | 3.75 | 160+160 | / | Best speed skill on longer tracks for non-Front-Runners, can help to release PDM on some longer tracks |
| Tail Held High | ◎ | ◎ | 5 | 100 | / | Cheap and consistent, though note the condition of requiring 3 skill activations before acquiring it |
| Slipstream | ◎ | ◎ | 3.12 | 160 | / | Consistent and facilitates overtaking when activated |
| Playtime's Over! | ◎ | ◎ | 3.12 | 160 | / | Consistent and improves Uma's capacity to maintain her placement |
| Burning Spirit GUTS | ◎ | ◎ | 3 | 200+200 | / | Good random Late-Race accel but in the game's current state,<br>this skill's effect is likely 80% (when Total Guts ≤ 1200) or 90% (when 1200 < Total Guts ≤ 1600) |
| Corner Recovery ◯ | ◎ | ◎ | 2.94 | 170 | / | Consistent and effective recovery |
| Swinging Maestro | ◎ | ◎ | 3.53 | 170+170 | / | Consistent and effective recovery |
| Ignited Spirit PWR | ◎ | ◎ | 2.5 | 200 | / | It's like a weaker but universal Slick Surge/On Your Left! |
| Burning Spirit PWR | ◎ | ◎ | 3 | 200+200 | / | It's like a weaker but universal Slick Surge/On Your Left! |
| Focus | ◎ | ▲ | 3.57 | 140 | / | Only take for Front Runners, Focus reduces the chance of a Late Start, while Concentration makes it impossible<br>You also get score for "strong starts" in Team Trials, so Concentration is always good there |
| Concentration | ◎ | ▲ | 4.29 | 140+140 | / | Only take for Front Runners, Focus reduces the chance of a Late Start, while Concentration makes it impossible<br>You also get score for "strong starts" in Team Trials, so Concentration is always good there |
| Hesitant [Run Style]s | ◎ | ◎ | 3.85 | 130 | / | Random Point in Late-Race |
| Subdued [Run Style]s | ◎ | ◎ | 3.85 | 130 | / | Random Point in Early-Race, ≥5 after Race Start |
| Flustered [Run Style]s | ◎ | ◎ | 3.85 | 130 | / | Random Point in Mid-Race |
| Trick (Front) | ◎ | ◎ | 3.57 | 140 | / | First Half of the Pack, ≥1 "Rushed" Uma behind |
| Tantalizing Trick | ◎ | ◎ | 4.29 | 140+140 | / | First Half of the Pack, ≥1 "Rushed" Uma behind |
| Trick (Rear) | ◎ | ◎ | 3.57 | 140 | / | 2nd-9th/12th Place, ≥1 "Rushed" Uma ahead |
| Tether | ◎ | ✕ | 3.12 | 160 | Medium | Last Half of the Pack, at Random Point during Late-Race |
| Dominator | ◎ | ✕ | 3.75 | 160+160 | Medium | Last Half of the Pack, at Random Point during Late-Race |
| Murmur | ◎ | ✕ | 3.12 | 160 | Medium | Blocked in Front for ≥1s, during Mid-Race |
| Mystifying Murmur | ◎ | ✕ | 3.75 | 160+160 | Medium | Blocked in Front for ≥1s, during Mid-Race |
| Lone Wolf | ◎ | ◎ | 7.14 | 70 | / | Easy to proc, you either benefit (you proc) or make it even (you prevent someone else's from proc'ing) |
| [Run Style] Savvy ◯ | ◎ | ◯ | 4.55 | 110 | [Run Style] | Consistent activation, FoV buff is useful for Nice Nature's All-Seeing Eyes |

##### ◯ Good (Team Trials): 14 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| Professor of Curvature | ◯ | ◯ | 3.33 | 180+180 | / | Consistent, but expensive<br>Rare ver. has greater speed boost making it more worth to acquire |
| Beeline Burst | ◯ | ◯ | 3.53 | 170+170 | / | Consistent |
| It's On! | ◯ | ◯ | 3.53 | 170+170 | / | Consistent. Even better when used in tandem with Tail Held High, Slipstream, and Playtime's Over! |
| In Body and Mind | ◯ | ◯ | 3.53 | 170+170 | / | Useful and (fairly) consistent Last Spurt speed boost, falls short of ◎ because it could activate at the very end of a race |
| Ignited Spirit GUTS | ◯ | ◎ | 2.5 | 200 | / | Good random Late-Race accel but in the game's current state,<br>this skill's effect is likely 80% (when Total Guts ≤ 1200) or 90% (when 1200 < Total Guts ≤ 1600) |
| Up-Tempo | ◯ | ✕ | 3.12 | 160 | Medium | Consistent |
| Killer Tunes | ◯ | ✕ | 3.75 | 160+160 | Medium | Consistent |
| Nimble Navigator | ◯ | ◎ | 3.33 | 150 | / | Strong accel but rng-dependent |
| No Stopping Me! | ◯ | ◎ | 4 | 150+150 | / | Strong accel but rng-dependent |
| Frenzied [Run Style]s | ◯ | ◎ | 3.85 | 130 | / | [Run Style] is "Rushed" |
| [Rotation]-Handed ◯ | ◯ | ◎ | 5.56 | 90 | / | Speed stat increase is significant |
| [Season] Runner ◯ | ◯ | ◎ | 5.56 | 90 | / | Speed stat increase is significant |
| Standard Distance ◯ | ◯ | ◎ | 5.56 | 90 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Non-Standard Distance ◯ | ◯ | ◎ | 5.56 | 90 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |

##### ▲ Situational (Team Trials): 5 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| Red Shift/LP1211-M | ▲ | ✕ | 2.5 | 200 | / | Powerful accel for Fronts/Paces, especially on tracks where Last Spurt Mode begins slightly before or on the Final Corner |
| Shooting for Victory! | ▲ | ◎ | 2.5 | 200 | / | Powerful accel for Paces/Lates, especially on tracks where Last Spurt Mode begins slightly before or on the Second Half of the Final Corner |
| Let's Pump Some Iron! | ▲ | ◎ | 2.5 | 200 | / | Strongest but most inconsistent accel for Lates/Ends on tracks where Last Spurt Mode begins slightly before or on the Final Corner |
| Angling and Scheming | ▲ | ◎ | 2.5 | 200 | / | Strongest accel for Fronts on tracks where Last Spurt Mode begins on a Corner |
| Condor's Fury | ▲ | ✕ | 2.5 | 200 | / | Powerful accel for Lates/Ends, especially on tracks where Last Spurt Mode begins slightly before or on the Final Corner |

##### △ Low priority (Team Trials): 95 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| [Run Style] Corners ◎ | △ | ⍟ | 1.85 | 130+140 | [Run Style] | Cheap and consistent, they are must-haves |
| [Run Style] Straightaways ◎ | △ | ⍟ | 1.85 | 130+140 | [Run Style] | Cheap and consistent, they are must-haves |
| [Distance] Corners ◎ | △ | ⍟ | 2.38 | 100+110 | [Distance] | Cheap and consistent, they are must-haves |
| [Distance] Straightaways ◎ | △ | ⍟ | 2.38 | 100+110 | [Distance] | Cheap and consistent, they are must-haves |
| Corner Adept ◯ | △ | △ | 2.78 | 180 | / | Consistent, but expensive<br>Rare ver. has greater speed boost making it more worth to acquire |
| Straightaway Adept | △ | △ | 2.94 | 170 | / | Consistent |
| Ramp Up | △ | △ | 2.94 | 170 | / | Consistent. Even better when used in tandem with Tail Held High, Slipstream, and Playtime's Over! |
| Homestretch Haste | △ | △ | 2.94 | 170 | / | Useful and (fairly) consistent Last Spurt speed boost, falls short of ◎ because it could activate at the very end of a race |
| Ignited Spirit SPD | △ | △ | 2.5 | 200 | / | 1.8s isn't very long and it costs 200 base SP |
| Burning Spirit SPD | △ | △ | 3 | 200+200 | / | 1.8s isn't very long and it costs 200 base SP |
| Steadfast | △ | ✕ | 3.12 | 160 | Medium | Essentially a band-aid protective measure against losing the lead on the Final Corner, could be good but it's very situational |
| Unyielding | △ | ✕ | 3.75 | 160+160 | Medium | Essentially a band-aid protective measure against losing the lead on the Final Corner, could be good but it's very situational |
| All I've Got | △ | ✕ | 3.12 | 160 | Medium | Other than a few 2400m tracks, most Medium tracks have their Last Spurt Modes activate on a Corner, so this skill acts as a better Homestretch Haste/In Body and Mind |
| Come What May | △ | ✕ | 3.75 | 160+160 | Medium | Other than a few 2400m tracks, most Medium tracks have their Last Spurt Modes activate on a Corner, so this skill acts as a better Homestretch Haste/In Body and Mind |
| Certain Victory | △ | ◎ | 2.5 | 200 | / | Identical to OG Teio's unique with slightly looser conditions |
| Legacy of the Strong | △ | △ | 2.5 | 200 | / | Effects aren't bad but inconsistent activation |
| Shooting Star | △ | ◯ | 2.5 | 200 | / | Consistent activation, but weak effect |
| The View from the Lead is Mine! | △ | △ | 2.5 | 200 | / | Somewhat consistent activation for Front Runners, but weak effect |
| Sky-High Teio Step | △ | ◎ | 2.5 | 200 | / | Mostly consistent for non-Front-Runners, with strong effect |
| Triumphant Pulse | △ | ◎ | 2.5 | 200 | / | Consistent for non-Front-Runners, with strong effect |
| Anchors Aweigh! | △ | ✕ | 2.5 | 200 | / | Consistent for Late Surgers/End Closers but minimal effect |
| Resplendent Red Ace | △ | ▲ | 2.5 | 200 | / | Accel can come in handy occasionally but still very situational and slightly unreliable |
| Where There's a Will, There's a Way | △ | △ | 2.5 | 200 | / | Decent speed skill option for non-Front-Runners |
| The Duty of Dignity Calls | △ | ◯ | 2.5 | 200 | / | Final Corner Target Speed boost is inconsistent (especially in Med race), but it can be situationally good for Front Runners/Pace Chasers |
| Victoria por plancha ☆ | △ | ◎ | 2.5 | 200 | / | Activation is mostly consistent, some tracks benefit from a Last Straight accel |
| This Dance Is for Vittoria! | △ | ◯ | 2.5 | 200 | / | Fairly consistent activation but Final Corner Target Speed boost could be inconsistent |
| Behold Thine Emperor's Divine Might | △ | ◎ | 2.5 | 200 | / | Consistent for non-Front-Runners, with strong effect |
| Blazing Pride | △ | ◯ | 2.5 | 200 | / | Final Corner Target Speed boost is inconsistent (especially in Med race), but it can be situationally good for Late Surgers |
| ∴win Q.E.D. | △ | ◯ | 2.5 | 200 | / | Final Corner Target Speed boost is inconsistent (especially in Med race), but it can be situationally good for Front Runners |
| Flashy☆Landing | △ | ◯ | 2.5 | 200 | / | Acceleration on and beyond Final Corner is decent, conditions to activate may not be consistent unless you're Front Runner or Pace Chaser |
| Blue Rose Closer | △ | △ | 2.5 | 200 | / | Consistent, but weak effect |
| Our Ticket to Win! | △ | △ | 2.5 | 200 | / | Side block on Last Straight is rare, weak effect as well makes it not worth getting |
| Just a Little Farther! | △ | ✕ | 2.5 | 200 | / | Fairly consistent, but also weak |
| #LookatCurren | △ | △ | 2.5 | 200 | / | Slightly consistent but effect is really weak since it usually activates at Mid-Race |
| Nemesis | △ | ◯ | 2.5 | 200 | / | Consistent for Late Surgers/End Closers but effect is weak |
| SPARKLY☆STARDOM | △ | ▲ | 2.5 | 200 | / | Mostly consistent for most Front Runners and helps them maintain their lead |
| Shadow Break | △ | ◯ | 2.5 | 200 | / | Should be consistent but effect isn't great enough to be used over other similar uniques |
| Eternal Moments | △ | △ | 2.5 | 200 | / | Fairly consistent for non-Front-Runners, but the effect is weak |
| Flowery☆Maneuver | △ | ▲ | 2.5 | 200 | / | ① Strong for Front/Pace on some tracks to carry over speed on final corner<br>② Strong for Late/End on tracks that start the Last Spurt on final corner |
| You and Me! One-on-One! | △ | △ | 2.5 | 200 | / | Decent Last Straight speed skill for Late Surgers or End Closers |
| Lights of Vaudeville | △ | ◯ | 2.5 | 200 | / | Consistent activation but effectiveness depends on track |
| A Kiss for Courage | △ | △ | 2.5 | 200 | / | Varying effectiveness depending on track but can be strong with Triple 7s activation |
| I Never Goof Up! | △ | ◯ | 2.5 | 200 | / | Good effect but rng and track dependent |
| Bountiful Harvest | △ | △ | 2.5 | 200 | / | Consistent but relatively weak |
| YUMMY☆SPEED! | △ | ✕ | 2.5 | 200 | / | Unfortunate timing at 60% of the Race makes this skill's acceleration practically useless |
| OMG! (ﾟ∀ﾟ) The Final Sprint! ☆ | △ | △ | 2.5 | 200 | / | Generally, when you overtake in Late-Race, you're still accelerating, so a Target Speed skill wouldn't be effective |
| Give Mummy a Hug ♡ | △ | ◯ | 2.5 | 200 | / | Good accel for tracks that have their Last Spurt Mode begin on/near a Last Straight |
| Chasing After You | △ | △ | 2.5 | 200 | / | Very weak effect but can be used as a debuff |
| Arrows Whistle, Shadows Disperse | △ | ◯ | 2.5 | 200 | / | Consistent, but weak effect |
| Pop & Polish | △ | ◯ | 2.5 | 200 | / | Consistent, but weak effect |
| Presents from X | △ | △ | 2.5 | 200 | / | Consistent, but weak effect |
| Festive Miracle | △ | ◯ | 2.5 | 200 | / | Strong on some tracks where Triple 7s can proc before the Last Spurt |
| Fairy Tale | △ | △ | 2.5 | 200 | / | Strong on some tracks where Triple 7s can proc before the Last Spurt |
| Straightaway Recovery | △ | △ | 2.94 | 170 | / | Inconsistent, it might be wasted on an early or late activation |
| Breath of Fresh Air | △ | △ | 3.53 | 170+170 | / | Inconsistent, it might be wasted on an early or late activation |
| Lay Low | △ | ✕ | 3.12 | 160 | / | Might proc in Early-Race which might overflow HP |
| Iron Will | △ | ✕ | 3.75 | 160+160 | / | Might proc in Early-Race which might overflow HP |
| Pace Strategy | △ | ✕ | 2.94 | 170 | / | Being overtaken is an inconsistent condition<br>More suitable on long, backline Run Styles |
| Indomitable | △ | ✕ | 3.53 | 170+170 | / | Being overtaken is an inconsistent condition<br>More suitable on long, backline Run Styles |
| Triple 7s | △ | ▲ | 3.12 | 160 | / | Consistent, but only effective on <2400m tracks, useful for some Uma that rely on Stamina skill procs |
| Shake It Out | △ | ✕ | 5 | 100 | / | Late-Race recovery is ineffective<br>consider acquiring it only for Team Trials because it's very cheap |
| Ignited Spirit STA | △ | △ | 2.5 | 200 | / | Definitely an option but it costs more than a usual skill (at 200 base SP) |
| Burning Spirit STA | △ | △ | 3 | 200+200 | / | Definitely an option but it costs more than a usual skill (at 200 base SP) |
| Rosy Outlook | △ | ✕ | 3.12 | 160 | Medium | Consistent recovery for Front Runners and perhaps even Pace Chasers |
| Trackblazer | △ | ✕ | 3.75 | 160+160 | Medium | Consistent recovery for Front Runners and perhaps even Pace Chasers |
| Soft Step | △ | ✕ | 3.12 | 160 | Medium | Consistent but effect isn't that strong<br>Rare ver. is actually worse as this tends to activate early on and the 5.5% recovery could overflow |
| Miraculous Step | △ | ✕ | 3.75 | 160+160 | Medium | Consistent but effect isn't that strong<br>Rare ver. is actually worse as this tends to activate early on and the 5.5% recovery could overflow |
| U=ma2 | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Pure Heart | △ | △ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Super-Duper Climax | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Superior Heal | △ | △ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Dazzl'n ♪ Diver | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Every Rose Has Its Fangs | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Corner Acceleration ◯ | △ | ✕ | 2.78 | 180 | / | Acceleration on the Corner 1/First Corner of any track is useless |
| Corner Connoisseur | △ | ✕ | 3.33 | 180+180 | / | Acceleration on the Corner 1/First Corner of any track is useless |
| Straightaway Acceleration | △ | ✕ | 2.94 | 170 | / | Random straight activations are too inconsistent to be effective |
| Rushing Gale! | △ | ✕ | 3.53 | 170+170 | / | Random straight activations are too inconsistent to be effective |
| Highlander | △ | ◎ | 3.12 | 160 | / | Very powerful on tracks with Uphills right before/as Last Spurt Mode begins |
| Groundwork | △ | ▲ | 5 | 100 | / | For Front Runners only, use with 3 Early-Race skills like Focus/Concentration+Green Skills |
| KEEP IT REAL. | △ | ✕ | 2.5 | 200 | / | Mostly useless accel but consistent activation |
| Moving Past, and Beyond | △ | ✕ | 2.5 | 200 | / | Mostly useless accel but consistent activation |
| Prudent Positioning | △ | ▲ | 4.17 | 120 | / | Use with Dodging Danger for a very powerful Early-Race burst of speed (Front Runner only) |
| Center Stage | △ | ✕ | 5 | 120+120 | / | Never use for Front-Runners that want to run the Dodging Danger tech |
| Go with the Flow | △ | ✕ | 4.17 | 120 | / | Random non-Early-Race Lane Movement Speed for non-Front-Runners are useless<br>Take only because they are very cheap and if you have no other options |
| Lane Legerdemain | △ | ✕ | 5 | 120+120 | / | Random non-Early-Race Lane Movement Speed for non-Front-Runners are useless<br>Take only because they are very cheap and if you have no other options |
| Ignited Spirit WIT | △ | ▲ | 2.5 | 200 | / | Use with Dodging Danger for a very powerful Early-Race burst of speed (Front Runner only) |
| Burning Spirit WIT | △ | ✕ | 3 | 200+200 | / | Never use for Front-Runners that want to run the Dodging Danger tech |
| Thunderbolt Step | △ | ✕ | 3.57 | 140 | Medium | Random non-Early-Race Lane Movement Speed for non-Front-Runners are useless<br>There is no need for any additional acceleration (unless it's toward the very end which is very RNG-dependent)<br>Take only because they are very cheap and if you have no other options |
| Lightning Step | △ | ✕ | 4.29 | 140+140 | Medium | Random non-Early-Race Lane Movement Speed for non-Front-Runners are useless<br>There is no need for any additional acceleration (unless it's toward the very end which is very RNG-dependent)<br>Take only because they are very cheap and if you have no other options |
| Hawkeye | △ | ✕ | 4.55 | 110 | Medium | Extra FoV is mostly useless<br>Take only because they are very cheap and if you have no other options |
| Clairvoyance | △ | ✕ | 5.45 | 110+110 | Medium | Extra FoV is mostly useless<br>Take only because they are very cheap and if you have no other options |
| [Location] Racecourse ◯ | △ | ◎ | 5.56 | 90 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| [Ground Condition] Conditions ◯ | △ | ◎ | 5.56 | 90 | / | Power Stat increase is decent but low priority |
| [Weather] Days ◯ | △ | △ | 5.56 | 90 | / | Guts is extremely unimportant, only take it you really need to |
| [Run Style] Savvy ◎ | △ | ▲ | 2.08 | 110+130 | [Run Style] | Consistent activation, FoV buff is useful for Nice Nature's All-Seeing Eyes |

##### ✕ Avoid (Team Trials): 35 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| Risky Business | ✕ | ✕ | 4.17 | 120 | / | This skill can completely kill your stamina, it's definitely not worth it unless you're trying to do some niche strat |
| Cut and Drive! | ✕ | ✕ | 2.5 | 200 | / | Not the most consistent, and also a weak effect, not worth taking |
| G00 1st. F∞; | ✕ | △ | 2.5 | 200 | / | 0.15m/s but has two additional checks (for Start Delay and Rushed) |
| Genius x Bakushin = Victory | ✕ | △ | 2.5 | 200 | / | Fairly consistent, but also weak |
| I See Victory in My Future! | ✕ | ✕ | 2.5 | 200 | / | Front Block condition is downright horrible |
| Prideful King | ✕ | ✕ | 2.5 | 200 | / | Extremely inconsistent, if not totally impossible to even activate in any distance but Sprint |
| Schwarzes Schwert | ✕ | △ | 2.5 | 200 | / | 0.15m/s but requires two additional checks (for Start Delay and Rushed) |
| A Princess Must Seize Victory! | ✕ | ✕ | 2.5 | 200 | / | Side block condition on the Last Straight is quite strict and difficult to proc |
| Dancing in the Leaves | ✕ | ✕ | 2.5 | 200 | / | Side Block isn't consistent, effect isn't outstanding either |
| Calm in a Crowd | ✕ | ✕ | 2.94 | 170 | / | Almost impossible to be boxed in on all sides in CM |
| Unruffled | ✕ | ✕ | 3.53 | 170+170 | / | Almost impossible to be boxed in on all sides in CM |
| [Rotation]-Handed ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Speed stat increase is significant |
| [Season] Runner ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Speed stat increase is significant |
| Fall Frenzy | ✕ | ✕ | 3.64 | 90+110+130 | / | Take only on Autumn CMs |
| Outer Post Proficiency ◯ | ✕ | ✕ | 5.56 | 90 | / | Post Numbers 6-8 is inconsistent |
| Outer Post Proficiency ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Post Numbers 6-8 is inconsistent |
| Maverick ◯ | ✕ | ✕ | 5.56 | 90 | / | Very rare to have no Umas use your run style |
| Maverick ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Very rare to have no Umas use your run style |
| Long Shot ◯ | ✕ | ✕ | 5.56 | 90 | / | Popularity-dependent skills are inconsistent |
| Long Shot ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Popularity-dependent skills are inconsistent |
| Sympathy | ✕ | ▲ | 7.14 | 70 | / | Practically impossible to proc |
| [Location] Racecourse ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Yodo Invicta | ✕ | ✕ | 3.64 | 90+110+130 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Standard Distance ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Non-Standard Distance ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| [Ground Condition] Conditions ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Power Stat increase is decent but low priority |
| Competitive Spirit ◯ | ✕ | ✕ | 5.56 | 90 | / | It's unlikely for 40% of the lobby to use the same run style as you |
| Competitive Spirit ◎ | ✕ | ✕ | 2.5 | 90+110 | / | It's unlikely for 40% of the lobby to use the same run style as you |
| [Weather] Days ◎ | ✕ | △ | 2.5 | 90+110 | / | Guts is extremely unimportant, only take it you really need to |
| Target in Sight ◯ | ✕ | ✕ | 5.56 | 90 | / | Guts is extremely unimportant, only take it you really need to |
| Target in Sight ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Guts is extremely unimportant, only take it you really need to |
| Inner Post Proficiency ◯ | ✕ | ✕ | 5.56 | 90 | / | Post Numbers 1-3 is inconsistent |
| Inner Post Proficiency ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Post Numbers 1-3 is inconsistent |
| Lucky Seven | ✕ | ✕ | 4.55 | 110 | / | Inconsistent, even more so than the Post Proficiency skills |
| Super Lucky Seven | ✕ | ✕ | 5.45 | 110+110 | / | Inconsistent, even more so than the Post Proficiency skills |

##### Quick view: skills grouped by PvP tier

- **⍟ Essential (8):** [Run Style] Corners ◯; [Run Style] Straightaways ◯; [Distance] Corners ◯; [Distance] Straightaways ◯; [Run Style] Corners ◎; [Run Style] Straightaways ◎; [Distance] Corners ◎; [Distance] Straightaways ◎
- **◎ Top tier (42):** Uma Stan; Super Stan; Tail Held High; Slipstream; Playtime's Over!; Burning Spirit GUTS; Corner Recovery ◯; Swinging Maestro; Ignited Spirit PWR; Burning Spirit PWR; Hesitant [Run Style]s; Subdued [Run Style]s; Flustered [Run Style]s; Trick (Front); Tantalizing Trick; Trick (Rear); Lone Wolf; Ignited Spirit GUTS; Nimble Navigator; No Stopping Me!; Frenzied [Run Style]s; [Rotation]-Handed ◯; [Season] Runner ◯; Standard Distance ◯; Non-Standard Distance ◯; Shooting for Victory!; Let's Pump Some Iron!; Angling and Scheming; Certain Victory; Sky-High Teio Step; Triumphant Pulse; Victoria por plancha ☆; Behold Thine Emperor's Divine Might; Highlander; [Location] Racecourse ◯; [Ground Condition] Conditions ◯; [Rotation]-Handed ◎; [Season] Runner ◎; [Location] Racecourse ◎; Standard Distance ◎; Non-Standard Distance ◎; [Ground Condition] Conditions ◎
- **◯ Good (19):** [Run Style] Savvy ◯; Professor of Curvature; Beeline Burst; It's On!; In Body and Mind; Shooting Star; The Duty of Dignity Calls; This Dance Is for Vittoria!; Blazing Pride; ∴win Q.E.D.; Flashy☆Landing; Nemesis; Shadow Break; Lights of Vaudeville; I Never Goof Up!; Give Mummy a Hug ♡; Arrows Whistle, Shadows Disperse; Pop & Polish; Festive Miracle
- **▲ Situational (11):** Focus; Concentration; Resplendent Red Ace; SPARKLY☆STARDOM; Flowery☆Maneuver; Triple 7s; Groundwork; Prudent Positioning; Ignited Spirit WIT; [Run Style] Savvy ◎; Sympathy
- **△ Low priority (31):** Corner Adept ◯; Straightaway Adept; Ramp Up; Homestretch Haste; Ignited Spirit SPD; Burning Spirit SPD; Legacy of the Strong; The View from the Lead is Mine!; Where There's a Will, There's a Way; Blue Rose Closer; Our Ticket to Win!; #LookatCurren; Eternal Moments; You and Me! One-on-One!; A Kiss for Courage; Bountiful Harvest; OMG! (ﾟ∀ﾟ) The Final Sprint! ☆; Chasing After You; Presents from X; Fairy Tale; Straightaway Recovery; Breath of Fresh Air; Ignited Spirit STA; Burning Spirit STA; Pure Heart; Superior Heal; [Weather] Days ◯; G00 1st. F∞;; Genius x Bakushin = Victory; Schwarzes Schwert; [Weather] Days ◎
- **✕ Avoid (66):** Tether; Dominator; Murmur; Mystifying Murmur; Up-Tempo; Killer Tunes; Red Shift/LP1211-M; Condor's Fury; Steadfast; Unyielding; All I've Got; Come What May; Anchors Aweigh!; Just a Little Farther!; YUMMY☆SPEED!; Lay Low; Iron Will; Pace Strategy; Indomitable; Shake It Out; Rosy Outlook; Trackblazer; Soft Step; Miraculous Step; U=ma2; Super-Duper Climax; Dazzl'n ♪ Diver; Every Rose Has Its Fangs; Corner Acceleration ◯; Corner Connoisseur; Straightaway Acceleration; Rushing Gale!; KEEP IT REAL.; Moving Past, and Beyond; Center Stage; Go with the Flow; Lane Legerdemain; Burning Spirit WIT; Thunderbolt Step; Lightning Step; Hawkeye; Clairvoyance; Risky Business; Cut and Drive!; I See Victory in My Future!; Prideful King; A Princess Must Seize Victory!; Dancing in the Leaves; Calm in a Crowd; Unruffled; Fall Frenzy; Outer Post Proficiency ◯; Outer Post Proficiency ◎; Maverick ◯; Maverick ◎; Long Shot ◯; Long Shot ◎; Yodo Invicta; Competitive Spirit ◯; Competitive Spirit ◎; Target in Sight ◯; Target in Sight ◎; Inner Post Proficiency ◯; Inner Post Proficiency ◎; Lucky Seven; Super Lucky Seven

#### Long

174 skills ranked for this build, grouped by their **Team Trials** tier. The PvP rank of each skill is shown in its own column.

##### ◎ Top tier (Team Trials): 25 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| [Run Style] Corners ◯ | ◎ | ⍟ | 3.85 | 130 | [Run Style] | Cheap and consistent, they are must-haves |
| [Run Style] Straightaways ◯ | ◎ | ⍟ | 3.85 | 130 | [Run Style] | Cheap and consistent, they are must-haves |
| [Distance] Corners ◯ | ◎ | ⍟ | 5 | 100 | [Distance] | Cheap and consistent, they are must-haves |
| [Distance] Straightaways ◯ | ◎ | ⍟ | 5 | 100 | [Distance] | Cheap and consistent, they are must-haves |
| Uma Stan | ◎ | ◎ | 3.12 | 160 | / | Best speed skill on longer tracks for non-Front-Runners, can help to release PDM on some longer tracks |
| Super Stan | ◎ | ◎ | 3.75 | 160+160 | / | Best speed skill on longer tracks for non-Front-Runners, can help to release PDM on some longer tracks |
| Tail Held High | ◎ | ◎ | 5 | 100 | / | Cheap and consistent, though note the condition of requiring 3 skill activations before acquiring it |
| Slipstream | ◎ | ◎ | 3.12 | 160 | / | Consistent and facilitates overtaking when activated |
| Playtime's Over! | ◎ | ◎ | 3.12 | 160 | / | Consistent and improves Uma's capacity to maintain her placement |
| Burning Spirit GUTS | ◎ | ◎ | 3 | 200+200 | / | Good random Late-Race accel but in the game's current state,<br>this skill's effect is likely 80% (when Total Guts ≤ 1200) or 90% (when 1200 < Total Guts ≤ 1600) |
| Corner Recovery ◯ | ◎ | ◎ | 2.94 | 170 | / | Consistent and effective recovery |
| Swinging Maestro | ◎ | ◎ | 3.53 | 170+170 | / | Consistent and effective recovery |
| Ignited Spirit PWR | ◎ | ◎ | 2.5 | 200 | / | It's like a weaker but universal Slick Surge/On Your Left! |
| Burning Spirit PWR | ◎ | ◎ | 3 | 200+200 | / | It's like a weaker but universal Slick Surge/On Your Left! |
| Focus | ◎ | ▲ | 3.57 | 140 | / | Only take for Front Runners, Focus reduces the chance of a Late Start, while Concentration makes it impossible<br>You also get score for "strong starts" in Team Trials, so Concentration is always good there |
| Concentration | ◎ | ▲ | 4.29 | 140+140 | / | Only take for Front Runners, Focus reduces the chance of a Late Start, while Concentration makes it impossible<br>You also get score for "strong starts" in Team Trials, so Concentration is always good there |
| Hesitant [Run Style]s | ◎ | ◎ | 3.85 | 130 | / | Random Point in Late-Race |
| Subdued [Run Style]s | ◎ | ◎ | 3.85 | 130 | / | Random Point in Early-Race, ≥5 after Race Start |
| Flustered [Run Style]s | ◎ | ◎ | 3.85 | 130 | / | Random Point in Mid-Race |
| Trick (Front) | ◎ | ◎ | 3.57 | 140 | / | First Half of the Pack, ≥1 "Rushed" Uma behind |
| Tantalizing Trick | ◎ | ◎ | 4.29 | 140+140 | / | First Half of the Pack, ≥1 "Rushed" Uma behind |
| Trick (Rear) | ◎ | ◎ | 3.57 | 140 | / | 2nd-9th/12th Place, ≥1 "Rushed" Uma ahead |
| Stamina Siphon | ◎ | ◎ | 3.75 | 160+160 | Long | ≥5th Place, at Random Point in Mid-Race |
| Lone Wolf | ◎ | ◎ | 7.14 | 70 | / | Easy to proc, you either benefit (you proc) or make it even (you prevent someone else's from proc'ing) |
| [Run Style] Savvy ◯ | ◎ | ◯ | 4.55 | 110 | [Run Style] | Consistent activation, FoV buff is useful for Nice Nature's All-Seeing Eyes |

##### ◯ Good (Team Trials): 13 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| Professor of Curvature | ◯ | ◯ | 3.33 | 180+180 | / | Consistent, but expensive<br>Rare ver. has greater speed boost making it more worth to acquire |
| Beeline Burst | ◯ | ◯ | 3.53 | 170+170 | / | Consistent |
| It's On! | ◯ | ◯ | 3.53 | 170+170 | / | Consistent. Even better when used in tandem with Tail Held High, Slipstream, and Playtime's Over! |
| In Body and Mind | ◯ | ◯ | 3.53 | 170+170 | / | Useful and (fairly) consistent Last Spurt speed boost, falls short of ◎ because it could activate at the very end of a race |
| Ignited Spirit GUTS | ◯ | ◎ | 2.5 | 200 | / | Good random Late-Race accel but in the game's current state,<br>this skill's effect is likely 80% (when Total Guts ≤ 1200) or 90% (when 1200 < Total Guts ≤ 1600) |
| Nimble Navigator | ◯ | ◎ | 3.33 | 150 | / | Strong accel but rng-dependent |
| No Stopping Me! | ◯ | ◎ | 4 | 150+150 | / | Strong accel but rng-dependent |
| Frenzied [Run Style]s | ◯ | ◎ | 3.85 | 130 | / | [Run Style] is "Rushed" |
| Stamina Eater | ◯ | ◎ | 3.12 | 160 | Long | ≥5th Place, at Random Point in Mid-Race |
| [Rotation]-Handed ◯ | ◯ | ◎ | 5.56 | 90 | / | Speed stat increase is significant |
| [Season] Runner ◯ | ◯ | ◎ | 5.56 | 90 | / | Speed stat increase is significant |
| Standard Distance ◯ | ◯ | ◎ | 5.56 | 90 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Non-Standard Distance ◯ | ◯ | ◎ | 5.56 | 90 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |

##### ▲ Situational (Team Trials): 5 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| Red Shift/LP1211-M | ▲ | ✕ | 2.5 | 200 | / | Powerful accel for Fronts/Paces, especially on tracks where Last Spurt Mode begins slightly before or on the Final Corner |
| Shooting for Victory! | ▲ | ◎ | 2.5 | 200 | / | Powerful accel for Paces/Lates, especially on tracks where Last Spurt Mode begins slightly before or on the Second Half of the Final Corner |
| Let's Pump Some Iron! | ▲ | ◎ | 2.5 | 200 | / | Strongest but most inconsistent accel for Lates/Ends on tracks where Last Spurt Mode begins slightly before or on the Final Corner |
| Angling and Scheming | ▲ | ◎ | 2.5 | 200 | / | Strongest accel for Fronts on tracks where Last Spurt Mode begins on a Corner |
| Condor's Fury | ▲ | ✕ | 2.5 | 200 | / | Powerful accel for Lates/Ends, especially on tracks where Last Spurt Mode begins slightly before or on the Final Corner |

##### △ Low priority (Team Trials): 96 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| [Run Style] Corners ◎ | △ | ⍟ | 1.85 | 130+140 | [Run Style] | Cheap and consistent, they are must-haves |
| [Run Style] Straightaways ◎ | △ | ⍟ | 1.85 | 130+140 | [Run Style] | Cheap and consistent, they are must-haves |
| [Distance] Corners ◎ | △ | ⍟ | 2.38 | 100+110 | [Distance] | Cheap and consistent, they are must-haves |
| [Distance] Straightaways ◎ | △ | ⍟ | 2.38 | 100+110 | [Distance] | Cheap and consistent, they are must-haves |
| Corner Adept ◯ | △ | △ | 2.78 | 180 | / | Consistent, but expensive<br>Rare ver. has greater speed boost making it more worth to acquire |
| Straightaway Adept | △ | △ | 2.94 | 170 | / | Consistent |
| Ramp Up | △ | △ | 2.94 | 170 | / | Consistent. Even better when used in tandem with Tail Held High, Slipstream, and Playtime's Over! |
| Homestretch Haste | △ | △ | 2.94 | 170 | / | Useful and (fairly) consistent Last Spurt speed boost, falls short of ◎ because it could activate at the very end of a race |
| Ignited Spirit SPD | △ | △ | 2.5 | 200 | / | 1.8s isn't very long and it costs 200 base SP |
| Burning Spirit SPD | △ | △ | 3 | 200+200 | / | 1.8s isn't very long and it costs 200 base SP |
| Inside Scoop | △ | ✕ | 3.12 | 160 | Long | Somewhat consistent but Target Speed boost during Final Corners are only useful if Uma will enter Last Spurt Mode in a few seconds/has already entered Last Spurt Mode.<br>Otherwise, boosting Target Speed right when Uma enters Last Spurt Mode renders it useless (doesn't actually increase speed since Uma's Current Speed hasn't reached Target Speed) |
| Innate Experience | △ | ✕ | 3.75 | 160+160 | Long | Somewhat consistent but Target Speed boost during Final Corners are only useful if Uma will enter Last Spurt Mode in a few seconds/has already entered Last Spurt Mode.<br>Otherwise, boosting Target Speed right when Uma enters Last Spurt Mode renders it useless (doesn't actually increase speed since Uma's Current Speed hasn't reached Target Speed) |
| Keeping the Lead | △ | △ | 3.12 | 160 | Long | 2.5m lead is somewhat possible in a Long race but still not the most consistent |
| Vanguard Spirit | △ | △ | 3.75 | 160+160 | Long | 2.5m lead is somewhat possible in a Long race but still not the most consistent |
| Pressure | △ | ✕ | 3.12 | 160 | Long | Overtakes and consequently, Target Speed boost is likely to occur toward the beginning of Last Spurt Mode,<br>rendering it useless (doesn't actually increase speed since Uma's Current Speed hasn't reached Target Speed) |
| Overwhelming Pressure | △ | ✕ | 3.75 | 160+160 | Long | Overtakes and consequently, Target Speed boost is likely to occur toward the beginning of Last Spurt Mode,<br>rendering it useless (doesn't actually increase speed since Uma's Current Speed hasn't reached Target Speed) |
| Certain Victory | △ | ◎ | 2.5 | 200 | / | Identical to OG Teio's unique with slightly looser conditions |
| Legacy of the Strong | △ | △ | 2.5 | 200 | / | Effects aren't bad but inconsistent activation |
| Shooting Star | △ | ◯ | 2.5 | 200 | / | Consistent activation, but weak effect |
| The View from the Lead is Mine! | △ | △ | 2.5 | 200 | / | Somewhat consistent activation for Front Runners, but weak effect |
| Sky-High Teio Step | △ | ◎ | 2.5 | 200 | / | Mostly consistent for non-Front-Runners, with strong effect |
| Triumphant Pulse | △ | ◎ | 2.5 | 200 | / | Consistent for non-Front-Runners, with strong effect |
| Anchors Aweigh! | △ | ✕ | 2.5 | 200 | / | Consistent for Late Surgers/End Closers but minimal effect |
| Resplendent Red Ace | △ | ▲ | 2.5 | 200 | / | Accel can come in handy occasionally but still very situational and slightly unreliable |
| Where There's a Will, There's a Way | △ | △ | 2.5 | 200 | / | Decent speed skill option for non-Front-Runners |
| The Duty of Dignity Calls | △ | ◯ | 2.5 | 200 | / | Final Corner Target Speed boost is inconsistent (especially in Med race), but it can be situationally good for Front Runners/Pace Chasers |
| Victoria por plancha ☆ | △ | ◎ | 2.5 | 200 | / | Activation is mostly consistent, some tracks benefit from a Last Straight accel |
| This Dance Is for Vittoria! | △ | ◯ | 2.5 | 200 | / | Fairly consistent activation but Final Corner Target Speed boost could be inconsistent |
| Behold Thine Emperor's Divine Might | △ | ◎ | 2.5 | 200 | / | Consistent for non-Front-Runners, with strong effect |
| Blazing Pride | △ | ◯ | 2.5 | 200 | / | Final Corner Target Speed boost is inconsistent (especially in Med race), but it can be situationally good for Late Surgers |
| ∴win Q.E.D. | △ | ◯ | 2.5 | 200 | / | Final Corner Target Speed boost is inconsistent (especially in Med race), but it can be situationally good for Front Runners |
| Flashy☆Landing | △ | ◯ | 2.5 | 200 | / | Acceleration on and beyond Final Corner is decent, conditions to activate may not be consistent unless you're Front Runner or Pace Chaser |
| Blue Rose Closer | △ | △ | 2.5 | 200 | / | Consistent, but weak effect |
| Our Ticket to Win! | △ | △ | 2.5 | 200 | / | Side block on Last Straight is rare, weak effect as well makes it not worth getting |
| Just a Little Farther! | △ | ✕ | 2.5 | 200 | / | Fairly consistent, but also weak |
| #LookatCurren | △ | △ | 2.5 | 200 | / | Slightly consistent but effect is really weak since it usually activates at Mid-Race |
| Nemesis | △ | ◯ | 2.5 | 200 | / | Consistent for Late Surgers/End Closers but effect is weak |
| SPARKLY☆STARDOM | △ | ▲ | 2.5 | 200 | / | Mostly consistent for most Front Runners and helps them maintain their lead |
| Shadow Break | △ | ◯ | 2.5 | 200 | / | Should be consistent but effect isn't great enough to be used over other similar uniques |
| Eternal Moments | △ | △ | 2.5 | 200 | / | Fairly consistent for non-Front-Runners, but the effect is weak |
| Flowery☆Maneuver | △ | ▲ | 2.5 | 200 | / | ① Strong for Front/Pace on some tracks to carry over speed on final corner<br>② Strong for Late/End on tracks that start the Last Spurt on final corner |
| You and Me! One-on-One! | △ | △ | 2.5 | 200 | / | Decent Last Straight speed skill for Late Surgers or End Closers |
| Lights of Vaudeville | △ | ◯ | 2.5 | 200 | / | Consistent activation but effectiveness depends on track |
| A Kiss for Courage | △ | △ | 2.5 | 200 | / | Varying effectiveness depending on track but can be strong with Triple 7s activation |
| I Never Goof Up! | △ | ◯ | 2.5 | 200 | / | Good effect but rng and track dependent |
| Bountiful Harvest | △ | △ | 2.5 | 200 | / | Consistent but relatively weak |
| YUMMY☆SPEED! | △ | ✕ | 2.5 | 200 | / | Unfortunate timing at 60% of the Race makes this skill's acceleration practically useless |
| OMG! (ﾟ∀ﾟ) The Final Sprint! ☆ | △ | △ | 2.5 | 200 | / | Generally, when you overtake in Late-Race, you're still accelerating, so a Target Speed skill wouldn't be effective |
| Give Mummy a Hug ♡ | △ | ◯ | 2.5 | 200 | / | Good accel for tracks that have their Last Spurt Mode begin on/near a Last Straight |
| Chasing After You | △ | △ | 2.5 | 200 | / | Very weak effect but can be used as a debuff |
| Arrows Whistle, Shadows Disperse | △ | ◯ | 2.5 | 200 | / | Consistent, but weak effect |
| Pop & Polish | △ | ◯ | 2.5 | 200 | / | Consistent, but weak effect |
| Presents from X | △ | △ | 2.5 | 200 | / | Consistent, but weak effect |
| Festive Miracle | △ | ◯ | 2.5 | 200 | / | Strong on some tracks where Triple 7s can proc before the Last Spurt |
| Fairy Tale | △ | △ | 2.5 | 200 | / | Strong on some tracks where Triple 7s can proc before the Last Spurt |
| Straightaway Recovery | △ | △ | 2.94 | 170 | / | Inconsistent, it might be wasted on an early or late activation |
| Breath of Fresh Air | △ | △ | 3.53 | 170+170 | / | Inconsistent, it might be wasted on an early or late activation |
| Lay Low | △ | ✕ | 3.12 | 160 | / | Might proc in Early-Race which might overflow HP |
| Iron Will | △ | ✕ | 3.75 | 160+160 | / | Might proc in Early-Race which might overflow HP |
| Pace Strategy | △ | ✕ | 2.94 | 170 | / | Being overtaken is an inconsistent condition<br>More suitable on long, backline Run Styles |
| Indomitable | △ | ✕ | 3.53 | 170+170 | / | Being overtaken is an inconsistent condition<br>More suitable on long, backline Run Styles |
| Triple 7s | △ | ▲ | 3.12 | 160 | / | Consistent, but only effective on <2400m tracks, useful for some Uma that rely on Stamina skill procs |
| Shake It Out | △ | ✕ | 5 | 100 | / | Late-Race recovery is ineffective<br>consider acquiring it only for Team Trials because it's very cheap |
| Ignited Spirit STA | △ | △ | 2.5 | 200 | / | Definitely an option but it costs more than a usual skill (at 200 base SP) |
| Burning Spirit STA | △ | △ | 3 | 200+200 | / | Definitely an option but it costs more than a usual skill (at 200 base SP) |
| Deep Breaths | △ | △ | 3.12 | 160 | Long | Inconsistent, it might be wasted on an early or late activation |
| Cooldown | △ | △ | 3.75 | 160+160 | Long | Inconsistent, it might be wasted on an early or late activation |
| Extra Tank | △ | △ | 3.12 | 160 | Long | If your HP drops to zero, you're cooked anyway, no recovery can save you |
| Adrenaline Rush | △ | △ | 3.75 | 160+160 | Long | If your HP drops to zero, you're cooked anyway, no recovery can save you |
| Passing Pro | △ | △ | 3.12 | 160 | Long | Mostly consistent but activation can occur on Early-Race, diminishing its value |
| U=ma2 | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Pure Heart | △ | △ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Super-Duper Climax | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Superior Heal | △ | △ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Dazzl'n ♪ Diver | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Every Rose Has Its Fangs | △ | ✕ | 2.5 | 200 | / | They cost a whopping 200 SP for 1.5% recovery<br>It's more worth to inherit other uniques<br>The only exceptions right now are Super Creek's and Grass Wonder (Fantasy)'s |
| Corner Acceleration ◯ | △ | ✕ | 2.78 | 180 | / | Acceleration on the Corner 1/First Corner of any track is useless |
| Corner Connoisseur | △ | ✕ | 3.33 | 180+180 | / | Acceleration on the Corner 1/First Corner of any track is useless |
| Straightaway Acceleration | △ | ✕ | 2.94 | 170 | / | Random straight activations are too inconsistent to be effective |
| Rushing Gale! | △ | ✕ | 3.53 | 170+170 | / | Random straight activations are too inconsistent to be effective |
| Highlander | △ | ◎ | 3.12 | 160 | / | Very powerful on tracks with Uphills right before/as Last Spurt Mode begins |
| Groundwork | △ | ▲ | 5 | 100 | / | For Front Runners only, use with 3 Early-Race skills like Focus/Concentration+Green Skills |
| KEEP IT REAL. | △ | ✕ | 2.5 | 200 | / | Mostly useless accel but consistent activation |
| Moving Past, and Beyond | △ | ✕ | 2.5 | 200 | / | Mostly useless accel but consistent activation |
| Prudent Positioning | △ | ▲ | 4.17 | 120 | / | Use with Dodging Danger for a very powerful Early-Race burst of speed (Front Runner only) |
| Center Stage | △ | ✕ | 5 | 120+120 | / | Never use for Front-Runners that want to run the Dodging Danger tech |
| Go with the Flow | △ | ✕ | 4.17 | 120 | / | Random non-Early-Race Lane Movement Speed for non-Front-Runners are useless<br>Take only because they are very cheap and if you have no other options |
| Lane Legerdemain | △ | ✕ | 5 | 120+120 | / | Random non-Early-Race Lane Movement Speed for non-Front-Runners are useless<br>Take only because they are very cheap and if you have no other options |
| Ignited Spirit WIT | △ | ▲ | 2.5 | 200 | / | Use with Dodging Danger for a very powerful Early-Race burst of speed (Front Runner only) |
| Burning Spirit WIT | △ | ✕ | 3 | 200+200 | / | Never use for Front-Runners that want to run the Dodging Danger tech |
| Smoke Screen | △ | △ | 4.55 | 110 | Long | Random Point in Late-Race |
| Illusionist | △ | △ | 5.45 | 110+110 | Long | Random Point in Late-Race |
| [Location] Racecourse ◯ | △ | ◎ | 5.56 | 90 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| [Ground Condition] Conditions ◯ | △ | ◎ | 5.56 | 90 | / | Power Stat increase is decent but low priority |
| [Weather] Days ◯ | △ | △ | 5.56 | 90 | / | Guts is extremely unimportant, only take it you really need to |
| [Run Style] Savvy ◎ | △ | ▲ | 2.08 | 110+130 | [Run Style] | Consistent activation, FoV buff is useful for Nice Nature's All-Seeing Eyes |

##### ✕ Avoid (Team Trials): 35 skills

| Skill | Team Trials | PvP | Score/SP | Base Cost | Distance/Run Style | Why? |
|---|---|---|---|---|---|---|
| Risky Business | ✕ | ✕ | 4.17 | 120 | / | This skill can completely kill your stamina, it's definitely not worth it unless you're trying to do some niche strat |
| Cut and Drive! | ✕ | ✕ | 2.5 | 200 | / | Not the most consistent, and also a weak effect, not worth taking |
| G00 1st. F∞; | ✕ | △ | 2.5 | 200 | / | 0.15m/s but has two additional checks (for Start Delay and Rushed) |
| Genius x Bakushin = Victory | ✕ | △ | 2.5 | 200 | / | Fairly consistent, but also weak |
| I See Victory in My Future! | ✕ | ✕ | 2.5 | 200 | / | Front Block condition is downright horrible |
| Prideful King | ✕ | ✕ | 2.5 | 200 | / | Extremely inconsistent, if not totally impossible to even activate in any distance but Sprint |
| Schwarzes Schwert | ✕ | △ | 2.5 | 200 | / | 0.15m/s but requires two additional checks (for Start Delay and Rushed) |
| A Princess Must Seize Victory! | ✕ | ✕ | 2.5 | 200 | / | Side block condition on the Last Straight is quite strict and difficult to proc |
| Dancing in the Leaves | ✕ | ✕ | 2.5 | 200 | / | Side Block isn't consistent, effect isn't outstanding either |
| Calm in a Crowd | ✕ | ✕ | 2.94 | 170 | / | Almost impossible to be boxed in on all sides in CM |
| Unruffled | ✕ | ✕ | 3.53 | 170+170 | / | Almost impossible to be boxed in on all sides in CM |
| [Rotation]-Handed ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Speed stat increase is significant |
| [Season] Runner ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Speed stat increase is significant |
| Fall Frenzy | ✕ | ✕ | 3.64 | 90+110+130 | / | Take only on Autumn CMs |
| Outer Post Proficiency ◯ | ✕ | ✕ | 5.56 | 90 | / | Post Numbers 6-8 is inconsistent |
| Outer Post Proficiency ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Post Numbers 6-8 is inconsistent |
| Maverick ◯ | ✕ | ✕ | 5.56 | 90 | / | Very rare to have no Umas use your run style |
| Maverick ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Very rare to have no Umas use your run style |
| Long Shot ◯ | ✕ | ✕ | 5.56 | 90 | / | Popularity-dependent skills are inconsistent |
| Long Shot ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Popularity-dependent skills are inconsistent |
| Sympathy | ✕ | ▲ | 7.14 | 70 | / | Practically impossible to proc |
| [Location] Racecourse ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Yodo Invicta | ✕ | ✕ | 3.64 | 90+110+130 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Standard Distance ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| Non-Standard Distance ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Stamina stat increase is good but not completely necessary unless you're short of stamina |
| [Ground Condition] Conditions ◎ | ✕ | ◎ | 2.5 | 90+110 | / | Power Stat increase is decent but low priority |
| Competitive Spirit ◯ | ✕ | ✕ | 5.56 | 90 | / | It's unlikely for 40% of the lobby to use the same run style as you |
| Competitive Spirit ◎ | ✕ | ✕ | 2.5 | 90+110 | / | It's unlikely for 40% of the lobby to use the same run style as you |
| [Weather] Days ◎ | ✕ | △ | 2.5 | 90+110 | / | Guts is extremely unimportant, only take it you really need to |
| Target in Sight ◯ | ✕ | ✕ | 5.56 | 90 | / | Guts is extremely unimportant, only take it you really need to |
| Target in Sight ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Guts is extremely unimportant, only take it you really need to |
| Inner Post Proficiency ◯ | ✕ | ✕ | 5.56 | 90 | / | Post Numbers 1-3 is inconsistent |
| Inner Post Proficiency ◎ | ✕ | ✕ | 2.5 | 90+110 | / | Post Numbers 1-3 is inconsistent |
| Lucky Seven | ✕ | ✕ | 4.55 | 110 | / | Inconsistent, even more so than the Post Proficiency skills |
| Super Lucky Seven | ✕ | ✕ | 5.45 | 110+110 | / | Inconsistent, even more so than the Post Proficiency skills |

##### Quick view: skills grouped by PvP tier

- **⍟ Essential (8):** [Run Style] Corners ◯; [Run Style] Straightaways ◯; [Distance] Corners ◯; [Distance] Straightaways ◯; [Run Style] Corners ◎; [Run Style] Straightaways ◎; [Distance] Corners ◎; [Distance] Straightaways ◎
- **◎ Top tier (44):** Uma Stan; Super Stan; Tail Held High; Slipstream; Playtime's Over!; Burning Spirit GUTS; Corner Recovery ◯; Swinging Maestro; Ignited Spirit PWR; Burning Spirit PWR; Hesitant [Run Style]s; Subdued [Run Style]s; Flustered [Run Style]s; Trick (Front); Tantalizing Trick; Trick (Rear); Stamina Siphon; Lone Wolf; Ignited Spirit GUTS; Nimble Navigator; No Stopping Me!; Frenzied [Run Style]s; Stamina Eater; [Rotation]-Handed ◯; [Season] Runner ◯; Standard Distance ◯; Non-Standard Distance ◯; Shooting for Victory!; Let's Pump Some Iron!; Angling and Scheming; Certain Victory; Sky-High Teio Step; Triumphant Pulse; Victoria por plancha ☆; Behold Thine Emperor's Divine Might; Highlander; [Location] Racecourse ◯; [Ground Condition] Conditions ◯; [Rotation]-Handed ◎; [Season] Runner ◎; [Location] Racecourse ◎; Standard Distance ◎; Non-Standard Distance ◎; [Ground Condition] Conditions ◎
- **◯ Good (19):** [Run Style] Savvy ◯; Professor of Curvature; Beeline Burst; It's On!; In Body and Mind; Shooting Star; The Duty of Dignity Calls; This Dance Is for Vittoria!; Blazing Pride; ∴win Q.E.D.; Flashy☆Landing; Nemesis; Shadow Break; Lights of Vaudeville; I Never Goof Up!; Give Mummy a Hug ♡; Arrows Whistle, Shadows Disperse; Pop & Polish; Festive Miracle
- **▲ Situational (11):** Focus; Concentration; Resplendent Red Ace; SPARKLY☆STARDOM; Flowery☆Maneuver; Triple 7s; Groundwork; Prudent Positioning; Ignited Spirit WIT; [Run Style] Savvy ◎; Sympathy
- **△ Low priority (40):** Corner Adept ◯; Straightaway Adept; Ramp Up; Homestretch Haste; Ignited Spirit SPD; Burning Spirit SPD; Keeping the Lead; Vanguard Spirit; Legacy of the Strong; The View from the Lead is Mine!; Where There's a Will, There's a Way; Blue Rose Closer; Our Ticket to Win!; #LookatCurren; Eternal Moments; You and Me! One-on-One!; A Kiss for Courage; Bountiful Harvest; OMG! (ﾟ∀ﾟ) The Final Sprint! ☆; Chasing After You; Presents from X; Fairy Tale; Straightaway Recovery; Breath of Fresh Air; Ignited Spirit STA; Burning Spirit STA; Deep Breaths; Cooldown; Extra Tank; Adrenaline Rush; Passing Pro; Pure Heart; Superior Heal; Smoke Screen; Illusionist; [Weather] Days ◯; G00 1st. F∞;; Genius x Bakushin = Victory; Schwarzes Schwert; [Weather] Days ◎
- **✕ Avoid (52):** Red Shift/LP1211-M; Condor's Fury; Inside Scoop; Innate Experience; Pressure; Overwhelming Pressure; Anchors Aweigh!; Just a Little Farther!; YUMMY☆SPEED!; Lay Low; Iron Will; Pace Strategy; Indomitable; Shake It Out; U=ma2; Super-Duper Climax; Dazzl'n ♪ Diver; Every Rose Has Its Fangs; Corner Acceleration ◯; Corner Connoisseur; Straightaway Acceleration; Rushing Gale!; KEEP IT REAL.; Moving Past, and Beyond; Center Stage; Go with the Flow; Lane Legerdemain; Burning Spirit WIT; Risky Business; Cut and Drive!; I See Victory in My Future!; Prideful King; A Princess Must Seize Victory!; Dancing in the Leaves; Calm in a Crowd; Unruffled; Fall Frenzy; Outer Post Proficiency ◯; Outer Post Proficiency ◎; Maverick ◯; Maverick ◎; Long Shot ◯; Long Shot ◎; Yodo Invicta; Competitive Spirit ◯; Competitive Spirit ◎; Target in Sight ◯; Target in Sight ◎; Inner Post Proficiency ◯; Inner Post Proficiency ◎; Lucky Seven; Super Lucky Seven


### 1.8 References

- Gametora: https://gametora.com/umamusume


---

## 2. Spark Procs and Lineage Planning

**Source:** Uma Musume: Spark Procs, created and maintained by @icedynamix on Discord.

### 2.1 Overview and Credits

This workbook answers one question: *how likely is a spark to trigger (proc) during an inspiration, and during a whole career?* It covers quick lookup tables, an affinity calculator, an extreme-aptitude planner, and a fully custom calculator for exact lineages.

| Item | Detail |
|---|---|
| Creator / maintainer | @icedynamix on Discord (support on Ko-fi is welcome) |
| Discussion | Victoria Frontier Discord server |
| Info sources | Crazyfellow's Parenting & Gene guide; Affinity Scaling by @BourBon_Polaris; Empirical Evidence for Base Chances by @BourBon_Polaris; u-tools announcements |

**Overview changelog**

| Date | Change |
|---|---|
| 2025-08-28 | Added a note about the affinity estimate in the "affinity assumptions" panel. |
| 2025-09-04 | Lowered the shared race count assumption from 10 to 5. |

### 2.2 Understanding Stars

- Sparks are evaluated **per spark**, not by the total star count. The stars of each spark set its chance.
- Strictly, one 2★ spark and two 1★ sparks are not the same. For a red spark the chance is 5.85% for a single 2★ and 3.86% for two 1★. The author judges the difference small enough to ignore, so the quick tables **count total stars and average across all possible splits**. In this example the average is 4.86%.
- You still need to tell **parent stars** apart from **grandparent stars**.
- If the difference matters to you, use the Full Custom Calculator (section 2.9).

### 2.3 Affinity Assumptions and Base Chances

The quick tables assume a fixed affinity. You can change the orange cells if you copy the sheet.

| Assumption | Value |
|---|---|
| Parent affinity (base) | 24 |
| Grandparent affinity (base) | 16 |
| Shared races/epithets | 5 |
| Resulting parent affinity score | 95 |
| Resulting grandparent affinity score | 21 |
| Resulting total affinity score | 161 |

The author calls this a decently high but reasonable estimate. If you have not planned your lineage or did not aim for shared races, you are very likely below it. Affinity scales the base chances, so lower affinity means fewer procs.

**Base chances differ by spark type, and are then scaled by affinity.** The table shows the base values per star count, and the values after scaling for the parent and grandparent affinity scores above.


| Spark type | Base 1★ | Base 2★ | Base 3★ | Parent 1★ | Parent 2★ | Parent 3★ | Grandparent 1★ | Grandparent 2★ | Grandparent 3★ |
|---|---|---|---|---|---|---|---|---|---|
| Blue | 70.0% | 80.0% | 90.0% | 100.00% | 100.00% | 100.00% | 84.70% | 96.80% | 100.00% |
| Red | 1.0% | 3.0% | 5.0% | 1.95% | 5.85% | 9.75% | 1.21% | 3.63% | 6.05% |
| Green | 5.0% | 10.0% | 15.0% | 9.75% | 19.50% | 29.25% | 6.05% | 12.10% | 18.15% |
| Skill | 3.0% | 6.0% | 9.0% | 5.85% | 11.70% | 17.55% | 3.63% | 7.26% | 10.89% |
| Race | 1.0% | 2.0% | 3.0% | 1.95% | 3.90% | 5.85% | 1.21% | 2.42% | 3.63% |
| Scenario | 3.0% | 6.0% | 9.0% | 5.85% | 11.70% | 17.55% | 3.63% | 7.26% | 10.89% |


The *scaled* columns already include the affinity assumptions above.

### 2.4 Chance of at Least One Proc During a Career

Use these tables when you need a particular spark to trigger **at least once** during the career. Typical examples are an aptitude upgrade from A to S, or a specific skill from a white spark. Each cell is the probability for the combination of parent stars (rows) and grandparent stars (columns), using the affinity assumptions in section 2.3.

#### Red sparks

| Parent stars \ Grandparent stars | 0★ | 2★ | 4★ | 6★ | 8★ | 10★ | 12★ |
|---|---|---|---|---|---|---|---|
| 0★ | 0.00% | 5.94% | 12.11% | 19.56% | 26.19% | 32.84% | 39.30% |
| 1★ | 3.86% | 9.57% | 15.50% | 22.66% | 29.04% | 35.44% | 41.65% |
| 2★ | 9.47% | 14.84% | 20.43% | 27.17% | 33.17% | 39.20% | 45.05% |
| 3★ | 16.67% | 21.62% | 26.75% | 32.96% | 38.49% | 44.04% | 49.42% |
| 4★ | 21.56% | 26.22% | 31.06% | 36.90% | 42.10% | 47.32% | 52.39% |
| 5★ | 27.80% | 32.09% | 36.54% | 41.92% | 46.71% | 51.51% | 56.18% |
| 6★ | 33.66% | 37.60% | 41.69% | 46.63% | 51.03% | 55.45% | 59.73% |

#### Skill sparks

| Parent stars \ Grandparent stars | 0★ | 2★ | 4★ | 6★ | 8★ | 10★ | 12★ |
|---|---|---|---|---|---|---|---|
| 0★ | 0.00% | 13.87% | 25.93% | 36.50% | 45.53% | 53.43% | 60.24% |
| 1★ | 11.36% | 23.65% | 34.34% | 43.71% | 51.72% | 58.72% | 64.76% |
| 2★ | 21.73% | 32.59% | 42.02% | 50.30% | 57.36% | 63.55% | 68.88% |
| 3★ | 31.45% | 40.96% | 49.23% | 56.47% | 62.66% | 68.08% | 72.75% |
| 4★ | 39.47% | 47.87% | 55.17% | 61.57% | 67.03% | 71.81% | 75.94% |
| 5★ | 47.00% | 54.35% | 60.74% | 66.34% | 71.13% | 75.32% | 78.93% |
| 6★ | 53.79% | 60.20% | 65.77% | 70.65% | 74.83% | 78.48% | 81.63% |

#### Race sparks

| Parent stars \ Grandparent stars | 0★ | 2★ | 4★ | 6★ | 8★ | 10★ | 12★ |
|---|---|---|---|---|---|---|---|
| 0★ | 0.00% | 4.77% | 9.32% | 13.69% | 17.83% | 21.81% | 25.61% |
| 1★ | 3.86% | 8.45% | 12.82% | 17.02% | 21.01% | 24.83% | 28.48% |
| 2★ | 7.61% | 12.02% | 16.22% | 20.26% | 24.09% | 27.76% | 31.27% |
| 3★ | 11.29% | 15.52% | 19.55% | 23.43% | 27.11% | 30.64% | 34.00% |
| 4★ | 14.75% | 18.81% | 22.69% | 26.41% | 29.95% | 33.34% | 36.58% |
| 5★ | 18.14% | 22.04% | 25.77% | 29.34% | 32.74% | 35.99% | 39.10% |
| 6★ | 21.43% | 25.17% | 28.75% | 32.18% | 35.44% | 38.56% | 41.55% |

#### Green sparks

| Parent stars \ Grandparent stars | 0★ | 2★ | 4★ | 6★ |
|---|---|---|---|---|
| 0★ | 0.00% | 22.41% | 40.07% | 54.14% |
| 1★ | 58.62% | 67.89% | 75.20% | 81.02% |
| 2★ | 67.56% | 74.83% | 80.56% | 85.13% |
| 3★ | 74.94% | 80.56% | 84.98% | 88.51% |

> The Green table is smaller because the same Uma cannot be used for both parents, and the same Uma cannot appear more than twice among the grandparents.

> In the source, a stray "Scenario" label sits under the Race table's header. The figures match the Race base chances, so the table is shown as Race.

### 2.5 Average Number of Procs During a Career

Use these tables when you need **more than one** proc, for example an upgrade from B to S, or when you simply want to count blue sparks. Each cell is the expected (average) number of procs over the whole career.

#### Red sparks

| Parent stars \ Grandparent stars | 0★ | 2★ | 4★ | 6★ | 8★ | 10★ | 12★ |
|---|---|---|---|---|---|---|---|
| 0★ | 0.000 | 0.061 | 0.127 | 0.213 | 0.296 | 0.387 | 0.484 |
| 1★ | 0.039 | 0.100 | 0.166 | 0.252 | 0.335 | 0.426 | 0.523 |
| 2★ | 0.098 | 0.158 | 0.225 | 0.310 | 0.394 | 0.485 | 0.582 |
| 3★ | 0.176 | 0.236 | 0.303 | 0.388 | 0.472 | 0.563 | 0.660 |
| 4★ | 0.234 | 0.295 | 0.361 | 0.447 | 0.530 | 0.621 | 0.718 |
| 5★ | 0.312 | 0.373 | 0.439 | 0.525 | 0.608 | 0.699 | 0.796 |
| 6★ | 0.390 | 0.451 | 0.517 | 0.603 | 0.686 | 0.777 | 0.874 |

#### Blue sparks

| Parent stars \ Grandparent stars | 0★ | 2★ | 4★ | 6★ | 8★ | 10★ | 12★ |
|---|---|---|---|---|---|---|---|
| 0★ | 0.000 | 2.662 | 4.917 | 5.956 | 7.159 | 7.783 | 8.000 |
| 1★ | 2.000 | 4.662 | 6.917 | 7.956 | 9.159 | 9.783 | 10.000 |
| 2★ | 3.000 | 5.662 | 7.917 | 8.956 | 10.159 | 10.783 | 11.000 |
| 3★ | 3.000 | 5.662 | 7.917 | 8.956 | 10.159 | 10.783 | 11.000 |
| 4★ | 4.000 | 6.662 | 8.917 | 9.956 | 11.159 | 11.783 | 12.000 |
| 5★ | 4.000 | 6.662 | 8.917 | 9.956 | 11.159 | 11.783 | 12.000 |
| 6★ | 4.000 | 6.662 | 8.917 | 9.956 | 11.159 | 11.783 | 12.000 |

#### Race sparks

| Parent stars \ Grandparent stars | 0★ | 2★ | 4★ | 6★ | 8★ | 10★ | 12★ |
|---|---|---|---|---|---|---|---|
| 0★ | 0.000 | 0.048 | 0.097 | 0.145 | 0.194 | 0.242 | 0.290 |
| 1★ | 0.039 | 0.087 | 0.136 | 0.184 | 0.233 | 0.281 | 0.329 |
| 2★ | 0.078 | 0.126 | 0.175 | 0.223 | 0.272 | 0.320 | 0.368 |
| 3★ | 0.117 | 0.165 | 0.214 | 0.262 | 0.311 | 0.359 | 0.407 |
| 4★ | 0.156 | 0.204 | 0.253 | 0.301 | 0.350 | 0.398 | 0.446 |
| 5★ | 0.195 | 0.243 | 0.292 | 0.340 | 0.389 | 0.437 | 0.485 |
| 6★ | 0.234 | 0.282 | 0.331 | 0.379 | 0.428 | 0.476 | 0.524 |

#### Green sparks

| Parent stars \ Grandparent stars | 0★ | 2★ | 4★ | 6★ |
|---|---|---|---|---|
| 0★ | 0.000 | 0.242 | 0.484 | 0.726 |
| 1★ | 0.780 | 1.022 | 1.264 | 1.506 |
| 2★ | 0.975 | 1.217 | 1.459 | 1.701 |
| 3★ | 1.170 | 1.412 | 1.654 | 1.896 |

> The Green table is smaller for the same reason as above.


### 2.6 Affinity in Detail

**Core rules**

- Affinity is always measured between **two individual Umas**, not as a grand total. The triangle, circle and double-circle shown in the game are only a rough estimate.
- Every Uma in your lineage has its own proc chance, set by **its own** affinity. If one Uma has poor affinity with the others, her sparks proc less often.
- The score rises by **1 for every race** an Uma shares with a direct relative. Shared epithets also add 1.

**Definitions used for the formulas**

| Symbol | Meaning |
|---|---|
| aff(x, y) | Base affinity between x and y |
| race(x, y) | Number of shared race wins between x and y |
| p0 | The Uma being trained (the base) |
| p1, p2 | Direct parents |
| p1.1, p1.2, p2.1, p2.2 | Grandparents |

| Score | Formula |
|---|---|
| Parent 1 affinity | aff(p0, p1) + aff(p1, p2) + aff(p1, p1.1) + aff(p1, p1.2) + race(p1, p2) + race(p1, p1.1) + race(p1, p1.2) |
| Parent 2 affinity | Same as parent 1 with p1 and p2 swapped |
| Grandparent affinity (e.g. p1.1) | aff(p0, p1, p1.1) + race(p1, p1.1) |

To see how aff(x, y) and aff(x, y, z) are looked up, copy the spreadsheet and open the hidden `_affinity` sheet.

**Scaling.** Affinity scales the base chance like this:

> actual chance = base chance × (1 + affinity / 100)

So an affinity of 110 gives a **2.1×** multiplier on the chance.

**Distribution of base affinities in the game data.**


| Base affinity | Number of pairs | Number of triplets |
|---|---|---|
| 0 | 31 | 677 |
| 1 | 3 | 81 |
| 2 | 6 | 232 |
| 3 | 11 | 64 |
| 4 | 2 | 10 |
| 5 | 3 | 1 |
| 6 | 0 | 0 |
| 7 | 5 | 287 |
| 8 | 11 | 752 |
| 9 | 22 | 424 |
| 10 | 23 | 282 |
| 11 | 16 | 40 |
| 12 | 8 | 16 |
| 13 | 8 | 1 |
| 14 | 7 | 254 |
| 15 | 13 | 625 |
| 16 | 40 | 565 |
| 17 | 56 | 500 |
| 18 | 48 | 188 |
| 19 | 26 | 40 |
| 20 | 18 | 5 |
| 21 | 8 | 43 |
| 22 | 10 | 100 |
| 23 | 18 | 87 |
| 24 | 24 | 79 |
| 25 | 31 | 52 |
| 26 | 19 | 17 |
| 27 | 16 | 9 |
| 28 | 7 | 4 |
| 29 | 7 | 0 |
| 30 | 5 | 4 |
| 31 | 7 | 12 |
| 32 | 4 | 3 |
| 33 | 6 | 2 |
| 34 | 3 | 0 |
| 35 | 4 | 0 |
| 36 | 2 | 0 |
| 37 | 0 | 0 |
| 38 | 0 | 0 |
| 39 | 0 | 0 |


**Summary statistics**

| Statistic | Pairs | Triplets |
|---|---|---|
| Minimum | 0 | 0 |
| Average | 17.21 | 11.10 |
| Maximum | 39 | 752 |


**Percentiles**

| Percentile | Pairs | Triplets |
|---|---|---|
| 10th | 4.70 | 0 |
| 25th | 11 | 8 |
| 50th (median) | 17 | 10 |
| 75th | 24 | 16 |
| 90th | 27 | 18 |
| 95th | 30 | 22 |
| 99th | 34.73 | 25 |
| 99.95th |  | 32 |


**Estimating a realistic in-game score.** Three scenarios show what affinity to expect. (The source marks this part as "needs rework".)


| Scenario | Parent base affinity | Grandparent base affinity | Assumed shared races | Parent affinity score | Grandparent affinity score | In-game affinity score |
|---|---|---|---|---|---|---|
| "No idea what I'm doing" (randomly chosen Umas) | 17 (50th percentile) | 10 (50th percentile) | 3 | 63 | 13 | 106 |
| Reasonably chosen (reasonably compatible Umas) | 24 (75th percentile) | 16 (75th percentile) | 10 | 110 | 26 | 186 |
| Affinitymaxxing (really compatible Umas) | 30 (95th percentile) | 27 (99.5th percentile) | 15 | 159 | 42 | 273 |


**One of the most compatible groups.** Base affinities between TM Opera O, Biwa Hayahide, Super Creek and Mejiro McQueen:

| Uma 1 | Uma 2 | Uma 3 | Base affinity |
|---|---|---|---|
| TM Opera O | Biwa Hayahide | - | 37 |
| Biwa Hayahide | Super Creek | - | 35 |
| TM Opera O | Super Creek | - | 34 |
| TM Opera O | Biwa Hayahide | Mejiro McQueen | 34 |
| TM Opera O | Super Creek | Mejiro McQueen | 33 |
| TM Opera O | Biwa Hayahide | Super Creek | 33 |

With 20 shared races added, this lineage reaches these scores:

| Position | Uma | Affinity score |
|---|---|---|
| Parent | Biwa Hayahide | 199 |
| Parent | Super Creek | 195 |
| Grandparent | Super Creek | 53 |
| Grandparent | Mejiro McQueen | 54 |
| Grandparent | Mejiro McQueen | 53 |
| Grandparent | Biwa Hayahide | 53 |

The in-game affinity score for this lineage would be **339**. TM Opera O is the base Uma.


### 2.7 Extreme Aptitude Upgrades

Use this when you must lift an aptitude from a very low rank, for example to help Haru Urara win the Arima Kinen.

**Rules**

- Parents give an **initial aptitude upgrade for every 1, 4, 7 and 10 actual stars** they carry.
- An aptitude cannot be raised past **A** this way. The upgrade from A to S must happen during an inspiration.

**Initial aptitude upgrades and stat effects**

| Starting aptitude | After 1★ | After 4★ | After 7★ | After 10★ | Stat modifier (surface aptitude) | Stat modifier (distance aptitude) |
|---|---|---|---|---|---|---|
| G | F | E | D | C | -90% | -90% |
| F | E | D | C | B | -70% | -80% |
| E | D | C | B | A | -50% | -60% |
| D | C | B | A |  | -30% | -40% |
| C | B | A |  |  | -20% | -20% |
| B | A |  |  |  | -10% | -10% |
| A |  |  |  |  | 0% | 0% |

**Examples**

- **Taiki Shuttle, Medium E→A (to use as a Medium parent):** no need to rely on inspirations. Use 10★ worth of Medium. Alternatively, use 7★ worth of Medium and gamble on an inspiration.
- **Haru Urara, Arima Kinen:** two aptitudes must go from G to C, or ideally G to B. With 9★ Turf and 9★ Long shared equally, this reaches **Turf D and Long D**. D/D cripples power by −30% and speed by −40%. Even C/C is only barely playable, so the aim is to get one or both to B.

**Chance of an upgrade during the career (Urara).** Assumes affinity 40 on the parents and 15 on the grandparents.

| Scenario | Parents | Grandparents | Upgrade during career | Long distance | Turf | Both |
|---|---|---|---|---|---|---|
| 14★ scenario | Turf 3★ / Long 3★ | Turf 2★, Turf 2★, Long 2★, Long 2★ | D→C | 24.84% | 24.84% | 6.17% |
| 14★ scenario | Turf 3★ / Long 3★ | Turf 2★, Turf 2★, Long 2★, Long 2★ | D→B | 2.79% | 2.79% | 0.08% |
| 18★ scenario | Turf 3★ / Long 3★ | Turf 3★, Turf 3★, Long 3★, Long 3★ | D→C | 31.75% | 31.75% | 10.08% |
| 18★ scenario | Turf 3★ / Long 3★ | Turf 3★, Turf 3★, Long 3★, Long 3★ | D→B | 4.82% | 4.82% | 0.23% |

The first scenario is a 14★ setup (3★ Turf and 3★ Long parents, with 2★ grandparents); the second is an 18★ setup (all 3★).


### 2.8 Lineage Planning (Work in Progress)

This tab is unfinished in the source. It notes that the spark generation chance follows the formula **c × (1.1)^n**, and links to a post by @aoneko_pochi (https://x.com/aoneko_pochi/status/1762370579603304731). The author plans to cover the topic in an upcoming video series.


### 2.9 Full Custom Calculator

The *Full Custom Calculation* tab is the "real deal": it holds the exact formula for anything you might want to compute. The sections below explain how to use it.


#### 2.9.1 How to Use the Calculator

1. **Copy the sheet first.** The original is view-only, so you must make your own copy before you can enter data.
2. **Step 1: Enter your lineage.** Fill in the base Uma, both parents, and the grandparents. Each Uma has room for **20 white sparks**.
3. **Step 2: Enter the races your Umas ran.** Tick the races each Uma won. Winning the same race in different years counts as **one** race.
4. **Read the outputs.** The most important numbers are the **purple** ones, because they directly scale your percentage chance.

#### 2.9.2 Tips and Limitations

| Topic | Note |
|---|---|
| Pasting values | Use **Ctrl+Shift+V** (paste values only), not plain Ctrl+V. |
| Scrolling | Hold **Shift + scroll** to move sideways through the sheet. |
| Fake sparks | Some listed "sparks" do not exist in game, such as gold skills and the debuff (purple) versions of certain skills. They were not filtered out, so use common sense. |
| Uma versions | The sheet does not distinguish between versions of the same Uma (for example, original Teio vs. anime Teio). This matters for green sparks, because the versions have different unique skills. |
| Affinity data | Taken directly from the Global version. Future Umas are **not** included, even if you can select them. |
| Race bonuses | URA races are excluded from the affinity calculation because they do not count. |
| Epithets | These apply automatically. The list may be incomplete. |
| Grandparent depth | The calculator's sample view omits great-grandparents (g2 and g3) for brevity. |

#### 2.9.3 Color Key for Affinity Calculation

| Color | Meaning |
|---|---|
| Blue | Base affinity |
| Red | Shared race bonus |
| Purple | The final chance values you care about most |

#### 2.9.4 Output Modes

| Mode | Use it when |
|---|---|
| Single proc fishing | You need **just one** proc during the career. |
| Multiple procs | You need **more than one** proc during the career. |
| Single spark, detailed analysis | You want a full breakdown for one chosen spark. |

Typical use cases mentioned for the calculator include aptitude upgrades (such as A to S), extreme aptitude upgrades, grandparent unique procs, and white spark skill drops.

#### 2.9.5 Race List Used for Affinity

The calculator tracks these races for the shared-race affinity bonus.

| Year | Races |
|---|---|
| Year 1 | Asahi Hai Futurity Stakes, Hanshin Juvenile Fillies, Hopeful Stakes |
| Year 2 | Oka Sho, Satsuki Sho, NHK Mile Cup, Japanese Oaks, Tokyo Yushun (Japanese Derby), Yasuda Kinen, Takarazuka Kinen, Japan Dirt Derby, Sprinters Stakes, Kikuka Sho, Shuka Sho, Tenno Sho (Autumn), JBC Classic, JBC Ladies' Classic, JBC Sprint, Queen Elizabeth II Cup, Japan Cup, Mile Championship, Champions Cup, Arima Kinen, Tokyo Daishoten |
| Year 3 | Kawasaki Kinen, February Stakes, Osaka Hai, Takamatsunomiya Kinen, Tenno Sho (Spring), Victoria Mile, Teio Sho |

**Epithets (applied automatically):** Classic Triple Crown, Triple Tiara, Senior Spring Triple Crown, Senior Autumn Triple Crown, Tenno Sweep.

#### 2.9.6 Worked Example (Sample Lineage in the Sheet)

The sheet ships with a demo lineage. It is useful for seeing how the inputs and outputs fit together.

**Base Uma:** Seiun Sky

| Role | Uma | Blue spark | Red spark | Green spark | Affinity |
|---|---|---|---|---|---|
| Parent 1 | Special Week | Stamina 2★ | Mile 2★ | Special Week Unique 2★ | 123 |
| Parent 2 | Silence Suzuka | Stamina 2★ | Mile 2★ | Silence Suzuka Unique 2★ | 106 |
| Grandparent 1.1 | Tokai Teio | Stamina 2★ | Mile 2★ | Tokai Teio Unique 2★ | 25 |
| Grandparent 1.2 | Gold Ship | Stamina 2★ | Pace Chaser 2★ | Gold Ship Unique 2★ | 33 |
| Grandparent 2.1 | Maruzensky | Stamina 2★ | Front Runner 2★ | Maruzensky Unique 2★ | 25 |
| Grandparent 2.2 | Daiwa Scarlet | Stamina 2★ | Mile 2★ | Daiwa Scarlet Unique 2★ | 24 |

The in-game affinity display for this lineage reads **196 (◎)**.

##### Base Chance per Spark

| Type | Spark | Chance per inspiration | Chance per career |
|---|---|---|---|
| Blue | Stamina | 100.00% | 100.00% |
| Green | Special Week Unique | 22.30% | 39.63% |
| Green | Silence Suzuka Unique | 20.60% | 36.96% |
| Red | Mile | 18.87% | 34.19% |
| Green | Gold Ship Unique | 13.30% | 24.83% |
| Green | Maruzensky Unique | 12.50% | 23.44% |
| Green | Tokai Teio Unique | 12.50% | 23.44% |
| Green | Daiwa Scarlet Unique | 12.40% | 23.26% |
| Red | Pace Chaser | 3.99% | 7.82% |
| Red | Front Runner | 3.75% | 7.36% |

##### Detailed Analysis: Red Mile Spark

Per-Uma chance of passing on the spark, per inspiration:

| Uma | Stars | Affinity | Chance |
|---|---|---|---|
| Parent 1 (Special Week) | 2★ | 123 | 6.69% |
| Grandparent 1.1 (Tokai Teio) | 2★ | 25 | 3.75% |
| Parent 2 (Silence Suzuka) | 2★ | 106 | 6.18% |

Overall results for this spark:

| Result | Per inspiration | Per career |
|---|---|---|
| Average procs | 0.20 | 0.41 |
| At least 1 | 18.87% | 34.19% |
| Exactly 0 | 81.13% | 65.81% |
| Exactly 1 | 17.46% | 28.32% |
| Exactly 2 | 1.37% | 5.27% |
| Exactly 3 | 0.05% | 0.55% |
| Exactly 4 | 0.00% | 0.04% |
| Exactly 5 to 8 | 0.00% | 0.00% |

> These figures come from the sample lineage. Your own numbers will differ once you enter your lineage.

#### 2.9.7 Calculator Changelog

| Date | Change |
|---|---|
| 2025-08-25 | Added shared epithets to the affinity calculation. |
| 2025-08-25 | Removed URA races from the affinity calculation, since they do not count. |
| 2025-09-09 | Fixed an incorrect Triple Tiara epithet formula (found by @nyanpasu7961). |
| 2025-09-09 | Added Seiun Sky affinity values. |

### 2.10 Other Calculator Tabs

- **Full Input** is a compact table-view calculator. Enter parent and grandparent stars for stats, surface, distance, strategy, green, URA Finale and white sparks, and it reports the chance of 0 to 12 procs per inspiration and per run, plus the chance of at least one and the average.
- **Urara** is a distribution sheet for the Haru Urara plan in section 2.7. It uses the affinity values from the Overview tab.
- **Complete Distribution Table** shows how the "square" tables above are calculated. Its author warns that anyone who does not know what they are looking at (and is not a "massive nerd") should not be there. It is left out of this guide because of its size.


---

## 3. Support Card Encyclopedia

**Source:** Luh's Umamusume Support Card Encyclopedia. Latest update: 29/06/26. Questions go to Luh on Discord (@luhsu).

### 3.1 Disclaimers

- Everything is based on the author's **subjective opinions**, so treat it with a grain of salt. Errors are possible.
- Pull suggestions reflect a card's value **at the time it is listed**. Personal favorites (oshi) and off-meta picks are set aside.

### 3.2 Scenarios Covered

| # | Scenario | Sheet |
|---|---|---|
| 1 | URA | URA |
| 2 | Unity Cup | Unity |
| 3 | Make a New Track!! (Trackblazer) | Trackblazer |
| 4 | Grand Live | GL |
| 5 | Grand Masters | GM |
| 6 | Project L'Arc | L'Arc |
| 7 | U.A.F. Ready Go! | U.A.F. |
| 8 | Great Food Festival! | GFF |
| 9 | Run, Mecha Umamusume! | MEKA |
| 10 | The Twinkle Legends | TL |
| 11 | Design Your Island | DYI |
| 12 | Yukoma Hot Springs | YHS |
| 13 | Beyond Dreams | BD |
| 14 | TBA: Welcome to Tracen-ken! | Not yet released |

### 3.3 Understanding Cards

This part explains what the numbers on a card mean, so you can build your own pull criteria.

**Card types.** There are seven types: one for each stat (Speed, Stamina, Power, Guts, Wit) plus **Pal** and **Group** cards. Each card allows friendship (rainbow) training on its own stat. Group cards have friendship training on Wit, and Pal cards have none. Cards also carry passive bonuses, support hints and event hints.

| Rarity | What it has |
|---|---|
| R | Skill hints and random events only |
| SR | Both, plus 2-chain events |
| SSR | Both, plus 3-chain events |

**Hints**

- **Support hints** give a chance at skill discounts or extra stats when the card's icon appears on a training facility. Their frequency comes from Hint Frequency %, and Hint Levels give more hints per appearance (2 hints at level 1, 3 at level 2, up to 5 at level 4).
- **Event hints** are fixed by the card's events. Random events are shared across all rarities of the same Uma (R Silence Suzuka has the same random events as SSR Silence Suzuka), while chain events are unique to each SR or SSR card.
- SSR cards add **3-chain events**, and the last event usually gives a gold skill. Some cards use a gamble ("coinflip") where you may get the white version instead. Coinflips have a hidden stat check: for example, Special Week SSR is more likely to give Gourmand if you have 1000+ speed.

**Passive bonuses** raise your stats throughout a run. They can change how much you get from mood, training and rainbows, from post-race and goal bonuses, from fans, and from a card's chance to appear at its facility. Some also reduce energy cost or protect against failure.

| Bonus | What it does | How a unique passive combines |
|---|---|---|
| Friendship Bonus | Amplifies stats from rainbow training. Applies only at orange bond, with the card on its own facility. | Multiplicative. Sweep Tosho SSR has 35% at MLB; her 10% unique makes it 48.5%. |
| Mood Effect | Boosts the existing mood bonuses (great: +20% training stats and +4% race bonus; good: +10% and +2%; bad: −10% and −2%; awful: −20% and −4%). Applied multiplicatively, so a 30% Mood Effect turns +20% into +26%. It also worsens bad moods (−10% becomes −13%). | Additive. Winning Ticket SSR has 30% at MLB; her 10% unique makes it 45%. |
| Training Effectiveness | Adds extra stats to every training done with the card, on any facility. | Additive. Daiwa Scarlet SSR has 5% at MLB; her 5% unique makes it 10%. |
| Stat Bonus +x | A flat +x to a stat's base training gain before other bonuses (or to skill points). Mejiro Ryan SSR's Power +1 and Guts +1 add +1 base power on Speed, Power or Guts training, and +1 base guts on Stamina or Guts training. | - |
| Specialty Priority | Raises the chance the card lands on its own facility. Each card has weight 100 for each of the 5 facilities and 50 for none, so at 0 priority it has a 100/550 (18.18%) chance per facility and 50/550 (about 9%) of not appearing. | Multiplicative. Vodka SSR has 65 at MLB and +20% from her unique: [(100+65) × 1.2] / 550 = 36% per turn on Power. |
| Race Bonus | Raises rewards after races (skill points, and stats on a win) and after career goals, including URA Qualifier, Semifinals and Final stat gains. | - |
| Fan Bonus | Raises fans gained from races. | - |
| Initial Stat +x | A flat +x to that stat at the start of a run. | - |
| Initial Friendship Gauge +x | A flat +x to the card's friendship gauge, so fewer turns are needed to reach orange bond. | - |
| Wit Friendship Recovery | A Wit and Group card bonus that raises energy recovered in friendship training. Group cards usually have +2, SRs +4 (except Ikuno Dictus SR) and SSRs +5 (except Matikanetannhauser SSR). | - |
| Event Recovery / Event Effectiveness | Percentage increases to a Pal card's events (energy, stats and skill points). | - |
| Energy Cost Reduction / Failure Protection | Percentage reductions in training energy cost and failure chance. Usually on Pal cards, except Matikanefukukitaru SSR. | - |

**The "trifecta".** Training Effectiveness, Mood Effect and Friendship Bonus combine by multiplication. Example: Kitasan Black SSR at MLB has 5% unique Training Effectiveness, 10% Training Effectiveness, 30% Mood Effect and 25% Friendship Bonus. In Great mood that is 15% training effectiveness, 26% mood bonus and 25% friendship bonus, so 1.15 × 1.26 × 1.25 = 1.81, or 81% extra stats on your base speed training.

### 3.4 What Makes a Card Good

Every card has some niche. Japanese-server players used to joke that Air Shakur SSR was the only card worth pulling for, but today she is the only card that gives a guaranteed Straightaway Spurt hint from an event chain. Every account differs: some players have Kitasan Black, Super Creek and Fine Motion at MLB, others have a few SRs, and some have everything maxed. All of them share one problem, which is not knowing what to bring in each deck. You do not want Super Creek in a Mile deck, more than four speed cards for an Uma with 20% speed growth, or an SSR when you own a better SR.

**Worked example: Kitasan Black (bonuses by limit break).** The unique passive stays fixed; the other bonuses rise until 3LB, then Specialty Priority jumps.


| Limit break | Unique bonus | Friendship Bonus | Training Effectiveness | Mood Effect | Race Bonus | Initial Friendship Gauge | Other |
|---|---|---|---|---|---|---|---|
| 0LB | 5% Training Eff. + 20 Specialty Priority | 20% | 5% | 20% | 5% | 25 | - |
| 1LB | same | 21% | 6% | 23% | 5% | 27 | Power Bonus +1 |
| 2LB | same | 23% | 8% | 26% | 5% | 30 | Power Bonus +1 |
| 3LB | same | 25% | 10% | 30% | 5% | 32 | Power Bonus +1, Specialty Priority 40 |
| MLB | same | 25% | 10% | 30% | 5% | 35 | Power Bonus +1, Specialty Priority 80 |


**What that means in practice.** Assume five turns of Speed training with 0% speed and power growth, URA Finale, facility level 1 (+10 speed, +5 power), friendship already unlocked (bond 80+), Great mood, and ignoring energy.


| Limit break | Chance to land on Speed each turn | Total multiplier | Gain per Speed training (speed / power) | 5 turns | 4 turns | 3 turns | 2 turns | 1 turn | 0 turns |
|---|---|---|---|---|---|---|---|---|---|
| 0LB | 21.81% (120/550) | 1.2 × 1.1 × 1.24 = 1.6378 | 16 / 8 | 0.05% | 0.93% | 6.3% | 22.7% | 40.8% | 29.2%* |
| 1LB | 21.81% | 1.21 × 1.11 × 1.246 = 1.6735 | 17 / 10 | 0.05% | 0.93% | 6.3% | 22.7% | 40.8% | 29.2%* |
| 2LB | 21.81% | 1.23 × 1.13 × 1.252 = 1.7401 | 17 / 10 | 0.05% | 0.93% | 6.3% | 22.7% | 40.8% | 29.2%* |
| 3LB | 30.55% ((100+40) × 1.2 / 550) | 1.25 × 1.15 × 1.26 = 1.8113 | 18 / 11 | 0.27% | 3% | 13.75% | 31.3% | 35.5% | 16.2% |
| MLB | 39.27% ((100+80) × 1.2 / 550) | 1.25 × 1.15 × 1.26 = 1.8113 | 18 / 11 | 0.93% | 7.2% | 22.3% | 34.5% | 26.7% | 8.3% |


\* The source prints 41.6% in these three cells, but the row would then exceed 100%. The binomial calculation for 21.81% gives about 29.2%, which is shown here.

Reading the table: from 0LB to 2LB the stats rise by about 10%, but Speed training with Kitasan is still unreliable. From 2LB to 3LB stats rise another 7% (17.35% in total from 0LB), and the chance of no Speed training drops by about 25%. From 3LB to MLB the stats stay the same, but the chance of no Speed training falls by about 33% from 0LB, and longer streaks surge: five straight turns of Speed is almost 19 times more likely than at 0LB. In short, Kitasan is a good card on numbers alone: consistent, high value with or without rainbow, and inside or outside friendship training.

**Skills matter too.** Gold skills on SSR cards are a large part of their value. Super Creek is the standard example: besides strong bonuses (15% Training Effectiveness, 37.5% Friendship Bonus and 10% Race Bonus at MLB) she brings one of the best recoveries on any track, Swinging Maestro.

- **Generalist cards** are good everywhere, such as Super Creek, Kitasan Black, Yukino Bijin, Matikanetannhauser and Tokai Teio.
- **Specialist cards** focus on a style or track type, such as Mr. C.B. (End Closers), Maruzensky (Front Runners), Nice Nature (Late Surgers), Agnes Tachyon (Pace Chasers), Taiki Shuttle (Miles) and The Throne's Assemblage (Mediums).
- For skill rankings, conditions and general information, use the tools listed in the Links section (3.7).
- **Scenario link and Pal cards** become more useful in certain scenarios. Most Pal cards are very strong in their own scenario, even at 0LB or 1LB. Scenario link cards also give extra skill hints that should be part of your deck planning for that scenario.

### 3.5 How to Read the Scenario Tables

Each scenario has a header (release timing, gimmick, links, skills and spark) followed by a card table.

- **Notable hints** are the skills the author considers valuable, as of the date the list was made or updated.
- Event and SR cards are shown at **MLB** value.
- Information marked *(est.)* is an estimate (shown in red in the source).
- In the hints column, **bold** marks the gold skill, and skills in (parentheses) are the coinflip chains.
- **Bold** in the Style/Distance column means the card works exceptionally well for that style.
- **Pull?** values are the author's suggestion at the time of the list: Yes, No, Free, With Kitasan, and so on. Some have a longer note attached, shown under each table.
- Card art is left out of this text version.

### 3.6 Scenario Tables


#### URA

**Release timing (Global):** Jun 26th '25

- Scenario gimmick: none! Pure vanilla honse training
- Scenario links: Aoi Kiryuin (Iron Will)
- Scenario skills: Iron Will, (random) Beeline Burst, (random) Breath of Fresh Air
- Scenario spark: URA Finale (SPD/STA)

| Support Card | Date | Style/Distance | LB Breakpoints | Notable Bonuses | Notable Hints | Pull? | Notes |
|---|---|---|---|---|---|---|---|
| Oguri Cap | Jun 26th '25 | Late<br>Mile | MLB | Power Bonus +1<br>Friendship Bonus (15-20%)<br>Mood Effect (40-60%)<br>Power Bonus +2 (1LB+)<br>Training Eff. (5-10%) (3LB+) | Corner Adept<br>Homestretch Haste<br>Nimble Navigator<br>Up-Tempo<br>Groundwork<br>Focus<br>Outer Swell<br>Stamina to Spare<br>**Furious Feat** | No | Not worth pulling, power cards are unusable early game |
| Sweep Tosho | Jun 26th '25 | End | MLB | Training Eff. (10%)<br>Friendship Bonus (30%)<br>Mood Effect (40%)<br>Specialty Priority (50) | Slipstream<br>Prudent Positioning<br>After-school stroll | No | Good card, including an event with Charming, but never pull for SRs in banners, they'll eventually make your way into your account |
| Haru Urara (Friend Points Shop) | Jun 26th '25 | All-rounder | MLB | Friendship Bonus (32%)<br>Training Eff. (15%)<br>Race Bonus (10%)<br>Specialty Priority (50) | **Unruffled** | Free | Good once guts starts becoming more useable (around MANT) |
| Mejiro McQueen (Story) | Jun 26th '25 | Pace<br>Long | MLB | Friendship Bonus (30%)<br>Mood Effect (30%)<br>Stamina Bonus +1<br>Specialty Priority (50)<br>Guts Bonus +1 | Corner Adept<br>Straightaway Adept<br>Prepared to Pass<br>Inside Scoop<br>Stamina to Spare<br>Deep Breaths<br>Extra Tank<br>**Cooldown**<br>(Deep Breaths) | Free | Plain stamina card, useable for long races |
| Rice Shower (Story) | Jun 26th '25 | Pace<br>Long | MLB | Friendship Bonus (32%)<br>Mood Effect (50%)<br>Guts Bonus +1 | Straight Descent<br>Highlander<br>Deep Breaths<br>**Adrenaline Rush**<br>(Extra Tank) | Free | Nothing going on here, at all |
| Special Week (Event) | Jun 26th '25 | Pace/Late | MLB | Friendship Bonus (35%)<br>Mood Effect (30%)<br>Training Eff. (5%)<br>Race Bonus (10%)<br>Speed Bonus +1 | Homestretch Haste<br>Outer Swell<br>Steadfast<br>Hydrate<br>Shake It Out<br>Extra Tank<br>**Gourmand**<br>(Hydrate) | Free | Free card, always worth going for MLB |
| Twin Turbo | Jul 02 '25 | Front | MLB | Mood Effect (55-75%)<br>Friendship Bonus (15-20%)<br>Speed Bonus +1 (1LB+)<br>Training Eff. (5-10%) (3LB+) | Fast-Paced<br>Leader's Pride<br>Early Lead<br>Watchful Eye<br>**Taking the Lead**<br>(Early Lead) | No | Starts being good at 3LB when unlocking training effectiveness, and best at MLB where you can hit 10% training effectiveness, but it's pointless pulling if Kitasan is around the corner |
| Mejiro Palmer | Jul 10 '25 | Front<br>Long | N/A | Training Eff. (5%)<br>Friendship Bonus (25-35%)<br>Mood Effect (30-40%)<br>Specialty Priority (50-65)<br>Power Bonus +1 (1LB+) | Front-Runner Straightaways<br>Fast-Paced<br>Early Lead<br>Moxie<br>**Vanguard Spirit**<br>(Keeping the Lead) | No | Can be used for front parents, that's it |
| Matikanetannhauser (Event) | Jul 16 '25 | All-rounder<br>(Medium/Long+) | MLB | Friendship Bonus (37.5%)<br>Mood Effect (30%)<br>Training Eff. (5%)<br>Specialty Priority (65)<br>Initial Guts +55<br>Guts Bonus +1 | Steadfast<br>Pace Strategy<br>Deep Breaths<br>**Unruffled**<br>(Calm in a Crowd) | Free | Free guts card that shares a similar fate as Haru Urara, somewhat good when guts is useable |
| Kitasan Black | Jul 16 '25 | All-rounder<br>(Front+) | 3LB+ | Training Eff. (10-15%)<br>Friendship Bonus (20-25%)<br>Mood Effect (20-30%)<br>Specialty Priority (20-100)<br>Power Bonus +1 (1LB+) | Long Corners<br>Front Runner Straightaways<br>Focus<br>Corner Recovery<br>Corner Adept<br>Straightaway Adept<br>**Professor of Curvature** | Yes | The speed card® 3LB makes her useful Great training effectiveness, best specialty priority for a long while, great hints, great gold skill |
| Satono Diamond | Jul 16 '25 | Medium | 3LB+ | Mood Bonus (45-65%)<br>Friendship Bonus (15-20%)<br>Race Bonus (5-10%)<br>Guts Bonus +1 (1LB+)<br>Training Eff. (5-10%) (3LB+) | Medium Corners<br>A Small Breather<br>**Iron Will** | With Kitasan | It's fine if you get some dupes while pulling for Kitasan Does big numbers at MLB as long as you keep your mood up Gold skill is bad though |
| Yukino Bijin | Jul 27 '25 | Medium | MLB | Training Eff. (5%)<br>Mood Effect (40-60%)<br>Friendship Bonus (15-20%)<br>Wit Friendship Recovery (3-5)<br>Wit Bonus +1 (1LB+) | Medium Corners<br>Steadfast<br>Hydrate<br>**No Stopping Me!** | No | Kinda plain for being a banner card, but gives No Stopping Me! |
| Nishino Flower | Jul 27 '25 | Pace | MLB | Race Bonus (15%)<br>Friendship Bonus (20%)<br>Mood Effect (55%)<br>Specialty Priority (50)<br>Power Bonus +1 | Pace Chaser Corners<br>Updrafters<br>Straightaway Adept | No | Another good SR card with a Charming event, but you don't necessarily have to pull for it |
| Winning Ticket (Story) | Aug 03 '25 | Late | MLB | Friendship Bonus (32%)<br>Training Eff. (5%)<br>Mood Effect (30%)<br>Power Bonus +1 | Late Surger Corners<br>Position Pilfer<br>Slick Surge<br>Outer Swell<br>**In Body and Mind** | Free | Good for late parents |
| Yaeno Muteki | Aug 03 '25 | All-rounder<br>(Pace+) | 0LB | Training Eff. (10%)<br>Friendship Bonus (15-20%)<br>Mood Effect (30-40%)<br>Hint Levels (2-4)<br>Hint Frequency (40-60%)<br>Power Bonus +1 (1LB+)<br>Race Bonus (5-10%) (3LB+) | Medium Corners<br>Ramp Up<br>Tail Held High<br>Prepared to Pass<br>Up-Tempo<br>Homestretch Haste<br>Playtime's Over (ends 2nd chain)<br>**It's On!** | No | Great generalist skills, which are great for parents, borrow it |
| Super Creek | Aug 12 '25 | **All-rounder** | 3LB+ | Friendship Bonus (32-37.5%)<br>Training Eff. (10-15%)<br>Race Bonus (5-10%)<br>Specialty Priority (40-55)<br>Stamina Bonus +1 (1LB+) | Ramp Up<br>Homestretch Haste<br>Corner Recovery<br>**Swinging Maestro** | If Dolphin+ | Super Creek is good even at 0LB because of Swinging Maestro The stamina bonus at 1LB bumps her even further, and getting her to MLB for the extra friendship gauge lets you snowball easier |
| Tazuna Hayakawa | Aug 12 '25 | All-rounder | 1LB+ | Failure Reduction (30-40%)<br>Energy Reduction (15-30%)<br>Training Eff. (5-10%) (1LB+) | Tail Held High<br>**Concentration**<br>(Focus) | With Creek | Tazuna is a nice card, but it's better to save up for other, more impactful ones |
| Sakura Chiyono O | Aug 20 '25 | Medium<br>(Pace+) | 3LB+ | Training Eff. (5%)<br>Friendship Bonus (15-20%)<br>Mood Effect (40-60%)<br>Race Bonus (5-15%)<br>Stamina Bonus +1 (1LB+) | Medium Corners<br>Medium Straightaways<br>Steadfast<br>Shifting Gears<br>Stamina to Spare<br>**Speed Star** | No | Only thing good about this card is the fact she has 15% race bonus, and it's not useful yet at all |
| Mejiro Dober (Event) | Aug 28 '25 | Mile/Medium | MLB | Training Eff. (5%)<br>Friendship Bonus (30%)<br>Mood Effect (30%)<br>Race Bonus (10%)<br>Wit Bonus +1<br>Wit Friendship Recovery (5) | Up-Tempo<br>Steadfast<br>Unyielding Spirit | Free | Pretty underwhelming SSR, but it's free nonetheless MLB it |
| Kawakami Princess | Aug 29 '25 | Pace<br>Medium | MLB | Speed Bonus +1<br>Friendship Bonus (25-30%)<br>Mood Effect (20-30%)<br>Race Bonus (5-10%)<br>Power Bonus +1 (1LB+) | Tactical Tweak<br>Preferred Position<br>Soft Step<br>Steadfast<br>**Center Stage** | No | Not much going on with this card at all |
| Hishi Akebono | Aug 29 '25 | Front<br>Sprint | 0LB | Training Eff. (5%)<br>Friendship Bonus (20-25%)<br>Mood Effect (15-45%)<br>Hint Levels (2-4)<br>Hint Frequency (40-60%)<br>Guts Bonus +1 (1LB+) | Sprint Corners<br>Countermeasure<br>Gap Closer<br>Sprinting Gear<br>Final Push<br>**Sixth Sense**<br>(Dodging Danger) | No | Similar case as Yaeno Muteki, good for sprint parents and nothing else, just borrow it |
| Tamamo Cross | 08 Sep '25 | Late<br>Medium | 1LB | Training Eff. (10-15%)<br>Friendship Bonus (15-20%)<br>Mood Effect (20-30%)<br>Stamina Bonus +1 (1LB+)<br>Initial Stamina +50 (MLB) | Medium Corners<br>Tail Held High<br>1,500,000 CC<br>Rosy Outlook<br>Soft Step<br>**Fast & Furious** | No | Useable Stamina statstick for lates, although you're probably better off using Super Creek anyways |
| Silence Suzuka | 08 Sep '25 | Front | MLB | Friendship Bonus (25-35%)<br>Mood Effect (45-55%)<br>Specialty Priority (50-65) | Left-Handed<br>Front Runner Corners<br>Front Runner Straightaways<br>Fast-Paced<br>Leader's Pride<br>Early Lead<br>Final Push<br>Focus<br>**Unrestrained** | No | Decent statstick for fronts with all of the hints she hands out and a good gold as well, but probably not worth being pulled for |
| Bamboo Memory | 18 Sep '25 | Late | MLB | Training Eff. (10-15%)<br>Friendship Bonus (20-25%)<br>Power Bonus +1 | Late Surger Straightaways<br>Mile Straightaways<br>Homestretch Haste<br>Straightaway Adept<br>Gap Closer<br>**Rising Dragon**<br>(Outer Swell) | No | Doesn't become useable until MLB, and even then, she's still pretty underwhelming Gives Rising Dragon, though |
| Shinko Windy | 18 Sep '25 | Pace<br>Mile | MLB | Friendship Bonus (37.5%)<br>Training Eff. (5%)<br>Mood Effect (30%)<br>Race Bonus (10%)<br>Speed Bonus +1 | Prepared to Pass<br>Shifting Gears<br>Unyielding Spirit | No | Good SR statstick, but like other SRs, no need to pull for it |
| Gold Ship (Event) | 21 Sep '25 | End<br>Long | MLB | Power Bonus +1<br>Training Eff. (10%)<br>Friendship Bonus (25%)<br>Mood Effect (20%)<br>Hint Levels (3)<br>Hint Frequency (60%) | Long Straightaways<br>Inside Scoop<br>Pressure<br>Straightaway Spurt<br>Highlander<br>Groundwork<br>Uma Stan<br>Standing By<br>After-School Stroll<br>**Innate Experience**<br>(Inside Scoop) | Free | Good parent card, although the amount of possible hints kinda diminish the chance of getting good skills like Uma Stan, Straightaway Spurt or Groundwork |
| King Halo | 22 Sep '25 | Sprint | MLB | Friendship Bonus (37.5-43%)<br>Specialty Priority (55-70)<br>Training Eff. (5-10%)<br>Friendship Bonus +1 (1LB+) | Gap Closer<br>Uma Stan<br>Homestretch Haste<br>Corner Recovery<br>**Blinding Flash**<br>(Gap Closer) | No | Card with guaranteed Uma Stan hint, so it's useable in parent decks It becomes good at MLB with high specialty priority + training effectiveness, but it's a power card anyways... |
| Seiun Sky | 22 Sep '25 | Front<br>Long | MLB | Speed Bonus +1<br>Training Eff. (5-10%)<br>Friendship Bonus (25-35%)<br>Wit Friendship Recovery (3-5)<br>Speed Bonus +2 (1LB+) | Tail Held High<br>Keeping the Lead<br>**Vanguard Spirit** | No | Wit card for fronts in long races, viable at MLB, pretty meh otherwise |
| Mejiro Ryan | 3 Oct '25 | Medium | MLB | Power Bonus +1<br>Skill Point Bonus +1<br>Friendship Bonus (20-25%)<br>Mood Effect (40-50%)<br>Race Bonus (5-10%)<br>Guts Bonus +1 (1LB+) | Medium Straightaways<br>Up-Tempo<br>Pace Strategy<br>**Unyielding** | No | Underwhelming to say the least |
| Narita Brian (Story) | 7 Oct '25 | Pace/Late<br>Medium/Long | MLB | Speed Bonus +2<br>Friendship Bonus (+30%)<br>Training Eff. (5%) | Right-Handed<br>Medium Straightaways<br>Medium Corners<br>Long Straightaways<br>Preferred Position<br>Hydrate<br>Outer Swell<br>**Shatterproof** | Free | The best story card so far, useable as a speed statstick for free-to-play players Also makes for a fair parent card |
| Nishino Flower | 8 Oct '25 | All-rounder<br>(Pace+) | 3LB+ | Mood Effect (35-45%)<br>Starting friendship gauge (40-50)<br>Training Eff. (5-10%)<br>Friendship Bonus (15-20%)<br>Speed Bonus +1 (1LB+) | Pace Chaser Corners<br>Countermeasure<br>Updrafters<br>**Beeline Burst**<br>(Straightaway Adept) | No | Very basic card, with an outstandingly high starting friendship bond, although no specialty priority hurts her snowball potential |
| Vodka | 8 Oct '25 | Late<br>Medium/Mile | 1LB+ | Specialty Priority (70-85)<br>Friendship Bonus (37.5-48.5%)<br>Mood Effect (30-40%)<br>Power Bonus +1 (1LB+) | Mile Straightaways<br>Medium Straightaways<br>Straightaway Adept<br>Homestretch Haste<br>Updrafters<br>Slick Surge<br>Nimble Navigator<br>Straightaway Recovery<br>**Breath of Fresh Air** | If Whale | If she wasn't a power card, she'd be great anywere else She's the best early game power card starting from 1LB Could definitely pump great numbers at MLB Works great as a parent card from 3LB+ |
| Daiwa Scarlet | 14 Oct '25 | Pace<br>Mile/Medium | MLB | Power Bonus +1<br>Training Eff. (10%)<br>Starting Power +50 | Prepared to Pass<br>Shifting Gears<br>Up-Tempo<br>Stamina to Spare<br>**Race Planner**<br>(Preferred Position) | Free | Decent welfare card, 10% training effectiveness and no specialty priority means she's a roaming card with a coinflip gold recovery |
| Sweep Tosho | 15 Oct '25 | End | MLB | Friendship Bonus (37.5-48.5%)<br>Specialty Priority (50-65)<br>Race Bonus (5-10%)<br>Mood Effect (15-30%) (3LB+) | Slipstream<br>Prudent Positioning<br>After-school stroll<br>Straightaway Spurt (coinflip)<br>**Crusader** | No | What a rollercoaster of a card She'd pump out great numbers if she actually had starting friendship bond, but if you grow it quickly, you'll snowball pretty hard Straightaway Spurt gamble on her first chain event, as well |
| Winning Ticket | 15 Oct '25 | Late<br>Medium | N/A | Stamina Bonus +1<br>Mood Effect (35-45%)<br>Friendship Bonus (15-20%)<br>Race Bonus (5-10%) (3LB+) | Medium Straightaways<br>Late Surger Corners<br>Position Pilfer<br>Slick Surge<br>Outer Swell<br>1,500,000 CC<br>Triple 777s<br>**Hard Worker** | No | Absolutely nothing on this card besides the hints Taking away the gold skill, of course — Fighter is already one of the worst skills in the game, Hard Worker is pretty close on being bottom-of-the-barrel as well |
| Special Week | 22 Oct '25 | Pace/Late | MLB | Guts Bonus +1<br>Friendship Bonus (15-20%)<br>Mood Effect (40-60%)<br>Training Eff. (5-10%) (3LB+) | Homestretch Haste<br>Outer Swell<br>Steadfast<br>Straight Descent<br>Hydrate<br>Soft Step<br>**In Body and Mind**<br>(Homestretch Haste) | No | Only does something at MLB, and it's not exactly great |
| Tokai Teio | 22 Oct '25 | Pace | MLB | Friendship Bonus (26.5-32%)<br>Mood Effect (40-60%)<br>Power Bonus +1 (1LB+)<br>Race Bonus (5-10%) (3LB+) | Pace Chaser Straightaways<br>Nimble Navigator<br>Shrewd Step<br>Soft Step<br>**Rushing Gale!** | No | Could be used as a statstick, but definitely lacking strength against other SSR MLBs like Kitasan or Biko |
| Nice Nature | 30 Oct '25 | **Late** | 3LB+ | Wit Bonus +1<br>Training Eff. (10-15%)<br>Friendship Bonus (20-25%)<br>Race Bonus (5-15%)<br>Wit Friendship Recovery (3-5)<br>Wit Bonus +1 (1LB+) | Ramp Up<br>A Small Breather<br>**On Your Left!** | Conditional | Staple wit card for Late decks because of gold skill Sadly, she's the last banner of URA scenario, which means next banner is a Pal card that will be used throughout the entire Unity Cup |
| Silence Suzuka (Event) | 03 Nov '25 | Front | MLB | Training Eff. (5%)<br>Friendship Bonus (25%)<br>Mood Effect (30%)<br>Initial Stamina +55<br>Stamina Bonus +1 | Left-Handed<br>Front Runner Corners<br>Front Runner Straightaways<br>Fast-Paced<br>Leader's Pride<br>Early Lead<br>Final Push<br>Focus<br>Hydrate<br>Soft Step<br>**Concentration** | Free | It's a free card, and useable for front parents |

**Notes attached to individual cells:**

- **Nice Nature** (Pull?): Nice Nature is a great card to drop carats on Consider pulling if you're planning on playing late surgers in the long run Consider pulling if you pulled in Kitasan but not on any other banner Save if you're going to pull for MLB Riko Kashimoto

#### Unity Cup

**Release timing (Global):** Nov 6th '25

- Scenario gimmick: team trials-like team formation. Increase your team stats by participating in Unity Trainings that can end up in Unity Bursts, providing extra stats where they explode Face off other NPC teams every 6 months until the end of senior year, when you'll run against Riko Kashimoto's Team Zenith
- Scenario links: Matikanefukukitaru (Clairvoyance), Taiki Shuttle (Mile Maven), Rice Shower (Cooldown), Haru Urara (Indomitable), None (No Stopping Me!), Riko Kashimoto
- Scenario skills: Burning Spirit SPD/PWR/STA/GUTS/WIT (Ignited Spirit SPD/PWR/STA/GUTS/WIT), It's On!
- Scenario spark: Unity Cup (PWR/WIT)

| Support Card | Date | Style/Distance | LB Breakpoints | Notable Bonuses | Notable Hints | Pull? | Notes |
|---|---|---|---|---|---|---|---|
| Riko Kashimoto | Nov 6th '25 | All-rounder | 1LB+<br>(R MLB > 0LB) | Failure Reduction (25-30%)<br>Energy Reduction (15-20%)<br>Race Bonus (5-10%)<br>Training Eff. (5-10%) (1LB+) | Ramp Up<br>**Rushing Gale!**<br>(Straightaway Acceleration) | 100 free pulls<br>1LB+<br>or<br>R MLB | 1LB is recommended through Unity Cup MLB is useable during MANT |
| Rice Shower | Nov 6th '25 | Pace<br>Long<br>Debuff | 3LB+ | Training Eff. (5-15%)<br>Stamina Bonus +1<br>Friendship Bonus (25-30%)<br>Specialty Priorty (25-50)<br>Power Bonus +1 (1LB+) | Straight Descent<br>Highlander<br>**Swinging Maestro<br>Cooldown** (Unity Cup only) | 100 free pulls<br>With Riko | Value decreased because of No Stopping Me! buff |
| Sakura Bakushin O | Nov 11th '25 | Front<br>Sprint | MLB | Friendship Bonus (26.5-32%)<br>Mood Effect (30-40%)<br>Race Bonus (5-10%)<br>Specialty Priority (35-50)<br>Speed Bonus +1 (1LB+)<br>Training Eff. (5-10%) (3LB+) | Sprint Straightaways<br>Sprint Corners<br>Huge Lead<br>Sprinting Gear<br>Countermeasure<br>**Turbo Sprint** | With Biko | Mostly used as a statstick |
| Biko Pegasus | Nov 11th '25 | Sprint/Mile | MLB | Training Eff. (15-20%)<br>Specialty Priority (40-55)<br>Race Bonus (5-10%)<br>Speed Bonus +1 (1LB+) | Sprint Straightaways<br>Gap Closer<br>Productive Plan<br>Updrafters<br>**Plan X** | If Whale | Decent at 1LB+, snowballs at MLB because of initial friendship gauge |
| Ikuno Dictus | Nov 19th '25 | Late<br>Medium | MLB | Training Eff. (10%)<br>Friendship Bonus (25-30%)<br>Race Bonus (5-15%)<br>Guts Bonus +1 (1LB+) | N/A | No | Useable in MANT, but that's it |
| Mihono Bourbon (Event) | Nov 24th '25 | **Front** | MLB | Friendship Bonus (20%)<br>Mood Effect (40%)<br>Training Eff. (5%)<br>Wit Friendship Recovery (5)<br>Speed Bonus +1 | Front Runner Straightaways<br>Front Runner Corners<br>Moxie<br>Focus<br>**Taking the Lead** | Free | Great free event card for front runners |
| Zenno Rob Roy | Nov 24th '25 | Late | 2LB+ | Friendship Bonus (26.5-32%)<br>Training Eff. (10%)<br>Mood Effect (20-30%)<br>Specialty Priority (35-50)<br>Speed Bonus +1 (1LB+) | Right-Handed<br>Left-Handed<br>Straightaway Adept<br>Nimble Navigator<br>Shrewd Step<br>**Lie in Wait** | If Whale | Good gold recovery for lates |
| Tamamo Cross | Nov 24th '25 | Late | 1LB+ | Friendship Bonus (32-37.5)<br>Mood Effect (40-60%)<br>Race Bonus (5-10%)<br>Specialty Priority (50-65)<br>Stamina Bonus +1 (1LB+) | Medium Corners<br>1,500,000CC<br>**15,000,000CC** | With<br>Zenno Rob Roy | In paper it's good... in reality it's just a power card |
| Seiun Sky | Dec 1st '25 | Front | 1LB+ | Mood Effect (45-55%)<br>Friendship Bonus (25-35%)<br>Specialty Priority (70-85)<br>Stamina Bonus +1 (1LB+) | Tail Held High<br>Dodging Danger<br>Keeping the Lead<br>**Escape Artist**<br>(Fast-Paced) | No | Considerable pick for fronts early game, other than that, nothing much going on |
| Yaeno Muteki (Rerun) | Dec 1st '25 | All-rounder<br>(Pace+) | 0LB | Training Eff. (10%)<br>Friendship Bonus (15-20%)<br>Mood Effect (30-40%)<br>Hint Levels (2-4)<br>Hint Frequency (40-60%)<br>Power Bonus +1 (1LB+)<br>Race Bonus (5-10%) (3LB+) | Medium Corners<br>Ramp Up<br>Tail Held High<br>Prepared to Pass<br>Up-Tempo<br>Homestretch Haste<br>Playtime's Over (ends 2nd chain)<br>**It's On!** | No | If you didn't get her at first, you probably don't need to get her now Keep borrowing it |
| Nakayama Festa | Dec 8th '25 | Late<br>Medium | 3LB+ | Friendship Bonus (26.5-32%)<br>Mood Effect (20-30%)<br>Specialty Priority (35-50)<br>Guts Bonus +1<br>Stamina Bonus +1 (1LB+)<br>Training Eff. (5-10%) (3LB+) | Late Surger Straightaways<br>Outer Swell<br>Slick Surge<br>All I've Got<br>Uma Stan<br>(if 1st option chosen in 1st chain)<br>**Come What May**<br>(All I've Got)<br>(if 2nd option chosen in 1st chain) | No | Actual solid stamina statstick, just overshadowed by Super Creek because of her gold skill |
| Yukino Bijin (Event) | Dec 14th '25 | Medium | MLB | Friendship Bonus (32%)<br>Training Eff. (10%)<br>Race Bonus (10%)<br>Specialty Priority (50)<br>Starting Friendship Gauge (40)<br>Guts Bonus +1 | Medium Corners<br>Playtime's Over (ends 2nd chain)<br>**Corner Connoiseur** | Free | Good for guts decks in MANT |
| Curren Chan | Dec 14th '25 | Sprint | MLB | Mood Effect (35-45%)<br>Race Bonus (6-10%)<br>Friendship Bonus (25-30%)<br>Specialty Priority (50-65)<br>Wit Friendship Recovery (3-5)<br>Wit Bonus +1 (1LB+) | Sprint Straightaways<br>Sprinting Gear<br>Playtime's Over (ends 1st chain)<br>**Perfect Prep!**<br>(Meticulous Measures) | #No | Don't get Curren'd, it's not worth it |
| Narita Brian | Dec 14th '25 | Pace/Late<br>Medium/Long | N/A | Training Effectiveness (10%)<br>Friendship Bonus (25-35%)<br>Mood Effect (20-30%)<br>Race Bonus (5-10%) (3LB+) | Right-Handed<br>Medium Straightaways<br>Medium Corners<br>Long Straightaways<br>Up-Tempo<br>Preferred Position<br>Hydrate<br>Outer Swell<br>**Beeline Burst** | No | The wolf does not concern herself with being useful, at all |
| El Condor Pasa | Dec 18th '25 | Pace<br>Medium | MLB | Friendship Bonus (26.5-32%)<br>Specialty Priority (55-70)<br>Mood Effect (30-40%)<br>Race Bonus (5-10%)<br>Power Bonus +1 (1LB+)<br>Training Eff. (5-10%) (3LB+) | Medium Straightaways<br>Pace Chaser Straightaways<br>Up-Tempo<br>Prepared to Pass<br>Stamina to Spare (ends 2nd chain)<br>**Killer Tunes** | With Kitasan | Best at MLB because of training effectiveness Good statstick if you get copies while pulling for Kitasan |
| Kitasan Black (Rerun) | Dec 18th '25 | **All-rounder (Front+)** | 3LB+ | Training Eff. (10-15%)<br>Friendship Bonus (20-25%)<br>Mood Effect (20-30%)<br>Specialty Priority (20-100)<br>Power Bonus +1 (1LB+) | Long Corners<br>Front Runner Straightaways<br>Focus<br>Corner Recovery<br>Corner Adept<br>Straightaway Adept<br>**Professor of Curvature** | If you have less<br>than 3LB<br>before banner | The speed card® returns 3LB makes her useful Great training effectiveness, best specialty priority for a long while, great hints, great gold skill |
| Daitaku Helios | Dec 28th '25 | Front/Pace<br>Mile | N/A | Power Bonus +1<br>Friendship Bonus (25-30%)<br>Mood Effect (40-50%)<br>Training Eff. (5%)<br>Skill Point Bonus +1<br>Race Bonus (5-10%) | Mile Corners<br>Pace Chaser Corners<br>(ends 1st chain)<br>Ramp Up<br>Slipstream<br>Early Lead<br>**Escape Artist**<br>(Fast-Paced) | No | Could see some use in parent decks |
| Marvelous Sunday (Event) | Jan 5th '25 | All-rounder<br>(Late+) | MLB | Friendship Bonus (37.5%)<br>Race Bonus (15%)<br>Stamina Bonus +1<br>Initial Stamina, Power +35 | Straightaway Adept<br>Ramp Up<br>Tail Held High<br>**Fast & Furious**<br>(Position Pilfer) | Free | Third great free card in a row Amazing race bonus and initial stats for MANT |
| Mayano Top Gun | Jan 5th '26 | All-rounder<br>(Front/Pace+) | 3LB+ | Friendship Bonus (20-25%)<br>Mood Effect (40-50%)<br>Training Eff. (5%)<br>Power Bonus +1<br>Speed Bonus +1 (1LB+)<br>Specialty Priority (40-80) (3LB+) | Corner Adept<br>Straightaway Adept<br>Nimble Navigator<br>Head-On<br>**Restless** | If Whale | Good card locked away behind her 80 specialty priority at MLB, although useable at 3LB |
| Narita Taishin | Jan 5th '26 | End<br>Long | MLB | Speed Bonus +1<br>Training Eff. (5-10%)<br>Friendship Bonus (25-35%)<br>Race Bonus (5-10%)<br>Wit Friendship Recovery (3-5)<br>Wit Bonus +1 (1LB+) | End Closer Corners<br>Masterful Gambit<br>Pressure<br>Standing By<br>**Sleeping Lion**<br>(Standing By) | With Mayano | Hardly viable, but at least has wit and speed bonuses with 10% training effectiveness at MLB |
| Manhattan Cafe | Jan 15th '26 | Long<br>Debuff | 3LB+ | Stamina Bonus +1<br>Friendship Eff. (37.5-48.5%)<br>Stamina Bonus +1 (1LB+)<br>Race Bonus (5-10%) (3LB+) | Long Corners<br>Long Straightaways<br>Highlander<br>**Stamina Siphon** | No | Big numbers if she lands on stamina training with 50 specialty priority at MLB, it's not too bad, but in the end, a Stamina card for Longs without a gold recovery is like shooting yourself on your foot Also has a chance to give Night Owl on her second chain |
| Silence Suzuka (Story) | Jan 22nd '26 | Front<br>Medium | MLB | Training Eff. (5%)<br>Friendship Bonus (25%)<br>Mood Effect (30%)<br>Specialty Priority (50)<br>Speed Bonus +1 | Left-Handed<br>Front Runner Corners<br>Front Runner Straightaways<br>Fast-Paced<br>Leader's Pride<br>Early Lead<br>Final Push<br>Focus<br>**Trackblazer** | Free | Slightly weaker version of her other speed SSR, but better than the free stamina one. Good for front parents. |
| Nice Nature (Rerun) | Jan 22nd '26 | **Late** | 3LB+ | Wit Bonus +1<br>Training Eff. (10-15%)<br>Friendship Bonus (20-25%)<br>Race Bonus (5-15%)<br>Wit Friendship Recovery (3-5)<br>Wit Bonus +1 (1LB+) | Ramp Up<br>A Small Breather<br>**On Your Left!** | If you have her<br>at 2LB+ | Staple wit card for Late decks because of gold skill Also a great wit card for MANT because of her 15% race bonus at MLB, although 10% at 3LB works well |
| Oguri Cap (Rerun) | Jan 22nd '26 | Late<br>Mile | MLB | Power Bonus +1<br>Friendship Bonus (15-20%)<br>Mood Effect (40-60%)<br>Power Bonus +2 (1LB+)<br>Training Eff. (5-10%) (3LB+) | Corner Adept<br>Homestretch Haste<br>Nimble Navigator<br>Up-Tempo<br>Groundwork<br>Focus<br>Outer Swell<br>Stamina to Spare<br>**Furious Feat** | With<br>Nice Nature | Could be a good roamer card but generally just falls flat as a Power card with a Mile gold skill |
| Admire Vega | Jan 29th '26 | **End** | 1LB+ | Training Eff. (15-20%)<br>Friendship Bonus (25-30%)<br>Power Bonus +1 (1LB+)<br>Race Bonus (5-10%) (3LB+) | End Closer Straightaways<br>Masterful Gambit<br>**Daring Strike** | **50 free pulls**<br>With<br>Fukukitaru *(est.)* | Another card suffering from the power card curse |
| Matikanefukukitaru | Jan 29th '26 | All-rounder<br>(Late+) | 3LB+ | Mood Effect (35-45%)<br>Friendship Bonus (15-20%)<br>Failure Reduction (10%)<br>Energy Reduction (5-10%)<br>All Initial Stats (+10-30)<br>Training Eff. (5-10%) (1LB+)<br>Race Bonus (5-10%) (3LB+) | Late Surger Corners<br>A Small Breather<br>Triple 777s<br>**Super Lucky Seven**<br>(Lucky Seven) | **50 free pulls**<br>Conditional *(est.)* | Cygames got real creative here, first and only non-pal card to have energy and failure reduction Gives +150 initial stats at MLB Basically a pal card disguised as a speed card Great for MANT at MLB with starting stats and 10% race bonus |
| Meisho Doto (Event) | Jan 29th '26 | Pace/Late<br>Medium | MLB | Training Eff. (10%)<br>Friendship Bonus (25%)<br>Stamina Bonus +1<br>Initial Stamina, Guts +35 | Medium Corners<br>Late Surger Straightaways<br>Pace Chaser Corners<br>Shake It Out<br>**Killer Tunes** | Free | She's free Just get her |
| Sasami Anshinzawa | Feb 5th '26 | Gambler | N/A | Mood Effect (40-60%) | Uma Stan<br>Risky Business<br>Wallflower<br>Corner Recovery ×<br>**Nothing Ventured**<br>(Risky Business) | No | A little troll, a little niche Used by whales to min-max in open league |
| Riko Kashimoto (Rerun) | Feb 11th '26 | All-rounder | 1LB+<br>(R MLB > 0LB) | Failure Reduction (25-30%)<br>Energy Reduction (15-20%)<br>Race Bonus (5-10%)<br>Training Eff. (5-10%) (1LB+) | Ramp Up<br>**Rushing Gale!**<br>(Straightaway Acceleration) | No | Don't get tempted, if you haven't pulled for Riko, now is not the time |
| Tazuna Hayakawa (Rerun) | Feb 11th '26 | All-rounder | 1LB+ | Failure Reduction (30-40%)<br>Energy Reduction (15-30%)<br>Training Eff. (5-10%) (1LB+) | Tail Held High<br>**Concentration**<br>(Focus) | No | Tazuna is a nice card, but it's better to save up for other, more impactful ones |
| Tosen Jordan (Event) | Feb 18th '26 | Pace/Late<br>Medium | MLB | Training Eff. (10%)<br>Friendship Bonus (20%)<br>Specialty Priority (50)<br>Speed Bonus +1<br>Initial Speed 35<br>Initial Power 30 | Medium Corners<br>Medium Straightaways<br>Pace Chaser Straightaways<br>Position Pilfer<br>Stamina to Spare<br>**Breath of Fresh Air**<br>(Straightaway Recovery) | Free | Decent free speed card |
| Nishino Flower | Feb 18th '26 | Pace<br>Mile | 3LB+ | Wit Bonus +3 when<br>bond is full<br>Training Eff. (5%)<br>Friendship Bonus (25-30%)<br>Wit Friendship Recovery (3-5)<br>Speed Bonus +1 (1LB+) | Pace Chaser Corners<br>Updrafters<br>Shifting Gears<br>**Determined Descent** | With Bakushin | Nothing much going on other than a huge +3 on wit when her gauge is full, with 50 specialty priority at 3LB+ |
| Sakura Bakushin O | Feb 18th '26 | Sprint | 1LB+ | Training Eff. (20%) in SPD, STA<br>PWR, WIT when bond is 80+<br>Friendship Bonus (25-30%)<br>Mood Effect (20-30%)<br>Race Bonus (5-10%)<br>Guts Bonus +1 (1LB+) | Sprint Straightaways<br>Sprint Corners<br>Huge Lead<br>Sprinting Gear<br>Countermeasure<br>Groundwork<br>Gap Closer<br>**In High Spirits**<br>(Light as a Feather) | If Whale | Good roaming card that gives big training effectiveness even at 0LB when not training in guts, so she gets better after MANT |
| Agnes Digital | Feb 25th '26 | Dirt<br>Mile/Medium<br>(Pace/Late+) | 1LB+ | Training Eff. (15%) in<br>highlander team<br>Friendship Bonus (20-25%)<br>Power Bonus +1<br>Stamina Bonus +1 (1LB+)<br>Mood Effect (15-30%) (3LB+) | Left-Handed<br>Mile Straightaways<br>Late Surger Straightaways<br>Uma Stan<br>Forward, March!<br>All I've Got<br>Hydrate<br>Focus<br>**Lead The Charge!** | No | Highlander team means 5 different card types, you could say Agnes Digital was way ahead of her time, since this strat is not viable so early on Could see some use as a parent card, with guaranteed Uma Stan |
| Fine Motion | Mar 5th '26 | **All-Rounder (Pace+)** | 3LB+ | Friendship Bonus (32-37.5%)<br>Training Eff. (10-15%)<br>Race Bonus (5-10%)<br>Wit Friendship Recovery (3-5)<br>Wit Bonus +1 (1LB+)<br>Mood Effect (15-30%) (3LB+) | Right-Handed<br>Nimble Navigator<br>Corner Adept<br>**Speed Star**<br>(Prepared to Pass) | **5 free pulls**<br>Conditional *(est.)* | Fine Motion debut banner, but it's somewhat a bait, since the following banner is 1st Anniversary with Narita Top Road Follow your instinct on this one, mind you we're getting free pulls soon |
| Kawakami Princess (Rerun) | Mar 5th '26 | Pace<br>Medium | MLB | Speed Bonus +1<br>Friendship Bonus (25-30%)<br>Mood Effect (20-30%)<br>Race Bonus (5-10%)<br>Power Bonus +1 (1LB+) | Tactical Tweak<br>Preferred Position<br>Soft Step<br>Steadfast<br>**Center Stage** | **5 free pulls**<br>No *(est.)* | Not much going on with this card at all, other than the cheap and easy to activate gold skill for Team Trials |

**Notes attached to individual cells:**

- **Matikanefukukitaru** (Pull?): Fukukitaru is worth it 3LB+, so you should value her whether or not you can chase after her dupes with the free pulls Dolphins should be able to afford this card after saving up since Riko or Biko+Bakushin banners If you didn't pull for Kitasan, you might wanna pull here (Fukukitaru is not a Kitasan replacement, but a good addition) If you are not planning on pulling for Narita Top Road banner during the first anni, then consider getting Fukukitaru, as both her and Top Road are staples in MANT decks and you won't be able to borrow both
- **Fine Motion** (Pull?): Are you pulling for Narita Top Road? If not, consider pulling here, but be mindful, Fine Motion returns with Maruzensky Speed in their first reruns Do you have Fine Motion 2LB+? Consider taking the free/paid SSR vouchers during the First Anniversary celebrations to bump it up to 3LB or MLB

#### Make a New Track!! (Trackblazer)

**Release timing (Global):** Early Mar '26

- Scenario gimmick: race, race, race. MANT revamps goals completely - your uma must now compete in races to become the Horsegirl of the Year In addition, participating in races now awards you with Shop Coins, a currency you can use in the scenario shop to get bonuses for your career In the end, you'll battle in the Twinkle Star Climax, a series of races that award more points the better you place in each of the three starts that take place
- Scenario link: none
- Scenario-specific events: trainee-specific events (secret events) are swapped for special epithets that grant extra stats, hints and skill points that are affected by Race Bonus %
- Scenario skills: The First Star (Glittering Stars)
- Scenario spark: Climax Scenario (STA/GUTS)

| Support Card | Date | Style/Distance | LB Breakpoints | Notable Bonuses | Notable Hints | Pull? | Notes |
|---|---|---|---|---|---|---|---|
| Mejiro Bright (Event) | Mar 12th '26 | Long | MLB | Stamina Bonus +2 when<br>bond is 80+<br>Friendship Bonus (25%)<br>Specialty Priority (50)<br>Guts Bonus +1 | Pressure<br>Early Start<br>Extra Tank<br>Passing Pro<br>**Overwhelming Pressure** | Free | Average free card |
| Satono Diamond (Event) | Mar 12th '26 | Late<br>(Long+) | MLB | Training Eff. (10%) in<br>rainbow teams<br>Friendship Bonus (25%)<br>Wit Friendship Recovery (5)<br>Wit Bonus +1<br>Skill Point Bonus +1 | Late Surger Corners<br>Late Surger Straightaways<br>Position Pilfer<br>Be Still<br>Pressure<br>**Lie In Wait**<br>(Be Still) | Free | Free card that is used in rainbow teams due to her unique giving 10% training effectiveness when using 4+ different card types so not great for MANT Has a good Gold recovery for lates |
| Narita Top Road | Mar 12th '26 | All-rounder<br>(Medium/Long+) | MLB | Training Eff. (20% at 200k fans)<br>Speed Bonus +1<br>Friendship Bonus (25-30%)<br>Power Bonus +1 (1LB+)<br>Race Bonus (5-10%) (3LB+) | Long Straightaways<br>Prepared to Pass<br>All I've Got<br>Pressure<br>Up-Tempo<br>**Firm Course Menace** | **60 free pulls**<br>If Whale *(est.)* | Viable during MANT because of her unique, then falls off considerably |
| Admire Vega | Mar 12th '26 | All-rounder<br>(End+) | MLB | Friendship Bonus (30%)<br>Mood Effect (30%)<br>Race Bonus (15%)<br>Speed Bonus +1<br>Power Bonus +1 | End Closer Straightaways<br>Masterful Gambit<br>Levelheaded | **60 free pulls**<br>With free pulls<br>or<br>With Top Road *(est.)* | Staple guts card during MANT, her 15% race bonus and speed and power bonuses make her a great option for guts/wit decks Try getting as many dupes through free pulls |
| Marvelous Sunday | Mar 22nd '26 | Long | N/A | Mood Effect (60%)<br>when bond is full<br>Friendship Bonus (25-30%)<br>Training Eff. (5%)<br>Specialty Priority (35-50)<br>Guts Bonus +1 (1LB+) | Ramp Up<br>Tail Held High<br>Straightaway Adept<br>**Adrenaline Rush** | No | Nothing worth in this card, here comes the great MANT carat save up |
| Team Sirius (Story) | Mar 26th '26 | Front/Late<br>Long | MLB | Training Eff. (10%) when<br>bond is 80+<br>Friendship Bonus (15%)<br>Mood Effect (20%)<br>Wit Friendship Recovery 2<br>Skill Point Bonus +1 | Left-Handed<br>Late Surger Corners<br>Early Lead<br>Risky Business<br>Corner Recovery<br>**Best in Japan** | Free | First group type card, and it's a lot to digest. First of all, it can't be used by any team Sirius members (Spe, McQueen, Rice Golshi, Narita Brian, Suzuka and Tickezo) nor decks with their cards Besides that, it provides a Passion Zone buff that negates Night Owl and Slacker, plus allows friendship training with the card |
| Zenno Rob Roy (Rerun) | Mar 26th '26 | Late | 2LB+ | Friendship Bonus (26.5-32%)<br>Training Eff. (10%)<br>Mood Effect (20-30%)<br>Specialty Priority (35-50)<br>Speed Bonus +1 (1LB+) | Right-Handed<br>Left-Handed<br>Straightaway Adept<br>Nimble Navigator<br>Shrewd Step<br>**Lie in Wait** | **12 free pulls**<br>No *(est.)* | No race bonus sadly means unuseable in MANT Gives a good gold recovery for lates |
| Curren Chan (Rerun) | Mar 26th '26 | Sprint | MLB | Mood Effect (35-45%)<br>Race Bonus (6-10%)<br>Friendship Bonus (25-30%)<br>Specialty Priority (50-65)<br>Wit Friendship Recovery (3-5)<br>Wit Bonus +1 (1LB+) | Sprint Straightaways<br>Sprinting Gear<br>Playtime's Over (ends 1st chain)<br>**Perfect Prep!**<br>(Meticulous Measures) | **12 free pulls**<br>#No *(est.)* | Still not worth it |
| Air Shakur (Event) | Apr 5th '26 | End Closer<br>(Medium+) | MLB | Speed Bonus +2 when<br>bond is 80+<br>Friendship Bonus (20%)<br>Mood Effect (30%)<br>Specialty Priority 50<br>Power Bonus +1 | End Closer Corners<br>End Closer Straightaways<br>Straightaway Spurt<br>Up-Tempo<br>Eager<br>Standing By<br>Levelheaded<br>**Serenity** | Free | It's a free event card... doesn't have a lot going on other than probably some decent numbers when speed training |
| Symboli Rudolf | Apr 5th '26 | Medium | MLB | Unique<br>Training Eff. (5-10%)<br>Friendship Bonus (20-25%)<br>Guts Bonus +1 (1LB+)<br>Race Bonus (5-10%) (3LB+) | Medium Corners<br>Medium Straightaways<br>All I've Got<br>Soft Step<br>**Burning Soul** | No | Creative unique that gives low (+60 stats), compared to others like Speed Fukukitaru (+50-150 stats) At least has race bonus... |
| Sirius Symboli | Apr 5th '26 | Late<br>Medium | MLB | Friendship Training (20-35%)<br>Mood Effect (40-60%)<br>Wit Friendship Recovery (3-5)<br>Speed Bonus +1<br>Wit Bonus +1 (1LB+)<br>Race Bonus (5-10%) (3LB+) | Late Surger Straightaways<br>Medium Corners<br>Be Still<br>Playtime's Over (ends 1st chain)<br>**From The Brink**<br>(Take The Chance) | No | Could potentially give big rainbows, but is only viable at MLB during MANT |
| Daiwa Scarlet | Apr 12th '26 | Pace | MLB | Power Bonus +2 when<br>bond is 80+<br>Friendship Bonus (25-35%)<br>Race Bonus (5-10%)<br>Stamina Bonus +1 (1LB+) | Pace Chaser Corners<br>Straight Descent<br>Prepared to Pass<br>Feature Act<br>Up-Tempo<br>Preferred Position<br>**Neck and Neck** | No | Good parent card for paces with gold Head-On skill, other than that, power training is not exactly in a good spot during MANT |
| Sweep Tosho | Apr 12th '26 | End | MLB | Training Eff. (10%)<br>Friendship Bonus (25%)<br>Wit Friendship Recovery 4<br>Race Bonus (10%)<br>Wit Bonus +1 | End Closer Corners<br>End Closer Straightaways<br>Slipstream<br>After-School Stroll | No | As always, not necessary to pull for an SR card, but it's a good addition to the SR roster if you get her to MLB |
| Twin Turbo (Rerun) | Apr 20th '26 | Front | MLB | Mood Effect (55-75%)<br>Friendship Bonus (15-20%)<br>Speed Bonus +1 (1LB+)<br>Training Eff. (5-10%) (3LB+) | Fast-Paced<br>Leader's Pride<br>Early Lead<br>Watchful Eye<br>**Taking the Lead**<br>(Early Lead) | No | No race bonus = bad during MANT |
| Ines Fujin | Apr 20th '26 | Front | MLB | Training Eff. (10-15%)<br>Friendship Bonus (15-20%)<br>Mood Effect (20-30%)<br>Race Bonus (5%)<br>Speed Bonus +1 (1LB+)<br>Specialty Priority (40-80) (3LB+) | Slipstream<br>Playtime's Over<br>Steadfast<br>Fast-Paced<br>Moxie<br>**Restless**<br>(Moxie) | No | Could work as a statstick in guts decks for fronts after MANT |
| Kawakami Princess (Event) | Apr 26th '26 | Medium<br>(Pace+) | MLB | Power Bonus +2<br>Friendship Bonus (35%)<br>Specialty Priority (65) | Tactical Tweak<br>Steadfast<br>Preferred Position<br>Soft Step<br>**Unyielding** | Free | Underwhelming welfare SSR |
| Seeking The Pearl | Apr 26th '26 | Late<br>Sprint<br>(Pace+) | MLB | Unique<br>Friendship Bonus (25-30%)<br>Specialty Priority (50-65)<br>Skill Point Bonus +1<br>Speed Bonus +1 (1LB+) | Uma Stan<br>Prepared to Pass<br>Head-On<br>Slick Surge<br>Sprinting Gear<br>Light as a Feather<br>Updrafters<br>**Dauntless** | **10 free pulls**<br>No *(est.)* | Only good in niche teams that stack maximum energy buffs |
| Bamboo Memory | Apr 26th '26 | Late<br>Mile | MLB | Unique<br>Friendship Bonus (15-20%+)<br>Race Bonus (5-10%)<br>Specialty Priority (20-65)<br>Speed Bonus +1<br>Guts Bonus +1 (1LB+)<br>Training Eff. (5-10%) (3LB+) | Mile Straightaways<br>Homestretch Haste<br>Outer Swell<br>Position Pilfer<br>Gap Closer<br>Updrafters<br>**Full of Vigor**<br>(Pumped) | **10 free pulls**<br>No *(est.)* | Could see some use at MLB, but not a necessity |
| Mr C.B. | Apr 30th '26 | **End** | 1LB+ | Wit Bonus +1 and Skill Point<br>Bonus +1 when bond is 80+<br>Friendship Bonus (25-30%)<br>Wit Friendship Recovery (3-5)<br>Speed Bonus +1<br>Training Eff. (5%)<br>Wit Bonus +1 (1LB+)<br>Mood Effect (15-30%) (3LB+) | Medium Corners<br>Homestretch Haste<br>Tail Held High<br>Straightaway Spurt<br>Early Start<br>Corner Recovery<br>**Daring Strike** | If Whale | Despite not having a great race bonus, Mr C.B. is useable in MANT (and after) paired with Nice Nature or Fine Motion She's also a great Wit option for End Closers and as a parent card for said style as well |
| Rice Shower (Rerun) | May 10th '26 | Pace<br>Long<br>Debuff | 3LB+ | Training Eff. (5-15%)<br>Stamina Bonus +1<br>Friendship Bonus (25-30%)<br>Specialty Priorty (25-50)<br>Power Bonus +1 (1LB+) | Straight Descent<br>Highlander<br>**Swinging Maestro<br>Cooldown** (Unity Cup only) | No | Not worth it at this point, she fell off |
| Matikanefukukitaru (Rerun) | May 10th '26 | All-rounder<br>(Late+) | 3LB+ | Mood Effect (35-45%)<br>Friendship Bonus (15-20%)<br>Failure Reduction (10%)<br>Energy Reduction (5-10%)<br>All Initial Stats (+10-30)<br>Training Eff. (5-10%) (1LB+)<br>Race Bonus (5-10%) (3LB+) | Late Surger Corners<br>A Small Breather<br>Triple 777s<br>**Super Lucky Seven**<br>(Lucky Seven) | No | If you didn't get her before, it's probably best to not get her now and save up for Summer Maruzensky or Agnes Tachyon |
| Rice Shower (Event) | May 18th '26 | Pace<br>(Long+) | MLB | Training Eff. (10%) when<br>bond is 80+<br>Friendship Bonus (25%)<br>Wit Friendship Recovery (5)<br>Speed Bonus +1<br>Wit Bonus +1 | Pace Chaser Corners<br>Straight Descent<br>Feature Act<br>Deep Breaths<br>**Shatterproof** | Free | Decent free card, probably gives nice wit rainbows Has 5% race bonus so could be useable in MANT, but Gold skill is pretty bad |
| Ikuno Dictus | May 18th '26 | Late | MLB | Unique<br>Friendship Bonus (25-30%)<br>Mood Effect (20-30%)<br>Race Bonus (5-10%)<br>Stamina Bonus +1 (1LB+) | Late Surger Corners<br>Position Pilfer<br>Be Still<br>**Keep Going!**<br>(Full Throttle) | No | Could see some use in late parent decks, other than that it's a pretty meh card Be mindful that her Gold skill (and white version) have stamina drain in them |
| Haru Urara | May 18th '26 | All-rounder | MLB | Skill Point Bonus +1<br>Friendship Bonus (15-20%)<br>Mood Effect (20-30%)<br>Race Bonus (5-10%)<br>Hint Frequency (40-60%)<br>Skill Point Bonus +1 (1LB+)<br>Training Eff. (5-10%) (3LB+) | **Hard Worker** | No | It's nice that she can give a bunch of stats through her hints, but she's miles away from being as good as her (free) guts variant Gold skill is also pretty bad, there's just no reason to get this card |
| Admire Vega (Rerun) | May 28th '26 | End | 1LB+ | Training Eff. (15-20%)<br>Friendship Bonus (25-30%)<br>Power Bonus +1 (1LB+)<br>Race Bonus (5-10%) (3LB+) | End Closer Straightaways<br>Masterful Gambit<br>**Daring Strike** | No | Still suffering from the power card curse, and now she lost value since Mr C. B. shares her Gold skill and is a better card overall |
| Sakura Chiyono O (Rerun) | May 28th '26 | Medium<br>(Pace+) | 3LB+ | Training Eff. (5%)<br>Friendship Bonus (15-20%)<br>Mood Effect (40-60%)<br>Race Bonus (5-15%)<br>Stamina Bonus +1 (1LB+) | Medium Corners<br>Medium Straightaways<br>Steadfast<br>Shifting Gears<br>Stamina to Spare<br>**Speed Star** | No | 15% race bonus, big rainbows in Stamina...but probably still not worth it |
| Taiki Shuttle | June 4th, '26 | **Mile**<br>(Pace+) | MLB | Speed Bonus +1 and Skill Point<br>Bonus +1 when bond is 80+<br>Friendship Bonus (20-25%)<br>Hint Frequency (40-60%)<br>Hint Levels (2-4)<br>Speed Bonus +1<br>Power Bonus +1 (1LB+)<br>Training Eff. (5-10%) (3LB+) | Mile Straightaways<br>Productive Plan<br>Shifting Gears<br>Prepared to Pass<br>Mile Corners (can end 2nd chain)<br>**Mile Maven** | If Whale | Solid pick for Mile races, or parents for the same reason, especially fronts and paces As a speed card, it gives good rainbows when landing in speed training, only at MLB |
| Zenno Rob Roy (Event) | June 11th, '26 | Medium | MLB | Training Eff. (10%) when<br>bond is 80+<br>Friendship Bonus (30%)<br>Initial Stamina, Guts +30<br>Stamina Bonus +1 | Medium Corners<br>Medium Straightaways<br>Up-Tempo<br>**Clairvoyance** | Free | Could only see some use if you don't have good cards for medium parents Gold skill is a Field of View skill...not good |
| El Condor Pasa | June 11th, '26 | Pace | MLB | Training Eff. (5-30%) when<br>1-6 cards are in the same<br>facility<br>Friendship Bonus (20-25%)<br>Guts Bonus +1 (1LB+)<br>Race Bonus (5-10%) (3LB+) | Pace Chaser Straightaways<br>Prepared to Pass<br>Head-On<br>Preferred Position<br>**Speed Star** | With Mambo | Ideally, this card could give very strong trainings, potentially in guts/wit decks But for MANT, you get the most value out of it when at MLB because of her 10% race bonus being locked behind it Decent parent card for paces |
| Matikanetannhauser | June 11th, '26 | All-rounder | 1LB+ | Wit Friendship Recovery (5)<br>when bond is full<br>Friendship Bonus (25-35%)<br>Wit Friendship Recovery (3-5)<br>Speed Bonus +1<br>Wit Bonus +1 (1LB+) | Homestretch Haste<br>Nimble Navigator<br>Ramp Up<br>**It's On** | If Whale | This is a card that gives insane recovery when it lands on wit at full bond Downside: its low specialty priority (which, at least, is not 0) It is a strong wit card for scenarios that rely on energy recoveries (like Unity, MANT) Also provides good generalist skills |
| Air Groove | June 18th, '26 | Late<br>(Mile/Medium+) | MLB | Power Bonus +1 and Skill Point<br>Bonus when bond is at 80+<br>Friendship Bonus (20-25%)<br>Mood Effect (40-60%)<br>Specialty Priority (50-65)<br>Stamina Bonus +1 (1LB+)<br>Race Bonus (5-10%) (3LB+) | Late Surger Straightaways<br>Fearless<br>Take the Chance<br>Updrafters<br>Be Still<br>**Lie in Wait** | No | Could give good power trainings but sadly only useable in MANT at MLB, which is, generally, a bad investment for a power card right now |
| Special Week (Story) | June 25th, '26 *(est.)* | Long | MLB | Friendship Bonus (35%)<br>Mood Effect (30%)<br>Training Eff. (5%)<br>Specialty Priority (35)<br>Guts Bonus +1<br>Power Bonus +1 | Right-Handed<br>Long Straightaways<br>Pressure<br>Feature Act<br>Straightaway Recovery<br>Deep Breaths<br>**Overwhelming Pressure** | Free | About average free card, gold skill is kinda bad |
| The Throne's Assemblage | June 25th, '26 | Medium<br>(Pace/Late+) | MLB | Skill Point Bonus +2 when<br>bond is 80+<br>Friendship Bonus (25-35%)<br>Training Eff. (5%)<br>Wit Friendship Recovery (1-2)<br>Speed Bonus +1 (1LB+)<br>Race Bonus (5-10%) (3LB+) | Pace Chaser Straightaways<br>Medium Corners<br>Fighting Spirit<br>Full Throttle<br>**Refraction Arc** | If Whale | Ah...the Throne Incident This card is made for MANT, in every sense, funny thing is, there's only like a month left of it before the fourth scenario Great bonuses all over, also grants the Passion Zone status It's best to borrow it, unless you're willing to whale for it |
| El Condor Pasa | June 25th, '26 | **Pace**<br>(Medium+) | MLB | Speed Bonus +1<br>Specialty Priority (70)<br>Friendship Bonus (20%)<br>Mood Effect (30%)<br>Training Eff. (5%)<br>Race Bonus (10%)<br>Power Bonus +1 | Pace Chaser Corners<br>Pace Chser Straightaways<br>Prepared to Pass<br>Head-On<br>Up-Tempo | With Throne | None other to be released with an overpowered card like Throne, than an overpowered SR like El Overall pretty great card, to the likes of Sweep Tosho and Shinko Windy, excels for paces with all of her hints As always, not necessary to pull for her, but good if you get copies while pulling for others |
| Sakura Chiyono O (Event) | Late Jun '26 *(est.)* | Pace<br>Mile | MLB | Training Eff. (10%) when<br>bond is 80+<br>Friendship Bonus (25%)<br>Specialty Priority (65)<br>Guts Bonus +1<br>Speed Bonus +1 | Pace Chaser Corners<br>Pace Chaser Straightaways<br>Mile Straightaways<br>Head-On<br>Shifting Gears<br>**Stop the Gas!**<br>(Acceleration) | Free | Good card for pace parents No race bonus, once again, means it's bad for MANT |
| Nakayama Festa | Late Jun '26 *(est.)* | Gambler<br>(Late+) | MLB | Unique<br>Friendship Bonus (15-20%)<br>Mood Effect (40-60%)<br>Training Eff. (10-15%)<br>Wit Friendship Recovery (3-5)<br>Wit Bonus +1<br>Race Bonus (5-10%) (3LB+) | Late Surger Straightaways<br>Uma Stan<br>Nimble Navigator<br>Risky Business<br>Slick Surge<br>All I've Got<br>Steadfast<br>**Nothing Ventured**<br>(Risky Business)<br>(if you chose bottom option in 2nd chain) | With Maru | Very fitting to her character, this card is great for people who love the adrenaline of gambling, from her unique, to her Gold skill, everything is a fest(a) of dopamine Besides the gambling, this card offers a good set of bonuses and is great for MANT at MLB because of her 10% race bonus |
| Maruzensky | Late Jun '26 *(est.)* | All-rounder<br>**(Front+)** | 1LB+ | Training Eff. (5-25%) scaling<br>off facility level<br>Friendship Bonus (20-25%)<br>Speed Bonus +1<br>Power Bonus +1 (1LB+)<br>Mood Effect (15-30%) (3LB+) | Front Runner Corners<br>Front Runner Straightaways<br>Slipstream<br>Playtime's Over<br>Leader's Pride<br>Early Lead<br>Groundwork<br>Focus<br>Triple 777s<br>**Top Runner** | If Dolphin | Very good card that provides a strong bonus even at 0LB Good at 1LB, best at MLB Absolutely insane card for fronts with the amount of dedicated hints for them Has 5% race bonus, so useable in MANT |
| Ikuno Dictus (Rerun) | Early Jul '26 *(est.)* | Late<br>Medium | MLB | Training Eff. (10%)<br>Friendship Bonus (25-30%)<br>Race Bonus (5-15%)<br>Guts Bonus +1 (1LB+) | N/A | No | Too late to even consider getting it |
| Yukino Bijin (Rerun) | Early Jul '26 *(est.)* | Medium | MLB | Training Eff. (5%)<br>Mood Effect (40-60%)<br>Friendship Bonus (15-20%)<br>Wit Friendship Recovery (3-5)<br>Wit Bonus +1 (1LB+) | Medium Corners<br>Steadfast<br>Hydrate<br>**No Stopping Me!** | No | After Unity Cup, it's the only way to get No Stopping Me! for now Doesn't justify pulling for this at all, since we're nearing the end of the scenario |
| Manhattan Cafe | Early Jul '26 *(est.)* | Long | MLB | Stamina Bonus +2 when<br>bond is 80+<br>Training Eff. (5-10%)<br>Friendship Bonus (20-25%)<br>Skill Point Bonus +1 (1LB+)<br>Guts Bonus +1-2 (3LB+) | Long Corners<br>Long Straightaways<br>Highlander<br>Pressure<br>Deep Breaths<br>Passing Pro<br>**Of Calm Mind** | No | Another Manhattan Cafe stamina card that provides nice numbers when landing in stamina training It's a long card with a Gold recovery that reduces your speed starting the mid-race, useable by lates and ends in some niche cases It's the last banner of the scenario |
| Seiun Sky | Early Jul '26 *(est.)* | Front | MLB | Training Eff. (10%)<br>Friendship Bonus (20%)<br>Mood Effect (50%)<br>Wit Friendship Recovery (4)<br>Specialty Priority (50)<br>Skill Point Bonus +1 | Fast-Paced<br>Early Lead<br>Groundwork<br>Keeping the Lead<br>Second Wind | No | Pretty good wit SR, similar in performance as Fukukitaru, Marvelous Sunday, Tachyon and other viable wit SRs Last banner before Grand Live and an SR, so again, not necessary to pull but good if you get copies while pulling for others |

**Notes attached to individual cells:**

- **Symboli Rudolf** (Notable Bonuses): Rudolf's unique is very...unique It provides +10 of a stat type for every card of that stat type in your deck So in a deck with 3 speed, 2 wit and her, you'd get 30 speed, 20 wit and 10 stamina Pal and team cards give +2 to all stats
- **Seeking The Pearl** (Notable Bonuses): Unique is a special training effectiveness scaling that depends on your amount of maximum energy Downside is you'd be probably restricted to using cards that increase maximum energy to get a big boost out of it
- **Bamboo Memory** (Notable Bonuses): Bamboo Memory's unique...more friendship training when you have less energy, so it's a sort of gambler card where you gamble failure chance for bigger rainbows, just not worth it at all
- **Ikuno Dictus** (Notable Bonuses): Ikuno Dictus' unique gives her training effectiveness scaling with all of your cards' bond gauges, it's not bad, but it means it's a card that takes a bit to ramp up
- **Nakayama Festa** (Notable Bonuses): Let's gamble! Nakayama Festa's unique makes your training have a 20% chance of 0 failure rate

#### Grand Live

**Release timing (Global):** Late July '26

- Scenario gimmick: prepare the biggest music fest through song lessons, that require tokens to access (gained through training, and Light Hello's special scenario link) and give training bonuses, every 6 months you'll get to participate in Promotional Lives that increase your Hype Level and grant additional bonuses (skill points and raised stat caps) Additionally, Grand Live features new inheritance events that depend on your parents' sparks, providing extra stat caps based on blue and green sparks
- Scenario link: Smart Falcon (Full Speed Ahead! (At Full Speed)), Mihono Bourbon (Concentration (Focus)), Silence Suzuka (Trailblazer (Bright Future)), Agnes Tachyon (Prepared to Die (All That There Is)), None (Lane Legardemain), Light Hello
- Scenario skills: I Want To Win With You (Halfway to a Dream)
- Scenario spark: Grand Live Scenario (SPD/GUTS)

| Support Card | Date | Style/Distance | LB Breakpoints | Notable Bonuses | Notable Hints | Pull? | Notes |
|---|---|---|---|---|---|---|---|
| Mihono Bourbon | Late Jul '26 *(est.)* | Front<br>Medium | MLB | Training Eff. (10%) when<br>bond is 80+<br>Friendship Bonus (20%)<br>Skill Point Bonus +1<br>Speed Bonus +2 | Front Runner Corners<br>Front Runner Straightaways<br>Early Lead<br>Prudent Positioning<br>Focus<br>Fast-Paced<br>**Trackblazer** | Free | Pretty normal free card, not as good as her welfare wit card but works as a parent card for front runners |
| Light Hello | Late Jul '26 *(est.)* | All-rounder | 2LB+<br>R MLB > 0LB | Energy Reduction (30) when<br>rainbow training<br>Failure Protection (20-30%)<br>Energy Reduction (5-10%)<br>Training Eff. (5-10%) (1LB+) | **See Ya Later!** | **100 free pulls**<br>1LB<br>or<br>R MLB *(est.)* | Grand Live's pal card, if you thought Riko was a nice addition, this gives her a run for her money Gets 10% training effectiveness at 2LB, so anything beyond that is extra luxury regarding her date events |
| Agnes Tachyon | Late Jul '26 *(est.)* | **Pace**<br>Medium | 1LB+ | Friendship Bonus (20%) when<br>bond is full<br>Friendship Bonus (15-20%)<br>Specialty Priority (50-80)<br>Training Eff. (5%)<br>Speed Bonus +1 (1LB+)<br>Skill Points Bonus +1~2 (3LB+) | Pace Chaser Corners<br>Pace Chaser Straightaways<br>Medium Corners<br>Medium Straightaways<br>Attack Stance<br>Head-On<br>**Unstoppable** | **100 free pulls**<br>Yes *(est.)* | Great speed card, big rainbows when at full bond, powered by her high specialty priority Specially designed for pacers, and their parents, with great skill hints and a good Gold skill |
| Biwa Hayahide (Event) | Late Jul '26 *(est.)* | Pace<br>Long | MLB | Training Eff. (10%) when<br>bond is 80+<br>Friendship Bonus (20%)<br>Specialty Priority (50)<br>Skill Point Bonus +1<br>Stamina Bonus +2 | Pace Chaser Straightaways<br>Tail Held High<br>Head-On<br>Prepared to Pass<br>Inside Scoop<br>Stamina to Spare<br>Passing Pro<br>Faultless<br>**VIP Pass** | Free | Decent stamina card for longs, great for paces specifically |
| Tokai Teio | Late Jul '26 *(est.)* | All-rounder<br>(Pace+) | MLB | Unique<br>Friendship Bonus (25-30%)<br>Wit Friendship Recovery (3-5)<br>Speed Bonus +1 (1LB+)<br>Wit Bonus +1~2 (3LB+) | Pace Chaser Corners<br>Pace Chaser Straightaways<br>Corner Adept<br>Nimble Navigator<br>Prudent Positioning<br>With All My Soul<br>Preferred Position<br>**Professor of Curvature** | If Whale | Strong roaming wit card with pretty good hints, it's actually good at 1-3LB but really gets a boost at MLB with the +2 wit bonus for big numbers when training in wit |
| Twin Turbo | Late Jul '26 *(est.)* | Front | MLB | Friendship Bonus (35-40%)<br>Specialty Priority (50-65)<br>Power Bonus +1<br>Skill Point Bonus +1 (1LB+)<br>Speed Bonus +1~2 (3LB+) | Fast-Paced<br>Early Lead<br>Leader's Pride<br>Frantic State<br>Playtime's Over (ends 1st chain)<br>**1000% Output** | With Teio | Niche card for fronts in shorter races, with a Gold skill that has a stamina drain bigger than Mystifying Murmur, for example Tends to drop big stats in guts training |
| Silence Suzuka (Rerun) | Early Aug '26 *(est.)* | Front | MLB | Friendship Bonus (25-35%)<br>Mood Effect (45-55%)<br>Specialty Priority (50-65) | Left-Handed<br>Front Runner Corners<br>Front Runner Straightaways<br>Fast-Paced<br>Leader's Pride<br>Early Lead<br>Final Push<br>Focus<br>**Unrestrained** | No | Sadly got powercrept by Summer Maruzensky, but is an scenario link card for Grand Live, so she could see some use there |
| Smart Falcon | Early Aug '26 *(est.)* | Front<br>(Dirt+) | 1LB+ | Power Bonus +1<br>Friendship Bonus (15-20%)<br>Mood Effect (40-60%)<br>Stamina Bonus +1 (1LB+)<br>Race Bonus (5-10%) (3LB+) | Groundwork<br>Final Push<br>Corner Recovery<br>Focus (ends 1st chain)<br>**Center Stage**<br>(Prudent Positioning) | No | Genuinely just a Groundwork skill hint generator Has one Dirt skill so...there's that |
| Daiichi Ruby | Early Aug '26 *(est.)* | Late<br>Sprint/Mile | 1LB+ | Power Bonus +2 when<br>bond is 80+<br>Friendship Bonus (25-30%)<br>Training Eff. (5%)<br>Specialty Priority (50-80)<br>Skill Point Bonus +1 (1LB+) | Late Surger Corners<br>Late Surger Straightaways<br>Slick Surge<br>Fearless<br>Gap Closer<br>Sprinting Gear<br>**Lightning Speed** | No | First dual-distance-specific skill, for short races (so, sprints and miles), and it's not a bad one for Lates, but it's still not time for power cards to shine just yet |
| Shinko Windy (Event) | Late Aug '26 *(est.)* | **Dirt**<br>(Pace+) | MLB | Training Eff. (10%) when<br>bond is 80+<br>Friendship Bonus (35%)<br>Initial Speed, Power, Guts +20<br>Guts Bonus +1 | Prepared to Pass<br>At Full Speed<br>Dirt Bath<br>Full of Zeal<br>Unyielding<br>**Mud Master** | Free | Pretty good card for dirt races with a Gold green skill that increases speed and power in soft or heavy dirt tracks |
| Mejiro Palmer | Late Aug '26 *(est.)* | Front | 1LB+ | Unique<br>Friendship Bonus (25-35%)<br>Specialty Priority (50-80)<br>Skill Point Bonus +1 (1LB+) | Front Runner Corners<br>Playtime's Over<br>Keeping the Lead<br>Early Lead<br>Final Push<br>Groundwork<br>Passing Pro (ends 1st chain)<br>**Taking the Lead** | If Whale | Basically a card meant to give Taking the Lead to umas that don't have it in their kit But...Mihono Bourbon wit already does the job! Exactly, this is almost tailor-made for Valentines Bourbon, since the only other card that gives it until now is Twin Turbo Speed |
| Daitaku Helios | Late Aug '26 *(est.)* | Mile<br>(Front+) | MLB | Unique<br>Friendship Bonus (25-30%)<br>Race Bonus (5-10%)<br>Skill Point Bonus +1 (1LB+)<br>Speed Bonus +1~2 (3LB+) | Front Runner Straightaways<br>Mile Corners<br>Slipstream<br>Tail Held High<br>Frantic State<br>Shifting Gears<br>**In The Right Place!** | With Palmer | Very lacking card in general Also the first card to get Gold Slipstream skill |
| Fine Motion (Rerun) | Late Aug '26 *(est.)* | **All-Rounder (Pace+)** | 3LB+ | Friendship Bonus (32-37.5%)<br>Training Eff. (10-15%)<br>Race Bonus (5-10%)<br>Wit Friendship Recovery (3-5)<br>Wit Bonus +1 (1LB+)<br>Mood Effect (15-30%) (3LB+) | Right-Handed<br>Nimble Navigator<br>Corner Adept<br>**Speed Star**<br>(Prepared to Pass) | If Dolphin | If you haven't gotten her, it's a good time to pull for her now If you have her at 2LB or less, also a good time to pull If you have her at 3LB, consider pulling if you don't have Maruzensky or if you need more copies of her She's still alive and well, very valuable banner |
| Maruzensky (Rerun) | Late Aug '26 *(est.)* | All-rounder<br>**(Front+)** | 1LB+ | Training Eff. (5-25%) scaling<br>off facility level<br>Friendship Bonus (20-25%)<br>Speed Bonus +1<br>Power Bonus +1 (1LB+)<br>Mood Effect (15-30%) (3LB+) | Front Runner Corners<br>Front Runner Straightaways<br>Slipstream<br>Playtime's Over<br>Leader's Pride<br>Early Lead<br>Groundwork<br>Focus<br>Triple 777s<br>**Top Runner** | If Dolpin | Still a good card that provides a strong bonus even at 0LB Good at 1LB, best at MLB Great card for fronts Very valuable banner if you don't have Maru nor Finemo MLB |
| Daiichi Ruby (Rerun) | Late Aug '26 *(est.)* | Late<br>Sprint/Mile | 1LB+ | Power Bonus +2 when<br>bond is 80+<br>Friendship Bonus (25-30%)<br>Training Eff. (5%)<br>Specialty Priority (50-80)<br>Skill Point Bonus +1 (1LB+) | Late Surger Corners<br>Late Surger Straightaways<br>Slick Surge<br>Fearless<br>Gap Closer<br>Sprinting Gear<br>**Lightning Speed** | No | She didn't even have time to set in the meta Still very poor timing for this card (like other power cards) |
| Symboli Kris S | Early Sep '26 *(est.)* | **Late<br>Long** | 1LB+ | Guts Bonus +2 when<br>bond is 80+<br>Friendship Bonus (25-30%)<br>Training Eff. (5%)<br>Skill Point Bonus +1 (1LB+)<br>Mood Effect (15-30%) (3LB+) | Late Surger Corners<br>Long Straightaways<br>1,500,000 CC<br>Slick Surge<br>Fearless<br>Devil-May-Care<br>Corner Recovery<br>Passing Pro<br>**Lose Yourself** | If Whale | Strong stamina card for lates in long races, its Gold skill is almost a must for any Late in Long races and it doesn't appear in another SSR for a while |
| Mejiro Ardan (Event) | Early Sep '26 *(est.)* | Pace | MLB | Power Bonus +2 when<br>bond is 80+<br>Friendship Bonus (20%)<br>Mood Effect (60%)<br>Speed Bonus +1 | Left-Handed<br>Pace Chaser Corners<br>Soft Step<br>Preferred Position<br>**Race Planner** | Free | Solid free speed card that is capable of dropping big stats in rainbow training |
| Yaeno Muteki | Early Sep '26 *(est.)* | Medium<br>(Pace+) | MLB | Guts Bonus +3 when<br>bond is full<br>Initial Guts +25-30<br>Initial Speed, Power +15-20<br>Skill Point Bonus +1 (1LB+)<br>Training Eff. (5-10%) (3LB+) | Left-Handed<br>Medium Corners<br>Medium Straightaways<br>Ramp Up<br>Tail Held High<br>Homestretch Haste<br>Prepared to Pass<br>Up-Tempo<br>Hydrate<br>**Killer Tunes** | No | Not a very strong card per se, but gives a lot of Guts if you're into that Just like her power card, her skill hints are very valuable for paces in medium tracks |
| Oguri Cap | Early Sep '26 *(est.)* | **Pace**<br>(Medium+) | MLB | All Support Cards bond +5<br>Friendship Bonus (25-35%)<br>Wit Friendship Recovery (3-5)<br>Training Eff. (5-10%)<br>Speed Bonus +1 (1LB+)<br>Wit Bonus +1~2 (3LB+) | Pace Chaser Corners<br>Pace Chaser Straightaways<br>Nimble Navigator<br>Corner Adept<br>Head-On<br>Straight Descent<br>All I've Got<br>Up-Tempo<br>Firm Step<br>Triple 777s<br>**Steady Advance** | If Whale | Great for pace parents, especially for medium tracks Other than that it's a card that provides good numbers when in wit training, but nothing other good wit SSRs don't do already |
| Mr. C.B. (Rerun) | Late Sep '26 *(est.)* | **End** | 1LB+ | Wit Bonus +1 and Skill Point<br>Bonus +1 when bond is 80+<br>Friendship Bonus (25-30%)<br>Wit Friendship Recovery (3-5)<br>Speed Bonus +1<br>Training Eff. (5%)<br>Wit Bonus +1 (1LB+)<br>Mood Effect (15-30%) (3LB+) | Medium Corners<br>Homestretch Haste<br>Tail Held High<br>Straightaway Spurt<br>Early Start<br>Corner Recovery<br>**Daring Strike** | If Dolphin | Another super valuable banner if you don't have neither Mr C.B. nor Super Creek, or if you want or need more copies of them |
| Super Creek (Rerun) | Late Sep '26 *(est.)* | **All-rounder** | 3LB+ | Friendship Bonus (32-37.5%)<br>Training Eff. (10-15%)<br>Race Bonus (5-10%)<br>Specialty Priority (40-55)<br>Stamina Bonus +1 (1LB+) | Ramp Up<br>Homestretch Haste<br>Corner Recovery<br>**Swinging Maestro** | If Dolphin | Another super valuable banner if you don't have neither Mr C.B. nor Super Creek, or if you want or need more copies of them |
| Eishin Flash | Late Sep '26 *(est.)* | Late | MLB | Power Bonus +1 and Skill Point<br>Bonus +1 when bond is 80+<br>Training Eff. (5-10%)<br>Friendship Bonus (15-20%)<br>Specialty Priority (50-65)<br>Power Bonus +1 (1LB+)<br>Speed Bonus +1~2 (3LB+) | Late Surger Corners<br>Late Surger Straightaways<br>Position Pilfer<br>Take the Chance<br>Soft Step<br>**Incisive Slash** | If Whale | Basically her SR on steroids with +2 speed, +2 power, +1 skill point bonuses at MLB So pretty decent when in speed training, and very good late skills |
| Sakura Laurel (Event) | Early Oct '26 *(est.)* | Late<br>Long | MLB | Stamina Bonus +2 when<br>bond is at +80<br>Friendship Bonus (20%)<br>Mood Effect (50%)<br>Guts Bonus +1 | Long Corners<br>Devil-May-Care<br>A Small Breather<br>Deep Breaths<br>Be Still<br>**Dauntless** | Free | Good free stamina card for lates in long tracks |
| Air Groove | Early Oct '26 *(est.)* | Late | 1LB+ | Speed Bonus +1 and Skill Point<br>Bonus +1 when bond is 80+<br>Friendship Bonus (25-30%)<br>Training Eff. (5%)<br>Specialty Priority (50-65)<br>Wit Friendship Recovery (3-5)<br>Wit Bonus +1<br>Speed Bonus +1 (1LB+)<br>Mood Effect (15-30%) (3LB+) | Late Surger Straightaways<br>Position Pilfer<br>Fearless<br>Updrafters<br>**Fast & Furious** | If Whale+ | Similar in power as Oguri wit, but for lates instead |
| Narita Brian | Early Oct '26 *(est.)* | Pace/Late<br>Medium/Long | MLB | Training Eff. (5-25%) scaling<br>off facility level<br>Friendship Bonus (15-20%)<br>Specialty Priority (50-65)<br>Skill Point Bonus +1 (1LB+)<br>Stamina Bonus +1~2 (3LB+) | Right-Handed<br>Long Straightaways<br>Outer Swell<br>Firm Step<br>Tooth and Tail<br>True Worth<br>Preferred Position<br>Faultless<br>**Hot Pursuit** | With Air Groove | Same unique as Maruzensky speed, but with a lot weaker bonuses and very specific skill hints |
| Light Hello (Rerun) | Early Oct '26 *(est.)* | All-rounder | 2LB+<br>R MLB > 0LB | Energy Reduction (30) when<br>rainbow training<br>Failure Protection (20-30%)<br>Energy Reduction (5-10%)<br>Training Eff. (5-10%) (1LB+) | **See Ya Later!** | No | Kinda like Riko rerun situation, unless you don't have her 2LB+, there's not much of a reason to pull Even if you have her at 0LB, there's no need to bring it any higher if you don't wanna splurge |
| Mayano Top Gun (Rerun) | Early Oct '26 *(est.)* | All-rounder<br>(Front/Pace+) | 3LB+ | Friendship Bonus (20-25%)<br>Mood Effect (40-50%)<br>Training Eff. (5%)<br>Power Bonus +1<br>Speed Bonus +1 (1LB+)<br>Specialty Priority (40-80) (3LB+) | Corner Adept<br>Straightaway Adept<br>Nimble Navigator<br>Head-On<br>**Restless** | No | Still a good card, but it got slightly powercrept with Tachyon and Maru |
| Yamanin Zephyr | Late Oct '26 *(est.)* | Pace<br>Mile/Medium | MLB | Skill Point Bonus +2 when<br>bond is at 80+<br>Training Eff. (10-15%)<br>Friendship Bonus (15-20%)<br>Guts Bonus +1<br>Speed Bonus +1 (1LB+) | Mile Corners<br>Medium Corners<br>Shifting Gears<br>Unyielding Spirit<br>Ambitions<br>Slipstream<br>**Winds of Change** | No | Nothing too exciting except the 15% training effectiveness and skill point bonus |
| Grass Wonder (Event) | Late Oct '26 *(est.)* | Long | MLB | Training Eff. (10%) when<br>bond is 80+<br>Friendship Bonus (25%)<br>Power Bonus +1 | Long Corners<br>Faultless<br>Pressure<br>Cooldown | Free | Sadly a power card, doesn't have a lot going on |
| Sweep Tosho | Late Oct '26 *(est.)* | End | MLB | Specialty Priority (40) when<br>bond is 80+<br>Friendship Bonus (25-30%)<br>Mood Bonus (20-30%)<br>Specialty Priority (20-35)<br>Wit Friendship Recovery (3-5)<br>Skill Point Bonus +1 (1LB+)<br>Wit Bonus +1~2 (3LB+) | End Closer Straightaways<br>Slipstream<br>Breakthrough Plan<br>Witful<br>After-School Stroll<br>**Unrivaled Wits** | **50 Free Pulls**<br>With Spe *(est.)* | Wit card for ends that feels slightly weaker or less universal than Mr C. B. wit, has great rainbows but that's about it |
| Special Week | Late Oct '26 *(est.)* | Medium | MLB | Mood Effect (60%) when<br>friendship training<br>Friendship Bonus (15-20%)<br>Stamina Bonus +1<br>Skill Points Bonus +1<br>Guts Bonus +1 (1LB+)<br>Training Eff. (5-10%) (3LB+) | Left-Handed<br>Homestretch Haste<br>Nimble Navigator<br>Up-Tempo<br>All I've Got<br>Fighting Spirit<br>Feature Act<br>Soft Step<br>Extra Tank<br>**No Stopping Me!** | **50 Free Pulls**<br>If Whale+ *(est.)* | Most of this card's value is in the No Stopping Me! hint, after Unity Cup, only Yukino Bijin wit and her hand it out She also has decent enough rainbows |
| Tokai Teio (Rerun) | Early Nov '26 *(est.)* | All-rounder<br>(Pace+) | MLB | Unique<br>Friendship Bonus (25-30%)<br>Wit Friendship Recovery (3-5)<br>Speed Bonus +1 (1LB+)<br>Wit Bonus +1~2 (3LB+) | Pace Chaser Corners<br>Pace Chaser Straightaways<br>Corner Adept<br>Nimble Navigator<br>Prudent Positioning<br>With All My Soul<br>Preferred Position<br>**Professor of Curvature** | If Whale+ | Not necessary to pull for this card, as Mejiro Ramonu wit is close to release by this time |
| Agnes Tachyon (Rerun) | Early Nov '26 *(est.)* | **Pace**<br>Medium | 1LB+ | Friendship Bonus (20%) when<br>bond is full<br>Friendship Bonus (15-20%)<br>Specialty Priority (50-80)<br>Training Eff. (5%)<br>Speed Bonus +1 (1LB+)<br>Skill Points Bonus +1~2 (3LB+) | Pace Chaser Corners<br>Pace Chaser Straightaways<br>Medium Corners<br>Medium Straightaways<br>Attack Stance<br>Head-On<br>**Unstoppable** | If Dolphin | If you need your deck to get slightly better, you could consider pulling here if you didn't during the 1.5 Anniversary banner |
| K. S. Miracle | Early Nov '26 *(est.)* | **Pace**<br>Sprint | 1LB+ | Power Bonus +2 when<br>bond is at 80+<br>Mood Bonus (40-50%)<br>Friendship Bonus (25-30%)<br>Specialty Priority (50-65)<br>Guts Bonus +1 (1LB+) | Sprint Corners<br>Pace Chaser Straightaways<br>Attack Stance<br>Countermeasure<br>Light as a Feather<br>Updrafters<br>**Neck and Neck** | If Whale | Remember the Daiwa power card from a while back? This is her but better Gold skill is a must for paces, and with all other sprint hints, it's almost a guaranteed slot for paces that run sprint races |
| Matikanefukukitaru (Rerun) | Late Nov '26 *(est.)* | All-rounder<br>(Late+) | 3LB+ | Mood Effect (35-45%)<br>Friendship Bonus (15-20%)<br>Failure Reduction (10%)<br>Energy Reduction (5-10%)<br>All Initial Stats (+10-30)<br>Training Eff. (5-10%) (1LB+)<br>Race Bonus (5-10%) (3LB+) | Late Surger Corners<br>A Small Breather<br>Triple 777s<br>**Super Lucky Seven**<br>(Lucky Seven) | No | Fukukitaru's life expectancy is about to come to and end Don't feel compelled to pull for her anymore |
| Taiki Shuttle (Rerun) | Late Nov '26 *(est.)* | **Mile**<br>(Pace+) | MLB | Speed Bonus +1 and Skill Point<br>Bonus +1 when bond is 80+<br>Friendship Bonus (20-25%)<br>Hint Frequency (40-60%)<br>Hint Levels (2-4)<br>Speed Bonus +1<br>Power Bonus +1 (1LB+)<br>Training Eff. (5-10%) (3LB+) | Mile Straightaways<br>Productive Plan<br>Shifting Gears<br>Prepared to Pass<br>Mile Corners (can end 2nd chain)<br>**Mile Maven** | If Whale | Still good pick for Mile races Training-wise, it gives good rainbows when landing in speed training, only at MLB |
| Hishi Akebono (Event) | Late Nov '26 *(est.)* | Sprint | MLB | Wit Bonus +2 when<br>bond is 80+<br>Friendship Bonus (25%)<br>Mood Effect (30%)<br>Wit Friendship Recovery (5)<br>Skill Point Bonus +1 | Sprint Corners<br>Final Push<br>Countermeasure<br>Sprinting Gear<br>Hydrate<br>**Plan X** | Free | Good welfare wit for sprint races during Grand Live |
| Biko Pegasus | Late Nov '26 *(est.)* | Late<br>Sprint | 1LB+ | Unique<br>Friendship Bonus (15-20%)<br>Mood Bonus (40-50%)<br>Power Bonus +1<br>Skill Point Bonus +1 (LB1+) | Late Surger Corners<br>Nimble Navigator<br>Position Pilfer<br>Slick Surge<br>Fearless<br>Sprinting Gear<br>Mighty Leap<br>**Incisive Slash** | No | Has the same issue as Seeking the Pearl speed, it's just too niche to make proper use of the buff Plus this time it's sadly on a power card... |
| Marvelous Sunday | Late Nov '26 *(est.)* | Medium/Long<br>(Late+) | 1LB+ | Training Eff. (15%) when<br>bond is full<br>Friendship Bonus (20-25%)<br>Specialty Priority (50-65)<br>Speed Bonus +1<br>Power Bonus +1<br>Skill Point Bonus +1 (1LB+)<br>Mood Effect (15-30%) (3LB+) | Long Straightaways<br>Tail Held High<br>All I've Got<br>Eager<br>Take the Chance<br>Devil-May-Care<br>Straightaway Recovery<br>**Indomitable** | If Whale | Speed card on a similar level as Kitasan or Agnes Tachyon with a great 15% training effectiveness when you fill her friendship gauge If anything dragged her down, it's her skill hints, we're nearing a meta where cards are meta-defining based on their hints Also, 2nd Anni is very near! |
| Nishino Flower (Rerun) | Early Dec '26 *(est.)* | Pace<br>Mile | 3LB+ | Wit Bonus +3 when<br>bond is full<br>Training Eff. (5%)<br>Friendship Bonus (25-30%)<br>Wit Friendship Recovery (3-5)<br>Speed Bonus +1 (1LB+) | Pace Chaser Corners<br>Updrafters<br>Shifting Gears<br>**Determined Descent** | **6 Free Pulls**<br>No *(est.)* | Last banner before the 2nd Anniversary, best to save up! |
| Maruzensky (Rerun) | Early Dec '26 *(est.)* | All-rounder<br>**(Front+)** | 1LB+ | Training Eff. (5-25%) scaling<br>off facility level<br>Friendship Bonus (20-25%)<br>Speed Bonus +1<br>Power Bonus +1 (1LB+)<br>Mood Effect (15-30%) (3LB+) | Front Runner Corners<br>Front Runner Straightaways<br>Slipstream<br>Playtime's Over<br>Leader's Pride<br>Early Lead<br>Groundwork<br>Focus<br>Triple 777s<br>**Top Runner** | **6 Free Pulls**<br>No *(est.)* | Last banner before the 2nd Anniversary, best to save up! (This is her third time around... you should've already gotten her) |

**Notes attached to individual cells:**

- **Tokai Teio** (Notable Bonuses): Same as Ikuno Dictus stamina, Tokai Teio wit gets training effectiveness scaling off your cards' bonds, so again, is a card that takes a while to ramp up but gives good stats when achieving its purpose
- **Mejiro Palmer** (Notable Bonuses): Reverse Bamboo Memory guts unique, it gives more training effectiveness the more energy you have Ideally you'd want a lot of energy all the time, but I don't know if that's viable in a stamina deck...
- **Daitaku Helios** (Notable Bonuses): Same unique as Symboli Rudolf stamina, gives +10 to each stat for every card of its type in your deck (+2 to every stat for pal/group cards) So 3 speed + 2 wit + Light Hello decks would get +32 speed, +22 wit, +2 to every other stat
- **Tokai Teio (Rerun)** (Notable Bonuses): Same as Ikuno Dictus stamina, Tokai Teio wit gets training effectiveness scaling off your cards' bonds, so again, is a card that takes a while to ramp up but gives good stats when achieving its purpose
- **Biko Pegasus** (Notable Bonuses): Same unique as Seeking the Pearl speed, gives training effectiveness based off maximum energy capacity So you'd probably need a pretty niche deck to make use of it

#### Grand Masters

**Release timing (Global):** Early Dec '26

- Scenario gimmick: every turn you can acquire fragments (one out of three colors - blue, yellow, red; and six types, one for each stat and one for skill points, totals 18 types of fragments) doing any action (including resting and dating), fragments give +1 bonus stat to their respective type, then, two fragments combine into a shard, that gives +2 or 3 bonus to its type, then two shards will combine into a crystal, and two crystals combine into a Goddess' Wisdom, which gives permanent bonuses (training effectiveness, hint chances, extra events, discounted energy, support event buffs...) and a one-turn buff depending on the color of the Goddess' Wisdom, then your fragments will reset and you can start getting them again Besides, you'll run in three different races each at the end of each year, getting extra bonuses based off the amount of Goddess' Wisdom you get before the races
- Scenario link: Ancestors & Guides
- Scenario skills: Wisdom of the Sun (Blessing of the Sun), Wisdom of the Ocean (Blessing of the Ocean), Wisdom of the Land (Blessing of the Land), Firm Track Demon, In Body and Mind
- Scenario spark: Grand Masters Scenario (SPD/PWR)

| Support Card | Date | Style/Distance | LB Breakpoints | Notable Bonuses | Notable Hints | Pull? | Notes |
|---|---|---|---|---|---|---|---|
| Katsuragi Ace (Event) | Early Dec '26 *(est.)* | Front<br>Medium | MLB | Friendship Bonus (25%)<br>Mood Effect (30%)<br>Skill Point Bonus +1<br>Speed Bonus +2<br>Specialty Priority (35) | Front Runner Corners<br>Medium Straightaways<br>Fast-Paced<br>Leader's Pride<br>Ambitions<br>Firm Step<br>Final Push<br>Groundwork<br>**Unyielding** | Free | Solid free card for front runners Nothing out of the ordinary but definitely useable if you lack the resources |
| Symboli Kris S (Event) | Early Dec '26 *(est.)* | Late<br>Medium | MLB | Guts Bonus +2 when<br>bond is 80+<br>Friendship Bonus (20%)<br>Training Eff. (10%)<br>Skill Point Bonus +1<br>Specialty Priority (65) | Late Surger Corners<br>Medium Corners<br>All I've Got<br>Fighting Spirit<br>Fearless<br>**Burning Soul** | Free | Eh guts card Useable for medium decks |
| Mejiro Ramonu | Early Dec '26 *(est.)* | **Mile<br>Medium** | 3LB+ | Training Eff. (4%) per speed<br>skill, up to 5 skills (max. 20%)<br>Friendship Bonus (25-30%)<br>Wit Friendship Recover (3-5)<br>Specialty Priority (35-50)<br>Skill Point Bonus +1 (1LB+)<br>Wit Bonus +1~2 (3LB+) | Mile Corners<br>Mile Straightaways<br>Medium Corners<br>Medium Straightaways<br>Straightaway Adept<br>Shifting Gears<br>Unyielding Spirit<br>Graceful Step<br>Firm Step<br>Fighting Spirit<br>All I've Got<br>**Ascendance** | **120 Free Pulls**<br>Yes *(est.)* | First powercreep we're seeing in wit cards Some people can start benching Fine Motion now This card alone can get you to 1000+ wit easily |
| Sirius Symboli (Rerun) | Late Dec '26 *(est.)* | Late<br>Medium | MLB | Friendship Training (20-35%)<br>Mood Effect (40-60%)<br>Wit Friendship Recovery (3-5)<br>Speed Bonus +1<br>Wit Bonus +1 (1LB+)<br>Race Bonus (5-10%) (3LB+) | Late Surger Straightaways<br>Medium Corners<br>Be Still<br>Playtime's Over (ends 1st chain)<br>**From The Brink**<br>(Take The Chance) | **11 Free Pulls**<br>No *(est.)* | Not worth it anymore |
| Oguri Cap (Rerun) | Late Dec '26 *(est.)* | Pace<br>(Medium+) | MLB | All Support Cards bond +5<br>Friendship Bonus (25-35%)<br>Wit Friendship Recovery (3-5)<br>Training Eff. (5-10%)<br>Speed Bonus +1 (1LB+)<br>Wit Bonus +1~2 (3LB+) | Pace Chaser Corners<br>Pace Chaser Straightaways<br>Nimble Navigator<br>Corner Adept<br>Head-On<br>Straight Descent<br>All I've Got<br>Up-Tempo<br>Firm Step<br>Triple 777s<br>**Steady Advance** | **11 Free Pulls**<br>No *(est.)* | Sadly sandwiched between Mejiro Ramonu and Ancestors banners, not worth to pull now |
| Ancestors & Guides | Late Dec '26 *(est.)* | **All-rounder** | 1LB+ | Friendship Bonus (10%), Mood<br>Effect (15%) and Skill Point<br>Bonus +1 when bond is full<br>Friendship Bonus (15%-20%)<br>Speed Bonus +1<br>Power Bonus +1<br>Wit Friendship Recovery (1-2)<br>Stamina Bonus +1 (1LB+)<br>Training Eff. (5-10%) (3LB+) | Sprint Corners<br>Mile Corners<br>Medium Corners<br>Long Straightaways<br>Corner Adept<br>Straightaway Adept<br>Ramp Up<br>Uma Stan<br>Rapid<br>Triple 7s<br>**Divine Speed** | **10 Free Pulls**<br>1LB+ *(est.)* | Grand Master's scenario link card, and it doesn't have an R counterpart like other pal cards we've had so far Absolute bonkers of a card, and like the other group cards, has the passion zone buff that removes Night Owl and Slacker |
| Tokai Teio (Event) | Early Jan '27 *(est.)* | Pace<br>Medium | MLB | Training Eff. (10%) when<br>bond is 80+<br>Friendship Bonus (20%)<br>Speed Bonus +1<br>Power Bonus +2 | Pace Chaser Corners<br>Pace Chaser Straightaways<br>Nimble Navigator<br>Prudent Positioning<br>**Lightning Step** | Free | Meh free card, decent statstick and nothing else |
| Nice Nature | Early Jan '27 *(est.)* | All-rounder | MLB | Power Bonus +3 when<br>bond is full<br>Friendship Bonus (25-30%)<br>Skill Point Bonus +1<br>Hint Frequency (40-50%)<br>Hint Levels (2-3)<br>Stamina Bonus +1 (1LB+)<br>Mood Effect (15-30%) (3LB+) | Corner Adept<br>Straightaway Adept<br>Homestretch Haste<br>Nimble Navigator<br>Uma Stan<br>Slipstream<br>Tail Held High<br>Ramp Up<br>Slick Surge<br>**In The Right Place!** | With McQueen | This is just a card for parents |
| Mejiro McQueen | Early Jan '27 *(est.)* | Long<br>(Front+) | 1LB+ | Stamina Bonus +3 when<br>bond is full<br>Friendship Bonus (25-35%)<br>Specialty Priority (50-80)<br>Skill Point Bonus +1 (1LB+)<br>Guts Bonus +1~2 (3LB+) | Long Corners<br>Long Straightaways<br>Feature Act<br>Early Lead<br>True Worth<br>Corner Recovery<br>Straightaway Recovery<br>Extra Tank<br>Stay the Course<br>Faultless<br>**Ahead of the Game** | If Whale | This is one of the best stamina cards released so far and is pretty strong for any long race, if you can afford the luxury Her gold skill provides recovery and speed Gives a lot of stats on rainbow training |
| Eishin Flash (Rerun) | Early Jan '27 *(est.)* | Late | MLB | Power Bonus +1 and Skill Point<br>Bonus +1 when bond is 80+<br>Training Eff. (5-10%)<br>Friendship Bonus (15-20%)<br>Specialty Priority (50-65)<br>Power Bonus +1 (1LB+)<br>Speed Bonus +1~2 (3LB+) | Late Surger Corners<br>Late Surger Straightaways<br>Position Pilfer<br>Take the Chance<br>Soft Step<br>**Incisive Slash** | No | Noticed the amount of hints we're getting in new cards? This card just fell off Is a good statstick nonetheless |
| Air Groove (Rerun) | Early Jan '27 *(est.)* | Late | 1LB+ | Speed Bonus +1 and Skill Point<br>Bonus +1 when bond is 80+<br>Friendship Bonus (25-30%)<br>Training Eff. (5%)<br>Specialty Priority (50-65)<br>Wit Friendship Recovery (3-5)<br>Wit Bonus +1<br>Speed Bonus +1 (1LB+)<br>Mood Effect (15-30%) (3LB+) | Late Surger Straightaways<br>Position Pilfer<br>Fearless<br>Updrafters<br>**Fast & Furious** | No | Same as Eishin Flash, her time was cut short |
| Symboli Rudolf | Late Jan '27 *(est.)* | Medium<br>(Pace+) | MLB | Speed Bonus +2 when<br>bond is 80+<br>Training Eff. (5-10%)<br>Friendship Bonus (15-20%)<br>Power Bonus +1 (1LB+)<br>Guts Bonus +1~2 (3LB+) | Right-Handed<br>Medium Corners<br>Fighting Spirit<br>Eager<br>Ambitions<br>Tooth and Tail<br>Firm Step<br>Mold Breaker<br>Corner Recovery<br>Corner Adept<br>**Swinging Maestro** | No | Statstick guts card, mostly Has decent hints, including Swinging Maestro which is nice to have on a Medium (and sometimes Long) card No reason to pull for it anyways |
| Ikuno Dictus (Event) | Late Jan '27 *(est.)* | Late | MLB | Stamina Bonus +2 when<br>bond is 80+<br>Friendship Bonus (20%)<br>Mood Effect (50%)<br>Specialty Priority (50)<br>Power Bonus +1 | Late Surger Straightaways<br>Position Pilfer<br>**Hard Worker** | Free | Probably gives good rainbows in power, other than that...eh... |
| Sakura Laurel | Late Jan '27 *(est.)* | Late | 1LB+ | Stamina Bonus +1 per recovery<br>skill, up to 3 skills (max. +3)<br>Friendship Bonus (25-30%)<br>Mood Effect (20-30%)<br>Training Eff. (5%)<br>Skill Point Bonus +1 (1LB+) | Overflowing Passion<br>On the Move<br>Great Haste<br>Corner Recovery<br>Straightaway Recovery<br>**On Your Left!** | **80 Free Pulls**<br>No *(est.)* | Does not dethrone Nice Nature wit as an On Your Left! provider Unique is very weak for a stamina card |
| Mihono Bourbon | Late Jan '27 *(est.)* | Front | 3LB+ | Unique<br>Training Eff. (10-15%)<br>Friendship Bonus (25-30%)<br>Specialty Priority (50-65)<br>Wit Friendship Recovery (3-5)<br>Speed Bonus +1 (1LB+)<br>Wit Bonus +1~2 (3LB+) | Left-Handed<br>Fast-Paced<br>Early Lead<br>Final Push<br>Second Wind<br>Highlander<br>Groundwork<br>**Unshakeable Stance** | **80 Free Pulls**<br>If Whale *(est.)* | Dedicated wit card for fronts Gold groundwork Sadly can't be used with her other wit card |
| Yamanin Zephyr (Rerun) | Early Feb '27 *(est.)* | Pace<br>Mile/Medium | MLB | Skill Point Bonus +2 when<br>bond is at 80+<br>Training Eff. (10-15%)<br>Friendship Bonus (15-20%)<br>Guts Bonus +1<br>Speed Bonus +1 (1LB+) | Mile Corners<br>Medium Corners<br>Shifting Gears<br>Unyielding Spirit<br>Ambitions<br>Slipstream<br>**Winds of Change** | No | Still pretty underwhelming |
| K. S. Miracle (Rerun) | Early Feb '27 *(est.)* | **Pace**<br>Sprint | 1LB+ | Power Bonus +2 when<br>bond is at 80+<br>Mood Bonus (40-50%)<br>Friendship Bonus (25-30%)<br>Specialty Priority (50-65)<br>Guts Bonus +1 (1LB+) | Sprint Corners<br>Pace Chaser Straightaways<br>Attack Stance<br>Countermeasure<br>Light as a Feather<br>Updrafters<br>**Neck and Neck** | No | A good card still, gets outclassed relatively soon, though |
| Jungle Pocket | Early Feb '27 *(est.)* | Late<br>Medium | MLB | Speed Bonus +3 when<br>bond is full<br>Friendship Bonus (25-30%)<br>Race Bonus (5-10%)<br>Specialty Priority (50-65)<br>Skill Point Bonus +1<br>Power Bonus +1 (1LB+)<br>Training Eff. (5-10%) (3LB+) | Medium Corners<br>Medium Straightaways<br>Corner Adept<br>Slick Surge<br>Witful<br>Take the Chance<br>Rising Passion<br>Devil-May-Care<br>All I've Got (ends 2nd chain)<br>**Surging Beat** | If Whale | Strong only at MLB due to her training effectiveness being locked behind it Gambling event chain, so you could end with no gold skill Good card nonetheless |
| Vodka (Event) | Early Feb '27 *(est.)* | Late | MLB | Training Eff. (10%) when<br>bond is 80+<br>Friendship Bonus (15%)<br>Mood Effect (30%)<br>Guts Bonus +1 | Position Pilfer<br>Full-Throttle<br>Take the Chance<br>Nimble Navigator<br>**15,000,000 CC** | Free | Not great, not abysmally bad It's free anyways |
| Daiwa Scarlet | Early Feb '27 *(est.)* | Front<br>Medium | 1LB+ | Training Eff. (max 20%) based<br>on combined facility level<br>Friendship Bonus (20-25%)<br>Specialty Priority (50-80)<br>Skill Point Bonus +1<br>Guts Bonus +1 (1LB+) | Medium Straightaways<br>Leader's Pride<br>Steadfast<br>Dodging Danger<br>With All My Soul<br>Up-Tempo<br>Fast-Paced<br>**Untouchable Shadow** | No | She's just lacking numbers, really |
| Aston Machan | Early Feb '27 *(est.)* | Sprint<br>(Front+) | 1LB+ | Mood Effect (60%) when<br>friendship training<br>Training Eff. (10-15%)<br>Friendship Bonus (15-20%)<br>Specialty Priority (50-65)<br>Wit Friendship Recovery (3-5)<br>Skill Point Bonus +1<br>Wit Bonus +1 (1LB+) | Sprint Corners<br>Sprint Straightaways<br>Early Lead<br>Dodging Danger<br>Sprinting Gear<br>Meticuluous Measures<br>Light as a Feather<br>**Concentration** | No | Big rainbows Probably only good for sprint races Gold skill is pretty underwhelming |
| Silence Suzuka | Late Feb '27 *(est.)* | Front | MLB | Mood Effect (15%)<br>Training Eff. (10%)<br>Friendship Bonus (30%)<br>Specialty Priority (50)<br>Skill Point Bonus +1 | Left-Handed<br>Front Runner Corners<br>Front Runner Straightaways<br>Fast-Paced<br>Leader's Pride<br>Rushing in Blind | No | As always, not necessary to pull for this card, but it's a good addition to the speed SR roster She's only lacking a couple bonuses to speed or power to make it top tier But definitely useable if you get her to MLB |
| TM Opera O | Late Feb '27 *(est.)* | Long<br>(Pace+) | MLB | Wit Bonus +2 when<br>bond is 80+<br>Friendship Bonus (15-20%)<br>Mood Effect (40-60%)<br>Wit Friendship Recovery (3-5)<br>Training Eff. (5-10%) (1LB+)<br>Speed Bonus +1~2 (3LB+) | Long Corners<br>Long Straightaways<br>Corner Adept<br>Straightaway Adept<br>Inside Scoop<br>Feature Act<br>Lock On<br>True Worth<br>Straightaway Recovery<br>Deep Breaths<br>**Monster<br>Beeline Burst** | No | First double-gold skill support card, yippee !! But she's kinda meh Could see some use for a handful of pacers that run longs (the next long CM should be like 4 months after this card drops) |
| Mayano Top Gun | Late Feb '27 *(est.)* | Pace | 1LB+ | Training Eff. (10%) when<br>bond is 80+<br>Friendship Bonus (25-35%)<br>Mood Effect (20%)<br>Specialty Priority (50-65)<br>Skill Point Bonus +1<br>Power Bonus +1 (1LB+) | Pace Chaser Straightaways<br>Straightaway Adept<br>Ramp Up<br>Nimble Navigator<br>Head-On<br>Firm Step<br>**No Stopping Me!** | If Whale | Third coming of No Stopping Me! Also probably in its strongest card, statwise Sadly...it's a power card and they still haven't bloomed properly |
| Daitaku Helios (Event) | Early Mar '27 *(est.)* | Sprint | MLB | Specialty Rate (40) when<br>bond is at 80+<br>Friendship Bonus (15%)<br>Mood Effect (50%)<br>Training Eff. (5%)<br>Wit Friendship Recovery (3-5)<br>Wit Bonus +1<br>Speed Bonus +1 | Sprint Corners<br>Mile Corners<br>Slipstream<br>Light as a Feather<br>**Staggering Lead** | Free | Pretty packed wit card Definitely get her while you can |
| Mejiro Palmer | Early Mar '27 *(est.)* | Long | 0LB | Speed Bonus +1 per recovery<br>skill, up to 3 skills (max. +3)<br>Friendship Bonus (25-35%)<br>Mood Effect (20%)<br>Specialty Priority (50-80)<br>Skill Point Bonus +1<br>Race Bonus (5-10%) (3LB+) | Long Corners<br>Long Straightaways<br>Front Runner Straightaways<br>Corner Adept<br>Playtime's Over<br>Groundwork<br>Frantic State<br>Up the Vibes<br>Deep Breaths<br>Moxie<br>**Seriously☆Good↑Vibes** | If Whale+ | Strong speed card for longs, although it suffers the same fate as TM Opera O wit (no longs nearby) and Sakura Laurel stamina (having to buy 3 recoveries, but at least this time it makes sense on a speed card meant for long races) |
| Gold City | Early Mar '27 *(est.)* | Mile | 1LB+ | Guts Bonus +3 when<br>bond is full<br>Friendship Bonus (25-30%)<br>Training Eff. (5%)<br>Mood Effect (20-30%)<br>Power Bonus +1 (1LB+) | Mile Corners<br>Tail Held High<br>Mighty Leap<br>Unyielding Spirit<br>Rushing in Blind<br>High Hopes<br>Shifting Gears<br>**Summer Gale<br>High Voltage** | With Palmer | Strong rainbows in guts training Pretty good card for miles, but not a necessity |
| Twin Turbo (Rerun) | Early Mar '27 *(est.)* | Front | MLB | Friendship Bonus (35-40%)<br>Specialty Priority (50-65)<br>Power Bonus +1<br>Skill Point Bonus +1 (1LB+)<br>Speed Bonus +1~2 (3LB+) | Fast-Paced<br>Early Lead<br>Leader's Pride<br>Frantic State<br>Playtime's Over (ends 1st chain)<br>**1000% Output** | No | Good rainbows Scenario is about to end, though |
| Daiichi Ruby (Rerun) | Early Mar '27 *(est.)* | Late<br>Sprint/Mile | 1LB+ | Power Bonus +2 when<br>bond is 80+<br>Friendship Bonus (25-30%)<br>Training Eff. (5%)<br>Specialty Priority (50-80)<br>Skill Point Bonus +1 (1LB+) | Late Surger Corners<br>Late Surger Straightaways<br>Slick Surge<br>Fearless<br>Gap Closer<br>Sprinting Gear<br>**Lightning Speed** | No | Still not a good time for power cards ! |
| Wonder Acute | Late Mar '27 *(est.)* | Dirt | MLB | Power Bonus +2 when<br>bond is 80+<br>Friendship Bonus (20-25%)<br>Training Eff. (5%)<br>Skill Point Bonus +1<br>Mood Effect (20-40%) (1LB+)<br>Stamina Bonus +1~2 (3LB+) | Tail Held High<br>Unyielding Spirit<br>Top Pick<br>At Full Speed<br>Dust Bath<br>Forward, March!<br>**Leisurely Dust Bath** | No | Same as above |
| Air Groove (Event) | Late Mar '27 *(est.)* | Pace | MLB | Training Eff. (10%) when<br>bond is 80+<br>Friendship Bonus (20%)<br>Mood Effect (30%)<br>Power Bonus +1 | Pace Chaser Corners<br>Attack Stance<br>Head-On<br>Straight Descent<br>Stamina to Spare<br>**Speed Star** | Free | Decent roaming speed card It's also free ! |
| Jungle Pocket | Late Mar '27 *(est.)* | Late | 1LB+ | Friendship Bonus (20%) when<br>bond is full<br>Friendship Bonus (15-20%)<br>Mood Effect (20%)<br>Speed Bonus +1<br>Specialty Priority (50-65)<br>Guts Bonus +1 (1LB+) | Medium Straightaways<br>Late Surger Corners<br>Position Pilfer<br>Slick Surge<br>1,500,000 CC<br>Overflowing Passion<br>On the Move<br>Take the Chance<br>Devil-May-Care<br>**Blitzing Spirit** | No | Possibly big rainbows past 1LB, but nothing great other than that Also very close to 2.5 Anni |
| Manhattan Cafe | Late Mar '27 *(est.)* | Late<br>Long | MLB | Wit Bonus +2 and Skill Point<br>Bonus +1 when bond is full<br>Training Eff. (10-15%)<br>Friendship Bonus (20-25%)<br>Race Bonus (5-10%)<br>Wit Friendship Recovery (3-5)<br>Mood Effect (20-40%) (1LB+) | Long Straightaways<br>Late Surger Corners<br>Great Haste<br>Devil-May-Care<br>Deep Breaths<br>Tail Held High (ends 1st chain)<br>**Lose Yourself<br>Cooldown** | If Whale++ | Manhattan Cafe is finally free from stamina prison, and what a way to get out This is a great card for lates in long races Also pretty strong statwise alone 2.5 Anniversary is two banners away, be careful when planning |
| Maruzensky (Rerun) | Late Mar '27 *(est.)* | All-rounder<br>**(Front+)** | 1LB+ | Training Eff. (5-25%) scaling<br>off facility level<br>Friendship Bonus (20-25%)<br>Speed Bonus +1<br>Power Bonus +1 (1LB+)<br>Mood Effect (15-30%) (3LB+) | Front Runner Corners<br>Front Runner Straightaways<br>Slipstream<br>Playtime's Over<br>Leader's Pride<br>Early Lead<br>Groundwork<br>Focus<br>Triple 777s<br>**Top Runner** | No | Last banner before the 2.5 Anniversary, best to save up! (This is her FOURTH time around you should've already gotten her) |
| Mejiro Ramonu (Rerun) | Early Apr '27 *(est.)* | **Mile<br>Medium** | 3LB+ | Training Eff. (4%) per speed<br>skill, up to 5 skills (max. 20%)<br>Friendship Bonus (25-30%)<br>Wit Friendship Recover (3-5)<br>Specialty Priority (35-50)<br>Skill Point Bonus +1 (1LB+)<br>Wit Bonus +1~2 (3LB+) | Mile Corners<br>Mile Straightaways<br>Medium Corners<br>Medium Straightaways<br>Straightaway Adept<br>Shifting Gears<br>Unyielding Spirit<br>Graceful Step<br>Firm Step<br>Fighting Spirit<br>All I've Got<br>**Ascendance** | No | Bait banner! 2.5 Anniversary Banner is next |

**Notes attached to individual cells:**

- **Mihono Bourbon** (Notable Bonuses): It's been a while ! Same as other uniques that provide +10 of a stat type for every card of that stat type in your deck So in a deck with 3 speed, 2 wit and her, you'd get 30 speed, 20 wit and 10 stamina Pal and team cards give +2 to all stats

#### Project L'Arc

**Release timing (Global):** Early Apr '27

- Scenario gimmick: prepare for international racing with extra training partners (similar to Unity Cup!) that each have a Star Gauge to fill up. When it's full, they'll join an SS Match where you'll have to race against them to level up their Star Gauges, gain stats, an assortment of buffs and Support Points that fill up an Expectation Gauge. When more than 5 people are present in an SS Match, you'll have the chance to pop an SSS Match, getting extra stats. Summer camp is replaced by Overseas Expedition, where you'll raise your overseas aptitudes through special tasks and trainings, as well as races like Prix Foy and Prix Niel, getting special buffs and preparing to participate in the L'Arc races (early October in Classic and Senior year)
- Scenario link: Mei Satake, El Condor Pasa, Manhattan Cafe, Gold Ship, Orfevre, Nakayama Festa, Tap Dance City, Sirius Symboli, Satono Diamond
- Scenario skills: Dreaming of the Peak (Bearer of Hope), See Ya Later!, and specific-event skills that depend on scenario link trainee or support card, and can be random if no scenario links are present, every listed skill: Child of Longchamp (Longchamp Racecourse), Photon Flash (Medium Straightaways), It's On! (Ramp Up), Innate Experience (Inside Scoop), Miraculuous Step (Soft Step), Nothing Ventured (Risky Business), Center Stage (Prudent Positioning), Overwhelming Pressure (Pressure)
- Scenario spark: L'Arc Scenario (PWR/STA), Overseas Turf (PWR), Longchamp (Skill Pts.), Everyday Rhythm (GUTS), Nutrition Management (STA), French Fluency (WIT), Overseas Expedition (SPD), Boldness (STA/GUTS), Mental Strength (PWR/WIT), L'Arc Hopes (SPD, Corner Adept), L'Arc Domination Dreams (Downhill Speedster)

| Support Card | Date | Style/Distance | LB Breakpoints | Notable Bonuses | Notable Hints | Pull? | Notes |
|---|---|---|---|---|---|---|---|
| Admire Vega (Event) | Early Apr '27 *(est.)* | End | MLB | Stamina Bonus +2 when<br>bond is 80+<br>Friendship Bonus (30%)<br>Mood Effect (40%)<br>Specialty Priority (50) | End Closer Corners<br>Medium Corners<br>Early Start<br>Masterful Gambit<br>**Serenity** | Free | Underwhelming free card Gold skill is pretty bad |
| Mei Satake | Early Apr '27 *(est.)* | **All-rounder** | 1LB+<br>R MLB > 0LB | Unique<br>Training Eff. (5%)<br>Mood Effect (20%)<br>Energy Reduction (15-25%)<br>Failure Reduction (15-20%)<br>Skill Point Bonus +1 (1LB+) | Straightaway Adept<br>**Never Give Up** | **100 Free Pulls**<br>1LB+<br>or<br>R MLB *(est.)* | L'Arc's pal card, you'll be using her for a while in here Lots of energy regen in her dates, and the chance to dispel negative effects right after getting them |
| El Condor Pasa | Early Apr '27 *(est.)* | **Pace<br>Medium**<br>(Late+) | MLB | All Stats Bonus +1 and<br>Skill Point Bonus +1 when bond<br>is full<br>Friendship Bonus (15-20%)<br>Mood Effect (30-40%)<br>Specialty Priority (50-65)<br>Speed Bonus +1<br>Skill Point Bonus +1 (1LB+)<br>Training Eff. (5-10%) (3LB+) | Pace Chaser Corners<br>Medium Corners<br>Corner Adept<br>Downhill Speedster<br>Attack Stance<br>Satisfying Pace<br>Up-Tempo<br>With All My Soul<br>Steadfast<br>**Check<br>Professor of Curvature** | **100 Free Pulls**<br>Yes *(est.)* | Kitasan's crown tipped a bit here Her unique is absurd Her bonuses are great, only at MLB because of her Training Effectiveness being locked behind it She's a decent card even at 2LB or below, though |
| Nakayama Festa | Early Apr '27 *(est.)* | All-rounder | MLB | Training Eff. (10%) when<br>bond is 80+<br>Friendship Bonus (20-25%)<br>Mood Effect (40-60%)<br>Specialty Priority (50-80)<br>Wit Friendship Recovery (3-5)<br>Skill Point Bonus +1<br>Wit Bonus +1~2 (3LB+) | Right-Handed<br>Ramp Up<br>Homestretch Haste<br>Fighting Spirit<br>**Right-Handed Demon** | No | Strong rainbows, but that's about it, compared to other wit cards, this is lacking stat bonuses that would push this card's numbers further Also very weak hints |
| Special Week (Rerun) | Late Apr '27 *(est.)* | Medium | MLB | Mood Effect (60%) when<br>friendship training<br>Friendship Bonus (15-20%)<br>Stamina Bonus +1<br>Skill Points Bonus +1<br>Guts Bonus +1 (1LB+)<br>Training Eff. (5-10%) (3LB+) | Left-Handed<br>Homestretch Haste<br>Nimble Navigator<br>Up-Tempo<br>All I've Got<br>Fighting Spirit<br>Feature Act<br>Soft Step<br>Extra Tank<br>**No Stopping Me!** | No | Despite still being one of the few cards to give No Stopping Me! her value is still pretty low |
| Mejiro McQueen (Rerun) | Late Apr '27 *(est.)* | Long<br>(Front+) | 1LB+ | Stamina Bonus +3 when<br>bond is full<br>Friendship Bonus (25-35%)<br>Specialty Priority (50-80)<br>Skill Point Bonus +1 (1LB+)<br>Guts Bonus +1~2 (3LB+) | Long Corners<br>Long Straightaways<br>Feature Act<br>Early Lead<br>True Worth<br>Corner Recovery<br>Straightaway Recovery<br>Extra Tank<br>Stay the Course<br>Faultless<br>**Ahead of the Game** | No | Still pretty much a luxury card for long races, don't feel forced to pull for this and save for upcoming cards |
| Hishi Amazon | Late Apr '27 *(est.)* | **End** | MLB | Skill Point Bonus +2<br>when bond is 80+<br>Friendship Bonus (20-25%)<br>Mood Effect (40-50%)<br>Stamina Bonus +1<br>Training Eff. (5-10%) (3LB+) | End Closer Corners<br>End Closer Straightaways<br>Corner Adept<br>Homestretch Haste<br>Nimble Navigator<br>Masterful Gambit<br>Straightaway Spurt<br>**Moonlight Slash<br>Encroaching Shadow** | If dedicated<br>to Ends | First time Encroaching Shadow is accessible in a card And for those who already have it, they now have access to Moonlight Slash as well, both are very strong gold skills for End Closers Downside: it's a power card Strong parent card For F2P end enjoyers, I'd say wait for Narita Taishin wit |
| Taiki Shuttle | Early May '27 *(est.)* | Mile | MLB | Speed Bonus +1<br>Specialty Priority (55)<br>Training Eff. (15%)<br>Friendship Bonus (20%)<br>Wit Friendship Recovery (4) | Mile Corners<br>Shifting Gears<br>Productive Plan<br>High Hopes<br>Prepared to Pass | With Hishiama | Strong wit SR, big rainbows Good skills for mile races |
| Fine Motion (Event) | Early May '27 *(est.)* | Pace | MLB | Training Eff. (10%) when<br>bond is at 80+<br>Friendship Bonus (20%)<br>Mood Effect (30%)<br>Race Bonus (10%)<br>Spee Bonus +1 | Right-Handed<br>Corner Adept<br>Prudent Positioning<br>Attack Stance<br>Productive Plan<br>Up-Tempo<br>Stamina to Spare<br>**Calm and Collected** | Free | Basic statstick free speed card Good for paces |
| Tanino Gimlet | Early May '27 *(est.)* | Medium<br>(End+) | 1LB+ | Guts Bonus +2 when<br>bond is 80+<br>Friendship Bonus (15-20%)<br>Mood Effect (40-50%)<br>Training Eff. (10-15%)<br>Skill Point Bonus +1 (1LB+) | End Closer Straightaways<br>Medium Straightaways<br>Straightaway Adept<br>Nimble Navigator<br>Striaghtaway Spurt<br>Steadfast<br>Eager<br>**Elated** | No | Strong stamina card for lates and ends in medium races Still best to save up, since we'll be getting Sounds of Earth soon |
| Tap Dance City | Early May '27 *(est.)* | Front | 1LB+ | Training Eff. (5%) per speed<br>skill, up to 3 skills (max. 15%)<br>Friendship Bonus (20-25%)<br>Mood Effect (20-30%)<br>Skill Point Bonus +1 (1LB+) | Front Runner Corners<br>Fast-Paced<br>Early Lead<br>Final Push<br>Leader's Pride<br>Moxie<br>**Unrestrained<br>Escape Artist** | No | Pretty meh card for front runners Lacking severely in numbers |
| Gold Ship | Early May '27 *(est.)* | All-rounder<br>(End+) | MLB | Speed Bonus +2 when<br>bond is 80+<br>Friendship Bonus (25-35%)<br>Training Eff. (5%)<br>Specialty Priority (50-65)<br>Speed Bonus +1 (1LB+)<br>Skill Point Bonus +1~2 (3LB+) | Right-Handed<br>End Closer Corners<br>End Closer Straightaways<br>Uma Stan<br>Ramp Up<br>Homestretch Haste<br>Risky Business<br>Straightaway Spurt<br>**Superstan** | No | Big speed numbers on rainbows and that's about it Best as a parent card with that Superstan hint |
| Nice Nature | Late May '27 *(est.)* | All-rounder<br>(Late+) | MLB | Stamina Bonus +1<br>Specialty Priority (70)<br>Friendship Bonus (30%)<br>Mood Effect (50%)<br>Guts Bonus +1 | Homestretch Haste<br>Ramp Up<br>Slick Surge<br>A Small Breather<br>Be Still | No | Good SR stamina card added to the roster Not necessary to pull or spark it |
| Haru Urara (Event) | Late May '27 *(est.)* | N/A | MLB | Specialty Priority (60)<br>when bond is 80+<br>Friendship Bonus (25%)<br>Mood Effect (40%)<br>Power Bonus +2<br>Race Bonus (10%) | **Iron Will** | Free | Could only see some use as a roamer card with that mood effect + power bonus At least it's free...? |
| Tsurumaru Tsuyoshi | Late May '27 *(est.)* | Medium<br>(Pace+) | MLB | The more energy you have,<br>the higher Training Effectiveness<br>you'll get<br>Friendship Bonus (15-20%)<br>Mood Effect (20-30%)<br>Skill Point Bonus +1 (1LB+)<br>Power Bonus +1~2 (3LB+) | Medium Straightaways<br>Homestretch Haste<br>Attack Stance<br>Tooth and Tail<br>Prepared to Pass<br>Steadfast<br>Full Throttle (ends 1st chain)<br>**Flash Forward** | No | That unique again...shivers Somewhat weak power card |
| King Halo | Late May '27 *(est.)* | Sprint<br>(Late+) | MLB | Speed Bonus +1 per speed<br>skill, up to 3 skills (max. +3)<br>Friendship Bonus (15-20%)<br>Training Eff. (5-10%) (1LB+)<br>Skill Point Bonus +1~2 (3LB+) | Sprint Straightaways<br>Homestretch Haste<br>Outer Swell<br>Fearless<br>Pressure<br>Sprinting Gear<br>Meticuluous Measures<br>Single-Minded Advance<br>**Dginified<br>Unyielding Tenacity** | No | Lots of speed on a guts card Focused for sprints, mostly for lates or end closers Not worth pulling for it |
| Mejiro McQueen | Late May '27 *(est.)* | **Pace** | 1LB+ | Wit Bonus +2 when<br>bond is 80+<br>Friendship Bonus (25-30%)<br>Mood Effect (40-60%)<br>Training Eff. (5%)<br>Specialty Priority (50-80)<br>Wit Friendship Recovery (3-5)<br>Speed Bonus +1<br>Wit Bonus +1<br>Skill Point Bonus +1 (1LB+) | Pace Chaser Straightaways<br>Tail Held High<br>Attack Stance<br>Prepared to Pass<br>Head-On<br>Towards Victory<br>Honing In<br>Early Lead<br>**Send It Flying!** | If dedicated<br>to Paces | Pretty strong card for paces even at 1LB because of her high starting value bonuses Very good rainbows and pretty decent training outside wit with that mood effect% |
| Sounds of Earth | Early Jun '27 *(est.)* | **All-rounder** | 3LB+ | Training Eff. (10%) when<br>there are 4+ types in your deck<br>Friendship Bonus (25-30%)<br>Training Eff. (5%)<br>Race Bonus (5-10%)<br>Specialty Priority (50-65)<br>Skill Point Bonus +1<br>Mood Effect (20-40%) (1LB+) | Homestretch Haste<br>Slipstream<br>Playtime's Over<br>Early Race Adept<br>Mid-Race Adept<br>Nimble Navigator<br>Straightaway Adept<br>Straightaway Recovery<br>Lock On<br>**Beeline Burst<br>Breath of Fresh Air** | If Dolphin | Very strong card overall, you can take it as a stamina card for your deck, or as a roaming card with those training eff. and mood effect %s Very strong hints as well and adaptable whether you need a recovery or a speed skill Downside: initial gauge locked behind 3LB, could be used 2LB or below, but you're in the hands of fate for highrolling |
| Mejiro Ryan (Event) | Early Jun '27 *(est.)* | Late | MLB | Training Eff. (10%) when<br>bond is 80+<br>Friendship Bonus (20%)<br>Mood Effect (40%)<br>Specialty Priority (50)<br>Power Bonus +1<br>Guts Bonus +1 | Late Surger Straightaways<br>Fighting Spirit<br>Pressure<br>Pace Strategy<br>**Hard Worker** | Free | Stat-wise, it's a good card But that gold skill...just, no |
| Mejiro Ramonu | Early Jun '27 *(est.)* | Medium<br>(Pace/Mile+) | MLB | Power Bonus +1 per acceleration<br>skill, up to 3 skills (max. +3)<br>Training Eff. (5-10%)<br>Friendship Bonus (15-20%)<br>Mood Effect (20-30%)<br>Stamina Bonus +1 (1LB+)<br>Skill Point Bonus +1~2 (3LB+) | Right-Handed<br>Medium Corners<br>Medium Straightaways<br>Highlander<br>Playtime's Over<br>Satisfying Pace<br>Up-Tempo<br>All I've Got<br>Firm Step<br>Graceful Step<br>Refined Conduct<br>Take the Chance<br>**Chilling Wind** | No | The amount of hints in this card is insane The stats aren't bad at all either, but it's a power card and they're not ready to bloom yet Very powerful parent card for medium races |
| Mejiro Dober | Early Jun '27 *(est.)* | Mile<br>(Late+) | 0LB | Power Bonus +2 when<br>bond is 80+<br>Friendship Bonus (25-30%)<br>Mood Effect (30-40%)<br>Training Eff. (5%)<br>Specialty Priority (50-65) | Mile Corners<br>Ramp Up<br>Outer Swell<br>Overflowing Passion<br>Updrafters<br>Unyielding Spirit<br>Pumped<br>Mighty Leap<br>**Full of Vigor** | No | Decent at base value since her growths don't really go anywhere important Basically a mile card for lates Not worth pulling for, though |
| Vivlos | Late Jun '27 *(est.)* | Late | MLB | Guts Bonus +2 when<br>bond is 80+<br>Friendship Bonus (15-20%)<br>Mood Effect (30-40%)<br>Training Eff. (5%)<br>Skill Point Bonus +1 (1LB+)<br>Power Bonus +1~2 (3LB+) | Late Surger Straightaways<br>Medium Straightaways<br>Position Pilfer<br>1,500,000 CC<br>Slick Surge<br>On the Move<br>Eager<br>**Fast & Furious<br>Lie in Wait** | No | Very average card for lates |
| Twin Turbo (Event) | Late Jun '27 *(est.)* | Front | MLB | Guts Bonus +2 when<br>bond is 80+<br>Friendship Bonus (20%)<br>Mood Effect (60%)<br>Race Bonus (10%) | Ramp Up<br>Risky Business<br>Frantic State<br>Early Lead<br>Final Push<br>Leader's Pride (ends 2nd chain)<br>Steadfast<br>Keeping the Lead<br>**Top Runner** | Free | Good roaming card Decent skills for fronts |
| Carvers of History (Event) | Late Jun '27 *(est.)* | All-rounder | MLB | Training Eff. (10%) when<br>bond is 80+<br>Friendship Bonus (20%)<br>Speed Bonus +1<br>Skill Point Bonus +1<br>Wit Friendship Recovery (2) | Pace Chaser Straightaways<br>Long Straightaways<br>Homestretch Haste<br>Extra Tank<br>**In Body and Mind** | Free | Our fourth group card and it comes with all the benefits all others have had: Passion Zone that allows rainbow training with the card and negates Night Owl and Slacker, as well as hints from all of the members It's not a bad card but there are way better options for most decks |
| Satono Diamond | Late Jun '27 *(est.)* | Late<br>(Medium+) | MLB | Friendship Bonus (10%) and<br>Skill Point Bonus +1 when<br>bond is 80+<br>Training Eff. (5-10%)<br>Friendship Bonus (15-20%)<br>Wit Friendship Recovery (3-5)<br>Mood Effect (20-40%) (1LB+)<br>Wit Bonus +1~2 (3LB+) | Late Surger Corners<br>Corner Acceleration<br>Prudent Positioning<br>Full Throttle<br>Overflowing Passion<br>On the Move<br>Slick Surge<br>Fighting Spirit<br>Rising Passion<br>**Keep Going!<br>Burning Soul** | **100 Free Pulls**<br>With Duramente *(est.)* | Arguably more universal than Manhattan Cafe for lates, with both skills being really strong depending on the situation Stat gains are pretty similar between the two with Satono giving better wit clicks and Cafe better clicks elsewhere |
| Duramente | Early Jul '27 *(est.)* | **All-rounder** | 3LB+ | Friendship Bonus (10%) and<br>Mood Effect (15%) when<br>bond is 80+<br>Training Eff. (10-15%)<br>Friendship Bonus (20-25%)<br>Mood Effect (20%)<br>Power Bonus +1 (1LB+)<br>Specialty Priority (60-120) (3LB+) | End Closer Straightaways<br>Medium Straightaways<br>Slipstream<br>Rapid<br>Unbreakable Mind<br>Rising Passion<br>Ignition<br>**Never Give Up** | **100 Free Pulls**<br>If Whale *(est.)* | As we've been seeing through past scenarios, a pretty strong card releasing just a few banners before the next anniversary drops Plan and pull according to your needs! This is a more general speed card which acts like a sidegrade to El Condor Pasa |
| Hokko Tarumae | Early Jul '27 *(est.)* | Dirt | 1LB+ | Training Eff. (15%) when<br>rainbow training<br>Friendship Bonus (15-20%)<br>Mood Effect (40-50%)<br>Training Eff. (5%)<br>Skill Point Bonus +1 (1LB+) | Promising Omen<br>At Full Speed<br>Backup Planning<br>Full of Zeal<br>Forward, March!<br>Top Pick<br>Head-On (ends 1st chain)<br>**Call & Response** | No | Somewhat underwhelming card Very weak, but the skills are worth for dirt races Who runs stamina cards for dirt anyways? |
| North Flight (Event) | Late Jul '27 *(est.)* | Mile | MLB | Speed Bonus +2 when<br>bond is 80+<br>Friendship Bonus (25%)<br>Mood Effect (30%)<br>Wit Bonus +1<br>Wit Friendship Recovery (5) | Mile Corners<br>Prepared to Pass<br>Updrafters<br>Productive Plan<br>High Hopes<br>**Changing Gears** | Free | Decent card for miles It's the only card with the Changing Gears skill for now It's free ! |
| Sakura Bakushin O | Late Jul '27 *(est.)* | Sprint | 1LB+ | Speed Bonus +2 when<br>bond is 80+<br>Training Eff. (5-10%)<br>Friendship Bonus (20-25%)<br>Mood Effect (30-40%)<br>Specialty Priority (50-65)<br>Speed Bonus +1<br>Power Bonus +1 (1LB+) | Sprint Corners<br>Early Race Adept<br>Groundwork<br>Light as a Feather<br>Sprinting Gear<br>Gap Closer<br>Single-Minded Advance<br>Countermeasure<br>Swift Takeoff<br>**Rocket Start<br>Lightning Slash** | No | Last banner of the scenario Good card for sprints, but don't feel the necessity to pull for it |
| Winning Ticket | Late Jul '27 *(est.)* | Late | 1LB+ | Friendship Bonus (20%) when<br>bond is full<br>Friendship Bonus (15-20%)<br>Training Eff. (5%)<br>Specialty Priority (50-80)<br>Stamina Bonus +1<br>Power Bonus +1<br>Skill Point Bonus +1 (1LB+) | Left-Handed<br>Late Surger Corners<br>Nimble Navigator<br>Position Pilfer<br>Slick Surge<br>Overflowing Passion<br>On the Move<br>Razor-sharp Stride<br>**Top Gear** | No | Last banner of L'Arc scenario |

**Notes attached to individual cells:**

- **Mei Satake** (Notable Bonuses): Mei's unique gives her the chance to appear in two different facilities in the same turn after reaching 60+ bond (when it turns green)

#### U.A.F. Ready Go!

**Release timing (Global):** Early Aug '27

- Scenario gimmick: training facilities are replaced by 15 new disciplines (one for each facility, divided by three colors: Sphere (blue), Fight (red) and Free (yellow)), and each discipline has a level that goes from 1 to 100. Each turn, your facilities will shuffle between the 15 disciplines, and whenever two or more disciplines appear, you'll be able to do link training, which allows to train in all of the disciplines at the same time, giving the corresponding stats (with a slight boost), plus levels for all of the disciplines. Every 50 levels, you'll get a Heat-Up effect for two turns, blue heat-up gives more stats and skill points on all disciplines, red raises the main stats of all disciplines in a link training and yellow increases hint appearance and allows getting up to two hints per turn. You can use a special feature, Consultation (phone icon) to reshuffle the disciplines in your current turn, although it's got limited uses. Lastly, the scenario features a tournament where you'll put your disciplines to test. Every 6 months you'll be put to a test where you'll fight for each discipline, and wins are determined by your disciplines' levels. You'll have a torunament gauge to keep track of your progress, and every win contributes towards extra training effectiveness% You'll need 12 discipline wins to achieve a victory in the Showdown (final) stage.
- Scenario link: Tosen Jordan, Narita Top Road, Mejiro Ryan, Winning Ticket, Yaeno Muteki, Ryoka Tsurugi
- Scenario skills: Now I'm Fired Up!! (It's On!), Doing My Best! (In Body and Mind), Sparkling Contest (Battle for Initiative), Stay Tuned (Killer Tunes), Connecting Elation (Elated), Unstoppable Muscles (Full of Vigor), Reckless Passion (Reckless), Blazing Radiance (Burning Soul), Athlete's Spirit
- Scenario spark: U.A.F: Sphere (SPD/SP), U.A.F: Fight (PWR/SP), U.A.F: Free (GUTS/SP)

| Support Card | Date | Style/Distance | LB Breakpoints | Notable Bonuses | Notable Hints | Pull? | Notes |
|---|---|---|---|---|---|---|---|
| Gentildonna (Event) | Early Aug '27 *(est.)* | Mile<br>Medium | MLB | Speed Bonus +2 when<br>bond is 80+<br>Friendship Bonus (30%)<br>Training Eff. (10%)<br>Specialty Priority (35) | Mile Straightaways<br>Medium Straightaways<br>Straightaway Adept<br>Homestretch Haste<br>Uma Stan<br>Downhill Speedster<br>Graceful Step<br>**It's On!** | Free | Useable if you have nothing else to pick from Which should be very rare at this point |
| Ryoka Tsurugi | Early Aug '27 *(est.)* | **All-rounder** | 0LB+ | Unique<br>Mood Effect (40-50%)<br>Race Bonus (5-10%)<br>Failure Protection (20-30%)<br>Energy Reduction (5-10%)<br>Training Eff. (5-10%) (3LB+) | Homestretch Haste<br>**Battle for Initiative** | **100 Free Pulls**<br>Yes *(est.)* | UAF's pal card, she's a must in most decks |
| Orfevre | Early Aug '27 *(est.)* | **All-rounder** | 1LB+ | Unique<br>Friendship Bonus (25-30%)<br>Race Bonus (5-10%)<br>Specialty Priority (50-80)<br>Guts Bonus +1 (1LB+)<br>Training Eff. (5-10%) (3LB+) | Corner Adept<br>Playtime's Over<br>Tail Held High<br>Rapid<br>Nimble Navigator<br>Rising Passion<br>Mighty Step<br>Mold Breaker<br>**Divine Speed** | **100 Free Pulls**<br>Yes *(est.)* | First guts card you should actively pull for. Highlander teams (one card of each type) start becoming more and more prominent now Great generalist gold skill Comes with free pulls, try to get as many copies as possible |
| Rhein Kraft (Story) | Late Aug '27 *(est.)* | Pace<br>Mile | MLB | Training Eff. (10%) when<br>bond is at 80+<br>Friendship Bonus (25%)<br>Mood Effect (20%)<br>Specialty Priority (50)<br>Guts Bonus +1<br>Power Bonus +1 | Mile Corners<br>Mile Straightaways<br>Prepared to Pass<br>Productive Plan<br>Unyielding Spirit<br>**Unstoppable** | Free | Very average card for paces |
| Cheval Grand | Late Aug '27 *(est.)* | Long | 3LB+ | Stamina Bonus +2 when<br>bond is 80+<br>Friendship Bonus (25-35%)<br>Mood Effect (20-30%)<br>Specialty Priority (50-65)<br>Stamina Bonus +1 (1LB+)<br>Skill Bonus +1~2 (3LB+) | Long Corners<br>Long Straightaways<br>Pace Chaser Straightaways<br>Prepared to Pass<br>Attack Stance<br>Toward Victory<br>True Worth<br>Inside Scoop<br>Feature Act<br>Stamina to Spare<br>**Headliner** | **9 Free Pulls**<br>If Whale *(est.)* | Strong card for long races Very big stamina numbers |
| Bamboo Memory (Event) | Early Sep '27 *(est.)* | End<br>(Sprint/Mile+) | MLB | Power Bonus +2 when<br>bond is 80+<br>Friendship Bonus (20%)<br>Mood Effect (20%)<br>Training Eff. (5%)<br>Specialty Priority (50)<br>Stamina Bonus +1 | Masterful Gambit<br>Breakthrough Plan<br>Gap Closer<br>Meticuluous Measures<br>Updrafters<br>Unyielding Spirit<br>**Moonlit Flash** | Free | Decent card for end closers in shorter races It's free |
| K.S.Miracle | Early Sep '27 *(est.)* | Sprint | 1LB+ | Power Bonus +1 and Skill Point<br>Bonus +1 when bond is 80+<br>Training Eff. (10-15%)<br>Friendship Bonus (20-25%)<br>Mood Effect (20-30%)<br>Specialty Priority (50-65)<br>Power Bonus +1 (1LB+)<br>Race Bonus (5-10%) (3LB+) | Sprint Straightaways<br>Early Race Adept<br>Downhill Speedster<br>Straightaway Adept (ends 1st chain)<br>Countermeasure<br>Sprinting Gear<br>Swift Takeoff<br>Light as a Feather<br>**Turbo Sprint** | No | Useable sprint card but you're probably better off taking her guts variant 90% of the time, especially if building paces |
| Yamanin Zephyr | Early Sep '27 *(est.)* | Mile<br>(Pace+) | 3LB+ | Skill Point Bonus +2 when<br>bond is 80+<br>Friendship Bonus (25-30%)<br>Mood Effect (40-50%)<br>Training Eff. (5%)<br>Specialty Priority (50-80)<br>Speed Bonus +1~2 (3LB+) | Pace Chaser Straightaways<br>Slipstream<br>Prepared to Pass<br>Head-On<br>Ambitions<br>Productive Plan<br>Rushing in Blind<br>Graceful Step<br>**Reckless** | No | Good card for paces in miles, but that's about it If you can, it's best to borrow rather than to pull for it |
| Neo Universe | Late Sep '27 *(est.)* | Medium<br>(Late+) | 3LB+ | Wit Bonus +2 when<br>bond is 80+<br>Friendship Bonus (20-25%)<br>Mood Effect (40-50%)<br>Wit Friendship Recovery (3-5)<br>Training Eff. (5-10%) (1LB+)<br>Skill Point Bonus +1~2 (3LB+) | Medium Corners<br>Uma Stan<br>On the Move<br>All I've Got<br>Eager<br>Mold Breaker<br>Ignition<br>Take the Chance<br>**From the Brink** | If Whale | Great card for lates (or ends, sometimes even paces) in medium races Only go for it if you can guarantee 3LB+ or if you desperately need a card for mediums |
| No Reason (Event) | Early Oct '27 *(est.)* | Late | MLB | Guts Bonus +2 when<br>bond is 80+<br>Friendship Bonus (25%)<br>Mood Effect (50%)<br>Specialty Priority (50) | Straightaway Acceleration<br>Tooth and Tail<br>Fighting Spirit<br>All I've Got<br>A Small Breather<br>**Dauntless** | Free | Somewhat 'meh' card, but it's free so just take it |
| Narita Taishin | Early Oct '27 *(est.)* | **End** | 1LB+ | Wit Bonus +2 when<br>bond is 80+<br>Training Eff. (10-15%)<br>Friendship Bonus (25-35%)<br>Mood Effect (20%)<br>Specialty Priority (50-65)<br>Wit Friendship Recovery (3-5)<br>Skill Point Bonus +1 (1LB+)<br>Race Bonus (5-10%) (3LB+) | End Closer Straightaways<br>Breakthrough Plan<br>Boiling Blood<br>Sufficient Thrust<br>No Reluctance<br>Shadowstepper<br>Straightaway Spurt<br>Seize the Chance<br>**Encroaching Shadow<br>Soaring Stride** | **80 Free Pulls**<br>If dedicated<br>to Ends *(est.)* | Very strong card for ends, almost mandatory, even at 1LB Both gold skills are great for end closers |
| Hishi Miracle | Early Oct'27 *(est.)* | Late<br>Long | 3LB+ | Friendship Bonus (20%) when<br>bond is 80+<br>Friendship Bonus (15-20%)<br>Skill Point Bonus +1<br>Specialty Priority (50-65)<br>Mood Effect (20-40%) (1LB+)<br>Stamina Bonus +1~2 (3LB+) | Slick Surge<br>On the Move<br>Great Haste<br>Lock On<br>A Small Breather<br>Deep Breaths<br>**One-shot** | **80 Free Pulls**<br>With Taishin *(est.)* | Sadly not a good banner partner for Narita Taishin, very underhwelming card for lates in longs, when we already have Kris S and Manhattan Cafe |
| Vodka | Late Oct '27 *(est.)* | Late<br>Mile<br>(Sprint+) | 3LB+ | Speed Bonus +1 and Power<br>Bonus +1 when bond is 80+<br>Friendship Bonus (25-30%)<br>Power Bonus +1<br>Mood Effect (20-40%) (1LB+)<br>Guts Bonus +1~2 (3LB+) | Left-Handed<br>Corner Adept<br>Nimble Navigator<br>Outer Swell<br>Full Throttle<br>Unyielding Spirit<br>Mighty Leap<br>**Lightning Speed** | No | Average mile card for lates, I wouldn't necessarily pull for it Also very close to the end of the scenario |
| Verxina (Event) | Early Nov '27 *(est.)* | Mile | MLB | Speed Bonus +2 when<br>bond is 80+<br>Training Eff. (10%)<br>Friendship Bonus (20%)<br>Specialty Priority (50) | Ramp Up<br>Corner Acceleration<br>Focus<br>Go with the Flow<br>Shifting Gears<br>Productive Plan<br>Graceful Step<br>**Cyclone Flash** | Free | Statstick speed card for miles |
| Vivlos | Early Nov '27 *(est.)* | All-rounder | 3LB+ | Speed Bonus +1 and Skill Point<br>Bonus +1 when bond is 80+<br>Friendship Bonus (25-30%)<br>Speed Bonus +1<br>Race Bonus (5-10%)<br>Specialty Priority (60-100)<br>Power Bonus +1 (1LB+)<br>Training Eff. (10-20%) (3LB+) | Mile Straightaways<br>Late Surger Straightaways<br>Early Race Adept<br>Straightaway Adept<br>Uma Stan<br>Nimble Navigator<br>Tail Held High<br>On the Move<br>**Tail Nine** | If Whale++ | Great generalist speed card Very strong stats all around, and good hints as well Downside: this is the last banner before next scenario, so plan your pulls accordingly |
| Seiun Sky | Early Nov '27 *(est.)* | Front<br>Medium | 1LB+ | Power Bonus +2 when<br>bond is 80+<br>Friendship Bonus (25-30%)<br>Mood Effect (20-30%)<br>Training Eff. (5%)<br>Race Bonus (5-10%)<br>Specialty Priority (50-65)<br>Power Bonus +1<br>Skill Point Bonus +1 (1LB+)<br>Stamina Bonus +1~2 (3LB+) | Right-Handed<br>Front Runner Straightaways<br>Medium Corners<br>Dodging Danger<br>Leader's Pride<br>Steadfast<br>With All My Soul<br>Early Bird<br>Keeping the Lead<br>**Further than Anyone** | With Vivlos | Could give good numbers at MLB with all the bonuses Power card curse is about to end, but this card is nothing notoriously great Gold skill is gold Groundwork for mediums |

**Notes attached to individual cells:**

- **Ryoka Tsurugi** (Notable Bonuses): Ryoka's unique makes your cards appear more often in training facilities when she reaches 60+ gauge
- **Orfevre** (Notable Bonuses): Orfevre's unique is VERY strong, it gives +1 stat bonus per card type in your deck, pal and group cards give skill point bonus, when her bond is at 80+ For example, on a highlander deck + Ryoka, this card will be getting +1 bonus to every stat and +1 skill point bonus

#### Great Food Festival!

**Release timing (Global):** Late Nov '27

- Scenario gimmick: Umamusume turned Cooking Mama...? This scenario focuses on harvesting, cooking and serving up dishes. You gather vegetables (carrots, garlics, potatoes, chili pepper and strawberries) from different actions, as well as field points to increase vegetable yields. Once you gather enough vegetables, you'll be able to cook different dishes that provide different bonuses to your trainings for one turn, cooking more dishes increases a cooking gauge that, once filled, gives a great success on your next dish. Cooking also grants cooking points that increases the buffs and gives higher chances for a random great success to appear. Every 6 months you'll undergo a Tasting Party, where you'll need to get to a certain amount of points by cooking dishes, by the last Tasting Party, you should have achieved 12000 points.
- Scenario link: Special Week (Gourmand (Hydrate)), Hishi Akebono (Lightning Blitz (Explosive Force)), Rice Shower (Determined Descent (Straight Descent)), Nishino Flower (Beeline Burst (Straightaway Adept)), Katsuragi Ace (Sixth Sense (Dodging Danger)), Yayoi Akikawa (Wind Rider (Wind Vane))
- Scenario skills: Curve Grand Chef (Corner Connoisseur), Cultivation Sprint! (Turbo Sprint), Three-Star Cornering (Lightning Slash), Respect! Uma Mania! (Superstan), Here You Go! (Lightning Speed), Mid-Meal Seasoning! (Exquisite Timing), The Races We Run (Forever Healthy), Essence of Food
- Scenario spark: GFF: Carrot (SPD/SP), GFF: Garlic (STA/SP), GFF: Potato (PWR/SP), GFF: Chili Pepper (GUTS/SP), GFF: Strawberry (WIT/SP)

| Support Card | Date | Style/Distance | LB Breakpoints | Notable Bonuses | Notable Hints | Pull? | Notes |
|---|---|---|---|---|---|---|---|
| Yayoi Akikawa | Late Nov '27 *(est.)* | **All-rounder** | 1LB+ | Unique<br>Mood Effect (20%)<br>Speed Bonus +1<br>Energy Reduction (10-15%)<br>Failure Protection (15-20%)<br>Skill Point Bonus +1 (1LB+)<br>Training Eff. (5-10%) (3LB+) | Straightaway Adept<br>Mid Race Adept<br>**Superstan** | **80 Free Pulls**<br>Yes *(est.)* | Great Food Festival's pal card, you either pull for it, or borrow it |
| Nishino Flower | Late Nov '27 *(est.)* | **Sprint<br>Mile** | 1LB+ | Unique<br>Friendship Bonus (25-35%)<br>Specialty Priority (50-65)<br>Race Bonus (5-10%)<br>Power Bonus +1 (1LB+)<br>Training Eff. (5-10%) (3LB+) | Early Race Adept<br>Straightaway Adept<br>An Honest Step<br>Slipstream<br>Groundwork<br>Pounding Chest<br>**Fluttering Heart<br>Frontal Attack** | **80 Free Pulls**<br>With Yayoi *(est.)* | This is the resurgence of power cards, and this is a strong one that lasts for a while This card also has insane value for the scenario, which focuses on sprints and miles, and where all CMs will be 1800m or shorter |
| Dantsu Flame | Early Dec '27 *(est.)* | Medium<br>(Pace+) | 3LB+ | Stamina Bonus +1 and<br>Guts Bonus +2 when<br>bond is full<br>Friendship Bonus (20-25%)<br>Mood Effect (20-30%)<br>Race Bonus (5-10%)<br>Training Eff. (5-10%) (1LB+)<br>Skill Point Bonus +1~2 (3LB+) | Medium Corners<br>Medium Straightaways<br>Pace Chaser Straightaways<br>Playtime's Over<br>Nimble Navigator<br>Tooth and Tail<br>All I've Got<br>Unshakeable Faith<br>Stamina to Spare<br>Preferred Position<br>**Unwavering Ambition** | No | A Medium stamina card, if you ever need one Not necessarily great timing-wise, but it's a good statstick if that's what you're looking for |
| Wonder Acute (Event) | Late Dec '27 *(est.)* | Dirt | MLB | Training Eff. (10%) when<br>bond is 80+<br>Friendship Bonus (20%)<br>Mood Effect (20%)<br>Guts Bonus +1<br>Stamina Bonus +1<br>Specialty Priority (35) | Attack Stance<br>Forward, March!<br>Pace Strategy<br>Dust Off<br>**Full Speed Ahead!** | Free | Below average stamina card for dirt races |
| Smart Falcon | Late Dec '27 *(est.)* | **Front** | 1LB+ | Speed Bonus +1 per speed<br>skill, up to 3 skills (max. +3)<br>Training Eff. (5-10%)<br>Friendship Bonus (20-25%)<br>Mood Effect (20-30%)<br>Power Bonus +1<br>Specialty Priority (50-80)<br>Race Bonus (5-10%)<br>Skill Point Bonus +1 (1LB+) | Front Runner Corners<br>Front Runner Straightaways<br>Groundwork<br>Prudent Positioning<br>Leader's Pride<br>Fast-Paced<br>Early Lead<br>Final Push<br>Steadfast<br>**Taking the Lead** | If dedicated<br>to Fronts | Maruzensky speed's second coming Great (and budget-friendly) speed card for front runners Gets hint frequency and levels at 3LB+, so good for getting those hints online as well, but definitely works at 1LB and above |
| Copano Rickey | Late Dec '27 *(est.)* | Dirt | 1LB+ | Wit Bonus +1 and Skill Point<br>Bonus +1 when bond is 80+<br>Training Eff. (5-10%)<br>Friendship Bonus (25-30%)<br>Mood Effect (40-50%)<br>Skill Point Bonus +1<br>Specialty Priority (50-65)<br>Wit Friendship Recovery (3-5)<br>Wit Bonus +1 (1LB+) | Left-Handed<br>Dirt Corners<br>Dirt Straightaways<br>Groundwork<br>Dust Bath<br>Promising Omen<br>Pioneer<br>Dust Off<br>**Pioneer of the Sands<br>Sand Virtuoso** | With Falco | About average card for training dirt umas, but I wouldn't go the extra mile to grab it If you get it while pulling for Smart Falcon, that's fine! |
| Fine Motion | Early Jan '28 *(est.)* | Medium | 1LB+ | Skill Point Bonus +2 when<br>bond is 80+<br>Training Eff. (5-10%)<br>Friendship Bonus (25-30%)<br>Mood Effect (40-50%)<br>Race Bonus (5-10%)<br>Specialty Priority (50-65)<br>Power Bonus +1 (1LB+) | Medium Corners<br>Corner Adept<br>Leap Premonition<br>Graceful Step<br>Unshakeable Faith<br>Frontal Breakthrough<br>**Just Rule** | No | Another card for mediums, it's just very iffy timing-wise Also the banner before 3.5 Anni |
| Buena Vista (Event) | Early Jan '28 *(est.)* | Mile | MLB | Guts Bonus +2 when<br>bond is 80+<br>Friendship Bonus (30%)<br>Mood Effect (40%)<br>Specialty Priority (50)<br>Speed Bonus +1 | Straightaway Acceleration<br>Corner Acceleration<br>Ramp Up<br>Unyielding Spirit<br>Updrafters<br>Pumped<br>Overflowing Passion<br>**Corner Connoisseur** | Free | Not better than other free guts cards, but it's free so take it ! |
| Still In Love | Early Jan '28 *(est.)* | **All-rounder** | 1LB+ | Speed Bonus +1 and Skill Point<br>Bonus +1 when bond is 80+<br>Training Eff. (10-15%)<br>Friendship Bonus (20-25%)<br>Mood Effect (30-40%)<br>Specialty Priority (60-100)<br>Initial Skill Points +30~60<br>Speed Bonus +1<br>Power Bonus +1<br>Skill Point Bonus +1 (1LB+) | Medium Corners<br>Corner Adept<br>Straightaway Adept<br>Tail Held High<br>Playtime's Over<br>Nimble Navigator<br>Bare Passion<br>Boiling Emotions<br>Refined Conduct<br>Self-Restraint<br>**Pure Instincts<br>Sharp-Witted Composure** | **100 Free Pulls**<br>Yes *(est.)* | Next in line to get generalist speed cards' crown Very strong stat-wise, and also pretty good hints for medium or lates/ends Shines at 3LB or higher because she gets initial friendship gauge, but more than useable at 1LB+ |
| Symboli Kris S (Event) | Late Jan '28 *(est.)* | Long | MLB | Training Eff. (10%) when<br>bond is 80+<br>Friendship Bonus (20%)<br>Specialty Priority (50)<br>Wit Friendship Recovery (5)<br>Skill Point Bonus +1<br>Wit Bonus +2 | Long Corners<br>Mid Race Adept<br>Ramp Up<br>Pace Strategy<br>Deep Breaths<br>Extra Tank<br>**Innate Experience** | Free | Decent free card, but lacks severely in the hints department |
| Fuji Kiseki | Late Jan '28 *(est.)* | Pace | 1LB+ | Speed Bonus +1 and Guts<br>Bonus +1 when bond is 80+<br>Friendship Bonus (25-35%)<br>Mood Effect (20-30%)<br>Training Eff. (5%)<br>Specialty Priority (50-65)<br>Speed Bonus +1<br>Power Bonus +1<br>Skill Point Bonus +1 (1LB+) | Pace Chaser Corners<br>Playtime's Over<br>Attack Stance<br>Head-On<br>Leap Premonition<br>Prepared to Pass<br>Tooth and Tail<br>Pounding Chest<br>**Gamma Ray Burst** | With Taiki | Decent guts card for paces, a lot more generalist than K. S. Miracle |
| Taiki Shuttle | Late Jan '28 *(est.)* | **Mile** | 3LB+ | Speed Bonus +2 when<br>bond is 80+<br>Training Eff. (5-10%)<br>Friendship Bonus (25-30%)<br>Mood Effect (20%)<br>Specialty Priority (50-65)<br>Skill Point Bonus +1 (1LB+)<br>Wit Bonus +1~2 (3LB+) | Mile Corners<br>Groundwork<br>Prepared to Pass<br>Productive Plan<br>Unyielding Spirit<br>Rushing in Blind<br>Wind Vane<br>Fearless Advance<br>High Hopes<br>**Peerless Boldness** | If whale | Another Taiki card fit for the Greatest Miler herself Very strong wit card for miles, specifically fronts and paces Unlike other cards in this scenario that work at 1LB, sadly she works best at MLB (useable at 3LB for sure) |
| Espoir City | Early Feb '28 *(est.)* | **Dirt** | 3LB+ | Stamina Bonus +1 and Skill Point<br>Bonus +1 when bond is 80+<br>Friendship Bonus (25-35%)<br>Mood Effect (40-50%)<br>Specialty Priority (50-80)<br>Stamina Bonus +1 (1LB+)<br>Training Eff. (5-10%) (3LB+) | Dirt Corners<br>Playtime's Over!<br>Unyielding Spirit<br>Dust Bath<br>Pioneer<br>Contradicting Emotions<br>Promising Omen<br>Dust Off<br>**Embracing Virtue and Vice<br>Outstanding Step** | If whale+ | Strong power card for dirts, although a big chunk of her power resides in her 3LB+ training effectiveness, so expect to dump a bunch of carats if you want to use her |
| Cesario (Story) | Early Feb '28 *(est.)* | Medium | MLB | Training Eff. (10%) when<br>bond is 80+<br>Friendship Bonus (20%)<br>Mood Effect (30%)<br>Wit Friendship Recovery (5)<br>Specialty Priority (35)<br>Wit Bonus +2 | Ramp Up<br>Homestretch Haste<br>Tooth and Tail<br>Satisfying Pace<br>All I've Got<br>Fighting Spirit<br>**Refraction Arc** | Free | Average for a free card, nothing out of the ordinary Gold skill is good, but could use a bunch more hints in this time and age |
| Matikanefukukitaru (Event) | Late Feb '28 *(est.)* | Late | MLB | Training Eff. (10%) when<br>bond is 80+<br>Friendship Bonus (30%)<br>Specialty Priority (50)<br>Speed Bonus +1<br>Guts Bonus +1 | 1,500,000 CC<br>Pressure<br>From the First Step<br>Triple 7s<br>A Small Breather<br>**Incisive Slash** | Free | Pretty underwhelming free card, low on numbers, low on hints |
| Narita Brian | Late Feb '28 *(est.)* | Pace<br>(Long+) | 3LB+ | Speed Bonus +1 and Skill Point<br>Bonus +1 when bond is 80+<br>Training Eff. (10-15%)<br>Friendship Bonus (25-30%)<br>Mood Effect (20-30%)<br>Race Bonus (5-10%)<br>Specialty Priority (50-80)<br>Power Bonus +1~2 (3LB+) | Pace Chaser Corners<br>Pace Chaser Straightaways<br>Head-On<br>Aggressive<br>Restless Step<br>Tooth and Tail<br>True Worth<br>**Monster<br>Breaking Free** | No | Strong gold skills for paces, especially in long races with Monster Gives good speed trainings with a hefty power bonus at MLB Still not worth pulling, this is the last banner of the scenario |
| Hishi Amazon | Late Feb '28 *(est.)* | End | 1LB+ | Training Eff. (4%) per speed<br>skill, up to 5 skills (max. 20%)<br>Friendship Bonus (25-30%)<br>Mood Effect (20-30%)<br>Race Bonus (5-10%)<br>Specialty Priority (50-65)<br>Guts Bonus +1<br>Skill Points Bonus +1 | End Closer Corners<br>Uma Stan<br>Slipstream<br>Masterful Gambit<br>Straightaway Spurt<br>Boiling Blood<br>Early Start<br>Cleave<br>**Daring Strike** | No | Same as before but for ends, potentially a good card (albeit not too strong), but it's the last banner, so pulling is not recommended |

**Notes attached to individual cells:**

- **Yayoi Akikawa** (Notable Bonuses): Yayoi's unique gives every card in your deck +1 friendship gauge whenever you train with them, and +2 if the cards are training in the same facility as her It's practically the same value as Charming!
- **Nishino Flower** (Notable Bonuses): Nishino Flower's unique grants higher training effectiveness the higher your cards' total bond is This pairs excepcionally well with cards that grant bond bonuses like...Yayoi's pal card

#### Run, Mecha Umamusume!

**Release timing (Global):** Early Mar '28

- Scenario gimmick: your goal in this scenario is to train with the robot ST-2. You'll have a research level menu where you'll see your research progress on five categories that resemble the training facilities, and each training will boost the corresponding research type. Additionally, you'll also be able to get Overdrive gauge by clicking on facilities that show the Overdrive gear on it. This Overdrive gives a one-turn buff to your trainings, depending on your choices of upgrades for ST-2. Every 6 months, you'll get Upgrade Events where you can slot different bonuses on your ST-2 robot, split between cores: head, chest and legs, and each core divided into another three chips
- Scenario link: Biwa Hayahide (Mech initial energy, more gears, Peak Ferocity (Fervor)), Air Shakur (Mech initial energy, more bonuses, Professor of Curvature (Corner Adept)), Narita Taishin (initial Overdrive, more gears, Moonlit Flash (End Closer Straightaways)), Tanino Gimlet (initial Research level, more gears, Flash (Towards the Light)), Symboli Kris S (initial Overdive, initial Research level, Fast & Furious (Position Pilfer))
- Scenario skills: Archline Top Scholar (Professor of Curvature), Limiter Release (In Body and Mind), Lead-Preserving Algorithm (Top Runner), Monster Machine (Monster), All Systems Green (Sharp-Witted Composure), Recovery Sequence (Chain Reaction), Killer Tunes, For a Fleeting View
- Scenario spark: Mecha Umamusume: SPD (SPD/SP), Mecha Umamusume: PWR (PWR/SP), Mecha Umamusume: STA (STA/SP), Mecha Umamusume: GUTS (GUTS/SP), Mecha Umamusume: WIT (WIT/SP)

| Support Card | Date | Style/Distance | LB Breakpoints | Notable Bonuses | Notable Hints | Pull? | Notes |
|---|---|---|---|---|---|---|---|
| Air Shakur | Early Mar '28 *(est.)* | **All-rounder**<br>(Late/Long+) | 1LB+ | Stamina Bonus +2 when<br>bond is 80+<br>Training Eff. (10-15%)<br>Friendship Bonus (25-35%)<br>Mood Effect (20-30%)<br>Race Bonus (5-10%)<br>Initial Skill Points +30~40<br>Skill Points Bonus +1 (1LB+)<br>Specialty Priority (40-80) (3LB+) | Long Corners<br>Corner Adept<br>Homestretch Haste<br>Mold Breaker<br>Surprise Attack<br>Pace Strategy<br>Fuse<br>**Chain Reaction<br>Like a Blaze** | **80 Free Pulls**<br>Yes *(est.)* | Super Creek's formal powercreep Very strong card with very strong gold skills as well Works fine at 1LB+ but really cranks up at 3LB+ with her specialty priority One of JP's current top-tier stamina card for most situations Also a scenario link for the current scenario |
| Daiwa Scarlet | Early Mar '28 *(est.)* | **Front**<br>(Long+) | 3LB+ | Wit Bonus +1 per speed<br>skill, up to 3 skills (max. +3)<br>Friendship Bonus (28-40%)<br>Mood Effect (20%)<br>Specialty Priority (50-80)<br>Wit Friendship Recovery (3-5)<br>Skill Point Bonus +1 (1LB+)<br>Training Eff. (5-10%) (3LB+) | Front Runner Corners<br>Front Runner Straightaways<br>Playtime's Over!<br>Straightaway Adept<br>Early Race Adept<br>Leader's Pride<br>Spearhead<br>Doding Danger<br>Fast-Paced<br>Finale<br>Firm Resolve<br>No Hesitation<br>Feature Act<br>**Top Runner<br>One Sky, One Goal** | **80 Free Pulls**<br>With Air Shakur<br>or<br>If dedicated<br>to Fronts *(est.)* | Dedicated wit card for fronts, especially for those who run longs Very strong wit trainings, very good hints, very good gold skills If you get a copy during the free pulls and like front runners, I wouldn't mind going all the way to MLB it |
| Symboli Kris S | Late Mar '28 *(est.)* | **Late** | 3LB+ | Power Bonus +2 when<br>bond is 80+<br>Friendship Bonus (25-35%)<br>Specialty Priority (50-80)<br>Stamina Bonus +1<br>Race Bonus (5-10%)<br>Skill Point Bonus +1 (1LB+)<br>Training Eff. (10-20%) (3LB+) | Late Surger Corners<br>Slipstream<br>Position Pilfer<br>Razor-Sharp Stride<br>Pressure<br>Overflowing Passion<br>On the Move<br>Great Haste<br>Devil-May-Care<br>From the First Step<br>**Lose Yourself<br>Thousand-Mile Journey** | If whale+ | Good power card for lates, sadly only viable from 3LB+, with its biggest bonus (20% training effectiveness) locked behind MLB |
| TM Opera O (Event) | Early Apr '27 *(est.)* | Pace | MLB | Stamina Bonus +1 and Power<br>Bonus +1 when bond is 80+<br>Training Eff. (10%)<br>Friendship Bonus (20%)<br>Specialty Priority (50) | Pace Chaser Straightaways<br>Ramp Up<br>Toward Victory<br>Corner Recovery<br>Preferred Position<br>**Speed Star** | Free | Lacking everywhere, in my most honest opinion |
| Meisho Doto | Early Apr '27 *(est.)* | Late | 3LB+ | Speed Bonus +3 when<br>bond is full<br>Friendship Bonus (25-30%)<br>Specialty Priority (50-80)<br>Power Bonus +1<br>Skill Point Bonus +1<br>Mood Effect (20-40%) (1LB+)<br>Training Eff. (5-10%) (3LB+) | Right-Handed<br>Pace Chaser Corners<br>Late Surger Straightaways<br>Uma Stan<br>Forward Step by Step<br>1,500,000 CC<br>Full Throttle<br>Slick Surge<br>Tooth and Tail<br>On the Move<br>**Blitzing Spirit** | No | Very expensive card for lates, with most of its good bonuses locked behind LBs |
| Agnes Digital | Early Apr '27 *(est.)* | Mile | 3LB+ | Wit Bonus +1 per speed<br>skill, up to 3 skills (max. +3)<br>Friendship Bonus (20-25%)<br>Mood Effect (40-50%)<br>Wit Friendship Recovery (3-5)<br>Specialty Priority (50-65)<br>Speed Bonus +1<br>Skill Points Bonus +1 (1LB+)<br>Training Eff. (5-10%) (3LB+) | Mile Corners<br>Mile Straightaways<br>Slipstream<br>Unyielding Spirit<br>Pumped<br>Boiling Emotions<br>Wind Vane<br>Mighty Leap<br>High Pitch<br>**Brave and Bold** | No | Also pretty expensive card for miles, when we've recently gotten another wit mile card in the shape of Taiki Shuttle |
| Blast Onepiece | Late Apr '28 *(est.)* | Pace<br>(Long+) | 3LB+ | Power Bonus +2 when<br>bond is 80+<br>Friendship Bonus (25-30%)<br>Mood Effect (40-50%)<br>Power Bonus +1<br>Specialty Priority (50-65)<br>Skill Point Bonus +1 (1LB+)<br>Training Eff. (5-10%) (3LB+) | Pace Chaser Straightaways<br>Long Straightaways<br>Corner Adept<br>Uma Stan<br>Attack Stance<br>Decisive Blow<br>Believe in Yourself<br>Sready Effort<br>Honing In<br>Stamina to Spare<br>**Forthright<br>Fruits of Labor** | No | Very niche pace card for longs Decent skills for parents, but that's about it Pretty expensive card, too |
| Maruzensky (Event) | Early May '28 *(est.)* | Front | MLB | Speed Bonus +1 and Skill Point<br>Bonus +1 when bond is 80+<br>Friendship Bonus (30%)<br>Mood Effect (30%)<br>Specialty Priority (50) | Front Runner Corners<br>Focus<br>Playtime's Over!<br>An Honest Step<br>Final Push<br>Early Lead<br>Moxie<br>**Untouchable Shadow** | Free | Free card, and like most of them, pretty weak at this point of the game |
| Symboli Rudolf | Early May '28 *(est.)* | **All-rounder**<br>(Pace/Late+) | 3LB+ | Speed Bonus +1 and Wit<br>Bonus +1 when bond is 80+<br>Friendship Bonus (25-30%)<br>Mood Effect (20-30%)<br>Specialty Priority (50-80)<br>Wit Friendship Recovery (3-5)<br>Skill Point Bonus +1<br>Wit Bonus +1 (1LB+)<br>Training Eff. (10-20%) (3LB+) | Medium Straightaways<br>Uma Stan<br>Slipstream<br>Tail Held High<br>Rapid<br>Downhill Speedster<br>Early Race Adept<br>Satisfying Pace<br>Dynamic Motion<br>Check<br>**In The Right Place!** | **100 Free Pulls**<br>Yes *(est.)* | Becomes the standard generalist wit card Very strong bonuses, although they're locked behind 3LB+, but the investment is worth it Most hints are pretty good and generalist skills, and the golds are also pretty good |
| Mejiro Ardan | Early May '28 *(est.)* | **Pace**<br>Mile/Medium | 3LB+ | Stamina Bonus +1 and Power<br>Bonus +1 when bond is 80+<br>Friendship Bonus (28-40%)<br>Mood Effect (20-30%)<br>Specialty Priority (50-80)<br>Race Bonus (5-10%)<br>Training Eff. (5-10%) (1LB+)<br>Skill Points Bonus +1~2 (3LB+) | Left-Handed<br>Pace Chaser Corners<br>An Honest Step<br>Attack Stance<br>Leap Premonition<br>Decisive Blow<br>Restless Step<br>Graceful Step<br>Refined Conduct<br>Surpassing Ambitions<br>**Pure Perfection<br>Curtain Closer** | **100 Free Pulls**<br>With Rudolf<br>or<br>If dedicated<br>to Paces *(est.)* | Strong power card for paces, especially for miles and mediums Very powerful bonuses and skills |
| Seeking the Pearl | Late May '28 *(est.)* | **Sprint** | 1LB+ | Speed Bonus +2 and Skill Point<br>Bonus +1 when bond is full<br>Friendship Bonus (25-30%)<br>Mood Effect (40-50%)<br>Training Eff. (5%)<br>Specialty Priority (50-80)<br>Speed Bonus +1<br>Power Bonus +1<br>Skill Point Bonus +1 (1LB+) | Sprint Corners<br>Sprint Straightaways<br>Uma Stan<br>Turning Point<br>Sprinting Gear<br>Explosive Force<br>Pounding Chest<br>Mighty Leap<br>Single-Minded Advance<br>**Unyielding Tenacity** | No | Strong as a statstick if you're using her outside of a sprint deck, other than that, she's really just a speed card for sprints, pretty strong for lates specifically Last-by-one banner before the 4th Anniversary, though |
| Nice Nature (Event) | Early Jun '28 *(est.)* | Late | MLB | Training Eff. (10%) when bond<br>is 80+<br>Friendship Bonus (25%)<br>Guts Bonus +1<br>Stamina Bonus +1<br>Specialty Priority (50) | Ramp Up<br>Position Pilfer<br>Fearless<br>Eager<br>Pace Strategy<br>Be Still<br>**Relax** | Free | Average free card, not bad, not really good either Useable if you have nothing else to use |
| Ikuno Dictus | Early Jun '28 *(est.)* | **Mile** | 3LB+ | Speed Bonus +2 when<br>bond is 80+<br>Friendship Bonus (25-35%)<br>Mood Effect (20%)<br>Specialty Priority (50-65)<br>Wit Friendship Recovery (3-5)<br>Speed Bonus +1<br>Skill Point Bonus +1<br>Training Eff. (5-10%) (1LB+)<br>Wit Bonus +1~2 (3LB+) | Mile Corners<br>Mile Straightaways<br>Groundwork<br>Unyielding Spirit<br>Boiling Emotions<br>Wind Vane<br>Rushing in Blind<br>Pounding Chest<br>**Big-Sisterly** | If whale+++ | Very packed card for a reason: this is the last banner of the scenario, I'd say it's carat bait Despite being a really good card stat-wise and with very good skills for miles, I wouldn't recommend pulling on this banner unless you're ready to swipe, or if you've been saving up a lot |
| Curren Chan | Early Jun '28 *(est.)* | Sprint | MLB | Speed Bonus +1 and Guts<br>Bonus +1 when bond is 80+<br>Friendship Bonus (25-35%)<br>Mood Effect (20%)<br>Specialty Priority (50-65)<br>Speed Bonus +1<br>Skill Points Bonus +1 (1LB+)<br>Training Eff. (5-10%) (3LB+) | Sprint Corners<br>Sprint Straightaways<br>Early Race Adept (ends 1st chain)<br>Groundwork<br>Focus<br>Swift Takeoff<br>Sprinting Gear<br>Explosive Force<br>Flying Sparks<br>Light as a Feather<br>**Fierce Clash<br>Concentration** | With<br>Ikuno Dictus | Good for sprints, but suffers the same fate as Ikuno Dictus wit, this is the last banner of the scenario so it's pointless pulling right now |

#### The Twinkle Legends

**Release timing (Global):** Late Jun '28

- Scenario gimmick: you're tasked to save the Twinkle Series by holding the Dream Fest, with the help of three legendary Umamusume, St. Lite, Speed Symboli and Haiseiko. When training, there will be a colored wing above each action, increasing the Instruction Gauge of said color, and every 6 turns you'll get to choose a Knowledge Stamp, with different effects, colors and stars (all based on your instruction gauges), when you reach 10 stamps, you can replace another of your choosing. At the start of Classic Year Summer, you'll get a Legends' Guidance buff, based on the stamps you have the most of. St. Lite's gives an enhanced Mood effect, and can be reactivated by getting three mood ups after it expires. Haiseiko's gives a new friendship gauge to fill up which ends in a strong rainbow training, and also introduces 5 NPCs that will assist in training (similar to how support cards work) Speed Symboli gives an enhanced training state that increases stat gains and reduces energy consumption, giving stronger buffs the more you keep it up. The state begins "weakening" (starts giving chances to end the special training) after the fourth turn, but gives more stats if you succeed the failure checks, resting or dating ends the state immediately. Besides, at the end of each year you'll participate in a race to level up your skill and get some stats and skill points. The scenario ends after the third race (no URA finals!)
- Scenario link: Orfevre (Soaring Stride (Sufficient Thrust)), Mejiro Ramonu (Reckless (Rushing in Blind)), Gentildonna (Flash Forward (Medium Straightaways)), Sirius Symboli (Hot Pursuit (Tooth and Tail)), Smart Falcon (Sandstorm Slash (Dirt Corners)), Embodiment of Legends (Battle for Initiative (Opening Leg Adept))
- Scenario skills: Ahead of the Gale (Beeline Burst), Pioneer of Dreams (Taking the Lead), Guidance of Many Moons (Check), Crossroads of Revolution (Exquisite Timing), Soar Above the Clouds (Soaring Stride), Advent of the Legends (Unprecedented Prodigy), Forger of Legends (Herald of a New Age)
- Scenario spark: Twinkle Legends (PWR/GUTS)

| Support Card | Date | Style/Distance | LB Breakpoints | Notable Bonuses | Notable Hints | Pull? | Notes |
|---|---|---|---|---|---|---|---|
| Embodiment of Legends | Late Jun '28 *(est.)* | **All-rounder** | 0LB+ | Skill Point Bonus +1 and All<br>Stats Bonus +1 when bond is full<br>Friendship Bonus (25-30%)<br>Race Bonus (5-10%)<br>Event Recovery (20-30%)<br>Event Effectiveness (15-20%)<br>Wit Friendship Recovery (1~2)<br>Training Eff. (5-10%) (3LB+) | Corner Adept<br>Early Race Adept<br>Mid Race Adept<br>Slipstream<br>Tail Held High<br>Peerless<br>Groundwork<br>Fighting Spirit<br>**Unprecedented Prodigy** | **100 free pulls**<br>Yes *(est.)* | Twinkle Legends' scenario pal (or rather, group) card A very strong card overall Try to aim for 0LB at least |
| Almond Eye | Late Jun '28 *(est.)* | **All-rounder**<br>(Medium+) | 0LB+ | Power Bonus +1 and Skill Point<br>Bonus +1 when bond is 80+<br>Friendship Bonus (25-35%)<br>Race Bonus (10-15%)<br>Specialty Priority (75-120)<br>Initial Skill Points +30~40<br>Speed Bonus +1<br>Skill Point Bonus +1 (1LB+)<br>Training Eff. (10-20%) (3LB+) | Corner Adept<br>Straightaway Adept<br>Uma Stan<br>Tail Held High<br>Nimble Navigator<br>Leap Premonition<br>To Greater Heights<br>Surpassing Ambitions<br>Dynamic Motion<br>Refined Conduct<br>**Singularity<br>Brilliant Mind<br>Beeline Burst<br>Professor of Curvature** | **100 free pulls**<br>Yes *(est.)* | The hints should tell you this card's power level. Strong even at 0LB, with insane scaling into MLB. Aim for 3LB at least when pulling! |
| Gran Alegria (Event) | Late Jun '28 *(est.)* | Mile | MLB | Power Bonus +2 when<br>bond is 80+<br>Friendship Bonus (30%)<br>Training Eff. (5%)<br>Specialty Priority (50)<br>Stamina Bonus +1 | Mile Straightaways<br>Rapid<br>Forward Step by Step<br>Pounding Chest<br>Pumped<br>Updrafters<br>**Cyclone Flash** | Free | Free anniversary card, it's... a card, most definitely |
| Mejiro Bright | Early Jul '28 *(est.)* | Late<br>Long | 0LB+ | Stamina Bonus +2 and Guts<br>Bonus +1 when bond is full<br>Friendship Bonus (25-35%)<br>Mood Effect (20%)<br>Training Eff. (5%)<br>Specialty Priority (50-80)<br>Stamina Bonus +1<br>Guts Bonus +1<br>Skill Point Bonus +1 | Late Surger Straightaways<br>Long Straightaways<br>Lock On<br>Fierce Struggle<br>Devil-May-Care<br>Preliminary Preparation<br>Great Haste<br>Fuse<br>Deep Breaths<br>Be Still<br>**In One Fell Swoop** | No | Up to +3 stamina, +2 guts and +1 skill point bonus at 0LB, which means it's probably a great statstick card, but with Air Shakur around, it's not that much of a necessity, not even for late surgers |
| Symboli Kris S (Event) | Late Jul '28 *(est.)* | Long | MLB | Training Eff. (10%) when<br>bond is 80+<br>Friendship Bonus (35%)<br>Specialty Priority (50)<br>Speed Bonus +1 | Homestretch Haste<br>Pressure<br>Lock On<br>Fervor<br>Pace Strategy<br>Deep Breaths<br>Free-Spirited<br>**Wind Slash** | Free | Meh free card, but well, it's free! Take it, like always |
| Dream Journey | Late Jul '28 *(est.)* | **End** | 1LB+ | Speed Bonus +1 and Power<br>Bonus +1 when bond is 80+<br>Training Eff. (10-15%)<br>Friendship Bonus (25-35%)<br>Mood Effect (20-30%)<br>Specialty Priority (50-80)<br>Race Bonus (5-10%)<br>Skill Point Bonus +1<br>Speed Bonus +1 (1LB+) | Right-Handed<br>End Closer Corners<br>Nimble Navigator<br>Masterful Gambit<br>Early Start<br>Boiling Blood<br>Sufficient Thrust<br>No Reluctance<br>Shadowstepper<br>Capture<br>Breakthrough Plan<br>**Complete Combustion<br>Relentless Approach** | If dedicated<br>to Ends | Finally a speed card for end closers. And it's really affordable too, becoming a really good card at 1LB. Strong gold skills, and also very good white ones on her hints list |
| Vodka | Late Jul '28 *(est.)* | Late<br>Medium | 1LB+ | Stamina Bonus +1 and Power<br>Bonus +1 when bond is 80+<br>Friendship Bonus (25-30%)<br>Mood Effect (40-60%)<br>Training Eff. (10-15%)<br>Specialty Priority (50-<br>Power Bonus +1<br>Skill Point Bonus +1 (1LB+)<br>Race Bonus (5-10%) (3LB+) | Left-Handed<br>Late Surger Corners<br>Late Surger Straightaways<br>Medium Corners<br>Nimble Navigator<br>Razor-Sharp Stride<br>Overflowing Passion<br>Satisfying Pace<br>Towards the Light<br>Foothold<br>**Incisive Flash<br>Breach** | With Dorija<br>or<br>If Whale<br>dedicated to<br>lates | Good power card for lates, great rainbow trainings and strong skills overall, but keep in mind Tamamo Cross power is close and is an scenario banner! |
| Daring Tact | Early Aug '28 *(est.)* | **Late** | 3LB+ | Wit Bonus +2 when<br>bond is 80+<br>Friendship Bonus (28-40%)<br>Training Eff. (5-10%)<br>Mood Effect (20%)<br>Race Bonus (5-10%)<br>Specialty Priority (50-80)<br>Wit Friendship Recovery (3-5)<br>Speed Bonus +1 (1LB+)<br>Skill Point Bonus +1~2 (3LB+) | Late Surger Straightaways<br>Downhill Speedster<br>Forward Step by Step<br>Position Pilfer<br>1,500,000 CC<br>Razor-Sharp Stride<br>Overflowing Passion<br>On the Move<br>Pushing Through!<br>Descent<br>Graceful Step<br>**Independence<br>Fast & Furious** | If dedicated<br>to Lates | An upgrade to Manhattan Cafe or Satono Diamond So a very good wit card for lates! |
| Espoir City (Event) | Late Aug '28 *(est.)* | Dirt | MLB | Speed Bonus +1 and Guts<br>Bonus +1 when bond is 80+<br>Friendship Bonus (30%)<br>Training Eff. (10%) | Mile Straightaways<br>Ramp Up<br>Go With the Flow<br>Wind Vane<br>At Full Speed<br>Dust Bath<br>Dust Off<br>**Trending in the Charts!** | Free | It's a dirt card if you haven't gotten one before. Also free ! |
| Buena Vista | Late Aug '28 *(est.)* | End<br>Medium | 3LB+ | Training Eff. (10%) when<br>there are 4 or more types of<br>cards in your deck<br>Friendship Bonus (25-30%)<br>Training Eff. (5-10%)<br>Mood Effect (20-30%)<br>Specialty Priority (50-65)<br>Race Bonus (5-10%)<br>Stamina Bonus +1<br>Skill Point Bonus +1 (1LB+)<br>Power Bonus +1~2 (3LB+) | End Closer Corners<br>Medium Straightaways<br>Overflowing Passion<br>Gateway to Success<br>Creeping Footsteps<br>Mighty Step<br>Glimpse of Light<br>Graceful Step<br>Dynamic Motion<br>Switch Over Pro<br>**Reign<br>Elated** | **80 Free Pulls**<br>No *(est.)* | Very specific card for end closers in medium races. I don't particularly find it worth pulling for it, but it is a strong card nonetheless, so consider your choices and plan accordingly Like in Vodka's banner, be wary, since Tamamo Cross' banner is just around the corner |
| Transcend | Late Aug '28 *(est.)* | Dirt | 3LB+ | Guts Bonus +2 when<br>bond is 80+<br>Friendship Bonus (25-30%)<br>Mood Effect (20-30%)<br>Specialty Priority (50-65)<br>Guts Bonus +1<br>Skill Point Bonus +1<br>Power Bonus +1 (1LB+)<br>Training Eff. (5-10%) (3LB+) | Dirt Corners<br>Dirt Straightaways<br>Playtime's Over!<br>Groundwork<br>Forward, March!<br>Top Pick<br>Pioneer<br>Contradicting Emotions<br>Sand Stride<br>**Sandstorm Flash<br>Magnificent Sand Stride** | **80 Free Pulls**<br>No | I wouldn't really go out of my way to pull a guts card specifically for dirt races, really |
| Silence Suzuka | Early Sep '28 *(est.)* | Front<br>Medium | 0LB+ | Speed Bonus +2 when<br>bond is 80+<br>Training Eff. (10-15%)<br>Friendship Bonus (25-30%)<br>Mood Effect (20%)<br>Specialty Priority (50-65)<br>Guts Bonus +1<br>Skill Point Bonus +1 | Left-Handed<br>Front Runner Straightaways<br>Groundwork<br>An Honest Step<br>Prudent Positioning<br>Fast-Paced<br>Outstanding Step<br>Early Bird<br>Unprecedented<br>Pulling Away<br>Riding the Tailwind<br>**The Fight's Not Over Yet!<br>Escape Artist** | No | Again, hyper-specific guts card which I wouldn't really go for Also has hint frequency locked behind 3LB which I think is really mean |
| Air Messiah (Event) | Late Sep '28 *(est.)* | Late | MLB | Speed Bonus +1 and Wit<br>Bonus +1 when bond is 80+<br>Friendship Bonus (25%)<br>Mood Effect (40%)<br>Specialty Priority (50)<br>Wit Friendship Recovery (5) | Highlander<br>Go With the Flow<br>Descent<br>Position Pilfer<br>Slick Surge<br>Fuse<br>**15,000,000 CC** | Free | Surprisingly...decent? Nothing out of the ordinary and at this point you should already have gotten a decent late wit card, but she might work...? |
| Daring Heart | Late Sep '28 *(est.)* | Mile<br>(Pace+) | 3LB+ | Speed Bonus +1 and Skill Point<br>Bonus +1 when bond is 80+<br>Friendship Bonus (25-35%)<br>Mood Effect (30-40%)<br>Specialty Priority (50-80)<br>Wit Friendship Recovery (3-5)<br>Speed Bonus +1<br>Training Eff. (5-10%) (1LB+)<br>Wit Bonus +1~2 (3LB+) | Mile Corners<br>Pace Chaser Straightaways<br>Believe in Yourself<br>Head-On<br>Aggressive<br>Unyielding Spirit<br>Rushing in Blind<br>Fearless Advance<br>Pounding Chest<br>**Reckless** | No | Bait banner before new scenario, but if you insist, she's a decent mile card, good for paces |
| Rhein Kraft | Late Sep '28 *(est.)* | **Mile** | 1LB+ | Power Bonus +1 and Skill Point<br>Bonus +1 when bond is 80+<br>Friendship Bonus (25-35%)<br>Training Eff. (10-15%)<br>Specialty Priority (50-80)<br>Speed Bonus +1<br>Mood Effect (20-40%) (1LB+)<br>Race Bonus (5-10%) (3LB+) | Mile Corners<br>Mile Straightaways<br>Groundwork<br>An Honest Step<br>Overflowing Fighting Spirit<br>Productive Plan<br>Shifting Gears<br>Wind Vane<br>Mighty Leap<br>High Hopes<br>**Changing Gears<br>High Voltage** | No | Strong mile-specific speed card, especially for fronts and paces But the timing couldn't be more awful, right before a new scenario If you can, I'd try to get this card to 1LB through vouchers instead! |

#### Design Your Island

**Release timing (Global):** Early Oct '28

- Scenario gimmick: build your facilities and train in a deserted island. Easy work for an Umamusume, duh. You have a Construction Plan that refreshes 6 months, as well as a Development Gauge that keeps tracks of your facilities' development. You get to choose the construction plan (and therefore, the facilities you're upgrading) at the start of each construction phase. From level 3 onwards, your facilities can take an Instinct Full Throttle build (more stat gains, takes more to build) or Skilled Technique Route (more skill points and hints, cheaper to build). You can also build a Beach House that allows Island Training, a combination of all your trainings together, giving increased stats depending on your construction plan, as well as bond levels to all your supports. You can access island training after acquiring its tickets, two are given throughout each construction plan phase. During summer, facilities are replaced by their Island Versions which boosts several stats at the same time, with stronger clicks depending on the upgrades of your facilities. After each construction plan phase, an Evaluation Meeting will be held, which will provide stats and extra bonuses based on your development points.
- Scenario link: Mejiro Ryan (Top Gear (Razor-Sharp Stride)), Ines Fujin (Just Rule (Frontal Breakthrough)), Sakura Chiyono O (Breaking Free (Aggressive)), Gold City (Surging Beat (Rising Passion), Tamamo Cross (Tail Nine (Tail Held High)), Tucker Bryne (It's On! (Ramp Up))
- Scenario skills: Earth-Shaking Dash (In Body and Mind), Nature's Rhythm (Killer Tunes), Wild at Heart (Elated), Unyielding Survivalist Spirit (Never Give Up), Trails of Pioneers (Pathfinder), Trials into the Unknown (Long Haul), Guided By Instinct (Be Myself)
- Scenario spark: Desert Island (STA/WIT)

| Support Card | Date | Style/Distance | LB Breakpoints | Notable Bonuses | Notable Hints | Pull? | Notes |
|---|---|---|---|---|---|---|---|
| Tucker Bryne | Early Oct '28 *(est.)* | **All-rounder**<br>(Medium/Long+) | 3LB+ | Unique<br>Training Eff. (5-10%)<br>Mood Effect (20-30%)<br>Energy Reduction (10-20%)<br>Failure Protection (15-20%)<br>Stamina Bonus +1<br>Guts Bonus +1 (1LB+) | Straightaway Recovery<br>Fuse<br>Find a Way!<br>**Pathfinder** | **100 Free Pulls**<br>Conditional *(est.)* | Scenario tax, but a bit more expensive than we're used to, since part of her strongest scenario link buff is locked behind 3LB |
| Tamamo Cross | Early Oct '28 *(est.)* | **All-rounder** | 1LB+ | Mood Effect (60%) when<br>rainbow training<br>Friendship Bonus (28-40%)<br>Race Bonus (5-10%)<br>Specialty Priority (60-100)<br>Initial Skill Points +15~30<br>Stamina Bonus +1<br>Power Bonus +1<br>Skill Point Bonus +1 (1LB+)<br>Training Eff. (5-10%) (3LB+) | Early Race Adept<br>Tail Held High<br>Homestretch Haste<br>Rapid<br>Forward Step by Step<br>Peerless<br>Nimble Navigator<br>Slipstream<br>Mold Breaker<br>Trekker<br>**Divine Speed<br>Proven Mettle<br>Long Haul** | **100 Free Pulls**<br>Conditional *(est.)* | Strongest general power card when it releases, very strong hints, comes with free pulls ! |
| Fusaichi Pandora (Story) | Early Oct '28 *(est.)* | Pace | MLB | Speed Bonus +1 and Skill Point<br>Bonus +1 when bond is 80+<br>Friendship Bonus (35%)<br>Mood Effect (20%)<br>Specialty Priority (65) | Pace Chaser Corners<br>Homestretch Haste<br>Go With The Flow<br>Straight Descent<br>Firm Step<br>Leap Premonition<br>Switch Over Pro<br>Preferred Position<br>**Bravery Slash** | Free | Decent pace card for parents It's free |
| Mejiro Ryan | Late Oct '28 *(est.)* | Late<br>Medium | 1LB+ | Guts Bonus +2 when<br>bond is 80+<br>Friendship Bonus (30%)<br>Mood Effect (40-60%)<br>Training Eff. (10%)<br>Specialty Priority (80)<br>Skill Point Bonus +1<br>Stamina Bonus +1 (1LB+) | Late Surger Corners<br>Fearless<br>Slick Surge<br>Ceaseless Training<br>Preliminary Preparation<br>Descent<br>All I've Got<br>Eager<br>Foothold<br>Take the Chance<br>Pace Strategy<br>**Latent Fighting Spirit** | If Whale+ | Non-generalist stamina cards are a luxury, and this is one of those. Strong card for lates in mediums, if you need an stamina card for those It's very strong even at 1LB! |
| Vivlos (Event) | Early Nov '28 *(est.)* | Late<br>Mile | MLB | Power Bonus +2 when<br>bond is 80+<br>Friendship Bonus (30%)<br>Mood Effect (20%)<br>Race Bonus (10%)<br>Specialty Priority (50) | Late Surger Straightaways<br>Downhill Speedster<br>1,500,000 CC<br>From the First Step<br>Unyielding Spirit<br>**Full of Vigor** | Free | Gold is strong for lates in miles... and that's about it Free card :) |
| Win Variation | Early Nov '28 *(est.)* | **Long** | 2LB+ | Wit Bonus +2 when<br>bond is 80+<br>Friendship Bonus (25-35%)<br>Mood Effect (40-50%)<br>Specialty Priority (50-80)<br>Wit Friendship Recovery (3-5)<br>Speed Bonus +1<br>Skill Point Bonus +1~2<br>Training Eff. (5-10%) (1LB+) | Right-Handed<br>Long Corners<br>Long Straightaways<br>Peerless<br>Find a Way!<br>Inside Scoop<br>Fierce Struggle<br>Enthusiastic<br>Unwavering Heart<br>Rapid Overtakes<br>Straightaway Recovery<br>Stay the Course<br>**Innate Experience<br>Energetic** | If Whale<br>or<br>with Duramente | Veeeery good wit card for longs, with a bunch of caveats: it's good at 1LB with 5% training effectiveness, that goes up to 10% at 2LB. She has no initial friendship gauge until 3LB, which might hurt a bit. And she also gets an extra skill point bonus at MLB |
| Duramente | Early Nov '28 *(est.)* | End | 0LB+ | Stamina Bonus +1 and Guts<br>Bonus +1 when bond is 80+<br>Friendship Bonus (35%)<br>Training Eff. (10-15%)<br>Specialty Priority (80)<br>Stamina Bonus +1<br>Guts Bonus +1<br>Skill Point Bonus +1 | End Closer Corners<br>End Closer Straightaways<br>Slipstream<br>Bare Passion<br>Breakthrough Plan<br>Chasing the Shadow<br>Give Chase<br>Straightaway Spurt<br>Ignition<br>High Ambitions<br>Immovable Spirit<br>**Soaring Stride<br>Afterimage** | If Whale<br>or<br>with Win<br>Variation | Like Mejiro Ryan, a luxury card for end closers with very strong hints. It's pretty strong even at 0LB, with more LBs giving her 5% training effectiveness, 5% race bonus, 5 more initial bond, and some more hint frequency and levels |
| Chrono Genesis (Event) | Late Nov '28 *(est.)* | Pace<br>Medium | MLB | Speed Bonus +1 and Wit<br>Bonus +1 when bond is 80+<br>Friendship Bonus (30%)<br>Training Eff. (5%)<br>Specialty Priority (50)<br>Wit Friendship Recovery (5)<br>Wit Bonus +1 | Tooth and Tail<br>Restless Step<br>Unshakeable Faith<br>Frontal Breakthrough<br>**Killer Tunes** | Free | Statstick free wit card, but the hints are pretty weak |
| Admire Groove | Late Nov '28 *(est.)* | **Late<br>Medium** | 3LB+ | Speed Bonus +1 and Power<br>Bonus +1 when bond is 80+<br>Friendship Bonus (25-30%)<br>Mood Effect (20-30%)<br>Training Eff. (1-20%)<br>Race Bonus (10-15%)<br>Specialty Priority (60-100)<br>Skill Point Bonus +1~2<br>Initial Skill Points 5~50 | Medium Corners<br>Medium Straightaways<br>1,500,000 CC<br>Fearless<br>Simmering Heat<br>Descent<br>Overflowing Passion<br>Aim for the Summit<br>Foothold<br>Dynamic Motion<br>Model Student<br>Take the Chance<br>**Natural Talent<br>Brains and Beauty** | **120 Free Pulls**<br>If dedicated<br>to lates<br>or<br>With Stego *(est.)* | Very strong card for lates, especially in medium Consider the following: either complete your free pulls and get her to 3LB+, or wait for Eishin Flash, coming out a bit later |
| Stay Gold | Late Nov '28 *(est.)* | **All-rounder**<br>(Medium+) | 0LB+ | Unique<br>Friendship Bonus (25-35%)<br>Mood Effect (20%)<br>Training Eff. (5%)<br>Specialty Priority (60-100)<br>Guts Bonus +1<br>Skill Point Bonus +1<br>Initial Skill Points 25~50 | Corner Adept<br>Straightaway Adept<br>Uma Stan<br>Slipstream<br>Unbreakable Mind<br>Forward Step by Step<br>Peerless<br>Intrigued<br>Groundwork<br>Ignition<br>Dream-Fulfilling Challenge<br>Carefree Step<br>**Never Give Up<br>Curiosity<br>Freewheeling** | **120 Free Pulls**<br>Yes *(est.)* | Who would've thought Orfevre's dad put her son to rest? Very strong guts card due to her unique, and also gold skills Gets a lot better with more LBs, with more initial bond, better hints and more priority, but definitely useable even at 0LB |
| Danstu Flame (Event) | Early Dec '28 *(est.)* | Medium<br>(Pace/Late+) | MLB | Training Eff. (10%) when<br>bond is 80+<br>Friendship Bonus (25%)<br>Speed Bonus +1<br>Power Bonus +2<br>Specialty Priority (35) | Unbreakable Mind<br>Prepared to Pass<br>Tooth and Tail<br>Slick Surge<br>Full Throttle<br>Refined Conduct<br>To Greater Heights<br>**Come What May** | Free | About average free card, nothing outstanding, really |
| Calstone Light O | Early Dec '28 *(est.)* | **Sprint** | 1LB+ | Speed Bonus +2 when<br>bond is 80+<br>Friendship Bonus (35%)<br>Mood Effect (60%)<br>Training Eff. (1-10%)<br>Race Bonus (1-10%)<br>Specialty Priority (80)<br>Speed Bonus +1<br>Skill Point Bonus +1 | Sprint Straightaways<br>Straightaway Adept<br>Playtime's Over<br>An Honest Step<br>Prudent Positioning<br>In No Time<br>No Second Thoughts<br>No Third Chances<br>Sprinting Gear<br>Swift Takeoff<br>Unyielding Step<br>Pounding Chest<br>**In High Spirits<br>Foregone Conclusion** | With Durandal | Strong card for sprints, which happen competitively like twice a year at most, so not exactly a priority But she's very strong as a sprint card |
| Durandal | Early Dec '28 *(est.)* | **End**<br>Sprint | 0LB+ | Speed Bonus +1 and Skill Point<br>Bonus +1 when bond is 80+<br>Friendship Bonus (30%)<br>Mood Effect (60%)<br>Training Eff. (10-15%)<br>Specialty Priority (80)<br>Wit Friendship Recovery (3-5)<br>Wit Bonus +1~2 | End Closer Straightaways<br>Straightaway Adept<br>Breakthrough Plan<br>No Reluctance<br>Give Chase<br>Nosedive<br>Capture<br>Bare Passion<br>Heat Up<br>Mighty Leap<br>**Moonlit Flash<br>Lightning Speed<br>Swift Decision** | If dedicated<br>to Ends | Very strong wit card that provides a lot of stats even at 0LB Good hints for end closers, albeit no Spurt, so you might have to use this with Taishin wit, or on umas that already have Spurt/Encroaching Shadow in their kit |
| Daiichi Ruby | Early Dec '28 *(est.)* | Late<br>Sprint | 0LB+ | Training Eff. (10%) when<br>there are 4 different type of cards<br>Friendship Bonus (35%)<br>Training Eff. (5-10%)<br>Race Bonus (5-10%)<br>Specialty Priority (80-<br>Speed Bonus +1~2<br>Power Bonus +1<br>Skill Point Bonus +1 | Late Surger Corners<br>Sprint Straightaways<br>Slick Surge<br>With Pride<br>Turning Point<br>Single-Minded Advance<br>Prelude<br>Meticuluous Measures<br>Pounding Chest<br>Mighty Leap<br>Gap Closer<br>Radiant Treasure | No | Another very specific sprint card, now focused on lates I personally don't think you should take it over Stay Gold in any deck, so its value is heavily reduced |
| Tosen Jordan (Event) | Late Dec '28 *(est.)* | Late | MLB | Mood Effect (15%) and Power<br>Bonus +1 when bond is 80+<br>Friendship Bonus (30%)<br>Training Eff. (10%)<br>Specialty Priority (50) | Playtime's Over<br>Unbreakable Mind<br>Slick Surge<br>Overflowing Passion<br>Towards the Light<br>Be Still<br>**Dauntless** | Free | Another average free card, not much going on with it |
| Fuji Kiseki | Late Dec '28 *(est.)* | **Pace<br>Mile** | 0LB+ | Speed Bonus +1 and Power<br>Bonus +1 when bond is 80+<br>Friendship Bonus (35%)<br>Mood Effect (50%)<br>Training Eff. (5-10%)<br>Race Bonus (5-10%)<br>Specialty Priority (80)<br>Speed Bonus +1<br>Skill Point Bonus +1 | Mile Corners<br>Straightaway Adept<br>Nimble Navigator<br>Slipstream<br>Attack Stance<br>Prepared to Pass<br>Restless Stance<br>Head-On<br>High Hopes<br>Productive Plan<br>Fearless Advance<br>Resolute Stance<br>Refined Conduct<br>**Steadfast Spirit** | No | Very good card specifically made for paces in miles, again, I feel like such cards are pretty much a luxury, so it's up to you to know if you need it, or not Also, almost the last banner of the scenario |
| Eishin Flash | Late Dec '28 *(est.)* | **Late** | 0LB+ | Speed Bonus +1 and Power<br>Bonus +1 when bond is 80+<br>Friendship Bonus (25-35%)<br>Mood Effect (40-60%)<br>Training Eff. (10-15%)<br>Specialty Priority (50-80)<br>Skill Point Bonus +1 | Late Surger Corners<br>Late Surger Straightaways<br>Straightaway Adept<br>Ramp Up<br>Playtime's Over!<br>Fearless<br>Full Throttle<br>Overflowing Passion<br>From the First Step<br>Simmering Heat<br>Essence of Racing・Speed<br>Eyes on the Horizon<br>Glittering Star<br>**Thousand-Mile Journey<br>Heat Haze** | If dedicated<br>to Lates<br>and<br>didn't pull<br>Admire Groove | Someone get this woman out of speed card prison...? Very strong card for lates, again? Competes directly with Admire Groove, who was just released, for that spot in your deck Comparing both, this one gives slightly better speed trainings, whereas Admire Groove **(MLB)** gives more skill points At 0LB, Eishin Flash is better Also, almost the last banner of the scenario |
| Curren Bouquetd'Or | Early Jan '29 *(est.)* | Pace<br>Medium<br>(Long+) | 0LB+ | Friendship Bonus (20%) when<br>bond is 80+<br>Friendship Bonus (20%)<br>Mood Effect (30%)<br>Training Eff. (5%)<br>Race Bonus (5-10%)<br>Specialty Priority (80)<br>Stamina Bonus +1~2<br>Guts Bonus +1<br>Skill Point Bonus +1 | An Honest Step<br>Attack Stance<br>Leap Premonition<br>Time to Awaken<br>True Worth<br>Tooth and Tail<br>To Greater Heights<br>Luminance<br>Find a Way!<br>Corner Recovery<br>Stamina to Spare<br>**Blooming<br>Swinging Maestro** | No | Stats are somewhat underwhelming until MLB, compared to other cards we've been getting, plus it's the last banner of the scenario, huge skip |

**Notes attached to individual cells:**

- **Tucker Bryne** (Notable Bonuses): Tucker's unique gives +60 specialty priority for the next turn to cards that train with her So, if Almond Eye and Tamamo Cross train with her in the same facility, she'll give Almond Eye 180 priority and Tamamo Cross 160
- **Tucker Bryne** (Pull?): This banner is known for being somewhat skippable. If you've pulled for other power cards like Vodka, Mejiro Ardan or Buena Vista, you might not need Tamamo Cross. Plus Tucker is an expensive pal card, so you can borrow it if you need her.
- **Tamamo Cross** (Pull?): This banner is known for being somewhat skippable. If you've pulled for other power cards like Vodka, Mejiro Ardan or Buena Vista, you might not need Tamamo Cross. Plus Tucker is an expensive pal card, so you can borrow it if you need her.
- **Stay Gold** (Notable Bonuses): Like father, like son. Stay Gold has the same unique as Orfevre guts! Very strong unique that gives +1 stat bonus per card on your deck, depending on their type, when bond is 80+ So, a deck with 2 speed, 1 power, 1 wit, 1 pal and Stay Gold means the card would get +2 speed, +1 power, +1 wit, +1 guts, +1 skill point bonus!

#### Yukoma Hot Springs

**Release timing (Global):** Late Jan '29

- Scenario gimmick: time to take a rest at the Onsen. You'll be excavating for new Hot Springs, after choosing an excavation type, every action will count towards building it, shown in a progress bar. While excavating, there will be three ground types (Sand, Soil, Rock), which will require different tools to excavate through, and their effectiveness are based on your stats. When selecting a spring to dig, you'll be shown a tool to level up, and its effectiveness based on your stats and sparks (speed, power and guts sparks!) Throughout your career, you'll obtain Onsen Tickets, which provide energy and a bunch of buffs that last for two turns. Randomly, you might get a Super Recovery, which boosts your max energy to 150, gives extra energy, skill points and hints. There's also a PR Activity button that provides an onsen ticket at the expense of some energy. Each spring you dig up grants bonuses to your onsen tickets. At the end of each year, you'll get a Bathing Party, which will give you a ranking based on how many springs you were able to excavate. Better rank gives better super recovery buffs.
- Scenario link: Tokai Teio (+10 digging on Sand, Unstoppable (Attack Stance)), Mihono Bourbon (+10 digging on Soil, Untouchable Shadow (Steadfast)), Transcend (+10 digging on Soil, Concentration (Focus)), Hokko Tarumae (+10 digging on Rock, Magnificent Sand Stride (Sand Stride)), Wonder Acute (+10 digging on Rock, Hot Pursuit (Tooth and Tail)), Kiyoko Hoshina
- Scenario skills: First in the Bath! (Taking the Lead), Hot Spring Dash, (See Ya Later!), Bathe in Moderation (Exquisite Timing), Secret Onsen Power (Proven Mettle), Geyser Spirit (Surging Spirit), Battle For Initiative, Exquisite Timing, Miracle of Recreation (Rest and Rise)
- Scenario spark: Yukoma Hot Springs (GUTS/WIT)

| Support Card | Date | Style/Distance | LB Breakpoints | Notable Bonuses | Notable Hints | Pull? | Notes |
|---|---|---|---|---|---|---|---|
| Kiyoko Hoshina | Late Jan '29 *(est.)* | **All-rounder** | 0LB+ | Training Eff. (5%) and Energy<br>Reduction (5%) when bond is 60+<br>Mood Effect (40-60%)<br>Training Eff. (1-10%)<br>Failure Protection (10-15%)<br>Energy Reduction (15-25%)<br>Skill Point Bonus +1 | Early Race Adept<br>Mid Race Adept<br>**See Ya Later!** | **80 Free Pulls**<br>Yes *(est.)* | Scenario tax, but at least this time it's useable at 0LB |
| Tokai Teio | Late Jan '29 *(est.)* | **Pace** | 0LB+ | Skill Point Bonus +2 when<br>bond is 80+<br>Training Eff. (10-15%)<br>Friendship Bonus (25-35%)<br>Mood Effect (60-100%)<br>Race Bonus (5-10%)<br>Specialty Priority (60-100)<br>Initial Skill Points (30-60) | Pace Chaser Corners<br>Pace Chaser Straightaways<br>Peerless<br>Attack Stance<br>Head On<br>Restless Step<br>Time to Awaken<br>One Brave Step<br>To Greater Heights<br>Dynamic Motion<br>Luminance<br>**Surging Spirit<br>Forthright<br>To the Stage of Dreams** | **80 Free Pulls**<br>With Kiyoko<br>and<br>MLB if dedicated<br>to Paces *(est.)* | Veeery strong pace card, missing maybe one or two speed or power bonuses, but otherwise comes with a nice 100% mood effect (which is the same as 30% training effectiveness when in great mood) All hints are given at level 5 and also has 100% hint frequency, so it's basically a must for any pace going forward 0LB is great, MLB is insane value |
| Mihono Bourbon | Early Feb '29 *(est.)* | **Front** | 0LB+ | Skill Point Bonus +2 when<br>bond is 80+<br>Training Eff. (10-15%)<br>Friendship Bonus (28-40%)<br>Mood Effect (20-30%)<br>Race Bonus (1-15%)<br>Specialty Priority (60-100)<br>Stamina Bonus +1 | Front Runner Corners<br>Front Runner Straightaways<br>Groundwork<br>Prudent Positioning<br>Focus<br>Fast-Paced<br>Spearhead<br>Leader's Pride<br>Outstanding Step<br>Running is Winning!<br>Early Lead<br>**Taking the Lead<br>Preeminent** | If Whale+ | If you can spare the carats, this is a pretty great power card for fronts, who didn't have an specific power card yet |
| Orfevre (Event) | Late Feb '29 *(est.)* | End | MLB | Stamina Bonus +1 and Skill<br>Point Bonus +1 when bond is 80+<br>Training Eff. (10%)<br>Friendship Bonus (20%)<br>Mood Effect (30%)<br>Race Bonus (10%)<br>Specialty Priority (50) | Rapid<br>Early Start<br>Breakthrough Plan<br>Sufficient Thrust<br>Chasing the Shadow<br>Seize the Chance<br>Mold Breaker<br>Rising Passion<br>**Go-Home Specialist** | Free | Slightly-above-average free card, useable if you have nothing else, I guess? |
| Fenomeno | Late Feb '29 *(est.)* | Pace<br>Long | 0LB+ | Stamina Bonus +1 and Skill<br>Point Bonus +1 when bond is 80+<br>Training Eff. (10-15%)<br>Friendship Bonus (25-35%)<br>Mood Effect (40-50%)<br>Race Bonus (1-10%)<br>Specialty Priority (50-80)<br>Stamina Bonus +1<br>Skill Point Bonus +1 | Long Corners<br>Decisive Blow<br>Brute Force<br>One Brave Step<br>Rising Passion<br>Feature Act<br>Steady Effort<br>Take the Plunge<br>True Worth<br>Honing In<br>**Headliner<br>Laser-Focused** | No | I don't personally think specific stamina cards have a strong value, you're almost always only bringing one and it's hard to take that spot from Air Shakur at the moment |
| Gold Ship | Late Feb '29 *(est.)* | End<br>Long | 3LB+ | Stamina Bonus +2 when<br>bond is 80+<br>Friendship Bonus (25-35%)<br>Mood Effect (40-60%)<br>Training Eff. (1-10%)<br>Race Bonus (5-10%)<br>Specialty Priority (10-80)<br>Skill Point Bonus +1 | End Closer Straightaways<br>Long Corners<br>Uma Stan<br>Boiling Blood<br>Gateway to Success<br>Capture<br>Give Chase<br>Straightaway Spurt<br>Surprise Attack<br>Lock On<br>Seize the Chance<br>Rapid Overtakes<br>Immovable Spirit<br>**Encroaching Shadow<br>Clear Mind** | No | Same as Fenomeno, but even worse, since her specialty priority is hidden behind 3LB |
| Inari One | Early Mar '29 *(est.)* | Late<br>Long | 0LB+ | Guts Bonus +1 and Skill Point<br>Bonus +1 when bond is 80+<br>Friendship Bonus (25-35%)<br>Mood Effect (40-60%)<br>Training Eff. (10-15%)<br>Race Bonus (5-10%)<br>Specialty Priority (50-80) | Right-Handed<br>Long Corners<br>Long Straightaways<br>Devil-May-Care<br>Preliminary Preparation<br>Bare Passion<br>Rising Passion<br>Surprise Attack<br>Unwavering Heart<br>Great Haste<br>Crucial Stage<br>**Lose Yourself<br>Thorough Preparation** | No | Whatever possessed Cygames to make stamina cards for longs during these 3-4 weeks But...yeah, same as Fenomeno and Gold Ship, these cards are ultra-specific and feel like an extreme luxury |
| Bubble Gum Fellow (Event) | Late Mar '29 *(est.)* | Pace | MLB | Guts Bonus +1 and Skill Point<br>Bonus +1 when bond is 80+<br>Friendship Bonus (30%)<br>Mood Effect (40%)<br>Race Bonus (10%)<br>Specialty Priority (50) | Corner Acceleration<br>Groundwork<br>Ambitions<br>Tooth and Tail<br>Attack Stance<br>Aggressive<br>Head-On<br>**Valiant Flash** | Free | Like Orfevre, a little above average free card, decent hints for paces |
| Air Groove | Late Mar '29 *(est.)* | Pace/Late<br>**Medium** | 0LB+ | Training Eff. (5%) and Power<br>Bonus +1 when bond is 80+<br>Friendship Bonus (25-35%)<br>Mood Effect (20-30%)<br>Training Eff. (6-20%)<br>Race Bonus (5-10%)<br>Specialty Priority (75-120)<br>Skill Point Bonus +1~2 | Left-Handed<br>Medium Corners<br>Medium Straightaways<br>Tooth and Tail<br>Believe in Yourself<br>Preliminary Preparation<br>No Stagnation<br>All I've Got<br>Fighting Spirit<br>Towards the Light<br>Dynamic Motion<br>Dream-Fullfilling Challenge<br>**Check<br>Thousandfold Tempering<br>Crowning Beauty** | **100 Free Pulls**<br>Yes *(est.)* | 120 priority, 25% training effectiveness, power and skill point bonuses...I'll let you judge for yourself But yeah, strong at 0LB, gets massively stronger at MLB |
| Fine Motion | Late Mar '29 *(est.)* | Pace | 0LB+ | Power Bonus +1 and Hint Lv. +1<br>when bond is 80+<br>Friendship Bonus (28-40%)<br>Mood Effect (30-40%)<br>Training Eff. (10-15%)<br>Specialty Priority (60-100)<br>Skill Point Bonus +1~2 | Corner Adept<br>Straightaway Adept<br>Downhill Speedster<br>An Honest Step<br>Leap Premonition<br>Straight Descent<br>Aggressive<br>Ride the Momentum<br>Committed Push<br>Refined Conduct<br>With Light in my Heart<br>Essence of Racing・Stamina<br>Blessing of the Sun<br>**Send it Flying!<br>Smooth Sailing** | **100 Free Pulls**<br>Yes *(est.)* | Very strong power card that formally powercreeps Tamamo Cross, especially for paces Look at all those hints! |
| King Halo | Early Apr '29 *(est.)* | Late | 0LB+ | Power Bonus +1 and Skill Point<br>Bonus +1 when bond is 80+<br>Friendship Bonus (25-35%)<br>Mood Effect (20%)<br>Training Eff. (10-15%)<br>Race Bonus (5-10%)<br>Specialty Priority (50-80)<br>Guts Bonus +1 | Late Surger Straightaways<br>Forward Step by Step<br>Intrigued<br>Homestretch Haste<br>Position Pilfer<br>1,500,000 CC<br>Preliminary Preparation<br>Slick Surge<br>Pushing Through!<br>Bare Passion<br>Mighty Leap<br>Footloose<br>**Blitzing Spirit<br>United We Stand** | No | Not any better than other guts cards, not even for late specific builds |
| Silence Suzuka (Event) | Late Apr '29 *(est.)* | Front<br>Mile | MLB | Mood Effect (15%) and Speed<br>Bonus +1 when bond is 80+<br>Friendship Bonus (30%)<br>Wit Friendship Recovery (5)<br>Specialty Priority (35)<br>Speed Bonus +1<br>Skill Point Bonus +1 | Left-Handed<br>Mile Corners<br>Groundwork<br>Focus<br>Dodging Danger<br>Wind Vane<br>Pounding Chest<br>**Gale Flash** | Free | Interesting card because it has +2 speed and +1 skill points, which is nice for a free cards, but the rest of the bonuses are not good enough... |
| Neo Universe | Late Apr '29 *(est.)* | **Medium** | 0LB+ | Stamina Bonus +1 and Skill Point<br>Bonus +1 when bond is 80+<br>Friendship Bonus (25-35%)<br>Mood Effect (20%)<br>Training Eff. (10-20%)<br>Specialty Priority (60-100)<br>Power Bonus +1<br>Skill Point Bonus +1 | Tail Held High<br>Rapid<br>Forward Step by Step<br>On the Move<br>All I've Got<br>Ignition<br>Self-Restraint<br>Dream-Fulfilling Challenge<br>Take the Chance<br>Graceful Step<br>With a Light in my Heart<br>Find a Way!<br>**Luminiscence<br>Sharp-Witted Composure** | If Whale+ | Similar in performance to Fine Motion power, now more focused towards medium races It's the last banner of the scenario, so I'd say you've gotta be mindful of your pulls! |
| Matikanefukukitaru | Late Apr '29 *(est.)* | Pace<br>Long | 0LB+ | Training Eff. (10%) when<br>bond is 80+<br>Friendship Bonus (28-40%)<br>Mood Effect (30-40%)<br>Training Eff. (5-10%)<br>Race Bonus (5-10%)<br>Specialty Priority (80)<br>Power Bonus +1<br>Skill Point Bonus +1 | Right-Handed<br>Long Straightaways<br>Uma Stan<br>True Worth<br>Riding the Momentum<br>Overflowing Fighting Spirit<br>Honing In<br>Take the Plunge<br>True Worth<br>Inside Scoop<br>Up the Vibes<br>Fervor<br>**Gordian Cut** | With<br>Neo Universe | Not necessarily better than Almond Eye, nor Teio, nor Air Groove, so nothing really outstanding for this card Also the last banner of this scenario ! |

#### Beyond Dreams

**Release timing (Global):** Early May '29

- Scenario gimmick: mooom, the umas are travelling overseas! Again! But this time to America. Normal schedules are instead replaced by more real life-like schedules, which include a handful of national G1s before moving on to the international scene (specifically, the US races for the Breeders' Cup). You'll be joined by three Team Members from the DREAMS project, and each of them will have a personal Member Rank (G - US). Each team member grants additional Training Effectiveness, scaling off their rank. The overall Team Rank will be calculated based off the lowest scoring team member. After Debut and every 6 months after that, you'll organize a Reflection meeting which will yield better rewards the higher your team rank is. Right after, you'll initiate a Strategy Meeting, where you'll get to allocate Dreams Points for your Dreams Training into three different categories: Physical (Friendship Bonus, reduced Energy Cost), Technique (Training Effectiveness for SP Gain, more and several hints at the same time), Mental (extra bond, failure reduction, higher stat and SP limits) You'll get 2 DP after every strategy meeting, and 4 after the last one. Using one DP allows a Dreams Training that places all of your cards and team members into the same training facility of your choice, plus all of the buffs you've taken during strategy meetings. Instead of an URA finale ending, you'll get to fly to the US and participate in one of the BC races.
- Scenario link: Espoir City (Pioneer of the Sands (Pioneer)), Loves Only You (Floating with the Tide (No Stagnation)), Red Desire (Burning Soul (Fighting Spirit)), Forever Young (Unprecedented Prodigy (Peerless)), Marche Lorraine (Sandstorm Slash (Dirt Corners)), Casino Drive (See Ya Later! (Playtime's Over!))
- Scenario skills: Lightning Blitz, Lightning Slash, Lightning Flash, Cyclone Slash, Cyclone Flash, Wind Rider, Photon Flash, Flash, Exquisite Timing, World Captivating Brilliance (In Body and Mind), Aiming for Stardom! (In the Right Place), Hype☆Roadmap (Pathfinder), Journey to a New Dream (Uncharted Heights), Turn the Tables! (Innovation)
- Scenario spark: Dreams Scenario (SPD/GUTS)

| Support Card | Date | Style/Distance | LB Breakpoints | Notable Bonuses | Notable Hints | Pull? | Notes |
|---|---|---|---|---|---|---|---|
| Casino Drive | Early May '29 *(est.)* | **All-rounder** | 0LB+ | Power Bonus +1 and Skill<br>Point Bonus +1 when bond is 60+<br>Mood Effect (20-30%)<br>Training Eff. (1-10%)<br>Failure Protection (10-15%)<br>Energy Reduction (15-25%)<br>Initial Skill Points (30-45) | Slipstream<br>Uma Stan<br>Homestretch Haste<br>**In The Right Place!** | **80 Free Pulls**<br>Yes *(est.)* | Scenario tax banner Overall a very solid pal card Usable from 0LB, but you'd probably want to push to 3LB for the training effectiveness to hit Lovely bob cut |
| Forever Young | Early May '29 *(est.)* | **All-rounder (Dirt+)** | 0LB+ | Training Eff. (5%) and Hint Lv. +1<br>when bond is 80+<br>Training Eff. (1-10%)<br>Friendship Bonus (28-40%)<br>Mood Effect (20-30%)<br>Race Bonus (5-10%)<br>Specialty Priority (60-100)<br>Wit Friendship Recovery (3-5)<br>Wit Bonus +1~3<br>Skill Point Bonus +1~2<br>Initial Skill Points (30-40) | Straightaway Adept<br>Ramp Up<br>Playtime's Over!<br>Rapid<br>Peerless<br>Intrigued<br>Putting All On The Line<br>Nimble Navigator<br>Groundwork<br>With Light In My Heart<br>One More Push<br>Vitality<br>Pioneer<br>**Call & Response<br>Innovation<br>Tail Nine<br>Uncharted Heights** | **80 Free Pulls**<br>With<br>Casino Drive *(est.)* | See the hint list? Yeah... Scenario tax card, an absolute groundbreaker from John Umamusume II Absolutely puts all other wit cards on a tier directly below, barely anything comes close to this card during Beyond Dreams Scales hard pushing MLB so you might want to take it there |
| Victoire Pisa (Event) | Early May '29 *(est.)* | Medium<br>Long | MLB | Speed Bonus +1 and Skill Point<br>Bonus +1 when bond is 80+<br>Training Eff. (5%)<br>Friendship Bonus (35%)<br>Speed Bonus +1<br>Specialty Priority (65) | Uma Stan<br>Homestretch Haste<br>Mid Race Adept<br>Intrigued<br>Ignition<br>Find A Way!<br>Trekker<br>Corner Recovery<br>**Pathfinder** | Free | At least has +2 speed bonus |
| Marche Lorraine | Late May '29 *(est.)* | **Dirt** | 0LB+ | Friendship Bonus (10%) and<br>Power Bonus +1 when<br>bond is 80+<br>Friendship Bonus (25-50%)<br>Mood Effect (40-50%)<br>Training Eff. (10-20%)<br>Specialty Priority (50-80)<br>Skill Point Bonus +1 | Dirt Straightaways<br>Dirt Corners<br>Intrigued<br>Top Pick<br>Promising Omen<br>Dust Bath<br>Contradicting Emotions<br>Sand Stride<br>Diligence<br>Vitality<br>Thunderous Footfall<br>Forward, March!<br>Belligerent<br>**Sum of Small Efforts<br>Leisurely Dust Bath** | If Whale++ | Very good speed card for dirts, but probably not worth picking up after the anniversary unless you're a whale and can spare the carats Marginal increase from 0LB to MLB compared to others like Forever Young |
| Curren Bouquetd'Or (Event) | Early Jun '29 *(est.)* | Pace | MLB | Training Eff. (10%) when<br>bond is 80+<br>Friendship Bonus (20%)<br>Mood Effect (20%)<br>Specialty Priority (50)<br>Stamina Bonus +1<br>Skill Point Bonus +1 | Attack Stance<br>Time to Awaken<br>Tactical Tweak<br>Surpassing Ambitions<br>To Greater Heights<br>Steady Effort<br>Stamina to Spare<br>**Bravery Slash** | Free | She's pretty ! |
| Daring Heart | Early Jun '29 *(est.)* | **Mile**<br>Medium<br>(Front/Pace+) | 0LB+ | Training Eff. (10%) when<br>there are 4 different card types<br>Friendship Bonus (25-35%)<br>Mood Bonus (20%)<br>Training Effectiveness (5%)<br>Specialty Priority (10-80)<br>Race Bonus (5-10%)<br>Speed Bonus +1<br>Power Bonus +1<br>Guts Bonus +1<br>Skill Point Bonus +1~2 | Playtime's Over!<br>Early Race Adept<br>An Honest Step<br>With Feelings Aboard<br>Aggressive<br>Rushing in Blind<br>Unshakeable Faith<br>Carefree Step<br>Graceful Step<br>Refined Conduct<br>With a Light in My Heart<br>Perfect Sync<br>**Ascendance<br>Pure Perfection** | If Whale<br>or<br>with<br>Daring Tact | Very strong guts card for fronts and paces (moreso the latter), slightly better than Stay Gold stat-wise at MLB Strong even at 0LB anyways, so invest in it if you can 2 Skill Point Bonus unlocks at MLB, though |
| Daring Tact | Early Jun '29 *(est.)* | **Mile**<br>Medium<br>(Late/End+) | 0LB+ | Speed Bonus +1 and Skill Point<br>Bonus +1 when bond is 80+<br>Training Eff. (6-20%)<br>Friendship Bonus (25-30%)<br>Mood Effect (20%)<br>Specialty Priority (50-80)<br>Speed Bonus +1<br>Guts Bonus +1<br>Skill Point Bonus +1 | Uma Stan<br>Downhill Adept<br>Forward Step by Step<br>High Pitch<br>Boiling Emotions<br>Foothold<br>Tumbling Forward<br>Bare Passion<br>Graceful Step<br>Belligerent<br>With a Light in My Heart<br>Perfect Sync<br>**Killer Instinct<br>Soul Ablaze** | If Whale<br>or<br>with<br>Daring Heart | Like...grandmother, like granddaughter (except it's for backliners) Similarly to Daring Heart, she's slightly above Stay Gold in stats, at MLB, with hints focused on lates and end closers and a very solid pick at 0LB either way. No 2 Skill Point Bonus might put her behind in the future, maybe |
| Aston Machan | Late Jun '29 *(est.)* | **Sprint**<br>(Front/Pace+) | 0LB+ | Training Eff. (10%) when<br>bond is 80+<br>Friendship Bonus (25-35%)<br>Mood Effect (20%)<br>Training Eff. (1-10%)<br>Specialty Priority (10-100)<br>Race Bonus (5-10%)<br>Speed Bonus +1<br>Guts Bonus +1~2<br>Skill Point Bonus +1~2 | Sprint Corners<br>Sprint Straightaways<br>Unyielding Step<br>Flying Sparks<br>Dodging Danger<br>Committed Push<br>Light as a Feather<br>Explosive Force<br>Bouncy Step<br>Fierce Push<br>Swift Takeoff<br>Sprinting Gear<br>Light as a Feather<br>**Masterful Steering<br>Overwhelm** | If Whale+ | If we got two mile guts cards last time, surely the next will b- Sprint guts card! Front and pace exclusive, very strong at her job, but sprints are scarce so this might be better to have on your borrow slot, especially considering both her Guts and Skill Point Bonus +2 are locked behind MLB |
| Agnes Tachyon (Event) | Early Jul '29 *(est.)* | Pace | MLB | Speed Bonus +1 and Skill Point<br>Bonus +1 when bond is 80+<br>Friendship Bonus (25%)<br>Mood Effect (50%)<br>Guts Bonus +1<br>Specialty Priority (35) | Pace Chaser Corners<br>Mid Race Adept<br>Ambitions<br>Leap Premonition<br>Ride the Momentum<br>Shrewd Step<br>Tactical Tweak<br>Preferred Position<br>**Speed Star** | Free | It's a free card, alright...cut her some slack (No Training Effectiveness is very noticeable in cards at this point) |
| Tap Dance City | Early Jul '29 *(est.)* | **Front**<br>(Medium+) | 0LB+ | Power Bonus +1 and Hint Lv. +1<br>when bond is 80+<br>Friendship Bonus (25-40%)<br>Mood Effect (20-30%)<br>Training Eff. (10-20%)<br>Race Bonus (5-10%)<br>Specialty Priority (42-120)<br>Skill Point Bonus +1~2 | Front Runner Straightaways<br>Front Runner Corners<br>Early Race Adept<br>An Honest Step<br>Frantic State<br>Fast-Paced<br>Building Momentum<br>Dodging Danger<br>Running is Winning!<br>Overflowing Fighting Spirit<br>Early Bird<br>Pulling Away<br>**Concentration<br>Top Runner<br>Cloud-Riding Dragon** | If dedicated<br>to Fronts | Fronts might escape the LoH meta for a bit...or at least try to, this card is a great push in that direction. Personally lacks a bit of speed bonus but this should be miles above Smart Falcon's level |
| Agnes Digital | Early Jul '29 *(est.)* | **Late** | 0LB+ | Unique<br>Training Eff. (10-20%)<br>Friendship Bonus (25-30%)<br>Mood Effect (40-60%)<br>Specialty Priority (50-80)<br>Power Bonus +1<br>Skill Point Bonus +1~2 | Late Surger Corners<br>Late Surger Straightaways<br>Forward Step by Step<br>1,500,000 CC<br>On the Move<br>Pushing Through!<br>Be Ambitious<br>Slick Surge<br>Tooth and Tail<br>No Stagnation<br>Grand Fight<br>Go With the Flow<br>**Keep Going!<br>Mighty Warrior** | If dedicated<br>to Lates | An absolute must have for late surgers moving forward. About the same power level as Neo Universe and Fine Motion, but with hints fully dedicated to the late playstyle If there's anything to point out from the kit, is that her unique is kinda wonky and outdated for this time and age. But she's also very strong even at 0LB |
| Sakura Chiyono O | Late Jul '29 *(est.)* | **Pace**<br>Medium | 0LB+ | Guts Bonus +1 and Training Eff.<br>(5%) when bond is 80+<br>Training Eff. (6-20%)<br>Friendship Bonus (25-30%)<br>Mood Effect (20-30%)<br>Specialty Priority (50-65)<br>Guts Bonus +1<br>Skill Point Bonus +1~2 | Brute Force<br>Ride the Momentum<br>Honest Run<br>Satisfying Pace<br>To Greater Heights<br>Surpassing Ambitions<br>Up-Tempo<br>Fighting Spirit<br>Ignition<br>Unshakeable Faith<br>Carefree Step<br>Refined Conduct<br>Stamina to Spare<br>**Proof of Strength<br>Persistence Is Power** | If Whale+<br>and<br>If dedicated<br>to Paces | Very very good card for paces that can dish out great stamina and guts clicks, especially for mediums, but not at all necessary and more of a luxury |
| Blast Onepiece (Event) | Early Aug '29 *(est.)* | Pace<br>Late | MLB | Training Eff. (10%) when<br>bond is 80+<br>Friendship Bonus (30%)<br>Mood Effect (30%)<br>Specialty Priority (50) | Long Straightaways<br>Corner Adept<br>Mid Race Adept<br>Razor-Sharp Stride<br>Be Ambitious<br>No Stagnation<br>Rising Passion<br>Preferred Position<br>**Hot Pursuit** | Free | This card...is actually not that far off from Super Creek in terms of stat output, it's definitely better than most of the other free cards they have been releasing |
| Gran Alegria | Early Aug '29 *(est.)* | **Mile** | 0LB+ | Power Bonus +1 and Training Eff.<br>(5%) when bond is 80+<br>Training Eff. (10-20%)<br>Friendship Bonus (20-25%)<br>Mood Effect (10-40%)<br>Race Bonus (5-10%)<br>Specialty Priority (50-80)<br>Power Bonus +1<br>Skill Point Bonus +1~2 | Mile Corners<br>Mile Straightaways<br>Unyielding Spirit<br>Pumped<br>Boiling Emotions<br>Step Up<br>Lively<br>Footloose<br>I'll Go My Way!<br>Pounding Chest<br>Electrifying Run<br>Mighty Leap<br>**Carefree Stride<br>Energetic and Lively** | If Whale+<br>or<br>With<br>Satono Diamond | A strong mile card, but a luxury at that. With this card release, you can basically build an exclusive mile deck Excellent for backliners, and paces to some extent |
| Satono Diamond | Early Aug '29 *(est.)* | **Long**<br>(Late+) | 0LB+ | Power Bonus +2 when<br>bond is 80+<br>Training Eff. (1-20%)<br>Friendship Bonus (25-35%)<br>Mood Effect (20-30%)<br>Race Bonus (5-<br>Specialty Priority (60-<br>Skill Point Bonus +1~2 | Long Corners<br>Long Straightaways<br>Inside Scoop<br>Lock On<br>Fierce Struggle<br>Unwavering Heart<br>Shining Brightly<br>High Ambitions<br>Crucial Stage<br>Straightaway Recovery<br>Fuse<br>Long Recovery<br>**Chain Reaction<br>With All My Might<br>Brilliant and Dazzling** | If Whale | A speed card with a recovery! In this economy! The newest scenario is around the corner and it starts with the feared 3600m CM. This might be a must, after all. Stat-wise it's very strong but needs a bit of LBs to scale (3LB -> MLB jump is insane) |


### 3.7 Links

Resources the author recommends.

**General info**

| Resource | Link |
|---|---|
| Umamusume bible (Gametora) | https://gametora.com/umamusume |
| Uma.moe's timeline | https://uma.moe/timeline |
| Global reference document | https://docs.google.com/document/d/11X2P7pLuh-k9E7PhRiD20nDX22rNWtCpC1S4IMx_8pQ/preview?tab=t.0 |

**Tools**

| Resource | Link |
|---|---|
| VF Umalator | https://kachi-dev.github.io/uma-tools/umalator-global/ |
| Henry Handsome's carat calculator | https://docs.google.com/spreadsheets/d/1ezTaKNCe5_NCPW6vv21Y6B3T4-zz5C2OOHibjQhWhCU/edit?gid=607505096 |
| Card scoring | https://docs.google.com/spreadsheets/d/17nbTcHUPqq8O6h_4Z6cVXwfkgEbpgO1VHzdLf-3YSfw/edit?gid=1776774504 |
| dylank's skill spreadsheet | https://docs.google.com/spreadsheets/d/1oB3eTvKqREtJDWJL0q80O_VjBcpOmRl5xE0z5fZKgFY/edit?gid=2142834421 |
| Umamusume Tier List (Global) | https://euophrys.github.io/uma-tiers/ |

**Gacha info**

| Resource | Link |
|---|---|
| celery's card evaluation document | https://docs.google.com/document/d/1iUV8pAc5-eXePJJA8hhgeJA6KjuCczjf68ZxdzYY4tM/edit?tab=t.0 |
| Banner recommendations | https://docs.google.com/spreadsheets/d/1JFrjSvG2Ld9zDk78zH0fqlK1GZzAsj8WRoP0AWeqBLI/edit?gid=0 |
| Future releases | https://docs.google.com/spreadsheets/d/14-b9KYeXCE-o43LZ_X8-pRqRo_Mnn_9_meAj3Bo6QOo/edit?gid=1772302825 |

**Guides**

| Resource | Link |
|---|---|
| Crazyfellow's parenting guide | https://docs.google.com/document/d/1Q3IJKbtkplmuY-PAJMNjYiLtasv0eU0aIBEqp8_C3tg/edit?tab=t.0 |
| celery's GM guide | https://docs.google.com/document/d/1fWc31yOOD-3SMJQQ-Mjsj1S9M9iaZoQVvy5OGJw6en4/edit?tab=t.0 |
| celery's L'Arc guide | https://docs.google.com/document/d/19mJAzyljQrfTQz468yIY_1jIfhYdMTGCtFTLe-AKTvc/edit?tab=t.0 |
| celery's UAF guide | https://docs.google.com/document/d/1s4fKD7aLnZ0Y7toxAjmsuIjfYr0RAhmKF0ndYsCXebM/ |
| celery's GFF guide | https://docs.google.com/document/d/1hBjeQ6J9SQVIOm5sfysy_G2L4ZNRC_ng_-aPZxFLlXg |
| celery's MEKA guide | https://docs.google.com/document/d/1pOYzeqdeFJsDJT_HmXtfB7_S-I6D7AY_GYidXUNZsTI |
| celery's TL guide | https://docs.google.com/document/d/1v9w4Tr48Xh5mXWHSLGGUU_XEYY148t7wqPd9120QjBU |
| celery's DYI guide | https://docs.google.com/document/d/1kmCbUtdQap3YtXnnGRrdk-_Di3pXaATnJBrPACPQcAc |
| celery's YHS guide | https://docs.google.com/document/d/1Ud4JO6zlU9R1n9YjP13ORdWmFRab0o5_NLHIi5c_imY |
| Han's BD guide | https://docs.google.com/document/d/1ibD_nSFr923JtCxRS7GJikwY9csnMBkfRzsLnew5jvg/edit?tab=t.0 |
| SizzledStar's BD guide | https://docs.google.com/document/d/1pTtEtdN0TT7SEsYXp-FML7731NWsYWWf0ieJ7BVnSJk/edit?tab=t.0 |


### 3.8 Changelog

| Month | Changes |
|---|---|
| January 2026 | Sheets creation. Added every card's info up until Project L'Arc scenario. Added disclaimers and Links sheet. |
| February 2026 | Updated the sheets to include every card until Yukoma Hot Springs scenario. Added new scenario-related evolved skills. Added Read Me sheet. Adjusted release dates for some cards based on global schedule. |
| March 2026 | Updated Make A New Track into Trackblazer following Global's rename. Revised some cards. Adjusted some free pulls. Added March's updated global schedule. |
| April 2026 | Added April's updated global schedule. |
| May 2026 | Added May's updated global schedule. Revised some cards. |
| June 2026 | Added June's updated global schedule. Adjusted release dates beyond Great Food Festival Scenario. Added the cards released during Beyond Dream scenario. Updated Links to include newer scenario guides. Added a TBA for Welcome to Tracen-ken scenario. Created the Changelog sheet. |


---

## 4. Quick Cross-Guide Workflow

The three references fit together in this order.

| Stage | Question | Where to look |
|---|---|---|
| 1. Pick your scenario | Which training scenario am I running? | Section 3.2 and 3.6 |
| 2. Build your team | Which support cards suit this scenario and my style? | Section 3.6 (scenario tables) |
| 3. Plan your lineage | How likely are the sparks I want to trigger? | Section 2 |
| 4. Spend your SP | Which skills are worth buying for my distance and style? | Section 1.6 and 1.7 |


---

## 5. Sources and Credits

| Guide section | Original work | Author |
|---|---|---|
| Skills | Uma Musume Skills Spreadsheet | @dylank0 (info), @sayaduck (formatting) |
| Spark Procs | Uma Musume: Spark Procs | @icedynamix (with sources from @BourBon_Polaris, Crazyfellow and u-tools) |
| Support cards | Luh's Support Card Encyclopedia | Luh (@luhsu on Discord) |

This guide is a reformatted, text-only compilation. Please support the original authors and check their sheets for the latest updates, since game data changes often.

---

## 6. What Was Left Out

| Workbook | Tabs not included | Why |
|---|---|---|
| Skills Spreadsheet | Acceleration Skills (old), Other Skills (old), Debuff Skills (old), Green Skills (old), Speed Skills (old), Stamina Recovery Skills (old) | Older versions replaced by the current category tabs. |
| Skills Spreadsheet | alldata | Raw backing table that feeds the tier lists. |
| Spark Procs | Complete Distribution Table | About 2,100 rows by 40 columns of lookup values (see section 2.10). |
| Spark Procs | _base_chances, _affinity, _affinity_counts, _dv, _races, _chars, _relations, _relation_members, _skills | Hidden helper tables used by the calculators. |
| Support cards | Card art and column images | The guide is text only. |

If you want any of these added (for example the old skill tabs as an appendix), say so and they can be appended.
