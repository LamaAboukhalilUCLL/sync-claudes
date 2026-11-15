# Step 8d - phone fix for the table pop-up (Victor)

**Date:** Sun 15 Nov 2026, about 14:40 to 14:50 · **By:** Victor (found it on his phone), with Claude (Cowork) for the diagnosis, the edit and the tests. Repository `Data-Beyond-Space`, file `docs/styles.css`. **Goes into the open pull request from branch `victor/review-and-ai-marks`; not merged: waiting for Lama.**

## What was wrong
On a phone, "View NASA's table" on the Open questions page seemed to do nothing. The table did open, but off the right edge of the screen, with its close button, so the page only went dark and the reader was stuck until pressing Back. The same pop-up is used by every "Open NASA's table" button and every "Row n" link, so all of them were affected on phones. On a laptop it worked only because the screen is wider than the pop-up.

## Why
The table cells never wrap, so the table is very wide. The pop-up is centred with a CSS grid, and that grid's one column grew to the full width of the table; the pop-up was then centred inside that over-wide column.

## What was changed
| File | Change |
|---|---|
| `docs/styles.css` | `#modal` gets `grid-template-columns: minmax(0, 1fr);` so the column can never be wider than the screen. The table still scrolls sideways inside the pop-up |

One line. No data, text or design changed. The cache version for `styles.css` is already raised to `v=17` in the same pull request, so phones load the new file.

## How it was tested
Headless Chromium with phone emulation (Playwright), on a copy of the live site and on the pull-request branch:

| Device and page | Before | After |
|---|---|---|
| iPhone 13 Pro, Open questions | Pop-up from 326 to 1,506 px on a 390 px screen; close button unreachable | 16 to 374 px; fits; × closes it |
| Pixel 7, Open questions | Off-screen (same cause) | 16 to 396 px on 412 px; fits; × closes it |
| iPhone 13, Explore finder, "Row n" | Off-screen (same cause) | Fits; × closes it |
| Desktop 1440 px, Open questions | Fine | Unchanged, 1,180 px box centred |

No JavaScript errors. Not tested on a real phone after the fix: Victor checks the live site once it is merged.

## How to run it
```
cd Data-Beyond-Space/docs
py -m http.server 8000
```
Open it in the browser, press F12, switch on the phone view (Ctrl+Shift+M), go to Open questions and tap "View NASA's table".

## Next
1. Victor commits and pushes to the same branch; the fix appears in the open pull request.
2. Lama reviews the pull request.
3. After the merge: open the live site on a phone and check again.
