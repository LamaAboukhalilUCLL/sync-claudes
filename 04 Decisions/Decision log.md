# Decision log

One entry per decision: what, why, who decided, when. Newest at the bottom.

## D1 - Work step by step, explain before building
- **When:** 14 Nov 2026
- **Decided by:** Lama
- **Why:** quality target is Global Finalist; she must understand and own every part.

## D2 - Obsidian vault as project memory
- **When:** 14 Nov 2026
- **Decided by:** Lama
- **What:** context grows in notes instead of a fixed spec. The connected folder `NASA_hackathon` is the vault.

## D3 - Two assistants, synced through the folder
- **When:** 14 Nov 2026
- **Decided by:** Lama, on Claude's recommendation
- **What:** Claude Code in VS Code builds and runs the app in `app/`. Claude in the desktop app does strategy, research, the Space Apps site, review and submission text. `CLAUDE.md`, `Status.md` and the build log keep them in sync.

## D4 - Commit the PSI snapshot
- **When:** 14 Nov 2026
- **Decided by:** Lama
- **What:** `app/raw/` (search result, 24 records, 22 Experimental Tables, manifest with checksums) is committed to git, not ignored.
- **Why:** every number must be traceable to a saved file, and PSI's endpoints are undocumented and may change.

## D5 - Ambient oxygen and burner-flow oxygen are separate fields
- **When:** 14 Nov 2026
- **Decided by:** Lama
- **Why:** oxygen blown from a burner into a fuel atmosphere (CFI-G and Flame Design inverse flames, up to 85%) is not the atmosphere a crew breathes. Mixing them would make the oxygen story wrong.

## D6 - Odd cells are shown as written, never cleaned silently
- **When:** 14 Nov 2026
- **Decided by:** Lama
- **What:** a cell is used as a number only if it is a plain number or a `;`-separated list of plain numbers. Everything else (`3400%`, `~ 21.5`, `RAMP`, blanks) is displayed exactly and kept out of ranges.

## D7 - One repository, code in `app/`
- **When:** 14 Nov 2026
- **Decided by:** Lama
- **What:** code lives in the vault's `app/` folder. The repository is private now and becomes public before submission, notes included.

