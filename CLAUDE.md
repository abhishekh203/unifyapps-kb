# CLAUDE.md — UnifyApps Learning & Build Project

Read this first, every session — then read **`MEMORY.md`** (repo-based memory: durable lessons,
procedures, quirks). Durable lessons go into `MEMORY.md` in the repo, NOT machine-local memory,
so they travel with the repo on GitHub.

## What this is

A workspace for **building real client solutions on the UnifyApps platform**. UnifyApps is an
enterprise "Horizontal AI Operating System" — a low-code/no-code platform to build apps,
automations, data pipelines, AI agents, and integrations. Docs: https://www.unifyapps.com/docs

The learning phase (onboarding assignments) is **done** — `assignments/` and `playbook/` stay
as reference material built during it.

We work in the **UnifyApps builder** — the tenant/URL varies by project (the user provides it;
e.g. the old training tenant was `employee-onboarding.uat.unifyapps.com`).

## Your role (important — read this)

**You (Claude) drive the builder yourself via the Claude in Chrome extension.** The old
"user is the hands, Claude gives steps, user shares screenshots" loop is RETIRED (2026-08-25).
The docs mirror is complete, so the new loop is:

1. The user picks a task (assignment or client work).
2. **You do it directly in the browser** via Claude in Chrome, grounded in `docs/` + `playbook/`.
3. The user only steps in for things you genuinely cannot do in the extension
   (e.g. logins/2FA) — and you say exactly what you need.
4. When you solve something non-obvious, **write the how-to into `playbook/`** as before.

**Do NOT save new screenshots.** `screenshots/` is a frozen archive of the old learning loop —
existing files stay (playbook/assignments reference them), but nothing new goes in.
`playbook/` and `notes/` remain the living learning assets.

## Builder AI (use these before building manually)

The UnifyApps builder has built-in AI that should do the heavy lifting — prefer prompting it
over hand-building from scratch:

- **AI FDE tool** — an AI chat interface inside the builder (**✦ AI FDE button, top-right of
  the builder chrome**; opens a right-side chat panel with attach + voice input and
  context-aware suggestions — full details: `playbook/how-to-ai-fde.md`). Two uses:
  1. **Fallback Q&A**: if `docs/` + `playbook/` don't answer a platform question, ask AI FDE
     in the builder chat (before going to the public internet).
  2. **It builds things from prompts**: object schemas, inserting/managing records and other
     object-related work, and entire automations. Write a good prompt, let it build, then verify.
- **Text-to-Automation** — builds a whole automation from a single prompt.
- **Text-to-Application** — builds a whole application from a single prompt.
- **Text-to-Agent** — the AI Agents section is prompt-first too ("Describe. Build. Deploy." —
  an "Ask anything…" box builds the agent from one prompt; manual fallback: Simple Agent /
  Advanced Agent / Workflow Agent).

So the default build flow is: craft the prompt → let the builder AI generate → review/fix the
result manually only where it falls short. Capture good prompts + AI FDE quirks in `playbook/`.
Tenant seen in client work: `tool.prod-aps1.unifyapps.com` (agent builder at
`/p/0/ai-agents/…`).

## How to answer (rules)

- **Local-first.** Always read `docs/` and `playbook/` before answering. Do NOT go online for
  info we already have saved.
- **Find pages via `docs/MANIFEST.md` first** (curated index + topic quick-jump for all 388
  conceptual pages) — jump to the right file instead of grepping. Then open only that file.
  Connector pages live in `docs/integrations/` — find those via `docs/integrations/INDEX.md`.
- **The entire docs site is mirrored locally** (last full refresh: 2026-08-25, incl. all 288
  connectors). Don't fetch pages online — read the local copy. To refresh the mirror:
  `.venv/bin/python scripts/scrape_docs.py --force --connectors`.
- **Answer-lookup ladder:** `docs/` (via MANIFEST) → `playbook/` + `notes/` → ask the **AI FDE
  tool** in the builder chat → only then the public internet. Do not ask the user for
  screenshots anymore; if you need to see the UI, look yourself via Claude in Chrome.
- After solving something non-obvious, **write it to `playbook/`** AND, if it's a durable lesson,
  to project memory. Don't make the user re-explain.

## Folder map

```
unifyapps/
├── CLAUDE.md            ← this brief (loaded every session)
├── docs/                ← local copy of UnifyApps official docs (pulled, saved)
│   ├── 00-index.md      ← map of everything + source URLs (all sections fully mirrored)
│   ├── applications/    ├ automations/  ├ data/  ├ agentic-ai/
│   ├── integrations/    ├ embedded-integrations/  ├ platform-tools/  ├ governance/
│   └── _concepts-data-sources-and-state.md  ← assignment-critical concepts, consolidated
├── playbook/            ← THE GOLD: reusable "how to do X in the builder", built from doing
├── assignments/         ← one file per assignment question; steps, status, gotchas
│   └── README.md        ← index of the 9-question onboarding assignment
├── projects/            ← REAL CLIENT APPS (not onboarding). One folder per app: README.md
│   │                      (task breakdown, owners, decisions) + data-model.md (objects/fields).
│   ├── itc-happay-claims-app/  ← ITC Happay Claim App, Workspace Dashboard build
│   └── tricon-ai-work-order-management/  ← Tricon AI work-order/bid analysis (Orbit)
├── screenshots/         ← FROZEN archive (old learning loop) — referenced, but add nothing new
└── notes/               ← scratch, questions, decisions
```

## Current work

**Onboarding assignments: DONE.** Now on **real client projects** — one folder per app in
`projects/` (README.md = task breakdown/owners/decisions, data-model.md = objects/fields).
- Active: **`projects/tricon-ai-work-order-management/`** — Tricon AI Work Order Management
  (Orbit app `tricon-uc-2` + agent; discovery pending) — and
  **`projects/itc-happay-claims-app/`** — ITC Happay Claim App, Workspace Dashboard build.
  Both on tenant `orbit.uat.unifyapps.com`.
- Reusable builder how-tos still go to `playbook/` (one pattern per file), not into project folders.
- Assignment archive: `assignments/` (`assignment-NN-<slug>.md`, index in `assignments/README.md`).

## Conventions

- Naming in the builder follows the client/project convention (assignment-era: suffixed with the user's name).
- Keep playbook entries narrow: one reusable pattern per file (e.g. `how-to-storage-fetch-datasource.md`).
- Keep each project's `README.md` (tasks/decisions) and `data-model.md` honest as the build progresses.
