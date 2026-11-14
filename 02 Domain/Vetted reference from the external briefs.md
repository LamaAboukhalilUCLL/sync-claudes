# Vetted reference from the external briefs

**Date:** Sat 14 Nov 2026 · **By:** Claude Code, at Lama's request

Lama supplied three documents: "Technical Architecture & Research Report" (5 pages), "Step 1: Central Thesis, Mission Presets & Evaluation Rubric" (3 pages) and a pasted execution plan. This note keeps **only what could be checked** against the PSI snapshot in `app/raw/` or the challenge statement, and lists what was rejected and why, so it is not reintroduced later.

Three levels are used below:
- **Verified** - found in a saved PSI record or table, or in the challenge statement. Safe to use, with the source shown.
- **Unverified** - plausible, but no source in our hands. Must not appear in the app or project page until a citable source is added to [[References]].
- **Rejected** - wrong, or not in PSI.

Quotes from PSI records are word for word; only typographic quote marks and hyphens are normalised.

## 1. Verified: the atmospheres

| Environment | Oxygen | Total pressure | Source |
|---|---|---|---|
| Earth sea level | 21 % | 14.7 psi | Challenge statement; also PSI-20 (BRE) objective |
| Spacesuit | 100 % | 4.3 psi | Challenge statement |
| Moon Base and pressurized rovers | 30 % or more | 10.2 psi or less | Challenge statement |
| "NASA - considered atmosphere for human space missions" | 21 % | 14.7 psia | PSI-20 (BRE), `objective` field |
| same | 26.5 % | 10.2 psia | PSI-20 (BRE), `objective` field |
| same | 34 % | 8.2 psia | PSI-20 (BRE), `objective` field |

Things to keep straight:
- The briefs call "34 % at 8.2 psi" the nominal Moon Base value. PSI-20 lists it as one of three atmospheres NASA considered; it does **not** say it is the Moon Base value. The challenge statement only says "30 % or more at 10.2 psi or less".
- At 10.2 psia PSI-20 pairs **26.5 %**, which is below the challenge statement's 30 %. Both are sourced; they are not the same claim.
- No PSI record assigns an atmosphere to Mars. A "Mars habitat, 34 %, 8.2 psi" preset would be our assumption.

**Oxygen partial pressure** (our arithmetic: oxygen fraction x total pressure; not a PSI value):

| Atmosphere | Partial pressure of oxygen |
|---|---|
| 21 % at 14.7 psi | 3.09 psi |
| 26.5 % at 10.2 psi | 2.70 psi |
| 30 % at 10.2 psi | 3.06 psi |
| 34 % at 8.2 psi | 2.79 psi |
| 100 % at 4.3 psi | 4.30 psi |

The exploration atmospheres give the crew about the same oxygen to breathe as Earth air while the oxygen *concentration* is much higher. If the project says "more flammable", it must say it is because of concentration, not partial pressure. (That flammability follows concentration is itself **unverified** here: it needs a source.)

## 2. Verified: what PSI itself says about gravity

**No PSI combustion record mentions partial gravity, the Moon or Mars.** A search of the description, objective, approach, hypothesis and research-impact fields of all 24 records found none of: partial gravity, lunar, Moon, Martian, Mars. The statement that E-FIELD Flames "mimicked partial gravity" comes from the challenge statement, not from the PSI-22 record, which describes ion-driven convection from an electric field.

What the records do say about microgravity versus normal gravity:

