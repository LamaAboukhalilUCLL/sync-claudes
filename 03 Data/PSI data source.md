# PSI data source

NASA's Physical Sciences Informatics repository: https://psi.nasa.gov/physci/repo/search?q=combustion
No login needed. License on the records checked: CC0-1.0. **Cite each investigation by DOI.**

## What one investigation contains
- **Description:** project type, flight platform, dates, objective, approach, hypothesis, research impacts, sub-research area, related investigations, hardware.
- **Experimental Table:** a small CSV, one row per test.
- **Publications** with DOIs.
- **Data files:** documents, reports, raw data. Raw data is huge (BASS-II 275 GB, FLEX 924 GB, ACME CFI-G 2,086 GB). **Do not download raw data.**

## The JSON endpoints the PSI website itself uses
Found by watching the site's own network requests on 14 Nov 2026. They are not a documented public API, so they may change.
- Search: `https://psi.nasa.gov/geode-py/ws/repo/search?term=combustion&source=psi&type=investigation&sort=Public%20Release%20Date&order=desc` (returns 25 per page; add `&size=50` to get all 26 hits. 24 are Combustion Science; PSI-181 is Materials Science and PSI-108 is Fluid Physics. The hit on the second page is PSI-47, DAFT.)
- One investigation: `https://psi.nasa.gov/geode-py/ws/repo/investigations/PSI-25`
  - useful fields: `title`, `investigationAcronym`, `doi`, `projectType`, `flightProgram`, `subResearchArea`, `experimentHardware`, `objective`, `approach`, `hypothesis`, `researchImpacts`, `publications[]`, `related_glds`, `experimentalTable[]`, `totalFileSize`, `licenseIdentifier`
- Experimental table CSV: `https://psi.nasa.gov/geode-py/ws/studies/PSI-25/download?file=<file_name>&version=<version>&redirect=false`
  - This does not return the file. It returns a **temporary download link** (valid for a short time, containing short-lived access keys). The script follows the link and never saves it.

## The snapshot (14 Nov 2026)
`app/fetch_snapshot.py` saved an untouched copy of all of this in `app/raw/`, which is committed to git: `search.json`, 24 investigation records, 22 Experimental Tables, and `manifest.json` (source URL, time, size and SHA-256 of every file). Every number in our notes and app must trace back to these files.

## What the Experimental Tables hold (verified against the snapshot)
Full detail, every odd cell and every header: [[Oxygen evidence (generated)]]. Ranges below are exactly as the tables state them, units included.

**Ambient oxygen** is the atmosphere around the flame. **Burner-flow oxygen** is oxygen blown out of the burner into a fuel atmosphere ("inverse" flames). They are separate fields and must never be mixed.

| Investigation | Table | Rows | Ambient oxygen before test | Burner-flow oxygen | Pressure | Other useful columns |
|---|---|---|---|---|---|---|
| FLEX | 1 | 274 | 0.12-0.34 mole fraction | - | 0-2,319.9 mmHg (the 0 is as written; next lowest 526.3) | fuel, N, CO, He fractions, droplet diameter, extinction diameter, test end |
| ACME CFI-G | Normal flames | 179 | 0.1797-0.3997 mole fraction | - | 0.507-3.04 bar | fuel, cool flame?, hot ignition, self-extinction |
| ACME CFI-G | Inverse flames | 154 | - (atmosphere is fuel) | 0.12-0.85 mole fraction | 0.495-3.31 bar | fuel, hot ignition, colour |
| ACME Flame Design | Normal flame | 207 | 0.198-0.40 mole fraction | - | 0.93-1.30 atm | fuel (C2H4, C3H8), flow rates, adiabatic temperature |
| ACME Flame Design | Inverse flame | 120 | - (atmosphere is C2H4) | 0.212-0.85 mole fraction, plus `RAMP` x9, `LOW O2` x2 | 0.42-3.01 atm | flow rates |
| BASS-II | 1 | 129 | 13.6-22.2 % by volume | - | not in table | fuel sample material (51 distinct), flow settings, final O2, CO2, CO |
| BASS | 1 | 122 | not in table | - | not in table | fuel sample material (34 distinct spellings: PMMA spheres, SIBAL, wax candle ...) |
| SPICE | 1 | 469 | not in table | - | not in table | fuel (propylene, propane, ethylene, methane), nozzle, fuel rate, air rate |
| SAME-R | 1 | 109 | not in table | - | not in table | sample type, inlet velocity |
| CFI | 1 | 87 | 0.17 (24 rows) and 0.21 (63 rows) | - | `0.5 atm` to `5 atm` (text) | fuel, nitrogen, helium |
| ACME CLD Flame | 1 | 32 | not in table | - | not in table | test type, fuel bottle, fuel concentration |
| ACME E-FIELD Flames | 1 | 32 | not in table | - | not in table | mesh polarity, fuel |
| ACME BRE | 1 | 18 (one per test day) | lists from `21; 26.5; 34` to `25; 34; 40` percent in 16 rows; `3400%` and `2100%` in 2 rows | - | not in table (note says it was varied) | burner size, fuel bottle, flames ignited |
| ACME s-Flame | 1 | 18 (one per test day) | text: `~21% O2 ...` in 10 rows, `~30% O2 ...` in 3, `~30% and ~21% O2 with He` in 5 | - | note: about 1 atm | fuel bottle |
| Saffire-II | 1 | 15 (9 samples, 2 flow-visualization rows, 4 note rows) | `~ 21.5`, `~ 22.1`, `22.1 to 22.0`, `22.0 to 21.9` percent | - | not in table | material (silicone, SIBAL, PMMA, Nomex), 20 cm/s, burn length in 0 g and 1 g |
| SLICE | 1 | 12 | not in table | - | not in table | fuel type |
| SAME | 1 | 8 | not in table | - | not in table | sample material, air flow |
| FLEX-2 | 1 | 8 (one per fuel) | `0.17; 0.21;0.25; 0.3` mole fraction in every row | - | `0.5; 1.0; 1.5; 2.0; or 3.0` atm | fuel, droplet diameter, flow velocity |
| Cool-flame transitions (ground, PSI-142) | 1 | 8 | - | - | - | pointers to figures in publications |
| Saffire-I | 1 | 4 (2 samples, 2 flow-visualization rows) | `21.5 - 21.7` and `~ 21.5` percent | - | not in table | SIBAL fabric, 20 cm/s |
| Saffire-III | 1 | 2 | not in table | - | not in table | SIBAL fabric, 30 cm/s |
| DAFT / DAFT-2 | 1 | 2 | - | - | - | dust sampling sessions |
| 4 ground studies (PSI-60, 62, 115, 117) | no table | | | | | |

