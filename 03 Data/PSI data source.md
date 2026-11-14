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
- Search: `https://psi.nasa.gov/geode-py/ws/repo/search?term=combustion&source=psi&type=investigation&sort=Public%20Release%20Date&order=desc` (returns 25 per page; 26 hits, some not Combustion Science)
- One investigation: `https://psi.nasa.gov/geode-py/ws/repo/investigations/PSI-25`
  - useful fields: `title`, `investigationAcronym`, `doi`, `projectType`, `flightProgram`, `subResearchArea`, `experimentHardware`, `objective`, `approach`, `hypothesis`, `researchImpacts`, `publications[]`, `related_glds`, `experimentalTable[]`, `totalFileSize`, `licenseIdentifier`
- Experimental table CSV: `https://psi.nasa.gov/geode-py/ws/studies/PSI-25/download?file=<file_name>&version=<version>&redirect=false`

## What the Experimental Tables hold (first look, 14 Nov)
Read in the browser from the live CSVs. Ranges are as the tables state them; **to be re-verified by the pipeline in Step 2**.

| Investigation | Rows | Oxygen (ambient) | Pressure | Other useful columns |
|---|---|---|---|---|
| FLEX | 274 | 0.12-0.34 mole fraction | up to 2,320 mmHg | fuel (methanol, heptane), CO2 and He fractions, droplet diameter, extinction diameter, test end |
| ACME CFI-G | 179 | 0.18-0.40 | 0.5-3.0 bar | fuel, cool flame?, hot ignition, self-extinction |
| ACME Flame Design | 207 | 0.198-0.40 | 0.93-1.30 atm | fuel (C2H4, C3H8), flow rates, adiabatic temperature |
| BASS-II | 129 | 13.6-22.2 % initial | not listed | fuel sample material (51 kinds: PMMA rods and films, SIBAL fabric), flow settings, CO2, CO |
| BASS | 122 | not listed | not listed | fuel sample material (PMMA spheres, SIBAL, wax candle) |
| SPICE | 469 | not listed | not listed | fuel, nozzle, fuel rate, air rate |
| SAME-R | 109 | not listed | not listed | sample type (Kapton, silicone, lampwick, Pyrell, Teflon), inlet velocity |
| CFI | 87 | 0.17-0.21 | 0.5-5 atm | fuel, helium, nitrogen |
| ACME CLD Flame | 32 | not listed | not listed | test type, fuel bottle |
| ACME E-FIELD Flames | 32 | not listed | not listed | mesh polarity, fuel |
| ACME BRE | 18 | 21-40 % (listed per test day) | not listed | burner size, fuel |
| ACME s-Flame | 18 | about 21 % and 30 % | not listed | atmosphere, fuel |
| Saffire-II | 15 | has a "Percent O2" column, not yet read | not listed | material (silicone, SIBAL, PMMA, Nomex), 20 cm/s flow, burn length in 0 g and 1 g |
| SLICE | 12 | not listed | not listed | fuel type |
| SAME | 8 | not listed | not listed | sample material, air flow |
| FLEX-2 | 8 | 0.17-0.30 | 0.5-3.0 atm | fuel, droplet diameter, flow velocity |
| Cool-flame transitions (ground) | 8 | - | - | pointers to figures in publications |
| Saffire-I | 4 | about 21.5 % | not listed | SIBAL fabric 40.6 x 94 cm, 20 cm/s |
| Saffire-III | 2 | not listed | not listed | SIBAL fabric, 30 cm/s |
| DAFT / DAFT-2 | 2 | - | - | dust sampling sessions |
| 4 ground studies | no table | | | |

## Quirks seen
- Oxygen is given as percent in some tables and mole fraction in others.
- Pressure units vary: mmHg, bar, atm.
- Some cells hold several values ("0.17; 0.21; 0.25; 0.3") or text ("~30% and ~21% O2 with He").
- Obvious typos exist (one BRE cell reads "3400%"; a FLEX pressure of 0).
- Saffire tables include rows that are not burn tests ("Pre-test flow visualization data").

## A pattern worth examining in Step 1 (not yet a conclusion)
In these tables, **solid materials** (BASS-II, Saffire-I) were tested at about 22% oxygen or below, while oxygen at **30% and above** appears only for **gases and liquid droplets** (FLEX to 34%, CFI-G, Flame Design and BRE to 40%). NASA expects 30% or more in the Moon Base. This needs checking against BASS, Saffire-II/III and the investigation documents before we rely on it.
