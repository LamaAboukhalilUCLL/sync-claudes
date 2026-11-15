# Step 12b - review of pull request #6, Victor's Ask upgrade

_Sun 15 Nov 2026, about 19:25 to 19:45. Claude Code in VS Code, for Lama. Nothing was changed on Victor's branch or on `main`; the review ran in a separate copy that was deleted afterwards._

Pull request #6, branch `victor/ask-upgrade`, 13 commits, last `01e1991` (19:20). Covers Steps 11b and 11c, plus three later commits (new example questions, "Read it in context" link from Ask results to the marked passage in NASA's record).

## Checks run on the branch
- `build_dataset.py`, `validate.py`, `check_recount.cjs`, `check_model.cjs`, `check_ask.cjs` (28 checks): **all pass**.
- `build_search.mjs` rebuilt on this machine: passage texts identical; vectors differ by rounding only (at most 3 of 127).
- `eval_ask.mjs` rerun: on this machine the site setting scores **14 / 17** on the held-out half and **28 / 33** on all 40, where the branch publishes 13 / 17 and 27 / 33. One question of difference, from the rounding; Victor's note already says 20 questions cannot separate settings.
- Merges into `main` without conflicts (tested, not merged).
- Real Chrome, local copy of the branch: 9 questions on Ask, the context link, an investigation page, the Data page, and Overview, Habitat, Analysis, Explore, Ranking, Open questions. **No console errors; no page broken.** Counted answers match the build (solid materials: 129 tests with oxygen, 13.6 to 22.2 %, 0 at 30 % or more; droplets: 273 with both, 0 in Moon Base air). The unrelated question ("best pizza recipe in Naples") shows nothing.

## Findings
**To fix before merging**
1. **The score's labels are still unchecked, and the live page would say so:** "To be checked by a team member." `checked_by` is empty in `ask_eval_questions.json` and in `ask_glossary.json`. Victor planned to check them before the score goes live.
2. **Word-list false match:** "drop" maps to "droplet", so "Does the burning rate drop at low pressure?" also searches for droplets and the first result is a droplet paper. Remove "drop" from the list (keep "bead").

**Worth fixing**
3. "Closest by meaning" on investigation pages shows similarities of 0.96 to 0.98 with the new model, and the note says "1 would be the same text". Readers will read that as near-identical records. Show the order without the numbers.
4. "Read it in context" marks the passage only when the reader comes from the Ask page; a shared link opens the right section but without the mark (passages are not loaded on a direct visit).

**Minor, no action needed**
5. The first example, "Will cabin materials burn in Moon Base air?", also shows the Moon-gravity card because the question contains "Moon". The card is true, but the question is about the air.
6. Questions that only mention "pressure" get a counted card over all 1,982 tests, which adds little.
7. The word list maps "alcohol" only to methanol and "plastic" only to PMMA; it adds search terms, so nothing is lost, but it is narrower than the words.

## Decision for Lama
- Model switch to snowflake-arctic-embed-s: same score with the word bonus, clearly better by meaning alone (helps questions that share no word with NASA's text); download 62 MB instead of about 50 MB; both models stay in the repository.
- Merge order (Status): this pull request first, then `si-coverage` re-applied on top, keeping Victor's score on the Ask page.

## Update, about 20:05: two fixes on branch `ask-fixes`
Lama asked for findings 2 and 4. Claude Code was not allowed to push onto Victor's branch, so the fixes are on a new branch **`ask-fixes`**, made from Victor's latest commit (`46cac59`, 19:29) plus two commits:
- `718b8df`: "drop" removed from the word list (`ask_glossary.json` and its copy inside `passages.json`; vectors untouched, so `ask_eval.json` stays valid; no test question contains "drop").
- `a688c87`: "Read it in context" also marks the passage when the link is opened directly (the page loads the passages itself). Cache version 23.
All checks pass. Tested in Chrome: a shared link opened directly marks the passage and scrolls to it; "Does the burning rate drop at low pressure?" no longer adds "droplet"; "bead" and "smoke alarm" still expand.
**To use them:** Victor merges `ask-fixes` into `victor/ask-upgrade` (a fast-forward: `git pull origin ask-fixes`), or opens a pull request from `ask-fixes` into his branch.

## Lama's idea for finding 3: a map by meaning (preview only, not pushed)
Lama proposed an Obsidian-style graph instead of the similarity numbers. Built as a preview in the local copy: each investigation a dot coloured by what burns, joined to its three nearest by meaning (same similarities as `related.json`, recomputed from the stored vectors), a spring layout so closer text means a shorter line, hover highlights neighbours, drag moves a dot, click opens it. On investigation pages the numbers are replaced by the names and a "See it on the map" button; Explore gets a fourth tab "Map by meaning". The note under it says every pair lies between 0.86 and 0.99 similarity, so the map stretches a small range, and that it shows wording and topic, not test results. Waiting for Lama's yes or no.
