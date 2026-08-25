# How-to: Data Table Pagination (Infinite Scroll + Page Based)

Confirmed in builder 2026-07-03. Applies to the Data Table component (Components → Rich → Data Table).

## Where pagination lives
Pagination is a TABLE ADD-ON — it does NOT exist by default. You must add it:
- Select table → **Content** tab → scroll to very bottom → **Add-ons** section → click **`+`** → select **Pagination**.
- After adding, a Pagination sub-panel opens (separate view, back arrow to return to Content).

## Pagination panel fields
- **Type**: `Scroll based` (infinite scroll) | `Page based` (numbered pages)
- **Page Size Mode**: `Fixed` (hardcoded) | `User Selectable` (user can change it)
- **Page Size**: number of rows per page/fetch (e.g. 20)
- **Initial Page**: which page to start on (default = 1, leave empty)
- **Total Records**: (Page based only) total row count — needed for page count display

## Type mapping to data source Paginate By

| Assignment requirement | Table Type | Data source Paginate By | Data source returns |
|---|---|---|---|
| Infinite scroll (Q1A) | Scroll based | CURSOR + Limit | objects[] + hasMore + cursor.next |
| Offset / numbered pages (Q1B) | Page based | OFFSET + Offset + Limit | objects[] + total count |

## Object mode vs Mapped mode
- **Object mode** (Source = Object → pick object): table manages fetching internally. Simplest for Q1.
  Pagination Add-on drives page size; table handles cursor/offset automatically.
- **Mapped mode** (Source = Mapped → pick a data source): developer must wire
  `Table > Content > Page > Page Size` and `Table > Content > Page > Offset` pills
  to the data source's inputs manually (per docs). More control, more setup.

## For Q1A (Infinite Scroll) — confirmed steps
1. Data source: Paginate By = **Cursor**, Limit = 20, object = product_inventory.
2. Table: Source = **Object → Product Inventory**, Primary Key = Id.
3. Table → Content → Add-ons → `+` → **Pagination** → Type = **Scroll based**, Page Size = 20.
4. Preview → scroll inside table → next 20 rows auto-load.
5. Table footer shows "Showing 1-20 of N rows".

## For Q1B (Offset / Page Based) — pattern (not yet confirmed)
1. Data source 2: Paginate By = **Offset**, Limit = 20, same object.
2. Table 2: Source = Object → Product Inventory, Primary Key = Id.
3. Table 2 → Add-ons → `+` → Pagination → Type = **Page based**, Page Size = 20.
4. Preview → shows page numbers / next-prev navigation.

## Gotchas
- "No Pagination in Add-ons" → it's not there by default. Must click `+` to add it.
- Pagination Add-on is a SEPARATE panel — clicking it opens a sub-view; use back arrow to return.
- "Scroll based" doesn't work in the builder canvas — only works in **Preview** mode.
- Page Size default was 30 — remember to change to 20 for Q1.
- In Object mode, setting Paginate By on the data source doesn't directly wire to the table —
  the table uses its own internal mechanism. The Pagination Add-on is what matters on the table.
