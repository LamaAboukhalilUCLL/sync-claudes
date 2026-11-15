# Step 9b - AI marks on the drawings (Victor)

**Date:** Sun 15 Nov 2026, about 13:50 to 14:15 · **By:** Victor, with Claude (Cowork) for the edits. Repository `Data-Beyond-Space`. **Changed locally, not committed or pushed: waiting for Lama's OK.**

## Why
The Project Submission Guide: SI-generated images "must include a visible watermark to indicate SI generation", and SI-generated code and data must be acknowledged "in descriptive text and metadata". Three pictures on the site are not photographs and were drawn by AI as SVG code: the logo, the route map (overview) and the habitat schematic. Before this change the site said only "The drawing is a schematic, not a NASA design" (habitat), and the footer and metadata named code and summaries but not the drawings or the extracted attributes. Found while compiling [[Project page fields (draft)]].

## What was changed
| File | Change |
|---|---|
| `docs/app.js` | A visible line directly under the route map: "Drawing made with AI assistance. The photographs are NASA's." |
| `docs/app.js` | A visible line directly under the habitat schematic: "Schematic drawn with AI assistance; not a NASA design." |
| `docs/app.js` | Data page, "How AI was used": "three jobs" becomes "four jobs"; new item: the logo, route map and habitat schematic were drawn as code with AI assistance, each carries a note, the photographs are NASA's |
| `docs/styles.css` | One rule `.ai-mark`, same size and colour as the existing `.ai` label |
| `docs/index.html` | Footer sentence now also names the extracted attributes and the drawings (logo, route map, habitat schematic); the HTML comment and the `ai-assistance` meta tag say the same |
| `docs/index.html` | Cache version `v=16` to `v=17` for `styles.css`, `recount.js` and `app.js`, so browsers load the new files |
| `README.md` | "Use of AI": four jobs instead of three, with the drawings as the fourth |
| `docs/img/CREDITS.md` | New "Drawings" section for the route map and the habitat schematic |

No data, number, quotation or design was changed.

The two marks under the drawings say only "made with AI assistance" (shorter on the page, Victor's choice); the tool, Claude (Anthropic), is named in the footer, on the Data page, in the README and in [[SI use log]].

## How it was tested
The edited site was served locally with the data from the build of 13:00 and rendered in headless Chromium at 1440 px:
- the route-map line shows under the drawing on the overview, the habitat line under the schematic;
- the footer and the Data page show the new wording;
- no JavaScript errors; `app.js` passes a syntax check.

Not tested: phones, Firefox, Safari.

## How to run it
```
cd Data-Beyond-Space/docs
py -m http.server 8000
```
Look at: Overview (under the route map), Habitat (under the drawing), Data and method ("How AI was used"), the footer.

## Next
1. Lama reviews (together with [[2026-11-15 Step 9a review of AI-written texts (Victor)]]).
2. With her OK: rebuild, validate, commit, push.
