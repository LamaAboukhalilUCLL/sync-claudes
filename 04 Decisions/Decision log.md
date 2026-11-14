# Decision log

One entry per decision: what, why, who decided, when. Newest at the bottom.

## D1 - Work step by step, explain before building
- **When:** 14 Nov 2026
- **Decided by:** Lama
- **Why:** quality target is Global Finalist; she must understand and own every part.

## D2 - Obsidian vault as project memory
- **When:** 14 Nov 2026
- **Decided by:** Lama
- **What:** context grows in notes instead of a fixed spec. The connected folder `NASA_hackathon` is the vault.

## D3 - Two assistants, synced through the folder
- **When:** 14 Nov 2026
- **Decided by:** Lama, on Claude's recommendation
- **What:** Claude Code in VS Code builds and runs the app in `app/`. Claude in the desktop app does strategy, research, the Space Apps site, review and submission text. `CLAUDE.md`, `Status.md` and the build log keep them in sync.

## D4 - Commit the PSI snapshot
- **When:** 14 Nov 2026
- **Decided by:** Lama
- **What:** `app/raw/` (search result, 24 records, 22 Experimental Tables, manifest with checksums) is committed to git, not ignored.
- **Why:** every number must be traceable to a saved file, and PSI's endpoints are undocumented and may change.

## D5 - Ambient oxygen and burner-flow oxygen are separate fields
- **When:** 14 Nov 2026
- **Decided by:** Lama
- **Why:** oxygen blown from a burner into a fuel atmosphere (CFI-G and Flame Design inverse flames, up to 85%) is not the atmosphere a crew breathes. Mixing them would make the oxygen story wrong.

## D6 - Odd cells are shown as written, never cleaned silently
- **When:** 14 Nov 2026
- **Decided by:** Lama
- **What:** a cell is used as a number only if it is a plain number or a `;`-separated list of plain numbers. Everything else (`3400%`, `~ 21.5`, `RAMP`, blanks) is displayed exactly and kept out of ranges.

## D7 - One repository, code in `app/`
- **When:** 14 Nov 2026
- **Decided by:** Lama
- **What:** code lives in the vault's `app/` folder. The repository is private now and becomes public before submission, notes included.

## D8 - Git routine
- **When:** 14 Nov 2026
- **Decided by:** Lama
- **What:** Claude Code pulls before every write and commits its own work with clear messages. Obsidian Git (on Lama's computer, "ellegio") commits her note edits.

## D9 - No live AI key in the design yet
- **When:** 14 Nov 2026
- **Decided by:** Lama
- **What:** the AI provider is decided at Step 5. Nothing before then may depend on a live API key.

## D10 - `Data-Beyond-Space` is the repository the judges see
- **When:** 14 Nov 2026
- **Decided by:** Lama
- **What:** the public submission repository is `Data-Beyond-Space` (github.com/LamaAboukhalilUCLL/Data-Beyond-Space). This vault (`sync-claudes`) stays the team's shared notes. Publication abstracts stay in `Data-Beyond-Space`.
- **Changes D7:** the product code no longer ends up in the vault's `app/` folder.
- **Consequence, not yet done:** everything a judge needs to trace a number must be in `Data-Beyond-Space` before submission: the PSI snapshot with its manifest, the scripts, the app, the references and the AI acknowledgements. Today the snapshot and two scripts are only in the vault's `app/`. Moving them is a step that waits for Lama's go.

## D11 - Direction for the central insight: Earth-gravity screening
- **When:** 14 Nov 2026
- **Decided by:** Lama
- **What:** the central insight will be about row A of [[NASA stated fire safety needs]]: Earth-gravity material screening may miss the fire risk. Lama chose it from the list of NASA's stated needs.
- **Still to do:** Lama writes the one-sentence insight in her own words; it is then checked against the snapshot.

## Open decisions
- **Central insight sentence** (direction chosen in D11; the sentence itself is still to be written by Lama).
- **Scope:** which views are must-have (Step 1 / Step 3).
- **Tech stack** for the app (Step 3).
- **AI provider** for cited answers (Step 5). Options: [[AI provider and hosting options]].
- **When and how the snapshot and scripts move** from the vault's `app/` into `Data-Beyond-Space` (follows from D10).
- **Demo format:** 30-second video or 7 slides (Step 6).
