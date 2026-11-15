# Step 15 - everything up to date before submission

_Sun 15 Nov 2026, about 20:17 to 20:24 by the machine clock. Claude Code in VS Code, for Lama. After this the code is frozen; Lama works on the slides._

## Merged
- `map-by-meaning` into `main` (`743bb57`) at Lama's word, after re-checking Status, open pull requests (none) and teammates' branches.

## Brought up to date (`7262f78`, live with cache version 27)
- **README:** every view described as it is now (overview with the problem in three steps and the route map; Explore with the map by meaning; Analysis with the next test; Open questions with the coverage chart; investigation pages with the closest by meaning); full folder and script list; the checks of the White Sands reader, the droplet model and the question labels; the map in the AI section; middle dots removed from the header.
- **Ask page:** briefly changed to plain frames (no middle dots, no left bars, no round labels), then **restored to Victor's design at Lama's request** (`09109b2`, cache version 28): "it wasnt a big deal to have something round".
- **Data page:** the White Sands paper and pypdf in the references; the map named in "How AI was used".
- **index.html:** the AI acknowledgement comment names the sorting of NASA's text and the in-browser model.
- **Vault:** project page draft (new checked numbers, tools, Use of SI no longer conditional), decision log (D26 confirmed, D27, D28), Status.

## Checked
- All checks pass: `build_dataset.py`, `validate.py`, `check_recount.cjs`, `check_model.cjs`, `check_ask.cjs`, `build_topics.mjs` (every quote).
- **Live site**, fresh Chrome profile: Overview, Habitat, Explore (all four tabs), Analysis, Ranking (both tabs), Open questions, Data, an investigation page, a comparison and the Ask page all render; no console errors; the Ask page shows Victor's design again (checked after the restore: renders, no errors).

## Still open (not code)
- A team member checks a sample of the AI labels (question labels, Ask test questions, word list).
- Project page text and the 7 slides (Lama).
