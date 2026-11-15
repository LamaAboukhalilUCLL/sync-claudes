# Step 6 - choose an atmosphere, and a finder for materials and tests

**Date:** Sun 15 Nov 2026, 10:46 · **By:** Claude Code (VS Code); the two features were chosen by Lama from a list of six. Repository `Data-Beyond-Space`, branch `main`, commit `6fce490`, pushed and live.

## Why
The site showed one finding for one fixed question (the Moon Base). Lama wanted it to feel useful, with less scrolling. Options considered and not built: full RAG with a language model (needs a key and a server, thin source text for solids), an MCP server, and a predictive ML model (the data covers droplets and gas only, so predictions for solids or the Moon would not be valid).

## What was built
1. **Choose an atmosphere.** Presets: Moon Base and pressurized rovers (default), the three cabin atmospheres named in PSI record PSI-20 (34 % at 8.2 psia, 26.5 % at 10.2 psia, 21 % at 14.7 psia), a spacesuit (100 % at 4.3 psi), or the reader's own oxygen and pressure. "At least this much oxygen, at most this much pressure." The three key figures, the charts, the ranking and the investigation pages all follow the choice. A link can carry it, for example `#/explore/pressure?atm=c34`.
2. **Explore page** (replaces "Coverage map"): three tabs in one frame.
   - Oxygen, by what burns (every test, one lane per kind of fuel).
   - Oxygen against pressure (the chosen air is a red frame).
   - Find a material or a test: searches all 1,982 table rows as NASA wrote them, says how many are in the chosen air and for how many NASA's table does not say enough to tell, opens NASA's table at the row, and downloads the filtered rows as CSV.
3. **Less scrolling.** Shorter overview that leads into the tool; tabs instead of stacked charts; questions and long sections open on demand.

## How the numbers stay honest
- The preset figures are quoted from NASA: the build refuses to run unless "8.2 psia, 34 % oxygen", "10.2 psia, 26.5 %" and "14.7 psia, 21 % oxygen" are found word for word in the PSI-20 record. The Moon Base and spacesuit figures are from the challenge statement.
- The Moon Base numbers are still computed by the build. Other atmospheres are recounted in the browser by `docs/recount.js` with the same rules.
- New check `scripts/check_recount.js`: the recount must equal the build for the Moon Base, number for number, for all 24 investigations. It passes. Writing it caught one flaw: the build printed FLEX's lowest pressure as "10.2 psi" when it is 10.18; the build now prints two decimals.
- `tests.json` now holds every table row that names a fuel or material (1,982), not only the rows that state oxygen or pressure (1,205).

## Design notes
- Chart colours were re-picked from NASA's dark-background palette (solid `#f29d49`, droplets `#609af6`, gas flames `#0cc9ac`, burner emulating solids `#f5af0c`) after a palette checker showed the earlier slate and blue were hard to tell apart.
- Files now carry a version in their address, so a browser cannot mix an old script with new data. This was the cause of pages looking stale after an update.

## How it was tested
Build, `validate.py` and `check_recount.js` pass. Headless Chrome screenshots at 1440 px: overview with the Moon Base and with the spacesuit, explorer tabs with the Moon Base and with the 8.2 psia cabin, ranking with Earth air, questions, an investigation page. **Not tested:** a person clicking and typing (the finder's search box, the own-atmosphere inputs, the CSV download), phones, Firefox and Safari.

## Next
Lama tries it. Then the project page text and the demo, which are still not written.
