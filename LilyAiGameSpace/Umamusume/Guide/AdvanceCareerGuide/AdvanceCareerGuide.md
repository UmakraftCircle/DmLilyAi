# Umamusume: Advance Career Guide (Unified Reference, Master Index)

Merged from 7 uploaded source documents (rebuilt 2026-10-01 without shortening). Where sources agree they are unified into one statement. Where they disagree, **both values are kept with their source tags** (marked ⚖️ and collected in section 5 of this file). Nothing is my own opinion; anything inferred rather than stated is labelled *(inferred)*.

Because the GitHub tool needs the full text of every write, the guide is split into six detail files in this same folder. They are one guide; read them in any order.

| File | Contents |
|---|---|
| `Part1_CareerTraining.md` | The run itself: bond, training formula, energy, moods/statuses, failure, seasonal events and odds, fan checkpoints, race rewards and rows of races, recorded benchmark runs, auto-kun/background auto, score/ranks, URA fan farming (decks, farmers, race routes), first month and account setup |
| `Part2_StatsAndRaceMechanics.md` | Stat definitions and caps, aptitudes, what each stat does, stamina/guts/required Stamina tables, speed/accel model, phases and strategies, skill engine (conditions, scaling), lanes/blocking/vision, position keeping, Rushed, Spot Struggle, Dueling, Conserve Power, Compete/Secure Lead/Stamina Keep, Stamina Limit Break, Zenkai Spurt, Wiz Limit Break, course/frame order |
| `Part3_SupportCards.md` | Card passives, race bonus, S5 scoring method, deck order, every card write-up by type, welfare/tickets/shop/reroll, friend/group cards per scenario |
| `Part4_InheritanceAndParenting.md` | Genes, compatibility (current and legacy), proc formulas, red/blue/white/green/race/scenario generation, grade effects, building parents, Uma Plan/bulk inheritance, parent-scenario ratings |
| `Part5_SkillsAndPvP.md` | Skill types and math, strategy builds, track analysis, Umalator workflow, Stadium, Champions Meeting, League of Heroes, popularity |
| `Part6_AccountGachaEvents.md` | Gacha rates and pity table, every currency and income source, circles, Legend Races, events, collection/menus |

## 1. Sources and how to read this

| Tag | Document | Author | Scope / date | Usage notes |
|---|---|---|---|---|
| **S1** | Umamusume Reference (5th Anniversary) | shory + JP veterans (orig. Erzzy) | JP server, 5th-anniversary edition (2026-02) | Training, PvP, cards, skills, currencies, events |
| **S2** | Uma Musume Race Mechanics | KuromiAK (reverse-engineering credit: @umamusu_reveng, @kak_eng, @hoffe_33; simulators by Aya, kakku, Tunnelblick) | Mostly JP; post-1st-anniversary parts partly speculative (parameter file, packet captures, manual testing) | Formulas |
| **S3** | Umamusume Global Reference Document | Erzzy (terms: Kireina) | Global server, changelog to 2025-11-14 | Global numbers, terms, builds |
| **S4** | Luh's support cards encyclopedia | Luh | Google Drive shell (1 page) | **No usable content** (navigation bar only); nothing taken from it |
| **S5** | UmaMusu Support Card Evaluation Doc | celery6305 | JP meta, Yukoma Hot Springs parameters, PvP-oriented (2025-07-15 update) | Score images did not extract; only text notes used |
| **S6** | Crazyfellow's Parenting & Gene guide | Crazyfellow | JP terms; through Aug 2026 | Inheritance, compatibility, parent scenarios |
| **S7** | URA Fans Farming Guide | Pekoge | URA scenario; updated 2025-11-26 | Fan farming |

Tags: **(JP)** = Japanese server, **(GL)** = Global server. Time-sensitive facts have drifted: S5 (Jul 2025), S3 (Nov 2025), S7 (Nov 2025), S1 (Feb 2026), S6 (Aug 2026). Prefer the newest source where it directly addresses the same mechanic, and read ⚖️ lines before acting.

