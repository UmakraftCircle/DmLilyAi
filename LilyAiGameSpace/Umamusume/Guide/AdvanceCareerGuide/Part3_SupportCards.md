# Part 3: Support Cards, Decks and Card Economy

Master index and conflict register: `AdvanceCareerGuide.md`. Tags: S1 JP Reference, S3 Global Reference, S5 celery6305 card evaluation (JP meta, Yukoma Hot Springs parameters, PvP-oriented, cards scored at MLB), S7 fan-farm guide. S4 (Luh's encyclopedia) had no extractable content, so nothing from it appears here. ⚖️ = sources disagree.

## 3.1 Card passives

- **Friendship Bonus (FB):** multiplies training when the card is rainbowing (orange bond and on its own training).
- **Training Bonus (TB):** multiplies every training the card participates in (cross-training).
- **Motivation Bonus (MB):** multiplies the mood effect (Mood Multiplier) for trainings the card is on. In value MB ÷ 5 is roughly an equivalent TB (S5). Example (S1): Kitasan MLB +30% MB turns +20% mood into +26%.
- **<Stat> Bonus:** +1 to that stat's base gain before all multipliers, only on trainings that normally give that stat (S1, S3). A Speed bonus on a Speed card works on 3 trainings (Speed, Power, Guts trainings give Speed) so it is very strong (S5). SP bonus is "also amazing"; offset (secondary stat) bonuses are decent (S5).
- **Specialty Rate:** weighting of the card's appearance on its own training (see Part 1, 1.3). Initial ~35 matters a good amount; beyond ~50 quickly becomes less important (S5).
- **Initial bond / Starting bond:** speeds up reaching rainbow (0-bond cards like Urara, Mayano Top Gun SR/SSR, Matikanetannhauser, Ikuno Dictus, etc. can grief a run when they fail to bond).
- **Initial <Stat>:** added at the start of training; saves a day or two of training and is especially useful on card types you bring 1 or 2 of, e.g. Power cards in a 4-Speed 2-Power deck (S3).
- **Hint frequency:** increases the chance of hint "!" on the card; each hint = +5 bond, so it also gets rainbows sooner and unlocks the card's skills (S3).
- **Hint levels:** increases discount on the skills it hints (saves SP if you would buy them anyway; S5 notes you effectively "gain" SP from discounts on skills you'd buy, e.g. Ramonu).
- **Wisdom (Wit) Friendship Recovery:** on Wit and later Group cards: when there is a rainbow on Wit training it restores extra energy (4 for MLB SR, 5 for MLB SSR, except Ikuno SR has none) (S3, S1: ~4-5 at MLB).
- **Race Bonus (RB):** boosts stats and skill points from finishing races, including the mandatory +3 all stats and the URA +10 all stats. No rounding: to go from +3 all to +4 all you need 34% RB (S3); on most umas going from 33% to 34% would be +10 all stats (S3, likely refers to the URA finals or similar breakpoints).
- **Fan Bonus (FB2):** bonus to fans gained (S3: usually ignorable except for umas with early fan checkpoints; S7: central to fan farming, see Part 1, 1.14).
- **Friend/Pal card passives (S1, S3):** multiple Pal cards cannot appear on the same training so they do not stack. Failure Protection (35% turns 9% into ~6%), Energy Cost Reduction (20% turns 25 into 20), Event Recovery (more energy from events, notably dates), Event Effectiveness (more SP/other event rewards).
- **Gold skill rate ("agemasen"):** some cards only have a chance to give the gold skill at chain end; chance depends on your stat of the card's own type: <400 30%; 400+ 60%; 600+ 65%; 700+ 75%; 800+ 80%; 1000+ 90% (S1 = S3). ⚖️ S1 (JP, 5th anniversary): modern cards no longer "agemasen"; the outcome now affects the event result instead; S3 (Global) still lists it as a chance for older cards (e.g. Fine Motion giving Speed Star or its white version).

## 3.2 Race Bonus breakpoints

- Every 10% RB gives +1 stat from G1 and final races; every 12.5% gives +1 from G2/G3. The first value divisible by both is 50%. In Trackblazer (MANT) the ideal is 50% (+5 G1, +4 G2/G3), and its last-three-race hammers multiply by 1.35 (S1).
- In other scenarios: +3 all stats after objectives becomes +4 at **34%** and +5 at **67%** (S1). Max per card is 15% (JP), so a full deck could reach 90% (S1). S1 says URA/Aoharu builds should reach ≥34%.
- S3 table for a URA-like run: RB 0% → 351 stats/870 SP; 5% → 351/906; 10% → 372/946; 15% → 372/991; 20% → 393/1044; 25% → 393/1080; 30% → 414/1123; 35% → 461/1165; 40% → 482/1218. The jump is at 34%.
- ⚖️ Importance: S5 says race bonus is "not important" for YHS but ≥34% "gives a minor boost"; breakpoints are excluded from card scores but worth ~25 score points to a card that lifts you over 34% (example: 5% RB vs 10% RB card). S7 (URA fans) says higher Race Bonus is central because it correlates with Fan Bonus. S1: URA/Aoharu should reach ≥34%. S5 also notes L'Arc gives fewer stats from races (so the missing RB on Eishin Flash/Bourbon "is not a big issue in L'Arc").

## 3.3 How S5 scores cards (methodology and caveats)

- Ratings come from S5's own tool, aimed at PvP stat gain on the **JP** meta; since 15 Jul 2025 (after the Design Your Island scenario) S5 uses a generalised scenario model rather than accurate scenario mechanics; parameters (race stats, scenario stat bonuses, meta decks) are still adjusted per scenario. Pros: less coding, fairer to future scenarios, maybe better for Global. Cons: doesn't reflect scenario-specific strengths (e.g. Pasa Speed SSR with DYI's +all stats bonus).
- Why: DYI was overbuffed and gave too many stats, so card strength matters less there; pick cards by **skills** (as has been the case for years).
- The tool evaluates average stats given weighed over every combination of trainings a card can land on, weighted by probability; the "best training" for each situation is chosen using stat weights; the results are multiplied by the situation probability, summed and multiplied by turns in that phase (6 phases from early bonding to late game). Energy/failure is not simulated; a number of turns are reserved for rest/dating/objectives; total energy from training and events affects score. Race and event stats count; initial bond affects rainbow chances in phases 2-3 somewhat; race bonus gains have no rounding.
- Each card is compared with **5 fixed strong companion cards** from meta decks; weaker/low-LB cards are therefore slightly less accurate.
- "Cards within 20-40 score are practically equal; choose by skills, since skills matter more for PvP."
- Ranking of bonuses by how much they raise stats (S5, normalised to what the game considers equal): 1) flat stat bonuses (esp. Speed bonus on Speed cards; SP bonus; offset bonuses decent), 2) Training/Motivation bonus (MB÷5 ≈ TB), 3) Friendship bonus, 4) Specialty rate, 5) Race bonus, 6) other bonuses like initial stats.
- Friend/Group cards are excluded from the evaluation ("Fuku Speed SSR" and similar friend-like cards too); each scenario typically has a must-use scenario friend/group card (3.9).
- Cards not ranked: forgotten or too complicated. The author's credentials (S5): plays daily on JP since Sep 2021, "undefeated in mid/long CM finals since June 2022", top-96 list in LoH once, low spender.
- Card categories in S5 also carry a "Current card meta (YHS)": 1-2 top cards used in all decks, 1 used most of the time, 1 used always, 1 used sometimes, etc. (icons only; the extracted text does not name them).

