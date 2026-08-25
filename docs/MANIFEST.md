# Docs Manifest — find the right page fast

Curated index of all 388 local doc pages (AI-written descriptions). **Use this first**: scan to the
right file, then open only that file — don't grep 388 pages. The 288 connector pages (unify-integrations)
are also fully mirrored in `integrations/` — find them via `integrations/INDEX.md`, not here.
Rebuild the raw digest with `scripts/build_manifest.py`.

Last full re-scrape from unifyapps.com: **2026-08-25** (`scripts/scrape_docs.py --force`).

---

## ⚡ Quick jump — by topic (covers Assignment 01 + the common stuff)

**Data sources — create / configure / test**
- `applications/adding-data-sources.md` — add & manage data sources in an app (compatible sources, steps)
- `applications/data-source-settings.md` — **run behavior: auto vs manual, RUN ON PAGE LOAD, run periodically** (KEY: Q5, Q8)
- `applications/storage-by-unifyapps-2.md` — **Storage data source = fetch/manipulate Object records in an app** (the "storage fetch records" → Q1, Q2, Q7)
- `applications/analytics-by-unifyapps-data-source.md` — Analytics data source (aggregations); "Using Analytics in Stat Cards"
- `applications/connect-to-data-source-callable-by-unifyapps.md` — **Callable data source = call an automation, use its output** (KEY: Q3, Q4, Q5, Q6, Q8, Q9)
- `applications/testing-your-data-source.md` — preview a data source's output shape
- `applications/map-data-to-interface-components.md` — data pills: bind data-source output / state / inputs to components

**Pagination**
- `applications/data-table.md` — Data Table component: source, columns, add-ons, **pagination**, filters (Q1 A/B/C, Q2 action column)
- `data/polling-with-pagination-and-offsets.md` — offset/limit pagination concept (pipeline side)
- `applications/using-repeatable.md` + `repeatable.md` + `repeatable-list.md` — **Repeatable for custom/infinite pagination** (Q3 B)

**Filtering**
- `applications/filters.md` — filter components; **stitching filters to data sources**; filterable fields via aggregation metadata (Q1C, Q3C)
- `applications/data-table.md` — built-in table filter toolbar (add-ons)

**Inputs / display components**
- `applications/text-input.md` — Text Input (Q1 search, Q3 customer name, Q8 product id)
- `applications/form-component.md` — Form (text, dropdown/single-select, number, date…) (Q2 modal form)
- `applications/modal.md` — Modal pop-up (card modal / page modal) (Q2)
- `applications/stat-card.md` + `multi-stat-card.md` — Stat Card(s) for metrics (Q4, Q7)
- `applications/text.md` — Text/Typography component (Q6 final total)

**Interactions / navigation / events**
- `applications/handle-interactions-in-interface.md` — events (OnClick…), conditional interactions, **trigger data source / open page** (Q2, Q5, Q6, Q8, Q9)
- `applications/pages.md` — create pages, custom URL, **share data across pages**, page permissions (Q5, Q9)
- `applications/navigation.md` + `navigation-container.md` — side-panel nav / nav hierarchy (Q9 nav buttons)

**Callables (automation side — for authoring your own, Q3)**
- `automations/callable.md` — reusable automations triggered externally/from others (Key Features, use case)
- `automations/callable-via-api.md` — callable triggered by API request (inputs/trigger/request)
- `automations/callable-trigger-from-automation.md` — trigger one automation from another
- `automations/automation-interfaces.md` — define a reusable input/output **schema** for callables
- `automations/build-your-first-automation.md` — trigger types, action types, create an automation
- `automations/setup-triggers.md` — trigger types (connector/API/scheduler)

**Transform Results / data math (Q7)**
- `data/overview-transformations.md` — why/what of transformations; independent vs single- vs multi-field
- `data/types-of-transformations.md` — catalog: shielding, cleansing, manipulation, enrichment, blob
- `data/spreadsheet-formula.md` — Excel-like formulas in a pipeline (calc/agg) — closest to "compute avg/sum"
- `automations/formula-suggestions.md` — formulas in automations (numeric/text/date/logic)
- `automations/code-by-unifyapps.md` — run custom code (JS/Python/Groovy/Java) in an automation
- `applications/js-variables-and-functions.md` — JS variables & functions inside an app
- `applications/utilities.md` — built-in app utility functions (formatDate, formatNumber…)

**App-level vs page-level state / persistence (Q9)**
- `applications/pages.md` — "Share Data Across Pages"
- `applications/adding-data-sources.md` + `data-source-settings.md` — where data sources are scoped & run behavior

