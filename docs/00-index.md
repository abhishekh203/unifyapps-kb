# UnifyApps Docs — Local Index

Source site: https://www.unifyapps.com/docs (pulled and saved locally; local-first from here on).

> **To find a page fast, use [`MANIFEST.md`](MANIFEST.md)** — curated one-line descriptions for all
> 361 pages + a topic quick-jump (data sources, pagination, callables, transforms, …). Use it before grepping.

**All conceptual sections fully scraped to local markdown (363 pages)** via `scripts/scrape_docs.py`
(re-runnable; skips already-saved). Only the 1000+ connectors stay fetch-on-use.

The 8 "courses" / sections:

| # | Section | Local folder | Pages | Status |
|---|---------|-----------|------|--------|
| 1 | Unify Applications (no-code app builder) | `applications/` | 78 | ✅ fully saved |
| 2 | Unify Automations (workflows) | `automations/` | 103 | ✅ fully saved |
| 3 | Unify Data (replication, objects, transforms) | `data/` | 99 | ✅ fully saved |
| 4 | Unify Agentic AI (agents) | `agentic-ai/` | 49 | ✅ fully saved |
| 5 | Unify Integrations (connectors) | `integrations/` | 247 listed | 🔎 [`integrations/INDEX.md`](integrations/INDEX.md) — names+URLs; fetch each page on first use |
| 6 | Embedded Integrations (SDKs) | `embedded-integrations/` | 9 | ✅ fully saved |
| 7 | Platform Tools | `platform-tools/` | 12 | ✅ fully saved |
| 8 | Governance (policies, roles, compliance) | `governance/` | 11 | ✅ fully saved |

Each `overview.md` is a hand-written summary; the other files are the scraped article pages
(full click-by-click builder steps — these are the real depth). 24 category/hub pages had no body
of their own (just child links) and were skipped — their child articles are all saved.

**Images are included.** Each section has an `_img/` folder; pages embed screenshots via
`![](_img/<hash>.webp)`. Images are pulled through UnifyApps' own optimizer (WebP, width-capped)
so the folder stays small. The scraper (`scripts/scrape_docs.py`) preserves nested lists, bold/code,
links, note callouts, and tables. Run `python3 scripts/scrape_docs.py --force` to refresh,
`--no-images` for text-only.

Assignment-critical pages to know: `applications/data-table.md`, `using-repeatable.md`,
`repeatable.md`, `modal.md`, `form-component.md`, `stat-card.md`, `multi-stat-card.md`,
`map-data-to-interface-components.md`, `adding-data-sources.md`, `data-source-settings.md`,
`connect-to-data-source-callable-by-unifyapps.md`, `handle-interactions-in-interface.md`,
`pages.md`; `data/types-of-transformations.md`, `polling-with-pagination-and-offsets.md`.

**Assignment-critical consolidated concepts:** `_concepts-data-sources-and-state.md`
(data sources, the 3 pagination styles, callables, Transform Results, app- vs page-level state).

## Important note on doc depth

The public docs are **conceptual** — they describe *what* features exist, not the exact
click-by-click builder steps. The real "how to do X in the builder" is captured in
`../playbook/`, built from actually doing the assignments + the user's screenshots.

## Fetch-on-use rule

When we need a page not yet saved (a specific connector, an Agentic-AI deep page, a Platform
Tools / Governance article), fetch it ONCE from the source URL, save it under the matching
`docs/` subfolder, update this index, then use the local copy forever.
