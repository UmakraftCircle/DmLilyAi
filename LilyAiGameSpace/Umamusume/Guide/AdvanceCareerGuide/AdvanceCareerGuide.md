# Umamusume: Advance Career Guide (Unified Reference)

Merged from 7 source documents on 2026-09-30. Where sources agree they are unified into one statement. Where they disagree, **both values are kept and referenced** (marked ⚖️ and collected in section 16). Nothing here is my own opinion; anything inferred rather than stated is labelled *(inferred)*.

## 0. Sources and how to read this

| Tag | Document | Author | Scope / date | Usage notes |
|---|---|---|---|---|
| **S1** | Umamusume Reference (5th Anniversary) | shory + JP veterans (orig. Erzzy) | JP server, 5th-anniversary edition | Training, PvP, cards, skills |
| **S2** | Uma Musume Race Mechanics | KuromiAK (reverse-engineering credit: @umamusu_reveng, @kak_eng, @hoffe_33, Aya, kakku, Tunnelblick) | Mostly JP; post-1st-anniversary parts are partly speculative | Formulas |
| **S3** | Umamusume Global Reference Document | Erzzy (terms: Kireina) | Global server, changelog to 2025-11-14 | Global numbers and terms |
| **S4** | Luh's support cards encyclopedia | Luh | Google Drive shell | **No usable content** (1 page, navigation bar only). Not used. |
| **S5** | UmaMusu Support Card Evaluation Doc | celery6305 | JP meta, Yukoma Hot Springs parameters, PvP-oriented | Score images did not extract; only the text write-ups are used, so exact scores/orderings are missing |
| **S6** | Crazyfellow's Parenting & Gene guide | Crazyfellow | JP terms; updated through Aug 2026 | Inheritance, compatibility |
| **S7** | URA Fans Farming Guide | Pekoge | URA scenario, Global-style terms (Unity Cup); updated 2025-11-26 | Fan farming |

Tags: **(JP)** = Japanese server, **(GL)** = Global server. Time-sensitive facts have drifted (see 16 and 17): S3 is the oldest on mechanics, S6 the newest.

## 1. TL;DR

1. Support cards decide your account's power; reroll for strong ones when free rolls are on (S1, S3, S5).
2. Stat priority: **enough Stamina to finish > Speed > Power > Wisdom > Guts**. Being ~300 Stamina under the requirement makes Speed nearly worthless (S3, S1).
3. Always train on the newest scenario unless it is distance-locked (S1). Use the scenario's friend/group card (S5).
4. Early game: bond every support card to 80 for rainbow trainings; then rainbows, Wit for energy, races when nothing is good (S1, S3).
5. Hit the 34% Race Bonus breakpoint if you can (S1, S3, S5).
6. Distance aptitude S is the most valuable aptitude; parents' pink factors and G1 overlap (compatibility) drive inheritance (S6, S3).
7. Borrow the best rental parent you can find instead of building junk parents (S1, S3, S6).
8. Skills matter more than small stat differences between top cards (S5, S1).
9. Use the Umalator and a stamina calculator before PvP (S1, S3).

## 2. Terminology map

| Global (S3) | JP / community | Notes |
|---|---|---|
| Front Runner | Runner, Nige, Front | Oonige = Great Escape/Runaway, a Runner subset |
| Pace Chaser | Leader, Senkou, Pace | |
| Late Surger | Betweener, Sashi, Late | |
| End Closer | Chaser, Oikomi, End | |
| Wit | Wisdom, Int, 賢さ, "Wiz" (S2) | |
| Sprint | Short | 1000-1400m |
| Mile | Mile | 1401-1800m |
| Medium | Mid | 1801-2400m |
| Long | Long | 2401-3600m |
| Mood | Motivation, Yaruki | |
| Rushed | Kakari, Panic | |
| Legacy / Guest Legacy | Parent / Rental parent | |
| Sparks | Factors, Genes, 因子 | Blue = stat, Pink/Red = aptitude, Green = unique skill, White = skills/races/scenario |
| Affinity | Compatibility | |
| Team Trials | Stadium | |
| Club / Club Points | Circle / Trainer Medals | |
| Cleats | Horseshoes | |
| Carats | Jewels | |
| Fast Learner | Sharp (切れ者) | -10% skill cost |
| Charming | 愛嬌 | ⚖️ effect worded differently (section 8.5) |
| Slow Metabolism | Overweight | |
| Slacker | Lazy | |
| Night Owl / Insomnia | 夜ふかし気味 | |
| Poor Practice / Practice Perfect | Bad / Good Practice | |
| Unity Cup | Aoharu | scenario name |
| MANT | Trackblazer scenario | |
| Stamina Compete | Stamina Limit Break, スタミナ勝負 | S2/S1 |

Other shorthand (S1): MLB = max limit break (4LB); Ult = unique skill; agemasen = a card fails to give its gold skill; Spark = pity after 200 rolls (JP usage; on Global "sparks" also means inheritance factors, S3).

## 3. Career run basics

**Structure (S1).** A run lasts about 2.5-3 years, one turn per half month. Each free turn: Rest, Infirmary (only when a non-unique negative status exists), Outing/Date, Race, or Train. Races unlock from July of Junior Year. Trainings: Speed, Stamina, Power, Guts, Wisdom (+ a 6th scenario-specific button).

**Energy (S1, S3).**
- Wisdom training normally *recovers* energy; the other four consume it. Energy cost rises +1 at training level 2 and 3, +2 at level 4 and 5 (level-5 Speed example: 25 energy).
- Rest gives 30/50/70 (see 8.5 for odds). Outings are the main energy source in most scenarios. Infirmary (S1) removes one removable negative status and gives 20 energy; if you must use it to survive, restarting is usually better.
- Resting is mostly used in URA only; newer scenarios offer better recovery (S1).

**Bond (S1).** Gauge 0-100; each training with a support card gives +7; hint event +5. 60-79 green, 80-99 orange, 80+ enables **rainbow (friendship) training** when the card sits on its own type of training. (JP) At 60 bond the odds of starting a card's event chain rise greatly (S1). Reporter/Director bond is mostly irrelevant in newer scenarios.

**Training formula (S1, S3 agree).**
`Gain = (Base + ΣStatBonus) × (1 + MotivationMult × ΣMotivationBonus) × ΣTrainingBonus × ΠFriendshipBonus × (1 + 0.05 × NumCards)`
- MotivationMult is 0 at neutral, ±0.1 per mood step. Friendship bonus needs orange bond *and* matching training type. Stat bonus applies only if that training normally gives that stat.
- Motivation Bonus ≈ Training Bonus / 5 in value (S5).

**Two-phase flow (S1, S3).** (1) Bonding phase: pick trainings with the most bond gain while managing energy; Wisdom trainings recover energy; a hint on a card with a relevant skill pool beats an extra participant. (2) After bonds: take rainbows, do Wit when no rainbow, race when nothing is good. Some scenarios let you leave phase 1 early (e.g. Yukoma onsen tickets).

**End goals by scenario era (S1).** URA/Aoharu: hit as many stat caps as possible (Stamina > Speed > Power > Wit) plus enough SP. Post-DYI: squeeze SP; late Classic/Senior training pads and caps stats. In between: maximise scenario mechanics; rainbows give most stats.

**Hidden career bonus (S3, S2).** In training ("single mode"), every uma gets **+400 adjusted stats**. This is why career Stamina requirements are far lower than PvP requirements (S3).

## 4. Stats

### 4.1 Definitions (S2, S1)
- Raw stats: shown on the stat panel. Raw above 1200 counts half toward base stat (1600 raw → 1400 base) (S2, S1). Green skills add full value.
- Base stat = (Raw + Aoharu team rank bonus) × Motivation coefficient: 絶好調 1.04, 好調 1.02, 普通 1.00, 不調 0.98, 絶不調 0.96.
- Adjusted stats: Speed = Base × CourseModifier + Ground; Stamina/Guts = Base; Power = Base + Ground; Wiz = Base × StrategyProficiency. Final = Adjusted + skill modifiers.
- Stat cap: 1-2000 in S2. ⚖️ **(JP)** cap raised to 2500 at the 5th anniversary (S2); **(GL)** still 1200 (S6: uncap mechanics do not apply to Global until the cap goes beyond 1200).
- Ground modifier, speed: Heavy (不良) −50 on turf and dirt, else 0. Power: Turf Firm 0, Good/Soft/Heavy −50; Dirt Firm −100, Good −50, Soft −100, Heavy −100.
- Course modifier: courses with 1-2 threshold stats give Speed × +0.05 (≤300), +0.10 (≤600), +0.15 (≤900), +0.20 (>900), averaged across threshold stats.

