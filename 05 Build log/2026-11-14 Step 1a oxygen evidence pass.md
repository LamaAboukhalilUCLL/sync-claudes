# Step 1a - PSI snapshot and oxygen evidence pass

**Date:** Sat 14 Nov 2026 · **By:** Claude Code (VS Code), on Lama's decision (Option A)

## What was done
1. **Snapshot.** `app/fetch_snapshot.py` downloaded, without changing anything, the PSI search result, the 24 Combustion Science investigation records and their 22 Experimental Tables into `app/raw/`, with `manifest.json` recording source URL, time, size and SHA-256 for each file. `app/raw/` is now committed (removed from `.gitignore`).
2. **Evidence note.** `app/evidence_oxygen.py` reads only `app/raw/` and writes [[Oxygen evidence (generated)]]: a summary per table, every oxygen and pressure column in detail, row counts per oxygen level, the reason each column is read as ambient or burner-flow oxygen, every table header, and the 24 records with DOIs.
3. **Notes corrected** against the snapshot: [[PSI data source]] (table rewritten, corrections listed), [[Investigations overview]], [[Rules and eligibility]] (three missing rules added), the team guide (counts, BASS-II size, PSI-47, SPICE/SLICE fuels), [[References]] (24 DOIs), [[SI use log]], [[Decision log]] (D4 to D9).

## Why
Lama chooses the central insight herself, and wanted to choose it on verified facts instead of a first look in the browser.

## How to run it
From the `app/` folder (Python 3, no packages to install):
```
py fetch_snapshot.py      # only downloads what is missing from raw/; delete raw/ to refresh
py evidence_oxygen.py     # rewrites "03 Data/Oxygen evidence (generated).md"
```

## How the evidence script treats cells
- A cell is a number only if it is a plain number, or a `;`-separated list of plain numbers.
- Every other cell is printed exactly as PSI wrote it and kept out of the ranges.
- Ambient oxygen and burner-flow oxygen are separate. Which column is which is declared by hand at the top of the script (`COLUMNS`), with the reason, and printed in section 4 of the note.
- The only conversion: mole fraction x 100 to read as percent, marked with †.

## Learned
- **Two tables were missed in the first look.** CFI-G and Flame Design each have a second table of "inverse" flames, where oxygen comes out of the burner into a fuel atmosphere. The 85% oxygen figure is burner-flow oxygen. Ambient oxygen in both tops out at 40%.
- **Solids:** BASS-II 13.6-22.2% (no row at 30% or more), Saffire-I about 21.5%, Saffire-II about 21.5-22.1%. **BASS and Saffire-III state no oxygen value in their tables**, so the pattern is unverified for them, not confirmed.
- **30% ambient oxygen or more** appears in FLEX, FLEX-2, CFI-G, Flame Design, BRE and s-Flame: all gases or droplets.
- **BRE** is a gas burner that emulates burning solids. Its objective text names NASA's considered atmospheres: 14.7 psia / 21%, 10.2 psia / 26.5%, 8.2 psia / 34%. So the draft's "34%, 8.2 psi" does have a PSI source.
- A table row is not always one test (test days in BRE and s-Flame, fuels in FLEX-2).
- The table download address returns a temporary link with short-lived access keys. The script follows it and never saves it; `app/raw/` was checked and contains none.
- The BASS-II size mismatch was units: 274.63 GB is 255.77 GiB.
- Odd cells found: BRE `3400%` and `2100%`; FLEX pressure `0`; BASS-II final oxygen 39.1 and 40.4; drag-fill damage (`N3`..`N6`, `CH5`, `CH6`); `#VALUE!` twice in CFI-G.

## Not done
- Investigation documents and publications were not read; only metadata and tables.
- DOI links were collected but not clicked.
- The draft in `app/_draft/` was not touched. The stray nested vault `nasa/` (only `Welcome.md`) was left alone.

## Next
Lama reads the evidence note and decides the central insight (rest of Step 1). Then Step 2, the data pipeline, which starts from `app/raw/`.