| Record, field | What it says |
|---|---|
| PSI-26 BASS, hypothesis | "materials in microgravity, with adequate ventilation, burn as well if not better than the same material in normal gravity with other conditions being identical (pressure, oxygen concentration, temperature, etc.)" |
| PSI-25 BASS-II, hypothesis | "NASA tests and controls materials from a flammability perspective using an upward burning test in normal gravity, which is considered to be the worst-case geometry for flammability of the material on Earth." |
| PSI-26 BASS, research impacts | Current materials selection uses NASA-STD-6001 Test 1, which "segregates material based on 1-g behavior without consideration of low gravity effects." |
| PSI-25 BASS-II, objective (PSI-26 BASS has the same sentence) | "Begin to bridge the gap between the normal gravity NASA-STD-6001 Test #1 method, ground-based microgravity tests, and actual material flammability in microgravity." |
| PSI-98, 99, 100 Saffire, objective | To "investigate the low-g flammability limits compared to those obtained in" NASA's normal gravity material flammability screening test. |
| PSI-62 (ground study on BASS data), hypothesis | Names "the 'Goldilocks' flammability zone" as a phenomenon of concurrent flame spread in microgravity that its model should reproduce. |
| PSI-69 FLEX, hypothesis | "the lack of buoyant convection in microgravity will lead to significant differences in the flammability limits and suppression efficacy of various fire suppressant agents compared to normal gravity conditions." |
| PSI-101 and PSI-102 SAME, hypothesis | Without buoyancy-induced flows, smoke particles grow larger than in 1g, which "will, in turn, affect the response of the smoke detectors and possibly result in some detectors not producing an alarm". |
| PSI-20 BRE, research impacts | Burning continued "despite the absence of air flow"; this "was notably seen in elevated-oxygen atmospheres which are being considered for use in future spacecraft, whereas such flames in a normal atmosphere of 21% oxygen self-extinguished in a short time." |

These are hypotheses and stated impacts, not measured results. Cite them as "PSI-26 states the hypothesis that ...".

## 3. Verified: the one table that pairs microgravity with normal gravity

Saffire-II (PSI-99) lists a microgravity and a 1-g burn result for the same sample. All at 20 cm/s, concurrent flow unless noted, oxygen `~ 21.5` to `~ 22.1` percent. Cells as written (the header reads `?-g`, where the micro sign was lost).

| Sample | Material | Thickness | Microgravity burn length | 1-g burn length |
|---|---|---|---|---|
| 2-1 | Silicone | `0.27 mm` | `~ 0` | `Complete` |
| 2-2 | Silicone | `0.61 mm` | `~ 0` | `7.6 cm` |
| 2-3 | Silicone | `1.03 mm` | `~ 0` | `~ 0` |
| 2-4 | Silicone (opposed flow) | `037 mm` | `~ 0` | `Complete` |
| 2-5 | Cotton-Fiberglass (SIBAL) | `037 mm` | `29 cm` | `Complete` |
| 2-6 | (blank) | `037 mm` | `29 cm` | `Complete` |
| 2-7 | PMMA & Nomex | `0.85 and 0.37 mm` | `5 cm & 0 (note 2)` | `~ 0 (Nomex)` |
| 2-8 | PMMA | `See Fig. 5` | `~ 10 cm (note 3)` | `Complete` |
| 2-9 | (blank) | `1 cm` | `~ 10 cm (note 4)` | `Complete` |

Why this matters: here thin silicone burned completely in 1 g and did **not** burn in microgravity. So "microgravity is always the worse case" is not what this table shows. Any gravity story we tell has to survive this table.

## 4. Verified: which investigations belong together

From each record's "related investigations" field (`related_glds`). Blank means PSI lists none; links are not always listed in both directions.

| Record | PSI lists as related |
|---|---|
| PSI-22 E-FIELD Flames | PSI-23 |
| PSI-25 BASS-II | PSI-26 |
| PSI-26 BASS | PSI-107, PSI-25 |
| PSI-39 CFI | PSI-69 |
| PSI-47 DAFT | PSI-102 |
| PSI-60 (ground: SPICE data, colour-ratio pyrometry on Nikon NEF images) | PSI-107 |
| PSI-62 (ground: flamelet generated manifold modelling) | PSI-25, PSI-26 |
| PSI-98 Saffire-I | PSI-99, PSI-100, PSI-26 |
| PSI-100 Saffire-III | PSI-99, PSI-98 |
| PSI-101 SAME-R | PSI-102 |
| PSI-102 SAME | PSI-101 |
| PSI-106 SLICE | PSI-107 |
| PSI-115 (ground: smoke simulation) | PSI-102 |
| PSI-117 (ground: cool-flame CFD) | PSI-69, PSI-142 |
| PSI-142 (ground: cool-flame transitions) | PSI-69 |
| PSI-10, 20, 21, 23, 68, 69, 99, 107, 159 | (blank) |

