# Step 5c - design round two

**Date:** Sun 15 Nov 2026, 01:40 · **By:** Claude Code (VS Code), on Lama's feedback. Repository `Data-Beyond-Space`, branch `main`, commit `d93a62a` plus a credits follow-up, pushed and live.

## Lama's feedback and what was done
| Feedback | Change |
|---|---|
| "For Earth put an Earth" | The journey stops are NASA photographs: Earth (Apollo 17), the space station (STS-132) and the Moon (LRO). All public domain, sources and checksums in `docs/img/CREDITS.md` |
| No dashed lines, no floating dot | The line between stops is solid; the placeholder dot is gone; chart reference lines are solid |
| No middle dots, it reads as AI | Every "·" separator removed from the page text (9 places) |
| No line on the left of boxes, no boxed labels | Accent bars removed from question tiles, notes and quotations. Status is a coloured dot and plain words ("Open", "Partly answered"). Fuel types are a dot and a word. "AI-written" is plain italic text. "See the table" is a text link |
| Vary the fonts | Titles in Cormorant Garamond (serif), reading text in Inter, small technical labels in DM Mono. Large numbers in Inter |
| Circular logo saying Data Beyond Space | A circular mark drawn as SVG: the team name around a ring, "dbs" in the centre. In the header and the footer |
| Look at the best sites for this theme | NASA's own Horizon Design System (public repository `nasa/hds-core`) ships exactly Inter, DM Mono and Public Sans, so two of our three families match what NASA uses. Its stated aim is to cut visual noise. We use the fonts only, not NASA's theme or any NASA insignia |

## Added afterwards: NASA's colours
Lama asked for NASA's colours on the points and coloured elements. The values come from NASA's public design system: solids `#f29d49`, droplets `#609af6`, gas flames `#79a3ad`, burner emulating solids `#c2b47c`, Moon Base line NASA Red `#f64137`, emphasis `#ff5c52`, condition met Active Green `#47da84`, greys from the Carbon scale. Recorded as D18.

## Why these choices
- Fonts are served from `docs/fonts/` (SIL Open Font License), so the site makes no request to an outside font service and still works offline.
- Buttons and navigation are in sentence case; uppercase is kept only for a few small technical labels.

## How it was tested
Headless Chrome screenshots at 1440 px: overview (top and full page), questions, an investigation page, ranking. Build and all validation checks pass. **Not tested:** a person clicking through, phones, Firefox and Safari.

## Next
Lama looks at the live site. Then the project page text and the demo.
