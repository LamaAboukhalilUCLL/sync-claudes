# Step 12 - SI maps what NASA has written about each fire question (branch `si-coverage`, not merged)

_Sun 15 Nov 2026, about 18:45 to 19:00 by the machine clock. Claude Code in VS Code, for Lama. Commit `49572f3`._

## What Lama asked for
She found the SI part weak. From three ideas she chose idea 1 (SI maps what NASA has written about each fire question), then idea 2 (the next test that teaches the most) if time allows. "Make sure it is very well done."

## A change of method, and why
The plan was to let the site's small language model (all-MiniLM-L6-v2) sort the passages. Tried first: it could not. With the best rule found it put 133 passages under Moon gravity, almost all about weightlessness, and scored generic combustion text high for "materials". Counts like that would mislead. So:
- **Claude (Anthropic) read all 925 passages** (311 from NASA's records, 614 from paper titles and abstracts) and labelled each with the questions it addresses, following a written guide per question fixed before labelling (`data/content/question_topics.json`).
- **Every label quotes the words that justify it.** `scripts/build_topics.mjs` stops if a quote is not in its passage word for word or if any passage changed since labelling.
- After the pass, a script listed passages with tell-tale words but no label; they were re-read and 4 labels added (363 of 925 passages carry at least one label).
- **The small model is now measured against the labels**, which is the honest test of the Ask page.

## Findings (all computed by the build)
- Passages per question: putting a fire out 155, detection 101, cabin materials 93, trusting the Earth test 41, tested in Moon Base air (high oxygen or low pressure) 26, **Moon gravity 1** (a paper, not a NASA record).
- **Solid materials in high-oxygen or low-pressure air: 4 passages from 2 sources** (the ACME BRE record, a gas burner imitating solids, and one paper on an Earth-based narrow-channel test).
- Detection in high-oxygen or low-pressure air: **0 passages**.
- Ask search, measured: typing each question gives on average **4.8 of the top 10** passages that address it (words and meaning together; 4.2 words alone, 3.4 meaning alone; chance about 1). For the question "Has any fire been tested in Moon Base air at all?" the search finds 0. Published as it is.

## Where it shows
Open questions page (chart, three key numbers, the justifying sentences under each question), Habitat answer panel (one line), Ask page (the measured score), Data page (method and the full measurement table), README "Use of AI" (now five jobs), footer and meta tag.

## Checked
All checks pass (data build, external table, validate, recount, model check, topic quotes). Data page table and Habitat line read in a real Chrome session; Open questions and Ask pages looked at as screenshots.

## Limits
- The labels are the judgement of a language model following a guide. A person should check a sample (for example 30 random passages).
- These count what NASA wrote about, not tests run. Duplicated record text (Saffire I to III, SAME and SAME-R) counts once per passage; the page also gives distinct records and papers.
- Idea 2 not built yet.

## Update, about 19:05: merged, then undone
Lama said "merge". Claude Code merged `si-coverage` into `main` (`bfe1f4b`) and pushed **without first reading Status**, where Victor's branch `victor/ask-upgrade` was listed as waiting for Lama. That branch touches the same files (Ask page, README, styles) and also measures the Ask search, so it no longer merged cleanly. Lama asked to undo the merge.
- `main` was reverted with commit `ee99c38`; `main` is now identical to its state before the merge, and the live site is back to the previous version.
- Victor's branch merges cleanly into `main` again (tested without merging).
- Victor's branch keeps the same 925 passage texts (checksum compared), so the labels in `si-coverage` stay valid with his new language model.
- **To re-apply later:** after Victor's branch is merged, revert the revert (`git revert ee99c38`) or merge `si-coverage` again with that revert undone, then resolve the overlap on the Ask page (keep one score) and rebuild `topics.json` with the model then in use.
- Lesson recorded: pull the vault and read Status before any merge or push to `main`.
