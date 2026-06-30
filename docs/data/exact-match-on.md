# Exact Match On

Source: https://www.unifyapps.com/docs/unify-data/exact-match-on
Section: data

---

**Overview**

Within the UnifyApps Master Data Management (MDM) framework, Match Rules are the logic engines responsible for identifying duplicate records across your dataset.

The Exact Match On criterion is the most deterministic and rigid matching strategy available.

Unlike fuzzy matching algorithms that allow for slight variations (e.g., "Jon" vs. "John"), an "Exact Match On" rule requires the data in the selected field to be 100% identical—character for character—to be considered a match.

**Use Cases**

This rule type is best suited for high-confidence identifiers where no ambiguity is acceptable:

- **Unique Identifiers:** Matching on system-generated IDs like User_ID , Social_Security_Number , or ISBN .
- **Digital Coordinates:** Matching on fields like Email Address or Phone Number (normalized) where a single character difference implies a different entity.**Codes:** Matching on standardized business codes such as Store_ID or Cost_Center_Code . **Configuration Guide**Configuring an exact match rule involves defining the criteria in the Match Rule Definition panel.
  1. **Navigate to Rule Definitions** From the specific Entity's dashboard, select the Match Rules tab and click + New Match Rule. Enter a descriptive Rule Name (e.g., "Primary Key Exact Match") and Description to document the rule's intent.
  2. **Set the Match Condition** In the Match Rule Definition section, you will define the logic logic used to compare records:
    1. **Where:** Select **Exact Match On** from the primary condition dropdown. This instructs the system to look for strict equality.
    2. **Select a Field:** Choose the specific attribute you want to compare (e.g., Branch_Code or Primary_Key ).
  3. **Advanced Combinations** For more complex validation, you can layer multiple exact match conditions: a. **Add Field:** Clicking this allows you to create a compound key match (e.g., Match EXACTLY on First Name AND EXACTLY on Last Name ). b. **Add Field Group:** This enables more sophisticated logic groupings, effectively allowing for "OR" conditions within your match strategy.
  4. **Define Merge Policy** Once the system identifies records that satisfy the "Exact Match" criteria, you must define the action to take:
    1. **Automatically Merge:** The confidence level is high enough to merge records without human intervention.
    2. **Flag for Review:** The match is detected but requires a data steward to verify it in the "Potential Matches" queue.
