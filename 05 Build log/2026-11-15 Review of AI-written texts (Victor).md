# Review of AI-written texts (Victor)

**Date:** Sun 15 Nov 2026, about 12:30 to 13:05 · **By:** Victor, with Claude (Cowork) for the first checks and the edits. Repository `Data-Beyond-Space`, files `data/content/interpretation.json` and `data/content/attributes.json`. **Changed locally, not committed or pushed: waiting for Lama's OK.**

## What was checked
The build already proves every quotation is NASA's wording and that no number is typed by hand. This review covered what a program cannot check:
1. Does the plain text say more than the quoted NASA sentence?
2. Is the label (aim, expected, result, stated) right for the field the quote comes from?
3. Is the quote fair once the whole NASA sentence around it is read?
4. The 24 "what they did" sentences and the six question answers, which have no quote behind them.
5. Does any text contradict the investigation's own table?
6. Is a caveat NASA states (preliminary, hypothesis) missing?

Covered: all 46 summary points (each against the full NASA sentence), all 24 "what they did" sentences (facts checked against records and tables), all six questions with their evidence, and a scan of the attribute matrix.

## What was changed (11 fixes, in 15 places)
| Where | Before | After | Why |
|---|---|---|---|
| Question "Can the Earth test...", Saffire-II evidence | "at near-normal oxygen the Earth burn is not the smaller one" | wherever the table gives both for the same material, it burned at least as far on Earth as in space, so near normal air the Earth test was on the safe side; no such comparison at 30 % or more | The double negative hid what the table shows, which cuts against the question's framing (see table PSI-99, rows 2-1 to 2-9) |
| Same question, answer | "...the comparisons that exist were made near normal air" | adds that the one direct comparison found the Earth burns at least as long | Same reason |
| Question "If a fire starts...", BRE evidence | "Stopping the airflow did not stop the flame" | "In still air, with no airflow at all, flames kept burning in higher-oxygen air" | BRE never stopped an airflow: it ran in still air throughout (PSI-20 objective, "quiescent") |
| Same question, answer | "one warning" | "one early warning ... NASA calls these results preliminary" | PSI-20 research impacts: "results are still preliminary" |
| Same question, new evidence line | - | "NASA calls these BRE results preliminary." (quote: "results are still preliminary") | Same |
| Question "Will cabin materials burn...", BASS-II evidence | "Oxygen was only lowered, never raised." | "Oxygen was kept at or below about normal air, by adding nitrogen." | BASS-II's own table goes up to 22.2 %, above 21 % |
| BASS-II summary point | "only varied downward from normal air" | same wording as above | Same |
| Saffire-II "what they did" | "in the same test on Earth" | "how far it burned on Earth" | The record compares with NASA's normal-gravity screening test, not the same test |
| PSI-62 summary point | "predict whether a spacecraft material will burn" | "predict the flammability limits of spacecraft materials" | Matches the quote |
| CFI-G summary point | "Cool flames are a recent discovery." | "Cool diffusion flames were only discovered recently." | The record says cool *diffusion* flames were discovered in 2012; cool flames in general are much older |
| CFI-G summary point | "The purpose is better engines, not fire safety." | "Its record names engines as the purpose and never mentions fire safety." | Checked: no field of PSI-159 mentions fire, safety, spacecraft or crew |
| BRE summary, new point (stated) | - | "NASA calls these results preliminary." | The summary stated the still-air finding as a plain result |
| Flame Design summary point | "A perfectly round flame can hold steady" | "A round flame can burn steadily in weightlessness." | The record says "steady-state spherical diffusion flames are possible" |
| PSI-142 summary point | warm flame "governs the switch" | "plays a key role in the switch" | The record says "plays a critical role" |
| FLEX-2 attribute, airflow | "A slow flow made by moving the droplet" | "A slow flow; its speed is in the table" | The source is only a column name, which does not say how the flow was made |

Six fixes came from the first pass, five from the full read of all 46 points; some fixes touch two places.

## Checked and left as written
- The other 40 summary points match their NASA sentences; hypotheses are labelled "expected", results are results.
- "What they did" facts verified: Saffire-I sample about 0.94 m long (record), SAME-R five materials (table), DAFT used Arizona Red Dust (record), BASS used nitrogen as extinguishing gas (record), CFI burned dodecane mixtures (table), CFI-G holds the only tests inside the Moon Base zone (computed).
- BASS-II "may not be on the safe side" is labelled "stated" although it comes from the hypothesis field; defensible as NASA's own assessment of its screening test. Lama may prefer "expected".
- Noticed, not changed: Saffire-I's table lists length 40.6 cm and width 94 cm, Saffire-III's the other way round; the record says 0.94 m long. Shown as NASA wrote it.

## How it was tested
The team's own scripts were run on a copy with the edited files: `build_dataset.py` passes; `validate.py` passes all checks ("all 81 quotations are word for word", previously 79: the two new "preliminary" quotes). Headline numbers unchanged (659, 20, 13.6 to 22.2 %, 876, 270). The edited pages were not yet looked at in a browser.

## How to run it
From the `Data-Beyond-Space` repository:
```
py scripts/build_dataset.py
py scripts/validate.py
cd docs
py -m http.server 8000
```
Pages to look at: Open questions ("Can the Earth test...", "If a fire starts...", "Will cabin materials burn..."), and the investigation pages of BASS-II, Saffire-II, BRE, CFI-G, Flame Design, PSI-62, PSI-142.

## Learned
- The quote check is strong, but the risk sat in the plain wording around the quotes and in sentences without a quote.
- One possible addition, not made: CFI-G's table records for each test whether the flame self-extinguished (`SE`) or was still burning when the fuel was cut (`FT`). Below 25 % oxygen all 41 ignited flames self-extinguished; at about 40 % oxygen 29 of 89 were still burning. That is table evidence for the still-air point now resting on BRE's text. It would need a new computed value in the build; Lama's call.

## Next
1. Lama reviews these edits (this note, or `git diff` in `Data-Beyond-Space`).
2. With her OK: rebuild, validate, commit, push.