### 4.2 What each stat does (S1, S2, S3)
- **Speed:** only affects speed in the last spurt (early/mid target speed ignores it). `MaxSpurt = (BaseTargetSpeed_LateRace + 0.01·BaseSpeed)×1.05 + sqrt(500·Speed)×DistProf×0.002 + (450·Guts)^0.597×0.0001`; the Guts term was added after the 1st anniversary (S2). ⚖️ S3's version omits the Guts term (older).
- **Stamina:** HP = `0.8 × StrategyCoef × Stamina + Distance`. Strategy coef: Front 0.95, Pace 0.89, Late 1.0, End 0.995, Oonige 0.86. Running out of HP drops you to minimum speed.
- **Power:** acceleration `= BaseAccel × sqrt(500·Power) × StrategyPhaseCoef × GroundProf × DistProf`; BaseAccel 0.0006 (0.0004 uphill). Also uphill penalty `|slope%|×200/Power`, lane-change speed, and (JP, >1200 Power) conserved-power release.
- **Guts:** lowers late-race HP use (`1 + 200/sqrt(600·Guts)`: 200→1.577×, 400→1.408×, 600→1.333×); raises minimum speed (`0.85·BaseSpeed + sqrt(200·Guts)·0.001`) and spurt speed; feeds Spot Struggle, Dueling, Compete Before Spurt, Secure Lead.
- **Wit:** skill activation `max(100 − 9000/BaseWiz, 20)%` (300→70%, 400→77.5%, 500→82%, 600→85%, 900→90%, 1200→92.5%), Rushed chance, downhill mode, Pace Up/Speed Up entry, per-section random speed, last-spurt selection. Uses **base** Wit, so strategy aptitude and skills do not change activation chance (S2; S1 notes the same).

### 4.3 Priorities and targets: unified, with server differences
- Order: **enough Stamina > Speed > Power > Wit > Guts** (S1, S3). S1 FAQ: enough STA ≫ SPD > PWR > (max STA on Long) ≫ Wit above 1200 ≫ Guts. S3: Stamina/Guts up to the track's requirement > Speed > Power > Wit.
- **Stamina vs Speed (S3 tests, 1200 Power, 250 Guts, 1000 Wit, no skills):** Sprint 1400m (rec. 500): 1200 Spd/450 Sta loses to 1010/500; 1200/350 loses to 470/500. Mile 1800m (rec. 800): 1200/700 loses to 920/800. Medium 2400m (rec. 900 + gold recovery): 1200/1000 loses to 710/1200. Rule of thumb: ~300 under the requirement makes Speed a decoration; ~100 under makes a point of Stamina worth ~3 Speed. Above the recommendation adds little except insurance against debuffers and Rushed. 100 Stamina removed from an opponent ≈ 300 Speed.
- **Guts targets (S3):** thresholds 210 (Sprint), 260 (Mile/Dirt), 320 (Medium), 380 (Long 3000m), 440 (Long 3600m). Below the threshold a Guts point beats a Stamina point; above it, worse (50 over ≈ 43-46 Stamina). S3 also says ~300 Guts, rarely >400.
- ⚖️ **Wit target:** (GL, S3) aim 300-500; more falls off. (JP, S1) push 1200+; excess raw Wit over 1200 boosts unique/gold/evolved skills (Wiz Limit Break, 4.5). Difference is patch/cap dependent; S3 predates JP's 5th-anniversary cap change.
- **Stamina Limit Break (S2, S1 JP):** Stamina (base + skills) >1200 gives extra target speed after reaching max spurt speed: `sqrt(Stam−1200) × 0.0085 × DistFactor × RandomFactor` m/s. DistFactor: <2101m 0; <2201 0.5; <2401 1.0; <2601 1.5 (1.2 before 2024-10-29); ≥2601 1.8 (1.5 before). Random factor (unclear): table 0 (50%) 0.98-1.00, table 1 (30%) 0.95-0.98, table 2 (20%) 1.00-1.02. Recommendation (S1): max Stamina on 2400m+ even above the requirement.
- **Zenkai Spurt (S2, S1; JP 5th-anniv):** with Speed >2000 and enough HP, continuous extra speed after reaching spurt speed; accel roughly `0.068 × AccelFromPower / (Dist/1000)^1.5 + skills` (still under investigation); running out of HP mid-spurt drops you straight to minimum speed (confirmed bug).

### 4.4 Required Stamina chart (S3, Umalator, GL values)
Assumes 1200 Speed/Power, 600 Wit, Guts 300 (Sprint/Mile) or 400 (Med/Long), no downhills, only heals.

| Distance | Front | Pace | Late | End |
|---|---|---|---|---|
| Short 1400m | 570 | 540 | 500 | 510 |
| Mile 1800m | 800 | 770 | 720 | 740 |
| Mile 1800m + 1 gold | 640 | 600 | 560 | 580 |
| Mid 2400m + 1 gold | 910 | 930 | 870 | 900 |
| Mid 2400m + 2 gold | 710 | 720 | 680 | 700 |
| Long 2600m + 1 gold | 1130 | 1110 | 1030 | 1060 |
| Long 2600m + 2 gold | 900 | 870 | 820 | 850 |
| Long 3200m + 2 gold | 1080 | 1060 | 990 | 1020 |
| Long 3200m + 3 gold | 830 | 800 | 750 | 780 |

Downhills lower the numbers (Hanshin 3000m ≈150 less than Kyoto 3000m); debuffers raise them. Each gold recovery only works with your Wit-based activation chance, so relying on more golds lowers consistency:

| Wit | 300 | 400 | 500 | 600 | 700 | 800 |
|---|---|---|---|---|---|---|
| 1 gold | 70.0% | 77.5% | 82.0% | 85.0% | 87.1% | 88.8% |
| 2 golds (both) | 49.0% | 60.1% | 67.2% | 72.3% | 75.9% | 78.9% |
| 3 golds (all) | 34.4% | 46.5% | 55.1% | 61.4% | 66.1% | 70.0% |
| 2 of 3 golds | 78.4% | 87.1% | 91.4% | 93.9% | 95.4% | 96.5% |

Tools (S1, S3): hoffe's Stamina Calculator, Umalator (`alpha123.github.io/uma-tools/umalator-global/` for GL). Estimates differ by 100-200 between tools; the calculator ignores hills so it can overestimate.

**Career-run checks (S7, URA, includes the +400 hidden bonus):** Tokyo Yushun/Derby needs ~330+ Stamina (else learn at least a white recovery); Tenno Sho (Spring) needs ≥480 Stamina + 1 gold recovery, or 600 Stamina, otherwise run Milers Cup.

## 5. Aptitudes

Surface (row 1) changes **acceleration**; Distance (row 2) changes **speed** (E or lower also hits acceleration); Strategy (row 3) changes **Wit**. A = baseline. S1 and S2 agree.

| Rank | S | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|---|
| Surface | +5% | 0 | −10% | −20% | −30% | −50% | −70% | −90% |
| Distance | +5% | 0 | −10% | −20% | −40% | −60% | −80% | −90% |
| Strategy | +10% | 0 | −15% | −25% | −40% | −60% | −80% | −90% |

- The accel multiplier by distance aptitude is 1.0 for S-D, 0.6 E, 0.5 F, 0.4 G (S2).
- +5% raw converts to about +10.25% Speed/Power (≈+120 at 1200); −10% ≈ −19% (≈−230) (S1).
- S6 (early-2021 data) is consistent; it adds that S strategy helps Runners most because Wit drives Position Keep and lead-fighting.
- (JP, Feb 2026, S6) over-Wit boosts Unique/Gold/Pink skills; inherited uniques are excluded.
- Pink factors raise base aptitude up to 4 times before the run (max A): 1★ total → 1 rank, 4★ → 2, 7★ → 3, 10+★ → 4 (S1). S3 agrees (1 star for the first rank, then +3 stars per rank). **S can only come from mid-run inheritance** (S6).
- Example (S3): Mayano Top Gun (Dirt E, Mile D) needs 10★ for Dirt and 7★ for Mile to reach A; one pink per uma means one aptitude ends at B and is raised in an inspiration event.
- Distance aptitude S is the most valuable (S6, S3); priority for red genes: **Distance > Ground > Strategy** (S6).
- S2: distance categories affect green "core distance" skills; PvP frequencies are in 13.

