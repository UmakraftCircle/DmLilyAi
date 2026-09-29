# Race Mechanics Handbook (detailed fact reference)

**Source:** https://gametora.com/umamusume/race-mechanics
**Authors:** robflop and Gertas, published on GameTora (created 2023-12-26)
**Note:** This is an original, fact-focused reference written from that handbook for LilyAi to read. It is reorganized and reworded, not a copy. Full credit belongs to the original authors and GameTora. Game materials are copyright Cygames, Inc.
**Deeper numbers:** The handbook points to KuromiAK's Race Mechanics document for raw formulas: https://docs.google.com/document/d/15VzW9W2tXBBTibBRbZ8IVpW6HaMX8H0RP03kq6Az7Xg
**Time sensitivity:** Several mechanics were added to the Japanese server at dated anniversaries and reached Global later. Those dates are listed in section 12. Some values (for example how the pacemaker is chosen) changed after the JP 1.5-year anniversary and are described in the source as not well understood.

---

## 1. Terminology to keep straight

- The **Last Spurt phase** (the final sixth of a race) and the **last spurt mechanic** (the speed boost for the final push) are two different things that share a name.
- **Target Speed** is the speed a horsegirl is trending toward. **Current Speed** is the speed she is running at right now.
- **HP** (also called effective stamina) is what the Stamina stat converts into during a race.

## 2. Stats and what they do

General rules:
- Each of the five base stats ranges from **1 to 2000**.
- In calculations, any value **above 1200 counts at half**. Example: 1500 counts as 1350 (1200 plus half of 300).
- **Mood** changes the stat values used in mechanics by **2% per mood level**. Normal (yellow) mood leaves them unchanged.
- During a Career run, all stats get a temporary flat **+400**.

| Stat | What it affects |
|------|-----------------|
| Speed | Target Speed in the Late-Race and Last Spurt phases, and the extra Target Speed from the last spurt mechanic. It does **not** affect earlier phases. Can be lowered by terrain type and condition and raised by course stat thresholds. |
| Power | The height of acceleration reachable at any point, and lane-changing ability. Also feeds Stamina Contest, Repositioning, Power Conservation and Release. Reduces Target Speed lost on uphills (more Power means less loss). Lowered by terrain type and condition. |
| Stamina | Maximum HP, calculated once at race start. Also affects how much Target Speed Stamina Contest can add and how long and fast the last spurt is. |
| Guts | The strength and duration of last spurt bonuses, Spot Struggle, Dueling, Repositioning and Securing the Lead. Also lowers stamina consumption in the Late-Race and Last Spurt phases. |
| Wit | Skill activation chance, rushing probability, and the chance of Target Speed gain and stamina savings on downhills. Also influences entry into some Position Keep modes. It does **not** affect Late Starts, despite popular belief. |

### Stamina and HP details
- HP is mostly spent by running, but other mechanics can spend or restore it.
- Strategies convert Stamina to HP with different efficiency. Late Surgers and End Closers convert best and Pace Chasers worst, a spread of **11%** between the extremes.
- Recovery skills restore a **percentage of max HP** (for example a value of 0.055 means 5.5%). So recovery is worth more the higher your max HP, and longer races give higher recovery.
- Terrain type and condition can change HP consumption.

### Wit and aptitude
- The effectiveness of Wit in mechanics is scaled by the character's aptitude for her running strategy: **S = +10%, A = unchanged**, and lower ranks reduce it (for example **D = -40%**, **G = -90%**).
- Aptitude sparks and skill-based aptitude increases do **not** change skill activation chance.

## 3. Race phases

Every race has four phases regardless of length, numbered 0 to 3 in skill conditions:

| Phase | Japanese | Span |
|-------|----------|------|
| Early-Race | 序盤 | 1st sixth |
| Mid-Race | 中盤 | 2nd to 4th sixths |
| Late-Race | 終盤 | 5th sixth |
| Last Spurt | ラストスパート | 6th sixth |

The Last Spurt phase can be treated as part of the Late-Race except for skills that trigger only during it.

