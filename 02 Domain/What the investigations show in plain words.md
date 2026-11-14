# What the investigations show, in plain words

**Added:** Sat 14 Nov 2026, 23:00 · **By:** Claude Code (VS Code), asked for by Lama. Written for a reader with no combustion background. Facts only; it proposes no insight.

**Source:** the 24 records and 22 tables in `app/raw/`. One caution: most PSI records describe what an experiment **set out to do** and what its authors **expected**. Only a few state a result. Each line below says which it is.

## Four ideas you need first
1. **Fire needs three things:** fuel, oxygen and heat. Remove one and it stops.
2. **On Earth, hot air rises.** That pulls fresh air into a flame from below, which feeds it and gives it its pointed shape. This rising is called buoyancy.
3. **In space nothing rises.** A flame becomes a slow, round, blue ball. It only gets fresh oxygen if air is blown at it, for example by the cabin fans. So airflow speed matters a great deal in space.
4. **More oxygen in the air makes things burn more easily.** Earth air is 21 % oxygen. Moon habitats are planned at 30 % or more.

"Microgravity" means the near-weightlessness on the space station. "1 g" means normal Earth gravity.

## Group 1: solid materials (things a cabin is made of)
| Investigation | What they did | What the record says |
|---|---|---|
| BASS and BASS-II (251 tests) | Burned small pieces of plastic, fabric and wax in a tiny wind tunnel on the station, changing fan speed and, in BASS-II, lowering the oxygen | **Expected:** with enough airflow, materials burn "as well if not better" in space than on Earth. **Stated:** NASA picks spacecraft materials with an Earth test that does not consider low gravity. BASS-II oxygen: 13.6 to 22.2 % |
| Saffire-I, II, III (large fires in an empty cargo ship) | Burned fabric sheets up to about a metre long, and in Saffire-II nine smaller samples | **Aim:** see how fast a big fire grows in space and compare with the Earth test. **Result in the Saffire-II table:** at about 22 % oxygen, each sample burned as much or more on Earth than in space. Thin silicone burned fully on Earth and not at all in space |
| BRE (a gas burner that imitates a burning solid) | Fed gas through a plate so it burns like plastic would, at 21 to 40 % oxygen | **Result stated:** flames kept burning with **no airflow at all** in higher-oxygen air, while at 21 % they went out by themselves quickly. Turning off ventilation is a standard step for putting out a spacecraft fire. Marked preliminary |
| Flame-spread modelling (ground study using BASS data) | Computer model of flame spreading along a solid | **Aim:** a tool to predict whether a new material will burn. Mentions a "Goldilocks" zone: a range of airflow that is just right for burning, with no burning when flow is too slow or too fast |

## Group 2: smoke and detecting a fire
| Investigation | What they did | What the record says |
|---|---|---|
| SAME and SAME-R (117 tests) | Heated spacecraft materials until they smoked and measured the smoke particles | **Expected:** without rising air, smoke particles grow **larger** than on Earth. Smoke detectors are tuned to particle size, so Earth-tuned detectors may respond differently |
| DAFT (2 sessions) | Checked that a particle counter works in weightlessness | A preparation step for SAME |
| Smoke modelling (ground study using SAME data) | Computer model of how smoke forms | **Aim:** explain why space smoke differs from Earth smoke |

## Group 3: liquid fuel droplets and putting flames out
| Investigation | What they did | What the record says |
|---|---|---|
| FLEX (274 tests) | Burned single fuel droplets in different mixes of oxygen, nitrogen, carbon dioxide and helium, 12 to 34 % oxygen | **Aim:** map when a flame goes out, and how well extinguishing gases such as CO2 work in space |
| FLEX-2, CFI (95 rows) | More fuels and pressures | Mostly about engines and fuels on Earth |
| Two ground studies using FLEX data | Computer work on "cool flames" | **Result stated:** a flame can drop to a much lower temperature and keep burning almost invisibly instead of going out. The CFI-G record says these cool flames "were discovered in 2012" |

## Group 4: gas flames (basic flame science)
ACME Flame Design, CFI-G, s-Flame, CLD Flame, E-FIELD Flames, SLICE, SPICE and one ground study. Together they are over 1,200 table rows, the largest part of the data.

What their own records say they are for: cleaner engines, power plants, less soot and pollution on Earth, and better computer models of flames. The E-FIELD record says outright that it "is not being conducted to serve any space applications". SPICE and SLICE mention safer spacecraft only in general terms.

## What stands out when you put all 24 side by side
1. **Only about half are about fire safety by their own description.** Solids, smoke and FLEX are. The gas-flame group, the biggest by row count, is mainly engine and pollution science.
2. **The safety experiments on real solid materials were done at normal oxygen or below** (13.6 to 22.2 %). Oxygen of 30 % or more appears only with gases and droplets. BASS and Saffire-III do not state their oxygen at all.
3. **NASA's own records question the Earth test.** BASS, BASS-II and all three Saffire records say the Earth-gravity test used to approve materials may not show how they behave in space.
4. **The direct comparisons do not all point one way.** Near normal oxygen, Saffire-II shows less burning in space than on Earth. Near the lowest oxygen and slow airflow, BASS-II's authors report burning in space where an Earth flame would stop.
5. **Airflow cuts both ways.** Too little and a space flame starves; too much and it blows out; in between it burns. And in higher oxygen (BRE), a flame may not need airflow at all.
6. **Flames can hide.** Round, dim blue flames, and cool flames that are nearly invisible, are harder to notice than an Earth fire.
7. **Smoke is different in space,** which matters for detectors.
8. **Most records state aims and expectations, not results.** The results are in the publications, and we have abstracts for only 73 of 235.
9. **The tables do not line up with each other.** Oxygen is written as percent, as a fraction, as text or not at all. Only 10 of 24 investigations state it. Nobody can currently compare them without doing what we did by hand.
10. **No record mentions the Moon, Mars or partial gravity.** Everything is weightlessness or Earth.

See also: [[NASA stated fire safety needs]], [[Step 1 decision sheet]], [[Oxygen evidence (generated)]].
