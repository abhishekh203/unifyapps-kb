# Max Value

Source: https://www.unifyapps.com/docs/unify-data/max-value
Section: data

---

## **Overview**

The Maximum Value strategy is a data-driven survivorship rule designed specifically for numerical or ordered data fields.

Unlike strategies that rely on metadata (like timestamps) or provenance (like source system hierarchy), this rule evaluates the actual content of the field.

It compares the values from all duplicate records and preserves the largest one for the Golden Record, ensuring that the master data represents the highest magnitude found across your system landscape.

## **The Logic: Highest Wins**

When this strategy is applied, UnifyApps scans the target field across all records in the match group.

Selection Criteria: The system identifies and selects the "highest value among duplicates".

## **Behavior:**

- **Numbers:** It selects the largest integer or decimal (e.g., between 500 and 1000 , it chooses 1000 ).
- **Dates:** If applied to date fields, the "maximum" value typically corresponds to the date furthest in the future (the latest date).

## **Configuration Options**

You can deploy the Maximum Value strategy as a primary rule or as a backup mechanism:

1. **Primary Strategy** You can assign Maximum Value as the main rule for specific quantitative fields using the Custom Strategy toggle. This is often safer than setting it as a global default, as "maximum" is not always the desired state for every field type.
2. **Fallback Strategy** This strategy is highly effective as a fallback. For example, if your primary "Recency" rule results in a tie (two records updated at the exact same second), you can use Maximum Value as the tie-breaker to ensure a deterministic outcome (e.g., picking the higher transaction amount).
