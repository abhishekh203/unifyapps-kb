# Assignment 02 — Morning Brief Automation

Status: PHASE A DONE ✅ (worker sends brief with emails + schedule PDF to own inbox, 2026-07-30).
Next: Phase B (runtime connections) + Phase C (schedule driver). Owner: Abhishekh.

## Hard-won gotchas (all confirmed 2026-07-30) — read before rebuilding
1. Gmail List Emails returns ONLY id+threadId → must Loop + Get message per id.
2. Loop-captured inner output is NOT exposed as pills → collect via Variable "Create list"
   (before loop) + "Add item to list" (inside loop) + read list after loop.
3. Loop **Iterable source** must be the ARRAY (`2 messages`), not a scalar (`2 Id`) — else 0 iterations.
4. Code by UnifyApps (WurkNow) output convention: set a global var **`result = {...}`** (NO `var`);
   sandbox does `{"result": result}`. Applies to BOTH JS and Python. Individual vars are ignored.
5. JS sandbox does NOT keep helper `function` declarations in scope → INLINE all logic (no funcs).
6. Top-level `return` is illegal in the sandbox (JS & Python) → assign to `result` instead.
7. Editor paste can inject leading whitespace → IndentationError; paste flush-left.
8. Gmail Send `To` & `Attachments` are list fields: single value in "Mapped List" mode yields
   NOTHING → use the "..." → Input Mode → **Fixed List** for a known single item.
9. Files "Upload file" Source is a RELATIVE path (no protocol) → don't attach by URL. Attach via
   **"Use binary content"** = node 9 `pdfBase64` (also keeps the brief private, no public URL).
10. Calendar `DATE()` didn't strip time → date range was now→now+24h (still worked); refine to true
    midnight/timezone later.
Progress (2026-07-29): Email half DONE & tested — List Emails → Loop(Capture Iterations=True)
→ Get message → Code (JS) extracting {subject, from, preview}. 0 errors.
Code gotcha: sandbox JS forbids top-level `return {...}` — assign vars named after output
schema fields instead (subject/from/preview); avoid `.find`/arrow fns (use for-loop, ES5-safe).

## Goal
Every morning, send each user a PDF "Morning Brief" = latest 5 Gmail emails + today's
full Google Calendar schedule, emailed to the user's own address. Each user sees ONLY
their own data via **runtime connection switching**.

## Architecture — TWO automations (why two?)
Runtime connection switching REQUIRES a **Callable** trigger (docs/automations/runtime-connection-switching.md, line 36).
But the task needs a **Schedule** (every morning). A schedule can't do runtime switching directly.
So: a Schedule "driver" calls a Callable "worker" once per user, passing that user's connections.

```
[Schedule 7AM]  morningBriefScheduler | Abhishekh   (driver)
      └── for each user → Call automation ──► morningBriefWorker | Abhishekh  (worker, Callable)
                                                     ├─ Gmail: List Emails (5)
                                                     ├─ Calendar: List Events (today)
                                                     ├─ Template: build HTML brief
                                                     ├─ Create PDF  ← CONFIRM mechanic
                                                     ├─ Files: base64 → file object
                                                     ├─ Gmail: Send Email + attach PDF
                                                     └─ Respond to automation
```

---

## Automation A — WORKER  `morningBriefWorker | Abhishekh`
Trigger: **Callable → "Trigger via automation"** (lets us define our own input+output schema).

### INPUT (Setup schema) — what the caller passes in
| Field | Type | Example | Purpose |
|---|---|---|---|
| `userEmail` | String | abhishekhkapar@gmail.com | where to send the brief |
| `gmailConnectionId` | String | conn_gmail_abc | runtime Gmail connection for THIS user |
| `calendarConnectionId` | String | conn_cal_xyz | runtime Calendar connection for THIS user |

### OUTPUT (Result schema) — what it returns to the caller
| Field | Type | Example |
|---|---|---|
| `status` | String | "sent" / "failed" |
| `message` | String | "Brief sent to abhishekhkapar@gmail.com" |

### Nodes (in order)
1. **Callable trigger** — define the input/output schema above.
2. **Dates (Variable/Formula by UnifyApps)** — compute:
   - `todayLabel` = e.g. "Tuesday, 29 Jul 2026" (for the header/subject)
   - `dayStart` = today 00:00 ISO, `dayEnd` = today 23:59 ISO (for the calendar query)
3. **Gmail → List Emails** — connection = runtime (`gmailConnectionId`), Query = `in:inbox`, Count = **5**.
   ⚠️ GOTCHA (confirmed 2026-07-29): List Emails returns ONLY `id` + `threadId` per message —
   NO subject/sender/preview. Must fetch each message separately.
3b. **Loop → For each loop** over `List Emails.messages`. Set **Capture Iterations = True**
    (so results collect into a list for the PDF). Iterable source = the `messages` array.
3c. **(inside loop) Gmail → Get a message** — Message ID = loop current item's `id`, Format = Full.
    Returns: `snippet` (preview, direct field) and `payload.headers[]` (array of {name,value};
    Subject/From live here).
