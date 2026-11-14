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

## Open decisions
- **Central insight** the project is built around (Step 1).
- **Scope:** which views are must-have (Step 1 / Step 3).
- **Tech stack** for the app (Step 3).
- **AI provider** for cited answers (Step 5).
- **Demo format:** 30-second video or 7 slides (Step 6).
