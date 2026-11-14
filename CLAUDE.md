# Flame in Freefall - project instructions

Read this first, then `Status.md`, then the newest note in `05 Build log/`.

## What this is
Team **Data Beyond Space**, NASA Space Apps Challenge 2026, Universal Event.
Challenge: **Flame in Freefall: SI-Powered Fire Safety Insights from Microgravity Combustion Data**.
Deliverable: an interactive, AI-powered, web-based dashboard that **summarizes, ranks and interprets** NASA's microgravity combustion investigations (PSI database) to give fire safety insights for human spaceflight.
Deadline: **Sunday 15 November 2026, 23:59**, local time of the Team Owner.

## How Lama wants to work (non-negotiable)
1. **One step at a time.** Do not build ahead of the agreed step.
2. **Explain before building.** Say what you will do, why, and the options. Wait for her decision.
3. **Explain after building.** Walk through what the code does in plain language.
4. **Quality over speed.** Target is Global Finalist level. Small, verified pieces.
5. **The ideas are hers.** Offer options and trade-offs; she chooses. (Space Apps rule: AI must not come up with the solution idea.)
6. **Never invent data or numbers.** Every figure shown in the app must come from PSI and link to its investigation and DOI.

## After every step
- Add a note to `05 Build log/` named `YYYY-MM-DD Step N short title.md` (what was done, why, how to run it, what was learned, what is next).
- Update `Status.md`.
- If a choice was made, add it to `04 Decisions/Decision log.md`.
- If an AI tool, dataset, library, image or text source was used, add it to `06 Submission/SI use log.md` or `06 Submission/References.md`.

## Hard rules from Space Apps (details in `01 Challenge/Rules and eligibility.md`)
- Must use NASA data (PSI) and cite each investigation by DOI.
- Demo: video of 30 seconds or less, or at most 7 slides. Over the limit means ineligible.
- Project and demo on public links with no login. Everything in English.
- AI-generated images/video need a visible watermark; AI-generated code and data must be acknowledged in text and metadata. No NASA logos or mission identifiers in AI content.
- List every external resource used.
- Do not download PSI raw data (hundreds of GB). Use investigation metadata and Experimental Tables.

## Where things are
- `00 Home.md` - map of the vault
- `01 Challenge/` - what NASA asks, rules, judging
- `02 Domain/` - fire science and the investigations
- `03 Data/` - PSI structure and API
- `04 Decisions/` - decision log
- `05 Build log/` - one note per step
- `06 Submission/` - project page text, demo, AI disclosure, references
- `app/` - the code. `app/_draft/` holds an untested first draft; treat it as reference only.

## Two assistants, one memory
Lama uses Claude in the desktop app (strategy, research, Space Apps site, review, submission text) and Claude Code in VS Code (building and running code). They do not share memory. **This folder is the shared memory**, so keep the notes current.
