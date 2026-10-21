# Architecture and design

The browser collects preferences and requests `/api/recommend`. The Python server sends those preferences to the recommendation function. That function filters the sample catalog and returns matching outfits. The browser displays the results.

## Responsibilities
- `web/index.html`: preference form and results area.
- `web/style.css`: layout and appearance.
- `web/app.js`: send the request and render the response.
- `src/server.py`: serve the page and handle the HTTP request.
- `src/recommendations.py`: validate budgets, filter outfits, and calculate totals.

## Design learning
Single responsibility is the main principle. The HTTP handler does not decide which outfits fit the budget. That decision belongs in the recommendation module, so it can be tested without starting a server.

Outfits are stored as data rather than repeated branches for every style. Money uses whole cents, so totals do not depend on floating point rounding. Input checks return early. A few short `if` checks are useful for validation and routing. Long nested if/else chains would make this harder to read.

This is the first implementation, so there is no earlier code refactor to claim. The improvement over the original plan is a clear division between the page, server, and recommendation rules. No extra design pattern is needed for this small version.

## Sprint 2 design
Keep the current rule-based recommender as a fallback. Add an AI provider function only when credentials are available. Keep its key on the server, validate returned item IDs, and calculate prices from the catalog. Add browser storage for favorites. Avoid accounts and a database until they are needed.

The Python server is for local development. GitHub Pages can host a project information page, but cannot run this Python backend.