## D8 - Git routine
- **When:** 14 Nov 2026
- **Decided by:** Lama
- **What:** Claude Code pulls before every write and commits its own work with clear messages. Obsidian Git (on Lama's computer, "ellegio") commits her note edits.

## D9 - No live AI key in the design yet
- **When:** 14 Nov 2026
- **Decided by:** Lama
- **What:** the AI provider is decided at Step 5. Nothing before then may depend on a live API key.

## D10 - `Data-Beyond-Space` is the repository the judges see
- **When:** 14 Nov 2026
- **Decided by:** Lama
- **What:** the public submission repository is `Data-Beyond-Space` (github.com/LamaAboukhalilUCLL/Data-Beyond-Space). This vault (`sync-claudes`) stays the team's shared notes. Publication abstracts stay in `Data-Beyond-Space`.
- **Changes D7:** the product code no longer ends up in the vault's `app/` folder.
- **Consequence, not yet done:** everything a judge needs to trace a number must be in `Data-Beyond-Space` before submission: the PSI snapshot with its manifest, the scripts, the app, the references and the AI acknowledgements. Today the snapshot and two scripts are only in the vault's `app/`. Moving them is a step that waits for Lama's go.

## D11 - Direction for the central insight: Earth-gravity screening
- **When:** 14 Nov 2026
- **Decided by:** Lama
- **What:** the central insight will be about row A of [[NASA stated fire safety needs]]: Earth-gravity material screening may miss the fire risk. Lama chose it from the list of NASA's stated needs.
- **Still to do:** Lama writes the one-sentence insight in her own words; it is then checked against the snapshot.

## D12 - The central insight
- **When:** 14 Nov 2026
- **Decided by:** Lama
- **What:** > "Our dashboard shows how much of NASA's microgravity fire data applies to the new Moon Base habitats and their higher-oxygen air, and where that data stops, so engineers planning those habitats can see which fire questions are already answered and which are not."
- **Where the idea came from:** Lama saw NASA's Moon Base page (updated 12 Nov 2026) and proposed building the dashboard around the new lunar habitats and their higher-oxygen air. Claude Code put her idea into sentence form; she confirmed it.
- **Sources for the claims:** higher oxygen (30 % or more at 10.2 psi or less) is from the challenge statement, and the reason for it from the [[Challenge video]]. The Moon Base page itself says nothing about oxygen or fire. What the data covers is in [[What the investigations show in plain words]] and [[Oxygen evidence (generated)]].
- **Honesty rule that follows:** the dashboard shows coverage and gaps, not predictions of how fire behaves on the Moon. No PSI record tests Moon gravity, and solids stop at about 22 % oxygen.
- **Replaces D11** as the main direction; Earth-gravity screening (D11) stays as a supporting argument for why gaps matter.

## D13 - Scope: the five views
- **When:** 14 Nov 2026
- **Decided by:** Lama asked Claude Code to pick the views; she approved the list and said to build.
- **What:** coverage map, ranked list, investigation page with compare, Moon Base question board, download. No live chat box and no predicted Moon flame behaviour. The AI element is the plain-language summaries and the question board, written in advance, labelled, and checked by program.

## D14 - How the ranking works (proposed by Claude Code, to be confirmed by Lama)
- **When:** 14 Nov 2026
- **What:** five conditions, one point each, no weights: (1) the record's own text names spacecraft fire safety as its purpose, (2) it tests solid cabin materials, (3) a test states 30 % ambient oxygen or more, (4) a test states 10.2 psi or less, (5) both in the same test. Half a point where fire safety is only named as a benefit, or a burner or model stands in for solids. Ties: purpose, then material, then PSI number.
- **Why:** it uses all 24 investigations, every point can be shown with its evidence, and it avoids invented weights.
- **Result:** best score is 3 of 5 (FLEX, ACME CFI-G); none meets all five.
- **Open point for Lama:** D6 keeps cells such as `0.5 atm` (CFI) and `~30% O2` (s-Flame) as text, so they score nothing. Allowing "number plus unit" cells would credit CFI and FLEX-2 for low pressure. Keep D6 strict, or relax it?

## D15 - Obsidian Git auto-sync every 2 minutes
- **When:** 14 Nov 2026
- **Decided by:** the team
- **What:** the Obsidian Git plugin commits and syncs 2 minutes after edits stop (`autoSaveInterval: 2` in `.obsidian/plugins/obsidian-git/data.json`). Pull stays every 5 minutes.
- **Why:** the plugin settings are committed, so both team members share one value. Picking one together stops each person's sync from overwriting the other's setting.

## D16 - PSI only, and a visual-first dashboard (proposed by Mylene, to be confirmed by Lama)
- **When:** 15 Nov 2026
- **Decided by:** Mylene, pending Lama
- **What:** (1) nothing from outside PSI on the site: a "Beyond PSI" page with NASA-report figures was built and removed. (2) The dashboard leads with pictures and keeps text short: overview after a ChatGPT mockup, colour-grid ranking, question tiles, investigation tiles. (3) One real Moon photo (public domain, credited).
- **Why:** rule 6 (every figure from PSI), and the first version felt overwhelming.
- **Where:** branch `research-gaps-on-site`, commit `08ade33`, see [[2026-11-15 Step 5a visual dashboard]].

## D17 - Visual style: calm, photographic, no neon
- **When:** 15 Nov 2026
- **Decided by:** Lama
- **What:** dark and restrained, in the manner of the reference designs she supplied: a real Moon photograph behind the pages, one warm accent, no glows or "AI" look, navigation that a first-time visitor understands. D16 (Mylene's visual-first dashboard, PSI only) is accepted: Lama merged it.
- **Also:** no clickable map of the Moon's surface, because PSI has no lunar locations. A three-stop journey (Earth, low Earth orbit, Moon Base) is used instead. Lama can still overrule this.

## D18 - NASA's colour values
- **When:** 15 Nov 2026
- **Decided by:** Lama
- **What:** points, lines and status marks use the colour values NASA publishes in its Horizon Design System: NASA Red for the Moon Base line and for emphasis, NASA's dark-background chart palette for the fuel types, Active Green for a condition that is met, the Carbon greys for text and lines.
- **Limits kept:** no NASA logo or insignia anywhere, and the footer still says the project is not affiliated with or endorsed by NASA. Commit `Data-Beyond-Space` after `ac5fd84`.

## D19 - Design B, "the poster"
- **When:** 15 Nov 2026
- **Decided by:** Lama, from two previews
- **What:** black page, large Moon photograph, condensed uppercase headlines, no cards, and one accent colour: NASA Red for the Moon Base only.
- **Changes D18:** fuel types no longer have their own colours (tests are grey, solid materials white). The red and the greys remain NASA's values.
- **Why:** the earlier look read as AI-made. See [[2026-11-15 Step 5d design B]].

## D20 - Adjustments to design B
- **When:** 15 Nov 2026
- **Decided by:** Lama
- **What:** keep B's type and black page, but: the Moon whole and fixed in the background; data points coloured by what burns; frames where they add clarity; the clickable journey instead of photographs. This restores the colours of D18 and partly reverses D19's "one accent".

## D21 - Two tools: choose an atmosphere, find a material
- **When:** 15 Nov 2026
- **Decided by:** Lama, from six options
- **What:** build an atmosphere chooser and a material and test finder. Not built: RAG with a language model, an MCP server, a predictive ML model.
- **Why:** they turn the finding into something a reader can use, with low risk on the last day. See [[2026-11-15 Step 6 atmosphere chooser and finder]].

## D22 - Three additions: attribute matrix, Ask the records, reading lists outside PSI
- **When:** 15 Nov 2026
- **Decided by:** Lama, from a list of options with effort and risk
- **What:** (1) an AI-extracted, machine-checked table of what every investigation burned, varied and measured; (2) a question box answered with NASA's own sentences, matched by a small language model that runs in the browser; (3) links to NASA reports outside PSI under each open question.
- **Why:** more technical depth and usefulness without giving up the rule that nothing is invented. No language model writes text on the site, and no API key is needed (keeps D9).
- **Note:** (3) partly reverses D16 (PSI only on the site). Only titles and links are shown; no figure comes from outside PSI. See [[2026-11-15 Step 7 matrix, ask the records, reading lists]].

## D23 - Introduction with a route map, and a Habitat page
- **When:** 15 Nov 2026
- **Decided by:** Lama (her ideas; chosen from PNG previews: introduction A, habitat yes)
- **What:** the overview opens with the problem in three steps and a route map from Earth to the Moon Base; a new Habitat page places the six open questions in a drawing of a habitat.
- **Why:** the start should state the problem at a glance, and readers should see where each fire question sits in a habitat. See [[2026-11-15 Step 8 introduction, route map and habitat]].

## D24 - A statistical model of FLEX (confirmed: Lama merged it on 15 Nov)
- **When:** 15 Nov 2026
- **Decided by:** Lama asked for more depth on a new branch and left the choice of what to build to Claude Code. **Merging is her decision and still open.**
- **What:** an Analysis page with an ordinary least squares model of NASA's FLEX droplet tests, checked by an independent refit, plus a near-miss count on the overview.
- **Why:** FLEX is the only table with high oxygen and an outcome per test, so it is where real analysis is possible. Goes beyond D12 (no predictions) in a limited way: droplets only, inside tested conditions, with ranges. See [[2026-11-15 Step 9 droplet model on a branch]].

## D25 - One table from outside PSI: Earth tests at Moon Base pressure
- **When:** 15 Nov 2026
- **Decided by:** Lama (her idea to look for NASA partner data on solids at 30 % oxygen or more; she said yes to building it)
- **What:** the NASA White Sands Test Facility table of 2007 (NTRS 20070018178) is shown on the Habitat page, marked as not from PSI and as an Earth test. It is never mixed into the PSI counts.
- **Why:** it is the nearest public NASA evidence on solids in Moon Base air, and it sharpens the insight: tested on Earth, not confirmed in space. Reverses D16 for this one table. See [[2026-11-15 Step 10 Earth tests from White Sands and fixes]].

## D26 - SI maps what NASA has written about each fire question (confirmed: Lama merged it on 15 Nov)
- **When:** 15 Nov 2026
- **Decided by:** Lama chose the idea. The method change (a large model labels, the small model is measured) was made by Claude Code after the small model failed, and **awaits her confirmation**.
- **What:** all 925 passages labelled by question with machine-checked quotes; counts and overlaps on the Open questions page; the Ask search scored against the labels.
- **Why:** it extends the coverage finding from tables to text, makes the SI produce a result, and replaces a claim about the search with a measurement. See [[2026-11-15 Step 12 what NASA wrote about each question]].

## D27 - The next test that would teach the most, and the map by meaning
- **When:** 15 Nov 2026
- **Decided by:** Lama (idea 2 chosen from three ideas; the map was her own idea, an Obsidian-style graph instead of similarity numbers). Both merged at her word.
- **What:** on the Analysis page, every condition FLEX's hardware ran is ranked by how much one more test would narrow the model's range at the chosen air; on Explore and the investigation pages, the 24 investigations on a map placed by the language model's similarity of their NASA text.
- **Why:** the first turns the gap into a concrete next step and shows that more droplet tests add little, so the real gap is solids; the second replaces misleading 0.96 to 0.98 numbers with something readable. See [[2026-11-15 Step 14 next test that would teach the most]] and [[2026-11-15 Step 12b review of pull request 6 (Victor Ask upgrade)]].

## D28 - Victor's Ask upgrade and the model switch (confirmed)
- **When:** 15 Nov 2026
- **Decided by:** Lama merged pull request #6 (`33968e0`), which settles the open items below: the Ask upgrade is live, the model is snowflake-arctic-embed-s, and the score is shown with its note that the labels are Claude's and unchecked. Two fixes from the review were merged after it (`bb98735`).

## Open decisions
- **Confirm D14** (ranking conditions) and the D6 question inside it.
- **Project name and wording** on the site (working title: "Flame in Freefall: Moon Base fire data coverage").
- ~~Make `Data-Beyond-Space` public and switch on GitHub Pages~~ Done (public and live, checked 15 Nov 12:30).
- ~~**Approve Victor's 11 wording fixes** to the AI-written texts, the visible AI marks on the drawings ([[2026-11-15 Step 8b AI marks on drawings (Victor)]]) and the phone fix for the table pop-up ([[2026-11-15 Step 8d phone fix for the table pop-up (Victor)]]), all in the pull request from `victor/review-and-ai-marks`, before it is merged.~~ **Done:** merged as pull request #2 (`57a41b9`).
- ~~**Merge or drop two reading-list links** (NESC TM-20260003925 under the materials question, ICES-2025-392 under the gravity question), branch `victor/reading-list-additions`. Links only, no numbers. See [[2026-11-15 Step 11a two reading-list links (Victor)]].~~ **Done:** merged as pull request #5 (`0397c6f`).
- ~~**Merge or drop the Ask upgrade** (branch `victor/ask-upgrade`): counted answers, evidence reach, Moon/partial-gravity card, glossary, related records by meaning, measured score on the Data page. D22 is unchanged (no model writes text). Inside it, three smaller choices: (1) show the score while the labels are Claude's, or only after Victor's re-labelling; (2) keep or drop the AI-drafted glossary; (3) whether to say anywhere that "related by meaning" recovers the cross-links the challenge statement names (the check says: mostly shared words, small gain on ACME BRE and BASS). See [[2026-11-15 Step 11b Ask upgrade (Victor)]].~~ **Done:** merged (D28).
- ~~**Language model for Ask: snowflake-arctic-embed-s or all-MiniLM-L6-v2** (same branch). The branch switches to arctic (Apache-2.0). For it: by meaning alone it is far better on the held-out questions (14 of 20 first, 17 in three; MiniLM 9 and 10). Against it: with the word bonus the site actually uses, the two are level (13 / 17 against 13 / 16), the download grows from about 50 to 62 MB, and it is a new model a few hours before the deadline. Going back is one line in `docs/ask.js` and a rebuild. See [[2026-11-15 Step 11c search quality (Victor)]].~~ **Done:** arctic is live (D28).
- **README and `.gitattributes` suggestions from the fresh-clone test** (Windows `py`, CSV line endings, search-index vectors). See [[2026-11-15 Step 8c eligibility checks and fresh-clone test (Victor)]]. Optional: add CFI-G's self-extinction counts as table evidence for the still-air point. See [[2026-11-15 Step 8a review of AI-written texts (Victor)]].
- **AI provider** for cited answers (Step 5). Options: [[AI provider and hosting options]].
- **Demo format:** 30-second video or 7 slides (Step 6).
