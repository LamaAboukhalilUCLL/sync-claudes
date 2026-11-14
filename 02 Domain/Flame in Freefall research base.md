# Mapping fire's blind spots for lunar habitats

The strongest finding for a "Flame in Freefall" dashboard is a coverage gap. NASA's Physical Sciences Informatics (PSI) repository holds about two dozen completed combustion investigations. Its solid-material tests sit almost entirely near air-level oxygen (about 21-22%). Its gas and droplet tests reach 40% ambient oxygen, but with no real partial gravity. The planned lunar and Martian atmosphere, by contrast, is **34% oxygen at 8.2 psia, with materials certified at 37%** ([Aly et al., ICES-2026-301](https://ntrs.nasa.gov/api/citations/20260003042/downloads/301-ICES_Paper_2026-FR-Textiles_Final_04-13-2026.pdf)). That matters because the PSI data say three things together:

- Microgravity is **not automatically safer than Earth**. PMMA (acrylic) burned at 13.6% oxygen in orbit against a 16% limit at 1 g ([BASS-II poster](https://ntrs.nasa.gov/api/citations/20160000593/downloads/20160000593.pdf)).
- **Still air puts out flames at 21% oxygen but not at 26.5% and above**. In the Burning Rate Emulator (BRE) tests, all flames in 21% oxygen went out on their own within 40 s, while flames at 26.5%, 34% and 40% kept burning ([Dehghani 2022](https://drum.lib.umd.edu/items/c6e2cba9-7fb5-4496-828e-7a38138de1ff/full)).
- A fire of only about 3 kW in a spacecraft-sized cabin hits **carbon monoxide (CO) and carbon dioxide (CO2) limits before the cabin gets hot**, and the smoke alarm sounded about six minutes after ignition, after most of the toxic gas was already out ([Saffire-VI, ICES-2024-365](https://ntrs.nasa.gov/api/citations/20240002981/downloads/Saffire-ICES-2024-ICES-365-accepted%20final.pdf)).

Partial gravity is a real gap, not a bounded one. Flammability can peak between 0 g and 1 g, so microgravity and Earth results do not automatically bracket the Moon or Mars. The one flown lunar-g test, LUCI (2025), did not test the conditions where the worst case is predicted. FM2, the lunar-surface flammability experiment, has not reported results. For the build, PSI has no documented API: the team's own (undocumented) JSON endpoints plus a committed snapshot are the practical path. The corpus is small enough to hand-check, so the AI should extract text attributes with quoted evidence while code computes every number.

Two caveats run through this whole report. First, psi.nasa.gov and the challenge page could not be fetched during research. Every `PSI-<n>` identifier, table row count and endpoint below comes from the team's own 14 Nov 2026 notes and has not been independently re-verified. Second, items that the notes mark as unverified, conflicting or from outside PSI are labelled as such, and the verification ledger near the end lists them all.

## Three sources of truth, and how far each can be trusted

The research rests on three layers of evidence, and the dashboard should keep them visibly separate.

- **NASA's public "PSI investigations by research area" page.** It lists **19 Combustion Science entries, all "Complete"** ([NASA PSI by research area](https://www.nasa.gov/physical-sciences-informatics-psi/psi-investigations-by-research-area/)). The page is out of date compared with the repository: it leaves out ACME CFI-G, CLD Flame and Flame Design.
- **The team's own browser crawl of the repository (14 Nov 2026).** A "combustion" search returned 26 hits, of which 24 are combustion investigations. The crawl recorded IDs, table sizes, raw-data volumes and a CC0-1.0 licence on the records checked (team notes `02 Domain/Investigations overview.md` and `03 Data/PSI data source.md`; not re-verified).
- **Published papers, NASA Technical Reports Server (NTRS) reports and NASA pages, fetched directly.** They supply nearly all the physics and the quantitative results.

The challenge wording also comes second-hand. The phrases "CFI-G up to 85% oxygen" and "E-FIELD Flames mimicked partial gravity", and the exploration-atmosphere framing, are quoted from the team's `01 Challenge/Challenge brief.md`. The live page refused automated fetching.

The practical consequence: the PSI repository is the source of truth for *which* investigations exist and what their test matrices are, and the papers are the source of truth for *what they found*. The experiment tables (the "experimental table" of samples and runs on each PSI record) are mostly small test lists, not measurement data. Two examples:

- BRE's PSI table has **18 day-level rows**, so heat-flux and mass-flux values must come from the papers.
- The FLEX-2 table has only 8 rows, each covering a group of tests through multi-value cells such as "0.17; 0.21; 0.25; 0.3" (team note, not re-verified).

## Twenty-four PSI combustion records, sorted by fire-safety value

The table below gives the team's 24-record inventory. Identifiers come from the team note and were **not re-verified**. Record pages follow the pattern `https://psi.nasa.gov/physci/repo/data/investigations/PSI-<n>`; NASA's BPS Data page confirms this pattern ([BPS Data](https://science.nasa.gov/biological-physical/data/)). Row counts are the team's first look. The relevance ratings are the research team's own judgement, not NASA's.

Hardware abbreviations used in the table and below:

- **ISS:** International Space Station.
- **CIR:** Combustion Integrated Rack, the station's only rack dedicated to combustion.
- **ACME:** the set of gas-flame experiments run inside the CIR.
- **MDCA:** Multi-user Droplet Combustion Apparatus, also inside the CIR.
- **MSG:** Microgravity Science Glovebox.
- **Cygnus:** the uncrewed cargo vehicle used for Saffire after it left the ISS.

| PSI ID                    | Investigation                                                                                                                                                                                   | Fuel type / geometry                                                                              | Platform                  | PSI table (team first look)              | Fire-safety relevance             |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------- | ---------------------------------------- | --------------------------------- |
| PSI-20                    | ACME BRE (Burning Rate Emulator)                                                                                                                                                                | Ethylene or methane gas through flat porous burner, 25 and 50 mm, standing in for a burning solid | ISS CIR/ACME              | 18 rows, O2 21-40%                       | High                              |
| PSI-69                    | FLEX (Flame Extinguishment)                                                                                                                                                                     | Single fuel droplets, 1.5-5 mm                                                                    | ISS CIR/MDCA              | 274 rows, O2 0.12-0.34                   | High                              |
| PSI-25                    | BASS-II                                                                                                                                                                                         | PMMA sheets, rods and slabs; SIBAL fabric                                                         | ISS MSG wind tunnel       | 129 rows, O2 13.6-22.2%, 51 sample kinds | High                              |
| PSI-98/99/100             | Saffire-I/II/III                                                                                                                                                                                | Large SIBAL fabric (0.4 x 0.94 m); nine material coupons on Saffire-II                            | Cygnus, after leaving ISS | 4 / 15 / 2 rows                          | High                              |
| PSI-102/101               | SAME / SAME-R                                                                                                                                                                                   | Smoke from overheated (not burning) Teflon, Kapton, silicone, cotton, Pyrell foam                 | ISS MSG                   | 8 / 109 rows                             | High (detection)                  |
| PSI-159                   | ACME CFI-G (Cool Flames with Gases)                                                                                                                                                             | Ethane, propane, n-butane; 6.4 mm porous sphere                                                   | ISS CIR/ACME              | 179 rows, O2 0.18-0.40                   | Medium-high                       |
| PSI-39                    | CFI (Cool Flames, droplets)                                                                                                                                                                     | Droplets                                                                                          | ISS CIR/MDCA              | 87 rows, O2 0.17-0.21, 0.5-5 atm         | Medium-high                       |
| PSI-26                    | BASS                                                                                                                                                                                            | PMMA spheres, SIBAL fabric, candle wax                                                            | ISS MSG                   | 122 rows                                 | Medium                            |
| PSI-10                    | ACME Flame Design                                                                                                                                                                               | Ethylene (table also lists propane); porous sphere                                                | ISS CIR/ACME              | 207 rows, O2 0.198-0.40                  | Medium                            |
| PSI-23                    | ACME s-Flame                                                                                                                                                                                    | Hydrogen, methane and mixtures, ethylene; nitrogen or helium diluent; sphere                      | ISS CIR/ACME              | 18 rows                                  | Medium                            |
| PSI-21                    | ACME CLD Flame                                                                                                                                                                                  | Nitrogen-diluted methane and ethylene; coflow burner                                              | ISS CIR/ACME              | not recorded                             | Medium                            |
| PSI-107                   | SPICE (smoke point)                                                                                                                                                                             | Gas jets of six hydrocarbon fuels and blends                                                      | ISS (MSG per team note)   | 469 rows                                 | Medium                            |
| PSI-68                    | FLEX-2                                                                                                                                                                                          | Droplets, droplet pairs, two-component fuels                                                      | ISS CIR/MDCA              | 8 rows                                   | Medium                            |
| PSI-22                    | ACME E-FIELD Flames                                                                                                                                                                             | Methane and ethylene gas jets with up to 10 kV applied                                            | ISS CIR/ACME              | 32 rows                                  | Medium (body-force analogue only) |
| PSI-106                   | SLICE                                                                                                                                                                                           | Nitrogen-diluted methane gas jet in coflowing air                                                 | ISS (MSG per team note)   | 12 rows                                  | Low-medium                        |
| PSI-47                    | DAFT / DAFT-2                                                                                                                                                                                   | Dust and particle-counter feasibility test                                                        | ISS                       | 2 rows                                   | Low                               |
| PSI-62, 115, 117, 142, 60 | Ground studies: flame-spread modelling (BASS data), smoke simulation (SAME data), cool-flame computer simulation (FLEX data), cool-flame transitions in counterflow flames, SPICE data analysis | Modelling and ground tests                                                                        | Ground                    | n/a                                      | Model-validation links            |

Several investigations are **not in PSI** according to the team's crawl and NASA's list. They should appear in the dashboard only as "related, outside PSI" context cards:

- **Droplet and Shuttle-era:** FLEX-2J and FLEX-ICE-GA (droplet experiments), and the Shuttle-era DCE, FSDC, LSP, ELF, TGDF, SOFBALL and SSCE.
- **Newer solid-fuel work:** SoFIE (all five projects), Saffire-IV/V/VI, and Confined Combustion.
- **Partner and partial-gravity work:** JAXA's FLARE, LUCI and FM2.

This matters because the best exploration-atmosphere solid data (Saffire-V and VI, SoFIE) sit outside PSI. A dashboard limited to PSI will under-represent exactly the conditions the challenge cares about unless it adds literature values by hand, and labels them as such. It is also unverified whether PSI files any of these under names a "combustion" search missed.

## Gas and droplet flames: extinction limits, cool flames and soot

### The ACME suite

The six ACME investigations shared one instrument, so their numbers are directly comparable:

- **Chamber:** an insert of about 83 L free volume in the station's Combustion Integrated Rack (CIR).
- **Gas supply:** three mass-flow controllers.
- **Burners:** one at a time, from gas-jet, coflow, spherical-porous or flat-porous types.
- **Sensors:** radiometers; photomultiplier tubes for CH* and OH* (light emitted by short-lived molecules in the flame); a thermocouple rake; thin silicon-carbide fibres, 14 micron, for thin-filament pyrometry; and five cameras, including a soot light-extinction view and intensified OH* and CH*/CH2O cameras.

Source: [ACME overview paper](https://ntrs.nasa.gov/api/citations/20210021781/downloads/JASMAC%20ACME%20paper%2020210921.pdf). ACME ran about four and a half years from 2017 and ignited **over 1,500 flames, more than three times the plan**, before it was removed to make room for SoFIE, launched in February 2022 ([NASA, Quest for the Secrets of Fire](https://www.nasa.gov/humans-in-space/space-stations-quest-for-the-secrets-of-fire/)).

**BRE (PSI-20)** is the one gas experiment built explicitly for spacecraft fire prevention.

- **Concept:** gas fed through a flat porous burner with embedded heat-flux gauges stands in for a burning solid or liquid. The ethylene/nitrogen mixtures were chosen to match the heat of combustion, heat of gasification, surface temperature and smoke point of real plastics ([ACME overview paper](https://ntrs.nasa.gov/api/citations/20210021781/downloads/JASMAC%20ACME%20paper%2020210921.pdf)).
- **Conditions:** 25 and 50 mm burners, **oxygen 21-40%, pressure 0.57-1 bar, no imposed airflow** ([Wright 2021](https://drum.lib.umd.edu/items/b21822b4-9024-46d6-8cef-88f1e01a9d31/full)).
- **Varied:** fuel flow, dilution, oxygen, pressure and burner size.
- **Sensors:** heat-flux gauges, a slug calorimeter, radiometers and cameras.
- **Headline result:** every flame at 21% oxygen self-extinguished within 40 s, while flames at 26.5%, 34% and 40% burned steadily ([Dehghani 2022](https://drum.lib.umd.edu/items/c6e2cba9-7fb5-4496-828e-7a38138de1ff/full)). The programme-level summary puts the threshold at **about 25% oxygen by volume**; methane flames went out within about a minute, while ethylene at raised oxygen burned for minutes ([ACME overview paper](https://ntrs.nasa.gov/api/citations/20210021781/downloads/JASMAC%20ACME%20paper%2020210921.pdf)).
- **Model outputs:** BRE produced flammability maps (heat of gasification against heat of combustion) at oxygen fractions of 0.265, 0.34 and 0.40 ([Dehghani 2022](https://drum.lib.umd.edu/items/c6e2cba9-7fb5-4496-828e-7a38138de1ff/full)). It also produced an extinction-time correlation, scaling as **oxygen fraction cubed times Reynolds number to the power -0.5**, with no dependence on pressure ([Wright 2021](https://drum.lib.umd.edu/items/b21822b4-9024-46d6-8cef-88f1e01a9d31/full)).

The 30%-plus exploration atmosphere sits on the burning side of BRE's threshold. That is the cleanest single fire-safety statement any gas experiment in PSI supports.

**CFI-G (PSI-159)** is where the challenge's "85% oxygen" comes from, and the figure needs care.

- **Setup:** ethane, propane and n-butane on a 6.4 mm sintered-steel porous sphere.
- **Normal flames** (fuel from the burner): ambient oxygen of **only 0.21-0.40**.
- **Inverse flames:** the *burner* injected oxidizer at 0.12-0.85 oxygen into a fuel/nitrogen atmosphere. **The 85% is injected oxidizer, not cabin oxygen.**
- **Pressure:** 0.46-3 bar.
- **Outcomes:** 280 hot flames ignited and 189 went out from radiative heat loss. Fifteen cool flames appeared, only for n-butane at 2 bar, 39% oxygen and a burner hotter than 515 K.
- **Re-ignition:** with a thermocouple present, the system cycled between cool and hot flames.

Source for all of the above: [Kim et al. 2023](https://par.nsf.gov/servlets/purl/10426596). The fire-safety reading is that a flame that looks out can leave a near-invisible cool flame that later re-ignites.

The remaining ACME investigations mainly supply model-validation data:

- **CLD Flame (PSI-21):** methane and ethylene coflow flames at matched fuel and air speeds of 10-40 cm/s, close to spacecraft ventilation speeds. Sooty microgravity flames carried **5 to 8 times more soot** than the same flames at 1 g, and weak mixtures stayed lit at lower fuel concentrations ([ACME overview slides](https://ntrs.nasa.gov/api/citations/20210022542/downloads/ACME%20JASMAC-33%2020211007.pdf)).
- **Flame Design (PSI-10):** spherical ethylene flames up to 40% oxygen. Small flames reached steady state; large flames grew until radiative loss put them out, after an oscillating partial quench-and-reform phase ([ACME overview slides](https://ntrs.nasa.gov/api/citations/20210022542/downloads/ACME%20JASMAC-33%2020211007.pdf)).
- **s-Flame (PSI-23):** found extinction from radiative loss at high flow and kinetic (chemistry-limited) extinction at low flow, with helium dilution shifting both limits. No journal paper reporting the flight data was found ([ACME overview slides](https://ntrs.nasa.gov/api/citations/20210022542/downloads/ACME%20JASMAC-33%2020211007.pdf)).
- **E-FIELD Flames (PSI-22):** applied up to 10 kV between the burner and a downstream mesh ([ACME overview paper](https://ntrs.nasa.gov/api/citations/20210021781/downloads/JASMAC%20ACME%20paper%2020210921.pdf)). Ions made in the flame drag the surrounding gas with them, an "ion wind" ([NASA Science, E-FIELD Flames](https://science.nasa.gov/biological-physical/investigations/e-field-flames)). This is a real body force, like buoyancy. A drop-tower precursor found that an electric field alone can make microgravity flames look like 1 g flames ([Combust. Sci. Technol., doi:10.1080/00102202.2012.694740](https://informahealthcare.com/doi/full/10.1080/00102202.2012.694740)). A simulation study equated a 2 g flame to a 1 g flame with 0.5 kV/cm applied, but only for a 2-D methane/air case ([Lopez-Camara 2020](https://escholarship.org/content/qt2057k3tp/qt2057k3tp.pdf)).

**No source gives a voltage-to-gravity calibration for the ISS tests, and the challenge's "mimicked partial gravity" wording was not traced to a primary NASA source.** NASA itself says E-FIELD was not run for a specific space application ([NASA Science](https://science.nasa.gov/biological-physical/investigations/e-field-flames)). Present it as a qualitative body-force analogue, not as partial-gravity data.

### FLEX, cool flames and suppressants

**FLEX (PSI-69)** was purpose-built to test inert-gas fire suppressants.

- **When and what:** run from March 2009 to December 2011 ([UC San Diego](https://today.ucsd.edu/story/how_do_you_fight_fire_in_space_experiments_provide_some_answers)). Free or fibre-tethered droplets of 1.5-5.0 mm burned at **oxygen 0.1-0.4, pressure 0.7-3.0 atm**, with nitrogen, CO2 or helium as diluent ([Dietrich et al. 2014](https://link.springer.com/doi/10.1007/s12217-014-9372-2)).
- **Two extinction modes:** diffusive extinction for small droplets and radiative extinction for large ones.
- **Limiting oxygen index (LOI):** the lowest oxygen level at which steady burning continues. In oxygen/nitrogen it is **methanol about 0.12 and heptane about 0.15**. Adding CO2 raises it only to 0.14 and 0.17, and that takes 20-30% CO2, a level that is itself dangerous to crew ([Dietrich et al. 2014](https://link.springer.com/doi/10.1007/s12217-014-9372-2)).
- **Helium:** gave heptane almost no benefit.
- **Xenon:** simulations validated against ISS data indicate xenon *lowers* the LOI and so is a poor suppressant ([Combust. Sci. Technol. 2016](https://informahealthcare.com/doi/full/10.1080/00102202.2015.1085033)). The authors were not visible on the fetched page, and whether FLEX burned droplets in xenon on orbit is unconfirmed.
- **Test-count conflict:** one source says over 300 tests ([Nayagam et al. 2014](https://ntrs.nasa.gov/api/citations/20140006750/downloads/20140006750.pdf)), while the NASA data report covers "the first 284 tests" ([NTRS 20150023456](https://ntrs.nasa.gov/citations/20150023456)). Use the PSI record's count.

FLEX's biggest surprise was the **cool flame**. Large heptane droplets kept vaporising at nearly the hot-flame rate after the visible flame had radiated itself out ([Dietrich et al. 2014](https://link.springer.com/doi/10.1007/s12217-014-9372-2)). The burning rate was **about 80% of the hot-flame rate**, and the effect also appeared with n-octane and n-decane ([Nayagam et al. 2014](https://ntrs.nasa.gov/api/citations/20140006750/downloads/20140006750.pdf)). It produced carbon monoxide and formaldehyde, and it occurred even in nitrogen-, CO2- and helium-diluted atmospheres ([UCSD/Nanowerk 2014](https://www.nanowerk.com/news2/space/newsid=36716.php)). The peak temperature of about 700 K is a model value, not a measurement. No source quantified CO or formaldehyde yields. For fire safety, "visible flame out" is **not an all-clear**.

### Smoke-point and jet-flame data

- **SPICE (PSI-107):** gas-jet flames of methane through propylene in coflowing air, at nozzles of 0.76-3.2 mm and air speeds of 3-47 cm/s. It produced **112 smoke points** (the flame length at which soot starts to escape), with smoke-point length scaling as nozzle diameter^-0.67 and coflow speed^0.27 ([DeBold 2012 thesis](https://drum.lib.umd.edu/items/8f83b34a-3a69-45d6-9aef-26aa04bcef43/full)).
- **SLICE (PSI-106):** 36 flames, half at 0 g and half at 1 g. Microgravity flames were **28% longer and about 300 K cooler** at the peak centreline ([Cao et al. 2014 preprint](https://ntrs.nasa.gov/api/citations/20150002322/downloads/20150002322.pdf)).
- **Unverified:** the investigator names and MSG hardware for SPICE and SLICE come from the researcher's recall and the team note, not from a fetched source.

## Solid materials and smoke: the evidence closest to real cabins

### BASS and BASS-II: materials burn at lower oxygen in orbit

BASS-II (PSI-25) is the clearest proof that Earth-based screening tests are not conservative.

- **Setup:** a small wind tunnel in the Microgravity Science Glovebox (MSG). Oxygen was lowered with nitrogen to 13.6-21%, with both opposed and concurrent flow. Samples were thin and thick PMMA, PMMA rods, and SIBAL cotton-fibreglass fabric.
- **Headline result:** a 1/4-inch PMMA rod spread steadily at **13.6% oxygen in microgravity, against a 16% limit at 1 g**. That is a **"negative oxygen margin of safety" of 2.4 percentage points**, and the team said Earth limits "should be derated by at least that amount" ([BASS-II poster](https://ntrs.nasa.gov/api/citations/20160000593/downloads/20160000593.pdf)).
- **Flow-speed data:** flow speed was quoted inconsistently in the same poster, as "up to 40 cm/s" and "0 to 55 cm/s".
- **Cylinder results:** flames sustained at 17% oxygen in 0 g, while 1 g flames could not exist at 18% or below. Spread rate rose and then fell with flow, and no flame spread below about 0.6 cm/s ([Link et al., Sci. Rep. 2018](https://link.springer.com/10.1038/s41598-017-18398-4)).
- **Fan-off quenching:** flames always went out when the fan was switched off, which supports the ISS practice of stopping ventilation in a fire. Quiescent tests at elevated oxygen suggest **this may not hold** in high-oxygen, low-pressure or partial-gravity conditions ([Olson et al., ICES 2019](https://ttu-ir.tdl.org/items/1922ad9f-ef4c-4f52-96a4-980c23debe5e)).

**Conflict to show, not resolve:** the SoFIE overview quotes a negative margin of **1.4%** for PMMA rods ([NTRS 20200000361](https://ntrs.nasa.gov/api/citations/20200000361/downloads/20200000361.pdf)). It probably refers to different rod sizes or 1 g reference tests, so report both values with their sources.

BASS (PSI-26) used the same tunnel with PMMA spheres, SIBAL and candles. Two SIBAL points from it (spread 2.7 and 5.1 mm/s in a 7.6 cm duct) serve as small-scale anchors for Saffire ([Olson et al. manuscript](https://discovery.ucl.ac.uk/id/eprint/10164340/1/SIBAL-cotton%20revised%20Sept%20per%20review%20track%20changes%20accepted.pdf)).

### SoFIE (outside PSI): extinction data at higher oxygen

SoFIE, the Solid Fuel Ignition and Extinction facility in the CIR, extends the same physics but is **outside PSI**.

- **Setup:** a 4 cm PMMA sphere at about 1 atm, oxygen 13-28%.
- **U-shaped limit:** the lowest extinction oxygen (**13.5% at about 11.5 cm/s**) came at intermediate flow. More oxygen was needed for the flame to survive at very low flow (14.2% at 4.8 cm/s; 20.8% at 0.44 cm/s) and at high flow (15.0% at 34 cm/s) ([Li et al., NTRS 20240007628](https://ntrs.nasa.gov/api/citations/20240007628/downloads/GELsymposiumfinalRev1.pdf)).
- **Sphere-size conflict:** the SoFIE overview says "40 cm" spheres. The flight paper says 4 cm; treat 4 cm as correct.
- **Missing results:** SMuRF (the project aimed at spacecraft materials in exploration atmospheres) and MIST (ignition and extinction maps under radiant heating) had **no retrieved flight results**.

### Saffire: fires at real scale

The Saffire series (PSI-98/99/100 for I-III; IV-VI outside PSI) burned large samples inside Cygnus after it left the ISS, in a vehicle volume of about 19 m³ ([Saffire ICES 2024 presentation](https://ntrs.nasa.gov/api/citations/20240007488/downloads/Saffire%20ICES%202024%20Saffire%20presentation072124small.pdf)). Large fabric flames in microgravity settle to a **short, steady length and a spread rate of about 2-4 mm/s**, instead of growing without limit as upward flames do on Earth. Confinement matters: spread roughly doubled when the duct height dropped from 51 to 30.5 cm ([Olson et al. manuscript](https://discovery.ucl.ac.uk/id/eprint/10164340/1/SIBAL-cotton%20revised%20Sept%20per%20review%20track%20changes%20accepted.pdf)).

Saffire-VI moved into exploration-like atmospheres: SIBAL at **31.0% oxygen and 54.1 kPa**, and PMMA at 28.8-30.3% oxygen and about 55 kPa. Nomex did not ignite, and both PMMA samples kept growing until the flow was cut ([ICES-2024-365](https://ntrs.nasa.gov/api/citations/20240002981/downloads/Saffire-ICES-2024-ICES-365-accepted%20final.pdf)).

| Test | Burn (s) | Peak heat release (W) | Total heat (kJ) | CO2 rise (ppm / mmHg) | CO rise (ppm) |
|---|---|---|---|---|---|
| IV-1 SIBAL | 130 | 3,150 | 409 | 1,390 / 1.03 | 80 |
| V-2 cotton | 200 | 2,800 | 560 | 2,360 / 1.26 | 83 |
| VI-2 SIBAL | 112 | 3,217 | 580 | 2,800 / 1.15 | 120 |
| VI-3 PMMA, two-sided | 780 | 3,080 | 1,280 | 8,539 / 3.51 | 308 |
| VI-4 PMMA, one-sided | 1,200 | 1,507 | 830 | 8,117 / 3.37 | 320 |

Source: [ICES-2024-365](https://ntrs.nasa.gov/api/citations/20240002981/downloads/Saffire-ICES-2024-ICES-365-accepted%20final.pdf); [presentation](https://ntrs.nasa.gov/api/citations/20240007488/downloads/Saffire%20ICES%202024%20Saffire%20presentation072124small.pdf).

Both PMMA burns pushed CO2 over the **1-hour limit of 3 mmHg** and CO over the **24-hour limit of 100 ppm**, while cabin temperature barely moved. The ionisation smoke detector reached its alarm level **344 s after ignition, after much of the toxic gas had been released** ([ICES-2024-365](https://ntrs.nasa.gov/api/citations/20240002981/downloads/Saffire-ICES-2024-ICES-365-accepted%20final.pdf)). PMMA produced about three times the CO2 and CO of the fabrics because it burned 6-10 times longer, not because it burned hotter.

Two conflicts must stay visible:

- **Heat release:** a 2021 abstract reports heat release "up to 10 kW" ([Urban et al., ICES 2021](https://ttu-ir.tdl.org/items/ee71c701-f97a-437e-be4a-1193c517cadf)), against 1.5-3.2 kW peaks in the 2024 tables.
- **Saffire-IV/V conditions:** the ICES tables give 22.0% oxygen / 100.0 kPa and 26.2% / 70.7 kPa, while the journal manuscript gives 23.1% / 99 kPa and 26.9% / 76 kPa. Duct heights also differ between the two sources ([ICES-2021-266](https://ntrs.nasa.gov/api/citations/20210011521/downloads/ICES%202021-266%200503-2021%20final.pdf)).

### SAME and SAME-R: smoke particles too small for the ISS detector

SAME (PSI-102) and SAME-R (PSI-101) overheated five spacecraft materials below ignition and aged the smoke for 10-1,800 s. They measured particle number, size and mass, and collected particles for electron-microscope (TEM) images ([Urban et al., SAE 2009-01-2468](https://saemobilus.sae.org/papers/smoke-particle-sizes-low-gravity-implications-spacecraft-smoke-detector-design-2009-01-2468)).

- **Particle sizes:** geometric mean diameters were about **140-380 nm** depending on material and ageing ([Meyer et al. 2015](https://core.ac.uk/download/33145886.pdf)). The ISS forward-scattering detector is most sensitive **above about 1 micron**.
- **Detector misses:** the ISS detector missed Kapton smoke in about half of tests and Teflon smoke in about two-thirds ([Fortenberry et al. white paper](https://ntrs.nasa.gov/api/citations/20210022143/downloads/Fire%20detection%20white%20paper%20final%20211031.pdf)).
- **Gravity effect, nuanced:** Meyer et al. found low-g and 1 g particles similar at typical flow, and larger only in a no-flow test. The white paper says particles were larger below 8.1 cm/s. The common claim that "microgravity smoke is bigger" holds only at low flow.
- **Two numbers to keep apart:** a NASA summary quotes means of about 100-200 nm, with silicone at 227 nm but nearly half its mass above 1 micron ([NASA SAME summary](https://www.nasa.gov/wp-content/uploads/2025/07/smoke-aerosol-measurement-experiment-same.pdf)). Those are different statistics from Meyer's geometric means, so label which one is shown.
- **DAFT (PSI-47):** a feasibility test that checked a commercial particle counter (the P-Trak, down to 20 nm) works in long-duration microgravity, as risk reduction for SAME ([Sheredy 2005](https://ntrs.nasa.gov/citations/20050215648)).

## Numbers that a flammability model can actually use

Most model-ready numbers sit in the papers rather than in PSI's small tables. Together they form six groups that a "predictive" panel can draw on:

| Quantity | Value | Source |
|---|---|---|
| Droplet LOI, oxygen/nitrogen | Methanol 0.12, heptane 0.15 (0.14 / 0.17 with CO2) | [Dietrich et al. 2014](https://link.springer.com/doi/10.1007/s12217-014-9372-2) |
| Hot vs cool-flame burning rates | n-decane 0.41 vs 0.33 mm²/s; n-octane 0.48 vs 0.38 mm²/s (cool ≈ 80% of hot) | [Nayagam et al. 2014](https://ntrs.nasa.gov/api/citations/20140006750/downloads/20140006750.pdf) |
| Quiescent oxygen threshold (BRE) | Out within 40 s at 21%; steady at 26.5/34/40%; programme value about 25% | [Dehghani 2022](https://drum.lib.umd.edu/items/c6e2cba9-7fb5-4496-828e-7a38138de1ff/full) |
| Solid oxygen limits, 0 g vs 1 g | PMMA rod 13.6% vs 16%; cylinders 17% vs above 18%; sphere 13.5-15% at 5-50 cm/s | [BASS-II](https://ntrs.nasa.gov/api/citations/20160000593/downloads/20160000593.pdf); [Link 2018](https://link.springer.com/10.1038/s41598-017-18398-4); [GEL](https://ntrs.nasa.gov/api/citations/20240007628/downloads/GELsymposiumfinalRev1.pdf) |
| Extinction flow speeds | Thin PMMA quenches below about 2 cm/s and blows off at about 40 cm/s | [BASS-II](https://ntrs.nasa.gov/api/citations/20160000593/downloads/20160000593.pdf) |
| Concurrent spread, fabrics | 1.8-2.6 mm/s (51 cm duct), 3.4-3.6 (30.5 cm), 2.7-5.1 (7.6 cm); scales with oxygen × √pressure | [Olson et al.](https://discovery.ucl.ac.uk/id/eprint/10164340/1/SIBAL-cotton%20revised%20Sept%20per%20review%20track%20changes%20accepted.pdf) |
| Heat release and toxic yield | 1.5-3.2 kW peak; CO2 +1,390 to +8,539 ppm; CO +80 to +320 ppm in about 17-19 m³ | [ICES-2024-365](https://ntrs.nasa.gov/api/citations/20240002981/downloads/Saffire-ICES-2024-ICES-365-accepted%20final.pdf) |
| Smoke size | Geometric mean 139-382 nm; size spread (GSD) 1.6-2.2 | [Meyer et al. 2015](https://core.ac.uk/download/33145886.pdf) |
| Soot | 5-8× more soot at 0 g (CLD); smoke-point scaling (SPICE) | [ACME slides](https://ntrs.nasa.gov/api/citations/20210022542/downloads/ACME%20JASMAC-33%2020211007.pdf); [DeBold 2012](https://drum.lib.umd.edu/items/8f83b34a-3a69-45d6-9aef-26aa04bcef43/full) |

One thread runs through all of it: **radiative extinction**, where a flame grows until it loses more heat by radiation than it can sustain. It ends large flames in BRE, Flame Design, s-Flame, CFI-G and large FLEX droplets, and it is the low-flow branch of the solid-fuel limit curve.

A dashboard comparison view should carry these features:

- fuel phase and thickness;
- sample geometry and size;
- oxygen fraction **and** total pressure;
- flow speed and direction;
- duct height or confinement;
- gravity level;
- dominant extinction mode.

**Oxygen partial pressure alone is misleading.** Saffire-VI ran 31% oxygen at 54 kPa, an oxygen partial pressure below sea-level air, yet fabrics burned as fast as or faster than in air ([Olson et al.](https://discovery.ucl.ac.uk/id/eprint/10164340/1/SIBAL-cotton%20revised%20Sept%20per%20review%20track%20changes%20accepted.pdf); [ICES-2024-365](https://ntrs.nasa.gov/api/citations/20240002981/downloads/Saffire-ICES-2024-ICES-365-accepted%20final.pdf)).

The data set is too small and varied for free-form machine learning. Physics-based scalings used as transparent estimators, validated against these points and shown with uncertainty, are more defensible. Examples are oxygen × √pressure for spread, stretch rate = 3U/2R (a measure of how strongly the flow strains the flame), and Damköhler-type limits (a ratio of flow time to chemistry time).

The existing NASA cabin model shows the right division of labour. An FDS (Fire Dynamics Simulator) model of Cygnus, validated on Saffire-VI, does **not** model the flame. It injects measured heat and species at the outlet, predicts hydrogen chloride (HCl) transport, and shows HCl above 50 ppm with the fans off. All its runs are at 0 g ([Niehaus et al., ICES-2026-092](https://ntrs.nasa.gov/api/citations/20260001600/downloads/Spacecraft%20Fire%20Safety%20Predictions.pdf)). Its SIBAL heat input (0.45 kW, 124 kJ) is not directly comparable with the 3.2 kW measured peak, so do not chart the two side by side without explanation.

## Partial gravity: why 0 g and 1 g do not bracket the Moon

The challenge's suggestion that microgravity and normal-gravity results could bound intermediate gravity is **only partly true**.

**Where bounding works:** upward (concurrent) spread over thin fuels in air scales roughly **linearly with g from 0.1 to 1 g** ([AIAA 2001-0466](https://ntrs.nasa.gov/api/citations/20010059376/downloads/20010059376.pdf)), so 0 g and 1 g do bracket it.

**Where it fails:** oxygen limits and downward (opposed) spread. Several results point the same way:

- For thin cellulose burning downward, the limiting oxygen fell from **15.6% at 1 g to 13-14% at 0.05-0.1 g**, and spread in air peaked in partial gravity about 20% above the 1 g value ([Sacksteder & T'ien, OSTI 93323](https://www.osti.gov/biblio/93323)).
- SIBAL fabric that cannot burn downward in air at 1 g burned steadily downward at lunar g in centrifuge and aircraft tests ([FM2 poster 2024](https://ntrs.nasa.gov/api/citations/20240008623/downloads/20240008623.pdf)).
- NASA's "Fire on the Moon" charts quote a model in which the required oxygen reaches a **minimum near lunar gravity** ([NTRS 20210020516](https://ntrs.nasa.gov/api/citations/20210020516/downloads/Fire%20on%20the%20Moon-Overview%20charts-v1.pdf)).
- A parabolic-flight wire study found the limit for one wire type fell as gravity fell, while another was nearly insensitive to g ([Konno et al.](https://discovery.ucl.ac.uk/10154634/1/PCI39_CNES-Partial-G-report_manuscript.pdf)).

The FM2 team explains the mechanism as a "goldilocks zone". At lunar g, buoyant flow is slow enough that the flame is not blown off, yet strong enough to keep supplying oxygen. The team itself frames enhanced partial-gravity flammability as a **hypothesis**: partial-gravity fire "may be substantially worse than 0-g and possibly worse than 1-g" ([Ferkul et al., LPSC 2026](https://ntrs.nasa.gov/api/citations/20260000646/downloads/Ferkul-Lunar%20and%20Planetary%20Science%20Conference%202026.pdf)).

### LUCI and FM2

**LUCI (flown, outside PSI)** gives the only direct lunar-g data so far.

- **Flight:** a Blue Origin New Shepard capsule spun at 11 RPM (about 0.165 g) on **4 February 2025**.
- **Test:** SIBAL fabric and a 4 mm PMMA rod burned upward in ordinary air for over 2.5 minutes.
- **Result:** lunar-g spread was **0.38-0.6 times the 1 g rate**, although the SIBAL flame lasted about 45 s longer than at 1 g.
- **Artefacts:** Coriolis forces deflected the PMMA flame.

Source: [ASGSR 2025 slides](https://ntrs.nasa.gov/api/citations/20250010653/downloads/ASGSR%202025-LUCI-Ferkul-Presentation-v2-20250010653.pdf). LUCI tested only the regime where bounding works: upward, in air, away from the limit. **It neither confirms nor refutes the worst-case hypothesis.** The results are conference slides only, with no DOI. The name ("Lunar-g" vs "Lunar Combustion Investigation") and the industrial partner (ZIN vs Voyager) differ between sources.

**FM2 (Flammability of Materials on the Moon; planned, outside PSI)** is a 14.4 L chamber planned to fly on a SpaceX lunar-lander (HLS) uncrewed demonstration flight.

- **Original plan (2024):** SIBAL in air and PMMA in 34% oxygen ([2024 poster](https://ntrs.nasa.gov/api/citations/20240008623/downloads/20240008623.pdf)).
- **Revised plan (2026):** four upward burns of one lander-relevant fabric at 8.2 psia, starting at 37%, 33%, 29% and 25% oxygen. This brackets an expected lunar limiting oxygen of **24-26%**, and the oxygen used up during each burn lets every test "scan" toward the limit ([LPSC 2026 slides](https://ntrs.nasa.gov/api/citations/20260001966/downloads/Ferkul-Lunar%20and%20Planetary%20Science%20Conf%202026%20v2.pdf)).
- **Expected impact:** FM2 is expected to lead to an amended NASA-STD-6001B Test 1 procedure ([LPSC 2026 paper](https://ntrs.nasa.gov/api/citations/20260000646/downloads/Ferkul-Lunar%20and%20Planetary%20Science%20Conference%202026.pdf)).
- **Status:** the "late 2026" launch date comes from March and April 2026 sources. **No evidence was found that FM2 has flown, slipped or been cancelled as of November 2026.** The "CP-21" mission designation comes from a single student poster.

### A defensible bounding rule

The bounding variable that works is **flow speed at the flame, not gravity level**. NASA's scaling puts lunar buoyant flow at roughly **10-40 cm/s** for small flames ([NTRS 20210020516](https://ntrs.nasa.gov/api/citations/20210020516/downloads/Fire%20on%20the%20Moon-Overview%20charts-v1.pdf)). That lies inside the low-speed forced-flow range (about 1-30 cm/s) already explored in microgravity by BASS-II, Saffire and FLARE.

JAXA makes the same argument from the other side. Buoyant flow at 1 g is never below about 30 cm/s, so tests on Earth cannot reach the low-flow regime ([JAXA FLARE](https://humans-in-space.jaxa.jp/en/biz-lab/experiment/theme/detail/000807.html)). FLARE is JAXA's experiment linking 1 g and microgravity oxygen limits, with FLARE-2 and FLARE-3 planned for lunar gravity ([JAXA leaflet 2026](https://humans-in-space.jaxa.jp/2026/07/Leaflet_CombustionExperimentInMicrogravity.pdf)).

A transparent dashboard rule follows. For a given material and atmosphere, estimate the partial-gravity oxygen limit as **no higher than the lower of the 1 g limit and the lowest microgravity limit over the tested flow range**. Then subtract a margin (BASS-II suggests at least 2.4 percentage points) and flag "non-monotonic risk" for downward spread or near-limit atmospheres. This rule is the researchers' synthesis, not a NASA method, and the product should say so.

### Exploration atmospheres

The challenge frames exploration atmospheres as "30%+ oxygen at 10.2 psi or less". That matches the historic Test 1 condition of **30% oxygen at 10.2 psia** ([LPSC 2026 slides](https://ntrs.nasa.gov/api/citations/20260001966/downloads/Ferkul-Lunar%20and%20Planetary%20Science%20Conf%202026%20v2.pdf)).

Current NASA planning goes further:

- **8.2 psia / 34% oxygen** was recommended by the Exploration Atmospheres Working Group as a compromise between fire risk, low-oxygen stress (hypoxia), decompression sickness and pre-spacewalk oxygen pre-breathing time ([Garbino et al. 2024](https://ntrs.nasa.gov/api/citations/20240005151/downloads/2024_05_06_Garbino_EA_final.pdf)).
- **33.7% oxygen** was set in a 2021 memo, with materials **certified at 37%** ([ICES-2026-301](https://ntrs.nasa.gov/api/citations/20260003042/downloads/301-ICES_Paper_2026-FR-Textiles_Final_04-13-2026.pdf)).
- **Apollo-style 100% oxygen cabins** were judged an unacceptable fire risk for Artemis ([NTRS 20220011152](https://ntrs.nasa.gov/api/citations/20220011152/downloads/Exploration%20Atmosphers%20OAF%2020220805.pdf)).

**The suit condition (100% oxygen at 4.3 psi) is only partly sourced.** Chamber studies used 4.3 psia to simulate spacewalks, but no programme document for the suit, HLS lander or pressurized rover atmosphere was retrieved, and in 2022 those parameters were described as not finalised.

The flame-relevant number is oxygen *fraction*. The partial pressures (simple arithmetic) are: 8.2 psia × 34% gives 19.2 kPa of oxygen, slightly below sea-level air's 21.3 kPa, yet the 34% fraction is 62% higher than air's. In short, a normoxic habitat is "Earth-like to lungs, oxygen-enriched to flames".

Material data at 10.2 psia and 1 g show who loses margin in that atmosphere ([Hirsch et al., NTRS 20070018178](https://ntrs.nasa.gov/api/citations/20070018178/downloads/20070018178.pdf)):

- **At or near the limit:** single-layer Nomex fails below 30% oxygen. P1700 polysulfone (limit 31.7%), Kydex (34.4%) and Solimide foam (35.3%) sit right at the edge.
- **With margin:** Ultem (45.2%), glass-filled PEEK (46.8%) and Zotek foam (46.2%) keep margin.

This gives a ready-made "what fails at 34%?" view, provided it carries the 1 g / 10.2 psia caveat.

## Turning experiments into controls: detect, suppress, clean up, prevent

NASA's 2013 Spacecraft Fire Safety Systems Maturation Team listed seven technology gaps ([Ruff & Urban, ICES 2016](https://ntrs.nasa.gov/api/citations/20170000230/downloads/20170000230.pdf)):

1. low- and partial-gravity material flammability;
2. fire detection;
3. suppression that is compatible with life support (ECLS-compatible);
4. an emergency crew mask;
5. post-fire monitoring;
6. post-fire cleanup;
7. fire-scenario modelling.

A 2020 plan added the exploration drivers: higher oxygen, partial gravity, dust, dormant vehicles and long missions ([Ruff & Dietrich, ICES 2020](https://ttu-ir.tdl.org/items/8ffcb981-49d1-450f-8c93-1988f29d6667)). No 2024-2026 official roadmap text was retrieved, so nothing here should be cited as "the 2026 roadmap".

**Detection.** ISS detectors sit in the air-return vents, because smoke does not rise without buoyancy ([Fortenberry et al.](https://ntrs.nasa.gov/api/citations/20210022143/downloads/Fire%20detection%20white%20paper%20final%20211031.pdf)).

- **False alarms:** the ISS logged **at least 20 automated fire responses in six years, all false**. Each one shuts down oxygen generators abruptly, and crews sometimes inhibit detectors during dusty work ([ICES-2025-126](https://ntrs.nasa.gov/api/citations/20250003954/downloads/ICES-2025-126_Final_Rev%20A.pdf)).
- **Missed smoke:** SAME showed the ISS detector misses wire-insulation smoke, and Saffire showed alarms lagging behind the toxic gas.
- **Recommended direction:** networked multi-parameter sensing that adds CO, discriminates smoke from lunar dust, and uses machine learning to identify the source ([Fortenberry et al.](https://ntrs.nasa.gov/api/citations/20210022143/downloads/Fire%20detection%20white%20paper%20final%20211031.pdf)).
- **Handheld monitoring:** the Anomaly Gas Analyzer is replacing the handheld combustion-products analyser ([Tobias & McMillan 2023](https://ntrs.nasa.gov/api/citations/20220019247/downloads/Emergency%20Ops%20History%20for%20SpaceOps%20Conference%202023.pdf)). Its deployment status as of November 2026 is unverified.

**Suppression.**

- **Current equipment:** the US segment uses CO2 extinguishers (about 2.7 kg), which work by displacing oxygen and require a supplied-oxygen mask. The Russian segment uses water-foam units. Fine-water-mist extinguishers were added, with the last of nine units arriving in 2016 ([Tobias & McMillan 2023](https://ntrs.nasa.gov/api/citations/20220019247/downloads/Emergency%20Ops%20History%20for%20SpaceOps%20Conference%202023.pdf); [NASA Spinoff 2020](https://spinoff.nasa.gov/node/11065)).
- **Batteries:** water mist is the agent for lithium-ion battery fires, where displacing oxygen is not enough.
- **Agent quantity depends on flow:** aircraft tests found the inert-agent concentration needed rose with flow up to 10 cm/s ([Ruff, Hicks, Pettegrew 2004](https://ntrs.nasa.gov/citations/20040161262)).
- **The case for water in small cabins:** FLEX's LOI data show how far oxygen would have to be diluted, which is impractical in a crewed cabin. CO2's drawbacks grow as cabin volume shrinks (Orion, landers, rovers), which supports water-based agents there.
- **Unverified:** whether the Orion water-spray extinguisher or Saffire-VII/VIII have flown.

**Response and cleanup.** An automatic alarm switches off fans, oxygen generation and rack power. Crews then mask up, probe panels through fire ports with the gas analyser, and use an extinguisher only if the fire persists ([Tobias & McMillan 2023](https://ntrs.nasa.gov/api/citations/20220019247/downloads/Emergency%20Ops%20History%20for%20SpaceOps%20Conference%202023.pdf)). The ISS post-fire cleanup kit is **legacy Shuttle hardware with limited stock that has never been formally deployed** ([ICES-2025-126](https://ntrs.nasa.gov/api/citations/20250003954/downloads/ICES-2025-126_Final_Rev%20A.pdf)). Saffire-IV to VI flew a prototype Orion "smoke eater" filter and a CO2 scrubber; their removal rates were not retrieved.

**Prevention.** NASA-STD-6001 Test 1 is a 1 g upward-burn, pass/fail test at the worst-case atmosphere. A burn longer than 15.2 cm, or burning drips, is a fail. The test is valid only at the atmosphere tested ([Olson, Beeson, Fernandez-Pello, ICES-2014-179](https://ntrs.nasa.gov/api/citations/20150004099/downloads/20150004099.pdf)). The standard itself was not opened, so the exact pass/fail wording is second-hand. Proposed complements:

- limit-based indices: the upward limiting oxygen index (ULOI) and maximum oxygen concentration (MOC);
- a pressure-based limit at near-normal oxygen partial pressure (NULP), with a microgravity margin of about 10 kPa;
- extrapolating 1 g stagnation-flow tests to zero stretch ([Marcum, Olson, Ferkul](https://ttu-ir.tdl.org/items/42f57c92-9547-46b8-8e20-65586173babc)).

These proposals reward investigations that report a **limit** (oxygen, flow or pressure at extinction) rather than only a spread rate. That is a natural scoring axis for the dashboard, on which BASS-II, BRE and Saffire-IV to VI score highest.

The research team's own mapping from PSI investigations to controls is:

| PSI investigations                   | Control it informs                                                     |
| ------------------------------------ | ---------------------------------------------------------------------- |
| BASS, BASS-II, PSI-62                | Material acceptance margins; ventilation-shutoff rule; Test 1 derating |
| Saffire-I/II/III (IV-VI outside PSI) | "Design fire" size for extinguishers, relief valves and cleanup        |
| ACME BRE                             | Materials screening across oxygen levels                               |
| SAME, SAME-R, DAFT, PSI-115          | Detector type, thresholds, dust rejection, reference aerosols          |
| FLEX, FLEX-2                         | Inert-agent effectiveness and LOI; case for water-based agents         |
| CFI, CFI-G, PSI-117, PSI-142         | "Flame-out is not all-clear": post-suppression gas monitoring          |
| E-FIELD Flames                       | Qualitative body-force analogue only                                   |

The white space with little or no PSI coverage is itself worth showing: masks, cleanup hardware, lithium-ion battery fires, lunar dust, partial gravity and dormant vehicles.

## Incidents that keep repeating the same three ingredients

Every well-documented crewed-cabin fire combines three things: an electrical or oxygen-system ignition source, an oxygen-enriched or poorly understood atmosphere, and underestimated materials.

**Apollo 1** (27 January 1967, a ground test on the launch pad) had its cabin pressurised with **100% oxygen**. No single ignition source was proven, but there was evidence of arcing near the environmental control wiring. The hatch could not be opened against the rising internal pressure. **The crew died of carbon monoxide and toxic-gas asphyxia; their burns were judged likely survivable** ([NASA SMA, Apollo 1](https://sma.nasa.gov/sma-disciplines/accllp/apollo-1)). The fixes were a hatch that opens in about three seconds, controls on combustible materials, and fire-resistant suits. The often-quoted **16.7 psi** cabin pressure is **unverified** in these notes.

**Apollo 13** (April 1970) traces back to a 1965 change that raised the tank heater voltage from 28 to 65 V without upgrading the thermostatic switches. The heaters stayed on for about eight hours during a pad test, reached roughly 1,000 °F and degraded the Teflon wire insulation inside an oxygen tank ([NASA SMA, Apollo 13](https://sma.nasa.gov/sma-disciplines/accllp/apollo-13)). That the insulation itself burned inside the tank is the standard review-board account, but it was **not explicit** in the page that was retrieved.

**Mir** (24 February 1997): a solid-fuel oxygen generator canister, of a type used more than 2,500 times without incident, ignited with six people aboard.

- The flame was about three feet long, threw sparks and molten metal, and blocked the path to one of the two Soyuz escape vehicles.
- The crew used three foam extinguishers, and life support needed hours to clear the smoke.
- The root cause was most likely a fragment of latex glove contaminating the canister.

Source: [NASA History](https://www.nasa.gov/history/25-years-ago-fire-aboard-space-station-mir/).

Other events follow the same pattern:

- **Ground chamber fires:** a Soviet altitude-chamber fire in 1961 (the Bondarenko case; details beyond NASA's one-line entry come from Wikipedia) and a 1962 US Navy fire in 100% oxygen at 5 psi ([NASA SMA Significant Incidents](https://sma.nasa.gov/SignificantIncidents/assets/2024/Significant_Incidents_Report-Spring2024.pdf)).
- **Shuttle:** five overheating events, about one per 1,600 mission hours, all involving odour or smoke and none triggering an alarm ([Friedman, NASA TM-106430](https://ntrs.nasa.gov/api/citations/19940022933/downloads/19940022933.pdf)).
- **ISS:** the 2006 Elektron oxygen-generator overheating event ([Spaceflight Now](https://spaceflightnow.com/station/exp13/060918elektron.html)).
- **Unverified:** the Salyut and 1994 Mir fire markers on NASA's incident chart have no descriptions, and the widely repeated details about them are unverified.

The lesson for the dashboard is that crews have been harmed by **toxic gas and smoke more than by heat**. That is exactly what Saffire measured, and it argues for gas-plus-particle detection.

## Earth spinoffs are mostly engineering, not combustion science

The documented spinoffs mirror the spacecraft controls, but most come from spacecraft engineering rather than PSI-type experiments:

- **Breathing apparatus:** a lightweight firefighter air system weighing 20 lb with 30 minutes of air, co-developed by NASA's Johnson Space Center (Spinoff 1976) ([NASA Spinoff](https://spinoff.nasa.gov/node/9582)).
- **Fire detection:** a Shuttle-derived incipient fire detector that tells combustion particles from dust (Spinoff 1978) ([NASA Spinoff](https://spinoff.nasa.gov/node/9407)).
- **Protective clothing:** PBI fabric, developed with Celanese after Apollo 1, introduced to the US fire service in 1978 and specified by the New York City Fire Department in 1994 ([NASA Spinoff 2008](https://spinoff.nasa.gov/node/10564)). Project FIRES (1982) applied Apollo-derived materials to firefighter gear ([NASA Spinoff](https://spinoff.nasa.gov/node/9918)).

Only **water mist** links directly to a microgravity combustion experiment. The STS-107 Water Mist test (2003) aimed at replacing halon extinguishers, in a market the release put at $2 billion a year ([NASA/EurekAlert](https://www.eurekalert.org/news-releases/607515)). The ISS mist extinguisher's zero-leak valve later reached industrial and military markets ([NASA Spinoff 2020](https://spinoff.nasa.gov/node/11065)). No evidence was retrieved that the STS-107 flight data themselves produced a commercial product; Columbia was lost on that mission.

Benefits from cool-flame and soot research for cleaner engines (for example HCCI engines) are stated **conditionally** by the sources ([UC San Diego 2014](https://today.ucsd.edu/story/researchers_discover_cool_burning_flames_in_space_that_could_lead_to_better)). SAME lists submarine smoke detection as a relevant Earth use ([NASA SAME summary](https://www.nasa.gov/wp-content/uploads/2025/07/smoke-aerosol-measurement-experiment-same.pdf)). The dashboard should label these "engineering spinoff" and "potential combustion-science benefit", respectively. The commonly told story of a NASA-origin household smoke detector (Skylab/Honeywell) was **not confirmed**.

## Building the dashboard: data pipeline, AI's role and judging

### Getting the data

PSI is NASA's repository for reduced-gravity physical-science data.

- **Size:** over 100 investigation datasets, about 30 TB, by July 2025.
- **Platform:** moved to AWS in 2024, with **DOIs for every dataset** ([PSI Updates](https://science.data.nasa.gov/features-events/physical-sciences-informatics-updates)).
- **Website:** shown alongside the biology repository OSDR on one NASA data page since September 2025 ([NASA](https://science.nasa.gov/science-research/biological-physical-sciences/osdr-and-psi-unveil-new-consolidated-website/)), but it keeps its own `PSI-<n>` identifiers.
- **Record contents:** objectives, approach, hypothesis, an experiment table, hardware, publications, data files split into reduced-gravity and Earth-gravity folders, and a "Cite this Investigation" control ([PSI Database Guide](https://science.nasa.gov/wp-content/uploads/2024/11/psi-database-guide.pdf)).

**No documented public API exists.** NASA's OSDR API covers biological data only ([OSDR API](https://www.nasa.gov/osdr-api)). The workable path is the undocumented JSON services the PSI site itself calls, which the team found under `psi.nasa.gov/geode-py/ws/...` (search, record and table-CSV endpoints; team note, not verified).

Because the endpoints are undocumented and the raw data are huge (team figures: FLEX 924 GB, CFI-G 2,086 GB), the sensible design is:

1. fetch the metadata and table CSVs once, sequentially with a delay;
2. commit the snapshot with its retrieval date;
3. have the deployed app read only the snapshot.

NASA mission data are **CC0 by default**, with citation encouraged ([NASA Science Data License](https://science.data.nasa.gov/about/license)).

For enrichment, NTRS (NASA's technical reports server) has a documented, keyless API at **500 requests per 15 minutes** with full-text PDF links ([NTRS OpenAPI docs](https://sti.nasa.gov/docs/20221122_OpenAPI_Documentation.pdf)). Crossref serves DOI metadata at 5-10 requests per second ([Crossref](https://crossref.org/blog/announcing-changes-to-rest-api-rate-limits/)). OpenAlex now needs an API key, although single-DOI lookups are free; this comes from secondary reporting ([CASRAI](https://casrai.org/news/openalex-api-keys-mandatory-usage-based-pricing-2026)).

### Where AI fits

With about 24 records and a team-estimated ~1,500 table rows, **numbers should come from deterministic parsing**: oxygen as percent or mole fraction, pressure in mmHg, bar or atm, multi-value cells, and typos such as BRE's "3400%". Keep the raw cell next to every normalised value. The team's draft script already does this.

The language model should do two bounded jobs:

- **Schema extraction at build time:** fill fields such as fuel class, geometry, what was varied, sensors, key finding and fire-safety pillar, each with a verbatim evidence quote. Automatically reject any value whose quote is not found in the source text.
- **Question answering over the small corpus:** cite `PSI-<n>` and the DOI, and refuse when nothing relevant is retrieved.

Comparison should be field-by-field (a structured matrix) rather than by embedding similarity, which is hard to explain. Ranking should use a **transparent additive score with adjustable weights**, for example:

- realism of the material (solid spacecraft materials above gas jets);
- overlap of tested oxygen and pressure with a user-chosen habitat preset (8.2 psia/34%, 8.2/37%, 10.2/30%);
- whether the investigation reports a limit;
- richness of the data.

Validate honestly: hand-label all 24 records for 6-8 fields, report precision and recall, and score 15-20 known-answer questions with the Ragas faithfulness metric (the share of answer statements supported by the retrieved text) ([Ragas, arXiv 2309.15217](https://arxiv.org/abs/2309.15217)). A light schema modelled on ChemKED, an open format for combustion experiments (investigation → test → outcome → diagnostics → provenance), is enough ([ChemKED, arXiv 1706.01987](https://arxiv.org/abs/1706.01987)).

### Judging

Prior art points to one focused insight rather than a library with a chatbot. The 2025 Best Use of Science winner, SpaceGenes+, centred on a single combined-stressor finding shown in a dashboard ([NASA 2025 winners](https://www.nasa.gov/learning-resources/stem-engagement-at-nasa/nasa-announces-2025-international-space-apps-challenge-global-winners/)). The Galactic Impact winner computed a risk index from public data. No existing AI tool over PSI combustion data was found, which is "not found in searches", not proof that none exists.

**The judging criteria are in conflict.** The fetched Judging & Awards Guide lists Influence, Creativity, Validity, Relevance and Presentation, with 2024 dates and no AI rules ([Judging & Awards Guide](https://www.spaceappschallenge.org/resources/judging-awards-guide)). The team's 13 Nov 2026 notes record "Impact", 2026 dates and AI-disclosure rules. Re-check the live guide before writing the submission.

## Verification ledger: what not to state as fact

| Item | Status | What to do |
|---|---|---|
| All 24 `PSI-<n>` IDs, row counts, raw sizes, CC0 licence, `geode-py` endpoints | Team notes only; not re-verified | Re-pull from PSI JSON; take DOIs from records |
| Challenge wording (85% O2, E-FIELD "mimicked partial gravity", 30%+ / 10.2 psi, suits 100% / 4.3 psi) | Team brief only; page blocked | Quote the brief, mark as challenge framing |
| CFI-G "85% oxygen" | Verified, but only injected oxidizer in inverse flames; ambient max 40% | Label accordingly |
| E-FIELD as partial-gravity analogue | No voltage-to-g calibration; no primary NASA source for "mimicked" | Tag "qualitative body-force analogue" |
| Negative oxygen margin, PMMA rod | Conflict: 2.4% (BASS-II) vs 1.4% (SoFIE overview) | Show both with sources |
| Saffire heat release | Conflict: "up to 10 kW" (2021 abstract) vs 1.5-3.2 kW (2024 tables) | Prefer 2024 tables, show discrepancy |
| Saffire-IV/V oxygen, pressure, duct height | Conflict between ICES and journal | Prefer journal; expose both |
| GEL sphere size | Conflict: 40 cm vs 4 cm | Use 4 cm (flight paper) |
| BASS-II flow range | Inconsistent in same poster (40 vs 55 cm/s) | Quote as range with caveat |
| FLEX test count | >300 vs 284 (first data report) | Use PSI record |
| Xenon as poor suppressant | Modelling result; authors not seen; on-orbit xenon tests unconfirmed | Present as modelled |
| "Microgravity smoke is larger" | True only at low/no flow | State the flow condition |
| FM2 launch / status | "Late 2026" planning date; no confirmation | Mark "planned, status unknown" |
| LUCI | Conference slides only; name and partner differ by source | Mark "preliminary" |
| SoFIE, Saffire-IV to VI, Confined Combustion, FLARE, LUCI, FM2, SSCE | Outside PSI | "External context" cards |
| Apollo 1 at 16.7 psi; Apollo 13 Teflon burning in tank; Salyut / Mir 1994 details | Unverified | Omit or flag |
| SPICE/SLICE investigators and MSG hardware; FLEX-ICE-GA details | Recall or team note only | Verify before use |
| Suit / HLS / rover atmosphere specs | No programme document retrieved | Treat as challenge framing |
| Judging criteria (Influence vs Impact), AI rules | Conflict between fetched guide and team notes | Re-check live guide |
| Anomaly Gas Analyzer deployment; Orion extinguisher; Saffire-VII/VIII | Unverified status | Omit status claims |
| NASA-origin household smoke detector; NBS role in air tanks | Not confirmed | Do not claim |

## Conclusion

The research changes what the dashboard should be for. It should not mainly summarise experiments that already have abstracts. It should **show where PSI's tested conditions stop and the exploration envelope begins**. The gap has three dimensions:

- **Oxygen:** solid fuels in PSI reach about 22%, against 34-37% planned.
- **Gravity:** PSI has only 0 g and 1 g; LUCI and FM2 are outside it and early.
- **Scale:** only Saffire is cabin-scale, and its exploration-atmosphere runs are outside PSI.

The physics explains why each gap matters. Flammability limits follow flow speed rather than gravity and can be worst at intermediate g. Toxic gases, not heat, set the survival margin. The most visually convincing proof of a fire being out, a vanished flame, is unreliable for liquid fuels.

The deliverable that would most help NASA's stated aim of making PSI datasets comparable is a provenance-first system. Every number traces to a PSI cell or a cited paper, every conflict is shown rather than averaged away, and every estimate for the Moon or Mars carries its bounding rule and uncertainty. That honesty is also the team's best route to the Validity criterion, because it is what competing "library plus chatbot" entries typically lack.
