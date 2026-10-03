---
title: Career Start Workflow
aliases: [career start workflow, career guide, start career, new career, career workflow]
author: lordofumakraft (with help from ChatGPT)
---

# Career Start Workflow

Interview flow for helping a trainer plan a new Umamusume career. LilyAi asks one thing at a time, looks facts up in the game docs, gives a recommendation, and moves on once the trainer confirms. Written from hands-on play by lordofumakraft (Champions Meeting winner), with Ura Finale as the worked example.

Flow: Scenario → Trainee → Target → Inheritance → Support Cards → (play the career) → Result

Main principle: build for the actual race conditions and career requirements, not for a static ranking of skills or cards.

## How to run this workflow

- Ask one question per message. Do not skip ahead.
- Keep a one-line state and repeat it after each confirmed step: `State: scenario=… | trainee=… | target=… | inheritance=… | deck=…`
- Look facts up in the docs instead of answering from memory: Character docs for trainees, Skill docs for skills and unique conditions, Support Cards docs for cards, Glossary for terms, Guide docs (Affinity, scenario guides) for mechanics.
- Never assume what the trainer owns. Ask which inheritance umas and support cards they have.
- A skill, spark or card is only good if it works in the intended race. Judge by the target, not by a fixed ranking.
- If a doc is missing or unclear, say so instead of guessing.

## Step 1 — Scenario

Ask which scenario the career is for: Ura Finale, Unity Cup, Trackblazer or Grand Concert (written Grand Live in the docs).

- Cost to start a career: 30 TP. During a 1/2 TP event: 15 TP.
- Look up the scenario guide under Guide/Career/Scenario.
- The inheritance rules below are fully written for Ura Finale and Unity Cup. For Trackblazer and Grand Concert, say that scenario-specific inheritance advice is not covered here and rely on the scenario guide.

Confirm the scenario, then move on.

## Step 2 — Trainee

Ask which trainee (playable Umamusume). Look up her Character doc and note:

- Career goals: each trainee has goals based on her real-life counterpart. The build must be able to win the required races.
- Secret events: they depend on career performance, so consider them when judging the finished build.
- Stat growth bonuses (example: Oguri Cap has +20% Speed and +10% Power). Decide what training and Support Cards must supply.
- Skills: 1 Unique Skill and 2 built-in Gold Skills. The Unique can also be inherited through Inspiration. Potential unlocks extra skills (example: Oguri Cap Potential 5 → Corner Connoisseur).

Summarize in two or three lines and confirm.

## Step 3 — Target

Ask what the career is for. Get:

- Target race: track, distance and running style.
- Target stats (keep them within the scenario's stat cap; look the cap up).
- Skills the trainee must finish with.

Everything after this step depends on the target, including whether a Unique Skill is usable (see the Unique Skill Gate below). If the target is unknown, ask. Do not guess. Add it to the state line.

## Step 4 — Inspiration (inheritance)

Ask which two Inheritance umas the trainer has, one slot at a time. An Inheritance uma can also be borrowed or rented with in-game currency.

```
New Trainee
├── Inheritance 1
│   └── Parent
│       ├── Grandparent 1
│       └── Grandparent 2
└── Inheritance 2
    └── Parent
        ├── Grandparent 1
        └── Grandparent 2
```

The Parent is the directly selected uma. The Grandparents are the two umas used to create that Parent.

- Hold parents to a strict standard. Independent Training makes good parents easy to produce, and scenario white skills (Racing Spirit, Burning Spirit) can be obtained by completing a career through Independent Training or manually.
- Check compatibility with the trainee in-game. A ◎ rating is preferred because it raises spark proc chances. See the Affinity guide.

### Priority order

1. White Skill
2. Pink Spark
3. Blue Spark
4. Unique Skill

The Unique Skill has no permanently fixed rank. Its value depends on whether its activation condition can realistically be met in the target race.

### White skills

Scenario white skills are a major priority.

- Ura Finale, Racing Spirit: Speed, Stamina, Power, Guts, Wit. The Mood version gives Skill Points when inherited, and the "+" versions give extra stats when inherited.
- Unity Cup, Burning Spirit (also written Ignited Spirit): Speed, Power, Stamina, Guts, Wit. The "+" versions give an extra stat bonus when inherited.
- Main Parent: should carry the relevant scenario white skill whenever possible. 60+ white skills is preferred, 40+ is acceptable.
- Grandparents: should add relevant scenario white skills and a strong white pool.

### Pink sparks

Priority, for both inheritance slots:

1. Distance aptitude
2. Track aptitude (Turf or Dirt)
3. Running style

Distance S is especially valuable for PvP.

### Blue sparks

Evaluate Blue after the required white skills and pink sparks. Pick the stat that the target race and the trainee's growth bonuses need most.

### Unique skills

A Parent's Unique can be inherited, and a Grandparent's Unique can be inherited during the Inspiration event. The inherited version is weaker than the original. Example: with Oguri Cap as main inheritance, the new trainee can inherit Triumphant Pulse in its weaker form.

No Unique Skill is the strongest in general. Run the gate below before recommending any of them.

### Unique Skill Gate

A strong Unique that cannot activate in the target race is worse than having none. Treat its value as zero.

Check against the Step 3 target:

- Track and distance, and where the last spurt starts (corner or straight).
- Running style.
- Position requirement, and the expected race formation.
- Activation timing: too early or too late means it is dead.
- Whether another runner can deny the required position.

If every check passes, the skill has practical value. If any fails, do not inherit it and do not pick the Parent for it. Choose a Unique that fits, or reconsider the running style for that track.

Example: Angling and Scheming (Seiun Sky) fires too early or too late on a given track, and the Front Runner is effectively dead. It needs first place and a spurt that starts on a corner (all Medium and Mile G1 tracks). Long G1 tracks start the spurt on a straight, so use Kitasan Black there.

### Unique skill picks by style

These are default picks when the gate passes. Position ranges are for a 9-runner race. Confirm exact conditions in the Skill docs, since they can change with patches.

- Front Runner: Seiun Sky Original Unique as main inheritance. Kitasan Black Original Unique as an extra for long races, in the Grandparent section.
- Pace Chaser: Seiun Sky and Kitasan Black also work when there is no Front Runner, or when the Pace Chaser can overtake the Front Runner and meet the condition. Mejiro Dober and Mejiro Ryan Original Uniques give acceleration when the required position is around 5th or 6th. That happens when there are more Front Runners, or the Pace Chaser loses position to other Pace Chasers.
- Late Surger and End Closer: Mejiro Ryan and Mejiro Dober Original Uniques are the default picks when their conditions can be used. If the track makes both unusable, reconsider the backline strategy.
- Sprint and Mile, Pace Chaser: Nishino Flower, Budding Blossom (3rd–4th). Taiki Shuttle, Shooting for Victory (2nd–5th). Front Runners can use these too, as extra acceleration in front-heavy formations.

### Position competition

Position-based Uniques interact between strategies. A Front Runner can take a position a Pace Chaser needs and deny the skill. If Nishino Flower or Taiki Shuttle is central to the expected Pace plan, a Front Runner running the same skill can contest the position and act as a counter-strategy. Judge both whether a skill can activate and whether another strategy can interfere.

## Step 5 — Support cards

A career uses 6 Support Card slots: 5 owned cards and 1 borrowed card. Take card information from the Support Cards docs. Do not hardcode cards, and do not assume one card is always right.

Ask which Support Cards the trainer owns. Then:

1. Confirm the trainee build and the target race requirements.
2. Work out the training structure the build needs, such as which stats must be trained and which card types are required.
3. Query the Support Cards docs.
4. Build the Ideal Deck: the best 6 cards for this build, ignoring ownership.
5. Compare it with the owned cards.
6. Use the borrowed slot for the most important card the trainer does not own.
7. Replace other missing cards with accessible alternatives.
8. Build the Budget Deck: the owned cards plus the borrowed card.
9. State any remaining limitation. If the collection cannot reproduce the needed training structure, say so clearly and do not present the Budget Deck as equivalent to the Ideal Deck.

Give both decks with one line of reasoning per card.

## Step 6 — Result

After the career, ask for the final stats, skills, aptitudes and grade. Compare them with the Step 3 target, the trainee's career goals and her secret events. Then:

1. Did the career reach its goal?
2. Were the planned build requirements met?
3. What worked, and what did not?
4. What requirements were missing?
5. What caused the problems? Separate bad luck (spark or hint rolls) from build mistakes (inheritance choice, deck, training).
6. What should change in the next career?
7. Can this uma be a useful Parent or Grandparent? A career does not have to be perfect to have value.

## Limits

- Inheritance rules here are written for Ura Finale and Unity Cup only.
- Unique skill conditions, spark odds and stat caps change with patches. Confirm them in the docs before recommending.

Guide by lordofumakraft, with help from ChatGPT.