## 6. Support cards

### 6.1 Passives explained (S1, S3, S5)
- **Friendship Bonus, Training Bonus, Motivation Bonus, <Stat> Bonus, Specialty Rate, Starting Bond** are the main stat-stick passives. Example (Kitasan, MLB, S1): motivation +30% → +26% at max mood; ×1.26 × 1.15 × 1.25 ≈ +81%.
- **Specialty rate** (S1, S3): each training has weight 100, "not appearing" 50 → 100/550 = 18.18% with zero specialty. Card specialty adds to 100; unique specialty multiplies. Kitasan: (100+80)×1.2 = 216 → 216/666 = 32.4% (i.e. "116", not 100). S3 confirms JP community uses this method.
- `<Stat> Bonus` adds +1 to that stat's base gain before all multipliers (Speed bonus on a Speed card helps 3 trainings).
- Other: Initial stat up, Hint Rate Up (each hint = +5 bond), Hint Lv bonus (skill discount), Wisdom Training Recovery Up (extra energy on Wit rainbow, ~4-5 at MLB), **Race Bonus**, Fan Bonus (JP; fan count).
- **Friend-card passives (S1):** Failure Rate Down (35% turns 9% into ~6%), Energy Discount (20% turns 25 into 20), Event Recovery Up, Event Effect Up. Only one friend card can appear on a training, so they do not stack.
- **Gold skill rate ("agemasen")**, same in S1 and S3, by your stat of the card's type: <400 30%; 400+ 60%; 600+ 65%; 700+ 75%; 800+ 80%; 1000+ 90%. (JP, S1) modern cards no longer miss their gold; it now affects event outcomes. S3 (GL) still treats it as a chance for older cards.

### 6.2 Race Bonus (S1, S3, S5)
- Every 10% Race Bonus = +1 stat from G1 races/finals; every 12.5% = +1 from G2/G3. First value divisible by both is 50% (MANT: +5 G1 / +4 G2-G3 ideal at 50%; hammers multiply 1.35 on last three races).
- Other scenarios: +3 all stats after objectives becomes **+4 at 34%** and **+5 at 67%**. URA/Aoharu builds should reach ≥34% (S1). Max per card is 15% (JP), so 90% total (S1).
- S3 table (URA-type run): 0% 351 stats/870 SP; 10% 372/946; 20% 393/1044; 30% 414/1123; 35% 461/1165; 40% 482/1218. The jump is at 34%.
- ⚖️ Importance: S5 (YHS): "not important but ≥34% gives a minor boost", and hitting 34% is worth ~25 card-score points; S7 (URA fans): higher Race Bonus is central. S1: URA/Aoharu should aim for 34%.

### 6.3 Deck building rules (S5, S1)
- Rank of usefulness for raw stat gain (S5): flat stat bonuses (esp. Speed on Speed cards) > Training/Motivation bonus > Friendship bonus > Specialty rate (only the first ~35 matters much) > Race bonus > other. SP bonus is also strong.
- Cards within 20-40 score points are practically equal: choose by **skills**. Hint discounts effectively give skill points (e.g. Ramonu).
- Investment order when short of cards: **Speed → Wisdom → Stamina/Guts** (S1). Speed and Wisdom SSRs work in almost every build (S5).
- Use the scenario's friend/group card and no second friend card unless you have a strong reason (S5).
- S5 evaluates every card as MLB, with 5 fixed strong companions; treat weaker/low-LB results as less accurate. 0LB-1LB SSRs are rarely better than SRs; MLB SRs can beat MLB SSRs. 0 bond or 0 specialty cards are hard to score. Welfare cards are only evaluated from 2LB.
- ⚖️ Scenario simulation: S5 moved in July 2025 to a generalised scenario model, so scenario-specific strengths (e.g. Pasa speed in DYI) are not reflected.

### 6.4 Friend/Group cards by scenario (S5)
| Scenario | Card | Necessity |
|---|---|---|
| URA | none | - |
| Aoharu / Unity Cup | Kashimoto Riko | Not required |
| Grand Live | Light Hello | Necessary |
| Grand Masters | 3 Goddesses | Necessary |
| Project L'Arc | Satake Mei | Necessary |
| U.A.F. Ready Go! | Tsurugi Ryoka | Necessary |
| Great Food Festival | Akikawa Yayoi | Necessary |
| Mecha Umamusume | none ("free") | - |
| Twinkle Legends | 3 Legends | Necessary |
| Design Your Island | Tucker Bryne | Necessary (3LB+) |
| Yukoma Hot Springs | Hoshina Kiyoko | Necessary |
| Breeders' Cup | Casino Drive (S6) | Mandatory |
| Tracen-ken / Ramen | Tazuna (Alt) best, OG Tazuna/OG Light Hello weaker (S6) | Optional but strongly advised |

### 6.5 Card highlights (S5, JP meta; text notes only, scores unavailable)
**Speed:** Tokai Teio (leader; early speed + choice of final-leg or mid accel); Almond Eye (universal; choose 2 of 4 golds); Admire Groove (mid betweener accel + generic betweener gold); Still in Love (SP-heavy; mid-distance gold or betweener/chaser gold; better in practice than its score); Rhein Kraft (mile frontline; High Voltage); Dream Journey (chaser); Narita Brian (leader only; Monster long accel); Smart Falcon (runner opening accel); Vivlos (Hold Your Tail High gold); El Condor Pasa (+1 all stats at 100 bond; Arcline Professor); Jungle Pocket (+3 speed at max bond); Duramente (specialty 120; Never Give Up gold); Sakura Bakushin O (short); **Maruzensky** (best cross-training among speed cards, 5% TB per training level, Top Runner gold, runner staple); Mejiro Palmer (overrated: unique needs 3 recoveries bought early); Marvelous Sunday; Eishin Flash; Kitasan Black (old staple, still good; Arcline Professor); Taiki Shuttle (mile frontline; Ruler of Mile). SR: Tosen Jordan, Agnes Tachyon (leader).

**Stamina:** Fenomeno (long leader), Inari One (long betweener), Gold Ship (long chaser; Imminent Shadow + chaser heal), Air Shakur (universal recovery+speed), Mejiro Ryan (mid betweener), Sounds of Earth (2nd best; gold recovery or speed gold), Curren Bouquetd'or (leader heal), Duramente (chaser), Tanino Gimlet / Dantsu Flame (mid, guts training), Hokko Tarumae (dirt), Ikuno Dictus (huge cross-training but 0 specialty), **Super Creek** (15% TB, 10% RB, Arc Maestro gold recovery), Satono Diamond. Notes: Mejiro McQueen for long PvP, Mejiro Palmer for runner opening accel, Symboli Kris S (long betweener accel), Yaeno Muteki SR.

**Power:** Tamamo Cross (Divine Speed + midleg options), Vodka (mid betweener; also a power-focused variant with a universal gold recovery), Mejiro Ardan (+2 SP; leader/mile-mid frontline), Nishino Flower (up to 30% TB), KS Miracle (short leader accel), Seiun Sky (mid runner), Espoir City / Wonder Acute (dirt), Winning Ticket (betweener), Tsurumaru Tsuyoshi, El Condor Pasa (Killer Tune), Hishi Amazon (gold Straight Shot for chasers), Admire Vega (Daring Attack for chasers). Power as a category "sucks" for scoring but you click it for the stat.

**Guts:** Stay Gold (universal), Fine Motion (niche: 2000m mid frontline), Hishi Amazon (chaser), Orfevre (+1 per card type at 80 bond; Divine Speed), Silence Suzuka (runner), Curren Chan (short frontline; Concentration), Fuji Kiseki / Blast Onepiece (leader), **Haru Urara** (free welfare; stacked bonuses, low starting bond, no good skills), King Halo (short backliners), Tap Dance City (runner), Gold City (+3 guts, mile skills). Symboli Rudolf (Arc Maestro), Ikuno Dictus, KS Miracle, Ines Fujin (old but good), Winning Ticket, Admire Vega (SR 15% RB).

**Wisdom:** Daring Tact (2 betweener golds, +2 SP), Win Variation (long), Symboli Rudolf (universal slipstream gold, Oute), Daring Heart (mile frontline), Mejiro McQueen (+3 int; leader only), Daiwa Scarlet (Top Runner/long accel for runners), Copano Rickey (dirt), Narita Taishin (chaser), Taiki Shuttle (mile frontline), **Manhattan Cafe** (15% TB, 40% MB, 10% RB, +2 int, +1 SP; essential for long betweeners), **Mejiro Ramonu** (35% FB, +2 int, 4% TB per speed skill up to 20%; best mile/mid int), Mihono Bourbon, Nakayama Festa, TM Opera O (long leader; +2 speed), Satono Diamond, Aston Machan (short; Concentration), Fine Motion (old), Nice Nature (Switch-Up Pro gold; 15% RB), Mr. CB (chaser Daring Attack). Int cards should be chosen mainly by skills.

