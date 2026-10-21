# Sprint 1 review and Sprint 2 plan

Prepared October 20, 2026. This is the current implementation snapshot. It does not backdate new code to Course Weeks 5-8.

## Sprint 1 metrics
- Implementation LoC: 153 nonblank lines, comprising 73 Python and 80 HTML/CSS/JavaScript lines.
- Test LoC: 64 nonblank Python lines.
- Method: count nonblank lines in `src/*.py`, `web/*`, and `tests/*.py`. Comments and markup count. Dependencies, documents, and lockfiles do not.
- Available feature baseline: 11 from the September 13 README. Separate HW2 approval unavailable.
- Proposed current scope: 11 features and 12 testable requirements.
- Completed: 5/11 features (45.5%) with sample data limits, and 7/12 requirements (58.3%).
- Remaining: 6 features and 5 requirements.

## Course Weeks 5-8 and burndown

| Checkpoint | Remaining requirements | Evidence |
|---|---|---|
| Sprint start | Not recorded | HW2 requirement baseline unavailable |
| End of Week 5 | Not recorded | No weekly implementation record supplied |
| End of Week 6 | Not recorded | No weekly implementation record supplied |
| End of Week 7 | Not recorded | No weekly implementation record supplied |
| End of Week 8 | Not recorded | No verified weekly snapshot supplied |
| October 20 current snapshot | 5 of the proposed 12 | Current code and tests |

The available earlier history contains a README plan. It does not support a weekly numeric burndown. These missing records should be discussed with the instructor rather than filled with estimated accomplishments.

## Retrospective
What went well: The idea has a clear use case. A small sample catalog makes it possible to test the form and budget rules without API access.

What went wrong: The original plan included AI images, product search, and several filters before there was a working base. The repository also lacked weekly progress evidence.

Cause and improvement: The scope was too broad for the first version. Keep the next tasks small, commit each working step, and update Canvas every week. Ask the instructor to confirm the proposed requirement breakdown and any scope changes.

Design learning: Separate the recommendation rules from the server. This keeps the functions easier to test and explain. Evidence: [recommendation code](https://github.com/basilwaz/AI-Fashion-Assistant/blob/main/src/recommendations.py), [HTTP code](https://github.com/basilwaz/AI-Fashion-Assistant/blob/main/src/server.py), and [design notes](https://github.com/basilwaz/AI-Fashion-Assistant/blob/main/docs/architecture.md).

## Sprint 2 plan
- MVP goal: turn the sample prototype into a small usable outfit tool with fit preferences, checked product links, favorites, and cheaper alternatives.
- Design improvement: keep catalog rules separate and place a future AI call behind one provider function.
- Quality goal: keep tests passing, finish the manual, and record weekly evidence.
- Planned remaining work: 6 original features and 5 proposed requirements. AI previews are a stretch goal and require a scope discussion.

| Course weeks | Planned work | Evidence target |
|---|---|---|
| 9-10 | Add fit preferences and a small verified product catalog. Try one AI recommendation call if credentials are available. | R8-R10 code and tests |
| 11-12 | Add favorites and cheaper alternatives. Improve the provider fallback and browser layout. | R11-R12 tests and weekly report |
| 13 | Run acceptance checks, finish documents, and publish an initial GitHub Pages information site. | Test record, manual, site link |
| 14-15 | Fix problems, complete the final evaluation files, and prepare the final review. Attempt image previews only if core work is done. | Final demo, tests, and documents |

Use Canvas for exact dates. These course-week targets are planning guidance, not claims about work already done.

## Publication and review evidence
- [Slides](https://github.com/basilwaz/AI-Fashion-Assistant/blob/main/slides/sprint1-review.md)
- [Commit history](https://github.com/basilwaz/AI-Fashion-Assistant/commits/main/)
- [Canvas Project page](https://nku.instructure.com/courses/91834/pages/individual-project-page-of-basil-wazwaz)
- [Canvas Progress page](https://nku.instructure.com/courses/91834/pages/individual-project-progress-page-of-basil-wazwaz-in-ase420)

The exact HW4 deadline was not provided. The three-day publication rule cannot be marked complete until the deadline and actual Canvas link date are checked. Publication timestamps remain visible in GitHub history. Canvas edits still need to be pasted by Basil.
