# Project page fields (draft)

**Added:** Sun 15 Nov 2026, 13:40 · **By:** Victor, with Claude (Cowork) compiling from the vault and the repository. **Draft for Lama.** The summary, the description and the project name are hers to write (rule 5: the ideas are hers). Everything else here is compiled and checked, ready to paste.

**Updated:** Sun 15 Nov 2026, 18:30 (Use of SI: one conditional bullet for the Ask upgrade, Step 11b). Before that 17:10, to match the live site (`main`, `f841a17`: White Sands table, Check your habitat, droplet Analysis page). Numbers re-run with `build_dataset.py`, `build_external.py` and `validate.py` on that commit.

Fields follow the order of the Project tab ([[Notes about project guide]], Project Submission Guide). Character and word limits as the guide states them.

---

## 1. Project name
**Lama decides.** Working title in the [[Decision log]]: "Flame in Freefall: Moon Base fire data coverage". The site title is "Flame in Freefall: how far NASA's fire data reaches toward the Moon Base".

## 2. High-level project summary (50-200 words)
**Lama writes.** The guide asks three things: what did you develop, how does it address the challenge, why is it important.

### Numbers she can use (all checked)
Source: the build and `validate.py` run on `main` (`f841a17`), 15 Nov, 17:05. Each one is also on the site.

