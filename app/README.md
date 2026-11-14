# app

The dashboard code lives here. Open the vault root (one level up) in VS Code so Claude Code reads `CLAUDE.md`.

`_draft/` contains an untested first draft written by Claude on 14 Nov. Reference only.

## What is here
- `fetch_snapshot.py` - downloads the PSI search result, the 24 Combustion Science records and their Experimental Tables into `raw/`, unchanged. Run: `py fetch_snapshot.py`
- `raw/` - that snapshot (NASA PSI data, retrieved 14 Nov 2026), with `manifest.json` listing source URL, time, size and SHA-256 of each file. Committed on purpose; do not edit.
- `evidence_oxygen.py` - reads `raw/` and writes `../03 Data/Oxygen evidence (generated).md`. Run: `py evidence_oxygen.py`

Python 3 only, no packages to install. Both scripts were written with AI assistance (Claude Code, Anthropic); the data in `raw/` is NASA's and is not AI-generated.
