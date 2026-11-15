# Step 11c - search quality of the Ask page (Victor)

**Date:** Sun 15 Nov 2026, evening · **By:** Victor, with Claude Code (design, code, checks) after five directions proposed by Claude (desktop app). Repository `Data-Beyond-Space`, **branch `victor/ask-upgrade`, four more commits (`81724e2`, `fc42c03`, `776b67a`, `964aa86`) on top of Step 11b, not pushed by Claude: the open pull request updates when Victor pushes. Waiting for Lama.**

## Why
After Step 11b, matching by meaning barely beat matching by words (28 against 27 of 40 right first), and meaning alone scored 18. The language model added almost nothing. Goal: make the model earn its place, without fooling ourselves and without breaking the parts that need no model.

## What was done
1. **Split of the 40 test questions** (`scripts/split_eval.mjs`): seed 20261115, stratified, 20 tuning (6 everyday-word) and 20 held-out (5 everyday-word). Saved as `half` on each question in `data/content/ask_eval_questions.json`.
2. **Ranking options in `docs/ask.js`**, all off by default: a header on each passage before embedding (`name`: investigation, what burns, field; `attrs`: plus the sample from the checked attributes), investigations ranked by their best two passages, reciprocal rank fusion of the meaning and word rankings, a weight for title-only passages, and support for a second model (pooling, question prefix, display floor per model).
3. **`scripts/tune_ask.mjs`**: scores every combination for every model in `docs/models/` on the tuning half and prints the held-out half beside it. 180 combinations per model. Full table in `data/eval/ask_tuning.json`.
4. **Model switched to snowflake-arctic-embed-s** (Snowflake, Apache-2.0 confirmed on the model card: `license: apache-2.0` and its License section). Quantised ONNX file, 34.0 MB, served from `docs/models/Snowflake/snowflake-arctic-embed-s/`; CLS pooling; question prefix `Represent this sentence for searching relevant passages: ` on questions only; 384 numbers, normalised. Works in the browser with Transformers.js and WASM.
5. **Data and method page**: the score table now shows the held-out half beside the totals, meaning alone, words alone and the earlier model. The download size on the Ask page is counted by the build from the files served (62 MB; it was a typed "about 50 MB").

## Results
"First / in first three". A hit: a passage shown comes from one of the question's investigations. Questions are embedded one at a time, as the page does.

| Setting | Tuning (20) | Held-out (20) | All (40) |
|---|---|---|---|
| Words only, no model | 13 / 16 | 14 / 16 | 27 / 32 |
| MiniLM, meaning alone | 10 / 15 | 9 / 10 | 19 / 25 |
| **MiniLM, meaning + 0.2 word bonus (before this step)** | 15 / 16 | **13 / 16** | 28 / 32 |
| arctic, meaning alone | 11 / 14 | 14 / 17 | 25 / 31 |
| **arctic, meaning + 0.2 word bonus (the site now)** | 14 / 16 | **13 / 17** | 27 / 33 |

Other settings, tuning / held-out / all (title weight 0.9 unless said):

| Model | Header | Combining | Ranking | Tuning | Held-out | All |
|---|---|---|---|---|---|---|
| MiniLM | name | bonus 0.2 | passages | 13 / 15 | 13 / 15 | 26 / 30 |
| MiniLM | attrs | bonus 0.2 | passages | 13 / 15 | 12 / 16 | 25 / 31 |
| MiniLM | none | bonus 0.2 | investigations | 13 / 16 | 13 / 15 | 26 / 31 |
| MiniLM | none | RRF | passages | 13 / 16 | 11 / 17 | 24 / 33 |
| MiniLM | none | bonus 0.1 | passages | 12 / 16 | 11 / 14 | 23 / 30 |
| MiniLM | none | bonus 0.2, title 0.5 | passages | 15 / 16 | 13 / 15 | 28 / 31 |
| arctic | attrs | bonus 0.2 | passages | 15 / 17 | 12 / 19 | 27 / 36 |
| arctic | none | bonus 0.2 | investigations | 15 / 16 | 14 / 16 | 29 / 32 |
| arctic | attrs | bonus 0.2 | investigations | 15 / 16 | 16 / 19 | 31 / 35 |
| arctic | name | bonus 0.2 | passages | 14 / 17 | 14 / 18 | 28 / 35 |
| arctic | none | bonus 0.1 | passages | 12 / 15 | 14 / 17 | 26 / 32 |

