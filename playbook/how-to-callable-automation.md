# How-to: Build a Callable automation & call it from an app

Confirmed 2026-07-03 building `getCategories` (returns distinct categories for a lookup dropdown, Q2).

## Create the automation
- Go to the **Automations** section (separate from interfaces; app switcher → Automations).
- **New Automation** → name it `<verb><Thing> | <Name>` (e.g. `getCategories | Abhishekh`).

## Trigger — use "Trigger via automation" (NOT "Trigger interface")
Add Trigger → **Callable** → event type options:
- **Trigger interface** → ❌ WRONG for this. It forces a *predefined* Callable Interface contract
  (Publish Response, Call LLM Model, PII Mask, AI Agent Tool…). You can't define your own schema.
- **Trigger via automation** → ✅ RIGHT. Lets you define your OWN setup (input) + result (output) schema.
- Trigger via API → external API endpoint. Streaming → streaming responses.

Define **Result Schema** = your output fields (e.g. `categories`, type Array → Object or String).

## Distinct values via Collapse
To get distinct values of a field, use **Storage → Fetch records → Collapse → Field = <field>**
(returns one doc per distinct value). Set **Page → Limit** high enough (e.g. 100). Leave
Max concurrent group searches + Inner hits blank. NOTE: collapse dedupe can still show near-dupes
if the source data has case/whitespace variants or garbage values — clean app-side if needed.

## MUST add a response step (or Save errors)
A "Trigger via automation" callable REQUIRES a response node, else:
  "This automation has a trigger which expects response. Please add a step to send a response."
Add it: `+` below last node → search **"callable"** → Callable app → **"Respond to automation"**
("Returns data to the calling automation"). In it, map your Result Schema fields:
- For an array output: set **List Source** = the fetch node's `Objects` array, and **Items** =
  the per-element value (e.g. `properties.category` for a String array of category names).
- Field path gotcha: object fields live under `objects[].properties.<field>` (e.g. `properties.category`).

## Deploy + WORKSPACE must match the app  ← the big gotcha
The app's Callable data-source picker only lists automations that are:
1. **Deployed** (toggle ON / not Draft), AND
2. In the **same workspace as the app** (or global/blank).
Symptom: automation exists + is ON, but doesn't appear in the app's Automation dropdown.
Check the **Workspace** column in the Automations list — if it says `Abhishekh` but the app is
global (workspace `-`), MOVE the automation to global (row `⋮` → Move to workspace / Settings →
Workspace → global), then it appears in the picker.

## Call it from the app
Data panel → `+` → **Callable** → Call automation → Select Automation → pick it → Save & Run.
Output appears as `{{ <dsName>.data.<outputField> }}` (e.g. `getCategoriesAbhishekh.data.categories`).
Use as dropdown options: source = that array; for a string array, Label = Value = the item itself.