Meta snapshot (S5): 1-2 top cards in all decks / 1 most of the time / 1 always; 34% RB recommended.

### 6.6 Welfare, tickets, shop (S5, S1, S3)
- **Welfare choice item** (monthly story events): pick what you lack. Otherwise int > guts ≫ power. Speed: Special Week, Fine Motion, Tosen Jordan (universal gold recovery). Stamina: Biwa Hayahide (universal recovery for Long; top), Zenno Rob Roy, Twin Turbo (Top Runner). Guts: Urara, Spe (strong enough); Matikanetannhauser (same 0-bond issue), Yukino Bijin (Curve Sommelier), Mejiro Ryan. Wisdom: Daitaku Helios (good), Mihono Bourbon (opening accel for runners). Power: none useful.
- **SSR pick ticket:** best used to get a meta card to high LB; wait after major patches/new scenarios; tickets do not expire.
- **Training-pass shop (JP 3rd anniversary):** Speed: Jungle Pocket, Maruzensky, Kitasan (3LB-MLB), Biko; Stamina: Super Creek; Power: Admire Vega, Vodka, Rice Shower (recovery); Guts: Ines Fujin; Wisdom: TM Opera O, Fine Motion/Mr. CB.
- Level up only the cards you take on runs (S3); do not buy from random shops except clocks (S3).

## 7. Scenarios

- Always run the **newest scenario** for competitive umas unless it is distance-restricted; older scenarios are only worth it for first-clear rewards/missions (S1, S3).
- Scenario list seen in sources (S1, S5, S6): URA, Aoharu/Unity Cup, Grand Live, Grand Masters, L'Arc, U.A.F., Great Food Festival, Run! Mecha Umamusume, Twinkle Legends, Design Your Island (DYI), Yukoma Hot Springs, MANT/Trackblazer, Breeders' Cup, Tracen-ken/Ramen. S1 says no master guide yet exists for Breeders' Cup. Celery6305 master guides exist for YHS, DYI, TL, Mecha, GFF, UAF, L'Arc, GM (linked from S5/S1; contents not in the source PDFs).
- S5: DYI was overbuffed, so card strength matters less there; picking skills matters more. Modern scenarios ramp stat boosts toward the end, so Junior/Classic matter less; Global still lags in these mechanics (S5).
- **Parent farming relevance (S6, as of June 2026):** Still relevant: **Breeders' Cup** (free race schedule, but shortened so ~4 fewer G1s and lower compatibility ceiling; ~5k SP on full auto; partial-manual first year gives ~+500-1000 SP; auto 30-40 min; scenario genes Speed and Guts) and **Tracen-ken/Ramen** (rated 9/5; stable hint mechanic; 6-7k SP; auto 25-40 min; Power and Guts genes very good). Superseded: DYI (needs LB3 Tucker Bryne; up to 35 extra races for hidden factors, but 90% of hidden factors only gave stats) and Yukoma Onsen (6-7k SP on auto, up to 8k manually; needs Hoshino Kiyoko).
- S6 scenario gene stat leanings: URA Speed/Stamina; MANT/GL/GM/L'Arc various; DYI Stamina/Int; Breeders' Cup Speed/Guts; Ramen Power/Guts.
- Race overlap across scenarios (S6): URA/Aoharu/UAF/GFF/Mecha/DYI share URA-style final races; MANT, L'Arc, GL, GM have scenario races that do not help compatibility across scenarios; Twinkle has no extra races. **URA Finals do not count** for compatibility (Cygames FAQ, corrected in S6 on 2025-09-11).

## 8. Running the career

### 8.1 Seasonal events (S1, S3)
- **Summer camp:** early July of Classic and Senior, 4 turns, all trainings Level 5, infirmary disabled, rest cures 1 bad condition. Arrive with full energy/mood; good time to fix Stamina, Guts, Wit.
- **New Year (early Jan):** Classic: +25 to a stat / +20 energy / +20 SP. Senior: +30 energy / +8 all stats / +35 SP. Pick energy or SP by need.
- **Lottery (late Jan, Senior):** tissues (mood down ~10%), single carrot +20 energy (~50%), bundle +20 energy, mood up, +5 all (~30%), curry +30 energy, mood up, +10 all (~10%), onsen ticket (~3%). Do not arrive with full energy.
- **Crane game** (after dates, 25%): once a year from Year 2; success gives mood, energy, hint. Aim the center of upright plushies; right-side plushies more often carry extras.
- **Acupuncturist Anshinzawa** (10% per run): options 1) +20 all / mood up, or −15 all/mood down/insomnia (50%); 2) Straight and Corner Recovery, or −20 energy/mood down (60%); 3) +12 max energy +40 energy, or −20/mood down/bad practice (80%); 4) +20 energy, mood up, Charming, or downside (90%); 5) +10 energy (100%). Early: option 4 (Charming speeds bonding). Late: option 2 or 3 depending on energy.

### 8.2 Fan checkpoints and unique-skill levels (S1, S3 agree)
Year 3: Feb 1H 60,000 fans (Urara/Falcon 40,000); Apr 1H 70,000 (Urara/Falcon 60,000) and President bond at least green in URA; Dec 2H 120,000 (Urara/Falcon 80,000). URA-specific: Nov Year 2, 50,000 fans → Aoi gives 20 Wit, 20 SP, a mostly useless gold skill; end Year 2, 100k fans → +30 SP; end Year 3, 240k fans → +30 SP.

### 8.3 Racing during a run (S3)
- Rewards: G1 +10 to a stat, +45 SP; G2/G3 +8, +35; OP/Pre-OP +5, +35; 2nd-5th reduced, 6th+ reduced again; all scaled by Race Bonus. Winning turf gives a 10% skill hint, dirt 20%.
- Consecutive-race penalties (not applied to mandatory races): 
  - Any energy: mood down 0/0/~60%/100% on races 1/2/3/4+; random stat loss ~40% on the 4th+; Skin Outbreak 0/0/~12%/~33%.
  - No energy: mood down ~20/~33/~95/100%; skin outbreak ~5/~10/~20/~33%.
- Only enter races showing 2 stars (good aptitude); the uma performs poorly otherwise. Win each graded race once for first-time jewels (S3).
- Fan goals in top bar: do optional races or the run fails.
- Failed training outcomes (JP, S1): fail chance 1-19% → worst outcome 0%; 20-79% → ~30%; 80-100% → 100%. Typical bad outcome: −1 mood and −5/−10 trained stat, possibly Bad Practice.

### 8.4 Statuses (S1, S3)
Positive: Good Practice (−2% fail), Gooder/Practice Perfect ◎ (−4%; Narita Taishin only in S3), Charming, Sharp/Fast Learner (−10% skill cost), Rising Star/Hot Topic, Positive Thinking (blocks one mood drop), Lucky Constitution (blocks one negative).
Negative: Bad/Poor Practice (+2% fail), Migraine (mood cannot rise), Dry Skin/Skin Outbreak (mood drops; from multi-race streaks), Insomnia/Night Owl (−10 energy periodically), Overweight/Slow Metabolism (Speed cannot rise; training can cure), Lazy/Slacker (may skip training; reporter cures). Generally do not burn a turn on the Infirmary; rely on scenario/card cures, or restart. Uma-unique statuses do not affect PvP.
⚖️ Charming: S1 (JP) "+2 bond gain from all sources"; S3 (GL) "+40% bond gain". Hot Topic (S3): +40% bond gain with Chairman/Reporter.

### 8.5 Event odds (S1 = S3)
Rest: 70 energy 25%; 50 energy 62.5%; 30 energy 10%; 30 energy + insomnia 2.5%. Outing: Karaoke +2 mood 35%; Stroll +1 mood +10 energy 30%; Shrine +1 mood +10/+20/+30 energy 20/10/5%; crane game after 25%. Universal event +5 all, +2 mood: 40% per run; getting Sharp from it 5% (S1) ⚖️ 10% (S3). Overweight from +30-energy choice 10%; cure after training 10%. Lazy event 6%; skip training 25%. Extra training after success 6%. Friend card post-training event 40%.

