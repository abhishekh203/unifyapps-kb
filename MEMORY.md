# MEMORY.md — durable lessons (repo-based memory)

Read this every session along with CLAUDE.md. This file replaces Claude's machine-local memory
so the knowledge travels with the repo on GitHub. **When a durable lesson is learned, append it
here** (newest on top per section). Repo-recorded facts (CLAUDE.md rules, playbook how-tos)
don't get duplicated — this file holds what's true *about* the work but written nowhere else.

## Docs mirror — refresh procedure & site quirks (2026-08-25)

- The ENTIRE docs site is local: 388 conceptual pages + all 288 connectors (`docs/integrations/`).
- Refresh: `.venv/bin/python scripts/scrape_docs.py --force --connectors`
  (delete `/tmp/ua_docs_urls.txt` first to re-pull the sitemap). Then update counts/dates in
  `docs/MANIFEST.md`, `docs/00-index.md`, regenerate `docs/integrations/INDEX.md`, and run
  `scripts/build_manifest.py` to digest new pages for MANIFEST descriptions.
- Site quirks learned:
  - 24 sitemap URLs are empty hub/category pages (e.g. `unify-applications/form`,
    `unify-data/transformation`) — no article body, only child links. "no-content" from the
    scraper for these is normal, not an error.
  - Aug 2026: the site moved ~33 connector pages (slack, jira, gmail, mysql, …) from
    unify-automations to unify-integrations. Our older copies remain in `docs/automations/`.
  - The site periodically rotates ALL image CDN URLs → a `--force` re-scrape re-downloads every
    image under new hashed names; delete orphaned old images afterward (compare files in
    `_img/` vs `_img/…` references in that section's .md files).
- The project `.venv` breaks if the repo folder moves (absolute paths inside); recreate with:
  `python3 -m venv .venv && .venv/bin/pip install beautifulsoup4 mkdocs-material`.

## Working model (2026-08-25)

- Claude drives the UnifyApps builder via the Claude in Chrome extension; the user only steps
  in for logins/2FA or true blockers. No new screenshots are saved — `screenshots/` is frozen.
- Build with the platform's AI first (AI FDE / text-to-application / text-to-automation /
  text-to-agent — see `playbook/how-to-ai-fde.md`), verify and hand-fix only the gaps.
- Client work seen on tenant `tool.prod-aps1.unifyapps.com`; tenant varies per project.
