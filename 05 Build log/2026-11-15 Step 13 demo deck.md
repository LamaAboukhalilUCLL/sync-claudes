# Step 13: demo deck (7 slides)

_15 Nov 2026, Claude desktop app (Cowork), for Lama_

## What was done
- Built the 7-slide demo deck as a Claude Slides artifact, 1920 x 1080, from Lama's full brief. Every word, number and quotation on the slides comes from her brief; nothing was added.
- Studied the live site first (`styles.css?v=20`): same colours, fonts (Barlow Condensed 600, Public Sans, DM Mono), frames (`#444447`, `rgba(12,12,14,.78)`) and Moon backdrop.
- Slides: 1 title, 2 problem, 3 what we built, 4 the finding, 5 check your habitat, 6 how it stays true, 7 what is still open.
- Images: the five site screenshots Lama attached (the oxygen chart cropped to its chart part, empty top and bottom trimmed), NASA's LRO Moon photo, and the team seal rendered from its SVG with the real fonts. No image was generated.

## Choices made while building
- The Moon photo was masked to a clean disc on black (the Slides format caps rounded corners), which also removes the small LROC caption in its corner.
- Footer on every slide at 14 px DM Mono, as asked. It is small when projected; easy to enlarge.
- Source lines on slide 2 begin with "Source:".
- Image alt texts avoid any number that is not in the brief.

## How to see it
Open the Slides artifact "Flame in Freefall: Data Beyond Space" in Claude. Export > PowerPoint or PDF from the deck's Share menu. A public link is set from Share.

## Checks
- Exactly 7 slides; team name, six names and challenge on slide 1.
- Automated scan: no "--", no em or en dash, no middle dot. Every number on each slide listed and compared with the brief.
- Rendered locally with the real fonts; nothing runs past the margins.

## Next
- Lama checks each slide in the viewer, then sets the public link and exports the PowerPoint.
- Add the deck link to the project page.