## 2. TL;DR (cross-source consensus)

1. Support cards decide your account's power; reroll for strong ones when free rolls are on (S1, S3, S5).
2. Stat priority: **enough Stamina to finish > Speed > Power > Wit > Guts**. About 300 Stamina under the requirement turns Speed into a decoration (S1, S3).
3. Run the newest scenario for competitive umas unless distance-locked (S1, S3); use the scenario's friend/group card (S5).
4. Early run: bond cards to 80 for rainbows; then rainbows, Wit for energy, races when nothing is good (S1, S3). ⚖️ S7's fan-farming exception (only Kitasan bond matters).
5. Reach 34% Race Bonus if you can: +3 all becomes +4 (S1, S3, S5).
6. Distance aptitude S is the most valuable (S6, S3); parents' red genes, G1 overlap and individual compatibility drive inheritance (S6).
7. Borrow the best rental parent you can find rather than building mediocre parents (S1, S3, S6).
8. Skills matter more than small stat differences among top cards (S5, S1).
9. Check Stamina with the Umalator or a calculator before PvP (S1, S3).

## 3. Terminology map

| Global (S3) | JP / community | Notes |
|---|---|---|
| Front Runner | Runner, Nige, Front | Oonige = Great Escape/Runaway, a Runner subset |
| Pace Chaser | Leader, Senkou, Pace | |
| Late Surger | Betweener, Sashi, Late | |
| End Closer | Chaser, Oikomi, End | |
| Wit | Wisdom, Int, 賢さ, "Wiz" (S2) | |
| Sprint | Short | 1000-1400 m |
| Mile | Mile | 1401-1800 m |
| Medium | Mid | 1801-2400 m |
| Long | Long | 2401-3600 m |
| Mood | Motivation, Yaruki | |
| Rushed | Kakari, Temptation, Panic | |
| Legacy / Guest Legacy | Parent / Rental parent | official JP term "Inheritance" (S6) |
| Sparks | Factors, Genes, 因子 | Blue stat, Pink/Red aptitude, Green unique skill, White skills/races/scenario/hidden |
| Affinity | Compatibility | |
| Team Trials | Stadium | |
| Club / Club Points | Circle / Trainer Medals | |
| Cleats | Horseshoes | |
| Carats | Jewels | |
| Fast Learner | Sharp (切れ者) | −10% skill cost |
| Charming | 愛嬌 | ⚖️ effect worded differently (Part 1, 1.2) |
| Slow Metabolism | Overweight | |
| Slacker | Lazy | |
| Night Owl | Insomnia / 夜ふかし気味 | |
| Poor Practice / Practice Perfect | Bad / Good Practice | |
| Unity Cup | Aoharu | scenario |
| MANT | Make a New Track / Trackblazer | scenario |
| Stamina Compete | Stamina Limit Break, スタミナ勝負 | S2/S1 |
| Oonige | Great Escape | |
| Spark | pity at 200 pulls (JP usage; on Global "sparks" also means inheritance factors, S3) | |

Other shorthand (S1): MLB = max limit break (4LB); Ult = unique skill; agemasen = a card fails to give its gold skill; GGP/GP = great-grandparent/grandparent; SP = skill points; TP = training points; RP = race points; MB/TB/FB = motivation/training/friendship bonus.

## 4. Reading order suggestions

- New player: Part 6 (6.7), Part 1 (1.1-1.4, 1.15), Part 3 (3.4, 3.7-3.9), Part 2 (2.3-2.4).
- Competitive trainer: Part 2, Part 5, Part 4, Part 3.
- Parent farmer: Part 4 then Part 1 (1.12) and Part 6.
- Fan farmer: Part 1 (1.14) and Part 3 (3.10).

## 5. Conflict register (all ⚖️ items)

