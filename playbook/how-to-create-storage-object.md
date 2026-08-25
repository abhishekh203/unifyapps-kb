# How-to: Create a Storage object (Objects Manager)

Reusable pattern for creating a new Storage object (schema + fields) in UnifyApps.
Confirmed in builder 2026-07-30 (Assignment 03, `LeaveBalance_Abhishekh`).
Sibling: `how-to-storage-fetch-datasource.md` (reading an existing object into a page).

## Where
Left rail → **Enterprise Resources → Objects Manager → New Object**
URL: `/p/0/objects/create`.

## Create-object screen (top → bottom)
- **Object name** (top row, next to the `+`) = the **singular** name. Drives auto-generated
  Plural + Unique ID.
- **Details**
  - **Plural name*** — used in lists/nav.
  - **Unique ID*** — auto-generated from singular; how the object is referenced in
    formulas/APIs/Tools. **Editable.** ⚠️ Must be globally unique in the tenant.
  - **About this object** — free text description.
- **Storage**
  - **Store data in*** — default **JSON Store** (fine for training/simple objects).
    ⚠️ Storage type can't be changed once the object has data.
  - **Retention period** — leave empty = keep records forever.
- **Organization** — Workspace / Tags, both optional.
- **Object features** — toggles (Enable reporting, Enable activity tracking, …). All reversible
  later from the Settings tab. Defaults fine.
- **Create object** (top-right) commits.

## GOTCHA — Unique ID collision on a shared tenant (confirmed 2026-07-30)
The training tenant is shared by many trainees. A plain Unique ID like `leave_balance` will
often already exist → red inline error **"Unique ID should be unique. Please enter a different
unique ID."** and Create is blocked.
FIX: suffix everything with your name. Object name `LeaveBalance_Abhishekh`, Plural
`LeaveBalances_Abhishekh`, Unique ID `leave_balance_abhishekh`. Matches the tenant naming
convention (apps/callables/objects suffixed with the user's name).
**Record the final Unique ID** — Storage Fetch/Create Tools & data sources reference it.

## After Create — define schema (fields)
Lands on **Edit Schema** (`/objects/<uniqueId>/schema`), "No fields defined yet" with two buttons:
**Use Code Snippet** and **+ Add Fields**.

### Fast path — Use Code Snippet (CONFIRMED 2026-07-30, RECOMMENDED)
The snippet dialog **infers the schema from a sample JSON record** (editor pre-seeds `{}`, an
object — not a field-definition array). Set dropdown = **JSON**, paste ONE representative row,
click **Use**. Unify creates a field per key and infers the type from the value:
quoted string → **Text** (icon `A`), bare number → **Number** (icon `±1`).
Example that produced EmployeeID/EmployeeName=Text, TotalAnnualLeaves/LeavesTaken=Number:
```json
{ "EmployeeID": "EMP001", "EmployeeName": "Alice Thomas", "TotalAnnualLeaves": 24, "LeavesTaken": 10 }
```
(Leave "Save as new snippet" unchecked. Existing sidebar snippets = unrelated prompt JSON, not schemas.)
NOTE: Date types are NOT inferred — a JSON date string ("2026-08-01") comes in as **Text** (`A` icon).
Fix after paste: click the field row → **Edit Field** panel → **Field Type** dropdown → pick **Date**
→ Save. (Type IS editable after creation via this panel — no delete/re-add needed. CONFIRMED 2026-07-30.)

### Edit Field panel (click a field row) — CONFIRMED 2026-07-30
Fields: **Key*** (the API/field name), **Display Label**, **Help Text**, **Field Type** (dropdown:
Text / Number / Date / … ), **Default value**, **Nest under**, checkboxes **Is Optional** /
**Primary Key** / **Unique Key**, plus **Advanced Settings**. This is where you change a field's
type post-creation.

### Edit Schema grid
Columns per field: **SEARCH · SORT · FILTER** (indexing toggles — speed up those query types) and
**OPTIONAL** (green check = not required). Enable **FILTER** on any field the agent/tool queries by
(e.g. `EmployeeID` for a Fetch-by-ID). **Save** (top-right) commits.

## Add records (CONFIRMED 2026-07-30)
Object → **Create Records** (`/object/<uniqueId>/records/create`). Dialog: "Create Records using
Form or JSON input". Paste a **JSON object OR array** — keys matching field names auto-map,
unmatched keys are skipped. Array = bulk insert all rows in one go. Click **Create**.
Example (5 rows at once):
```json
[
  { "EmployeeID": "EMP001", "EmployeeName": "Alice Thomas", "TotalAnnualLeaves": 24, "LeavesTaken": 10 }
]
```
