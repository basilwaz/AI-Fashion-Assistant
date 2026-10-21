# User manual

1. Install Python 3.11 or newer and download the repository.
2. Open a terminal in the repository folder.
3. Run `python -m src.server` (or use `python3`).
4. Open http://127.0.0.1:8000 in a browser.
5. Enter a budget. Choose a style and occasion, or leave either set to Any.
6. Select Find outfits. Compare the sample items and their totals.
7. If there are no matches, raise the budget or change a filter.
8. Press Ctrl+C in the terminal when finished.

## Example
Budget $70, Casual, Everyday returns Budget casual with a $67 total. A $10 budget returns no outfits. The current catalog has only four outfits, so some valid choices have no match.

## Limits and troubleshooting
Brands and prices are fictional sample data. Results do not include tax, shipping, size checks, live AI, or purchase links.

Run the Python server rather than opening the HTML file directly. If port 8000 is busy, stop the other server first. Run the test command in the README to check the Python code. Do not enter API keys in the browser.
