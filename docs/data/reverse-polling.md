# Reverse Polling

Source: https://www.unifyapps.com/docs/unify-data/reverse-polling
Section: data

---

# Overview

Reverse Polling is a specialized data retrieval pattern in UnifyApps Data Pipelines when working with API-based data sources that return results in chronological order (oldest records first). This approach requires specific handling techniques to efficiently process and extract the most recent or relevant data.

## What is Reverse Polling?

When consuming data from external APIs, some services return data in chronological order by default (oldest to newest). In Reverse Polling, the system must traverse through the entire list to find the most recent records, which are positioned at the end rather than the beginning of the result set.

## Why It Matters?

Understanding Reverse Polling helps data engineers and developers:

- Efficiently retrieve the most recent data when APIs present oldest records first
- Optimize data retrieval when only recent records are needed
- Implement proper pagination strategies for chronologically ordered APIs
- Reduce unnecessary data processing when only certain timeframes are relevant

## Technical Details

When an API returns data in chronological order (oldest first), the system must:

- Process the entire list to reach the newest records
- Implement efficient lookup mechanisms to find specific timestamps or IDs
- Use appropriate pagination parameters to navigate forward in time
- Optimize queries to potentially skip earlier pages when only recent data is needed

## Implementation Considerations

The UnifyApps platform handles these complexities behind the scenes by:

- Detecting API response ordering patterns
- Implementing optimized pagination strategies based on data ordering
- Using markers and indices to efficiently locate relevant data points
- Maintaining state information to optimize subsequent polling cycles

## Common API Examples

APIs that commonly return data in oldest-first order include:

- Certain legacy database systems
- Some financial transaction APIs
- Log management systems
- Historical data services

This knowledge article serves as background information for those interested in understanding the underlying concepts of API data retrieval patterns in UnifyApps Data Pipelines.
