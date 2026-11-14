# NASA's stated fire safety needs

**Added:** Sat 14 Nov 2026, 22:10 · **By:** Claude Code (VS Code), web research asked for by Lama.

Input for the central insight (Step 1). It lists what NASA itself says it needs, what our PSI snapshot holds on each need, and what data exists outside PSI. **It proposes no insight; that is Lama's.**

**Read directly** means I opened the document and the quotation is word for word. **Search summary** means I only saw a search engine's summary; open the source before quoting it anywhere.

## How NASA ranks the problem
- **2026 Civil Space Shortfalls** (read directly). Need 21.01: "Increase crew safety from fire hazards in low and partial gravity environments at reduced pressures and increased oxygen levels." It sits under shortfall 21, "Provide Earth-independent safety and crew health and performance countermeasures during long duration missions", ranked **20 of 32** in the FY26 prioritization. I did not find 21.01 among the 40 focus areas NASA Technology chose for FY26.
- **2024 ranking** (search summary): "Fire Safety for Habitation" was 10 of 187.

## NASA's own list of fire risks
From Gary Ruff (NASA Glenn, Saffire project manager), "Spacecraft Fire Safety Needs for Exploration", 25 Sep 2020 (read directly). Seven risk statements, shortened here; the labels in brackets are his.
1. Flame spread over solids differs in normal and reduced gravity, so "current material screening standards will not adequately identify the fire risk". (Test Methods) Sub-items include "Ambient pressure and oxygen mole fractions".
2. Ignitability of a solid could be influenced by the habitat environment. (Ignition)
3. Fire growth differs in reduced gravity, so conditions "could quickly become hazardous". Sub-items: heat release rate, "Production of smoke and toxic products". (Fire Growth)
4. The crew "may not be able to evacuate to another vehicle". (Fire Response)
5. Pre-ignition fire signatures in reduced gravity could differ from normal gravity. (Fire Detection)
6. A fire may propagate despite early detection, so active suppression may be needed. (Fire Suppression)
7. With clean-up the vehicle could be restored and the mission continue. (Post-fire Clean-up)

Other statements in the same deck:
- "Spacecraft designers and mission operations personnel will (generally) not realize the extent of the fire safety question they need answered until a solution is needed (quickly)".
- "As we push forward into new missions, we get further and further from what we know. Our ability to accurately quantify the risks decreases dramatically." Examples given: partial gravity (flammability, detection, suppression), elevated oxygen mole fraction and reduced pressures, dormancy.
- The flow chart that decides whether a vehicle needs fire detection and suppression "hasn't changed since it was developed for ISS itself" and "Doesn't account for new test results and data".
- "NASA doesn't have a clear set of items that must be demonstrated" to certify a fire detection or suppression system.
- "For the Saffire-IV PMMA sample, we turned off the flow for 20 seconds. The fire didn't extinguish and began to grow when we turned the flow back on".
- "Test data are invaluable to validate modeling of fire scenarios".

## Needs matched to data, most relevant to the challenge first
| # | NASA need | In our PSI snapshot | Outside PSI |
|---|---|---|---|
| A | **Earth-gravity screening may miss the risk** (Ruff risk 1) | BASS-II lowest oxygen is 13.6 %. Saffire-II pairs microgravity and 1-g burns (9 rows, both directions). BASS record text on NASA-STD-6001 Test 1 | BASS-II poster (read directly): "The 1g blowoff for the ¼” rod is at 16% oxygen, whereas we obtained steady spreading at 13.6% oxygen in BASS-II. Thus the material has a negative Oxygen Margin of Safety of 2.4% O2, and the normal gravity flammability limits should be de-rated by at least that much." Search summary: other work reports margins negative by up to 5.75 % O2; some sources call Test 1 conservative instead |
| B | **Higher oxygen at lower pressure** (need 21.01) | Solids tested at 13.6-22.2 %; 30 % and above only gases and droplets; BRE text on elevated oxygen | Search summaries: at 8.2 psia and 34-40 % oxygen about 70 % of assessed life-support subsystems need material replacements; ISS textiles may not be usable above 30 %; Saffire IV-VI burned solids at about 22-31 % oxygen; SoFIE slides say few thin materials passed 1-g testing at 34 % and 8.2 psia |
| C | **Decision rules do not use the new data** (Ruff slides 2, 15, 17) | The 24 records and their tables are that data; only 10 state ambient oxygen | The Ruff deck itself |
| D | **Putting fires out** (risk 6) | BRE: burning continued "despite the absence of air flow". FLEX: 274 droplet extinction rows. BASS-II: flow settings per test | Ruff slide 16 (Saffire-IV flow off 20 s). Search summary: a 2026 paper finds depressurization unsafe as suppression |
| E | **Fire growth, smoke and toxic gases** (risk 3) | BASS-II final O2, CO2, CO per test. Saffire-I to III burn rows | Search summary: Saffire-VI found CO2 and CO a bigger concern than heat or pressure |
| F | **Detection** (risk 5) | SAME, SAME-R (117 rows), DAFT (2 rows): smoke particle size | Search summary: NASA white paper calls current detection inadequate |
| G | **Partial gravity** (need 21.01) | Nothing | Search summaries: LUCI sounding rocket burned PMMA and SIBAL at lunar gravity, 9-21 % oxygen; 2026 conference abstracts say lunar gravity may be near the most flammable condition; the FM2 lunar-surface experiment has no results I could find |
| H | **Ignition, crew response, clean-up** (risks 2, 4, 7) | Little or nothing | Not searched in depth |

