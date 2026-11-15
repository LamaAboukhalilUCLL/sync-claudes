# Step 11a - two reading-list links on the Open questions page (Victor)

**Date:** Sun 15 Nov 2026, about 16:40 to 17:00 · **By:** Victor, with Claude (Cowork) for the search, the edit and the checks. Repository `Data-Beyond-Space`, file `data/content/interpretation.json`. **On branch `victor/reading-list-additions`, not merged: waiting for Lama.** Numbered 11a because it follows Lama's Step 11; it is not part of it.

## Why
Victor's search for data outside PSI (solids at 30 % oxygen or more, Moon gravity, habitat materials) found two NASA documents the site did not list. The White Sands 2007 table was already found by the team and is on the Habitat page (D25). Everything else found was left out to avoid clutter (list in [[References]] and the chat).

## What was changed
| Open question | Added to "NASA work on this outside PSI" | Why |
|---|---|---|
| Will cabin materials burn in Moon Base air? | NASA Engineering and Safety Center, *Impacts of Reduced Pressure Atmospheres on Environmental Control and Life Support Systems (ECLSS) Architectures*, NASA/TM-20260003925, May 2026 | NASA's own statement of the gap the site shows: "NASA has limited material flammability data at O2 concentration higher than 30%"; "Essentially all existing test data for flammability of flight materials are from 1-g testing" |
| Does Moon gravity change any of this? | Urban et al., *Solid Fuel Ignition Testing for Lunar Applications, Theory and Experimental Results*, ICES-2025-392 (conference paper, NTRS 20250002114) | Cabin materials at 8.2 psia, at White Sands (1-g) and in a drop-tower centrifuge at lunar gravity: "for some materials, there is a clear increased flammability at lunar gravity conditions", while "Other, higher temperature materials may show decreased flammability at lunar conditions" |

Links only: no number on the site comes from either document. The paper is linked rather than the slides (NTRS 20250006779), because the slides word the finding more strongly than the paper.

## How it was checked
- Both NTRS pages opened and their titles, years and document types match the entries.
- On a copy of `main` (`f841a17`) with the edit: `build_dataset.py`, `build_external.py`, `validate.py` (all 81 quotations, all DOIs) and `check_recount.cjs` pass. Only `interpretation.json` and `dataset.json` change for real; the three CSVs differ only in line endings and are not committed.
- The Open questions page rendered in headless Chromium: the materials question lists 4 links, the gravity question 3, no JavaScript errors.
- No script checks reading-list links; they were checked by hand.

## How to run it
```
py scripts/build_dataset.py
py scripts/validate.py
cd docs
py -m http.server 8000
```
Open questions: "Will cabin materials burn in Moon Base air?" and "Does Moon gravity change any of this?".

## Next
Lama reviews the branch and merges or drops it. Separately, the NESC sentence is offered to her for the project page text.
