# Step 11 - the habitat drawing becomes the tool ("Check your habitat")

_Sun 15 Nov 2026, about 16:00 to 16:10. Claude Code in VS Code, for Lama. Branch `droplet-model`, commit `e6e42e3`, not merged._

## What Lama asked for
Focus everything on a finding and a tool, not on showing things. After a preview she asked to keep the habitat sketch she likes, make it "one big thing", put each input next to the part it belongs to, and keep it easy on the eye.

## What was built
- The Habitat page is now **Check your habitat**. Five boxes sit on top of the drawing, each tied by a line to a part: the air inside, mattress and padding (foams), curtain and bedding (fabrics), equipment rack (rigid plastics), hull and wall panels (composites and laminates).
- Each material box lists the samples of that group from the NASA White Sands table. Choosing one colours the part: red when it fails NASA's flame test on Earth at the chosen oxygen level, white when it passes on Earth. The box says "Passes on Earth, not confirmed in space", because PSI has no solid-material test in weightlessness at that oxygen level.
- A strip of three numbers sums it up (fail on Earth, pass on Earth, 0 confirmed in space).
- **Download this report** gives a text file with the choices, NASA's printed values, the open questions and both sources. **Copy a link** reopens the same habitat (`#/habitat?atm=...&m=...`).
- The six numbered question spots stay on the drawing; the list and the answer panel sit below. The chart of all 26 samples is folded away.
- The starting materials are the first sample of each group in the paper's order, so nothing is hand-picked.

## Checked
All builds and checks pass. In a real Chrome session: changing a material and the air updates the numbers, and the pressure warning appears at 8.2 psi. Screenshots at 30 % and 34 % oxygen looked right. Not checked: the clipboard copy (cannot be read in the test browser; the page shows the link as text if copying fails), phones, other browsers.

## Limits
The parts are examples: NASA's table does not say what a mattress or a rack is made of. The page says the parts are examples and the materials are samples NASA tested.