All rows are from the final run, with each model's display floor (0.3 for MiniLM, 0.65 for arctic).

## What was decided, and by which rule
Rule fixed before looking: choose on the tuning half only; a one-question difference is a tie, and a tie keeps the simpler setting.

- **Headers, investigation ranking, RRF, title weight: not adopted.** For MiniLM none beats the existing setting on the tuning half. For arctic the best of them is one tuning question ahead of the plain setting, which is a tie. Smaller word bonuses (0.05, 0.1) are worse on the tuning half for both models.
- **Model: arctic.** With the word bonus the two models are level on the held-out half (13 / 17 against 13 / 16). By meaning alone arctic is far ahead (14 / 17 against 9 / 10 held-out; 25 / 31 against 19 / 25 in all). The earlier in-browser test that suggested arctic was also meaning-only. **This choice used the held-out half** (that was the instruction), so for the model the held-out half is not untouched. The Data page says so.
- **Display floor for arctic: 0.65.** arctic gives even unrelated questions a similarity near 0.5 to 0.6, so MiniLM's 0.3 would never hide anything. 0.65 lies below the first right passage of every tuning question (lowest 0.694) and hides "best pizza recipe in Naples" and similar. Cost: one held-out question lost its first-three hit.

## What was learned
- **The headline did not move.** With the word bonus, the site scores 27 / 33 of 40 now against 28 / 32 before, and words alone score 27 / 32. At first place the model still adds nothing measurable over words.
- **What did change:** the model alone is now about as good as words alone (25 / 31 against 27 / 32), where MiniLM alone was clearly worse (19 / 25). For questions that share no word with NASA's text, the model is the only thing that can match, and it is now much better at that.
- **Twenty questions cannot separate these settings.** Embedding the questions one at a time instead of in a batch moved some counts by one. Most differences in the tables are within that noise.
- **The split came late.** All 40 questions and the glossary were written by Claude, and the word bonus was chosen on all 40 in Step 11b.
- `attrs` headers plus investigation ranking look strong on the held-out half for arctic (16 / 19). It was not chosen, because the tuning half did not single it out. Worth a fresh test with questions a team member writes.
- "Related by meaning" on the investigation pages is now computed with arctic; its similarities are bunched high (about 0.92 to 0.98). The cross-link table in Step 11b was made with MiniLM and has not been redone.

## How it was checked
- `py scripts/build_dataset.py`, `py scripts/validate.py`, `node scripts/build_search.mjs`, `node scripts/eval_ask.mjs`, `node scripts/check_recount.cjs`, `node scripts/check_model.cjs`, `node scripts/check_ask.cjs`: all pass. CSVs restored.
- `check_ask.cjs` has five new checks (28 in all): the index was built with the model the site loads, that model is in `docs/models/`, the stated download size equals the files served, the split is balanced and recorded, the halves in `ask_eval.json` add up. No earlier expectation had to change: counted answers, evidence reach, Moon card, glossary and the word-matching score (27 / 32) are as before.
- Local site in the built-in browser: desktop, model loads and returns smoke-detector papers for the smoke-detector question; phone width, "Matching by words ... about 62 MB" then loads on tap; an unrelated question shows "Nothing ... matches that closely"; Data page table renders; no console errors. First-load time over a real connection was not measured (local load was about 2 seconds).

## How to run it
```
py scripts/build_dataset.py
py scripts/validate.py
npm install
node scripts/build_search.mjs
node scripts/tune_ask.mjs
node scripts/eval_ask.mjs
node scripts/check_ask.cjs
git restore docs/data/*.csv
```
To go back to MiniLM: set `SETTINGS.model` to `"Xenova/all-MiniLM-L6-v2"` in `docs/ask.js`, then `build_search.mjs`, `eval_ask.mjs`, `check_ask.cjs`. MiniLM's files are still in `docs/models/`.

## Not done, and open
- Labels and glossary are still Claude's and unchecked (as in Step 11b).
- The download grew from about 50 MB to 62 MB, and `docs/` holds both models (34 MB more in the repository).
- Real phone, Firefox and first-load time on the live site not tested.

## Next
Victor pushes; the open pull request updates. Lama decides on the model (see "Open decisions" in [[Decision log]]).
