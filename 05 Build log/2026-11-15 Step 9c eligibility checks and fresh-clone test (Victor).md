# Step 9c - eligibility checks and fresh-clone test (Victor)

**Date:** Sun 15 Nov 2026, about 13:50 to 14:20 · **By:** Victor, with Claude (Cowork) running the checks. Nothing in either repository was changed.

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

## Windows run by Victor (about 14:05 to 14:20)
Fresh clone in a separate test folder (`NASA-Hackathon/fresh-clone-test/`), Windows, Git 2.55, Python 3.14.7, Node 24.20, npm 11.19. Clone at `f554eff`, 27 MB download, working tree clean.

| Step | Result |
|---|---|
| `python --version` | **Fails**: "Python was not found" (Windows opens the Microsoft Store shortcut). `py` works. Common on Windows: `python` only exists if "Add python.exe to PATH" was ticked at install |
| Site, `cd docs` then `py -m http.server 8000` | All pages opened and looked right; Ask worked |
| `py scripts/build_dataset.py` | Passes |
| `py scripts/validate.py` | All checks pass, 79 quotations (GitHub's version, without the review edits) |
| `node scripts/check_recount.cjs` | Passes |
| `git status` after the build | The same three CSVs as on Linux show as modified; `git diff --ignore-cr-at-eol` shows nothing, so line endings only (Git warns "CRLF will be replaced by LF") |
| `npm install` | **Works**: 42 packages, 0 vulnerabilities. npm 11 skipped two install scripts (`onnxruntime-node`, `protobufjs`; "not yet covered by allowScripts") and the next step still worked |
| `node scripts/build_search.mjs` | Works: "embedded 925 of 925", 311 passages from NASA records, 614 from 235 papers, 73 with an abstract |
| `git status` after the search build | `docs/data/passages.json` modified. Compared with GitHub's copy: `about` and all 925 passage texts and sources are identical; the vectors differ slightly (4.6 % of the 355,200 numbers, by at most 3 on a scale of -127 to 127; every passage's old and new vector at least 99.1 % similar). Normal for a language model run on different machines; could at most swap two near-equal search results |

Also run in Victor's working copy by mistake, on branch `victor/review-and-ai-marks`: build, validate (81 quotations) and recount pass with the review edits on Windows; the one CSV it touched differed only in line endings and was restored.

### Suggestions for Lama (README and `.gitattributes`, her call)
1. Under the README's commands: "On Windows, use `py` instead of `python`. On macOS or Linux, use `python3` if `python` is not found." (Replacing `python` with `py` would break it for macOS and Linux.)
2. In `.gitattributes`: `docs/data/*.csv -text`, so a rebuild no longer shows the three CSVs as modified.
3. In the README, one sentence: the search index rebuilds with the same passages, but its vectors can differ very slightly from machine to machine.

## Still to do by a person
1. ~~**Every one of the six members** confirms they are registered for the 2026 hackathon, in the Universal Event, and appear on the team's Members tab.~~ Done: all members confirmed (Victor, 15 Nov).
2. ~~Open the site and the repository in a **private window** on a computer and on a phone~~ Done by Victor: Chrome private window fine; the phone check found the table pop-up bug, fixed in [[2026-11-15 Step 9d phone fix for the table pop-up (Victor)]]. Still to do: the demo link, once it exists.
3. A quick click-through in **Firefox** (and Safari if anyone has it); the Ask page is the most fragile part. Not done yet.
4. ~~Optional: `npm install` and `node scripts/build_search.mjs` on a Windows machine~~ Done, see the Windows run above.

## Next
Lama: decide on the `.gitattributes` line and the stray PNG (both can go into the same commit as the review edits).
