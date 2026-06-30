# Forward Polling

Source: https://www.unifyapps.com/docs/unify-data/forward-polling
Section: data

---

## Overview

Forward Polling is a standard data retrieval pattern in UnifyApps Data Pipelines when working with API-based data sources that return results in reverse chronological order (newest records first). This approach is the most common pattern for efficiently collecting recent data from modern APIs.

## What is Forward Polling?

In Forward Polling, APIs return the most recent data at the beginning of the result set, allowing systems to efficiently retrieve and process new records without traversing through older data. This pattern aligns with the natural way most systems want to consume data - prioritizing the newest information.

## Why It Matters?

Understanding Forward Polling helps data engineers and developers:

- Efficiently retrieve the most recent data without processing older records
- Implement incremental data collection strategies
- Optimize API usage within rate limits
- Reduce latency for time-sensitive data processing

## Technical Details

When an API returns data in reverse chronological order (newest first), the system can:

- Process only the first few pages to get the most recent records
- Use timestamp or ID-based parameters to retrieve only data newer than the last poll
- Implement efficient incremental loading strategies
- Minimize data transfer and processing overhead

## Implementation Considerations

The UnifyApps platform leverages Forward Polling by:

- Tracking the most recent timestamp or ID from previous poll cycles
- Using "since" or "after" parameters to request only new data
- Optimizing polling frequencies based on data change patterns
- Storing state information for efficient incremental processing

## Common API Examples

Most modern APIs implement Forward Polling patterns, including:

- Social media platforms
- Modern CRM and ERP systems
- E-commerce platforms
- Cloud service providers
- IoT data services

This knowledge article serves as background information for those interested in understanding the standard and most common API data retrieval pattern in UnifyApps Data Pipelines.
