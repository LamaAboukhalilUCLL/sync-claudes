# Project page final text

**Added:** Sun 15 Nov 2026, 21:10, Claude Code for Lama. Drafts for Lama to edit before pasting. The summary keeps Lama's central insight (D12) word for word. Every number is checked against the live site (`main`, `09109b2`). Link lists: [[Project page fields (draft)]] sections 7 and 8.

## Project name
Flame in Freefall: Moon Base fire data coverage

## Summary
Flame in Freefall is an interactive dashboard over all 24 combustion investigations in NASA's Physical Sciences Informatics (PSI) repository. It shows how much of NASA's microgravity fire data applies to the new Moon Base habitats and their higher-oxygen air, and where that data stops, so engineers planning those habitats can see which fire questions are already answered and which are not.

A Moon Base is expected to hold 30 % oxygen or more at 10.2 psi or less, and more oxygen makes materials burn more easily. The dashboard summarizes, ranks and interprets every investigation against that air, or any air the user chooses. Its main finding: of 659 tests that state both oxygen and pressure, 20 were run in Moon Base air, all gas flames, and none of the 129 solid-material tests that state their oxygen reaches 30 %.

SI reads NASA's records into plain summaries and question labels, a small language model in the browser finds the sentences in NASA's records and listed papers that answer any question, and statistics on NASA's droplet tests show which next test would teach the most. Every number is counted from NASA's files, and every quotation is checked by program.

## Project details

**What it does**
The dashboard reads all 24 combustion investigations in NASA's PSI repository and every row of their 22 experimental tables (1,982 rows), and checks them against the air planned for the Moon Base: 30 % oxygen or more, at 10.2 psi or less. The user can switch to another atmosphere (the cabin atmospheres named in NASA's records, a spacesuit, or their own) and every count is recalculated. The Overview states the problem and shows on a route map where NASA's fire tests were run: 5 investigations on Earth, 19 in low Earth orbit, none at the Moon Base. Check your habitat lets the user choose the air and the material of four parts of a habitat, and marks each part that fails NASA's flame test on Earth at that oxygen level. Explore shows every test against the chosen air, finds any material or test, and opens NASA's table at the exact row. Analysis models NASA's droplet tests. Ranking orders the 24 investigations against five conditions and compares them side by side. Ask finds the sentences in NASA's records and listed papers that answer a question. Open questions sets out six fire-safety questions for a Moon Base, with NASA's evidence and what is missing.

**What we found**
Of 659 tests that state both oxygen and pressure, 20 were run in Moon Base air, all gas flames in one investigation (ACME CFI-G). Another 17 droplet tests in FLEX miss the pressure limit narrowly, at 10.33 to 10.5 psi. All 129 solid-material tests that state their oxygen ran between 13.6 and 22.2 %, so none reaches 30 %. None of the 24 records mentions the Moon, Mars or partial gravity, and no investigation meets all five conditions we rank by (the closest meet 3). On Earth, NASA's White Sands Test Facility did test materials at Moon Base pressure (10.17 psi): at 30 % oxygen, 7 of 26 samples did not reliably put themselves out, and none of the materials is confirmed in weightlessness. Of six fire-safety questions for a Moon Base, 3 are partly answered and 3 are open.

**How SI is used, and how it is kept honest**
Claude (Anthropic) wrote the plain-language summaries, extracted what each investigation burned, varied and measured, and read all 925 passages of NASA's records and the papers they list to label the fire questions each one addresses. Every summary and label carries a quotation that a program checks word for word, and the build rejects any hand-typed number. The labels show, for example, that only 1 of the 925 passages is about fire in Moon gravity. A small open language model (snowflake-arctic-embed-s) runs in the user's browser: on the Ask page it finds the NASA sentences that answer a question, and on Explore it places the 24 investigations on a map by meaning. It writes no text. On 20 held-out test questions (drafted with AI), it finds the right investigation first in 13. A statistical model of NASA's 274 FLEX droplet tests, refitted independently by a second program, shows that heptane burns about 43 % faster at 30 % oxygen than at 21 %. It also ranks the conditions FLEX's hardware covered by how much one more test there would teach: the best one narrows the model's range by only 6.0 %, so the real gap is solid materials.

**Benefits and intended impact**
Engineers planning Moon habitats can see in minutes which fire questions NASA's data already answers for their air, which it does not, and which NASA work to read first. Researchers and students get the 24 investigations in plain words, side by side, with every number traceable to a NASA table row and DOI. The open questions point to the next experiments: solid materials burned in weightlessness at 30 % oxygen, and any fire test in Moon gravity.

**Tools, languages and software**
Plain HTML, CSS and JavaScript with hand-made SVG charts, published with GitHub Pages. Data pipeline in Python 3, standard library only. Node.js for the search index and the checks. Transformers.js 4.3.2 and ONNX Runtime Web run the language model in the browser. Git and GitHub for the code, Obsidian for team notes. Code and data: https://github.com/LamaAboukhalilUCLL/Data-Beyond-Space

**How it is creative**
Instead of a search box over NASA's files, the dashboard asks one question of all of them: how close did each test come to the air of a Moon Base? It turns the answer into tools an engineer can use: a habitat check, an atmosphere chooser, a ranking, a map of what NASA has and has not written, and the next test that would teach the most.

**Factors we considered**
Accuracy first: the site shows coverage and gaps, not predictions. NASA's files are stored byte for byte with checksums, headline numbers are counted twice by separate code, and cells NASA wrote as text are shown as written, never estimated. Access: free, public, no login, no server and no API key; the language model runs on the user's own computer and nothing leaves it. Cost and energy: static hosting and a small model in the browser instead of a large one on a server. Licences: NASA public-domain data and photographs, open-licence fonts and models, all listed below. Limits stated on the site: the Earth tests are in normal gravity, and AI-made texts, labels and test questions are marked as such.
