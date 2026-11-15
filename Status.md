# Status

_Last updated: Sun 15 Nov 2026, 20:15 (Claude Code, for Lama)_

## Done
- [x] Step 0 - folder and vault set up ([[2026-11-14 Step 0 setup]])
- [x] Step 1a - PSI snapshot saved and oxygen evidence table built ([[2026-11-14 Step 1a oxygen evidence pass]])
- [x] Step 1b - external briefs checked against the snapshot ([[2026-11-14 Step 1b vetting the external briefs]])
- [x] Step 1 side task (Victor) - publication abstracts, outside the steps ([[2026-11-14 Step 1 side task publication abstracts (Victor)]])
- [x] Step 1c - Victor's work reviewed against the snapshot; D10: judges see `Data-Beyond-Space` ([[2026-11-14 Step 1c review of Victor's work]])
- [x] Web research: what NASA says it needs, matched to our data ([[NASA stated fire safety needs]])

- [x] Step 1 - central insight decided (D12) ([[2026-11-14 Step 1 central insight]])
- [x] Steps 2 to 4 - snapshot moved into `Data-Beyond-Space`, data pipeline, checks, and first full dashboard ([[2026-11-14 Steps 2-4 data pipeline and dashboard]])
- [x] Step 5a - visual dashboard on branch `research-gaps-on-site`, commit `08ade33`, not merged ([[2026-11-15 Step 5a visual dashboard]])

