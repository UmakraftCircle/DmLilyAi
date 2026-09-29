# Umamusume Guide

This guide explains how LilyAi supports the Umamusume clubs **Umakraft** and **Umakraft 2**: linking your account, the fan quota, the daily DM report, and the Leaderboard.

Club data comes from the [uma.moe](https://uma.moe) API.

---

## 1. Link your account

LilyAi needs to know which Discord user is which uma.moe trainer. Linking is done entirely in DMs, with no slash commands and no Discord modals.

| DM phrase | What it does |
|-----------|--------------|
| `link me` | Starts the link flow. LilyAi asks for your uma.moe **Trainer ID**. |
| `unlink me` | Removes your link. |

Only members linked by **both** Discord ID and uma.moe Trainer ID receive the daily quota DM.

---

## 2. Fan quota

| Quota | Amount |
|-------|--------|
| Monthly | 150,000,000 fans (fixed, regardless of days in the month) |
| Daily | 5,000,000 fans (5m x 30 = 150m) |

The quota carries over from day to day, so the month always totals 150m:

- **Deficit:** a day's shortfall is added to the next day's required amount and keeps stacking until it is paid off.
- **Surplus:** a day's surplus reduces the next day's requirement.

---

## 3. Daily DM report

Once per day, LilyAi sends each linked member one DM stating whether that day was:

- **Met**
- **Deficit**
- **Surplus**

---

## 4. Leaderboard

The Leaderboard shows daily gain and monthly gain per trainee in a table.

- **Club tabs:** one tab for Umakraft and one for Umakraft 2.
- **Paging:** 10 trainees per page, up to 3 pages (30-player roster cap per club). The page fits the screen without scrolling down.
- **Former Member tab:** 10 per page with no page cap. Shows each former member's total fan contribution and when they were last detected on uma.moe.

---

## 5. Where this lives in the codebase

| Area | Location |
|------|----------|
| Quota logic | `LilyAiTask/MonthlyTask/quota.py` |
| Daily deficit report | `LilyAiTask/DailyTask/DeficitTask/Deficit.py` |
| Trainer link storage | `LilyAiMemory/TrainerLink/TrainerLinkStore` |
| Leaderboard UI | `LilyAiFrontend` |

---

## Troubleshooting

- **Not receiving the daily DM?** Make sure you are linked: DM `link me` and enter your Trainer ID.
- **Wrong or outdated stats?** Data is pulled from uma.moe, so it reflects whatever uma.moe has most recently detected.