Also verified: BASS-II's objective says it will "Provide SoFIE PIs with preliminary data". That is the only place SoFIE appears in PSI's combustion records.

No rocket or propellant study is among the 24 (no record mentions "rocket" or "propell"), so the scope filter the briefs ask for has nothing to remove.

## 5. Worth keeping as method (candidates for Lama's decision, not yet decided)

- **Provenance tag on every number.** The briefs propose `psi_metadata`, `psi_experimental_doc`, `unreported_in_metadata`. This matches decisions D4 and D6. Our data actually needs four cases: from an Experimental Table; from a record's text field; not stated in PSI; and our own label or arithmetic (for example "what burns", partial pressure).
- **Never merge investigations silently.** Keep PSI-25 and PSI-26 separate, CFI-G normal and inverse flames separate, and link ground studies to their flight parents (section 4).
- **Ranking criteria, as ideas without numbers:** how close the tested atmosphere is to the chosen one; how real the material is (spacecraft solids, then a burner emulating solids, then gas and droplet surrogates); size of the experiment; what was measured. The briefs' weights (35/25/20/20) and sub-scores (1.00, 0.70, 0.45 ...) have no source. If a ranker is built, the weights are Lama's choice and must be shown to the user as a choice.
- **"Audit drawer":** show the exact score calculation and the raw source cells beside every result.
- **Citation check for the AI layer (Step 5):** only pass saved PSI records to the model; after it answers, check by program that every `[PSI-n]` it cites is one of the records it was given; say "not stated in PSI" when a value is missing.
- **Static site first:** all ranking and charts run in the browser from a file built from `app/raw/`; live AI is an optional extra with saved answers as fallback. Consistent with D9.
- **Oxygen partial pressure** as an extra column beside concentration and total pressure (labelled as our arithmetic).

## 6. Unverified: the physics framing

