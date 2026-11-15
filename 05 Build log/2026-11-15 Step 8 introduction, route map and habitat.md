# Step 8 - introduction with a route map, and the Habitat page

_Sun 15 Nov 2026, about 11:40 to 12:25. Claude Code in VS Code, for Lama._

## What Lama asked for
Lama judged the Ask page honestly: it returns matching passages, which is search, not much "AI". Her two ideas: let readers **see their habitat**, and make the start of the dashboard **introduce the problem clearly with a visual map**. Rule for this step: previews as PNG first, build only after her yes.

## Previews and her choices
Three previews, built from the real data files: introduction A (route map), introduction B (chart of tested air), habitat. Lama chose **A** and **yes to the habitat**, and asked for the space station without a background and the Earth without a ring or circle.

## What was built (`Data-Beyond-Space`, commit `f554eff`, live)
- **Overview** now opens with a question ("Can NASA's fire data protect a Moon Base?"), the problem in three numbered steps, and a route map Earth, low Earth orbit, Moon Base with the number of investigations at each stop (5, 19 and 0 of 24, counted from the data). The line turns red after the space station. The older three-photo journey is replaced by this map.
- **Habitat** (`#/habitat`): a line drawing of a habitat in cross-section with six numbered spots, one per open question (air, bunk, approval sheet, extinguisher, smoke detector, Moon gravity). Choosing a number shows the answer and evidence already on the site. The atmosphere chooser sits on top.
- **Space station photo** replaced: NASA/Roscosmos fly-around photo of 2018, black sky made transparent. Credits updated in `docs/img/CREDITS.md` and the footer.

## Checked
Build, `validate.py`, `check_recount.cjs` pass. Screenshots at desktop width of both pages looked right. Live site serves the new version.

## Not checked or limited
- The six answers are written for Moon Base air. With another air chosen, only the test count changes; the page says so.
- The habitat drawing is a schematic drawn by the AI as SVG code, not a NASA design; the page says so.
- Phones: the headless test cannot go narrower than about 500 px, so a real phone check is still needed.