In-game: ticks on the top progress bar mark the start of Mid-Race (first tick) and Late-Race (second tick). The bar disappears around the start of the Last Spurt phase. On the race course charts (https://gametora.com/umamusume/racetracks) the phases are colored yellow, purple, cyan and red, and the start of the last spurt mechanic is a cyan "Fast Forward" icon.

Worked examples:

| Race | Early | Mid | Late | Last Spurt |
|------|-------|-----|------|------------|
| 2400m (one sixth = 400m) | 0 to 400m | 400 to 1600m | 1600 to 2000m | 2000 to 2400m |
| 1000m (one sixth about 167m) | 0 to 167m | 167 to 667m | 667 to 833m | 833 to 1000m |

## 4. Terrain, condition and course thresholds

- Terrain types: **turf (芝)** and **dirt (ダート)**.
- Conditions: **firm (良), good (稍重), soft (重), heavy (不良)**.

| Effect | Rule |
|--------|------|
| Heavy condition | Speed stat -50 |
| Turf, any condition except firm | Power -50 |
| Dirt, any condition except good | Power -100 |
| Dirt, good condition | Power -50 |
| Soft or heavy condition | HP consumption +2% per second |

- **Course stat thresholds:** some courses have thresholds. Exceeding a threshold stat raises the Speed stat by **5% per multiple of 300**, capped at **+20% at 900** over the threshold. Not every course has them. Details are on the racetrack pages.

## 5. Distance units

- One **horse length (バ身, bashin)** in this game is about **2.5 m** (the real-world term is usually 2.4 m). Half lengths appear as 1/2.
- **Long Shot (大差)** means a gap over 10 lengths.
- Result-screen margins: Nose (ハナ) about 20 cm, Head (アタマ) about 40 cm, Neck (くび) about 80 cm. These are flavor and generally do not matter mechanically.
- Underlying calculations use meters per second. Horse lengths are mostly cosmetic.

## 6. Speed, acceleration and how skills interact with them

### Target Speed vs Current Speed
- If Current Speed is below Target Speed, the girl accelerates. If above, she decelerates.
- Target Speed depends on skills, race length, strategy and phase. The Speed stat and distance aptitude matter for Target Speed only in the Late-Race and Last Spurt.
- Raising Target Speed does **not** instantly raise Current Speed. It only raises the cap she can accelerate up to. If acceleration is too slow to reach the new cap within the buff duration, the buff is partly or fully wasted. When the skill ends she decelerates back down.
- **Current Speed buffs** apply instantly for the full duration (no acceleration needed) but cause deceleration afterward. **Current Speed debuffs** are immediate and involve neither acceleration nor deceleration.
- The source says no Target Speed debuffs exist at the moment. They would look like an inverted buff.
- **Carry over:** a speed skill activating late in the Mid-Race with enough duration to last into the last spurt makes the spurt start at a higher Target Speed.
- **Blocking:** girls in front can cap the runner behind at roughly their speed. This is especially harmful to late-starting Front Runners and to backline (Late Surger or End Closer) girls trying to pass during the spurt.

### Baseline speeds (no modifiers)

| Moment | Speed |
|--------|-------|
| Race start | 3 m/s (about 11 km/h) |
| Start Dash, at the very start of Early-Race | 17 m/s (about 61 km/h) |
| Rest of Early-Race and Mid-Race | 20 m/s (about 72 km/h) |
| Last spurt mechanic | 25 m/s (about 90 km/h) |

Strategy shifts these only slightly. Example of scale: a skill adding 0.45 m/s in the Mid-Race is +2.25% over 20 m/s.

### Acceleration
- Acceleration is the rate of speed increase (for example 0.5 m/s squared gains 2 m/s in 4 seconds). Deceleration is the reverse.
- It depends on the Power stat, strategy, race phase, uphill running, and terrain and distance aptitude. Better stats and aptitudes give better acceleration, and uphill gives less.
- The community belief that acceleration only matters in the last spurt is a slight oversimplification. Horsegirls accelerate all race, but the Target Speed jump from Mid-Race to the last spurt is where extra acceleration matters most.
- **Worked example from the source:** Mid-Race Target Speed 20 m/s rises to 25 m/s at the spurt start. With A aptitudes and 1200 Power, base acceleration is about 0.46 m/s squared, taking about **11 seconds** to reach the new top speed. A skill adding between 0.2 and 0.66 m/s squared cuts that to about **7.5 seconds**, gaining about **8.75 m (3.5 lengths)** over a runner without it. For small boosts (for example 20 to 20.35 m/s from a gold skill in the Mid-Race), extra acceleration barely matters.
- Acceleration also helps Front Runners reach their target speed quickly at the start to claim the front.

## 7. Start delay and late starts (出遅れ)

- Each girl rolls a random start delay of **up to 0.1 seconds**. Wit does **not** affect it.
- Some skills change the roll: certain skills add a fixed value (guaranteeing a late start), some multiply it by a factor below 1 (making late starts less likely), and purple (debuff) skills multiply by a factor above 1 (making them more likely).
- Thresholds:

| Delay | Effect |
|-------|--------|
| Below 0.02 s | Grants the Strong Start bonus in Team Trials scoring (https://gametora.com/umamusume/team-trials-pvp-scoring#strong-start), otherwise irrelevant |
| 0.066 s or more | Counts as a **Late Start**: loses the acceleration normally gained at the start of Early-Race |
| 0.08 s or more | Also shows the on-screen "Late Start" indicator |

- Late starts hurt frontline strategies most, since they often cannot regain their intended position in time.

## 8. Last spurt mechanic

- Happens in the final stretch: the girl raises Target Speed for a final push. The boost depends on Speed, Guts and distance aptitude. Acceleration skills are especially valuable here.
- On entering the Late-Race, if she has enough HP to run the rest of the race at the boosted speed, she starts the spurt immediately with the full bonus.
- Otherwise one of three things happens: the bonus is reduced until the condition is met, the start is delayed, or both. In the worst case there is no spurt and no bonus.

## 9. Position Keep and modes

**Position Keep** runs from the race start until roughly the middle of the Mid-Race. Each girl has one of 6 modes. After it ends, modes no longer apply. On course charts the end is marked by a purple "Pause/Resume" icon. The game gives no in-race indicator apart from changed behavior.

| Mode | Available to |
|------|--------------|
| Normal | All strategies |
| Pace Up Ex | All strategies |
| Speed Up, Overtake | Front Runners (including Runaways) only |
| Pace Up, Pace Down | Pace Chasers, Late Surgers and End Closers only |

**Pacemaker:** before the JP 1.5-year anniversary it meant the highest-placed girl of the most forward strategy present (for example the top Front Runner, or the top Pace Chaser if there are no Front Runners). The logic changed afterward and is not well understood.

### Shared behavior
- From normal mode, a girl checks every **2 seconds** whether to switch modes.
- A non-normal mode ends when its exit condition is met or its max distance is reached. Max distance is **1/24 of the race length** (**3/24** for Runaway).
- **Pace Up Ex** was added at the JP second anniversary (2023-02-24) and takes priority over strategy modes. Front Runners enter it if a Pace Chaser, Late Surger or End Closer is ahead of them. Non-Front Runners enter it if the pacemaker's strategy should be behind them but is not. While active, Target Speed is raised to its maximum.

### Front Runner modes
- **Speed Up:** entered when leading without enough gap to second place, plus a Wit check. "Not enough" means less than **4.5 m** (Front Runner), **12.5 m** (Front Runner with no other Front Runner in the race) or **17.5 m** (Runaway).
- **Overtake:** entered when not first among girls with the same strategy (Front Runner or Runaway), plus a Wit check.
- Both end when the desired position is reached or on timeout.

### Non-Front Runner modes
- They try to stay within a minimum and maximum distance of the pacemaker, depending on race length and strategy (Pace Chasers stay closer than End Closers).
- **Pace Up:** entered when too far behind (past the maximum distance), plus a Wit check. Gives a slight Target Speed buff.
- **Pace Down:** entered when too close (inside the minimum distance). Any active speed-raising skill buff prevents it. Reduces Target Speed. Activating any speed-increasing skill (Target or Current Speed) during Pace Down ends it immediately.

## 10. Rushing (掛かり, kakari)

- Each race has a random chance for a girl to rush. The chance comes from her **Wit** and can be modified by skills (for example a flat 3% reduction from some skills).
- If it triggers, it happens **once**, at a random point between the middle of Early-Race and the middle of Mid-Race, and a "Rush" indicator appears.
- Every **3 seconds** there is a **60%** chance the state ends. It always ends after **12 seconds**. Some debuff skills add extra seconds to that timer per application.
- Effects while rushing:
  - Stamina consumption **x1.6**.
  - All Wit rolls automatically succeed.
  - Position Keep behavior changes temporarily.
- Behavior substitutions: Front Runners go into Speed Up mode. Pace Chasers act like Front Runners. Late Surgers act like Front Runners **75%** or Pace Chasers **25%**. End Closers act like Front Runners **70%**, Pace Chasers **20%** or Late Surgers **10%**.
- Budget some spare HP: on average a rush costs about **45 to 180 base Stamina stat** worth of HP, depending on race length.

## 11. Position and stamina mechanics added later

### Spot Struggle (位置取り争い)
- Can start from **150 m** after the start until shortly after the Mid-Race begins. Requires two or more Front Runners or Runaways close together: within **3.75 m** (Front Runners) or **5 m** (Runaways). It is always Front Runner-only or Runaway-only, never mixed. An indicator appears.
- Participants gain extra Target Speed (strength and duration depend on Guts) and burn more stamina:

| Situation | Stamina use |
|-----------|-------------|
| Front Runner | x1.4 |
| Runaway | x3.5 |
| Rushing Front Runner | x3.6 |
| Rushing Runaway | x7.7 |

- Ongoing Spot Struggles end slightly before the halfway point of the Mid-Race regardless of remaining duration.

### Dueling (追い比べ)
Conditions, all required:
- Current Speeds within **0.6 m/s** of each other.
- Within **3 m** of each other for longer than **2 seconds**.
- At least **15% HP** left.
- On the **Final Straight**.

Details:
- No time or distance limit beyond the Final Straight's length. A girl whose HP drops below **5%** drops out.
- Participants gain Target Speed and acceleration based on Guts.
- The Final Straight originally meant the straight after the final corner. Since the JP 2.5-year anniversary it means the literal last straight of the course, independent of corners. On a one-straight course, that straight is the Final Straight.

### Power Conservation (足を貯める) and Release (脚色十分)
- A girl can conserve power when her Power (base plus mood and skill modifiers) is **above 1200**.
- When her last spurt starts with enough conserved power, she releases it and her acceleration increases. Specifics are mostly unknown per the source.

### Stamina Contest (スタミナ勝負)
Triggers when all are true:
- Stamina (base plus modifiers) is above **1200**.
- The race is longer than **2100 m**.
- She is in the last spurt and has hit her maximum spurt speed.

Effect: last spurt Target Speed rises beyond the normal maximum, scaling with Stamina, Power and race length. It lasts until the finish.

### Repositioning (位置取り調整) and Stamina Conservation (持久力温存)
- Repositioning can occur only between the middle and end of the Mid-Race, in two cases: **Type 1** (large gap to the leader) or **Type 2** (many girls nearby).
- When it triggers she spends extra HP to raise Target Speed and improve position. HP cost depends on race length and strategy. Buff strength depends on Power, Guts, strategy and race length, and for Front Runners is larger with fewer other Front Runners nearby.
- Type 1 chance depends on Wit and on whether the gap counts as large (depends on race length and strategy). Type 2 chance depends on Guts, the number of nearby girls and how many share her strategy.
- It can happen multiple times, but only the first shows an indicator.
- **Stamina Conservation:** if she lacks HP to both reposition and finish at full speed, she rolls a Wit check every 2 seconds. On success, she stops repositioning so the spurt is not compromised. Restoring enough HP with recovery skills ends it.

### Securing the Lead (リード確保)
- Triggers when a girl judges the gap to girls who should be behind her is too small. Natural strategy order matters (Late Surgers behind Pace Chasers behind Front Runners). What counts as insufficient depends on race length and strategy.
- She spends extra stamina to raise Target Speed. Activation chance depends on Wit. Stamina cost depends on race length and strategy. Buff strength depends on Guts, and for Front Runners is larger with fewer Front Runners nearby.
- Can trigger multiple times between the middle and end of the Mid-Race. Only the first shows an indicator.

## 12. When mechanics were added (JP dates from the source)

| Mechanic | JP release | Global release |
|----------|------------|----------------|
| Spot Struggle | 1st anniversary, 2022-02-24 | Half-anniversary, 2025-11-11 |
| Dueling | 1st anniversary, 2022-02-24 | Half-anniversary, 2025-11-11 |
| Pace Up Ex | 2nd anniversary, 2023-02-24 | not stated |
| Power Conservation and Release | 2nd anniversary, 2023-02-24 | not stated |
| Stamina Contest | 2.5-year anniversary, 2023-08-24 | not stated |
| Repositioning and Stamina Conservation | 2.5-year anniversary, 2023-08-24 | not stated |
| Securing the Lead | 2.5-year anniversary, 2023-08-24 | not stated |

## 13. Corner numbering

- Corners are numbered 1 to 4 for skills that trigger on specific corners.
- The **last corner is always 4**. Numbers decrease going backward through the course (second-to-last is 3, and so on). With more than four corners the count **loops back to 4** after 1.
- Example: Sapporo 1000m dirt has only two corners: the last is 4 and the earlier one (near 777 m) is 3, with no corners 1 or 2.
- Example: Sapporo 2600m turf. The last corner (lap 2) is 4, the other lap 2 corner is 3. In lap 1, counting counterclockwise backward: leftmost is 2, bottom is 1, rightmost loops to 4, top is 3.
- For skills with the `corner_random` condition, the trigger point is always picked on the **last possible instance** of that corner number. On the 2600m course there are two corner 3s, but such a skill can only activate on the one in lap 2.

## 14. Gates and gate brackets

- **Gates** are the starting stalls. **Gate brackets** are groups of gates. Up to **8 brackets** and up to **18 gates**.
- Gate skills usually reference brackets, not single gates.
- Brackets **1 to 3** are Inner (内枠). Brackets **6 to 8** are Outer (外枠).
- With 8 or fewer runners, gate N is bracket N.
- With more than 8 runners, extra gates are added in reverse from the last bracket: 9 runners puts the extra gate in bracket 8, 10 runners adds bracket 7 as well. Above 16 runners the process restarts from bracket 8.

---

## Quick numbers reference

| Item | Value |
|------|-------|
| Stat range | 1 to 2000 (values over 1200 count half) |
| Mood effect on stats in mechanics | 2% per level |
| Career run stat bonus | +400 to all stats |
| Phase split | 1/6, 3/6, 1/6, 1/6 |
| Horse length | about 2.5 m |
| Baseline speeds | 3 / 17 / 20 / 25 m/s (start / start dash / early and mid / last spurt) |
| Late Start threshold | 0.066 s (indicator at 0.08 s) |
| Strong Start bonus | delay under 0.02 s (Team Trials only) |
| Heavy terrain | Speed -50 |
| Soft or heavy | +2% HP use per second |
| Course threshold bonus | +5% per 300, max +20% at 900 |
| Rushing stamina use | x1.6 |
| Rushing end checks | every 3 s at 60%, forced end at 12 s |
| Spot Struggle range | 3.75 m (Front Runner), 5 m (Runaway) |
| Dueling | within 0.6 m/s, within 3 m for over 2 s, at least 15% HP, on Final Straight, drop out under 5% HP |
| Power Conservation | Power over 1200 |
| Stamina Contest | Stamina over 1200, race over 2100 m, at max spurt speed |
| Position mode max distance | 1/24 of race (3/24 Runaway) |
| Position mode check interval | every 2 s |
| Strategy HP efficiency spread | 11% (Late Surger and End Closer best, Pace Chaser worst) |

## Related resources

| Resource | URL |
|----------|-----|
| Race Mechanics Handbook (source) | https://gametora.com/umamusume/race-mechanics |
| KuromiAK Race Mechanics document | https://docs.google.com/document/d/15VzW9W2tXBBTibBRbZ8IVpW6HaMX8H0RP03kq6Az7Xg |
| Race course charts | https://gametora.com/umamusume/racetracks |
| Team Trials scoring (Strong Start) | https://gametora.com/umamusume/team-trials-pvp-scoring#strong-start |
| Skill list | https://gametora.com/umamusume/skills |
| Character list | https://gametora.com/umamusume/characters |
| Support card list | https://gametora.com/umamusume/supports |
| Compatibility Calculator | https://gametora.com/umamusume/compatibility |
| Training Event Helper | https://gametora.com/umamusume/training-event-helper |
| Legacies article | https://gametora.com/umamusume/legacies |
| Guide For Absolute Beginners | https://gametora.com/umamusume/beginners-guide |
| Global Quickstart Guide | https://gametora.com/umamusume/guides/global-quickstart-guide |
| New Player FAQ | https://gametora.com/umamusume/guides/new-player-faq |
| Champions Meeting | https://gametora.com/umamusume/events/champions-meeting |

Repo siblings: see the other folders in `LilyAiGameSpace/Umamusume/Guide/` for reworded references to the guides above.

## Images from the source page

Binary files cannot be committed with the current repo tool, so each image is kept as its original URL plus a description. All are hosted by GameTora.

| Topic | Image URL | What it shows |
|-------|-----------|---------------|
| Header | https://media.gametora.com/umamusume/article/race_mechanics/header_race.png | Article header art. |
| Phases | https://media.gametora.com/umamusume/article/race_mechanics/race_progress.png | The in-race progress bar with phase ticks. |
| Course chart | https://media.gametora.com/umamusume/racetrack/simple/en/10005/10501.png | A race course chart with phase colors and the last spurt icon. |
| Speed changes | https://media.gametora.com/umamusume/article/race_mechanics/speed.png | Diagram of Target Speed and Current Speed changes from buffs. |
| Late start | https://media.gametora.com/umamusume/article/race_mechanics/late_start.png | The on-screen Late Start indicator. |
| Rushing | https://media.gametora.com/umamusume/article/race_mechanics/rushing.png | The Rush indicator. |
| Spot Struggle | https://media.gametora.com/umamusume/article/race_mechanics/lead_contest.png | The Spot Struggle indicator. |
| Power release | https://media.gametora.com/umamusume/article/race_mechanics/power_release.png | The power release indicator. |
| Stamina Contest | https://media.gametora.com/umamusume/article/race_mechanics/stamina_contest.png | The Stamina Contest indicator. |
| Repositioning | https://media.gametora.com/umamusume/article/race_mechanics/repositioning.png | The Repositioning indicator. |
| Stamina Conservation | https://media.gametora.com/umamusume/article/race_mechanics/stamina_conservation.png | The Stamina Conservation indicator. |
| Securing the Lead | https://media.gametora.com/umamusume/article/race_mechanics/secure_lead.png | The Securing the Lead indicator. |
| Corners (1000m) | https://media.gametora.com/umamusume/racetrack/simple/en/10001/10106.png | Sapporo 1000m dirt course chart used for corner numbering. |
| Corners (2600m lap 1) | https://media.gametora.com/umamusume/racetrack/simple/en/10001/10105_lap1.png | Sapporo 2600m turf, first lap. |
| Corners (2600m lap 2) | https://media.gametora.com/umamusume/racetrack/simple/en/10001/10105_lap2.png | Sapporo 2600m turf, second lap. |
| Gates | https://media.gametora.com/umamusume/article/race_mechanics/gates_combined.png | Visualization of gates and gate brackets. |