## Other data sources and whether we can use them by Sunday
| Source | What it is | Usable? |
|---|---|---|
| NTRS (ntrs.nasa.gov) | NASA's open report server; PDFs of the Saffire IV-VI, BASS-II and needs papers | Yes, as cited quotations. Numbers would be transcribed by hand from papers, each with its NTRS link. It has no data tables to download |
| OpenAlex abstracts | Already fetched by Victor, 73 of 235 | Yes |
| Saffire IV-VI | Solids at elevated oxygen | No dataset found; papers only. Not in PSI (PSI holds Saffire I-III) |
| SoFIE | ISS solid-fuel tests at exploration atmospheres | Not in PSI: searching PSI for "SoFIE" returns only BASS-II. Slides only |
| MAPTIS | NASA's material flammability test database | No: access by request form |
| flame.sdsu.edu | BASS-II catalogue named in the 2014 poster | Not checked whether it still exists |
| FM2 | Flammability test on the lunar surface | No results found |

## Limits
- The challenge asks for PSI data. Outside sources can support or frame the story; they cannot replace PSI as the data the dashboard runs on.
- Everything marked "search summary" is unverified until opened.

## Sources
- [2026 Civil Space Shortfalls](https://www.nasa.gov/wp-content/uploads/2026/03/2026-civil-space-shortfalls.pdf)
- [FY26 Civil Space Shortfall Prioritization](https://www.nasa.gov/wp-content/uploads/2026/05/fy26-civil-space-shortfall-prioritization.pdf)
- [Ruff, Spacecraft Fire Safety Needs for Exploration, 2020](https://ntrs.nasa.gov/api/citations/20205007829/downloads/Exploration%20Needs%20in%20Fire%20Safety_9-25-2020.pdf)
- [Ferkul et al., Results from the BASS-II Experiment, 2014 poster](https://ntrs.nasa.gov/api/citations/20160000593/downloads/20160000593.pdf)
- [2024 Civil Space Shortfall Ranking](https://www.nasa.gov/wp-content/uploads/2024/07/civil-space-shortfall-ranking-july-2024.pdf)
- [Reduced pressure atmospheres and life-support architectures](https://ntrs.nasa.gov/citations/20240003211)
- [2026 ICES paper on fire-resistant textiles](https://ntrs.nasa.gov/api/citations/20260003042/downloads/301-ICES_Paper_2026-FR-Textiles_Final_04-13-2026.pdf)
- [Fire detection white paper](https://ntrs.nasa.gov/api/citations/20210022143/downloads/Fire%20detection%20white%20paper%20final%20211031.pdf)
- [Saffire VI preliminary results, ICES 2024](https://ntrs.nasa.gov/citations/20240002981)
- [SoFIE project on ISS](https://ntrs.nasa.gov/search.jsp?R=20200000361)
- [Ferkul et al., material flammability at lunar and Martian gravity, LPSC 2026](https://www.hou.usra.edu/meetings/lpsc2026/pdf/1799.pdf)
- [Risks of depress as a fire suppression technique, ICES 2026](https://ttu-ir.tdl.org/items/cd24669b-8515-4bef-8304-bdeb0409c4aa)
- [LUCI, NASA Task Book](https://taskbook.nasaprs.com/tbp/index.cfm?action=public_query_taskbook_content&TASKID=492A5F96AAA7FB9492887E390BF6713F)

See also: [[Step 1 decision sheet]], [[Vetted reference from the external briefs]], [[PSI data source]].
