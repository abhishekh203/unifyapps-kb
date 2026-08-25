# Playbook — How to actually do things in the UnifyApps builder

**This is the gold.** The official docs say *what* features exist; this folder says *how* to do
them in the real builder — exact click-paths, panel names, gotchas — captured from doing the
assignments and the user's screenshots.

## Rules
- One reusable pattern per file. Narrow scope. Name `how-to-<thing>.md`.
- Each entry: **Goal → Steps (with exact UI labels) → Gotchas → Screenshot refs → Verified? (date)**.
- Mark `Verified ✅` only after a screenshot/the user confirms it worked. Until then `Draft ⏳`.
- When a step turns out wrong, fix it in place — keep the playbook truthful.

## Planned entries (filled as we hit them)
| File | Covers | Assignment | Status |
|------|--------|-----------|--------|
| `how-to-create-app-and-page.md` | new app + page | Q1, all | ✅ verified 2026-07-03 |
| `how-to-storage-fetch-datasource.md` | storage fetch records on an object | Q1, Q2, Q7 | ⏳ |
| `how-to-table-infinite-scroll.md` | Table block + infinite scroll, page size 20 | Q1A | ⏳ |
| `how-to-table-offset-pagination.md` | Table block + offset pagination | Q1B | ⏳ |
| `how-to-table-filter-toolbar.md` | built-in filter toolbar → query (category, price range, search) | Q1C | ⏳ |
| `how-to-create-button-and-modal-form.md` | Create button → modal form | Q2A | ⏳ |
| `how-to-lookup-widget-from-callable.md` | dynamic dropdown from callable | Q2A | ⏳ |
| `how-to-table-action-column-delete.md` | row delete action | Q2A | ⏳ |
| `how-to-refresh-datasources-parallel.md` | refresh both, no waterfall | Q2B, Q9 | ⏳ |
| `how-to-create-callable.md` | author a callable with inputs + pagination + total count | Q3A | ⏳ |
| `how-to-repeatable-pagination.md` | repeatable + infinite controls | Q3B | ⏳ |
| `how-to-filter-blocks-to-callable.md` | SingleSelect + Text Input → callable inputs | Q3C | ⏳ |
| `how-to-stat-cards-from-callable.md` | 4 stat cards + refresh button | Q4 | ⏳ |
| `how-to-autorun-onload-and-navigate.md` | run on page load + conditional nav | Q5, Q8 | ⏳ |
| `how-to-chained-datasources.md` | dependent data sources | Q6 | ⏳ |
| `how-to-transform-results.md` | Transform Results editor | Q7 | ⏳ |
| `how-to-app-level-datasource.md` | app-level data source + persistence | Q9 | ⏳ |

## Platform / general (client-project era)
| File | Covers | Status |
|------|--------|--------|
| `how-to-ai-fde.md` | AI FDE assistant (chat panel, prompt-building) + text-to-app/automation/agent | ✅ from live UI 2026-08-25 |

Add new files freely — this list is a starting map, not a cage.
