---
marp: true
size: 4:3
paginate: true
theme: default
---

# AI Fashion Assistant
## Sprint 1 Review and Sprint 2 Plan

Basil Wazwaz
ASE 420
October 20, 2026
AI-Assisted Development

---

# Problem and goal

Finding an outfit within a budget can take time.

My goal is to let a user enter preferences, compare outfits, and see what each outfit costs.

The first version uses a small sample catalog. Live AI and real shopping data are still planned.

---

# Working prototype demo

1. Run `python -m src.server`.
2. Open `http://127.0.0.1:8000`.
3. Choose $70, Casual, Everyday.
4. The sample Budget casual outfit costs $67.
5. Try $10 to see an empty result.

Show the form, item prices, and total during the live demo.

---

# Current metrics

- Implementation: 153 nonblank lines.
- Tests: 64 nonblank lines, 12 passing tests.
- Features: 5/11 complete, 45.5%.
- Requirements: 7/12 complete, 58.3%.
- Remaining: 6 features and 5 requirements.

Brands and prices are sample data. The 12 requirements are a proposed breakdown. HW2 approval is unverified.

---

# Weekly progress and burndown

Weeks 5-8 have no verified weekly counts in the available history. The earlier repository contained a README plan.

The October 20 snapshot has 5 remaining proposed requirements. This new work is not an end-of-Week-8 snapshot.

I need to keep weekly commits and update Canvas so the next review has a real burndown record.

---

# Sprint 1 retrospective

What went well: The basic budget flow is small enough to test without API access.

What went wrong: The first plan included too many advanced features before a working base existed.

Improvement: Finish one small feature at a time and record the result each week.

---

# Design learning

The page handles input and display. The server handles requests. The recommendation module handles outfit rules.

This follows single responsibility. I can test budget rules without starting the server.

Catalog data avoids repeated style branches. Short input checks are still useful. This is the first implementation, so no earlier refactor is claimed.

---

# Sprint 2 MVP and design

- Add fit preferences and checked products.
- Save favorite outfits and find cheaper alternatives.
- Try an AI call using known catalog items.
- Keep local rules as a fallback.
- Keep API keys on the server.

Generated outfit images are a stretch goal. Confirm scope changes with the instructor.

---

# Testing plan

Unit: budget rules now, then fit and favorite rules.

Integration: HTTP flow now, then storage and AI provider flow.

Regression: rerun all 12 tests after changes.

Acceptance: finish browser checks, verify product links, and test AI failures. Browser acceptance is still pending.

---

# Sprint 2 timeline

- Weeks 9-10: preferences, verified catalog, initial AI work.
- Weeks 11-12: favorites, alternatives, tests, layout.
- Week 13: acceptance checks, documents, Pages site.
- Weeks 14-15: fixes, final demo, and submission.

Check Canvas for exact dates. GitHub Pages will host project information, not the Python server.

---

# Evidence and remaining checks

[Repository](https://github.com/basilwaz/AI-Fashion-Assistant)
[Metrics and plan](https://github.com/basilwaz/AI-Fashion-Assistant/blob/main/docs/progress.md)
[Test record](https://github.com/basilwaz/AI-Fashion-Assistant/blob/main/docs/testing.md)

Paste the prepared Canvas pages and verify the links. Confirm the HW4 deadline before checking the three-day publication item.

Be ready to explain and reproduce at least 80% of the work without AI.
