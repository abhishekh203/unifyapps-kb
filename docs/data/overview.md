# Unify Data — Objects, Replication, Transforms

Source: https://www.unifyapps.com/docs/unify-data · pulled locally.

## What it is
Real-time data replication from any source to any destination + master-data governance: pipelines,
transformations, dedup, encryption.

## Capabilities
- **Sources** — MS SQL Server, Amazon Redshift, PostgreSQL, Salesforce, QuickBooks Online, Zoho Invoice, …
- **Ingestion modes** — Historical+Live, Live Only, Historical Only.
- **Manual Field Creation** — define fields: Key, Display Label, Description, Field Type, Default Value;
  flags: Filterable, Searchable, Hashable, Sortable, Primary Key, Required, Secure Field (encryption).
- **Fuzzy Match Rules** — dedup; "Exact Match On" = character-for-character match for IDs/SSNs.
- **Min Value** — survivorship: keep smallest value among duplicates (earliest date, top priority).
- **Encryption / Decryption** — AES-256 with IVs for PII.
- **Analytics Query** — projections, grouping, filtering, aggregations (Count, Sum, Min/Max);
  Aggregate Metadata returns field properties (sortable/filterable/searchable/updatable).
- **Pagination** — Offset/Limit for large datasets.

## Objects (assignment context)
The assignment queries **objects** via their records URL, e.g.:
- `…/object/product_inventory/records` (ProductInventory)
- `…/object/customer_order/records` (CustomerOrders)
A **"storage fetch records" data source** queries an object; supports pagination (infinite scroll,
offset) and filtering.

## Transform Results (assignment Q7) — KEY
A data-source feature to **post-process query results** in code before they reach the UI — compute
derived values like average price, total inventory value (sum of price × stockCount), category with
most products, total count. Output feeds UI (e.g. stat cards).

> Exact builder steps for storage-fetch config, pagination toggles, and Transform Results editor →
> captured in `../playbook/` as we do Q1 and Q7.
