# Step 14 - the next test that would teach the most (idea 2), merged and live

_Sun 15 Nov 2026, about 19:55 to 20:00 by the machine clock. Claude Code in VS Code, for Lama._

## What Lama asked for
"merge, and do idea 2". Before that, `si-coverage-2` (Step 12 re-applied) was merged into `main` after re-checking Status, open pull requests (none) and teammates' branches; all checks passed; live with cache version 24.

## What was built (commit on branch `next-test`)
On the Analysis page, a new section for the condition set with the sliders (it starts at the chosen atmosphere):
- Every condition FLEX's hardware covered for that fuel (oxygen in 1-point steps, 35 pressures, 9 droplet sizes, nitrogen only) is ranked by how much one more test there would narrow the 95 % range of the model's estimated average at the chosen condition.
- Exact algebra: adding a test at x changes (X'X)^-1 by the Sherman-Morrison formula, so the leverage at the target drops from h0 to h0 - (x0'Ax)^2/(1+x'Ax). Assumes the straight-line model holds and the scatter stays as it is. In `docs/model.js` (`nextTest`, `testsToShrink`).
- `scripts/check_model.cjs` verifies it independently: it adds the extra row to X'X, solves again, and must get the same leverage; it also checks that the reported number of tests really halves the range.
- Three tiles (best next test and how much it narrows; a test in a far air for comparison; how far tests at one condition can go) and a map over the tested oxygen and pressure.

## Results (heptane droplets, Moon Base air, median droplet size)
- Today: estimate 0.72, average known to within plus or minus 0.043 (95 %).
- Best single next test: 34 % oxygen, 10.21 psi, 1.13 mm droplet: narrows the range by **6.0 %**.
- One test in Earth air: **0.5 %**.
- However many tests at one condition: the range cannot go below **57 %** of today's; varied conditions are needed.
- Methanol, same condition: best test narrows by 4 %.
- Reading: the droplet data near Moon Base air is already fairly dense; more droplet tests add little. The gap is solid materials, where no test at 30 % oxygen exists and any test would be the first. The page says so.

## Checked
All checks pass (build, validate, recount, model check with the new verification, Ask check). In Chrome: tiles and map render, they follow the sliders and the fuel switch, no console errors.

**Merged** at Lama's word: `next-test` fast-forwarded into `main` (`9ade543`) after re-checking Status, open pull requests (none) and teammates' branches; all checks passed; live with cache version 25. On the live site, in a fresh Chrome profile, the section shows the same numbers, follows the sliders and the fuel switch, and logs no errors.
