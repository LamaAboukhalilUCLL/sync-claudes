# Step 11b - Ask upgrade (Victor)

**Date:** Sun 15 Nov 2026, evening · **By:** Victor, with Claude Code (design, code, checks) after six directions proposed by Claude (desktop app). Repository `Data-Beyond-Space`, **branch `victor/ask-upgrade`, five commits on top of `main` (`0397c6f`), pushed by Victor to `origin/victor/ask-upgrade`, pull request open, not merged: waiting for Lama.** Numbered 11b because it follows Lama's Step 11; it is not part of it.

## Why
The Ask page returned the closest quotations and nothing more. It computed nothing, did not say how far the evidence reaches toward Moon Base air, said nothing useful on Moon or partial-gravity questions, and its accuracy had never been measured. D22 stays as it is: no language model writes text on the site; the model only matches text.

## What was built
| Piece | What the reader sees | Needs the language model? |
|---|---|---|
| Shared module `docs/ask.js` | Nothing new by itself: ranking, counts and detection moved out of `app.js` so the site and the scripts run the same code | No |
| Moon / Mars / partial gravity card | When a question names them: "PSI holds no test at Moon or Mars gravity", the computed count (0 of 24 records), a link to the open question "Does Moon gravity change any of this?" and its reading list | No |
| Counted answers | For questions about oxygen, pressure, "how many", "which experiments": a card "Counted from NASA's tables" with the tests in scope (by fuel or material cell, kind, or investigation) and their oxygen, pressure and both-together counts. A number with % or psi in the question becomes the limit; otherwise the chosen atmosphere is used | No |
| Evidence reach | Above every result list: how many of the investigations behind the passages have a test in the chosen atmosphere, how many tests, and how many cannot be placed because the table does not state both conditions | No |
| Everyday words | "Also searched for PMMA, polymethylmethacrylate (you wrote plastic)". Fixed list of 18 entries in `data/content/ask_glossary.json`; the build stops if a NASA term is not in NASA's text or tables | No |
| Related by meaning | On each investigation page: the three records whose NASA text is closest, with the similarity. Built by `build_search.mjs` into `docs/data/related.json` | No (computed at build time) |
| Measured score | Data and method page, "How well Ask finds the right record": hit at 1 and hit at 3, with the label note and two cautions | No |

## Measurements (all from `node scripts/eval_ask.mjs`)
40 questions, 11 of them in everyday words. A hit means: a passage shown comes from one of the investigations listed for the question.

| Setting | First | In first three |
|---|---|---|
| **Site: meaning + word bonus 0.2 + glossary on words** | **28 of 40** | **32 of 40** |
| Site without the model (words + glossary) | 27 of 40 | 32 of 40 |
| Meaning only (bonus 0), no glossary | 18 of 40 | 25 of 40 |
| Bonus 0.1, no glossary | 19 of 40 | 27 of 40 |
| Bonus 0.2, no glossary (what was live, new stem) | 24 of 40 | 29 of 40 |
| Bonus 0.3 / 0.5 / 1, no glossary | 23 of 40 | 31 of 40 |

- **The word bonus does not hurt; it helps.** The earlier 20-question browser test (0.55 with, 0.65 without) is not confirmed on 40 questions: removing the bonus costs 6 first-place hits. It stays at 0.2. From 0.2 upward the score is flat.
- **Glossary:** on the 11 everyday-word questions, 4 first / 6 in three without it, 8 / 9 with it. The other 29 questions do not change (20 / 23). The glossary and the questions were drafted by the same AI in the same session, so this flatters the glossary.
- **Stem change** (flame = flames): one question either way. Kept because it is the correct behaviour, not because of the score.
- **Weak spot seen by hand:** for "Which experiments burned plastic?" the counted card is right (BASS, BASS-II, SAFFIRE-II) but with the model on, the first quotation is an unrelated droplet paper.
- **Caution, also printed on the site:** labels are by Claude and unchecked; the same questions were used to choose the settings.

## Related investigations: does it find the cross-links the challenge statement names?
Not on the site as a claim. For the team to decide.

| Pair | By meaning (rank of 23) | By shared words only (TF-IDF) | Listed by PSI as related? |
|---|---|---|---|
| DAFT → SAME-R | 1 | 1 | no |
| DAFT → SAME | 2 | 2 | yes |
| SAME → DAFT | 11 | 3 | no |
| SAME-R → DAFT | 6 | 2 | no |
| ACME BRE → BASS-II | 2 | 4 | no |
| ACME BRE → BASS | 3 | 5 | no |
| BASS-II → ACME BRE | 2 | 2 | no |
| BASS → ACME BRE | 3 | 6 | no |

- DAFT ↔ SAME: found from DAFT's side, but shared words find it just as well, and from SAME's side words do better than meaning. No evidence the embeddings add anything here.
- ACME BRE ↔ BASS / BASS-II: found in the top three in both directions by meaning; words alone put it at 2 to 6. A modest gain, and PSI's own "related" field does not list this link.
- Overall: of 21 links PSI lists itself, 17 are in the top three by meaning and 18 by words. The two top-three lists share 40 of 72 entries. Fair summary: mostly shared vocabulary, with a small real gain on BRE ↔ BASS.

## How it was checked
- `py scripts/build_dataset.py`, `py scripts/validate.py`, `node scripts/check_recount.cjs`, `node scripts/check_model.cjs`: all pass. CSVs restored after the build (line endings only).
- New `node scripts/check_ask.cjs` (24 checks, no model needed): the Moon pattern equals the one in `build_dataset.py`; it fires on Moon, lunar, Mars, Martian, partial gravity and not on microgravity, reduced gravity, low gravity; no number card on 11 ordinary questions; counts equal the build, `recount.js` and a separate count from `tests.csv`; glossary terms exist; `related.json` and the word-matching score are reproduced.
- Local site in the built-in browser: desktop with the model on, phone width (375 px) with the model off. Cards, reach line, glossary line, related line and score table render; no horizontal overflow; no console errors.
- `passages.json` was rebuilt on Victor's Windows machine. Texts are identical; vectors differ from the previous build by rounding only (at most 3 of 127), as Step 8c predicted.

## How to run it
```
py scripts/build_dataset.py
py scripts/validate.py
npm install
node scripts/build_search.mjs
node scripts/eval_ask.mjs
node scripts/check_ask.cjs
git restore docs/data/*.csv
cd docs
py -m http.server 8000
```

## Not done, and open
- **Labels unchecked.** Victor re-labels `data/content/ask_eval_questions.json` (set `checked_by`), reruns `eval_ask.mjs`, before the score goes live.
- **Glossary unchecked.** 18 entries in `data/content/ask_glossary.json`, drafted by Claude. Set `checked_by` after review, then rebuild the index.
- **New fixed sentences on the site** (the two cards, the reach line, the Data page paragraph) were drafted by Claude and need a team read, like the texts in Step 8a.
- One commit holds all page changes (`app.js`, `styles.css`, `index.html`) instead of one per feature.
- Real phone and Firefox not tested.

## Next
Done: Victor pushed the branch and opened the pull request (tested locally by Victor, fine). Lama reviews and merges or drops it (see "Open decisions" in [[Decision log]]).