| # | Topic | Source A | Source B | Note / where kept |
|---|---|---|---|---|
| 1 | Stat cap | S2 (JP): 2000, raised to 2500 at 5th anniversary | S3/S6 (GL): 1200; uncap not applicable until cap passes 1200 | Server difference. Part 2, 2.1 |
| 2 | Wit target | S1 (JP): push 1200+ (Wiz Limit Break) | S3 (GL): 300-500 | Patch/cap dependent. Part 2, 2.3 |
| 3 | Last-spurt speed formula | S2: includes a Guts term (added after 1st anniversary) | S3: omits Guts term | S3 older. Part 2, 2.3 |
| 4 | Distance S effect | S3: +10% Speed (as stated) | S2/S1: +5% raw, ≈+10.25% after conversion | Same effect described differently. Part 2, 2.2; Part 5, 5.5 |
| 5 | Strategy aptitude and activation | S1: matters little in URA but in PvP; theory it changes skill activation | S2: activation uses base Wit; strategy aptitude has no effect | S1 itself says it's possibly a bug. Part 2, 2.2 |
| 6 | Blue (stat) factor importance | S1 (JP): minimal | S3/S6: 9★ blue is the first goal | Server/meta. Part 4, 4.6 |
| 7 | 3★ blue odds | S3 table (per stat): 3★ ≈5-10%, requires >600 | S3 breeding text: "1% per 600 stat, 2★ ≈50%"; S6 umamusustation data: 0% below 600, ≈5-6.5% 600-1049, ≈10-11% from 1100 | Most detailed: S6 data. Part 4, 4.6 |
| 8 | Race overlap/compatibility | S3 legacy: +1 per graded win, G1/G2/G3 count; later +3 per G1, G2/G3 dropped | S6/S1: +3 per G1 only; GL switched 24 Jun 2026 | S6 newest. Part 4, 4.3 |
| 9 | URA Finals in compatibility | S6 (2021 text): counted | S6 (corrected 11 Sep 2025, Cygames FAQ): do not count | Corrected. Part 4, 4.3 |
| 10 | Gold inheritance | S6 early: flat ~20% chance that raises odds | S6 later (Polaris): only indicates a ★3 proc | Later wins. Part 4, 4.2 |
| 11 | Gene proc growth by lineage | S6 simplified: linear +2.5%/+5% per lineage member | Aoneko/Aya: 1.1^N exponential; linear over/underestimates | Part 4, 4.7 |
| 12 | Charming | S1 (JP): +2 bond gain from all sources | S3 (GL): +40% bond gain | Wording/server. Part 1, 1.2/1.4 |
| 13 | Sharp from universal event | S1: 5% | S3: 10% | Unreconciled. Part 1, 1.9 |
| 14 | New Year rewards | S1: +25 to a stat (Classic), +8 all (Senior) | S3: +10 to a stat (Classic), +5 all (Senior) | Server/version. Part 1, 1.6 |
| 15 | Open League limit (CM) | S1 (JP): UC or worse | S3 (GL): B or worse | Server difference. Part 5, 5.7 |
| 16 | Free-roll New Year | S1: December | S5: beginning of January | Unreconciled. Part 1, 1.15; Part 6, 6.2 |
| 17 | Race Bonus importance | S5: minor, 34% worth ~25 score points | S1: URA/Aoharu should reach 34%; S7: central for fan farming | Context. Part 3, 3.2 |
| 18 | Bonding all cards | S1: bond every card to 80 | S7: only Kitasan (and Biko/Bakushin) matter in URA fan farming | Context. Part 1, 1.2 |
| 19 | Recoveries and debuffs relevance | S1 (JP): recoveries mostly for Long; only Speed-down debuffs relevant | S3 (GL): stamina is scarce; Mid/Mile need recoveries; stamina debuffs matter | Server. Part 5, 5.1 |
| 20 | Recovery unique amount | S1: inherited unique 1.5% (3.5% strong) | S3: unique <3★ = 3.5%, else 5.5% | Different situations. Part 2, 2.4; Part 5, 5.1 |
| 21 | Agemasen | S1: no modern JP card misses its gold | S3: still a chance (GL, older cards) | Server. Part 3, 3.1 |
| 22 | Trainer Medal / Club limit-break priorities | S1 (JP): Rhein Kraft > Special Week > Silence Suzuka 3LB = McQueen 3LB > Brian 3LB … | S3 (GL): McQueen 3LB > Brian 3LB > Rice Shower 2LB > MLB Brian/McQueen > Winning Ticket | Server/era. Part 3, 3.8; Part 6, 6.2 |
| 23 | Specialty display | S3: some sites show 100, JP consensus 116 (changelog 2025-07-27) | S1: 116 | Display artifact. Part 1, 1.3 |
| 24 | Pace Down modifier | S2: 0.945× in mid-race after 1.5 anniversary | S2: 0.915× before | Patch history. Part 2, 2.9 |
| 25 | Wiz Limit Break worked example | S2: 1325 Wit is 125 over, "141 threshold, 0.14" | S2 table: 125 falls at the 121 row (0.12) | Internal inconsistency in S2; noted. Part 2, 2.10 |
| 26 | Compete Before Spurt coefficient table | S2: column heading lost in extraction (values Oonige 0.2, Nige 0.8, Senkou 1.0, Sashi 1.0, Oikomi 1.0) | Same section: Oonige 2.0/Nige 1.1 for a sole front runner | Extraction gap. Part 2, 2.9 |
| 27 | Compatibility display | S1/S3/S6 (older): hidden numbers; symbol only | S6 (Aug 2026, JP): numbers and links now shown | JP only. Part 4, 4.3 |
| 28 | Sprint/Mile gate blocks and Lucky Seven | S1: 1/9 in CM, 3/18 in large races, 2/12 in Stadium | S3: only a 50% chance to do something even in gate 7 | Complementary. Part 2, 2.6 |

