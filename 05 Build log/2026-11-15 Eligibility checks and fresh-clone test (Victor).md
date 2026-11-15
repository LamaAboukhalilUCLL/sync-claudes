# Eligibility checks and fresh-clone test (Victor)

**Date:** Sun 15 Nov 2026, about 14:30 to 14:50 · **By:** Victor, with Claude (Cowork) running the checks. Nothing in either repository was changed.

## Why
A judge must be able to open everything without a login, and the README promises that every number can be rebuilt. Both were untested by anyone outside the team.

## Fresh-clone test (what a judge gets)
`git clone https://github.com/LamaAboukhalilUCLL/Data-Beyond-Space.git` with no login, on a clean Linux machine (Python 3.13, Node 22). Clone at `f554eff`, 73 MB with history. Then the README's "Rebuild the data" steps, in order:

| Step | Result |
|---|---|
| `fetch_snapshot.py` | Skipped, as the README says (only if `data/psi/raw/` is missing) |
| `fetch_papers.py` | Skipped (optional; OpenAlex not reachable from the test machine) |
| `build_dataset.py` | Passes |
| `validate.py` | All checks pass: 47 checksums, 22 tables byte-identical, 659 / 20 / 13.6-22.2 % in 129 / 876 / 270, 24 ranked, 79 quotations, 24 DOIs |
| `check_recount.cjs` | Passes: the recount equals the build for all 24 investigations |
| `npm install` | **Not verified**: it failed on the test machine because `onnxruntime-node` downloads a binary from GitHub during install, which that machine's network blocks. Not a fault shown in the repository. Only needed to rebuild the Ask search index, which is committed |
| `build_search.mjs` | Not run (needs the previous step) |

**One finding:** after `build_dataset.py`, git shows `docs/data/attributes.csv`, `investigations.csv` and `tests.csv` as modified. With line endings ignored there is no difference at all. Python writes the CSVs with CRLF line endings and git stores them with LF. Content is reproduced exactly; only a rebuild looks "dirty". Possible fix, Lama's call: add `docs/data/*.csv -text` to `.gitattributes` so git stores the bytes as built, as already done for `data/psi/raw/**` and `docs/data/tables/**`.

**Also noticed:** `_previews$1.png` (179 KB, a preview image) is still in the repository root.

## Links (checked from a normal browser, no login)
- **All 24 DOIs** are registered and each resolves to its own PSI page (`https://psi.nasa.gov/physci/repo/data/investigations/PSI-n`); 24 of 24 match.
- **Live site:** the five data files the site links or loads (`investigations.csv`, `tests.csv`, `attributes.csv`, `dataset.json`, `tests.json`) all load.
- **Ask page, live:** the model loaded ("Matching by meaning"); "Does smoke behave differently without gravity?" returned 8 results, the first from a SAME paper, with its source.
- Repository and site public: confirmed earlier today (12:30).

## Still to do by a person
1. **Every one of the six members** confirms they are registered for the 2026 hackathon, in the Universal Event, and appear on the team's Members tab. This cannot be checked without each person's login.
2. Open the site and the repository in a **private window** on a computer and on a phone; later the demo link too.
3. A quick click-through in **Firefox** (and Safari if anyone has it); the Ask page is the most fragile part.
4. Optional: `npm install` and `node scripts/build_search.mjs` on a Windows machine, to confirm the last README step.

## Next
Lama: decide on the `.gitattributes` line and the stray PNG (both can go into the same commit as the review edits).