> If a topic isn't here, scan the section lists below; if still missing, it may be a connector page
> (fetch-on-use) — pull it once and save under the right `docs/<section>/`.

---

## applications/ — no-code app builder (79)

**Data & state:** adding-data-sources · data-source-settings · storage-by-unifyapps-2 · analytics-by-unifyapps-data-source · connect-to-data-source-callable-by-unifyapps · testing-your-data-source · map-data-to-interface-components · js-variables-and-functions · utilities

**Tables / lists:** data-table · nested-table · repeatable · repeatable-list · using-repeatable · image-grid

**Inputs / forms:** form-component · text-input · file-upload · calendar · code-editor · scanner · camera · qr-code

**Display / layout:** text · key-value · stat-card · multi-stat-card · card · container · stack · tabs · divider · navigation-container · stepped-container · stepper · drawer-component · modal · contextual-dialog · menu

**Buttons / actions / nav:** button · button-group · icon-button · icon · link · handle-interactions-in-interface · navigation · pages · page-templates

**Charts:** chart · column-chart · radar-chart

**Media / misc components:** image · video · audio-player · media (image/video/audio from static or dynamic sources) · carousel · avatar · avatar-group · alert-component · tag · progress-bar · loader · timer · timeline · organization-chart · comments

**App-building / admin:** overview · add-components-to-your-interface · defining-layout-of-your-interface · add-custom-component · module · filters · custom-css · interactive-mode-switcher · preview-application · privacy-settings · user-management · version-control

## automations/ — workflows & callables (107)

**Build / core:** overview · build-your-first-automation · add-actions · setup-triggers · use-operators · deploy-your-automation · test-your-automation · preview-your-work · monitor-your-runs · manage-your-versions · automation-settings · automation-templates-by-unifyapps (pre-built reusable workflow templates) · logging (per-node log messages + levels)

**Control flow nodes:** condition · branch · loop · delay · stop · retry-on-error · use-operators · workflow-debugger · dependency-graph · node-id · hooks (trigger child automations from a node, no extra node) · signals-by-unifyapps (wait-for-signals / emit-signal for parallel parent-child async)

**Callables (KEY):** callable · callable-via-api · callable-trigger-from-automation · call-another-automation · automation-interfaces · webhook · schedule

**UnifyApps utility nodes:** code-by-unifyapps · variable-by-unifyapps · utility-by-unifyapps · files-by-unifyapps · excel-by-unifyapps · pdf-by-unifyapps · csv-reader-by-unifyapps · template-by-unifyapps · storage-by-unifyapps · standard-entities-by-unifyapps · caches-by-unifyapps · cache-management · cache-policy · notifications-by-unifyapps · conversation-by-unifyapps · gen-ai-by-unifyapps · unify-ai · pii-by-unifyapps · audit-by-unifyapps · auth-by-unifyapps · audience-segments-by-unifyapps · streams-by-unifyapps · unified-entity · video-by-unifyapps · voicebot-by-unifyapps · analytics-by-unifyapps-node · formula-suggestions

**API manager / policies:** api · api-groups · cache-policy · cors-policy · jwt-validation-policy · ip-based-access-control-policy · rate-limiting · rate-limiting-policy · request-transformer-policy · request-validator-policy · response-transformer-policy · timeout-policy · usage-quota-policy · custom-http-endpoint · runtime-connection-switching · connection-troubleshooting

**Connectors (sample; site moved these under unify-integrations 2026-08, local copies kept as-is):** gmail · google-sheets · google-docs · slack · jira · zendesk · freshdesk · asana · clickup · monday · mongodb · mysql · postgresql · oracle-db · microsoft-sql-server · snowflake · clickhouse · amazon-s3 · amazon-athena · dropbox · figma · zoom · whatsapp · mailchimp · sendspark · stripe(see agentic) · pagerduty · okta · bamboohr · fleetio · crm/customer-support/ticketing/collaboration (category pages) · add-your-connector-sdk

## data/ — objects, pipelines, MDM, transforms (105)

**Concepts / MDM:** overview · core-concepts · overview-unified-data-model · multidomain-capabilities · golden-records · golden-record-metadata · access-control · identity · relationships · defining-entity-relationships · record-level-ontology

**Entities & fields:** overview-creating-entities · creating-entity-fields · manual-field-creation · import-field-using-sources · import-fields-using-csv-xls-files · entity-storage-types · advanced (see platform-tools/create-your-first-object)

