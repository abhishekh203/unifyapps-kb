# Assignment 01 — Data Sources & State Management

Training tenant: `https://employee-onboarding.uat.unifyapps.com`
Name suffix: append your name where asked (apps, callables).
Objects: ProductInventory → `…/object/product_inventory/records` · CustomerOrders → `…/object/customer_order/records`

**Status:** ⬜ not started  ·  Q-by-Q status in each section below.
Relevant local docs live in `../docs/` (see pointers per question). Verified builder steps → `../playbook/`.

---

## Q1 — Pagination Types & Filtering  🟡 (A done, B+C remaining)
**App:** "Product Catalog <name>" · **Page:** "Product Catalog" · **Object:** product_inventory

- **A. Infinite scroll:** storage-fetch data source on ProductInventory → Table block, infinite scroll, page size 20.
- **B. Offset:** a SECOND separate storage-fetch on the SAME object → second Table block, offset pagination, 20/page, mapped.
- **C. Filtering (one table):** built-in filter toolbar → map inputs to query → Category, Price Range (between), Search on Product Name.

Docs: `docs/applications/data-table.md`, `adding-data-sources.md`, `data-source-settings.md`, `map-data-to-interface-components.md`
Open Qs (confirm by screenshot): how toolbar filters bind to the query.

**Confirmed (UI, 2026-07-03):** In a Storage "Fetch records" data source, pagination type is set at the data-source level via **Page → Paginate By** (required). Options: **Cursor** and **Offset**.
- **Cursor** (fields: Cursor + Limit) → use for **A (infinite scroll)**. Leave Cursor blank; Table drives next-page cursor. Limit = page size (20).
- **Offset** (fields: Offset + Limit) → use for **B (offset pages)**. Leave Offset blank/0; Table drives offset. Limit = 20.
- `dataSource1` = Part A, Cursor/Limit 20. ✅ Save & Run verified: `objects[]` of product_inventory returned, `hasMore: true`. Playbook: `how-to-storage-fetch-datasource.md`.
- NEXT: build Table block bound to `dataSource1`, infinite scroll, page size 20.

## Q2 — Create & Delete Records  ⬜
**Page:** same "Product Catalog".

- **A.** "Create Product" button → modal form: Product Name (required), Category (**lookup dropdown** from a callable that returns all categories — not static), Price (number, required), Stock Count (number). Delete button in a table **action column**.
- **B.** On create/delete success → refresh **BOTH** table data sources from Q1. Optimize: parallel, **avoid waterfall**.

Docs: `docs/applications/modal.md`, `form-component.md`, `handle-interactions-in-interface.md`, `data-table.md` (action column), `adding-data-sources.md`
Open Qs: how to build the lookup widget from a callable; how to trigger two refreshes in parallel.

## Q3 — Callable with Repeatable Pagination  ⬜
**Page:** "Customer Orders" · **Object:** customer_order.

- **A.** Create callable **"getCustomerOrders | <name>"**: inputs status (string), customerName (string), pagination params → query CustomerOrders with filters + pagination → return paginated results + total count.
- **B.** **Repeatable** component shows: Order ID, Customer Name, Status, Order Date, Total Amount → infinite pagination controls.
- **C.** Filters: Status (**SingleSelect** block), Customer Name (**Text Input** block) → map to data source inputs.

Docs: `docs/applications/using-repeatable.md`, `repeatable.md`, `connect-to-data-source-callable-by-unifyapps.md`, `docs/automations/overview.md` (callables)
Open Qs: authoring a callable with pagination + total count; wiring repeatable infinite controls.

## Q4 — Displaying Metrics from Callable  ⬜
**Page:** "Sales Dashboard" · Callable: getSalesMetrics `…/automations/6910f7a0844c9e0c3c3559f1/preview`

- 4 **Stat Cards** showing the metrics from the callable. "Refresh" button re-triggers the data source.

Docs: `docs/applications/stat-card.md`, `multi-stat-card.md`, `connect-to-data-source-callable-by-unifyapps.md`

## Q5 — Automatic Navigation on Page Load  ⬜
**Pages:** "Access Gateway" + "Page A" + "Page B" · Callable: checkUserAccess `…/automations/691103be0102a73bb809b71c/preview`

- Page A: heading "Welcome to Page A". Page B: heading "Welcome to Page B".
- Access Gateway: NO UI. Data source calls checkUserAccess → returns `{ redirectTo: "PAGE_A" | "PAGE_B" }`.
- Run on page load; **success handler** → navigate to Page A or Page B accordingly. No clicks.

Docs: `docs/applications/handle-interactions-in-interface.md`, `pages.md`, `connect-to-data-source-callable-by-unifyapps.md`
Open Qs: how to auto-run a data source on page load; navigate action from a success handler.

## Q6 — Chained Data Sources  ⬜
**Page:** "Score Calculator" · Callables: getBaseScore + getBonusScore `…/6910fbe6844c9e0c3c3568b3/preview`; getFinalScore `…/6910fc6443683907c1473dbe/preview`

- Chain: getFinalScore ← getBonusScore ← getBaseScore.
- Number input (default 0) → passed to getBaseScore. Show final total in a **Typography** component.
- "Recalculate" button refreshes getBaseScore (cascades the chain).

Docs: `docs/applications/adding-data-sources.md`, `_concepts-data-sources-and-state.md` (chained section)
Open Qs: how to declare one data source's input as another's output (dependency).

## Q7 — Transform Results Feature  ⬜
**Page:** "Product Analytics" · **Object:** product_inventory (ALL records, no pagination)

- Data source queries all records → **Transform Results** computes: average price; total inventory value (Σ price×stockCount); category with most products; total number of products.
- Show the 4 values in **stat cards**. Comment the math in the transform function.

Docs: `docs/data/types-of-transformations.md`, `docs/data/overview.md` (Transform Results), `docs/applications/stat-card.md`
Open Qs: where the Transform Results editor lives; input/output shape.

## Q8 — Product Discovery with Dynamic Input  ⬜
**Page:** "Product Discovery" · Callable `…/automations/691107970102a73bb809c17e/preview`

- On load: auto-populate a **text input** "Product ID Search" with a random product ID from the callable.
- Show product details below the input for that ID.
- "Search" button → fetch details for a manually entered ID.

Docs: `docs/applications/handle-interactions-in-interface.md`, `connect-to-data-source-callable-by-unifyapps.md`, `form-component.md`
Open Qs: on-load populate of an input from a data source; manual re-trigger.

## Q9 — App-Level Data Sources  ⬜
**App (NEW):** "Multi-Page Demo | <name>" · Callables: getCounterValue `…/automations/69110…592ac/preview`; updateCounterValue `…/automations/69110b6e…d52d99/preview`

- **A.** App-level (not page-level) data source calling getCounterValue.
- **B.** Pages "Page A" + "Page B" both show the counter from the app-level source; nav buttons between them.
- **C.** "Increment Counter" on Page A → app-level data source calling updateCounterValue → on success refresh the app-level getCounterValue. Counter persists across navigation; `isLoading` should NOT re-fire on return.

Docs: `docs/applications/adding-data-sources.md`, `data-source-settings.md`, `_concepts-data-sources-and-state.md` (app-level + persistence)
Open Qs: creating an app-level vs page-level data source; how persistence avoids reload.

---

### Gotchas hit (promote reusable ones to ../playbook/)
_(empty — fill as we go)_

### Screenshots
_(saved in ../screenshots/assignment-01/ — link here as added)_
