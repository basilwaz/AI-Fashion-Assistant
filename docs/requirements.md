# Requirements and features

## Baseline and counting
The September 13 README is the available baseline: 11 planned features. A separate HW2 submission and instructor approval record were not supplied. The 12 requirements below are the current proposed testable breakdown. They are not a claim about what was approved in HW2.

Current prototype: 5/11 features = 45.5%, with sample data limitations. Requirements: 7/12 = 58.3%. Remaining: 6 features and 5 requirements. Counts describe the version prepared on October 20, 2026, not the end of Week 8.

## Features

| ID | Feature | Status |
|---|---|---|
| F1 | Personal fashion preferences | Complete for prototype: budget, style, occasion |
| F2 | Budget filter | Complete |
| F3 | Height, gender, and size options | Pending |
| F4 | Style and occasion filters | Complete |
| F5 | AI outfit recommendations | Pending |
| F6 | AI-generated outfit previews | Pending, stretch goal |
| F7 | Clothing brands and prices | Complete with sample data only |
| F8 | Links to buy clothing | Pending |
| F9 | Total outfit price | Complete, before tax and shipping |
| F10 | Save favorite outfits | Pending |
| F11 | Find cheaper alternatives | Pending |

F1 is limited to the current form. F7 uses fictional demo brands and prices. These are prototype completion counts, not completion of live shopping or AI capabilities. AI preview images remain part of the original feature list but are not part of the proposed core MVP requirement list.

## Requirements and acceptance criteria

| ID | Requirement | Acceptance criterion | Status |
|---|---|---|---|
| R1 | Open the preference form | The local home page shows budget, style, and occasion controls. | Complete |
| R2 | Validate the budget | Blank, invalid, zero, negative, non-finite, and more than two decimal places are rejected. | Complete |
| R3 | Filter by style | Only outfits with the chosen style appear, unless Any is selected. | Complete |
| R4 | Filter by occasion | Only outfits for the chosen occasion appear, unless Any is selected. | Complete |
| R5 | Stay within budget | Every returned total is at or below the entered budget. | Complete |
| R6 | Show item prices and total | Displayed items have sample brands and prices, and the total equals their sum. | Complete |
| R7 | Handle no matches | An empty list is returned and the page tells the user to change preferences. | Complete |
| R8 | Add fit preferences | Height, gender, and size are accepted and used against supported product information. | Pending |
| R9 | Add AI recommendations | A server-side AI call uses preferences and returns valid catalog item IDs, with a fallback on failure. | Pending |
| R10 | Add verified products and links | Each listed real product has a checked source link and a price-check date. | Pending |
| R11 | Save outfits | A user can save and remove an outfit and find it after refreshing. | Pending |
| R12 | Find cheaper alternatives | A lower-priced matching alternative appears when one exists. | Pending |

## Proposed MVP scope
Keep the form and budget rules. Add R8-R12 in small steps. Use a small manually verified catalog first, rather than depending on a full shopping API. AI should suggest combinations from known items and should not invent a price or purchase link. Keep the original feature list visible and ask the instructor before reducing final scope.
