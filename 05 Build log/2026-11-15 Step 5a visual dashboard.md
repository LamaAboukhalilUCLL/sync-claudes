# Step 5a - visual dashboard

**Date:** Sun 15 Nov 2026 · **By:** Claude Code (VS Code), asked by Mylene. Repository `Data-Beyond-Space`, branch `research-gaps-on-site`, commit `08ade33` (not pushed, not merged). **Needs Lama's approval before it is merged into `main`.**

## What was done, in order
1. **A "Beyond PSI" page was built and then removed.** It added habitat targets from NASA technical reports (33.7 % and 37 % oxygen at 8.2 psia) and five findings from outside PSI (Saffire-VI, SoFIE-GEL, a BASS-II poster result, LUCI, FM2), with quotations checked against the saved report text. Mylene removed it: it broke the rule that every figure comes from PSI, and it was too much text. **Nothing from outside PSI is on the site.**
2. **The dashboard was made visual.** Mylene found it overwhelming and text-heavy. Six changes, all from data the site already had:
   - **Overview** rebuilt after a design mockup Mylene made with ChatGPT: headline "Solid-material evidence stops before Moon Base air.", a range-bar chart (lowest to highest ambient oxygen per fuel type, against Earth air 21 % and the Moon Base 30 % line), three number tiles, the explanation behind "How to read this".
   - **Ranking** as a colour grid: one square per condition (met, half, not met, not stated). Click a row for the evidence.
   - **Open questions** as six tiles: red open, amber partly answered.
   - **Investigation pages** start with tiles: what burns, where tested, small oxygen and pressure range bars against the Moon Base lines.
   - **Coverage map**: shorter text; the "85 %" explanation is now a toggle.
   - **Phones**: charts are redrawn for narrow screens. Before, they kept a fixed width and scrolled inside their box, so the Moon Base zone was cut off.
3. **Moon photo** at the bottom of the overview: a crop of the Lunar Reconnaissance Orbiter near-side mosaic (NASA/GSFC/Arizona State University, public domain), https://commons.wikimedia.org/wiki/File:Moon_nearside_LRO_5000.jpg . Credited under the photo, on the Data page, in the README and in `docs/img/CREDITS.md` (with the checksum of the original and how it was cropped). It is a real photo, not the AI picture from the mockup, so no watermark is needed.

## Wording kept honest
- The mockup's headline "The evidence stops before Moon Base air" was changed to "**Solid-material** evidence stops before Moon Base air": droplets reach 34 % and gas flames 40 %.
- A first draft said "NASA never burned a solid material in that air". That is false outside PSI (Saffire-VI burned fabric at about 31 %), so the site only says what PSI's tables state. Two solid investigations (BASS, Saffire-III) state no oxygen; Saffire-I and II state it only as text.
- The gas bar starts at 17.97 %, the computed value (the mockup said 18 %).

## How to run it
```
cd Data-Beyond-Space
git switch research-gaps-on-site
py scripts/build_dataset.py
py scripts/validate.py        # all checks pass
cd docs
py -m http.server 8000        # open http://localhost:8000
```
No Node.js or other install is needed.

## How it was tested
Headless Chrome screenshots of every page at desktop width and inside a true 390 px phone frame; no script errors on any page; a click test (ranking row opens and closes its evidence, a question tile jumps to and highlights its answer). **Not tested:** a person clicking through, Firefox and Safari, a real phone.

## What was learned
- Earlier "pages scroll sideways on phones" was wrong: headless Chrome cannot make its window that narrow. The real phone bug was inside the charts.
- Research base note `02 Domain/Flame in Freefall research base.md` has two errors found while checking sources: Saffire-VI's alarm level was reached at **981 s** (ICES-2024-365), not 344 s; and the FM2 quote is "expected to be substantially worse than in 0-g and potentially worse than even 1-g".

## Commits
Commits are authored by Mylene alone (repository-local git name and email). AI use is acknowledged in the README "Use of AI" section, on the site's Data page, and in [[SI use log]].

## Next
- **Lama:** approve or change the visual design, then merge through a pull request.
- Push the branch and open the pull request (Mylene's go).
- Step 6: make the repository public, switch on GitHub Pages, project page text, demo.
