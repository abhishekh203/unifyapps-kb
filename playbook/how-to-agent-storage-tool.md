# How-to: Add a Storage action as an AI Agent Tool

Confirmed in builder 2026-07-30 (Assignment 03, LeaveManagementAgent). Sibling docs:
`how-to-create-storage-object.md`, `how-to-storage-fetch-datasource.md`.

## Where
Agent → Configuration → **Tools** (left panel) → **Add tool** → pick app **Storage by UnifyApps**
→ **Select an action** (searchable list: Fetch records, Fetch record by ID, Create record,
Delete records, Export records, Get records by IDs, …) → check one → **Add** → opens **Configure tool**.

Action choice for common needs:
- Read by a FIELD value (e.g. EmployeeID) → **Fetch records** + a filter. (NOT "Fetch record by ID"
  — that needs the internal `e_…` record id the agent won't know.)
- Insert a row → **Create record**.

## Configure tool — three tabs
- **Input** — the query shape:
  - **Object*** — the Storage object (by display name; "View Object" opens it to confirm the uid).
  - **Number of records to fetch** — Single / Multiple.
  - **Search records** (free-text Fields+Value) / **Filter records** (WHERE Field / operator / Value,
    Add Condition/Group/Filter) / **Sort** / **Fields**.
- **Controls** — execution policies only (Require approval before execution, Governance rules,
  Total Invocation Cost, Rate Limit, Cache). NOT input mapping.
- **Context** — what the AGENT sees & uses to decide calls:
  - **Name** — short tool name.
  - **Description** — the LLM uses this to decide when/how to call. Put the intent + which value(s)
    the agent must supply here.
  - **Tool output** — Send full / partial response; shows the output schema (Fetch: Objects[Array],
    Has More[Bool], Cursor{Next,Previous}, Inner Hits[Array]).

## KEY MECHANIC — how the agent passes dynamic values (CONFIRMED 2026-07-30)
There is **no** dynamic pill / `{{ }}` picker / AI toggle in the Input Value fields (typing `{{`
exposes nothing). The pattern is: **leave the input blank → the agent fills it at runtime.**
Anything you TYPE becomes a FIXED value; anything left EMPTY becomes an agent-provided parameter,
guided by the tool's **Context → Description**. So for "fetch balance by EmployeeID":
Filter = `EmployeeID` `Equals to` `<blank>`, and Description says "pass the EmployeeID the user gave".
⚠️ VERIFY via agent **Preview** that the agent actually populates the blank (risk: blank could be
read as empty-string match). Test one tool before replicating the pattern.

## Finish
**Add tool** (bottom-right) commits it into the agent's Tools list.

## Tools are a SHARED POOL (CONFIRMED 2026-07-30)
Tools added anywhere (agent-level Tools section OR via a Task's "Add Tool") join one shared pool.
Every Task's **Tools** table auto-lists ALL pool tools with a per-task **ON/OFF toggle** (columns:
ON · TOOL · APP · INPUTS · APP-conn). So you do NOT reconfigure tools per task — just toggle which
ones that task may use. "Add Tool" in a task = add a NEW tool to the pool (raw connector catalog),
not required to reuse existing ones.