## 3.4 Card investment order and limit breaks

- Order when short of cards: **Speed → Wisdom → Stamina/Guts** (S1, S5). Speed and Wisdom SSRs are usable in almost every build; other types are more situational (S5).
- Cards grow with copies (up to 5 including the first) via limit breaks (LB): 0LB-4LB (MLB = max limit break = 4LB, for now) (S1, S5). Generally MLB SR cards beat 0LB SSR cards; 0-1LB SSRs are rarely stronger than SRs; some SSRs are good at low LB (an exception, not the rule) (S5). Consult the score spreadsheet by LB (S5; not extractable).
- Level up only the cards you actually use (S3). Don't buy from random shops except clocks (S3).
- **Selector/crystal use (S1 FAQ):** "Should I use my crystal/selector on X? Most likely no. If the card is relatively new (<1 year), a top-tier meta card and will be used at a relevant LB (3LB+), consider it; if unsure ask."
- **Limit Break crystals (S1):** yellow crystals for SR, rainbow for SSR; 20 fragments = 1 crystal at the shop; fragments come from events (4-6 per month, so a crystal every 4-5 months).
- **Card-related restrictions in deck building (S3):** can't use the card of the uma being trained; can't have two versions of the same uma; can't add the same card twice.

## 3.5 Card write-ups by type (S5, text notes only; score images did not extract)