### 8.6 Fan-farming route and rules (S7, URA)
Goal: maximise fan bonus (higher Race Bonus ≈ higher Fan Bonus; 20% Fan Bonus cards all carry ≥10% Race Bonus). Decks (all with MLB Kitasan Black, 15% FB, because win rate needs her):
1. **115% FB**, inherit mostly Stamina + some Power: allows 3★ spark farming; reaches 600/600/600 SPD/STM/PWR on any uma with the highest win rate.
2. **120% FB**, inherit full Stamina: SR-only budget deck, lower win rate; strong on a 20%-growth Speed uma; may fail Tenno Sho (Spring).
3. **115% FB**, inherit mainly Stamina + some Power: lower win rate, still meets Tenno Sho (Spring) stamina.
4. **110% FB**: groundwork-parent hybrid (e.g. Seiun Sky parent); SSR Falcon now gives guaranteed groundwork on first chain. Replacements: Satono Diamond ↔ Manhattan Cafe; Sakura Bakushin O ↔ Biko/Shinko Windy.
20% Fan Bonus MLB replacements: Sakura Bakushin O (SPD), Kawakami Princess (SPD), Satono Diamond (STM), El Condor Pasa (PWR), Fine Motion (WIT), Winning Ticket, Mejiro Ryan, Ikuno Dictus (GUTS), Shinko Windy SR, Sweep Tosho (SPD), Tamamo Cross (PWR), Riko Kashimoto (Friend).

**Aptitudes needed (≥A via inherit):** Turf (most races); Mile (missing it costs ~200k fans at 120% FB); **Medium** (≥ half of total fans); Long (Arima Kinen on Classic + Senior up to 150k fans; Tenno Sho Spring bonus). Sprint optional (+15,100 base fans ≈ 33k at 120% FB). Dirt optional/risky: B or even C is enough; can bait and tank the win rate.

**Best farmers are Front Runners** (least blocking): Maruzensky (original), Silence Suzuka (if Long A; Focus/Concentration + 20% Speed growth), Oguri Cap (1M+ possible but needs 8+ risky wins in a row and dirt; forced Mile Championship costs ~33k), El Condor Pasa, Daiwa Scarlet, Mihono Bourbon, Seiun Sky, Grass Wonder, Gold Ship, Mayano Top Gun; also King Halo, Biwa Hayahide, Rice Shower, Mejiro Ryan, Matikanefukukitaru, Nice Nature, Agnes Digital (many long sparks), untested: Symboli Rudolf, Narita Brian, Hishi Amazon, Gold City.

**General route (S7):** Junior: Nov 1 Daily Hai Junior Stakes; Dec 1 Asahi Hai Futurity; Dec 2 Hopeful Stakes. Classic: Mar 1 Yayoi Sho; Mar 2 Spring Stakes; Apr 1 Satsuki Sho; May 1 NHK Mile Cup; May 2 Tokyo Yushun; Jun 1 Yasuda Kinen (skip if summer training is needed); Jun 2 Takarazuka; Aug 2 Sapporo Kinen; Sep 1 Centaur Stakes (Sprint B or do Rose Stakes/skip); Sep 2 Sprinters Stakes or All Comers; Oct 2 Tenno Sho (Autumn); Nov 1 Queen Elizabeth II Cup; Nov 2 Japan Cup; Dec 1 Champions Cup (only with Dirt B); Dec 2 Arima Kinen. Senior: Jan 2 American JCC; Feb 1 Kyoto Kinen; Feb 2 February Stakes (Dirt B only); Mar 1 Kinko Sho; Mar 2 Osaka Hai; Apr 2 Tenno Sho (Spring) or Milers Cup; May 1 Victoria Mile; Jun 1 Yasuda; Jun 2 Takarazuka; Aug 2 Sapporo; Sep 1 Centaur; Sep 2 Sprinters/All Comers; Oct 2 Tenno Sho (Autumn); Nov 1-2 QE II, Japan Cup; Dec 1 Champions Cup (Dirt B); Dec 2 Arima Kinen. If you are unsure of wins, do not chain 3+ races; winning 2 beats winning 1 and losing 2.
**Maruzensky route** (S7): Junior Nov 1, Dec 2; Classic Mar 1, May 1, Jun 1 (optional), Jun 2, **Jul 1 Radio Nikkei Sho** (secret event: Hot Topic, +2 mood), Aug 2, Sep 1-2, Oct 2, Nov 1-2, Dec 1 (Dirt B); Senior Jan 1 Nikkei Shinshun Hai, Feb 1 Kyoto Kinen, Feb 2 Nakayama Kinen (February Stakes with Dirt B), Mar 1 Kinko, Apr 2 Tenno Sho (Spring)/Milers Cup (with the same stamina rule), May 1 Victoria Mile, Jun 2 Takarazuka, Sep 1-2, Nov 1-2, Dec 1, Dec 2 Arima Kinen.

**Tips (S7):** Year 1: reach 80% bond on Kitasan ASAP, then Speed training and 2-3 Stamina trainings; other cards' bonds do not matter (Biko/Bakushin second). Learn general and strategy skills as you go; ignore distance-specific unless only option (Medium, then Mile/Long; Sprint ignorable). Use Seiun Sky as parent and take her unique early so any uma can front-run even at G. Get Focus/Concentration early.
⚖️ S7's "other cards' bonds do not matter" is specific to URA fan farming; S1 says bond every card to 80 in general.
**Min-max (S7):** only for screenshots; e.g. Suzuka ~1.05M fans with 37/37 wins vs ~1.13M with 44-47 races but slower fans/hour and missed spark stats. In Year 3 you race every turn only if you enter it with about 700/500/500 (which beats URA Finals); 500/300/400 is not enough.

## 9. Inheritance (Parents, Sparks, Compatibility)

### 9.1 Spark types (S1, S3, S6)
| Spark | Effect |
|---|---|
| Blue (stat) | Start stats and stat cap; stars scale amount (initial 1★ +5, 2★ +12, 3★ +21 per parent, i.e. 9★ = +63; borrowed 3 x 21) (S6, S3). Mid-run inspiration gains roughly up to 10 / 16 / 28 by ★ (S6) |
| Pink/Red (aptitude) | Raises aptitudes at start (section 5); mid-run: hidden 1-5 points per proc (S6) |
| Green (unique) | Weaker version of the parent's unique; ★ raises odds and hint level; small stat cap bonus |
| White | Skills (hint level), plus race, scenario, hidden ("目覚め") whites; can also give stats/aptitude |
Scenario genes give 10/20/30 to their stats, rolled independently; race genes give 3/6/9 (S6). There is no cap on white/red/scenario inheritance (S6; max 6 scenario procs = 360 stats).

### 9.2 Getting sparks after a run (S3, S6)
- Blue: one of five stats is picked at random; stars depend on that stat: <600: 1★ ~90%, 2★ ~10%, 3★ 0%; 600-1100: 50/45/6; >1100: 20/70/10. Pink: random among aptitudes at A or better. Win or lose does not matter (S3).
- Whites: 20% for a white skill, 25% for ◎, 40% for gold; +2.5% per ancestor holding it (+5% gold); race/scenario whites 20%; stars 50/45/5 (SS rank or higher: 20/70/10). S6: any skill has 5% flat 3★ chance; lowest generation chance 20%.
- Race genes: must **win the G1 in 1st**; 20-30% chance per run, 5% for 3★; running a race twice does not help. Scenario genes rise with common lineage: 0 common 19.89%, 1 → 21.75%, 2 → 24.93%, 3 → 27.81%, 4 → 30.39% (S6). Aoharu scenario gene can appear even if you fail Aoharu/URA parts.
- ⚖️ 3★ blue odds: S3 table says 3★ needs stat >600 (~6-10% after the stat is picked); S3's own breeding text says "1% per 600 stat, 2★ ~50%". Treat as unresolved.

