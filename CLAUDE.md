# CLAUDE.md — UnifyApps Learning & Build Project

Read this first, every session. This is the brief for working in this folder.

## What this is

A workspace for learning the **UnifyApps** platform by doing its onboarding assignments,
and (later) building real solutions for clients on it. UnifyApps is an enterprise
"Horizontal AI Operating System" — a low-code/no-code platform to build apps, automations,
data pipelines, AI agents, and integrations. Docs: https://www.unifyapps.com/docs

The builder we work in is the training tenant: `https://employee-onboarding.uat.unifyapps.com`

## Your role (important — read this)

**I (the user) am the hands; you (Claude) are the brain + memory.** You cannot click inside
the UnifyApps builder — it is an authenticated web app you have no access to. So the loop is:

1. The user picks an assignment task.
2. You give **exact, step-by-step builder instructions** grounded in `docs/` + `playbook/`.
3. The user does it, hits a wall, and **shares a screenshot** (saved in `screenshots/`).
4. You read the screenshot, correct the steps to match the real UI.
5. When it works, you **write the canonical how-to into `playbook/`** so it's instant next time.

**We learn on the process.** The official docs are conceptual and do NOT show click-by-click
builder steps. The real "how" only emerges from doing the assignments + the user's screenshots.
That knowledge lives in `playbook/` and grows every session. The playbook is the valuable asset.

## How to answer (rules)

- **Local-first.** Always read `docs/` and `playbook/` before answering. Do NOT go online for
  info we already have saved.
- **Find pages via `docs/MANIFEST.md` first** (curated index + topic quick-jump for all 361 pages) —
  jump to the right file instead of grepping. Then open only that file.
- **Fetch-once-and-save.** If you genuinely need a page we don't have (e.g. a specific connector,
  or the Agentic-AI deep pages), fetch it ONCE, save it under `docs/`, then use the local copy
  forever. Never re-fetch what's already saved.
- When the docs don't cover the exact builder mechanic (common), say so plainly, give your best
  step-by-step, and **ask for a screenshot** to confirm — then update `playbook/`.
- After solving something non-obvious, **write it to `playbook/`** AND, if it's a durable lesson,
  to project memory. Don't make the user re-explain.

## Folder map

```
unifyapps/
├── CLAUDE.md            ← this brief (loaded every session)
├── docs/                ← local copy of UnifyApps official docs (pulled, saved)
│   ├── 00-index.md      ← map of everything + source URLs + what's saved vs fetch-on-use
│   ├── applications/    ├ automations/  ├ data/  ├ agentic-ai/
│   ├── integrations/    ├ embedded-integrations/  ├ platform-tools/  ├ governance/
│   └── _concepts-data-sources-and-state.md  ← assignment-critical concepts, consolidated
├── playbook/            ← THE GOLD: reusable "how to do X in the builder", built from doing
├── assignments/         ← one file per assignment question; steps, status, gotchas
│   └── README.md        ← index of the 9-question onboarding assignment
├── screenshots/         ← UI screenshots the user shares (referenced from playbook/assignments)
└── notes/               ← scratch, questions, decisions
```

## Current work

**UnifyApps onboarding = ~20 assignments, then real client projects.**
- **One file per assignment** in `assignments/` (`assignment-NN-<slug>.md`), holding all its questions + per-question status.
- Master index: `assignments/README.md`. Screenshots per assignment: `screenshots/assignment-NN/`.
- Reusable builder how-tos are cross-assignment → `playbook/` (not duplicated per assignment).
- Active: **Assignment 01 — Data Sources & State Management** (Q1–Q9). Start tomorrow with Q1.

## Conventions

- Naming in the builder follows the assignment (e.g. apps/callables suffixed with the user's name).
- Keep playbook entries narrow: one reusable pattern per file (e.g. `how-to-storage-fetch-datasource.md`).
- Keep `assignments/README.md` status column honest as we complete each question.
