# Step 7 - attribute matrix, Ask the records, reading lists outside PSI

_Sun 15 Nov 2026, about 10:50 to 11:30. Claude Code in VS Code, for Lama._

## What Lama asked for
After an honest look at technical depth against the judging criteria, Lama chose three additions ("okay lets do these") and set the bar: finalist quality, technically deep, but nothing a reader could find confusing.

## What was built (in `Data-Beyond-Space`, commit `0663cde`)
1. **All 24 investigations side by side.** New file `data/content/attributes.json`: for each investigation the sample or burner, what was varied, the airflow, what was measured (nine kinds, such as camera, temperature, gas, particles) and the use on Earth. The AI extracted these from NASA's record text. The build refuses any entry whose quotation is not found word for word in the NASA record, or whose table column does not exist. Shown as a second tab on the Ranking page (`#/rank/matrix`), on each investigation page, and as `attributes.csv`.
2. **Ask the records** (`#/ask`). The reader types a question and gets the best-matching sentences from NASA's records and from the papers PSI lists. A small open language model (all-MiniLM-L6-v2, 23 MB) runs in the reader's own browser through Transformers.js; it only matches, it writes nothing, and no question leaves the computer. 925 passages: 311 from NASA records, 614 from 235 papers (73 with an abstract). Word matching works at once; meaning matching takes over when the model has loaded. `scripts/build_search.mjs` prepares the passages.
3. **Where to read on, outside PSI.** Each of the six open questions now links to NASA reports on the NASA Technical Reports Server (eight in total, each checked by title). Links and titles only: no number is taken from them. This partly reverses D16 (PSI only on the site), at Lama's request; see D22.

## How it was checked
- `build_dataset.py`, `validate.py` and `check_recount.cjs` all pass.
- The Ask page was run in a real Chrome session: the model loads from the site's own files and gives meaning matches; a question unrelated to fire ("banana bread recipe") returns nothing.
- The matrix and Ask pages were looked at as screenshots at desktop width.

## Not checked, and one blocker
- **The push to GitHub is blocked.** GitHub's secret scanner flags a line in the library file `docs/vendor/transformers.min.js` as a "Mistral AI API key". It is a false alarm: the file is byte for byte the public npm package (same SHA-256), and the line holds model names such as "mistral". Only the repository owner can allow it. Until then the live site is still the Step 6 version.
- Not tested: the live site, phones, Firefox, Safari, real clicking.
- Search quality is good for the example questions but not perfect; it ranks passages, so a paper can come before the NASA record it belongs to.
- The AI-extracted attributes need a human read, like the summaries.

## Is the data enough? (Lama's question)
For what the site claims, yes: it uses every one of the 24 records and every row of the 22 tables, and its finding is about what PSI holds and does not hold. More data would not change that count. Thin spots: only 73 of 235 papers have an abstract, almost none for the solid-material investigations, so Ask is weaker there; the raw files and PSI documents are not read.

## Update, about 12:00
Lama allowed the flagged line on GitHub (false positive) and the push went through. All new files are served by GitHub Pages. In a fresh Chrome profile the live Ask page reached "Matching by meaning" within five seconds, gave results for a fire question and nothing for "banana bread recipe". Still not tested: phones, Firefox, Safari.
