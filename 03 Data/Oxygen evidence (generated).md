# Oxygen evidence (generated)

Written by `app/evidence_oxygen.py` from the snapshot in `app/raw/` (PSI files retrieved 2026-11-14T16:22:21Z to 2026-11-14T16:25:41Z). **Do not edit by hand**; re-run the script.

How to read it:
- **Ambient oxygen** is the atmosphere around the flame. **Burner-flow oxygen** is oxygen blown out of the burner into a fuel atmosphere ("inverse" flames). They are different things and are kept apart.
- A cell counts as a number only if it is a plain number, or a `;`-separated list of plain numbers. Every other cell is shown exactly as PSI wrote it and is **not** in the ranges.
- † = mole fraction multiplied by 100 to read as percent. No other conversion is made.
- "What burns" is our own draft label, not a PSI field. "Rows" are table rows; in some tables a row is a test day or a fuel, not one test.
- Which column means what is our reading of each table (section 4).

## 1. Summary: oxygen stated in each Experimental Table

| PSI id | Investigation | What burns (our label) | Table | Rows | Ambient O2 before test, % | Rows at 30 % or more | Burner-flow O2, % | Other cells, as written |
|---|---|---|---|---|---|---|---|---|
| [PSI-10](https://psi.nasa.gov/physci/repo/data/investigations/PSI-10) | ACME/Flame Design | Gas | Flame Design_Normal Flame | 207 | 19.8 to 40† | 131 of 207 numeric rows | not in table |  |
| [PSI-10](https://psi.nasa.gov/physci/repo/data/investigations/PSI-10) | ACME/Flame Design | Gas | Flame Design_Inverse Flame | 120 | not in table | - | 21.2 to 85† | `RAMP` x9; `LOW O2` x2 |
| [PSI-20](https://psi.nasa.gov/physci/repo/data/investigations/PSI-20) | ACME BRE | Gas (burner emulating solids and liquids) | ACME BRE | 18 | 21 to 40 (from list cells) | 16 of 16 list rows | not in table | `3400%` x1; `2100%` x1 |
| [PSI-21](https://psi.nasa.gov/physci/repo/data/investigations/PSI-21) | ACME CLD Flame | Gas | CLD Flame | 32 | not in table | - | not in table |  |
| [PSI-22](https://psi.nasa.gov/physci/repo/data/investigations/PSI-22) | ACME E-FIELD Flames | Gas | ACME E-FIELD Flames | 32 | not in table | - | not in table |  |
| [PSI-23](https://psi.nasa.gov/physci/repo/data/investigations/PSI-23) | ACME s-Flame | Gas | ACME s-Flame | 18 | no plain numbers | see cells | not in table | `~21% O2 with N2` x2; `~21% O2 with N3` x2; `~21% O2 with N4` x2; `~30% O2 with N2` x1; `~21% O2 with N5` x1; `~21% O2 with N6` x1; `~21% O2 with He` x2; `~30% O2 with He` x2; `~30% and ~21% O2 with He` x5 |
| [PSI-25](https://psi.nasa.gov/physci/repo/data/investigations/PSI-25) | BASS-II | Solids | BASS-II | 129 | 13.6 to 22.2 | 0 of 129 numeric rows | not in table |  |
| [PSI-26](https://psi.nasa.gov/physci/repo/data/investigations/PSI-26) | BASS | Solids | BASS | 122 | not in table | - | not in table |  |
| [PSI-39](https://psi.nasa.gov/physci/repo/data/investigations/PSI-39) | CFI | Liquid droplets | CFI | 87 | 17 to 21† | 0 of 87 numeric rows | not in table |  |
| [PSI-47](https://psi.nasa.gov/physci/repo/data/investigations/PSI-47) | DAFT / DAFT-2 | Dust | DAFT | 2 | not in table | - | not in table |  |
| [PSI-60](https://psi.nasa.gov/physci/repo/data/investigations/PSI-60) | (no acronym) | Ground study (SPICE data) | no table | - | - | - | - | |
| [PSI-62](https://psi.nasa.gov/physci/repo/data/investigations/PSI-62) | (no acronym) | Ground study (BASS data) | no table | - | - | - | - | |
| [PSI-68](https://psi.nasa.gov/physci/repo/data/investigations/PSI-68) | FLEX-2 | Liquid droplets | Flex2 | 8 | 17 to 30† (from list cells) | 8 of 8 list rows | not in table |  |
| [PSI-69](https://psi.nasa.gov/physci/repo/data/investigations/PSI-69) | FLEX | Liquid droplets | FLEX | 274 | 12 to 34† | 24 of 274 numeric rows | not in table |  |
| [PSI-98](https://psi.nasa.gov/physci/repo/data/investigations/PSI-98) | SAFFIRE-I | Solids | SAFFIRE-1 | 4 | no plain numbers | see cells | not in table | `21.5 - 21.7` x1; `~ 21.5` x1; blank x2 |
| [PSI-99](https://psi.nasa.gov/physci/repo/data/investigations/PSI-99) | SAFFIRE-II | Solids | SAFFIRE-2 | 15 | no plain numbers | see cells | not in table | `~ 21.5` x1; `~ 22.1` x6; `22.1 to 22.0` x1; `22.0 to 21.9` x1; blank x6 |
| [PSI-100](https://psi.nasa.gov/physci/repo/data/investigations/PSI-100) | SAFFIRE-III | Solids | SAFFIRE-3 | 2 | not in table | - | not in table |  |
| [PSI-101](https://psi.nasa.gov/physci/repo/data/investigations/PSI-101) | SAME-R | Smoke | SAME-R | 109 | not in table | - | not in table |  |
| [PSI-102](https://psi.nasa.gov/physci/repo/data/investigations/PSI-102) | SAME | Smoke | SAME | 8 | not in table | - | not in table |  |
| [PSI-106](https://psi.nasa.gov/physci/repo/data/investigations/PSI-106) | SLICE | Gas | Slice | 12 | not in table | - | not in table |  |
| [PSI-107](https://psi.nasa.gov/physci/repo/data/investigations/PSI-107) | SPICE | Gas | Spice | 469 | not in table | - | not in table |  |
| [PSI-115](https://psi.nasa.gov/physci/repo/data/investigations/PSI-115) | (no acronym) | Ground study (SAME data) | no table | - | - | - | - | |
| [PSI-117](https://psi.nasa.gov/physci/repo/data/investigations/PSI-117) | (no acronym) | Ground study (FLEX data) | no table | - | - | - | - | |
| [PSI-142](https://psi.nasa.gov/physci/repo/data/investigations/PSI-142) | (no acronym) | Ground study (FLEX data) | Data Summary Table | 8 | not in table | - | not in table |  |
| [PSI-159](https://psi.nasa.gov/physci/repo/data/investigations/PSI-159) | ACME CFI-G | Gas | CFI-G_Normal Flames | 179 | 17.97 to 39.97† | 115 of 179 numeric rows | not in table |  |
| [PSI-159](https://psi.nasa.gov/physci/repo/data/investigations/PSI-159) | ACME CFI-G | Gas | CFI-G_Inverse Flames | 154 | not in table | - | 12 to 85† |  |

## 2. Every oxygen and pressure column, in detail

Units are as PSI states them (no conversion here). "Lowest / highest" lists the three smallest and three largest distinct numbers so unusual values stay visible.

| Table file | Column header | Our reading | Unit as stated | Rows | Plain numbers | Lowest | Highest | List cells | Blank | Other cells, as written |
|---|---|---|---|---|---|---|---|---|---|---|
| `PSI-10_table_1.csv` | `XO2 (init)` | Ambient oxygen, before test | mole fraction | 207 | 207 | 0.198, 0.1986, 0.1992 | 0.3985, 0.3986, 0.4 | - | 0 | - |
| `PSI-10_table_1.csv` | `XO2 (final)` | Ambient oxygen, after test | mole fraction | 207 | 187 | 0.1975, 0.198, 0.1986 | 0.3968, 0.3972, 0.3972 | - | 20 | - |
| `PSI-10_table_1.csv` | `pinit (atm)` | Pressure | atm | 207 | 207 | 0.932, 0.9887, 0.9914 | 1.296, 1.296, 1.297 | - | 0 | - |
| `PSI-10_table_2.csv` | `XO2` | Burner-flow oxygen | mole fraction | 120 | 109 | 0.212, 0.2123, 0.2123 | 0.6439, 0.6445, 0.85 | - | 0 | `RAMP` x9; `LOW O2` x2 |
| `PSI-10_table_2.csv` | `pinit (atm)` | Pressure | atm | 120 | 120 | 0.4246, 0.4253, 0.4266 | 3.005, 3.006, 3.008 | - | 0 | - |
| `PSI-159_table_1.csv` | ` XO2 before test` | Ambient oxygen, before test | mole fraction | 179 | 179 | 0.1797, 0.1802, 0.2067 | 0.3993, 0.3996, 0.3997 | - | 0 | - |
| `PSI-159_table_1.csv` | `XO2  after test` | Ambient oxygen, after test | mole fraction | 179 | 179 | 0.1794, 0.1797, 0.2066 | 0.3965, 0.3966, 0.3973 | - | 0 | - |
| `PSI-159_table_1.csv` | `approx p (bar)` | Pressure | bar | 179 | 179 | 0.5067, 0.9444, 1.013 | 1.013, 2.027, 3.04 | - | 0 | - |
| `PSI-159_table_2.csv` | `XO2` | Burner-flow oxygen | mole fraction | 154 | 154 | 0.12, 0.135, 0.15 | 0.5, 0.7, 0.85 | - | 0 | - |
| `PSI-159_table_2.csv` | `approx p (bar)` | Pressure | bar | 154 | 154 | 0.4954, 0.5516, 1.1 | 1.103, 2.207, 3.31 | - | 0 | - |
| `PSI-20_table_1.csv` | `Oxygen Conc (percent)` | Ambient oxygen, before test | percent | 18 | 0 | - | - | `21; 26.5; 40` x1; `26.5; 34` x4; `21; 26.5; 34; 40` x1; `26.5; 40` x1; `21; 26.5; 34` x2; `25; 34; 40` x4; `25; 40` x2; `34; 40` x1 | 0 | `3400%` x1; `2100%` x1 |
| `PSI-23_table_1.csv` | `Atmosphere*` | Ambient oxygen, before test | text | 18 | 0 | - | - | - | 0 | `~21% O2 with N2` x2; `~21% O2 with N3` x2; `~21% O2 with N4` x2; `~30% O2 with N2` x1; `~21% O2 with N5` x1; `~21% O2 with N6` x1; `~21% O2 with He` x2; `~30% O2 with He` x2; `~30% and ~21% O2 with He` x5 |
| `PSI-25_table_1.csv` | `Calibrated  initial O2 % by vol ` | Ambient oxygen, before test | percent by volume | 129 | 129 | 13.6, 14.2, 14.5 | 21.7, 21.8, 22.2 | - | 0 | - |
| `PSI-25_table_1.csv` | `Calibrated final O2 % by vol` | Ambient oxygen, after test | percent by volume | 129 | 127 | 0.6, 0.9, 1.6 | 22.2, 39.1, 40.4 | - | 0 | `none` x2 |
| `PSI-39_table_1.csv` | `Oxygen` | Ambient oxygen, before test | mole fraction (unit not stated in header) | 87 | 87 | 0.17, 0.21 | 0.17, 0.21 | - | 0 | - |
| `PSI-39_table_1.csv` | `Pressure` | Pressure | text with unit | 87 | 0 | - | - | - | 0 | `1 atm` x38; `1 atm ` x9; `1.25 atm` x9; `2 atm` x7; `3 atm` x10; `3 atm ` x4; `5 atm ` x3; `0.75 atm` x4; `0.5 atm` x3 |
| `PSI-68_table_1.csv` | `Oxygen Mole Fraction` | Ambient oxygen, before test | mole fraction | 8 | 0 | - | - | `0.17; 0.21;0.25; 0.3` x8 | 0 | - |
| `PSI-68_table_1.csv` | `Ambient Pressure (atm)` | Pressure | atm | 8 | 0 | - | - | - | 0 | `0.5; 1.0; 1.5; 2.0; or 3.0 ` x8 |
| `PSI-69_table_1.csv` | `O initial ambient composition; mole fraction` | Ambient oxygen, before test | mole fraction | 274 | 274 | 0.12, 0.13, 0.14 | 0.25, 0.3, 0.34 | - | 0 | - |
| `PSI-69_table_1.csv` | `Ambient pressure; mmHg` | Pressure | mmHg | 274 | 274 | 0, 526.3, 527.6 | 2319, 2320, 2320 | - | 0 | - |
| `PSI-98_table_1.csv` | `Percent O2` | Ambient oxygen, before test | percent | 4 | 0 | - | - | - | 2 | `21.5 - 21.7` x1; `~ 21.5` x1 |
| `PSI-99_table_1.csv` | `Percent O2 (Note 1)` | Ambient oxygen, before test | percent | 15 | 0 | - | - | - | 6 | `~ 21.5` x1; `~ 22.1` x6; `22.1 to 22.0` x1; `22.0 to 21.9` x1 |

## 3. Ambient oxygen before test: how many rows at each level

Plain-number cells only, rounded to the nearest whole percent (†: mole fractions x100). List and text cells are in section 2.

| Table file | Investigation | What burns (our label) | Rows per whole percent (percent: rows) |
|---|---|---|---|
| `PSI-10_table_1.csv` | ACME/Flame Design | Gas | 20: 45, 21: 26, 29: 3, 30: 3, 36: 8, 37: 18, 38: 30, 39: 42, 40: 32 |
| `PSI-159_table_1.csv` | ACME CFI-G | Gas | 18: 2, 21: 44, 22: 12, 23: 6, 33: 2, 34: 1, 35: 6, 36: 6, 37: 10, 38: 27, 39: 51, 40: 12 |
| `PSI-25_table_1.csv` | BASS-II | Solids | 14: 2, 15: 11, 16: 11, 17: 26, 18: 18, 19: 16, 20: 4, 21: 23, 22: 18 |
| `PSI-39_table_1.csv` | CFI | Liquid droplets | 17: 24, 21: 63 |
| `PSI-69_table_1.csv` | FLEX | Liquid droplets | 12: 8, 13: 9, 14: 11, 15: 20, 16: 10, 17: 21, 18: 36, 19: 7, 20: 30, 21: 54, 23: 19, 24: 19, 25: 6, 30: 15, 34: 9 |

## 4. Why each column is read as ambient or burner-flow oxygen

| Table file | Column header | Our reading | Reason |
|---|---|---|---|
| `PSI-10_table_1.csv` | `XO2 (init)` | Ambient oxygen, before test | Normal flames: fuel leaves the burner into an oxygen atmosphere; value before the test |
| `PSI-10_table_1.csv` | `XO2 (final)` | Ambient oxygen, after test | Same atmosphere after the test |
| `PSI-10_table_1.csv` | `pinit (atm)` | Pressure | Chamber pressure before the test |
| `PSI-10_table_2.csv` | `XO2` | Burner-flow oxygen | Inverse flames: oxygen leaves the burner into a fuel atmosphere (column 'XC2H4 initial') |
| `PSI-10_table_2.csv` | `pinit (atm)` | Pressure | Chamber pressure before the test |
| `PSI-159_table_1.csv` | ` XO2 before test` | Ambient oxygen, before test | Normal flames: oxygen atmosphere before the test |
| `PSI-159_table_1.csv` | `XO2  after test` | Ambient oxygen, after test | Same atmosphere after the test |
| `PSI-159_table_1.csv` | `approx p (bar)` | Pressure | Approximate chamber pressure |
| `PSI-159_table_2.csv` | `XO2` | Burner-flow oxygen | Inverse flames: oxygen leaves the burner into a fuel atmosphere (column 'Xf  before test') |
| `PSI-159_table_2.csv` | `approx p (bar)` | Pressure | Approximate chamber pressure |
| `PSI-20_table_1.csv` | `Oxygen Conc (percent)` | Ambient oxygen, before test | Table note: chamber oxygen 'as diluted with nitrogen on a volume basis'; one row per test day, listing the concentrations of tests that ignited |
| `PSI-23_table_1.csv` | `Atmosphere*` | Ambient oxygen, before test | Chamber atmosphere described in words; one row per test day |
| `PSI-25_table_1.csv` | `Calibrated  initial O2 % by vol ` | Ambient oxygen, before test | Oxygen in the glovebox work volume before the test |
| `PSI-25_table_1.csv` | `Calibrated final O2 % by vol` | Ambient oxygen, after test | Same, after the test |
| `PSI-39_table_1.csv` | `Oxygen` | Ambient oxygen, before test | Listed beside Nitrogen and Helium, which together sum to 1 |
| `PSI-39_table_1.csv` | `Pressure` | Pressure | Chamber pressure |
| `PSI-68_table_1.csv` | `Oxygen Mole Fraction` | Ambient oxygen, before test | One row per fuel, listing the planned values; column 'Ambient Gas Mixture' |
| `PSI-68_table_1.csv` | `Ambient Pressure (atm)` | Pressure | One row per fuel, listing the planned values |
| `PSI-69_table_1.csv` | `O initial ambient composition; mole fraction` | Ambient oxygen, before test | Header says initial ambient composition |
| `PSI-69_table_1.csv` | `Ambient pressure; mmHg` | Pressure | Header says ambient pressure |
| `PSI-98_table_1.csv` | `Percent O2` | Ambient oxygen, before test | Oxygen in the Cygnus cabin air flowing over the sample |
| `PSI-99_table_1.csv` | `Percent O2 (Note 1)` | Ambient oxygen, before test | Table note 1: derived from measured CO2 and the initial O2 reported by ISS |

## 5. All tables in the snapshot, with their full headers

Tables with no oxygen column are listed too, so absence is visible.

| PSI id | Investigation | DOI | Table file | PSI file name | Rows | Blank rows dropped | Encoding | Oxygen column? | Header |
|---|---|---|---|---|---|---|---|---|---|
| PSI-10 | ACME/Flame Design | [10.60555/w4zy-bt45](https://doi.org/10.60555/w4zy-bt45) | `PSI-10_table_1.csv` | PSI-10_Experimental table_Flame Design_Normal Flame.csv | 207 | 0 | UTF-8 | yes | `Flame Type`, `Day`, `Fuel`, `Test`, `Xfuel`, `mfuel (mg/s)`, `mN2 (mg/s)`, `mtot (mg/s)`, `XO2 (init)`, `XO2 (final)`, `pinit (atm)`, `pfinal (atm)`, `pmean (atm)`, `mean Zst`, `Tad (K)` |
| PSI-10 | ACME/Flame Design | [10.60555/w4zy-bt45](https://doi.org/10.60555/w4zy-bt45) | `PSI-10_table_2.csv` | PSI-10_Experimental table_Flame Design_Inverse Flame.csv | 120 | 0 | UTF-8 | yes | `Flame Type`, `Day`, `Test`, `XO2`, `mO2 (mg/s)`, `mN2 (mg/s)`, `mtot (mg/s)`, `XC2H4 initial`, `XC2H4 final`, `pinit (atm)`, `pfinal (atm)`, `pmean (atm)`, `mean Zst`, `Tad (K)` |
| PSI-20 | ACME BRE | [10.60555/vb93-3y72](https://doi.org/10.60555/vb93-3y72) | `PSI-20_table_1.csv` | PSI-20_Experimental table_ACME BRE.csv | 18 | 0 | UTF-8 | yes | `Year`, `Month`, `Date`, `Burner Size (mm)`, `Fuel Bottle`, `Oxygen Conc (percent)`, `Flames Ignited`, `Notes` |
| PSI-21 | ACME CLD Flame | [10.60555/23e1-9950](https://doi.org/10.60555/23e1-9950) | `PSI-21_table_1.csv` | PSI-21_Experimental table_CLD Flame.csv | 32 | 0 | UTF-8 | no | `Test Type`, `Test Day`, `Fuel MFC`, `N2 MFC`, `Fuel Bottle`, `Fuel conc. Range`, `Flames ignited`, `Notes` |
| PSI-22 | ACME E-FIELD Flames | [10.60555/se5a-8c73](https://doi.org/10.60555/se5a-8c73) | `PSI-22_table_1.csv` | PSI-22_Experimental table_ACME E-FIELD Flames.csv | 32 | 0 | UTF-8 | no | `Test Type`, `Test Day`, `Year`, `Month`, `Date`, `Mesh Polarity`, `Fuel Bottle`, `Fuel Conc`, `Flames Ignited`, `Notes` |
| PSI-23 | ACME s-Flame | [10.60555/k57n-p030](https://doi.org/10.60555/k57n-p030) | `PSI-23_table_1.csv` | PSI-23_Experimental table_ACME s-Flame.csv | 18 | 0 | UTF-8 | yes | `Test Type`, `Test Day*`, `Year`, `Month`, `Date`, `Atmosphere*`, `Fuel Bottle`, `Flames Ignited*`, `Notes` |
| PSI-25 | BASS-II | [10.60555/4qc4-de67](https://doi.org/10.60555/4qc4-de67) | `PSI-25_table_1.csv` | PSI-25_Experimental table_BASS-II.csv | 129 | 0 | UTF-8 | yes | `PI`, `Test #`, `Date`, `GMT`, `Sample #`, `Fuel Sample Material`, `Flow restrictor`, `Fan display`, `Air display`, `Radiometer gain   (1000   250   50   10)`, `Total Frames Shot`, `Calibrated  initial O2 % by vol `, `Calibrated final O2 % by vol`, `Initial CO2 % by vol`, `Final CO2 % by vol`, `Initial CO (ppm)`, `Final CO (ppm)` |
| PSI-26 | BASS | [10.60555/58h4-dy80](https://doi.org/10.60555/58h4-dy80) | `PSI-26_table_1.csv` | PSI-26_Experimental table_BASS.csv | 122 | 0 | UTF-8 | no | `Date`, `GMT`, `As Run Test #`, `Test #`, `Sample #`, `Fuel Sample Material` |
| PSI-39 | CFI | [10.60555/m6pj-a914](https://doi.org/10.60555/m6pj-a914) | `PSI-39_table_1.csv` | PSI-39_Experimental table_CFI.csv | 87 | 0 | UTF-8 | yes | `Flex Number`, `Test Date`, `Local Time`, `CIR `, `Pressure`, `Oxygen`, `Nitrogen`, `Helium`, `Fiber`, `Fuel ` |
| PSI-47 | DAFT / DAFT-2 | [10.60555/ztgj-d202](https://doi.org/10.60555/ztgj-d202) | `PSI-47_table_1.csv` | PSI-47_Experimental table_DAFT.csv | 2 | 0 | UTF-8 | no | `Session Name`, `Actual Day`, `Hardware Description`, `Sample Material`, `Sampled Location` |
| PSI-60 | (no acronym) | [10.60555/mzjm-yv57](https://doi.org/10.60555/mzjm-yv57) | no experimental table | | | | | | |
| PSI-62 | (no acronym) | [10.60555/e9xp-ex83](https://doi.org/10.60555/e9xp-ex83) | no experimental table | | | | | | |
| PSI-68 | FLEX-2 | [10.60555/byp8-h018](https://doi.org/10.60555/byp8-h018) | `PSI-68_table_1.csv` | PSI-68_Experimental table_Flex2.csv | 8 | 0 | UTF-8 | yes | `Sample (Fuel Type)`, `Initial Droplet Diameter (mm)`, `Ambient Gas Mixture `, `Oxygen Mole Fraction`, `Ambient Pressure (atm)`, ` Ambient Temperature (C)`, `Flow Velocity (cm/s)` |
| PSI-69 | FLEX | [10.60555/mbq8-0451](https://doi.org/10.60555/mbq8-0451) | `PSI-69_table_1.csv` | PSI-69_Experimental table_FLEX.csv | 274 | 0 | Windows-1252 | yes | `FLEX Test #`, `FLEX Identifier`, `Test Date`, `Test GMT`, `Fuel`, `Ambient pressure; mmHg`, `O initial ambient composition; mole fraction`, `N initial ambient composition; mole fraction`, `CO initial ambient composition; mole fraction`, `He initial ambient composition; mole fraction`, `Droplet initial diameter; mm`, `Visible flame extinction diameter; mm`, `Burning rate; mm`, `Burn time; s`, `Test end` |
| PSI-98 | SAFFIRE-I | [10.60555/0t15-1z43](https://doi.org/10.60555/0t15-1z43) | `PSI-98_table_1.csv` | PSI-98_Experimental table_SAFFIRE-1.csv | 4 | 0 | UTF-8 | yes | `Sample Number `, `Material`, `Sample Thickness (cm)`, `Sample Length (cm)`, `Sample Width (cm)`, `Air Flow (cm/s)`, `Percent O2`, `Ignition Power (W)`, `Ignition Time (s)`, `Burn Time (s)`, `Flow Direction `, `Camera 1`, `Camera 2` |
| PSI-99 | SAFFIRE-II | [10.60555/2chp-m469](https://doi.org/10.60555/2chp-m469) | `PSI-99_table_1.csv` | PSI-99_Experimental table_SAFFIRE-2.csv | 15 | 0 | UTF-8 | yes | `Sample Number`, `Material`, `Samle Thickness `, `Sample Length `, `Sample Width (cm)`, `Air Flow (cm/s)`, `Percent O2 (Note 1)`, `Ignition Power (W)`, `Ignition Time (s)`, `Burn Time (s)`, `Flow Direction`, `?-g Burn Length`, `?-g Spread Length`, `1-g Burn Length`, `1-g Spread Rate`, `Camera 1`, `Camera 2` |
| PSI-100 | SAFFIRE-III | [10.60555/040q-4h36](https://doi.org/10.60555/040q-4h36) | `PSI-100_table_1.csv` | PSI-100_Experimental table_SAFFIRE-3.csv | 2 | 0 | UTF-8 | no | `Sample Number `, `Material`, `Sample Thickness`, `Sample Length`, `Sample Width`, `Air Flow `, `Direction`, `Camera 1`, `Camera 2` |
| PSI-101 | SAME-R | [10.60555/2np7-jv14](https://doi.org/10.60555/2np7-jv14) | `PSI-101_table_1.csv` | PSI-101_Experimental table_SAME-R.csv | 109 | 0 | UTF-8 | no | `Sample Type`, `SAME Test #`, `Description`, `Date`, `Inlet velocity (cm/s)`, `Rt/R0`, `Duration (sec)`, `Primary aging time (sec)`, `Primary mixing time (sec)`, `Net aging time (sec)` |
| PSI-102 | SAME | [10.60555/gd4k-8h62](https://doi.org/10.60555/gd4k-8h62) | `PSI-102_table_1.csv` | PSI-102_Experimental table_SAME.csv | 8 | 0 | UTF-8 | no | `Sample #`, `Sample Material  `, `Air Flow (cm/s)`, `Weight loss rate (mg/min)`, `Aging Duration (minutes)` |
| PSI-106 | SLICE | [10.60555/pm12-rg61](https://doi.org/10.60555/pm12-rg61) | `PSI-106_table_1.csv` | PSI-106_Experimental table_Slice.csv | 12 | 0 | UTF-8 | no | `Test Date`, `Fuel Type` |
| PSI-107 | SPICE | [10.60555/9kbh-e962](https://doi.org/10.60555/9kbh-e962) | `PSI-107_table_1.csv` | PSI-107_Experimental table_Spice.csv | 469 | 0 | UTF-8 | no | `GMT date`, `GMT ignition`, `GMT  Flame Off `, `Fuel`, `Nozzle (mm)`, `Fuel Rate (sccm)`, `Fuel Rate (mg/s)`, `HC Fuel Rate (mg/s)`, `Air Rate (cm/s)` |
| PSI-115 | (no acronym) | [10.60555/q0v5-1v28](https://doi.org/10.60555/q0v5-1v28) | no experimental table | | | | | | |
| PSI-117 | (no acronym) | [10.60555/gz0q-b577](https://doi.org/10.60555/gz0q-b577) | no experimental table | | | | | | |
| PSI-142 | (no acronym) | [10.60555/80qf-vj95](https://doi.org/10.60555/80qf-vj95) | `PSI-142_table_1.csv` | PSI-142_Experimental table_Data Summary Table.csv | 8 | 0 | UTF-8 | no | `Data ID`, `Data Description`, `Reference Publication Link`, `Figure ID in Reference` |
| PSI-159 | ACME CFI-G | [10.60555/cyt1-kh64](https://doi.org/10.60555/cyt1-kh64) | `PSI-159_table_1.csv` | PSI-159_Experimental table_CFI-G_Normal Flames.csv | 179 | 0 | UTF-8 | yes | `Flame Type`, `Day`, `Fuel`, `Test`, `Cool flame?`, ` XO2 before test`, `XO2  after test`, `approx p (bar)`, `Xf`, `mHC (mg/s)`, `TFP`, `Tad (K)`, `Zst`, `Hot ignition`, `burn time (sec)`, `Self-ext or flow term`, `Peak burner T (C )`, `Comments` |
| PSI-159 | ACME CFI-G | [10.60555/cyt1-kh64](https://doi.org/10.60555/cyt1-kh64) | `PSI-159_table_2.csv` | PSI-159_Experimental table_CFI-G_Inverse Flames.csv | 154 | 861 | UTF-8 | yes | `Flame Type`, `Day`, `Fuel`, `Test`, `Xf  before test`, `Xf  after test`, `approx p (bar)`, `XO2`, `HC burnrate (mg/s)`, `O2 flow rate (mg/s)`, `TFP`, `Tad (K)`, `Zst`, `Hot ignition`, `burn time (sec)`, `Self -ext or flow term`, `Peak burner Temp (C)`, `Peak burner temp (K)`, `Color`, `Comments` |

## 6. The 24 investigation records

Straight from each record's fields. Size is `totalFileSize` in bytes divided by 10^9.

| PSI id | Acronym | Title | Project type | Sub-research area | Hardware | Total size, GB | License | DOI |
|---|---|---|---|---|---|---|---|---|
| [PSI-10](https://psi.nasa.gov/physci/repo/data/investigations/PSI-10) | ACME/Flame Design | Advanced Combustion via Microgravity Experiments / Flame Design | Microgravity Investigation | Flames of Gaseous Fuels | Advanced Combustion via Microgravity Experiments (ACME), Combustion Integrated Rack (CIR), Reconfiguration of Combustion Integrated Rack (CIR) | 2180.44 | (blank) | 10.60555/w4zy-bt45 |
| [PSI-20](https://psi.nasa.gov/physci/repo/data/investigations/PSI-20) | ACME BRE | Advanced Combustion via Microgravity Experiments - Burning Rate Emulator | Microgravity Investigation | Flames of Gaseous Fuels | Combustion Integrated Rack (CIR), ACME | 2035.57 | CC0-1.0 | 10.60555/vb93-3y72 |
| [PSI-21](https://psi.nasa.gov/physci/repo/data/investigations/PSI-21) | ACME CLD Flame | Advanced Combustion via Microgravity Experiments / Coflow Laminar Diffusion Flame | Microgravity Investigation | Flames of gaseous fuel | Combustion Integrated Rack (CIR), ACME | 2005.54 | CC0-1.0 | 10.60555/23e1-9950 |
| [PSI-22](https://psi.nasa.gov/physci/repo/data/investigations/PSI-22) | ACME E-FIELD Flames | Advanced Combustion via Microgravity Experiments Electric-Field Effects on Laminar Diffusion Flames | Microgravity Investigation | Laminar Flames | Combustion Integrated Rack (CIR), ACME | 950.21 | CC0-1.0 | 10.60555/se5a-8c73 |
| [PSI-23](https://psi.nasa.gov/physci/repo/data/investigations/PSI-23) | ACME s-Flame | Advanced Combustion via Microgravity Experiments-Structure and Response of Spherical Diffusion Flames | Microgravity Investigation | Flames of gaseous fuels | Combustion Integrated Rack (CIR), ACME | 782.17 | CC0-1.0 | 10.60555/k57n-p030 |
| [PSI-25](https://psi.nasa.gov/physci/repo/data/investigations/PSI-25) | BASS-II | Burning and Suppression of Solids - II | Microgravity Investigation | Spacecraft Fire Safety | Microgravity Science Glovebox (MSG) | 274.63 | CC0-1.0 | 10.60555/4qc4-de67 |
| [PSI-26](https://psi.nasa.gov/physci/repo/data/investigations/PSI-26) | BASS | Burning and Suppression of Solids | Microgravity Investigation | Spacecraft Fire Safety | Microgravity Science Glovebox | 163.55 | CC0-1.0 | 10.60555/58h4-dy80 |
| [PSI-39](https://psi.nasa.gov/physci/repo/data/investigations/PSI-39) | CFI | Cool Flames Investigation | Microgravity Investigation | Droplets | Multi-User Droplet Combustion Apparatus (MDCA), Combustion Integrated Rack (CIR) | 718.89 | CC0-1.0 | 10.60555/m6pj-a914 |
| [PSI-47](https://psi.nasa.gov/physci/repo/data/investigations/PSI-47) | DAFT / DAFT-2 | Dust and Aerosol Measurement Feasibility Test / Dust and Aerosol Measurement Feasibility Test-2 | Microgravity Investigation | Spacecraft Fire Safety | TSI P-Trak | 0.04 | CC0-1.0 | 10.60555/ztgj-d202 |
| [PSI-60](https://psi.nasa.gov/physci/repo/data/investigations/PSI-60) | (none) | Computational and Experimental Analysis of SPICE Data Sets | Ground Investigation | Gaseous | (blank) | 0.00 | CC0-1.0 | 10.60555/mzjm-yv57 |
| [PSI-62](https://psi.nasa.gov/physci/repo/data/investigations/PSI-62) | (none) | Concurrent Flame Spread Modeling using Flamelet Generated Manifolds in Microgravity with Comparison to BASS Experiments using Two-Color Tomography | Ground Investigation | Spacecraft Fire Safety | (blank) | 0.00 | CC0-1.0 | 10.60555/e9xp-ex83 |
| [PSI-68](https://psi.nasa.gov/physci/repo/data/investigations/PSI-68) | FLEX-2 | Flame Extinguishment Experiment - 2 | Microgravity Investigation | Spacecraft Fire Safety | Combustion Integrated Rack (CIR), Multi-user Droplet Combustion Appartatus (MDCA) | 1224.75 | CC0-1.0 | 10.60555/byp8-h018 |
| [PSI-69](https://psi.nasa.gov/physci/repo/data/investigations/PSI-69) | FLEX | Flame Extinguishment Experiment | Microgravity Investigation | Spacecraft Fire Safety | Combustion Integrated Rack (CIR)-Fluids and Combustion Facility (FCF), Multi-user Droplet Combustion Appartatus (MDCA) | 923.83 | CC0-1.0 | 10.60555/mbq8-0451 |
| [PSI-98](https://psi.nasa.gov/physci/repo/data/investigations/PSI-98) | SAFFIRE-I | Spacecraft Fire Safety Experiment-I | Microgravity Investigation | Spacecraft Fire, Smoke Distribution | Saffire 1 enclosure in Cygnus | 12.25 | CC0-1.0 | 10.60555/0t15-1z43 |
| [PSI-99](https://psi.nasa.gov/physci/repo/data/investigations/PSI-99) | SAFFIRE-II | Spacecraft Fire Experiment-II | Microgravity Investigation | Surface Combustion | Cygnus Pressurized Cargo Module, SAFFIRE | 16.93 | CC0-1.0 | 10.60555/2chp-m469 |
| [PSI-100](https://psi.nasa.gov/physci/repo/data/investigations/PSI-100) | SAFFIRE-III | Spacecraft Fire Experiment-III | Microgravity Investigation | Spacecraft Fire Safety | Saffire III enclosure in Cygnus | 35.21 | CC0-1.0 | 10.60555/040q-4h36 |
| [PSI-101](https://psi.nasa.gov/physci/repo/data/investigations/PSI-101) | SAME-R | Smoke Aerosol Measurement Experiment-Reflight | Microgravity Investigation | Spacecraft Fire Safety | Comparitive Soot Diagnostic Hardware; Refer to final report | 6.31 | CC0-1.0 | 10.60555/2np7-jv14 |
| [PSI-102](https://psi.nasa.gov/physci/repo/data/investigations/PSI-102) | SAME | Smoke and Aerosol Measurement Experiment | Microgravity Investigation | Spacecraft Fire Safety | Comparitive Soot Diagnostic Hardware | 0.66 | CC0-1.0 | 10.60555/gd4k-8h62 |
| [PSI-106](https://psi.nasa.gov/physci/repo/data/investigations/PSI-106) | SLICE | Structure and Liftoff In Combustion Experiment | Microgravity Investigation | (blank) | (blank) | 72.91 | CC0-1.0 | 10.60555/pm12-rg61 |
| [PSI-107](https://psi.nasa.gov/physci/repo/data/investigations/PSI-107) | SPICE | Smoke Point In Co-flow Experiment | Microgravity Investigation | Fire Safety | Microgravity Science Glovebox (MSG) | 6.95 | CC0-1.0 | 10.60555/9kbh-e962 |
| [PSI-115](https://psi.nasa.gov/physci/repo/data/investigations/PSI-115) | (none) | Utilization of the Smoke Aerosol Measurement Experiment Data for Advanced Modeling and Simulation of Smoke Generation in Micro-Gravity | Ground Investigation | Smoke Aerosol, Combustion Simulation | (blank) | 0.26 | CC0-1.0 | 10.60555/q0v5-1v28 |
| [PSI-117](https://psi.nasa.gov/physci/repo/data/investigations/PSI-117) | (none) | Effect of External Thermo-Convective Perturbation on Cool Flame Dynamics: A Multidimensional Multi-Physics CFD Analysis | Ground Investigation | Droplet | (blank) | 0.07 | CC0-1.0 | 10.60555/gz0q-b577 |
| [PSI-142](https://psi.nasa.gov/physci/repo/data/investigations/PSI-142) | (none) | Quantitative Studies of Cool Flame Transitions at Radiation / Stretch Extinction Using Counterflow Flames | Ground Investigation | Spacecraft Fire Safety | Principal Investigator Laboratory Hardware | 0.00 | CC0-1.0 | 10.60555/80qf-vj95 |
| [PSI-159](https://psi.nasa.gov/physci/repo/data/investigations/PSI-159) | ACME CFI-G | Advanced Combustion via Microgravity Experiments / Cool Flames Investigation with Gases | Microgravity Investigation | Flames of Gaseous Fuels | ACME, Combustion Integrated Rack (CIR) | 2085.59 | CC0-1.0 | 10.60555/cyt1-kh64 |
