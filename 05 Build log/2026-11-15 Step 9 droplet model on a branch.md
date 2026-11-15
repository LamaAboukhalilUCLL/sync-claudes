# Step 9 - a checked statistical model of the FLEX droplet tests (branch `droplet-model`, not merged)

_Sun 15 Nov 2026, about 15:20 to 16:05. Claude Code in VS Code, for Lama._

## What Lama asked for
More technical depth that is correct and useful for NASA engineers, on a new branch, with freedom to choose the most useful thing. She found the Ask page too simple ("just returning documents").

## Why this and not a bigger language model
Looking at all 22 tables, only one holds both high oxygen and an outcome for every test: **FLEX (PSI-69)**, 274 droplet tests with oxygen, pressure, carbon dioxide, helium, droplet size, burning rate and how the test ended. That allows real data analysis, which a chatbot would not add. No external data was used.

## A finding that touches our headline number
17 FLEX tests ran at 30 % or 34 % oxygen and **10.33 to 10.5 psi**. They miss the challenge limit of 10.2 psi by 0.1 to 0.3 psi, so the strict count ("20 of 659 in Moon Base air, all gas flames") leaves them out. The count is right by the rule, but an engineer would call these tests Moon Base air. The overview counter now adds: "17 more miss the pressure limit by 0.5 psi or less (FLEX)".

## What was built (commit `d2e9403` on branch `droplet-model`)
- `scripts/analyze_flex.py`: ordinary least squares, one model per fuel (heptane, methanol): burning rate = constant + oxygen + carbon dioxide + helium + pressure + droplet size. Standard library only. Reports confidence limits, the error when one test or one whole test day is hidden, and plain counts of how tests ended by oxygen band.
- `scripts/check_model.cjs`: a separate JavaScript program that reads NASA's CSV again, refits the model and fails unless it gets the same numbers. It caught a rounding inconsistency during the build, which was fixed.
- New **Analysis** page: three findings, an estimator with sliders (estimate, 95 % range, inside or outside what FLEX tested, the five nearest real tests with links to NASA's rows), a chart, a table of how tests ended, a validation table, a coefficient table, method and limits.

## Results (from the build output)
- Heptane: 105 tests, 71 % of variation explained, error with a day hidden 0.097 against 0.154 for guessing the average. Oxygen: +0.024 per point (95 % range 0.020 to 0.029).
- Methanol: 148 tests, 88 % explained, error 0.041 against 0.109. Oxygen: +0.018 per point.
- At 30 % oxygen or more, 0 of 10 heptane flames and 2 of 13 methanol flames went out on their own; below 21 % it was 37 of 53 and 85 of 87.
- Carbon dioxide lowers the burning rate, helium raises it.

## What was tried and dropped
A second model, for the share of fuel left when the flame went out. Dropped because that share only exists for tests that ended in extinction, and at 30 % oxygen almost none did; a straight line then gave impossible values (below zero). Replaced by the plain counts of how tests ended.

## Limits, stated on the page
Fuel droplets in weightlessness only; not solids, not Moon gravity. NASA chose the test conditions, so this is description, not causal proof. The unit of "Burning rate; mm" is not completed in NASA's table. "Disruption" is NASA's label and is not explained in the table.

## For Lama to decide
1. **Merge or not.** The page gives model estimates. D12 said "coverage and gaps, not predictions". The estimates are for droplets only, inside tested conditions, with ranges and the real tests beside them, but it is still a step beyond D12.
2. **The 17 near-miss tests**: keep the strict headline with the added sentence (as built), or change the headline.
3. Not built: the answer finder for the Ask page and the measured search quality.

## Checked
All five programs pass: build, validate, recount check, model fit, model check. The page was driven in a real Chrome session: sliders, fuel switch and "NASA's row" all work. Not checked: phones, other browsers.
