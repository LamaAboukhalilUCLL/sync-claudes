# Step 5b - redesign and Moon backdrop

**Date:** Sun 15 Nov 2026, 01:27 · **By:** Claude Code (VS Code), asked by Lama. Repository `Data-Beyond-Space`, branch `main`, commit `29d3921` and one small follow-up, pushed. Live at https://lamaaboukhalilucll.github.io/Data-Beyond-Space/

## Review of Mylene's work first
Her branch `research-gaps-on-site` (commit `08ade33`) was merged into `main` by Lama through pull request 1.
- Rebuilt and validated after the merge: all checks pass, no script errors.
- Her wording corrections are right: "Solid-material evidence stops before Moon Base air", not all evidence.
- Removing the "Beyond PSI" page keeps rule 6 (every figure from PSI).
- The Moon photo is properly sourced: the original file's checksum matches the one she recorded.
- The live site answered and served the data and table files.

## What was changed, on Lama's brief
Brief: look like the reference designs (dark, photographic, calm), a Moon in the background, very easy to navigate, **no neon or "AI" look**, fit for NASA.
1. **New visual style.** Near-black background, off-white text, one warm accent, quieter fuel colours, plain rectangular buttons, thin uppercase navigation with an underline for the current page. The glow on the Moon Base line and the coloured gradients were removed.
2. **Moon behind every page.** The full Lunar Reconnaissance Orbiter near-side mosaic (same public-domain source Mylene chose), strong on the overview and faint elsewhere. Credited in the footer of every page, on the Data page, in the README and in `docs/img/CREDITS.md`. The earlier cropped strip was removed.
3. **Overview rebuilt for a first-time visitor.** Headline with three key numbers beside it; "01 The gap in one picture" (Mylene's range-bar chart); "02 From Earth to the Moon Base"; "03 Explore" with three numbered ways in. Footer navigation on every page.
4. **The journey (answer to the "map on the Moon" idea).** Three stops to click: Earth (5 ground studies), Low Earth orbit (19 flight investigations), Moon Base (0 of 24 records mention it). Each stop lists its investigations and the facts for that place, all computed from the dataset.

## Why not a clickable map of the Moon's surface
PSI data has no locations on the Moon: no test was run there. Points on a lunar map would suggest places where something was measured, which would be invented. The journey shows the same thing honestly: where the evidence was gathered and where it is needed.

## How it was tested
Headless Chrome screenshots at 1440 px of the overview, ranking, questions, coverage map and an investigation page. **Not tested:** a person clicking the journey stops, phones, Firefox and Safari.

## Next
- Lama: look at the live site; say what to change.
- Still open: D14 (ranking rule), review of the AI-written texts, project name, project page text and demo.