- [x] Step 5b - redesign with Moon backdrop and journey, live on GitHub Pages ([[2026-11-15 Step 5b redesign and Moon backdrop]])
- [x] Step 5c - design round two: fonts, logo, NASA photos, plainer labels ([[2026-11-15 Step 5c design round two]])
- [x] Step 5d - design B chosen by Lama and applied to all pages ([[2026-11-15 Step 5d design B]])
- [x] Step 6 - atmosphere chooser and material finder, live ([[2026-11-15 Step 6 atmosphere chooser and finder]])
- [x] Step 7 - attribute matrix, Ask the records, reading lists outside PSI; live on GitHub Pages since 12:00 (`0663cde`); Ask tested on the live site in Chrome ([[2026-11-15 Step 7 matrix, ask the records, reading lists]])
- [x] Step 8 - introduction with route map, and Habitat page, live (`f554eff`) ([[2026-11-15 Step 8 introduction, route map and habitat]])
- [x] Step 8a (Victor) - review of the AI-written texts: 11 wording fixes, build and validate pass; **merged into `main` (pull request #2, `57a41b9`) and live** ([[2026-11-15 Step 8a review of AI-written texts (Victor)]])
- [x] Step 8b (Victor) - visible "made with AI assistance" marks on the AI-drawn route map and habitat schematic; footer, metadata, Data page and README name the drawings; **merged into `main` (pull request #2, `57a41b9`) and live** ([[2026-11-15 Step 8b AI marks on drawings (Victor)]])
- [x] Step 8c (Victor) - fresh clone rebuilds and validates on Linux and on Windows (incl. `npm install` and the search index); all 24 DOIs resolve; live downloads and Ask work ([[2026-11-15 Step 8c eligibility checks and fresh-clone test (Victor)]]). Private window on Chrome (computer) checked by Victor: fine. All members confirmed registered in the Universal Event (Victor, 15 Nov). **Still open:** Firefox click-through
- [x] Step 8d (Victor) - phone check found the table pop-up opening off-screen; one-line CSS fix, tested on emulated phones and desktop; **merged into `main` (pull request #2) and live**; still to check on a real phone ([[2026-11-15 Step 8d phone fix for the table pop-up (Victor)]])
- [x] Step 9 - droplet model and Analysis page, merged into `main` (`f841a17`) and live ([[2026-11-15 Step 9 droplet model on a branch]])
- [x] Step 10 - Earth tests from NASA White Sands on the Habitat page, near-miss and Saffire-II wording fixed; merged into `main` (`f841a17`) and live ([[2026-11-15 Step 10 Earth tests from White Sands and fixes]])
- [x] Step 11 - "Check your habitat": the drawing is the tool, with a downloadable report; merged into `main` (`f841a17`) and live ([[2026-11-15 Step 11 habitat check]])
- [x] Step 11a (Victor) - two NASA documents added to the reading lists of two open questions (links only); **merged into `main` (pull request #5, `0397c6f`)** ([[2026-11-15 Step 11a two reading-list links (Victor)]])
- [x] Step 11b (Victor) - Ask upgrade: counted answers from NASA's tables, evidence reach for the chosen atmosphere, Moon/partial-gravity card, everyday-word glossary, related records by meaning, measured score (28 of 40 first, 32 of 40 in the first three; labels by Claude, unchecked); **on branch `victor/ask-upgrade`, waiting for Lama** ([[2026-11-15 Step 11b Ask upgrade (Victor)]])
- [x] Step 11c (Victor) - search quality of Ask: test questions split into a tuning and a held-out half; headers, investigation ranking, rank fusion and title weight tried and not adopted; language model switched to snowflake-arctic-embed-s (Apache-2.0). Held-out half: 13 of 20 first and 17 in the first three (before: 13 and 16); by meaning alone 14 and 17 (before: 9 and 10). **Same branch `victor/ask-upgrade`, waiting for Lama** ([[2026-11-15 Step 11c search quality (Victor)]])
- [x] Step 12 - SI maps what NASA wrote about each fire question, Ask search measured; branch `si-coverage` (`49572f3`); merged at 19:00 by mistake before checking Victor's branch, **merge undone** (`ee99c38`), waits until `victor/ask-upgrade` is merged ([[2026-11-15 Step 12 what NASA wrote about each question]])
- [x] Step 13 - demo deck, 7 slides, built in Claude (Slides artifact) from Lama's full brief: site look, her numbers and quotations only; exportable as PowerPoint; still to check and share by public link ([[2026-11-15 Step 13 demo deck]])
- [x] Step 12b - pull request #6 (Victor) reviewed: all checks pass, merges cleanly, no errors in the browser; 2 fixes before merging (unchecked labels, "drop" in the word list), 2 worth fixing ([[2026-11-15 Step 12b review of pull request 6 (Victor Ask upgrade)]])
- [x] Review fixes merged into `main` and live (`bb98735`): word list without "drop", shared context links mark the passage
- [x] Step 12 re-applied on top of Victor's Ask upgrade: branch `si-coverage-2` (`c0c6270`), merged ([[2026-11-15 Step 12 what NASA wrote about each question]])
- [x] Step 12 merged into `main` and live (cache version 24)
- [x] Step 14 - the next test that would teach the most: branch `next-test`, **waiting for Lama to say merge** ([[2026-11-15 Step 14 next test that would teach the most]])

## In progress
- [ ] Merge `si-coverage-2` (Lama). A teammate checks a sample of the labels. Map by meaning: preview waiting for Lama's yes or no.
- [ ] **Waiting for Lama:** review and merge or drop branch `victor/ask-upgrade` ([[2026-11-15 Step 11b Ask upgrade (Victor)]]). Before the score goes live, Victor re-labels the 40 test questions and checks the glossary. The branch now also holds Step 11c, with a model switch for Lama to decide ([[2026-11-15 Step 11c search quality (Victor)]]).
- [ ] **17:00**: Lama writes the project page text and the demo. Compiled fields ready to paste (NASA data with all 24 DOIs, references, Use of SI draft, checked numbers): [[Project page fields (draft)]].
- [ ] **Lama reviews the dashboard**: run it (see the build log), read every AI-written text, confirm or change D14.
- [ ] **Lama approves the visual design (D16)** on branch `research-gaps-on-site`; then push and merge it into `main` through a pull request.

## Next
- [x] ~~Make `Data-Beyond-Space` public and switch on GitHub Pages~~ Done: the repository shows as public and the site is live (checked 15 Nov, 12:30). Still to do: open the link in a private window.
- [x] ~~Lama approves Victor's review edits, then they are pushed~~ Done: pull request #2 merged ([[2026-11-15 Step 8a review of AI-written texts (Victor)]])
- [ ] Project page text, demo (30-second video or 7 slides), submission checklist (next step number is Lama's; 8a to 8d are Victor's checks)

## Open questions
- ~~Who is the Team Owner?~~ **Answered:** Lama Abou Khalil (team page "Data Beyond Space", Members tab, marked Team Owner). She is in Belgium, so the deadline is **Sun 15 Nov, 23:59 CET**.
- ~~Does the Members tab show at least 2 people?~~ **Answered:** 6 members, all Belgium: Lama Abou Khalil, Mikho Demetrashvili, Nguyễn Thị Thanh Vy, Mylene Aradani, Lina Belabed, Victor Suciu. Still open: who does what.
- ~~Demo format (30-second video or 7 slides) and who owns it?~~ **Answered:** 7 slides, built from Lama's brief ([[2026-11-15 Step 13 demo deck]]).
- Who or what wrote the two external briefs and the pasted plan? Needed for the SI use log (a row is waiting there).
- BASS and Saffire-III state no oxygen value in their tables. Do we look for it in their documents, or present it as "not stated"?
- PSI-10 (Flame Design) has a blank license field. Fine to use (it is NASA open data with a DOI), but worth a line in the references.
- Which AI API will the app use for cited answers (Step 5)? Deferred by decision D9. Options gathered in [[AI provider and hosting options]].
- ~~Where do publication abstracts live?~~ **Answered (D10):** in `Data-Beyond-Space`, the repository the judges see.
- Abstract coverage is 73 of 235 and near zero for the solid-fuel investigations ([[Publications and abstracts]]). What does the AI layer read for those: PSI record text only, or also PSI reports and NASA factsheets?

## Clock
Deadline Sunday 15 Nov, 23:59 (Team Owner's local time). Aim for a first submission Sunday afternoon; it can be resubmitted until the deadline.
