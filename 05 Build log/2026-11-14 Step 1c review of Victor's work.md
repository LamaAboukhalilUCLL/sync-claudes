# Step 1c - review of Victor's work

**Date:** Sat 14 Nov 2026, 21:25 · **By:** Claude Code (VS Code), at Lama's request. No product code was written.

## What was checked
Victor's two vault commits (18:06 and 18:27) and the `Data-Beyond-Space` repository (4 commits, one branch).

| Check | Result |
|---|---|
| Publication counts 352 / 284 / 235 | Reproduced from `app/raw/` |
| BRE quotation in the [[Step 1 decision sheet]] (fact 5) | Word for word in the PSI-20 record; 16 publications listed |
| "10 of 24 investigations state ambient oxygen" | Matches [[Oxygen evidence (generated)]] |
| Snapshot checksums in `data/papers/manifest.json` | All 24 equal the ones in `app/raw/manifest.json` |
| Temporary PSI download keys in any commit of `Data-Beyond-Space` | None found |
| Abstract count | **73**, not 72 (both `papers.json` and its manifest). Corrected in two notes |

**Not checked:** the video notes, the Global Offers details, the Gemini limits, the retirement date of GitHub Models, and whether the 3 papers whose OpenAlex title differs from the PSI title are wrong matches.

## What was changed
- 72 corrected to 73 in [[Publications and abstracts]] and in the side-task build log; per-investigation coverage added.
- `.idea/` (JetBrains editor settings) removed from the vault repository and added to `.gitignore`, with `.vscode/`.
- **D10** added to [[Decision log]]: the judges see `Data-Beyond-Space`. This changes D7.

## Learned
- Abstract coverage is near zero for the solid-fuel investigations (BASS-II 1 of 9, Saffire-I 0 of 3, Saffire-II 0 of 5), and those are the ones the oxygen pattern concerns.
- After D10 the snapshot and the two scripts are in the wrong repository for the judges. `fetch_papers.py` currently reaches into a sibling folder (`../sync-claudes/app/raw`), which a judge cloning only `Data-Beyond-Space` does not have.

## Next
1. Lama decides the central insight (Step 1), using the [[Step 1 decision sheet]].
2. With her go: move the snapshot and scripts into `Data-Beyond-Space`.