### 9.3 Compatibility (affinity)
- Overall symbol: ◎ >150, ○ 51-150, △ ≤50 (S3, S6). S6 recommends **>300**; strong parents reach ~400-500. A ◎ made of many weak links (e.g. 50+25+25+50+25+25 = 150) is poor.
- ⚖️ **Race overlap rule changed** (S6): current system (JP since 2.0 anniversary/Grand Masters; **Global since 24 June 2026**): only overlapping **G1 wins** count, **+3 each**; G2/G3 and titles (Triple Crown/Tiara) no longer count; parent-to-parent overlaps count; each race counts once; ideal 22-26 races including dirt (20 turf-only). S3 (older) describes the legacy rule: +1 per identical graded win, later changing to +3 per matching G1 (G2/G3 dropped), retroactive. S1 (JP) says every G1 shared by all parents/grandparents adds compatibility and suggests a dirt rotation (parents at Dirt D-C).
- Hard-coded base compatibility exists between each pair (0 with itself; check Gametora, mee1080 umaishow, U-tools, design.u-ma.org). Mixing Triple Crown and Tiara rotations reduces overlap; dirt aptitude bridges it (S6). L'Arc bridges short/mile with mid/long but caps at 16 overlapping races (S6).
- JP (Aug 2026): the game now shows the full compatibility numbers and each individual link (S6).

### 9.4 Proc rates (S6 data, S3 table, same base numbers)
Base per-star odds at 0 compatibility: Blue 70/80/90% (☆1/2/3); Pink 1/3/5%; Green (unique) 5/10/15%; Race whites 1/2/3%; Other whites (skills, scenario, hidden) 3/6/9%.
**Formula (S6 from Cygames patent; verified by Polaris/Shoppo): `odds = base × (1 + individual compatibility / 100)`**. Example: 3★ green with 200 compat = 15% × 3 = 45%. S3 shows 30 affinity → ×1.3. Grandparents proc about half as often as parents. Individual (per-lineage-member) compatibility applies, not the overall symbol, so one weak grandparent can drag results. Genes can proc in both inheritance events.
⚖️ **Gold inheritance:** S6 concludes it is only a flag that a 3★ proc happened, not an extra bonus (earlier S6 theory: flat ~20% chance and better rolls). S1/S3 do not describe it.

### 9.5 Building parents (S3, S6, S1)
- Inspiration events occur early April of Year 2 and Year 3 (S3).
- **Beginning path (S3, GL):** keep only blues; total ★ counted across the uma and its two parents (a "9★ Speed" uma has a 3★ blue and both parents have 3★). Own 2★ base parent + guest 3★ base parent → 7★ (45 stats) → 8★ (54) → 9★ (63) → then two 9★ umas allow 18★ without guests. Loop breeding does not raise odds.
- **Advanced path (S3):** intentionally made parents win more races (affinity). Use a rental with ideal representative sparks; you can be greedy on grandparents (they are bred out). Keep unwanted aptitudes at B so pinks are not diluted (pink is picked randomly among A aptitudes). Trade blue ★ for scenario factors and better pinks to save time.
- **Distance parent:** 2★ distance pink base → 25-30% chance of S; 3★ → 35-40% (S3). **Dirt parent:** Mile 3★ on the parent, Dirt on grandparents → S Mile ~20%, S Dirt 15-20% (S3). Other parents: End Closer (straightaway spurt), Front Runner (Groundwork, Tail Held High), 6★ style parent (style pinks on grandparents, distance pinks on the parent).
- **Priorities (S6 ch. 8):** plan before the run: purpose (CM/LoH, GGP, main parent), route, rental, deck. Red genes first: **Distance > Ground > Strategy**. Aptitude hidden points: e.g. C→A needs ≥4 points, B→S ≥4, C→S in one go ≥7. Do not raise unwanted aptitudes to A. Don't run a conflicting-strategy parent with no usable whites; one good rental beats building mediocre parents. Blue genes shore up weak stats, but CM-specific whites (e.g. Essence of Stamina) matter more now. Global: first 9★ blue + at least 2★ distance on main parent is enough to start.
- ⚖️ **How much blue matters:** S1 (JP) says blue factors are minimal and people search for strong uniques, distance pinks and many whites; S3 and S6 (Global-facing) make 9★ blue the first goal. S6 says JP parents can even be "borrow one strong rental".
- **Friend search (S1, S3, S6):** UmaPureDB (`uma.pure-db.com`, Global `uma-global.pure-db.com`); Discord friend-ID channels. Look for: 9★ Speed (Long), 9★ Stamina (Mile/Medium), 9★ Power (Sprint), Mile/Dirt/Sprint pinks (Haru Urara, Pasa, Oguri, Air Groove), MLB Kitasan and Super Creek from 9★ umas (S3). CM: strong track uniques, 9★ distance, high race count. Stadium: highest-cap stat blue (Summer Gold Ship rental so a failed gold can be retried).
- **Rentals:** 3 borrows per day; parent +15 stats at start vs borrowed +63; inspiration ~45 total vs ~189 (S3). Mark 3★ blue or 2★ blue + 3★ pink umas as protected parents (S3).
- **Uma Plan (JP, 5th anniversary, S6):** extra roll on the mid-run inheritance (pick 1 of 2) and bulk inheritance farming (5 rolls, 10 with gene pack); products are separate from your hall of fame.

### 9.6 Auto training and background auto (S1, S6)
- Auto-kun (JP, orange "おまかせ"): 15 min (URA) to 25-35 min (Ramen); needs the device on; set options low; enable racing for fans and clocks on failure. Not competitive; good for parents, event points, filling Stadium. You can reroll sparks at run end (costs TP).
- **Background auto** (JP 30 Jun 2026; Global early July 2026): fixed 50 minutes, all scenarios, cannot fail, objective races auto-won; other races use aptitude-based odds, not stats: 110% at A/A. Sample (A ground/distance): <3 consecutive 100%, 3rd 100%, 4th 85.7%, 5th 75.2%, 6th+ 58.9%. A/B: 100/92.4/76.7/72.1/54.8. A/C (small sample): ~90/70/60/50/36.5. Umas that win with low aptitude via kit are underestimated.

## 10. Skills

### 10.1 Types (S1)
Green (stat, ignores cap; +40 at level 1, +60 at level 2 for stat greens; purples −40), Blue (recovery), Red (debuff), Orange (Speed/Accel/lane/start/vision). Value is by activation frequency (PvP: Speed greens most useful, sometimes Stamina green on Long because Stamina >1200 converts to speed).
- Recoveries: gold 5.5% HP, white 1.5%; range 1.5%-7.5%. (GL, S3) unique below 3★ restores 3.5%, else 5.5%. Best heal times are before the end of the Middle Leg. In JP most builds need recoveries only on Long (S1).
- Debuffs: **only Speed-down matters** in JP meta; HP-down does nothing when HP is ample; Kakari extension mostly griefing; Accel-down too rare. Teammates are not affected by debuffs (S2).
- Speed skills use Target Speed (useless before top speed) or Current Speed (never wasted); Accel skills only help while accelerating. Lane skills: outward in final leg, inward otherwise. Vision skills do nothing (vision hard cap).
- Uniques: 3★ uma can pass her unique; inherited unique strength −0.2, duration −40% (0.35/5s → 0.15/3s; dual uniques hit hardest: 0.25 speed +0.3 accel → 0.05/0.1; heal 5.5% → 1.5%, strong 7.5% → 3.5%). Level scaling: +1% first level up, then +3% per level (recovery +2% per level) (S1).
- Skill condition syntax (S1): `&` before `@`; conditions include order, order_rate, distance_rate, phase_random, straight_random, corner_random, accumulatetime, near_count, is_finalcorner, slope, is_overtake, change_order_onetime. `phase_random==0` with `accumulatetime` can be impossible (early spots). Skills activate in ID order (S2).
- Skill activation chance and Wit: section 4.2.
- Gate blocks (S1): 8 blocks; with 9 runners two in block 8; 12 (Stadium/LoH): two in blocks 5-8; 18: three in 7-8. Lucky Seven 2/12 in Stadium, Outer Gate 6/12, Inner 3/12; CM 9 runners Outer 4/9, Inner 3/9, Lucky Seven 1/9.

### 10.2 Effectiveness math (S1 examples)
Speed skill value = effect × duration × (track/1000): Speed Star 0.35 m/s × 1.8 s = 0.63 m (1.51 m on 2400m). Accel skills: compute time and distance to top speed with and without (0.424 m/s² at 1000 Power): Groundwork ≈ +4.1 m; Seiun unique ≈ +10.3 m; Imminent Shadow ≈ +6.4 m (2000m chaser).
Skill duration and cooldown scale with `distance/1000` (S2).

