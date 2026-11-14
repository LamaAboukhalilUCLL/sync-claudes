# Side task - publication abstracts

**Date:** Sat 14 Nov 2026 · **By:** Vic, with Claude (Cowork). Outside the numbered steps; no step was built ahead.

## What was done
1. Before this vault was shared with him, Vic wrote a separate fetch script in repository `Data-Beyond-Space` that downloaded PSI records and tables again and looked up the publication DOIs on OpenAlex. That duplicated `app/raw/` and went against D7 (one repository, code in `app/`).
2. Cleaned up the same day: the duplicate PSI records, tables and script were removed. `Data-Beyond-Space` now holds only `scripts/fetch_papers.py` and `data/papers/`, the one thing `app/raw/` does not cover: abstracts. The script reads DOIs from `app/raw/` and records the SHA-256 of each snapshot file it read.
3. Added notes: [[Challenge video]], [[Publications and abstracts]], [[AI provider and hosting options]]; rows in [[SI use log]] and [[References]]; answered two open questions in [[Status]].

## How to run it
From the `Data-Beyond-Space` repository, with `sync-claudes` cloned next to it:
```
python scripts/fetch_papers.py
```

## Learned
- 235 unique DOIs, 73 with an OpenAlex abstract (31 %). (Corrected from 72; see [[2026-11-14 Step 1c review of Victor's work]].)
- The removed duplicate (about 28 MB) is still in that repository's git history. It does no harm; rewriting shared history would.

## Open
- Keep abstracts in `Data-Beyond-Space`, or move `fetch_papers.py` into `app/` here? Lama's call (added to [[Decision log]]).

## Next
Unchanged: Lama decides the central insight (Step 1).
