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

## Update, about 20:00: architecture deck
Lama asked for a new structure: slide 1 shows the architecture of all components, each other slide shows the role of two components side by side. She chose to keep it in the Claude deck (the SharePoint .pptx can't be edited live from here) and to put the title details and the architecture together on slide 1.
- Slide 1: team, six names, challenge, link, and a diagram in three layers: NASA sources (1 PSI snapshot, 2 White Sands tests), build and checks (3 SI texts, 4 build and checks), dashboard in the browser (5 to 12).
- Slides 2 to 7: two components each, "What it does", "Why it helps", and one key number or a screenshot.
- Texts drafted by Claude from the build logs and the live site; numbers only from the earlier brief and the build logs (24, 22, 26, 10.17, 7, 81, 0 of 24 and 3, 274, 43 %, 925, 0/3/3). To be read by Lama.
- **To check:** slide 7 says "SI maps what NASA has written about each question" (Step 12). On the live site at about 19:55 (cache version 23) that part did not show yet. Delete the sentence if `si-coverage-2` is not live at submission.
- Slide 6 names the Ask model as snowflake-arctic-embed-s (Victor's Step 11c, merged with pull request #6).
