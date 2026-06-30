# Min Value

Source: https://www.unifyapps.com/docs/unify-data/min-value
Section: data

---

## **Overview**

The Minimum Value strategy is the precise inverse of the Maximum Value rule. It is a deterministic survivorship logic designed to identify and preserve the smallest data point found among duplicate records.

This strategy is particularly valuable when "less" signifies "better," "earlier," or "higher priority."

By filtering out higher values, UnifyApps ensures that your Golden Record reflects the most conservative estimate, the earliest historical event, or the highest rank (lowest integer) available in your data ecosystem.

## **The Logic: Lowest Wins**

When configured, the system evaluates the target field across all conflicting records within a match group.

Selection Criteria: As defined in the configuration panel, the system will "Select the lowest value among duplicates".

## **Behavior by Data Type:**

- **Numeric Data:** It selects the smallest number (e.g., comparison between $150 and $120 results in $120 ).
- **Date/Time Data:** It selects the earliest chronological timestamp (e.g., determining the "First Created Date").

## **Configuration Options**

Similar to other quantitative strategies, Minimum Value is most effective when applied granularly:

1. **Primary Strategy** You can assign this as the main rule for specific fields via the Custom Strategy configuration. This is ideal for fields where the lowest value represents the "truth" or the desired business state (like a queue position).
2. **Fallback Strategy** It serves as an effective tie-breaker in Fallback Strategies. If a primary rule (like "Source System") fails because a high-priority source is missing data, the Minimum Value rule can ensure that a valid, conservative value is picked from the remaining sources rather than leaving the field empty.
