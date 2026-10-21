# Testing

## Recorded automated result
October 20, 2026: `python -m unittest discover -s tests -v` completed with 12 tests passing on Python 3.12.14.

- Unit: seven tests cover valid and invalid budgets, decimal cents, combined filters, no matches, item totals, sorting, and the exact budget boundary.
- Integration: five tests start a real local HTTP server and check the page/assets, query-to-result flow, invalid inputs, empty results, and source-file isolation.
- Regression: rerun the same 12 tests after each change. The $98 boundary and $67 sample outfit provide stable checks.

## Acceptance checks
These are manual checks to complete in a browser. They are not recorded as passed. Browser automation could not start in the preparation environment because a Chromium executable was unavailable.

| Check | Expected result | Status |
|---|---|---|
| $70, Casual, Everyday | Budget casual, total $67 | API passed; browser check pending |
| $10, Any, Any | No matching outfits message | API passed; browser check pending |
| $100, Sporty, Gym | Simple activewear, total $100 | Unit passed; browser check pending |
| Blank or negative budget | Validation error | Server passed; browser check pending |
| Narrow phone window | Form and text fit the screen | Pending |
| Keyboard only | Labels, controls, button, and status are usable | Pending |

## Sprint 2 tests
- Unit: fit rules, favorite identifiers, cheaper alternatives, and AI response validation.
- Integration: saved outfits reload after refresh, and an AI request uses catalog item IDs.
- Regression: run the existing suite before merging each change.
- Acceptance: follow the user manual, verify real product links, test missing/failed AI credentials, and complete the browser checks above.

No live AI or shopping integration has been tested because neither is implemented.
