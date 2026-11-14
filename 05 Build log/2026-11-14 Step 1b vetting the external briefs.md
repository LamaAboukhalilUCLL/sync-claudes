# Step 1b - vetting the external briefs

**Date:** Sat 14 Nov 2026 · **By:** Claude Code (VS Code), at Lama's request

## What was done
Lama supplied two PDFs ("Technical Architecture & Research Report", "Step 1: Central Thesis, Mission Presets & Evaluation Rubric") and a pasted execution plan, and asked to keep only what is reliable. Every checkable claim was compared with the snapshot in `app/raw/`, plus a few live PSI searches (PSI-188, "SoFIE", "Saffire", "LUCI", "FLARE"). The result is [[Vetted reference from the external briefs]], sorted into verified, unverified and rejected. No code was written or changed. The PDFs themselves are not in the vault.

## Why
The briefs mix sound ideas with claims about data PSI does not hold. Rule 6 (never invent data) needs them separated before anything is built on them.

## Learned
- **No PSI combustion record mentions partial gravity, the Moon or Mars.** A partial-gravity thesis could not be driven by PSI data.
- PSI does state, as hypotheses, that materials in ventilated microgravity "burn as well if not better" than in normal gravity (BASS, BASS-II), and that the 1-g screening test ignores low-gravity effects.
- **Saffire-II is the one table pairing microgravity and 1-g results**, and it cuts both ways: thin silicone burned completely in 1 g and not in microgravity.
- The three atmospheres (14.7 psia / 21 %, 10.2 / 26.5 %, 8.2 / 34 %) are sourced from PSI-20. PSI does not label any of them "Moon Base" or "Mars".
- Oxygen partial pressure is about the same in all of them (2.7-3.1 psi); what rises is concentration.
- PSI-188 is a colloids experiment. SoFIE, Saffire-IV to VI, LUCI and FLARE are not in PSI.
- The briefs repeat the burner-flow mistake (CFI-G 85 % used as an atmosphere).
- "Related investigations" links are in the records and give the ground-study to flight-parent mapping.

## How to check it
Open any record in `app/raw/PSI-<n>.json` and search for the quoted sentence; open `app/raw/PSI-99_table_1.csv` for the Saffire-II rows.

## Next
Unchanged: Lama decides the central insight (Step 1). Then Step 2.