## 6. Coverage gaps (what was not condensed)

- **S4**: no usable content.
- **S5**: all ranking images (score lists per card type, non-MLB chart, reroll target cards, current card meta icons), so exact card scores, ranks and which cards are the "used always" ones are missing. Only the written notes are included.
- **S1**: UI/menu screenshot captions; Japanese-learning resource list; Popularity section after the "manipulating" paragraph; image-only tables (some base-skill score values partly garbled); the Stadium scoring article.
- **S3**: banner reviews and future banners; uma and skill tier lists/rankings (time-sensitive); the Grand Concert/Unity Cup scenario pages; the Global Team Trials race frequencies; the "Parents to Try Making" per-distance target lists beyond the numbers kept; the skill and gold-recovery ranking pages; micro-optimisations; Pal card pages. Several of these were skimmed, not preserved.
- **S6**: the images (compatibility screenshots, DYI/Onsen/Ramen setups), the tail of the bulk-inheritance section (cut off in extraction), the Chapter 4 data tables that were chart images (skill gene appearance counts by lineage, green gene grade table).
- **S2**: some formula images did not render in the PDF (formulas were reconstructed from the surrounding text and tables); the exact condition tables for several rare abilities; the "Position, World Transform" mathematics is only summarised.
- **S7**: deck images (card names for decks 1-4 are not named in the text), Maruzensky stat screenshots, and the min-max screenshot.
- Items I marked *(inferred)* or that sources flagged as unclear (e.g. race gene counts per G1, Stamina Keep formula, Secure Lead scaling) are kept as stated, not resolved.

## 7. Dates and drift

Sources span 2025-07 to 2026-08. Card meta, scenario relevance and compatibility rules move every ~4 months. As of the newest source (S6, Aug 2026): Global uses the new compatibility system since 24 June 2026; background auto exists on JP (30 Jun 2026) and Global (early July 2026); JP shows compatibility numbers (5.5 anniversary); Uma Plan is JP-only; Breeders' Cup and Tracen-ken/Ramen are the relevant parent-farming scenarios. Recheck the newest scenario guide and banner reviews before spending.

