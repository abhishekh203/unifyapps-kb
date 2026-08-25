# Assignment 03 — Leave Management AI Agent

Status: PLANNING (2026-07-30). Owner: Abhishekh.

## Goal
An AI agent (chat) that: reads leave balance from a **Leave Balances** object, collects a new
leave request via conversation, inserts a row into a **Leave Application** object, and emails a
confirmation via Gmail. Tools = 2 objects (read/create) + Gmail (send).

## Architecture (agent = Tasks + Tools)
Agent building blocks (from create-an-ai-agent.md): Knowledge, Tasks (journeys), Tools (actions),
Prompts (instructions), Guardrails. For this we mainly need **Tasks + Tools + a system prompt**.

Tools (direct connector actions, per configure-tools.md — no separate automations needed):
1. **Storage → Fetch records** on `LeaveBalances` (read a balance by EmployeeID).
2. **Storage → Create record** on `LeaveApplication` (insert a leave request).
3. **Gmail → Send Email** (confirmation).

## Data model (Step 1 — build first)
### Builder path (CONFIRMED 2026-07-30, screenshot)
Left rail → **Enterprise Resources → Objects Manager → New Object** (`/p/0/objects/create`).
Create-object screen fields: **Object name** (top = singular) · Details(**Plural name***, **Unique ID***
auto-gen from singular — NOTE the value, Tools reference it, About) · Storage(**Store data in*** =
JSON Store default; **Retention period** = leave empty=forever) · Organization(Workspace/Tags optional)
· Object features (reporting/activity-tracking toggles, default off). Then **Create object** (top-right)
→ next screen = add fields (screenshot pending).
Naming: suffix `_Abhishekh` (shared tenant). Objects = `LeaveBalance_Abhishekh` /
`LeaveApplication_Abhishekh`.

### Object: LeaveBalances  (populate ≥5 dummy rows)
- EmployeeID (String) e.g. EMP001
- EmployeeName (String) e.g. Alice Thomas
- TotalAnnualLeaves (Number) e.g. 24
- LeavesTaken (Number) e.g. 10
(Remaining = Total - Taken, computed by the agent, not stored.)

### Object: LeaveApplication  (schema only, 0 rows)
- EmployeeID (String)
- LeaveType (String) — Annual/Sick/Casual
- StartDate (Date)
- EndDate (Date)
- Reason (Text)

## Build progress (CONFIRMED 2026-07-30)
- Object #1 `LeaveBalance_Abhishekh` (uid `leave_balance_abhishekh`) DONE ✅ — 4 fields
  (EmployeeID/EmployeeName=Text, TotalAnnualLeaves/LeavesTaken=Number), FILTER on EmployeeID, 5 rows.
- Object #2 `LeaveApplication_Abhishekh` (uid `leave_application_abhishekh`) DONE ✅ — 5 fields
  (EmployeeID/LeaveType/Reason=Text, StartDate/EndDate=Date via Edit Field→Field Type), 0 rows.
- Agent `LeaveManagementAgent_Abhishekh` created; Role/Goal/Instructions set (prompt-driven validation).
  Config left-panel sections: Instructions · Knowledge · Tools · Skills · Capabilities · Tasks ·
  Memory · Models · Guardrails. Also has Conversation starters. Top: Preview / Publish; Configuration/
  Deployments/Observability tabs. URL `/ai-agents/<id>/configuration/instructions`.
- Phase 3 Tools (agent-tool pattern = leave input blank → agent fills; guided by Context→Description):
  - T1 "Get leave balance by EmployeeID" = Storage Fetch records, obj LeaveBalance, Single,
    filter EmployeeID Equals to <blank>. ADDED ✅
  - T2 "create leave application" = Storage Create record, obj LeaveApplication, 5 field boxes blank. ADDED ✅
  - T3 "Send leave confirmation email" = Gmail Send email. To* is a LIST field (To List Source +
    Items) w/ "..." Input Mode toggle = Assignment-02 gotcha. Left To List Source blank (agent fills),
    Email type=Text, From blank (uses connected acct = sender). ⚠️ VERIFY To in Preview; fallback =
    "..." → Fixed List.
- ⚠️ AI Preview/runtime was NOT working 2026-07-30 → could not verify any tool. Test all when it's back.
- NEXT: Phase 4 Tasks (Check balance / Apply for leave journeys), then test checklist.

## Agent functional flow (the 4 steps → map to Tasks)
- Task A "Check leave balance": user asks remaining leaves → Fetch from LeaveBalances by EmployeeID →
  reply "Total X, Taken Y, Remaining Z". If no record → ask for correct ID / say not found.
- Task B "Apply for leave": collect StartDate, EndDate, LeaveType, Reason, EmployeeID (clarify any
  missing). Validate requested days <= remaining, else reject & re-prompt. On confirm → Create record
  in LeaveApplication → show summary.
- Task C "Email confirmation": if user agrees → Gmail Send Email with the leave details.

## Testing checklist (from assignment)
- Query balance for unknown ID → ask for correct ID / "no record found".
- Request more days than available → reject, prompt for new input.
- Missing dates → ask for start & end before creating.
- Leave Application row actually inserted.
- Confirmation email delivered with correct details.

## Build order
1. Create the 2 Storage objects; seed LeaveBalances with 5 rows.
2. Create the AI Agent; add system prompt (role + rules).
3. Add Tools: Fetch LeaveBalances, Create LeaveApplication, Gmail Send.
4. Write Tasks + instructions wiring the flow + validations.
5. Test each checklist item in a chat session.

## Reuse from assignment 02
- Gmail Send Email connection + gotchas (To = Fixed List, etc.) — see assignment-02.
- Storage objects pattern — see playbook/how-to-storage-fetch-datasource.md.

## Open items to confirm in builder (screenshots)
- Exact path to create a Storage object + add fields + add records.
- How the agent tool config maps object fields ↔ agent-collected values.
- Whether validation (days <= remaining) lives in the prompt/instructions or a tool.