### Speed cards
Ranking notes: **Still in Love** is slightly better in practice than her score neighbours because she gives more SP and SP is more valuable than pure stats (already accounted for in weights, though S5 can't raise the SP weight further "just for one card").
- **Tokai Teio:** very strong leader-specific card; strong early leader speed boost; a choice of a final-leg skill or a mid-distance accel for leaders.
- **Almond Eye:** universal Speed card with stronger bonuses and skills than earlier releases; choose two gold skills out of four: either a pair of good mid-distance leader skills or two universal speed skills.
- **Admire Groove:** mid betweener-specialised; gives a nice accel gold for them and a general-use betweener gold.
- **Still in Love:** well-rounded; strong mid-distance gold or a good but slightly unreliable gold for betweeners/chasers; bonuses very SP focused ("ideal for strong PvP builds").
- **Rhein Kraft:** mile speed specialist aimed at frontliners: two frontline mile golds including the accel High Voltage; balanced stats.
- **Dream Journey:** chaser-specialised; rounded bonuses; only suitable for chasers; two chaser golds.
- **Narita Brian:** very strong for stats; skills leader-only so not universal; gives the long leader gold accel Monster and a strong leader midleg skill that spends some stamina.
- **Smart Falcon:** very strong runner specialty; gives an opening-leg accel gold for runners plus good runner skills.
- **Vivlos:** stacked bonuses all round ("2024-style powercreep"); universally useful with a gold version of the Speed skill Hold Your Tail High; main benefit is high stat gains.
- **Seeking The Pearl:** short-distance backline speed card, not noteworthy.
- **El Condor Pasa (speed):** very loaded; unique gives +1 all stat bonus at 100 bond; slightly lower race bonus but +2 SP total (good for SP gain); universal gold Arcline Professor; also a leader/betweener accel gold for a few tracks.
- **Jungle Pocket:** very high bonuses everywhere; 10 race bonus and 1 SP bonus (amazing SP gain); unique gives +3 Speed bonus at max bond (easy to cap Speed); mid/long/backline skills.
- **Duramente:** incredibly high specialty at 120 and very good cross-training bonuses; slightly lacking Speed/SP bonus but "insane chain events" compensate; gold skill **Never Give Up** is an amazing general-use gold for every strategy and distance.
- **Sakura Bakushin O:** short-distance specialist; up to +3 Speed bonus; lacks cross-training compared to Maruzensky; borrow her when you can afford to in short runs.
- **Maruzensky:** highest cross-training bonuses among Speed cards; unique gives 5% training bonus per level of training; staple in all runner decks (strong runner hints and gold **Top Runner**).
- **Mejiro Dober:** mile backline card, not amazing for stats but very front-loaded so usable for beginners; not otherwise notable.
- **Mejiro Palmer:** very strong for Speed **if** you activate her unique by buying 3 recoveries; usually not realistic, so overrated in S5's ranking (S5 assumed 3 recoveries bought early; with no recoveries she is around Pasa SR level; also very Speed-focused); if achievable the high specialty gives very high SP gain; 10 race bonus, 1 SP bonus, no power bonus; good long/runner skills.
- **Marvelous Sunday:** very high bonuses all around: 15% training bonus at max bond plus +1 Speed/Power/SP bonus; very similar to Kitasan Black but +1 Speed/SP over Kitasan at the cost of lower specialty; one of the few Speed cards with a gold recovery but too niche in skills.
- **Eishin Flash:** great stats especially the +Speed/+Power bonus and +1 SP (out of these, +1 pow/+1 SP come at 80 bond from her unique); no race bonus (fine in L'Arc); decent betweener skills.
- **Kitasan Black:** lower ranked now but was a staple due to super consistent rainbows and universal skills like Arcline Professor; still great for newer players.
- **Taiki Shuttle:** solid, almost every relevant bonus (2 Speed, 1 Power, +1 SP, 10% TB, 5% RB); gives strong mile skills (Ruler of Mile gold) for mile frontliner builds.
- **Honourable mentions:** Tosen Jordan (SR, very good), Agnes Tachyon (leader builds).

### Stamina cards
Note: Stamina card ranking is odd: long builds need pure Stamina gain while short/mid builds may want cross-training bonuses. Caveats: **Mayano** has 0 starting bond (lower in reality); **Palmer** assumed 15% TB; **Laurel**: S5 assumed you buy 3 recoveries early (Year 1-2) even though that's not usually realistic; **Ikuno** has 0 specialty but higher bonuses elsewhere (cross-training, race bonus), can be annoying due to inconsistency, "unless highrolling recommend Creek/Dia/Cafe"; **Tamamo** is similar with lower stats. Spreadsheet has the rest.
- **Fenomeno:** long leader stamina card; long random accel gold for leaders plus a late midleg gold.
- **Inari One:** long betweener; long accel gold for betweeners plus a midleg gold.
- **Gold Ship:** long chaser; chaser accel Imminent Shadow plus a chaser heal gold.
- **Air Shakur:** universally strong statline, further enhanced by the scenario link effect; a very good universal recovery+speed skill or a final-leg current speed skill (worse unless you're at the front of the pack).
- **Mejiro Ryan:** mid betweener; strong already at low LB; mid betweener gold from the first chain event.
- **Sounds of Earth:** all-round the second-best stamina card at the moment; good cross-training, good stamina, very high SP gain; gold recovery or gold speed as choices.
- **Curren Bouquetd'or:** leader specialty with a gold heal; not noteworthy.
- **Duramente:** chaser-specific stamina card with two chaser midleg golds.
- **Tanino Gimlet:** very high cross-training and especially good for Guts training; particularly mid-distance oriented (no stamina bonus, low friendship); nice mid-distance skills and a gold for mid backliners.
- **Dantsu Flame:** frontline version of Gimlet; mid distance; strong gold for mid frontliners.
- **Hokko Tarumae:** good all-round and great dirt skills; a spot in most mid dirt builds, otherwise not needed.
- **Ikuno Dictus:** ranked very high due to amazing cross-training (unique gives up to 20% TB) and race bonus; inconsistent as she lacks specialty; her betweener gold is very strong but drains a lot of stamina; great for highrolls, often ideal for CM builds.
- **Super Creek:** one of the older cards still great: 15% TB and 10% RB; gold recovery **Arc Maestro** works universally; a fine option when you need to survive a high stamina requirement.
- **Satono Diamond:** similar to Creek but more Guts gain; her recovery skill is less consistent; rarely used.
- **Honourable mentions:** Mejiro McQueen (lower than Creek but her skills are much better for long distance; higher long PvP potential if you can accept the stat loss), Mejiro Palmer (one of the only cards giving the runner opening-leg accel gold; useful in runner builds lacking it), Symboli Kris S (long-distance betweener accel gold; mostly replaced by Manhattan Cafe int), Yaeno Muteki (SR, very strong), Mayano Top Gun (SR, 0 bond but high bonuses; decent for highrolling).
- **El Condor Pasa (SR):** +1 Spd/Pow bonus; Shinko Windy and Sweep Tosho are fine alternatives.

### Power cards
Note: Power as a category "kind of sucks" for scores, you click it out of necessity since Power is a very good stat. Some power cards are for longer distance builds with stamina bonuses; for shorter distances Stamina is less important so take note of actual bonuses and skills, not just score. Caveats: **Agnes Digital SSR** unique requires 5 cards of different categories (S5 assumed it holds to be fair); **Biko** unique gives training bonus based on your max energy threshold (varies by deck/scenario); **Haru Urara** is not added (annoying unique; worthless anyway).
- **Special Week (S5 lists it here for the gold "Nonstop Girl"):** very strong accel skill for most mid/long tracks for runners.
- **Tamamo Cross:** for mid/long and backline builds; especially useful in DYI; gold choice of Divine Speed (universal speed boost) + either a midleg mid/long speed boost or a backline midleg speed boost.
- **Vodka (mid betweener version):** very strong in pure stats and raising Power, only +1 bonus; two golds (one betweener, one mid).
- **Mejiro Ardan:** very desirable for +2 SP and strong statline; leaders and mile/mid frontline; lacks skills for backliners unless the meta is backline-heavy.
- **Nishino Flower:** generic-use power card with very strong stats; the first card that can gain up to 30% training bonus in total; short/mile gold choice and a generic midleg gold for frontliners.
- **KS Miracle:** very balanced; short-distance power card; the leader accel gold she gives is almost a necessity in leader builds for shorter distances (also listed under Guts).
- **Seiun Sky:** mid-distance runner specialist; high stats with +2 Stamina bonus; limited use; close to Nishino Flower in evaluation but much lower in practice since Stamina is less important when you bring Power cards.
- **Espoir City:** dirt-specialised (2024 version of Wonder Acute) with lots of Stamina bonus; gold skills are a speed green and a recovery+speed skill; only good for something like mid dirt events.
- **Winning Ticket:** good for betweeners and needs few limit breaks; strong final-leg betweener gold; also gives the betweener accel Switch-Up Pro (great for short/mile).
- **Tsurumaru Tsuyoshi:** good overall stat gain and high power with its power bonus; skills not amazing enough in a meta where power cards aren't doing so hot.
- **Wonder Acute:** dirt specialist; weaker for shorter distances due to +2 Stamina bonus.
- **Vodka (power-optimised version):** bonuses focused on high Power and lots of power rainbows; very good ranked on power gain, less good for other stats; a universal gold recovery makes her possible for longer builds.
- **El Condor Pasa (power):** older card that has stood the test of time with its high bonuses, especially 10% race bonus; gold **Killer Tune** (great mid-distance runner/leader skill); can't be used together with Speed Pasa.
- **Hishi Amazon:** strong cross-training but not as good at raising Power; main use is getting the gold Straight Shot for chasers lacking it (via maximum discount hints on a few good chaser skills).
- **Admire Vega:** decent cross-training at 20% TB and 10% RB; the amazing chaser gold **Daring Attack**.
- **Honourable mention:** Daiichi Ruby (weak; short/mile backliner gold; decent for debuffer builds).

### Guts cards
Note: Guts isn't the most important stat to pad, so choose by skills. **Urara** is the go-to card for newbies: free, good stats (at the cost of no good skills and low starting bond).
- **Stay Gold:** universal guts card with decent stats; slightly lacking cross-training; useful skill spread including two good golds.
- **Fine Motion:** really good stats, basically the 2024 Urara Guts; but its gold is only useful for mid-distance frontlines and really only in exactly 2000m races; niche.
- **Hishi Amazon:** chaser-specialised; generically good chaser gold; quite niche uses.
- **Orfevre:** very strong versus earlier guts cards; unique gives +1 bonus at 80 bond for every card type in the deck (2 speed/2 guts/1 int/1 friend deck → +2 Speed +2 Guts +1 Int +1 SP); gold **Divine Speed**; very usable anywhere you need a guts card.
- **Silence Suzuka:** runner guts card: a generic runner speed gold or a mid-distance accel for some tracks.
- **Curren Chan:** not top stats but amazing skills for short-distance frontliners: Concentration or a leader short accel.
- **Blast Onepiece:** another leader-specialist guts card, decent skills.
- **Fuji Kiseki:** leader-specialist; always good as a second guts card in a leader deck.
- **Haru Urara:** "love it or hate it" welfare card, absolutely stacked bonuses except initial bond: amazing cross-training, 10 race bonus, high friendship bonus, +1 SP; great for highrolling big stats; no good skills; low bond can grief training; "the best welfare card ever printed".
- **King Halo:** great for short-distance backliners due to golds; fairly highly rated for good total stat gain, focused on Speed (up to +3 Speed bonus), +2 Guts bonus, lacking offstats.
- **Tap Dance City:** premium runner guts card; lacks hint bonuses but potent for high stats; unique gains training bonus per Speed skill bought (up to 3); Runaway and Escape Artist are gold skills for runners.
- **Gold City:** strong for raising Guts (+3 Guts bonus at max bond); starting bond helps; +1 Power bonus desirable; lower cross-training and race bonus; really good mile skills and a choice of a summer speed green and a very good mile accel gold mainly for frontliners.
- **Mayano Top Gun:** similar bonuses to Pasa but lower race bonus and SP bonus instead; solid; gold **Nonstop Girl** (acceptable for some mid/long builds).
- **Admire Vega:** 20% TB and 10% RB as above; SR version: highest SR in this list due to 15% race bonus.
- **Symboli Rudolf:** solid bonuses all round (2 Speed, 1 Power, and 2 ...); Arc Maestro universal gold recovery; more suited to long builds so less commonly used.
- **Ikuno Dictus:** 15% race bonus and very strong events; lots of Stamina, so don't overrate her high placement since Stamina is often unimportant in short/mile where guts cards see more play; her gold is useless outside stadium PvP.
- **KS Miracle:** staple in short/mile leader builds.
- **Honourable mentions:** Ines Fujin (old but still very good; consistent guts rainbows, good cross-training, outdated events; good hints; a good runner recovery gold that works on most tracks), Winning Ticket (Switch-Up Pro betweener accel; usable at low LB), Admire Vega (SR).

### Wisdom cards
Note: Ikuno has lots of Speed bonus so she is not as good for pure stat chasing unless you run 1 Speed card, but she gives good mile hints; int cards should be chosen mainly by skills since stat differences among top cards are negligible.
- **Daring Tact:** betweener specialty; very strong stat gain, esp. rainbows and SP (+2); two betweener golds at once.
- **Win Variation:** long-distance int card that works on all strategies; two long golds at once.
- **Symboli Rudolf:** very rounded stats; a really good selection of skills including a universal gold (slipstream gold) and, as another option, the leader/betweener accel **Oute** (works on a select few tracks).
- **Daring Heart:** mile frontline specialist; generically decent stats.
- **Mejiro McQueen:** great for pure int with up to +3 int bonus, 80 specialty, decent cross-training, speed/SP bonus; leader-only skills (good; gold is midleg speed).
- **Daiwa Scarlet:** runner specialty; solid stats and even better skills with max hint level; **Top Runner** or a long-distance instant accel for runners (mandatory for many long runner builds).
- **Copano Rickey:** dirt specialist with many dirt-only skills unobtainable elsewhere; frontline golds (speed skill or a gold heal).
- **Narita Taishin:** chaser specialist; very good cross-training and great SP gain; meta for all chaser builds for all distances, not really worth using otherwise.
- **Ikuno Dictus:** mile specialised with lots of Speed bonus.
- **Taiki Shuttle:** default for mile frontline builds; a bit stacked in Speed bonus so int isn't as easy to raise.
- **Neo Universe:** forgettable; gold is a mid random accel (quite bad); decent for parenting.
- **Manhattan Cafe:** all-round premium: 15% TB, 40% MB, 10% RB, +2 int and +1 SP at 100 bond; strongest cross-training among int cards; skills mainly for long distance and crucial for long betweeners.
- **Mejiro Ramonu:** very strong bonuses, especially 35% friendship and +2 int (fat int rainbows); unique gives 4% TB per Speed skill obtained (uniques that are speed count as one too), up to 20% TB; also maximum-discount hints for some very strong mile/mid skills so in practice more highly rated than the stat-based evaluation; strong mile/mid gold; "the best int card to own due to universality in mile/mid".
- **Mihono Bourbon:** very high bonuses except for race bonus (not a big issue in L'Arc); unique gives +60 initial stats distributed by the categories of the cards in your deck; no SP bonus so SP gain limited; good runner skills (gold = gold version of the opening-leg accel Groundwork).
- **Nakayama Festa:** very focused on int training with 80 specialty, reasonably decent cross-training; no race bonus but frequent int rainbows and strong events; gold version of right-turn green (solid for right-turn tracks).
- **TM Opera O:** similar to Ramonu but +2 Speed bonus instead of SP and increased friendship; very good for raising Speed and cross-training; great long-distance hints; gold **Mo…** (name truncated in extraction; the skill is described as "meta-defining for long-distance leader builds") with an option of a generic straight-speed gold.
- **Satono Diamond:** very solid, balanced; good betweener skill choices.
- **Aston Machan:** 65 specialty (high for Wit), unique gives +60% MB when she is on a rainbow training, plus 15% TB; very potent for showing up in other trainings; great short-distance skills; gold **Concentration** is a staple in many runner builds, sometimes leader.
- **Fine Motion:** used to be the go-to wisdom card early but fell behind due to powercreep, especially gold skill strength; the leader skill isn't too amazing.
- **Nice Nature:** older but with solid bonuses; the only card here with 15% race bonus; betweener accel **Switch-Up Pro** gold is a very strong option in short/mile builds.
- **Mr. CB:** old staple of chaser builds because of the chaser gold **Daring Attack**; notorious for being decent at 1LB already.

## 3.6 Non-MLB cards and welfare

- S5 evaluates cards at other LBs in its spreadsheet only (image not extracted). Rules from the notes: cards with weird uniques (Palmer Speed, Laurel Stamina, Agnes Digital SSR Power…) are evaluated very generously; if you can't activate the unique you probably shouldn't use them; some cards have 0 bond/0 specialty so the score is imperfect; is a Speed card that sucks at raising Speed still a good speed card if it raises other stats?; is a card that costs you a rainbow due to low bond still good? Answer depends on the person.
- **Free welfare cards are evaluated only from 2LB to MLB**, since their unique activates at 2LB instead of 0LB; "don't use welfare cards at 0LB/1LB since they'll be much worse" (S5).

## 3.7 Welfare card choice item (S5)

Monthly story events give a welfare selector; cards join the pool a few months after their event so all story-event welfares eventually become selectable. Pick whatever you need most: if Speed cards are lacking, Speed; if you need Stamina for a mid/long event, Stamina; otherwise probably **int > guts ≫ power**.
- **Speed (first choice):** Special Week (leader recovery useful for mid/long builds), Fine Motion (very similar; better hints, so better if you already own her), Tosen Jordan (universal gold recovery; only if you need a gold recovery for other strategies).
- **Stamina:** Biwa Hayahide is the top choice (universal recovery for long distance); Zenno Rob Roy has slightly higher stats but a bad gold; Twin Turbo is similar in stats but gives the crucial runner skill Top Runner (helps a new player without Maruzensky SSR who wants runners).
- **Power:** none particularly useful.
- **Guts:** Urara and Spe (the main story welfare guts card) are strong enough not to need these; Matikanetannhauser (strong on paper but shares Urara's 0-bond issue; just use Urara), Yukino Bijin (Curve Sommelier, only if needed), Mejiro Ryan (fine stats but lacks good skills except for stadium).
- **Wisdom:** mostly fine with SR cards but Daitaku Helios is good (short skills and a useless gold, but the stat gain is good); Mihono Bourbon (only if you're dead set on a runner build needing her gold opening-leg accel; sidelined by her gacha SSR).

## 3.8 Rerolling, pick tickets, shop

- **Reroll (S5 = S1):** spend initial jewels; without decent support cards the first month or so is painful; cards get stronger as copies arrive. Speed/Wisdom SSR targets that are already very strong at 0-1LB (images not extracted). Ideally 1 speed card from the list plus another from the list or decent SR speed cards; getting multiple copies is very good but rare. Best when a strong card is on the banner, even more in free-roll periods.
- **SSR pick ticket:** use it to try to get a meta card to high LB (0-1LB SSRs are rarely much stronger than SRs; stack tickets or already have a good SSR at 2-3LB to buy a top-tier card at MLB: "the best idea 90% of the time"); use the ranking to judge but remember 20-30 score gaps are small; pick a card that fills your roster (Speed → Wisdom → Stam/Guts); after a major patch/new scenario wait for the meta to settle; tickets don't expire.
- **Training-pass shop (JP 3rd anniversary; blue tickets; 10 tickets = 1 card):** Speed priority: Jungle Pocket (standout, much stronger stats than previous shop cards), Maruzensky (very good; runner skills and strong stats), Kitasan Black (another good option but wants 3LB-MLB), Biko Pegasus (similar strength, less useful), Mayano Top Gun (if you need a gold recovery for runners in longer distances, otherwise worse than Kitasan). Stamina: Super Creek (best by far). Power: Admire Vega and Vodka (great), Rice Shower (if coping for a gold recovery). Guts: Ines Fujin (most useful). Wisdom: TM Opera O (decently strong, especially long leader builds), Fine Motion/Mr. CB (best options). The shop's cards are dated and additions are "drip fed" (S1).
- **Club/Circle points, story welfare limit breaks (S1, S3):** prices of extra SSR copies 100, 900, 2000, 3000 (medals/points). ⚖️ Priorities: S3 (Global): Mejiro McQueen 3LB (Long) > Narita Brian 3LB (decent Speed) > Rice Shower 2LB (debuffers) > MLB Brian and McQueen > Winning Ticket. S1 (JP): Rhein Kraft > Special Week > Silence Suzuka 3LB = Mejiro McQueen 3LB > Narita Brian 3LB > Special Week MLB ≫ Winning Ticket ≫ Rice Shower; Team Sirius is in a weird spot as most scenarios have a Friend/Group card you already take.
- **JP Trainer Medals (S1):** buy the SSR limit break crystal fragment (8000 medals) and the random 3★ uma ticket (15,000 medals) monthly.
- **Cleats/Horseshoes (S1, S3):** gained from destroying duplicate support cards after maxing them; buy pink/gacha tickets and hint books; S3: one SR ticket per month per Cleat type, plus two R and 1★ tickets; never destroy the Urara Guts SSR; rainbow horseshoes come mostly from extra welfare copies.

## 3.9 Friend/Group cards by scenario (S5)

Most of the time running two friend/group cards is not viable; most recent scenarios have a specialty friend/group card that synergises with mechanics and is essentially a must-include.
| Scenario | Specialty card | Necessity |
|---|---|---|
| URA | none | - |
| Aoharu / Unity Cup | Kashimoto Riko | Not required |
| Grand Live | Light Hello | Necessary |
| Grand Masters | 3 Goddesses | Necessary |
| Project L'Arc | Satake Mei | Necessary |
| U.A.F. Ready Go! | Tsurugi Ryoka | Necessary |
| Great Food Festival | Akikawa Yayoi | Necessary |
| Mecha Umamusume | none ("You are free!!!") | - |
| Twinkle Legends | 3 Legends | Necessary |
| Design Your Island | Tucker Brine (Bryne in S6) | Necessary (3LB+) |
| Yukoma Hot Springs | Hoshina Kiyoko (Hoshino in S6) | Necessary |
(S6 adds: Breeders' Cup: Casino Drive, mandatory; Tracen-ken/Ramen: Tazuna (Alt) is best, OG Tazuna/OG Light Hello are weaker, optional but strongly advised.)
TL;DR (S5): use the scenario-specific friend/group card if one exists, don't use other friend/group cards without a very good reason.

## 3.10 Fan-bonus cards for URA farming (S7)

See Part 1, 1.14 for decks. Cards named as 20% FB at MLB: Sakura Bakushin O, Kawakami Princess, Satono Diamond, El Condor Pasa (PWR), Fine Motion, Winning Ticket, Shinko Windy (SR), Mejiro Ryan, Sweep Tosho, Ikuno Dictus, Tamamo Cross, Riko Kashimoto (FRIEND), Manhattan Cafe (STM), Daitaku Helios (PWR). Kitasan Black 15% FB but needed for win rate; Falco SSR 15% FB (groundwork hybrid).

## 3.11 Global vs JP framing for cards (S5, S3)

- S5 warns that its release-date filter is "pretty inaccurate for Global" because evaluations still use current JP-meta scenario parameters.
- Global lags JP in scenario mechanics: faster bonding, free energy events, and scenario stat boosts that ramp up towards the end of runs; Junior/Classic matter less in modern scenarios. Example: Sweep Tosho Speed SSR is reasonable in the modern meta but struggles in URA/Aoharu due to low starting stats (S5).
- Gacha economics per card (rates, spark, expected MLB odds) are in Part 6.