### 10.3 Skill level tables (S2)
| Lv | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Target speed | 1.00 | 1.01 | 1.04 | 1.07 | 1.10 | 1.13 | 1.16 | 1.19 | 1.22 | 1.25 |
| Accel | 1.00 | 1.02 | 1.04 | 1.06 | 1.08 | 1.10 | 1.125 | 1.15 | 1.175 | 1.20 |
| Stat | 1.00 | 1.01 | 1.02 | 1.03 | 1.04 | 1.05 | 1.06 | 1.07 | 1.08 | 1.10 |
| Recovery/current speed/lane | 1.00 | 1.02 | 1.04 | 1.06 | 1.08 | 1.10 | 1.12 | 1.14 | 1.16 | 1.18 |

Other scalings (S2): Aoharu skills by team base stats total (0.8× <1200 … 1.2× ≥3600); Climax skills by races won (0.8× <6 … 1.2× ≥25); MaximumRawStatus (0.8× <600 … 1.2× ≥1100); green-skill count (0-2 0×, 3-4 1×, 5 2×, 6+ 3×); MultiplySpeed by Speed stat; L'Arc potential level; top lead amount. Duration scaling: distance-from-top `min(0.8 + d/62.5m, 1.6)`; remaining HP (Mejiro Bright/McQueen tiers up to 4.0×; Matikane 3.0×); +1 s per overtake up to 3.

### 10.4 Wiz Limit Break (JP 5th-anniv, S2)
With Wit >1200, unique/evolved/gold skills that raise target speed (ID 27) or current speed with natural deceleration (ID 22) get extra effect: `BaseSkillValue × PhaseStrategyCoef × WizMultiplier`. Multiplier by (Wit−1200): 1→0 …, 21→0.02, then +0.02 per 20 up to 201→0.2; +0.06 per 20 up to 401→0.8; +0.01 per 20 up to 801→1.0; then +0.01 per 100 (901→1.01 … 1901→1.11; max 1.12). Wit here includes motivation/skills but not strategy proficiency. Phase-strategy coefficients (early/mid/late/last spurt): Front and Oonige 0.26/0.23/0.19/0.16; Pace 0.21 all; Late 0.19/0.18/0.23/0.24; End 0.15/0.17/0.25/0.27. Inherited and white skills are unaffected.

## 11. Race mechanics (condensed from S2, S1)

- **Frame:** 0.0666 s (~15 fps); 24 sections; phases: Early 1-4, Mid 5-16, Late 17-20, Last Spurt 21-24 (S1 gives 1/6, 3/6, 1/6, 1/6). 1 Bashin = 2.5 m. 1 course width = 11.25 m; horse lane = 1/18 course width.
- **Speed:** BaseSpeed = 20 − (Dist−2000)/1000 (1200m 20.8; 2500m 19.5). Target = BaseTarget × PositionKeepCoef + forced-in + skill + slope + lane modifiers; capped 30 m/s. Start speed 3 m/s; start dash +24 m/s² until 0.85 × BaseSpeed; start delay random up to 0.1 s (>0.08 s = late start; not affected by Wit).
- **Strategy phase coefficients (speed):** Front 1.0/0.98/0.962; Pace 0.978/0.991/0.975; Late 0.938/0.998/0.994; End 0.931/1.0/1.0; Oonige 1.063/0.962/0.95 (early/mid/late+spurt). **Acceleration:** Front 1.0/1.0/0.996; Pace 0.985/1.0/0.996; Late 0.975/1.0/1.0; End 0.945/1.0/0.997; Oonige 1.17/0.94/0.956.
- **Deceleration:** early −1.2, mid −0.8, late −1.0 m/s²; pace-down −0.5; out of HP −1.2.
- **Randomness per section:** +BaseSpeed × [Min, Max]%, Max = Wit/5500 × log10(0.1·Wit), Min = Max − 0.65 (400 Wit: +0.117%/−0.533%). Not in last spurt.
- **Last spurt:** decided at start of late-race with enough-HP check; if HP is short, candidates by lowering speed 0.1 m/s steps, accepted with `15 + 0.05·Wit`% each from best time; slowest if all fail. Recomputed after a heal (post-1st anniv).
- **HP consumption:** `20 × (V − BaseSpeed + 12)² / 144 × status × ground × downhill`; status: Rushed 1.6, Pace-down 0.6, Front Spot Struggle 1.4 (with Rushed 3.6), Oonige Spot Struggle 3.5 (with Rushed 7.7). Ground 1.02 (heavy/bad turf, bad dirt), dirt heavy 1.01. Downhill mode 0.4×. Late-race and spurt: Guts modifier.
- **Position keeping (sections 1-10):** checked every 2 s; 1 s cooldown after exit. Front Runner Speed Up 1.04× (first, <4.5 m ahead; Oonige 17.5 m; 12.5 m if only one runner after 1.5 anni.; chance `20·log10(0.1·Wit)`%); Overtake 1.05×; Pace Up 1.04× (chance `15·log10(0.1·Wit)`%); Pace Down 0.945× in mid-race (0.915× otherwise, or before the 1.5 anni. fix); **Pace Up Ex 2.0×** (someone behind by strategy is ahead). Thresholds vs pacemaker: CourseFactor = 0.0008×(Len−1000)+1; Pace 3.0 to 5.0×CF m, Late 6.5-7.0×CF, End 7.5-8.0×CF. If no Runner, the first Leader acts as one (S1).
- **Rushed (Kakari):** rolled before the race; chance `(6.5/log10(0.1·Wit+1))²`% (300→19%, 600→~14%, 900→~12%, 1200→~10%; 自制心 −3%); occurs in a random section 2-9; each 3 s 55% to snap out; ends by 12 s. Style change: Pace → Runner; Late → 75% Front/25% Pace; End → 70% Front/20% Pace/10% Late; HP 1.6×.
- **Spot Struggle:** after 150 m, two+ Front Runners (or Oonige) within 3.75 m and 0.165 course width; extra speed `(500·Guts)^0.6 × 0.0001` for `(700·Guts)^0.5 × 0.012 × StrategyProf` s; ends by section 9.
- **Dueling (final straight):** candidates within 3 m and 0.25 CW for 2 s, ≥15% HP, one in top 50%; extra speed `(200·Guts)^0.708 × 0.0001`, accel `(160·Guts)^0.59 × 0.0001`; exits below 5% HP.
- **Conserve Power / Release (JP; >1200 power):** Power used = BasePower + 0.5×max(Raw−1200,0). Gains credit in first 10 sections at 4.2 (normal) / 6.7 (pace down) × style (Front 1.0, Pace 0.75, Late 1.0, End 0.7) per second; blocked by Speed Up/Overtake/Pace Up/Ex, Rushed, Spot Struggle (+1.5 s cooldown); Spot Struggle ×0.95, Rushed ×0.8. Released at last spurt as acceleration for `Conserved × sqrt(Dist) × DistType/1450` s (Short 0.45, Mile 1.0, Mid 0.875, Long 0.8; not under 0.2 s).
- **Compete Before Spurt / Stamina Keep / Secure Lead (sections 11-15, from parameter file, unconfirmed):** extra speed for 2 s at HP cost then 1 s cooldown; Stamina Keep chance `30%×(Wit/1000+Wit^0.03)` (highly speculative).
- **Blocking:** front block if 0<gap<2 m and lane gap ≤ (1.0−0.6·gap/2)×0.75 lanes; speed limited to (0.988 + 0.012·gap/2m) × blocker's speed. Side block within 1.05 m and 2 lanes. Overlap <0.4 m and <0.4 lane: outer bumped. Vision starts at 20 m.
- **Lanes:** Target lane modes: Normal, Overtake, Fixed. Extra move lane set on entering the final corner. Lane speed `0.02×(0.3+0.001·Power)`. Running wide on corners or diagonally adds distance.
- **Slope:** Uphill loses `SlopePer×200/Power` target speed; downhill mode chance `0.04%×Wit` per second gives `0.3 + |slope|/10` m/s and −60% HP; ends 20%/s. Slope events replaced older calculation after 1st anniversary.
- **Finish time:** displayed time = actual × 1.18 with clamped bounds; margins: nose 0.2 m, head 0.4 m, neck 0.8 m (at 15 m/s scaling).
- **Strategy shape (S1):** Great Escape ★★★★★ opening /★★ mid /★ final; Runner ★★★★☆/★★★☆☆/★★☆☆☆; Leader ★★★☆☆/★★★★☆/★★★☆☆; Betweener ★★☆☆☆/★★★★☆/★★★★★; Chaser ★☆☆☆☆/★★★★★/★★★★★.
- **Ground/Distance profiency for accel/speed:** section 5.

## 12. Score and ranks (S1)

