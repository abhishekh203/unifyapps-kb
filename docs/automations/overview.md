# Unify Automations — Workflows & Callables

Source: https://www.unifyapps.com/docs/unify-automations · pulled locally.

## What it is
Low-code workflow/process automation. Automations are interconnected **nodes** (actions, logic,
data flow), triggered by events, running sequential or parallel steps that transform/validate/route data.

## Key nodes
- **Delay** — `Schedule Delay Until` (pause until a date/time) and `Set Delay Duration` (fixed interval).
- **Loop** — iterate over a collection.
- **Storage by UnifyApps** — persistent data store within a workflow (maintain state/history).
- **Analytics by UnifyApps** — SQL queries, aggregate metadata (sortable/filterable/searchable),
  Analytics Query (group/filter/projections; Count, Sum, Min/Max, % contribution), export CSV/XLS/XLSX,
  time-range queries.
- **Screen by UnifyApps** — user-interaction component.
- Triggers — event-driven (e.g. Razorpay "On payment"), webhook-style from connected apps.

## Callables (automations as data sources) — KEY for the assignment
An automation can be exposed as a **callable** that an app's data source invokes. A callable:
- **Accepts inputs** (e.g. `status`, `customerName`, pagination params).
- **Queries an object** with filters + pagination.
- **Returns** results, typically including a **total count** for pagination.

Callable URLs in the assignment look like:
`https://employee-onboarding.uat.unifyapps.com/p/0/automations/<id>/preview`

The app side creates a **data source that calls the callable**, maps inputs to it, and uses the
returned data (and success event handlers for navigation, refresh, etc.).

> Public docs are thin on exact callable input/output wiring → captured in `../playbook/` as we build.