Plausible and probably in the literature, but none of it is in PSI and we hold no source. Do not use in the app, page or demo until a citable source is in [[References]].
- Flame stability described by the Damkohler number (flow time over chemical time).
- A U-shaped flammability boundary: radiative quenching at very low flow, blow-off at high flow, most flammable in between. (PSI-62's "Goldilocks flammability zone" points at this, without numbers.)
- Flammability peaking at partial gravity or low forced flow, so that a material passing the 1-g test could burn on the Moon.
- Buoyant velocity scaling, U proportional to the square root of (g x L x temperature rise / ambient temperature), and using it backwards to give a microgravity test an "equivalent gravity".
- The figures 30-100 cm/s (buoyant flow at 1 g) and 5-20 cm/s (cabin flow).

Even with a source, the "equivalent gravity" axis needs a length and a temperature rise chosen by us for every test. Every point on such a chart would be our model's output, not PSI data.

## 7. Rejected

| Claim in the briefs | Why rejected |
|---|---|
| PSI-188 is a core combustion record | PSI-188 is "Advanced Colloids Experiment-Temperature 4" (soft matter). |
| SoFIE (GEL, MIST, NCA, RTDFS, SMuRF) as PSI data | No SoFIE record in PSI. A search for "SoFIE" returns only BASS-II. |
| Saffire-IV, V, VI as PSI data, including "1.5-3.2 kW" fires and SMAC results | PSI holds only Saffire-I, II, III. |
| LUCI, FM2, FLARE as "anchors" | Not in PSI (LUCI and FLARE searches return nothing; FM2 is named by the challenge as a future experiment). |
| "25-40 core Combustion Science records" | There are 24. |
| CFI-G's 85 % oxygen "bounds" the 100 % spacesuit case | 85 % is burner-flow oxygen in inverse flames, into a fuel atmosphere. CFI-G ambient oxygen stops at 40 %. Against decision D5. |
| "High-O2 BASS runs" | BASS states no oxygen in its table; BASS-II runs 13.6-22.2 %, and its approach says oxygen was "varied below 21%". |
| Saffire at "exploration O2% and reduced pressures" | Saffire-I and II tables show about 21.5-22.1 %; Saffire-III states none. |
| Saffire-III and E-FIELD as Lunar-atmosphere anchors | Saffire-III states no oxygen; E-FIELD's table has no oxygen column. |
| FLEX at 0.5-1.5 atm; FLEX-2 under PSI-69 | FLEX's table runs to 2,319.9 mmHg (about 3 atm). FLEX-2 is PSI-68. |
| BASS flow 0-50 cm/s | PSI-26 approach: "airflow speeds reaching as high as 40 cm/s". |
| "PMMA spheres (40 cm dia)", 90 L chamber, 17-19 m3 Cygnus, sample sizes for SoFIE | No PSI source. |
| An AI pass that turns record prose into numbers, with the example `o2_max: 85.0` | The example is exactly the burner-flow mistake. Numbers come from tables and are read by declared rules (D6). |
| Predicted flame spread rate or oxygen limit for the Moon and Mars; "export CFD validation tables" of extinction points and heat release | PSI has no partial-gravity data, and the Experimental Tables do not hold heat-release profiles. These would be invented numbers. |
| "Thesis sign-off: non-linear Damkohler scaling adopted" | The central insight is Lama's decision and is still open. |
| "Scientific Intelligence (SI)" | NASA's term is "Super Intelligence (SI)". |
| Next.js, FastAPI, DuckDB, LangChain, vector search, Pareto frontier | Not needed for 24 records; not buildable and testable by Sunday. |

## 8. The pasted execution plan, point by point

| Part | Verdict |
|---|---|
| Four-act story (past fires, new atmospheres, scattered data, our dashboard) | Acts I, III and IV are sound and sourced from the challenge statement. Act II (partial-gravity blind spot) rests on section 6, which is unverified, and on data PSI does not have. |
| "PSI lacks standard cross-investigation fields for oxygen, pressure, flow" | True, and well supported by [[Oxygen evidence (generated)]]: only 10 of 24 investigations state an ambient oxygen value in their table, variously as mole fractions, percentages, lists and free text. |
| Step 2: query the API, merge with known ids, cache raw JSON | Already done (`app/fetch_snapshot.py`, `app/raw/`). |
| Step 2 schema fields | Reasonable list. `o2_pct_range` must be split into ambient and burner-flow (D5). `pressure_psi_range` would need unit conversion, which must be declared, not silent. |
| Step 3 ranker | Idea is fine; weights need to be Lama's (section 5). |
| Step 3 equivalent-gravity mapping; Step 4 phase explorer with CFD export | Rejected for now (sections 6 and 7). |
| Step 4 compare view; controls and Earth spinoff view | Fine if every statement cites a PSI record. Spinoff sentences found in PSI: SAME (detectors for submarines, underwater laboratories), E-FIELD (reducing pollutants in terrestrial combustion), Saffire (mines, airplanes, submarines). Water-mist and firefighter-clothing links come from the challenge's resource list, not PSI. |
| Step 5 citation-locked AI; Step 6 methodology drawer | Keep (section 5). |
| Tech stack option A (static first, thin AI proxy) | The right direction; plain HTML and JavaScript is enough. Decision belongs to Step 3. |

See also: [[PSI data source]], [[Oxygen evidence (generated)]], [[Decision log]].
