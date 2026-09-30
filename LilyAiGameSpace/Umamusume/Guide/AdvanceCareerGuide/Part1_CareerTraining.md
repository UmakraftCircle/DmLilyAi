# Part 1: Career Training (the run itself)

Part of the Advance Career Guide. Master index and conflict register: `AdvanceCareerGuide.md`. Source tags: S1 = JP Reference (5th Anniversary), S2 = KuromiAK Race Mechanics, S3 = Global Reference, S4 = Luh's card encyclopedia (empty PDF), S5 = celery6305 Card Evaluation Doc, S6 = Crazyfellow Parenting guide, S7 = Pekoge URA Fans Farming guide. ⚖️ = the sources disagree, both values are given.

## 1.1 What a run is

- The umas you pull are **templates**, not finished racers. Selecting one makes a fresh clone with template base stats each run; stars/level raise the template only, never already-trained umas (S1, S3).
- Level (gold border = level 3+) comes from trading shoes and pennants/banners; stars come from Pieces (duplicates, statues, Legend Races). At 3★ an uma unlocks her outfit and can pass her unique skill via inheritance; 3★ uniques are also noticeably stronger than 1-2★ versions (S1, S3).
- A run lasts ~2.5-3 years, one turn per half-month (S1). Races open from July of Junior Year (S1).
- **Actions each free turn (S1):** Rest, Infirmary (only if a non-unique negative status exists), Outing/Date, Race, Train.
- Training buttons: Speed, Stamina, Power, Guts, Wisdom (left to right), plus a 6th "?" in scenarios with alternate training (e.g. Yukoma's PR training) (S1). Each training can have up to 5 support participants.
- **Energy:** Wisdom training normally recovers energy; the other four consume it (S1). Energy cost +1 at levels 2 and 3, +2 at levels 4 and 5; a level-5 Speed training costs 25 (S1, S3). Rest gives fixed 30/50/70 (odds in 1.9). Outings are the main energy source in most scenarios; rest is used mostly in URA (S1).
- **Infirmary (S1):** removes 1 removable negative status and restores 20 energy. If the run only survives by using it, restarting is better.
- **Friend/Group card and support card restrictions (S3):** you cannot use a support card of the uma you are training; you cannot have two cards of the same uma in one deck (e.g. Special Week Speed + Special Week Guts); you cannot add the same card twice.

## 1.2 Bond and rainbow training

- Bond gauge runs 0-100 for every support card, plus the Director (Yayoi/Aoi) and the Reporter. Each 20 bonds = one segment (S1). Default gain is **+7** per training the card participates in; a hint event gives **+5** (S1, S3).
- 60-79 bond gauge is green, 80-99 orange, 100 is max (S1). **Rainbow (friendship) training** happens when a card has ≥80 bond AND appears on its own stat's training; it uses the card's friendship bonus (S1).
- (JP, S1) At 60 bond the chance of a card starting its event chain rises greatly, helping reach 80.
- Positive statuses Charming (bond gain up) and Sharp/Fast Learner (skill cost −10%) matter early (S1). ⚖️ Charming is worded as "+2 bond from all sources" (S1, JP) versus "+40% bond gain" (S3, GL).
- Reporter and Director bond is mostly irrelevant in newer scenarios; the snowball from lost rainbows and scenario mechanics outweighs it (S1). ⚖️ S7 (URA fan farming) goes further: only Kitasan's friendship matters until 80, then Speed and 2-3 Stamina trainings; other cards' friendship "does not matter" (secondary: Biko/Bakushin if used). S1 says bond every card to 80 in general.

### The two-phase flow (S1, S3 agree)
1. **Bonding phase:** pick trainings that maximise bond gain while managing energy. Use Wisdom trainings for energy so you can keep bonding with low failure risk. A hint on a card whose skill pool is relevant is worth more than an extra participant. Early scenario mechanics (if any) come first, or maximise stat/SP if mechanics are easy.
2. **Rainbow phase:** take rainbows; if none, train Wit or do races (S3 flowchart). Experience teaches when to accept risk, when rainbow beats bonding, when to raise mood.
- Some scenarios let you leave phase 1 early because bond can be gained elsewhere (e.g. Yukoma onsen tickets) (S1).

### End goals by era (S1)
- **URA / Aoharu:** hit as many relevant stat caps as possible (enough Stamina > Speed > Power > Wisdom) while getting enough SP.
- **Post-DYI:** squeeze out as much SP as possible; late Classic/Senior trainings pad and cap stats.
- **In between:** maximise the scenario's mechanics; rainbows give most stat gain. Capping all relevant stats is trivial in modern scenarios versus older ones (S1).

## 1.3 Training gain formula (S1 = S3)

`Gain = (Base + ΣStatBonus) × (1 + MotivationMult × ΣMotivationBonus) × ΣTrainingBonus × ΠFriendshipBonus × (1 + 0.05 × NumberOfSupportCards)`

- MotivationMult is 0 at neutral mood and ±0.1 per mood step. (S3 calls it MoodMultiplier / MoodEffect.)
- Friendship bonus only applies if the card is at orange bond or higher and on its matching training. Stat bonus only applies if that training normally gives that stat.
- S3: MANT uses the Unity Cup base-value table.
- **Worked example (S1):** Kitasan MLB: motivation bonus +30% turns +20% (max mood) into +26%; Training Bonus 5% (unique) + 10% (card) → ×1.15; Friendship ×1.25 → ×1.26 × 1.15 × 1.25 ≈ **+81%** vs base.
- Motivation Bonus is roughly worth Training Bonus ÷ 5 (S5).
- "Race Bonus, initial bond, specialty rate, stat bonus, friendship bonus" are the components of card power (S5); ranking of usefulness is in Part 3.

### Specialty rate (S1, S3 agree)
Each training has base weight 100; "not appearing" weighs 50. With no specialty a card appears on its own training 100/550 = 18.18%. Card specialty adds to the 100 (Kitasan: 80 base → 180); unique specialty multiplies (×1.2 → 216); her Speed rate is 216/666 = 32.4%. That is why she is quoted as **116**, not 100. S3 changelog (2025-07-27) states the JP community consensus is that 116 is right and that simple addition ("100") is a website display artifact.

## 1.4 Mood, energy and statuses

**Positive statuses (orange; last until lost) (S1, S3):**
| Status (JP / GL) | Effect |
|---|---|
| 練習上手○ / Good Practice / Practice Perfect ○ | −2% training failure |
| 練習上手◎ / Practice Perfect ◎ | −4% (S3: Narita Taishin only) |
| Super Creek's Shining Brightly (大輪の輝き) | reduces failure (S3, Super Creek only) |
| 愛嬌○ / Charming | bond gain up (see ⚖️ above) |
| 切れ者 / Sharp / Fast Learner | skill cost −10% |
| 注目株 / Rising Star / Hot Topic | more from certain NPCs; S3: +40% bond with Chairman and Reporter |
| Positive Thinking | prevents one motivation decrease |
| Lucky Constitution | prevents one negative condition |
| Smart Falcon: Promise to fans (ファンとの約束) | win in the listed location for extra stats + mood (S3; not on Global then) |

Uma-unique positives/negatives are run fluff and do not carry into PvP (S1).

**Negative statuses (blue) (S1, S3):** Bad/Poor Practice (+2% failure, from failing a training), Migraine (mood cannot rise), Dry Skin/Skin Outbreak (mood drops on its own; from doing several races in a row), Insomnia/Night Owl (−10 energy periodically; about 2% of rests), Overweight/Slow Metabolism (Speed cannot rise; from the 10 vs 30 energy food option; training can cure), Lazy/Slacker (may skip training; reporter cures). Non-unique ones are cured by Infirmary or by summer rest; some support cards cure statuses. Rule of thumb: don't waste a turn on the Infirmary; rely on scenario/card cures or restart (S1). S3 adds: Super Creek only: "Under the Weather" (higher failure) (text truncated in extraction).

## 1.5 Failure and outcomes (S1)

- **Fail rate table for the worst outcome:** failure 1-19% → worst outcome 0%; 20-79% → ~30%; 80-100% → 100%.
- **Event outcomes after a failure (JP):**
  - Top ("normal") option: −1 mood, −5 trained stat (~92%), or the same + Bad Practice (~8%).
  - Normal (worst-branch) option: −1 mood, −10 trained stat ~30%; same + Bad Practice ~55%; Good Practice ~15%.
  - "Worst" bottom option: −3 mood, +10 energy, −10 trained stat, −10 to 2 random stats (50%), or with no energy and Bad Practice (~97% / ~3% +10 energy + Good Practice).
- Extra training event after a successful training: 6%. Curing a debuff via the +5 stat/−5 energy option: 20% (S1).

## 1.6 Seasonal events and random events

**Summer camp (S1, S3):** early July (7月前半) of Classic and Senior year; 4 turns; Tazuna announces it two turns earlier. All trainings become **Level 5**; the infirmary is disabled (S1) / can't fix all illnesses (S3); resting cures 1 bad condition (less energy than normal). Arrive with full energy/mood and high bonds. It is the best time for big rainbows and to fix lagging Stamina, Guts or Wit.

**New Year (early January, twice) (S1, S3):**
| | Top | Middle | Bottom |
|---|---|---|---|
| First (Classic) | ⚖️ +25 to a stat (S1, JP) / +10 to a stat (S3, GL) | +20 energy | +20 SP |
| Second (Senior) | +30 energy | ⚖️ +8 all stats (S1) / +5 all stats (S3) | +35 SP |
Guidance: choose energy unless energy is full, then SP (S3 argues 30 energy is enough for a training and any good training gives >25 stats).

**Lottery / Raffle (late Jan of Senior; S3: after the second New Year you do one training then raffle) (S1, S3):** tissues (mood down) ~10%; single carrot +20 energy ~50%; bundle +20 energy, mood up, +5 all ~30%; carrot curry/Deluxe Hamburger Steak +30 energy, mood up, +10 all ~10%; onsen ticket +30 energy, mood up, +10 all, plus an extra bathing scene after winning the URA Finals ~3% (events sometimes double it). Don't be at full energy before it.

**Crane game (S1, S3):** possible after a date (25%), once a year (S1: from Year 2; S3: from Classic Year). Farm it with Urara or Mayano (a 25-day stretch of dates in year 2). Press and hold, release when the claw is over the target. Plushies further right more often carry extras; further left are easier to secure. Aim for the plushie's centre; upright ones are easier; golden sparkles mean extras. 6 small plushies, or 1 big + 2 small, is a big success; any plushie is a small success. Success: mood up, energy, skill hint.

**Acupuncturist Anshinzawa (10% per run; S1):**
1. +20 to all stats and mood up, or −15 all stats, mood down and insomnia (50%).
2. Straight Recovery + Corner Recovery learned, or −20 energy and mood down (60%).
3. +12 max energy and +40 energy, or −20 energy, mood down and Bad Practice (80%).
4. +20 energy, mood up, Charming; failure: −10 energy and mood down, or −20 energy, mood down, Bad Practice (90%).
5. +10 energy (100%).
Early run: pick 4 (Charming speeds bonding). Later: 2 for free recoveries, or 3 if short of energy with little free energy income. If you need nothing, pick 5.

## 1.7 Fan checkpoints and unique-skill levels (S1 = S3)

Year 3, to upgrade the unique skill:
- Feb 1H (Valentine's): **60,000** fans (Urara and Falcon: **40,000**).
- Apr 1H (Fan Meeting/Fan Fest): **70,000** (Urara/Falcon 60,000). President bond must be at least green (URA mode).
- Dec 2H (Christmas): **120,000** (Urara/Falcon 80,000).
Other checkpoints: Nov Year 2 with 50,000 fans, Aoi gives +20 Wit, +20 SP and a mostly useless gold skill. End of Year 2 with 100k fans → +30 SP; end of Year 3 with 240k fans → +30 SP.

## 1.8 Optional races and their effects (S3, S1)

- Fan-goal/race-count requirement is shown in the top bar; missing it fails the run (game warns several times).
- Race rewards on a win: **G1 +10 to a stat, +45 SP; G2/G3 +8 to a stat, +35 SP; OP/Pre-OP +5 to a stat, +35 SP**; 2nd-5th reduced; 6th or worse reduced again; all scaled by Race Bonus (S3). Turf win: 10% chance of a skill hint; Dirt win: 20% (chosen among track-relevant greens and random whites).
- Only take races where your aptitude gives two stars; the uma performs badly otherwise. Grey trophy in the top right means the race has never been won; each first win gives jewels.
- **Racing in a row (S3; mandatory objective races do not incur it, so you can race twice then a mandatory race with no penalty):**
| Any energy | 1st | 2nd | 3rd | 4th+ |
|---|---|---|---|---|
| Mood down | 0% | 0% | ~60% | 100% |
| + random stat loss (−10 to three stats) | 0% | 0% | 0% | ~40% |
| + Skin Outbreak | 0% | 0% | ~12% | ~33% |
| **No energy** | | | | |
| Mood down | ~20% | ~33% | ~95% | 100% |
| + random stat loss | 0% | 0% | 0% | ~40% |
| + Skin Outbreak | ~5% | ~10% | ~20% | ~33% |
- Reward checking in run: bottom-right menu trophy icon shows races done (S3).
- Race Bonus consequences (also see 3.2 in Part 3): every 10% RB = +1 stat from G1/finals; every 12.5% = +1 from G2/G3; 34% RB raises the +3-all after objectives to +4; 67% to +5 (S1).

## 1.9 Event odds (S1 JP; S3 GL notes)

- **Rest:** 70 energy 25%; 50 energy 62.5%; 30 energy 10%; 30 energy + Insomnia/Night Owl 2.5%.
- **Outing/Recreation:** Karaoke +2 mood 35%; Stroll +1 mood +10 energy 30%; Shrine +1 mood +10 energy 20%; Shrine +1 mood +20 energy 10%; Shrine +1 mood +30 energy 5%; crane game afterwards 25%.
- **Universal event** (+5 all stats, +2 mood): 40% per run; getting Sharp/Fast Learner from it: ⚖️ 5% (S1) vs 10% (S3).
- Overweight/Slow Metabolism from the +30 energy option: 10%; character-specific outcomes can guarantee it; curing it after a successful training ("diet success"): 10%.
- Lazy/Slacker when its event occurs: 6%; skipping a training: 25%; −1 mood when skipping ≈23%.
- Migraine event: 6% (S1 lists the same 6%).
- Insomnia −10 energy event: 25%; −1 mood alongside ≈23%.
- Extra training after success: 6%; friend-card post-training event: 40%; +1 mood from it: ~8%.

## 1.10 Career-run stamina checks and requirement notes

- **Hidden bonus (S3, S2):** in single mode (training) every uma gains **+400 adjusted stats** (S2 "Single Mode Modifier"; S3 says Career gives secret +400 Stamina and Guts, i.e. lower the PvP stamina table by ~600 in training).
- S3 FAQ "how do I win this race": the most common issue is Stamina; refer to the Required Stamina Chart (Part 2, 2.8) minus ~600 in training; if Stamina is fine, Power is probably the issue; make sure surface and distance are A or better.
- **URA fan-farm checks (S7):** Tokyo Yushun (Derby) needs ≥330 Stamina (else learn at least one white recovery). Tenno Sho (Spring) needs ≥480 Stamina + 1 gold recovery, or 600 Stamina, else do Milers Cup instead.
- **Skill buying for a run (S3):** pick one distance and one style you are A or better in; buy skills with that in brackets; unbracketed skills are fine; avoid uniques at the top of the list.
- Debuffs do not affect your own umas; debuffs stack; all skills stack, even same-name ones; skills bought work anywhere (S3).

## 1.11 Run rating, aptitude and benchmarks (S3 recorded example runs)

Builds recorded on the JP server for URA with weak cards (S3, target lines for reference; format Speed/Stamina/Power/Guts/Wit):
- **Sprint:** inherit Wit and some Stamina; target 1200/500/1200/300/500. With a +63 Power parent, inherit full power and try 4 Speed 2 Wit; if you can't get 500 Stamina 900 Power, stay with Speed/Power. King Halo is the hardest Sprint uma; borrowing a 9★ Stamina uma gives enough Stamina.
- **Mile / Dirt:** inherit Stamina; target 1200/800/900/300/400, or 1200/600/1000/300/400 + 1 gold recovery. A Stamina card can replace inherit if Power cards are lacking.
- **Medium:** inherit Power; target 1200/900/800/300/400 + Swinging Maestro. A full Stamina inherit plus Vodka for a recovery may also work.
- **Long:** inherit Power; target 900/1200/600/400/400 + 2-3 gold recoveries. The Mejiro McQueen story card is very useful.
- S3: in URA, don't run more than two card types in a deck (Pal cards aside, replacing a Speed with Tazuna/Aoi); Wit cards are very hard to use in URA unless whaling.
- Recorded runs: Sprint King Halo (4 Speed 2 Power), Mile Daiwa Scarlet (5 Speed 1 Power; the run inherited all into Stamina; her 20% Guts bonus is bad), Medium Winning Ticket (5 Speed 1 Stamina), Long Matikanefukukitaru (2 Speed 4 Stamina; 20% Stamina bonus; Good Condition green bought early for +40 Power), A+ Mile Oguri Cap with MLB SRs (4 Speed 2 Power, 2 tries; forgot Satsuki Sho), 3★ blue farm Tokai Teio (4 Speed 1 Guts 1 Wit; 600 in every stat for 3★ odds; only 16 races so affinity suffered; you get good gains from also doing the parents' races).
- S3: **when a stat reaches 1100 the chance of a 3★ blue doubles** (a note from the Teio run). See Part 4 for the blue-gene table (~5% 3★ for 600-1049, ~10-11% for 1100+ per S6).

## 1.12 Automatic training (S1, S6)

- **Auto-kun / おまかせ (JP):** orange button top right. Real time (keep the screen on); set most values to low; check the boxes to race when you need fans and use clocks when you fail. Not competitive, but good for parents, event points and filling Stadium (S1). Speed: as fast as 15 min (URA), 25-35 min (Ramen scenario) (S6).
- Extra fast skip option in the menu; in-game event viewer (button bottom-right of an event with choices) shows each choice's result (S1).
- **Reroll sparks** at the end of a run (costs TP), keep either result (S1, no downside except TP; don't spend jewels).
- **Expeditions** (suitcase button) generate event points without runs (S1).
- **Background auto (JP 30 Jun 2026, Global early Jul 2026; S6):** runs a fixed 50 minutes in the background, usable in **every** scenario; cannot fail, objective races that end the run when failed are auto-won; other races use aptitude-based odds not stats; cannot be interrupted; usually gives worse wins than auto-kun on long race stretches. Odds start at 110% for A/A (S/A the same); lower per aptitude below A and per consecutive race from the 4th turn. Sample (A ground / A distance): under 3 races 100%, 3rd 100%, 4th 85.7%, 5th 75.2%, 6th+ 58.9%; (A/B): 100 / 92.4 / 76.7 / 72.1 / 54.8; (A/C, small sample): 90 / 70 / 60 / 50 / 36.5; (A/D): 80.9 / 62.5 ...; G ground/distance mostly 0%. Umas that win with a kit despite low aptitude are underestimated. Non-objective races follow the same odds as Green Ticket/inheritance-only umas.
- **Recommended usage (S6):** auto-kun for consecutive race stretches (better compatibility and saves clocks); background auto to watch bond stories/live theatre, or for parents in no-fuss situations.
- Do not use auto for decks, parents or PvP teams (S1, S3).

## 1.13 Training-run scoring and rank (S1)

- Unique skill level gives **170 points per level** (**120** per level for a 1-2★ uma). A level 6 unique = +1050.
- Every skill has a point value multiplied by **1.1** if you are A/S in the related strategy/distance, **0.9** for B/C, **0.7** for G, **0.8** for other; no association = ×1.0. Purple skills reduce score: −129 (cost 50) or −262 (cost 100), useful for A+ builds in Open League CM.
- Base skill values (from the S1 table, extraction partial): white 129-ish; ◎ 174; gold 461-559; evolved 508-696; concentration 394 (evolved 461); vision skills 94 (Hawkeye 142; gold/evolved 367/433). Inherited uniques: 180 (Vive la GOLD 198). Unique-derived values for Dual skills 263.
- Stat→points: 300→352, 400→577, 500→847, 600→1143, 700→1463, 800→1808, 900→2209, 1000→2653, 1100→3171, 1200→3841 (gain per +100: 225, 270, 296, 320, 345, 401, 444, 518, 670).
- Rank thresholds: G <300; G+ 300; F 600; F+ 900; E 1,300; E+ 1,800; D 2,300; D+ 2,900; C 3,500; C+ 4,900; B 6,500; B+ 8,200; A 10,000; A+ 12,100; S 14,500; S+ 15,900; SS 17,500; SS+ 19,200; UG 19,600; UF 23,900; UE 28,800; UD 34,400; UC 40,700; UB 47,600; UA 55,200; US 63,400; US9 71,400+; LG+ ??. Calculators: umsatei.com and yonkim.azurewebsites.net.

## 1.14 Fan farming in URA (S7 in full)

**Aim:** meet a circle's daily/monthly fan quotas. (Circles rank by monthly fan gain; serious circles set requirements like 30,000,000 fans/month, tracked by leaders' spreadsheets (S1).) URA is still faster and easier than Unity Cup for farming; the half-anniversary balance patch and Unity Cup release changed nothing except the option to run a Falco SSR (15% FB at MLB) in a groundwork-parent/fan hybrid (S7).

**Concept:** maximise "Fan Bonus". Rule of thumb: higher Race Bonus = higher Fan Bonus; every 20% FB card (the highest in the game) has ≥10% Race Bonus (e.g. MLB Manhattan Cafe (STM), MLB Daitaku Helios (PWR)). The example decks are those with the author's personal highest fan runs; any card can be replaced by one with similar FB.
- Kitasan Black has only 15% FB but is kept in decks because she gives the highest race win rate; with MLB Bakushin, Biko or Kawakami Princess you can replace her.
1. **115% FB**, inherit mostly Stamina + some Power: reaches 600/600/600 SPD/STM/PWR easily on any uma with the highest win rate: allows 3★ spark farming. (MLB Biko can be replaced with MLB Sakura Bakushin O or MLB Kawakami Princess.)
2. **120% FB**, inherit full Stamina: budget version requiring only SR cards but sacrificing win rate; strong on an uma with a 20% growth rate in Speed; can consistently hit 600/600/600/x/600; may fail Tenno Sho (Spring) due to a lack of stamina and recovery skills.
3. **115% FB**, inherit mainly Stamina + some Power: lower win rate (especially on umas with no Speed growth) but still reaches the Tenno Sho (Spring) stamina requirement.
4. **110% FB**, inherit mainly Stamina + some Power: groundwork parent (e.g. Seiun Sky parent) while farming; SSR Falcon gives guaranteed groundwork on the first chain. Replacements: MLB Satono Diamond ↔ Manhattan Cafe; Sakura Bakushin O ↔ Biko or Shinko Windy.
- **20% FB cards usable as replacements (MLB):** Sakura Bakushin O SSR (SPD), Kawakami Princess SSR (SPD), Satono Diamond SSR (STM), El Condor Pasa SSR (PWR), Fine Motion SSR (WIT), Winning Ticket SSR (GUTS), Shinko Windy SR (SPD), Mejiro Ryan SSR (GUTS), Sweep Tosho SSR (SPD), Ikuno Dictus SSR (GUTS), Tamamo Cross SSR (PWR), Riko Kashimoto SSR (FRIEND).

**Aptitudes to bring to at least A by inherit:**
- **Turf:** most URA races are turf; only bring a Dirt uma if you can raise Turf to A.
- **Mile:** no big Mile fan races, but not being able to run Mile loses ~200k fans at 120% FB.
- **Medium:** by far the most important; ≥ half of your total fans.
- **Long:** Arima Kinen (Classic + Senior) alone is up to 150k fans; Tenno Sho (Spring) is a bonus if stamina allows; some risky routes need long G2s.
- **Sprint:** optional (+15,100 base fans ≈ 33k at 120% FB). **Dirt:** optional and only for a risky route; can be a bait that tanks win rate; B or even C is enough.

**Who to farm with:** Front Runners, because most career losses come from being blocked. ⭐ = 1M+ fans reached; □ = untested. Maruzensky (Original)⭐, Silence Suzuka⭐ (most consistent if Long A: Focus/Concentration + 20% Speed growth), Oguri Cap⭐ (needs many risky wins, 8+ in a row, plus dirt; forced Mile Championship Nov 1 of Class Year loses ~33k fans), El Condor Pasa⭐, Daiwa Scarlet⭐, Mihono Bourbon⭐, Seiun Sky⭐, Grass Wonder⭐, Gold Ship⭐, Mayano Top Gun⭐, King Halo, Biwa Hayahide, Rice Shower, Mejiro Ryan, Matikanefukukitaru, Nice Nature, Agnes Digital (needs many long sparks), and □ Symboli Rudolf, Narita Brian, Hishi Amazon, Gold City. All Turf umas can be great farmers; only those needing few distance sparks are listed.

**General race route (S7):** includes multiple 3+ in a row races; adapt to your uma and risk; if not confident, don't do 3+ in a row. In general winning 2 races gives more fans than winning 1 and losing 2.
- *Junior:* Nov 1 Daily Hai Junior Stakes (Mile); Dec 1 Asahi Hai Futurity Stakes (Mile); Dec 2 Hopeful Stakes (Medium).
- *Class:* Mar 1 Yayoi Sho (Medium); Mar 2 Spring Stakes (Mile); Apr 1 Satsuki Sho (Medium); May 1 NHK Mile Cup (Mile); May 2 Tokyo Yushun/Japanese Derby (Medium; first minor stamina check, need 330+ else a white recovery); Jun 1 Yasuda Kinen (Mile; sometimes skipped if summer training is needed, else 4 races in a row); Jun 2 Takarazuka Kinen (Medium); Aug 2 Sapporo Kinen (Medium); Sep 1 Centaur Stakes (Sprint; without Sprint B do Rose Stakes or skip a turn); Sep 2 Sprinters Stakes (Sprint) / All Comers (Medium; All Comers if no Sprint B); Oct 2 Tenno Sho (Autumn, Medium); Nov 1 Queen Elizabeth II Cup; Nov 2 Japan Cup; Dec 1 Champions Cup (only with Dirt B); Dec 2 Arima Kinen (Long).
- *Senior:* Jan 2 American JCC (Medium); Feb 1 Kyoto Kinen (Medium); Feb 2 February Stakes (Mile, only with Dirt B); Mar 1 Kinko Sho (Medium); Mar 2 Osaka Hai (Medium); Apr 2 Tenno Sho (Spring) (Long) / Milers Cup (Mile) (Spring can be a bait: need ≥480 Stamina + 1 gold recovery or 600 Stamina, else Milers Cup); May 1 Victoria Mile; Jun 1 Yasuda; Jun 2 Takarazuka; Aug 2 Sapporo; Sep 1 Centaur (skip if no Sprint B+); Sep 2 Sprinters/All Comers; Oct 2 Tenno Sho (Autumn); Nov 1-2 QE II, Japan Cup; Dec 1 Champions Cup (Dirt B); Dec 2 Arima Kinen.
- **Maruzensky-only route:** *Junior* Nov 1 Daily Hai Junior; Dec 2 Hopeful. *Class* Mar 1 Yayoi; May 1 NHK Mile; Jun 1 Yasuda (optional); Jun 2 Takarazuka; **Jul 1 Radio Nikkei Sho** (only for Maruzensky: winning triggers her secret event with Hot Topic and +2 mood, useful for the risky route since mood tanks after 4-5 races in a row); Aug 2 Sapporo; Sep 1 Centaur; Sep 2 Sprinters; Oct 2 Tenno Sho (Autumn); Nov 1 QE II; Nov 2 Japan Cup; Dec 1 Champions Cup (Dirt B). *Senior* Jan 1 Nikkei Shinshun Hai; Feb 1 Kyoto Kinen; Feb 2 Nakayama Kinen (or February Stakes with Dirt B); Mar 1 Kinko Sho; Apr 2 Tenno Sho (Spring)/Milers Cup (same stamina rule); May 1 Victoria Mile; Jun 2 Takarazuka; Sep 1 Centaur; Sep 2 Sprinters; Nov 1-2; Dec 1 (Dirt B); Dec 2 Arima Kinen.

**Tips (S7):** Year 1: reach 80% Kitasan bond ASAP, then Speed + 2-3 Stamina (Biko/Bakushin bond secondary). Learn skills as you go (general and style skills first, ignore distance-specific unless it is the only option; then Medium, then Mile/Long; Sprint skills can be ignored). **Use Seiun Sky as parent and take her unique ASAP**: it lets any uma comfortably run Front Runner even with G in that aptitude and drastically raises G1 win rates (all but 2). Get Focus/Concentration early: it reduces blocking.

**Min-maxing a run (S7):** for screenshots only; it takes longer and gives fewer fans/hour. Example: Suzuka ~1.05M fans with 37/37 wins meeting 600/600/600; stretching to 44-47 races gains ~80K (~1.13M total) but takes much longer and likely misses spark-farming stats. Year 3 races every turn; years 1-2 follow the standard schedule. Only min-max if you enter Year 3 strong enough to beat the URA finale (e.g. 700/500/500 yes; 500/300/400 no).

## 1.15 Rerolling, first month and account setup (S1, S3, S5)

- **Reroll** at the start: it's fast; you don't need to redownload; spend all on support cards. If the banner uma is one you love you can try for both. If unsatisfied, return to title and delete account data. Ideal: banner card at 1LB+ (~20 pulls on average) then farm runs to clear races for Carats (S3). ⚖️ Free-roll windows: S1: scenario launches (~every 4 months), anniversaries 24 Feb and 24 Aug, and New Year in December; S5: Anniversary (end of Feb), Half-anniversary (end of Aug), New Years (beginning of January).
- S5 reroll targets: strong Speed/Wisdom SSRs already strong at 0-1LB; 1 speed card from the list + another from the list or decent SR speed cards; multiple copies are great but rare; reroll when a strong card is on the current banner; spark the featured banner (200 rolls) after the initial reroll for more copies.
- **First month checklist (S3):** reroll; level only cards you use (limited resources); read basic training strategy; add friends with good parents; win every graded race once; mark 3★ blue or 2★ blue + 3★ pink umas as protected parents; pull to pity if you rerolled on the current banner (200 total pulls); 30-50 uma rolls to collect 1-2★; save for a spark (30,000 jewels; two sparks ≈ 50/50 to MLB an SSR); train one uma per Team Trials distance (Bakushin Sprint, Vodka Mile, Daiwa Medium, Gold Ship Long, Urara Dirt); clear main story for free SSRs; join a Club for shoes→Club Points; finish missions then use random tickets then the 3★ pick ticket (Oguri, Maruzensky, Taiki); fill Team Trials slots weekly; use Friend Points for Urara copies; prepare umas for CM/LoH (rewards even when losing).
- **Tips (S1, S3):** reroll on strong cards, pull in multiples of 200 (ideally 400+), save pink tickets (≈150 jewels each; ~200 of each type per year), save the 3★ pick ticket until missions are done, join a Circle/Club, borrow parents (JP parents are extremely high quality), welfare cards can shore up a deck, use auto only for training, make a Link Password, connect to the Cystore (300 jewels).
- **Coming from Global (S1):** wait for a free-pull event to reroll; then save jewels for the next scenario banner; play the latest scenario for competitive umas; use the rental decks (rental borrow slot is usually the scenario's mandatory friend card); Global and JP save to the same place on PC, so use an emulator for both. Free-roll events happen at least every 4 months.
- **Link Password / Cygames ID (S1):** create early; link a Cygames ID (300 jewels).
- **JP 5th-anniversary QoL (S1):** in-game event viewer, extra fast skip, Expeditions, Daily Legend Races.