## Corrections to the first look
- CFI-G and Flame Design each have **two** tables (normal and inverse flames). The first look read only the normal ones.
- The "up to 85% oxygen" in CFI-G is **burner-flow** oxygen in inverse flames (79 of 154 rows at 0.85). Its ambient oxygen tops out at 0.3997. Flame Design also reaches 0.85 burner-flow oxygen.
- BRE has two odd cells, `3400%` and `2100%`, not one.
- BASS-II final oxygen has two odd values, 39.1 (test P22b) and 40.4 (test T28b), where the initial oxygen was 20 and 20.7. Shown as written; not used.

## Quirks seen
- Oxygen is given as percent in some tables and mole fraction in others.
- Pressure units vary: mmHg, bar, atm, and text such as `1 atm`.
- Some cells hold several values (`0.17; 0.21;0.25; 0.3`) or text (`~30% and ~21% O2 with He`).
- A row is not always one test: BRE and s-Flame rows are test days, FLEX-2 rows are fuels, E-FIELD has continuation rows.
- Saffire tables include rows that are not burn tests (flow visualization, notes).
- Spreadsheet drag-fill damage: s-Flame has `N3`, `N4`, `N5`, `N6` where `N2` is meant; CLD Flame has `CH5`, `CH6`.
- SPICE's first two rows are identical. FLEX is encoded in Windows-1252, the others in UTF-8.
- CFI-G inverse table has 861 blank rows after the data and two `#VALUE!` cells.
- PSI-10 (Flame Design) has a blank license field; the other 23 say CC0-1.0.

## The oxygen pattern: what the snapshot shows (facts only; the insight is Lama's decision)
First surfaced by Claude on 14 Nov, then checked here.
- **Solids, ambient oxygen stated:** BASS-II 13.6-22.2 % (0 of 129 rows at 30 % or more); Saffire-I about 21.5 %; Saffire-II about 21.5-22.1 %.
- **Solids, ambient oxygen not stated in the table:** BASS, Saffire-III. So for these the pattern is **unverified from the tables**, not confirmed. BASS-II's approach text says "oxygen varied below 21% by adding nitrogen".
- **Ambient oxygen at 30 % or more:** FLEX (24 of 274 rows, up to 34 %), FLEX-2 (30 % listed for every fuel), CFI-G normal flames (115 of 179 rows, up to 40 %), Flame Design normal flames (131 of 207, up to 40 %), BRE (34 or 40 % listed on all 16 readable test days), s-Flame (about 30 % on 8 of 18 test days). All are gases or liquid droplets.
- **BRE is a special case:** it is a gas burner built to emulate burning solids and liquids. Its objective text names the "NASA - considered atmosphere for human space missions": 14.7 psia with 21 % oxygen, 10.2 psia with 26.5 %, and 8.2 psia with 34 %. This is a PSI source for the 34 % / 8.2 psi figure used in the draft.
- **Not checked:** the investigation documents and publications behind each record (only metadata and tables are in the snapshot).