| Fact | Value | Where it comes from |
|---|---|---|
| Combustion investigations in PSI, all used | 24 | snapshot, `dataset.json` |
| Experimental tables read | 22 (from 20 investigations) | `dataset.json` |
| Table rows naming a fuel or material, all searchable | 1,990 | `dataset.json` (`entry_rows`; 1,982 before Lama's Step 10) |
| Tests stating ambient oxygen as a plain number | 876 | `validate.py` |
| ...of those at 30 % oxygen or more | 270: 246 gas flames, 24 droplets, **0 solid materials** | `validate.py`, `dataset.json` |
| Tests stating both oxygen and pressure | 659 | `validate.py` |
| ...inside Moon Base air (30 % or more, 10.2 psi or less) | **20**, all gas flames in one investigation (ACME CFI-G, PSI-159) | `validate.py` |
| ...narrowly missing the pressure limit (10.33 to 10.5 psi) | 17, all FLEX droplets (PSI-69) | `validate.py` (`rows_near_zone`) |
| Oxygen range of every solid-material test that states it | 13.6 to 22.2 % (129 tests, BASS-II) | `validate.py` |
| Investigations that state ambient oxygen / pressure in their table | 10 / 5 of 24 | `dataset.json` |
| Records that mention the Moon, Mars or partial gravity | 0 of 24 | `dataset.json` |
| Investigations meeting all five ranking conditions | 0; best is 3 of 5 (FLEX, ACME CFI-G) | `dataset.json` |
| Where the tests were run (route map) | Earth 5, low Earth orbit 19, Moon Base 0 | site overview |
| Publications PSI lists / unique DOIs / with an abstract | 352 / 235 / 73 | `dataset.json` |
| Passages the Ask page searches | 925 (311 from NASA records, 614 from papers) | [[2026-11-15 Step 7 matrix, ask the records, reading lists]] |
| Quotations checked word for word by program | 81 | `validate.py` |
| NASA White Sands Earth tests at Moon Base pressure (70.1 kPa, 10.17 psi), the one table not from PSI | 24 materials in 26 samples; at 30 % oxygen **7 fail** on Earth, 19 pass, **0 confirmed in space** | `earth_tests.json`, Habitat page ([[2026-11-15 Step 10 Earth tests from White Sands and fixes]]) |
| FLEX droplet tests in the Analysis page's model | 274 | [[2026-11-15 Step 9 droplet model on a branch]] |

Wording NASA itself uses, safe to quote:
- Moon Base and pressurized rovers, challenge statement word for word: "The intermediate oxygen concentration used on the Moon will likely be 30% or greater, with a corresponding pressure of 10.2 psi or less." and "that's more than a 40% increase in the oxygen concentration making materials much more flammable."
- Why the oxygen goes up: lower risk of decompression sickness, more frequent spacewalks ([[Challenge video]]).
- NASA confirming the gap the site shows, word for word (NASA Engineering and Safety Center, NASA/TM-20260003925, May 2026, https://ntrs.nasa.gov/citations/20260003925): "NASA has limited material flammability data at O2 concentration higher than 30%" and "Essentially all existing test data for flammability of flight materials are from 1-g testing". Fits the "why is it important" part of the summary or the description. Found by Victor's search, 15 Nov ([[References]]).

## 3. Link to project demo
**To do** once the demo exists (format still open: 30-second video or at most 7 slides). Public link, no login. A slide deck must show **team name, all member names and the challenge**:
- Team: Data Beyond Space
- Members: Lama Abou Khalil, Mikho Demetrashvili, Nguyễn Thị Thanh Vy, Mylene Aradani, Lina Belabed, Victor Suciu
- Challenge: Flame in Freefall: SI-Powered Fire Safety Insights from Microgravity Combustion Data

## 4. Link to final project
- Website: https://lamaaboukhalilucll.github.io/Data-Beyond-Space/ (live, checked 15 Nov 12:30)
- Repository (name it in the description): https://github.com/LamaAboukhalilUCLL/Data-Beyond-Space (public, checked 15 Nov 12:30)

Private window on a computer: checked by Victor (Chrome), fine. Phone: checked by Victor; the table pop-up bug he found is fixed and live ([[2026-11-15 Step 8d phone fix for the table pop-up (Victor)]]). Still open: Firefox.

## 5. Detailed project description
**Lama writes.** The guide's questions: what does it do and how does it work; what benefits; what do you hope to achieve; what tools, coding languages, hardware or software; how is it creative; what factors (energy, cost, accessibility) were considered.

### Ready-made: tools, languages, software
> Plain HTML, CSS and JavaScript (no framework), published with GitHub Pages from the repository's `docs/` folder. Data pipeline in Python 3 using only the standard library (`fetch_snapshot.py`, `fetch_papers.py`, `build_dataset.py`, `validate.py`). Node.js for two helper scripts (`check_recount.cjs`, `build_search.mjs`). In-browser search with the open model snowflake-arctic-embed-s (all-MiniLM-L6-v2 until Step 11c; pending Lama's decision) run by Transformers.js 4.3.2 and ONNX Runtime Web; no server, no API key, no data leaves the reader's computer. Code and notes kept in Git (GitHub); team notes in Obsidian. Since Step 9 to 11 also: `build_external.py` (reads the NASA White Sands table from the paper's text, with pypdf 7.1.0 used once to extract that text), `analyze_flex.py` and `check_model.cjs` (the droplet model on the Analysis page).

### Ready-made: how it stays honest (facts from the README, for the "how it works" part)
- A snapshot of NASA's files is stored byte for byte, with a SHA-256 checksum for each of the 47 files; `validate.py` re-checks them.
- One script builds every number on the site from that snapshot; nothing is typed by hand, and the build fails if a text contains a hand-typed number.
- Every quotation is checked word for word against the NASA record it is attributed to (81 quotations).
- Headline numbers are counted a second time by separate code (`validate.py`); the in-browser recount for other atmospheres is checked against the build (`check_recount.cjs`).
- Ambient oxygen and burner-flow oxygen are never mixed; cells NASA did not write as plain numbers are shown as written, never estimated.
- The site shows coverage and gaps; it does not predict fire behaviour on the Moon.

## 6. Use of SI
Not shown to the judges (data collection only), but required. The judges see the acknowledgements inside the project. Draft compiled from [[SI use log]]:

