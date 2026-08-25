# How-to: Storage "Fetch records" data source (with pagination)

Reusable pattern for reading records from a UnifyApps **Storage** object into a page/app data
source. Confirmed in builder 2026-07-03 (Product Catalog, `product_inventory`).

## Create it
- Left rail → **Data** panel → under a page group (e.g. "Product Catalog") click **+** → gives a
  data source (e.g. `dataSource1`).
- App-level sources go under the **App** group instead (shared across pages). Page-level go under
  the page group.
- Tabs across the top: **App & Action → Input → Advanced**.

## App & Action
- App = **Storage by UnifyApps**, Action = **Fetch records** ("Fetch a list of records which
  satisfy the given filter conditions from a predefined object").

## Input tab — the fields that matter
- **Object*** (required) — pick the Storage object (e.g. `product_inventory`). Nothing works until
  this is set; panel looks empty otherwise. "View Object" opens it in a new tab.
- **Number of records to fetch*** — `Single` (one record) or `Multiple` (a list → tables/dropdowns).
- **Search records** — free-text: Fields + Value. For search bars.
- **Filter records** — `WHERE` conditions (Field / operator / Value), Condition Groups for AND/OR.
- **Sort records** — order fields.
- **Page → Paginate By*** (required) — the pagination TYPE, set HERE at the data-source level:
  - **Cursor** (fields: **Cursor** + **Limit**) → use for **infinite scroll**. Leave Cursor blank;
    the Table supplies the next-page cursor as the user scrolls. Limit = page size.
  - **Offset** (fields: **Offset** + **Limit**) → use for **numbered / offset pages**. Leave
    Offset blank/0; the Table drives the offset. Limit = page size.
- **Fields** — empty = fetch all; or pick a subset to make the query lighter.
- **Collapse** — group/dedup by a keyword field (one top doc per distinct value). Rarely needed.
- Flags (leave default unless needed): Include count of records (turn ON for total-count/pagination
  UI), Search from analytics store, Include current user permissions, role mappings, translations,
  Read through session variables.
- **Run Behaviour** — `Automatic` (runs when its block becomes visible — good for tables/lists) or
  `Manual` (only on explicit trigger — good for search-on-click / heavy queries).

## Advanced tab (defaults are fine for a read-into-table)
- Timing: Run query on page load / Refresh on window focus / Run query periodically.
- Trigger Conditions → Disable query (validate/prevent unnecessary requests) + Disabled error msg.
- Caching, Retry On Error (default ON: 1 retry, 1500ms, backoff ×2), Permissions.

## Verify
- Click **Save & Run** → **Output** tab shows the JSON. Look for:
  - `"objects": [ ... ]` with your records, each `"entityType": "<object>"`.
  - `"hasMore": true` → more pages exist (cursor/offset pagination working). A single-page data
    source is SUPPOSED to return only `Limit` rows here — endless scroll is the **Table's** job,
    not the data source's.

## Gotcha
- "It only shows 20, it's not scrolling" in the data-source Output is EXPECTED. The data source
  returns one page (= Limit). Infinite scroll / paging lives on the **Table block**, which re-calls
  the source with the next cursor/offset. See `how-to-table-infinite-scroll.md` (to be written).
