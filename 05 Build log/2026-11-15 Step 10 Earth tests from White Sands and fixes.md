# Step 10 - Earth tests at Moon Base pressure (NASA White Sands), and three text fixes

_Sun 15 Nov 2026, about 15:42 to 15:55. Claude Code in VS Code, for Lama. Branch `droplet-model`, commit `e67c5c7`, not merged._

## What Lama asked for
Her idea: look for data from NASA partners or research centres about solid materials at 30 % oxygen or more, about the Moon, and about which materials habitats use. Then: "finish it and apply the fixes", and she merges after.

## What the search found
- **NASA White Sands Test Facility, 2007** (Hirsch et al., NTRS 20070018178, public use permitted): 26 material samples tested on Earth in NASA's upward-flame test at 70.1 kPa (10.17 psi), with the highest oxygen level at which each still put itself out. This is the find.
- **NASA Johnson, 2026** (fire-resistant textiles, NTRS 20260003042): says the lunar and Mars surface atmosphere was set in 2021 at 8.2 psia and 33.7 % oxygen, textiles are certified at 37 %, the space station uses Kevlar, Nomex, Vectran and blends, and very few textiles pass at 37 % and 8.2 psia. No large table. Already in our reading list.
- **Moon gravity**: no fire test on the Moon yet (FM2 is planned); LUCI burned materials in simulated lunar gravity on a rocket. Slides only skimmed; link only.
- **Not found**: an official list of lunar habitat materials; open Saffire IV to VI data (restricted); MAPTIS needs an access request.

## What was built
- `data/external/wstf2007/`: the PDF as downloaded, its text (extracted with pypdf 7.1.0), checksums, and `source.json` with the 26 sample names as printed.
- `scripts/build_external.py`: reads both numbers of every row from the paper's text. It stops if a name is not found exactly once, a number cannot be read, a quoted sentence is not in the paper, or a file changed. **No threshold is typed by hand.** All 26 rows were also compared by eye with the PDF text.
- Habitat page, new lower part "On Earth, solids were tested at Moon Base pressure": follows the chosen air. At 30 % oxygen: 19 of 26 put themselves out, 7 did not (Lexan 6006, P1700, three Nomex configurations, two graphite/epoxy laminates), against 0 of 129 solid-material tests in PSI. Warns when the chosen pressure differs from 10.17 psi.

## Fixes applied
1. **Near misses in the texts and summary.** The summary now has `rows_near_zone` (17), computed by the build and recounted by `validate.py`. The answer to "Has any fire been tested in Moon Base air at all?" and its FLEX evidence line now say that 17 FLEX tests ran at 30 % oxygen or more and 10.33 to 10.5 psi.
2. **Saffire-II**: "as long" is now "as far" (the table gives lengths), and "the Earth test was on the safe side" is now "the burn on Earth was the larger one" (the table does not say the 1-g burn was NASA's approval test).
3. The label "Disruption" is no longer explained by us; the page says NASA's table does not explain it.

## Limits to keep in mind
- The White Sands tests are **Earth gravity**. The materials were candidates for the Constellation programme (2007), not a Moon Base list.
- Our reading assumes a sample that passes at one oxygen level passes at lower ones, and one that fails also fails at higher ones. The page says so.
- This is a second source on the site. D16 (PSI only) is now reversed for this one table; see D25.

## Checked
All seven programs pass: `build_dataset.py`, `build_external.py`, `validate.py`, `check_recount.cjs`, `analyze_flex.py`, `check_model.cjs`, and `node --check` on the site code. Screenshots of the Habitat page at 30 % and at 34 % oxygen, 8.2 psi looked right. Not checked: phones, other browsers, the live site (the branch is not merged).