> **Yes.**
> - **Claude (Anthropic)**, through Claude Code and the Claude desktop app, was used to:
>   - research the challenge, NASA's PSI repository and NASA's published fire safety needs, and keep the team's notes;
>   - write the code: the data scripts and the website;
>   - write the plain-language summaries and the six-question board, and extract each investigation's attributes from NASA's record text. These texts are labelled AI-written on the site. A program checks every quotation word for word against NASA's records and forbids hand-typed numbers. A team member reviewed the summaries and the question board against the records and tables;
>   - draw the habitat schematic, the route map and the team logo as SVG code;
>   - remove the black sky from a NASA photograph of the space station with a script.
> - **ChatGPT (OpenAI)** produced one design mockup of the overview page, watermarked as AI-generated. The page layout follows it; the image is not on the site.
> - **snowflake-arctic-embed-s** (Snowflake; it replaced all-MiniLM-L6-v2 in Step 11c, pending Lama's decision), an open language model, runs in the reader's browser on the "Ask" page. It only matches a question to NASA's sentences and writes no text.
> - **Only if Lama merges `victor/ask-upgrade` (Step 11b):** Claude proposed six improvements to the Ask page and Claude Code built them: counted answers from NASA's tables, how far the evidence reaches into the chosen atmosphere, a notice when NASA has no Moon or Mars gravity data, a word list for everyday terms, related investigations by meaning, and a measured score (40 test questions). The word list and the test-question labels were drafted by Claude; say here whether a team member checked them. If the branch is dropped, delete this bullet.
>
> The project's idea, asking how much of NASA's fire data applies to the new Moon Base habitats, is the team's: Lama proposed it after reading NASA's Moon Base page. The photographs are real NASA images, not AI-generated.

**AI-drawn images: done.** The visible marks and the footer, Data page and README wording are merged and live (pull request #2, [[2026-11-15 Step 8b AI marks on drawings (Victor)]]). The background below is kept for the record.
- The rules say SI-generated images need a **visible watermark**. The habitat schematic, the route map and the logo were drawn by AI as SVG code.
- On the site, the habitat page only says "The drawing is a schematic, not a NASA design". The footer says "Code and plain-language summaries were written with AI assistance", which does not cover drawings or the extracted attributes.
- A small visible line under each drawing ("Drawn with AI assistance") and a footer that names drawings and extracted attributes would close this. Whether these count as "images" is debatable. A visible note costs little.

Also still open in [[SI use log]]: which tool, if any, wrote the two external briefs and the pasted plan (14 Nov row).

## 7. NASA data (link text and URL for each)
At least one NASA source is required for a Global Award.

**Data**
| Link text | URL |
|---|---|
| NASA Physical Sciences Informatics (PSI) Data Repository, Combustion Science | https://psi.nasa.gov/physci/repo/search?q=combustion |
| PSI-10: ACME/Flame Design | https://doi.org/10.60555/w4zy-bt45 |
| PSI-20: ACME BRE (Burning Rate Emulator) | https://doi.org/10.60555/vb93-3y72 |
| PSI-21: ACME CLD Flame | https://doi.org/10.60555/23e1-9950 |
| PSI-22: ACME E-FIELD Flames | https://doi.org/10.60555/se5a-8c73 |
| PSI-23: ACME s-Flame | https://doi.org/10.60555/k57n-p030 |
| PSI-25: BASS-II, Burning and Suppression of Solids - II | https://doi.org/10.60555/4qc4-de67 |
| PSI-26: BASS, Burning and Suppression of Solids | https://doi.org/10.60555/58h4-dy80 |
| PSI-39: CFI, Cool Flames Investigation | https://doi.org/10.60555/m6pj-a914 |
| PSI-47: DAFT / DAFT-2, Dust and Aerosol Measurement Feasibility Test | https://doi.org/10.60555/ztgj-d202 |
| PSI-60: Computational and Experimental Analysis of SPICE Data Sets | https://doi.org/10.60555/mzjm-yv57 |
| PSI-62: Concurrent Flame Spread Modeling ... Comparison to BASS Experiments | https://doi.org/10.60555/e9xp-ex83 |
| PSI-68: FLEX-2, Flame Extinguishment Experiment - 2 | https://doi.org/10.60555/byp8-h018 |
| PSI-69: FLEX, Flame Extinguishment Experiment | https://doi.org/10.60555/mbq8-0451 |
| PSI-98: SAFFIRE-I, Spacecraft Fire Safety Experiment-I | https://doi.org/10.60555/0t15-1z43 |
| PSI-99: SAFFIRE-II, Spacecraft Fire Experiment-II | https://doi.org/10.60555/2chp-m469 |
| PSI-100: SAFFIRE-III, Spacecraft Fire Experiment-III | https://doi.org/10.60555/040q-4h36 |
| PSI-101: SAME-R, Smoke Aerosol Measurement Experiment-Reflight | https://doi.org/10.60555/2np7-jv14 |
| PSI-102: SAME, Smoke and Aerosol Measurement Experiment | https://doi.org/10.60555/gd4k-8h62 |
| PSI-106: SLICE, Structure and Liftoff In Combustion Experiment | https://doi.org/10.60555/pm12-rg61 |
| PSI-107: SPICE, Smoke Point In Co-flow Experiment | https://doi.org/10.60555/9kbh-e962 |
| PSI-115: Smoke Aerosol Measurement Experiment Data for Modeling of Smoke Generation | https://doi.org/10.60555/q0v5-1v28 |
| PSI-117: External Thermo-Convective Perturbation on Cool Flame Dynamics (CFD) | https://doi.org/10.60555/gz0q-b577 |
| PSI-142: Cool Flame Transitions Using Counterflow Flames | https://doi.org/10.60555/80qf-vj95 |
| PSI-159: ACME CFI-G, Cool Flames Investigation with Gases | https://doi.org/10.60555/cyt1-kh64 |
| NASA White Sands Test Facility: Hirsch et al., Oxygen Concentration Flammability Thresholds of Selected Aerospace Materials Considered for the Constellation Program (2007) | https://ntrs.nasa.gov/citations/20070018178 |

All 24 DOIs were checked against the `doi` field of each record in `data/psi/raw/` (24 of 24 match). Clicking the DOI links is still to be tested.

**Other NASA resources**
| Link text | URL |
|---|---|
| NASA Space Apps 2026: Flame in Freefall (challenge statement; Moon Base atmosphere figures) | https://www.spaceappschallenge.org/2026/challenges/flame-in-freefall/ |
| NASA Space Apps: 2026 Challenge video, Flame in Freefall | https://www.youtube.com/watch?v=AVuEiKxOpc0 |
| NASA: Moon Base | https://www.nasa.gov/moonbase |
| G. A. Ruff, Spacecraft Fire Safety Needs for Exploration (NASA Glenn, 2020) | https://ntrs.nasa.gov/citations/20205007829 |
| Preliminary Results from the Saffire VI Experiment (NASA, 2024) | https://ntrs.nasa.gov/citations/20240002981 |
| Moon to Mars (M2M): Exploration Atmosphere (NASA, 2024) | https://ntrs.nasa.gov/citations/20240003211 |
| Combustion of Solids in Microgravity: Results from the BASS-II Experiment (NASA, 2014) | https://ntrs.nasa.gov/citations/20160000593 |
| Research Questions and Challenges for Improved Spacecraft Fire Detection (NASA, 2021) | https://ntrs.nasa.gov/citations/20210022143 |
| Material Flammability at Lunar and Martian Gravity (NASA, 2026) | https://ntrs.nasa.gov/citations/20260001966 |
| Flammability of Materials on the Moon (NASA, 2024) | https://ntrs.nasa.gov/citations/20240015307 |
| Fire-Resistant Textile Development (NASA, 2026) | https://ntrs.nasa.gov/citations/20260003042 |
| Impacts of Reduced Pressure Atmospheres on Environmental Control and Life Support Systems (ECLSS) Architectures (NASA Engineering and Safety Center, 2026) | https://ntrs.nasa.gov/citations/20260003925 |
| Solid Fuel Ignition Testing for Lunar Applications, Theory and Experimental Results (NASA Glenn and White Sands, ICES-2025-392) | https://ntrs.nasa.gov/citations/20250002114 |
| Photograph: Moon nearside, Lunar Reconnaissance Orbiter mosaic (NASA/GSFC/Arizona State University, public domain) | https://commons.wikimedia.org/wiki/File:Moon_nearside_LRO_5000.jpg |
| Photograph: The Earth seen from Apollo 17 (NASA, public domain) | https://commons.wikimedia.org/wiki/File:The_Earth_seen_from_Apollo_17.jpg |
| Photograph: ISS-56 International Space Station fly-around (NASA/Roscosmos, public domain) | https://commons.wikimedia.org/wiki/File:ISS-56_International_Space_Station_fly-around_(13).jpg |
| NASA Horizon Design System (colour values only; no insignia) | https://github.com/nasa/hds-core |

The NTRS reports above are the site's reading lists (links and titles only; no number is taken from them), except the White Sands paper, which is the one data source outside PSI (D25). The last two rows (2026 NESC report, ICES-2025-392) are on the site: `victor/reading-list-additions` was merged (pull request #5, `0397c6f`).

## 8. Space Agency Partner data and other references
Space Agency Partner data: **none used.**

| Link text | URL |
|---|---|
| OpenAlex (scholarly metadata, CC0): titles and abstracts of the papers PSI lists | https://openalex.org |
| snowflake-arctic-embed-s sentence-embedding model (Snowflake, Apache-2.0) | https://huggingface.co/Snowflake/snowflake-arctic-embed-s |
| all-MiniLM-L6-v2 sentence-embedding model (Apache-2.0), the earlier model, kept for comparison | https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2 |
| all-MiniLM-L6-v2, ONNX build (Xenova) | https://huggingface.co/Xenova/all-MiniLM-L6-v2 |
| Transformers.js 4.3.2 (Hugging Face, Apache-2.0) | https://github.com/huggingface/transformers.js |
| ONNX Runtime Web (Microsoft, MIT) | https://github.com/microsoft/onnxruntime |
| Barlow Condensed typeface (SIL OFL 1.1) | https://github.com/jpt/barlow |
| Public Sans typeface (SIL OFL 1.1) | https://github.com/uswds/public-sans |
| DM Mono typeface (SIL OFL 1.1) | https://github.com/googlefonts/dm-mono |
| Fontsource (font files) | https://fontsource.org |
| Wikimedia Commons (source pages of the three NASA photographs) | https://commons.wikimedia.org |
| Python 3 standard library | https://docs.python.org/3/library/ |
| pypdf 7.1.0 (BSD-3-Clause), used once to extract the text of the White Sands PDF | https://github.com/py-pdf/pypdf |
| Node.js | https://nodejs.org |
| GitHub Pages (hosting) | https://pages.github.com |
| Claude (Anthropic), AI assistant: research, code, texts, drawings (see Use of SI) | https://www.anthropic.com/claude |
| ChatGPT (OpenAI), AI design mockup, not on the site | https://chatgpt.com |

### Differences from [[References]] (on purpose)
- The STS-132 space station photo is left out: the site now uses the ISS-56 photo (`docs/img/CREDITS.md`).
- The Moon photo is described as used now (behind every page), not as "at the bottom of the overview".
- "Inter" is not listed: the site's fonts are Barlow Condensed, Public Sans and DM Mono (`docs/img/CREDITS.md`).
- Added: the original all-MiniLM-L6-v2 model page, Node.js, GitHub Pages, Wikimedia Commons, Claude and ChatGPT.

## 9. Before pressing "Submit for judging"
See [[Submission checklist]]. In short: all 6 members registered for the Universal Event and on the Members tab; both tick boxes; every link opened in a private window; demo within limits; first submission well before 23:59 CET (it can be resubmitted until then).
