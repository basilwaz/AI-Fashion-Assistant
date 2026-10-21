# AI Fashion Assistant

Basil Wazwaz, ASE 420. AI-Assisted Development.

## Problem and goal
Finding clothes that fit a budget can take a while. My goal is a website that helps users choose an outfit based on their preferences and see the total price.

## Current prototype
Enter a budget, style, and occasion. The app filters four sample outfits, shows sample brands and item prices, and adds up each outfit. It also handles invalid budgets and empty results.

The sample catalog is local. The prototype does not call an AI service, search stores, check fit, or show real products. Live AI recommendations and shopping data are still planned. Tax and shipping are excluded.

## Run
Requires Python 3.11 or newer. No third-party packages or API key are needed.

```bash
python -m src.server
```

Run that command from the repository folder, then open http://127.0.0.1:8000. Use `python3` if your computer uses that name. Press Ctrl+C to stop.

Optional UV commands: `uv sync`, then `uv run python -m src.server`.

## Tests

```bash
python -m unittest discover -s tests -v
```

There are 12 automated tests. See [test results and manual checks](docs/testing.md).

## Original feature plan
The original README listed 11 features. That list stays in [requirements](docs/requirements.md), including the advanced work that is still unfinished. The current tracked requirements are a proposed breakdown, not a recovered or approved HW2 baseline.

Sprint 2 will focus on size preferences, a small verified product list, saved outfits, cheaper alternatives, and one AI recommendation call if API access is available. Generated outfit images are a stretch goal. Any scope change needs instructor approval.

## Project files
- [Requirements and acceptance criteria](docs/requirements.md)
- [Architecture and design](docs/architecture.md)
- [Sprint 1 review and Sprint 2 plan](docs/progress.md)
- [User manual](docs/user-manual.md)
- [Individual Sprint 1 Review, Marp source](slides/sprint1-review.md)
- [Public HW4 evidence checklist](hw4/public-evidence.md)
- [Code](src) and [tests](tests)

## Official Canvas pages
- [Individual Project page](https://nku.instructure.com/courses/91834/pages/individual-project-page-of-basil-wazwaz)
- [Individual Progress page](https://nku.instructure.com/courses/91834/pages/individual-project-progress-page-of-basil-wazwaz-in-ase420)

Canvas is the official plan. GitHub holds the implementation and evidence. Canvas requires an NKU login. No public website is deployed yet. Private peer reviews are kept out of this repository.