- Unique skill level gives 170 points/level (120 for 1-2★ umas). Skill points = skill value × 1.1 (A/S in related strategy/distance), 0.9 (B/C), 0.7 (G), 0.8 (other), ×1.0 if no association. Inherited uniques 180 (Vive la GOLD 198). Purple skills −129 (cost 50) or −262 (cost 100). Aptitudes, wins, titles give no direct score.
- Stat → points (approx): 300 → 352; 400 → 577; 500 → 847; 600 → 1143; 700 → 1463; 800 → 1808; 900 → 2209; 1000 → 2653; 1100 → 3171; 1200 → 3841.
- Rank thresholds: G <300; G+ 300; F 600; F+ 900; E 1300; E+ 1800; D 2300; D+ 2900; C 3500; C+ 4900; B 6500; B+ 8200; A 10000; A+ 12100; S 14500; S+ 15900; SS 17500; SS+ 19200; UG 19600; UF 23900; UE 28800; UD 34400; UC 40700; UB 47600; UA 55200; US 63400; US9 71400+. Calculators: umsatei.com, yonkim.azurewebsites.net.

## 13. PvP essentials

### 13.1 Stadium / Team Trials (S1, S3)
- Five categories: Short, Mile, Medium, Long, Dirt (dirt always Mile). 1v1 early, then 3v3 by weekly promotion; win 3 of 5. No duplicate umas (or alternate versions of one uma) in a team, so you need 15 unique umas. Scoring is by points (start, skills used, closeness, dominance, best in position); using different strategies gives "Nice Position" bonus.
- 1-2★ ideas: Short: Sakura Bakushin O / Air Groove (inherit Short) / King Halo. Mile: Twin Turbo, Ikuno Dictus, Vodka. Medium: Daiwa Scarlet, Agnes Tachyon/Tsuyoshi/Royce, Winning Ticket/Mejiro Ryan. Long: Super Creek, Matikanefukukitaru/Matikanetannhauser, Gold Ship. Dirt: Mayano Top Gun (inherit Dirt+Mile), El Condor Pasa, Haru Urara (inherit Mile). S3 new-player set: Bakushin Sprint, Vodka Mile, Daiwa Medium, Gold Ship Long, Urara Dirt. Best 3★ ticket picks: Oguri Cap, Taiki Shuttle, Maruzensky (S1, S3).
- Promotion happens weekly (Mon 05:00 JST, S1). Items: max mood (+4% all stats), sunny, rainy, first-3 gate blocks, last-3 gate blocks.
- Frequencies (S1 JP): Short: 1000m 8%, 1200m 54%, 1400m 38%. Mile: 1500 5.3%, 1600 36.7%, 1800 58%. Medium: 2000 62.6%, 2200 20%, 2300 4.7%, 2400 12.7%. Long: 2500 18%, 2600 37.3%, 3000 16.7%, 3200 8%, 3400 10.7%, 3600 9.3%. Dirt: 1600 25%, 1700 25%, 1800 50%. Season: Spring 40, Summer 22, Fall 12, Winter 26; weather Sunny 58, Cloudy 30, Rain 11, Snow 1; track Good 77, Slightly Heavy 11, Heavy 7, Bad 5. Nocturnal and exchange-race skills do not trigger.

### 13.2 Champions Meeting (CM) (S1, S3)
- Monthly 3v3v3, all on one track; Graded League (any uma, much better rewards; 3rd in Graded finals ≈ 1st in Open finals) vs Open League. ⚖️ Open League limit: **(JP) UC or worse (S1)**; **(GL) B or worse (S3)**.
- Rounds 1 and 2: two days each, 4 entries/day, 5 races each; best score counts. Final: one race, uma registration 12 hours after Round 2 (else last entry umas). Opponents may be raced asynchronously.
- Prep: analyse track, spurt start, use the Umalator, check win-rate stats (booklet icon), build specialised umas with S distance and suitable uniques.

### 13.3 League of Heroes (LoH) (S1)
Monthly event; placement-based points, so debuffers/sacrificial umas are usually poor. 6 days, 5 tickets/day; Silver+ starts at 4000 points; max 34,000. Strategy: save tickets and run later days (5 per day, parfaits on 3) so weaker players rank up first. 12 runners: 25% inner gates, 50% outer, Lucky Seven 16.6%. Popularity is T-score based (Speed/Stamina/Power/Wit/Guts evaluations; symbols ◎○▲△; >70 large bonus). Top 30,000 get extra jewels/titles.

## 14. Resources and account (S1, S3, S5)

- **Reroll** on a strong banner, especially with free rolls; spend everything on support cards. Free-roll windows: scenario launches (~every 4 months), anniversary (24 Feb), half anniversary (24 Aug), New Year (S1: December; S5: beginning of January). Reroll targets: good Speed/Wisdom SSRs that work at 0-1LB (S5).
- **Gacha (S3):** SSR/3★ rate 3%, rate-up 0.75% each; the spark at 200 pulls picks any rate-up; on average you spark twice for an MLB SSR (~400 rolls; S3 tips). Pity does not carry between banners. Roll only with a spark ready (30,000 jewels) and in multiples of 200 (S1, S3). Save pink tickets (≈150 jewels each).
- **Banner rules (S3):** MLB card needs two pities; skill cards one; dual-SSR banners preferred; free-roll banners first (S1).
- **First month (S3):** level only the cards you use; add friends with good parents; win each graded race once; mark good parents; train one uma per Team Trials distance; join a Club/Circle for medals/points; Daily Legend Races give 250 jewels (JP).
- **Auto (S1, S3):** do not use auto for decks, parents or PvP teams; use rental decks early; link password and Cygames ID; JP Cystore link = 300 jewels.
- **Expected ranking of future spending (S3):** treat F2P income as about 300k carats/year.

## 15. Coverage gaps

- S4 had no content. S5's images (ranked score lists) and S1's images/graphs (e.g. some tables, position-keep graph) could not be read; only text is included.
- S1 sections on currencies, menu translation, in-game events, Analyzing Tracks, Popularity details, and S3's banner reviews, per-uma reviews, skill rankings and unity/scenario master-guide pages are not condensed here. Read the originals when needed.

## 16. Conflict register

| # | Topic | Source A | Source B | Note |
|---|---|---|---|---|
| 1 | Stat cap | S2 (JP): raised from 2000 to 2500 at 5th anniversary | S3/S6 (GL): 1200 cap, uncap not yet | Server difference |
| 2 | Wit goal | S1: 1200+ (Wiz LB, S2) | S3: 300-500 | Patch/cap dependent |
| 3 | Speed formula | S2 has Guts term | S3 omits Guts term | S3 predates the Guts update |
| 4 | Blue factors | S1: minimal in JP | S3/S6: 9★ blue is first goal | Server/meta difference |
| 5 | Compatibility source of race points | S3 legacy: +1 per graded win | S6/S1: +3 per G1 only (GL since 24 Jun 2026) | S6 newest |
| 6 | Charming effect | S1: +2 bond | S3: +40% bond | Wording/server |
| 7 | Sharp from universal event | S1: 5% | S3: 10% | Unreconciled |
| 8 | Open League limit | S1: UC or worse | S3: B or worse | Server difference |
| 9 | Free-roll New Year | S1: December | S5: beginning of January | Unreconciled |
| 10 | Race Bonus importance | S5: minor, 34% helps | S7/S1: central for URA fans; 34% breakpoint | Context (scenario/goal) |
| 11 | Bonding non-key cards | S1: bond all cards to 80 | S7: only Kitasan (and Biko/Bakushin) matter in URA fan farming | Context |
| 12 | 3★ blue odds | S3 table: 6-10% conditional on picked stat | S3 text: 1% per 600 stat | Unresolved |
| 13 | Gold inheritance | S6 early: flat ~20% chance, better results | S6 later: only indicates a 3★ proc | S6 later version wins |
| 14 | Recovery unique amount | S1: inherited unique 1.5% (3.5% strong) | S3: unique <3★ = 3.5%, else 5.5% | Different situations |
| 15 | Agemasen | S1: no JP modern card misses gold | S3: still a rate (GL) | Server |
| 16 | Pace-down modifier | S2: 0.945× mid-race after 1.5 anni.; 0.915× before | | Patch history |

## 17. Dates and drift

Sources span 2025-07 to 2026-08: S5 (YHS parameters, July 2025), S3 (Nov 2025), S7 (Nov 2025), S1 (5th anniversary, Feb 2026), S6 (Aug 2026, mentions 5.5-anniversary UI). Card rankings and scenario relevance move every ~4 months; recheck the newest scenario's guide and banner reviews before spending.
