# Publications and abstracts

**Added:** Sat 14 Nov 2026 · **By:** Vic, with Claude (Cowork)

The PSI snapshot in `app/raw/` holds each investigation's publication list (title, authors, DOI) but no abstracts. Step 1a notes that publications were not read. This note covers what we can get for them, for Step 5 (AI answers with citations).

## Numbers (first run, 14 Nov 2026)
- **352** publication entries across the 24 records; **284** have a DOI; **235 unique DOIs**.
- **72 of 235** DOIs (31 %) returned an abstract from OpenAlex. The rest have title, year and venue only.
- Most papers are in Combustion and Flame, Proceedings of the Combustion Institute, Fire Safety Journal and similar journals, often paywalled.

## Where the data is
Repository `Data-Beyond-Space` (LamaAboukhalilUCLL), separate from this vault:
- `scripts/fetch_papers.py` reads the DOIs from `sync-claudes/app/raw/PSI-*.json` (it does not download PSI again) and looks each one up on [OpenAlex](https://openalex.org).
- `data/papers/papers.json`: one entry per DOI, with the PSI ids that cite it, title, year, venue, open-access link, abstract (null when missing).
- `data/papers/manifest.json`: run time, which snapshot files were read (with their SHA-256 from `app/raw/manifest.json`), counts, errors.

Where this should live (that repo, or `app/` here) is an open decision, see [[Decision log]].

## What this means for Step 5
- An abstract is the authors' own summary, so it can support a cited sentence. A title alone cannot.
- With 31 % coverage, answers built only on abstracts will be thin, and uneven across investigations.
- Fallbacks, both NASA sources, not yet fetched or checked:
  - each investigation's own **Reports** and **Science Documents** folders in PSI (final reports exist for most flight experiments; check per record);
  - the NASA Glenn **factsheets** (1-2 pages each), linked from the [NASA Glenn combustion page](https://www.nasa.gov/glenn/glenn-expertise-space-exploration/physical-sciences-program/combustion-science/):
    - [ACME](https://www.nasa.gov/wp-content/uploads/2025/07/advanced-combustion-via-microgravity-experiments-acme.pdf)
    - [BASS](https://www.nasa.gov/wp-content/uploads/2025/07/burning-and-suppression-of-solids-bass.pdf)
    - [DAFT](https://www.nasa.gov/wp-content/uploads/2025/07/dust-and-aerosol-measurement-feasibility-test-daft.pdf)
    - [FLEX](https://www.nasa.gov/wp-content/uploads/2025/07/flame-extinguishment-experiment-flex.pdf)
    - [Saffire](https://www.nasa.gov/wp-content/uploads/2025/07/spacecraft-fire-safety-demonstration-saffire.pdf)
    - [SAME](https://www.nasa.gov/wp-content/uploads/2025/07/smoke-aerosol-measurement-experiment-same.pdf)
    - [SLICE](https://www.nasa.gov/wp-content/uploads/2025/07/structure-liftoff-in-combustion-experiment-slice.pdf)
    - [SPICE](https://www.nasa.gov/wp-content/uploads/2025/07/smoke-point-in-co-flow-experiment-spice.pdf)
- OpenAlex is not NASA data. If abstracts are used, OpenAlex goes in [[References]] and each abstract is cited by its paper DOI, not by the PSI DOI.

See also: [[PSI data source]], [[AI provider and hosting options]].
