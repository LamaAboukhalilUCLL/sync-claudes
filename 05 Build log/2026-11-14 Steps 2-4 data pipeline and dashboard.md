# Steps 2 to 4 - data pipeline and first full dashboard

**Date:** Sat 14 Nov 2026, 23:04 · **By:** Claude Code (VS Code), after Lama said to build. All code is in repository `Data-Beyond-Space` (commit `d9e1fba`, pushed).

## What was built
1. **Snapshot moved.** `data/psi/raw/` in `Data-Beyond-Space` is a byte-for-byte copy of the vault's `app/raw/`; all 47 checksums verified after the copy and again on the committed files. `fetch_papers.py` now reads the local copy. The vault's `app/` is left in place.
2. **`scripts/build_dataset.py`.** Turns the snapshot into `docs/data/`: `dataset.json`, `tests.json`, two CSV downloads, and copies of the 22 tables. It keeps D5 and D6, converts pressure to psi (marked), and fails if a quotation is not in NASA's record word for word or if a text contains a hand-typed number.
3. **`scripts/validate.py`.** Separate code that re-checks checksums, recounts the headline numbers from the raw CSVs, and re-checks all 79 quotations. All checks pass.
4. **`data/content/interpretation.json`.** The AI-written plain-language summaries (24) and the six-question board. Numbers are placeholders filled from computed data.
5. **`docs/`.** The website: overview, coverage map (oxygen by what burns; oxygen against pressure), ranking, investigation pages with compare, open questions, data and method. Clicking any mark opens NASA's table at that row. Plain HTML, CSS and JavaScript; no libraries.

## What the data turned out to say
- **20 of 659** tests that state both oxygen and pressure are inside the Moon Base zone (30 % or more, 10.2 psi or less). All 20 are gas flames in ACME CFI-G, an engine-research investigation.
- Solid materials with a stated number: **13.6 to 22.2 %** oxygen (129 BASS-II tests). None at 30 %.
- 876 tests state ambient oxygen as a plain number; 270 are at 30 % or more (246 gas, 24 droplet, 0 solid).
- Only 10 investigations state oxygen in their table and 5 state pressure.
- No investigation meets all five conditions; the best meet 3 (FLEX, ACME CFI-G).
- 0 of 24 records mention the Moon, Mars or partial gravity in their description.

## How to run it
```
cd Data-Beyond-Space/docs
py -m http.server 8000
```
Open http://localhost:8000. To rebuild: `py scripts/build_dataset.py` then `py scripts/validate.py` from the repository root.

## How it was tested
Screenshots of every page with headless Chrome at desktop width, and of the table viewer opened at a row. **Not tested:** real clicking and hovering by a person, phone screens, Firefox and Safari, the public GitHub Pages link (the repository is still private).

## Needs Lama
- Confirm or change the five ranking conditions (D14) and the D6 question in it.
- Read the AI-written texts; they are in one file and easy to edit.
- Project name; make the repository public; switch on GitHub Pages.

## Next
Review, then the project page text and the demo (Step 6).
