# Concepts — Data Sources & State Management (assignment-critical)

Consolidated from the UnifyApps docs + the assignment text. These are the ideas Q1–Q9 test.
Exact builder click-paths are confirmed/filled in `../playbook/` as we do each question.

## Data sources
A **data source** feeds data to UI components. Two creation scopes:
- **Page-level** — scoped to one page.
- **App-level** — shared across all pages (use for persistent state, e.g. a counter that survives navigation).

Kinds relevant here:
- **Storage Fetch Records** — queries an **object** (e.g. `product_inventory`, `customer_order`).
  Supports pagination + filtering. (Q1, Q2, Q7.)
- **Callable** — calls an automation exposed as a callable (URL `.../automations/<id>/preview`).
  Takes inputs, returns data (often with total count). (Q3, Q4, Q5, Q6, Q8, Q9.)

Data sources have **event handlers** — e.g. **on success** → run navigation, refresh another data
source, set a value. (Used in Q5 conditional nav, Q2 refresh, Q9 refresh.)

## The 3 pagination styles (Q1, Q3)
1. **Infinite scroll** — Table block keeps loading more as you scroll; configure page size (e.g. 20).
2. **Offset-based** — Table block with page numbers; offset + limit (e.g. 20/page).
3. **Repeatable pagination** — manual pagination built on the **Repeatable** component + a **callable**
   that accepts pagination params and returns `{ results, totalCount }`. (Q3 — "infinite pagination
   controls for the repeatable".)

A single object can back multiple data sources with different pagination — Q1 uses TWO separate
storage-fetch data sources on the SAME `product_inventory` object (one infinite, one offset).

## Filtering (Q1C, Q3C)
- **Table built-in filter toolbar** — the table's top toolbar; map toolbar filter inputs → data-source
  query inputs. Q1 wants: Category filter, Price Range (between), Search on Product Name.
- **Standalone filter blocks** — SingleSelect + Text Input blocks whose values map to a callable's
  inputs (Q3: Status = SingleSelect, Customer Name = Text Input).

## Lookup widget (Q2)
A dropdown whose options come from a **callable data source** (dynamic), not a static list.
Q2: Category dropdown = lookup, backed by a callable returning all categories.

## Refreshing data sources & avoiding waterfall (Q2B, Q6, Q9)
- On create/delete success → **refresh** the data sources backing the tables.
- **Avoid waterfall**: refresh both in parallel, not one-after-the-other (don't chain refreshes that
  could run concurrently).
- **Chained/dependent data sources** (Q6): when one genuinely depends on another's output, chain them
  intentionally — getFinalScore ← getBonusScore ← getBaseScore.

## Transform Results (Q7)
Data-source feature to compute derived values from query results in code (avg, sum of price×stock,
group-by category, count) → feed stat cards. Comment the math.

## Auto-run on page load + conditional navigation (Q5, Q8, Q9)
- A data source can **run automatically on page load** (no button).
- Q5: on-load callable returns `{ redirectTo: "PAGE_A" | "PAGE_B" }`; success handler navigates accordingly. No UI.
- Q8: on-load callable returns a random product ID → populate a text input → show details; plus manual search.

## State persistence across pages (Q9)
App-level data source holds a value (counter) that **persists** across page navigation — `isLoading`
should NOT re-trigger when returning to a page if the app-level source already has the value.
