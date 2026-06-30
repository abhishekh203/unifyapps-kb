# Core Concepts

Source: https://www.unifyapps.com/docs/unify-data/core-concepts
Section: data

---

### **Why Do We Need Master Data Management (MDM) in UDM?**

MDM consolidates, cleanses, and standardizes data from multiple systems to produce a single, trusted **golden record**. 
 Within UDM, MDM ensures data is accurate, deduplicated, validated, and governed before it’s used for analytics or operations. It eliminates inconsistencies, manages entity relationships, enforces access controls, and improves overall data integrity.

### **What Is a Multidomain Model in UDM?**

A multidomain model supports multiple entity types (customers, accounts, transactions, products, etc.) and the relationships between them. 
 In UDM, this allows organizations to build a unified, interconnected view of data across domains, enabling cross-domain insights, removing silos, and supporting complex data strategies—all configurable through the UDM interface.

**Architecture of UnifyApps' MDM Solution**
 UDM in UnifyApps uses a high-performance StarRocks staging layer for scalable validation, with dedicated tables for rejected and matched records to ensure traceability and effective deduplication. The iPaaS layer cleanses and enriches data before MDM processing. Survivorship creates accurate golden records with full source tracking, while RBAC secures and governs steward access .

#### **Why Is the MDM Staging Table Hosted on StarRocks?**

- **High Performance:** Handles large data volumes efficiently for fast validation and transformation.
- **Scalability:** Maintains speed as data grows.
- **Flexibility:** Supports complex data-quality rules early in the pipeline. **Why Do We Need the MDM Rejected Record Table?****Why Do We Need the MDM Match Record Table?**
  - **Audit & Traceability:** Captures failed records with rejection reasons.
  - **Remediation:** Enables correction and reprocessing without data loss.
  - **Governance:** Ensures transparency and supports compliance.
  - **Duplicate Detection:** Stores potential duplicate groups using match rules.
  - **Quarantine:** Holds records for manual review when needed.
  - **Survivorship:** Feeds merging logic to create clean golden records. **Usage of the iPaaS Layer (Enrichment & Cleansing)****What Is Deduplication?**Deduplication identifies and removes duplicate records so each entity appears only once. Using exact or fuzzy match rules, duplicates are flagged, merged, or reviewed based on policies. The outcome is a consistent, non-redundant **golden record**.**Impact of Survivorship on Source Tracking & Evaluation**Survivorship determines which field values are retained when merging duplicates.**Why Do We Need RBAC for Stewardship & Data Access?**In UnifyApps, RBAC enables field-level restrictions, record-level filters, and role-based access policies—forming the backbone of secure and governed master data management.
    - **Cleansing:** Standardizes and corrects data (e.g., phone formats, addresses).
    - **Enrichment:** Adds third-party or internal attributes (e.g., geocodes, demographics).
    - **Orchestration:** Automates workflows to ensure high-quality, enriched data flows into MDM.
    - **Source Tracking:** Maintains audit trails of which source contributed each value.
    - **Evaluation:** Helps assess and prioritize data sources based on quality or recency. Fallback rules ensure reliable value selection even when primary rules don’t resolve conflicts.
    - **Security & Privacy:** Controls who can view or edit specific fields and records.
    - **Stewardship:** Ensures only authorized stewards manage data-quality tasks.
    - **Operational Efficiency:** Simplifies permission management through role-based policies.