3d. **(inside loop) Code by UnifyApps → Execute javascript** — extract clean fields.
    Inputs: `headers` = Get message → payload.headers; `snippet` = Get message → snippet.
    Outputs (String): `subject`, `from`, `preview`. Code finds header by name.
    ⚠️ BIG GOTCHA (2026-07-29): loop-captured inner-node output is NOT exposed as pills after
    the loop. Capture Iterations output only shows Index/Size/IsFirst/IsLast; no capture-value
    field; "Map from step" does nothing. So to COLLECT per-iteration results, use the list-variable
    pattern (per pdf-by-unifyapps doc): create empty list var BEFORE loop, add item INSIDE loop,
    read full list AFTER loop.
3e. **(before loop) Variable → create list var `emailList` = []**.
3f. **(inside loop, after 3d) Variable → add {subject,from,preview} to `emailList`**.
    Then node 7 Python reads `emailList` as `emails`.
4. **Google Calendar → List Events** — connection = runtime (`calendarConnectionId`),
   timeMin = `dayStart`, timeMax = `dayEnd`. Output per event: `summary` (title),
   `start`, `end`, `attendees`. (Exact field names TBD — confirm in builder.)
5. **Template by UnifyApps → Compile template** (type = Email/HTML) — build the brief:
   header with `todayLabel`, Section 1 = the 5 emails, Section 2 = the schedule.
   Output: `Compiled Content` (HTML string).
5b. **Calendar → List events** (node 6). Confirmed 2026-07-29 output paths per event in `Items[]`:
    `summary` (title), `start.dateTime`, `end.dateTime`, `attendees[].email` (+responseStatus).
    Input date range: Single events=True, Date from `=DATE(YEAR(NOW()),MONTH(NOW()),DAY(NOW()))`,
    Date to `+1`. GOTCHA: DATE() didn't strip time (showed now→now+24h) — refine to true midnight/tz later.
6. **Create the PDF** — DECIDED & DONE: PDF-by-UnifyApps only READS. PDF.co needs external key.
   USE **Code by UnifyApps → Execute python script** with a ZERO-DEPENDENCY pure-Python PDF
   generator (don't rely on pymupdf being installed). Inputs `emails`(Array<Object> from emailList
   list-var), `events`(Array<Object> from List events Items); output `pdfBase64`(String).
   ⚠️ PYTHON CONVENTIONS (confirmed 2026-07-30): (a) sandbox wrapper does `json.dump({"result":result})`
   at end → you MUST set a var named `result` (dict of outputs), e.g. `result={"pdfBase64": pdfBase64}`,
   else NameError. (Different from JS node which uses individual output vars.) (b) Editor paste can
   inject leading whitespace on line 1 → IndentationError; re-paste clean/flush-left. Test output:
   `{"result":{"pdfBase64":"JVBERi0xLjQK..."}}` = valid %PDF-1.4. ✅
7. **Files by UnifyApps → Upload file** — Option = Base64, File Name =
   `Morning-Brief-<todayLabel>.pdf`, MIME = `application/pdf`. Output: file object.
8. **Gmail → Send Email** — connection = runtime (`gmailConnectionId`),
   To = `userEmail`, Subject = `Your Morning Brief - <todayLabel>`,
   Body = short text, Attachment = file object from step 7.
9. **Callable → Respond to automation** — return `status` + `message`.

### Gmail Send Email — list fields gotcha (confirmed 2026-07-30)
`To` and `Attachments` are list-builder fields. Mapping a single value into "List Source"
produces NOTHING (field silently absent from request → "Recipient address required").
FIX: click the **"..."** on the field → **Input Mode → "Fixed List"** (for a known single
item) instead of "Mapped List". Then add the one item (To 1 = User Email). Same pattern for
a single attachment. "Mapped List" is only for iterating an actual upstream array.
Email sent OK end-to-end after this. ✅

### Settings tab (runtime switching)
- Enable **"Runtime user connections"** for Gmail + Google Calendar, then Save.
- Configure **Connection overrides** so `gmailConnectionId` / `calendarConnectionId` swap the defaults.
- Set a default (fallback) connection for each = your own account.

---

## Automation B — DRIVER  `morningBriefScheduler | Abhishekh`
Trigger: **Schedule → New recurring event**, daily 7:00 AM (or Cron `0 7 * * *`).

Steps:
1. Get the list of users (for v1: just you, hard-coded).
2. (Per user) **Standard Entities by UnifyApps → Get connection details** to fetch that
   user's Gmail + Calendar connection IDs.
3. **Call automation → `morningBriefWorker | Abhishekh`**, passing `userEmail`,
   `gmailConnectionId`, `calendarConnectionId`.

---

## Open items to confirm in the builder (need screenshots)
1. Google Calendar connector: exact action name for listing events + exact date-range field names.
2. PDF creation mechanic (step 6) — HTML→PDF action vs Code by UnifyApps base64.

## Build order (test each before next)
Phase A: build worker with YOUR own connection hard-coded, test end-to-end.
Phase B: turn on runtime user connections.
Phase C: build the schedule driver.
