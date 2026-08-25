# How to use AI FDE (the builder's built-in AI assistant)

*From live UI, 2026-08-25 (tenant `tool.prod-aps1.unifyapps.com`).*

## What it is

**AI FDE** is UnifyApps' in-builder AI assistant. It both **answers platform questions** and
**builds things from prompts** (object schemas, record/object operations, automations).
It's our fallback when `docs/` + `playbook/` don't have the answer — ask it before going online.

## Where to find it

- **✦ AI FDE** button, **top-right corner of the builder chrome** (visible on every builder page).
- Clicking it opens a **right-side chat panel**: "Hey, I'm AI FDE — I can help you do your best work."

## The chat panel

- **"Ask anything…" input** at the bottom, with:
  - **+** button — attach files/context
  - **microphone** — voice input
- **Suggested questions** adapt to where you are (on the agent-builder page it offered:
  "How do I create an agent?", "How do Simple and Advanced agents differ?", "How do I deploy an agent?").
- Top of panel: **history** (clock icon), **feedback**, and **close** (×).
- Panel state is carried in the URL (`…&b_9U8lf-chatId=new`), so a chat can be linked/resumed.

## What it can do (grows as we learn)

| Capability | Notes |
|---|---|
| Q&A about the platform | Context-aware to the page you're on |
| Create object schemas | Prompt it with the entity + fields |
| Insert/manage records & object work | Prompt-driven |
| Build automations | Describes + creates the workflow itself |

## Related prompt-first builders (not AI FDE, but same "describe → build" idea)

- **Text-to-Application** — whole app from one prompt.
- **Text-to-Automation** — whole automation from one prompt.
- **Text-to-Agent** — AI Agents page is prompt-first: "**Describe. Build. Deploy.** Enterprise
  agents, built at the speed of thought." One "Ask anything…" prompt builds the agent
  (route: `/p/0/ai-agents/custom-gpt/edit/<id>/configuration`). Manual fallback below the
  prompt box: **Simple Agent / Advanced Agent / Workflow Agent**.

## Working rule

Craft the prompt → let AI FDE / text-to-X generate → verify and fix manually only where it
falls short. Save prompts that worked well (and quirks/limits discovered) back into this file.