**Match / dedup / survivorship:** survivorship (MDM conflict resolution: global default + field-level strategies) · overview-match-rules · exact-match-on · fuzzy-match-rule · primary-key-match-rule · match-rule-outcomes · potential-matches · manual-merge-flow · default-survivorship-strategy · field-level-survivorship · source-system · min-value · max-value

**Quality / quarantine:** overview-data-quality-rules · validation-rules · cleansing-rules · enrichment-rules · quarantined-records · rejected-records · reject-record · delete-records · edit-and-resubmit

**Pipelines:** overview-pipeline · create-your-first-data-pipeline · pipelines · data-sync · automations · set-up-the-source-and-destination · object-selection-and-schema-mapping · objects-selection · schema-mapping1 · settings-and-deployment · overview-settings · overview-pipeline-deployment · overview-logs · introduction-to-data-pipeline-connectors · application-connectors · database-connectors · data-warehouse-connectors · file-storage-connectors

**Polling / sync settings:** polling-techniques · polling-cursor · polling-with-pagination-and-offsets · forward-polling · reverse-polling · data-sync-by-avoid-duplicate-operations-setting · ingestion-order-setting-for-priority-based-multi-entity-mapping · scd-type-2-settings · timezone-adjustment-use-case · destination-timezone-setting-for-oracledb-as-destination · salesforce-as-source-polling-tuning

**Transformations:** overview-transformations · types-of-transformations · duplicate-field-transformation · spreadsheet-formula · extract-text · replace-value · text-casing-modification · encoding · encryption · hashing · transformations-masking · download-content-from-s3-transformation · download-content-from-azure-blob-storage · upload-content-to-s3

**Source/destination connectors (sample):** sources · *-as-source / *-as-destination (mysql, postgresql, oracledb, snowflake, microsoft-sql-server, amazon-redshift, google-bigquery, monday, hubspot, quickbooks, klaviyo, omnisend, facebook-ads, google-ads, amazon-athena…)

## agentic-ai/ — AI agents (52)

**Start / build:** overview · getting-started · ai-agent-overview · how-unify-ai-agents-work · benefits-of-ai-agents · create-an-ai-agent · create-your-first-agent · simple-agent · advanced-agent · settings-overview

**Agent parts:** instructions/prompts · setup-tasks · best-practice-for-setting-up-tasks · adding-tools-to-your-tasks · add-new-tool (add tools to an agent: types, steps) · expose-workflows-as-tools (turn automations into agent tools) · configure-tools · configure-mcp-servers · prerequisite-tasks · prerequisite-actions · integrate-knowledge-base · response-generation

**Knowledge pipeline:** indexing · knowledge-ingestion · knowledge-pipeline · knowledge-settings · pre-processing

**Models:** add-a-model · model-library · custom-models · model-playground (compare LLMs side-by-side) · import-external-agents-via-bedrock

**Guardrails:** guardrails-overview · content-filters · custom-word-filter · denied-topics · blocked-messaging · hallucination-control · pii-masking

**Test / eval / deploy / observe:** conversational-testing · datasets · metrics · evaluation-overview · experiments · publish-and-test · deployments · trigger-and-deploy · copilot-overview · observability · sessions-and-tracing · team-of-ai-agents-overview · stripe

## embedded-integrations/ — embed UnifyApps in your product (11)
authentication (two-token model) · application-embed-react-sdk · application-embed-angular-sdk · application-embed-javascript-sdk · application-embed-iframe · application-embed-salesforce · application-embed-shopify · application-embed-zendesk · platform-embed-react-sdk · platform-embed-javascript-sdk · platform-embed-iframe

## platform-tools/ — objects, connections, templates, env (13)
what-is-object-manager · create-your-first-object · advanced-configurations · what-is-connection-manager · set-up-your-first-connection · connections-insights · connector-sdk · create-your-first-connector-sdk · what-is-templates-manager · build-your-first-template · decision-table · environment-variables · open-telemetry (publish platform metrics to Prometheus)

## governance/ — roles, environments, security (21)
role · user · teams · users-insights-activities · security (SSO) · data-protection · alert-manager-by-unifyapps · business-hours-configuration · business-holidays (non-working days for automations) · connected-environments · inbound-changeset · outbound-changeset

**SSO / IdP setup guides (new 2026-08):** openid-connect-oidc-idp-configuration (generic OIDC) · custom-saml-idp-configuration-for-unifyapps (generic SAML: ForgeRock, JumpCloud…) · azure-openid-sso-configuration · azure-saml-idp-configuration-for-unifyapps · google-openid-sso-configuration · okta-openid-sso-configuration · okta-saml-idp-configuration · ldap-sso-configuration · external-session-setup-guide (external login session via cURL/automation)
