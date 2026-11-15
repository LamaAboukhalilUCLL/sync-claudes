# Step 5d - design B ("the poster")

**Date:** Sun 15 Nov 2026, 02:12 · **By:** Claude Code (VS Code); design chosen by Lama. Repository `Data-Beyond-Space`, branch `main`, commit `442774a`, pushed and live.

## Why
A friend of Lama's said the site looked AI-made. Lama asked for a proper study of design and previews before any change.

## What the study found
The earlier design used the habits that AI-built pages share: a coloured italic word in the headline, a frosted box of big numbers over a photo, two buttons under the headline, everything inside bordered cards, three equal cards in a row, small uppercase labels over every title, a colour per category, the Inter typeface throughout. Pages made by people (NASA's own, newspaper data desks) make fewer and firmer choices: captioned photographs, charts drawn on the page with a written note, one accent colour, tables with rules instead of boxes.

## How it was decided
Two previews were built from the real data and shown as images, nothing pushed: A "the report" (light, serif, like a science article) and B "the poster" (black, large Moon, condensed uppercase headline). **Lama chose B.** Recorded as D19. The preview files are in `Data-Beyond-Space/_previews/`, which git ignores.

## What B is
- **Type:** Barlow Condensed uppercase for headlines, Public Sans for text, DM Mono only for cells quoted from NASA's tables.
- **Colour:** NASA Red for the Moon Base and nothing else. Tests are grey, solid materials white, tests inside the Moon Base zone red. This replaces the per-category colours of D18; the red and the greys are still NASA's values.
- **No boxes:** no cards, glass panels, pills or coloured italics. Space and hairlines separate sections.
- **Figures:** each chart has a figure title, a note written on it and a source line.
- **Overview as one piece:** photograph and headline, three figures, Figure 1, three places with NASA photographs (replacing the clickable journey), the seven closest investigations, the six open questions.
- **Ranking:** plain marks (filled, half, ring, blank for "the table does not say") in a rules-only table.

## Adjusted the same morning, on Lama's feedback (D20)
- The Moon is the fixed background of every page, shown whole, instead of a cropped disc in the hero.
- Data points and bars are coloured again by what burns (NASA's chart palette). NASA Red stays reserved for the Moon Base.
- Frames are back where they help: charts, tables, the key figures, question blocks, detail blocks.
- The three clickable stops (Earth, low Earth orbit, Moon Base) are back in place of the three photographs.
Commit after `97af2e5` in `Data-Beyond-Space`.

## How it was tested
Headless Chrome screenshots at 1440 px of the overview, an investigation page and the coverage map; build and validation pass. **Not tested:** a person clicking through, phones, Firefox and Safari; the ranking, questions and data pages were not looked at after the change.

## Next
Lama looks at the live site. Then the project page text and the demo.
