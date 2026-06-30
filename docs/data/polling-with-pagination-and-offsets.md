# Polling with Pagination and Offsets

Source: https://www.unifyapps.com/docs/unify-data/polling-with-pagination-and-offsets
Section: data

---

## Overview

Polling with Pagination and Offsets is a fundamental data retrieval strategy employed in UnifyApps Data Pipelines when working with API-based data sources that organize results into discrete pages. This approach enables systematic processing of large datasets that cannot be returned in a single API response.

## What is Polling with Pagination and Offsets?

Pagination is a technique where API results are divided into sequential "pages" of data, with each page containing a limited number of records. Offset-based pagination uses numeric position indicators to navigate through these pages of data. When combined with polling, this creates a reliable mechanism for systematically processing large datasets.

## Key Concepts

**Pagination Parameters**

Most paginated APIs utilize two primary parameters:

- `Limit`: The number of records to return per page (often called "page size" or "count")
- `Offset`: The position in the dataset where retrieval should begin (may be called "start" or "skip")

**Offset Calculation**

The offset for each subsequent page is typically calculated as:

offset = (page_number - 1) * limit

## Implementation Process

1. Begin with an initial offset of 0 (the first page)
2. Process the returned records
3. Increment the offset by the page size
4. Request the next page
5. Continue until receiving fewer records than requested or an empty result set

## Example Data Retrieval Process

**Initial Request (Page 1)**

**Parameters**: limit=5, offset=0

| **Record #** | **Customer ID** | **Customer Name** | **Email** | **Created Date** |
|---|---|---|---|---|
| 1 | CUST-001 | Acme Corporation | contact@acmecorp.com | 2025-01-15 |
| 2 | CUST-002 | TechSolutions Inc | info@techsolutions.com | 2025-01-16 |
| 3 | CUST-003 | Global Enterprises | sales@globalent.com | 2025-01-17 |
| 4 | CUST-004 | Pacific Distributors | orders@pacificdist.com | 2025-01-18 |
| 5 | CUST-005 | Sunrise Industries | info@sunriseind.com | 2025-01-19 |

**Calculation for next page**: offset = 0 + 5 = 5

**Second Request (Page 2)**

**Parameters**: limit=5, offset=5

| **Record #** | **Customer ID** | **Customer Name** | **Email** | **Created Date** |
|---|---|---|---|---|
| 6 | CUST-006 | Quantum Innovations | support@quantuminv.com | 2025-01-20 |
| 7 | CUST-007 | Highland Services | info@highlandserv.com | 2025-01-21 |
| 8 | CUST-008 | Coastal Solutions | help@coastalsol.com | 2025-01-22 |
| 9 | CUST-009 | Metro Logistics | sales@metrolog.com | 2025-01-23 |
| 10 | CUST-010 | Atlas Technologies | contact@atlastech.com | 2025-01-24 |

**Calculation for next page**: offset = 5 + 5 = 10

**Third Request (Page 3)**

**Parameters**: limit=5, offset=10

| **Record #** | **Customer ID** | **Customer Name** | **Email** | **Created Date** |
|---|---|---|---|---|
| 11 | CUST-011 | Pinnacle Systems | info@pinnaclesys.com | 2025-01-25 |
| 12 | CUST-012 | Horizon Enterprises | sales@horizonent.com | 2025-01-26 |
| 13 | CUST-013 | Silverline Partners | contact@silverlinepr.com | 2025-01-27 |
| 14 | CUST-014 | Northern Solutions | support@northernsol.com | 2025-01-28 |
| 15 | CUST-015 | Evergreen Industries | orders@evergreenind.com | 2025-01-29 |

**Calculation for next page**: offset = 10 + 5 = 15

**Final Request (Page 4)**

**Parameters**: limit=5, offset=15

| **Record #** | **Customer ID** | **Customer Name** | **Email** | **Created Date** |
|---|---|---|---|---|
| 16 | CUST-016 | Sapphire Analytics | info@sapphireana.com | 2025-01-30 |
| 17 | CUST-017 | Redwood Partners | contact@redwoodp.com | 2025-01-31 |

**Result**: Only 2 records returned (less than the requested limit of 5), indicating we've reached the end of the dataset.

## Challenges and Considerations

**Performance Degradation**

Offset-based pagination can experience performance issues with very large datasets, as the database must still process all records up to the offset point. For example, retrieving records 10,000-10,100 requires the database to count through the first 10,000 records before returning results.

**Consistency Issues**

If data is being added or removed during the polling process, offset-based pagination can lead to:

- Missed records (if items are added before the current position)
- Duplicate records (if items are removed before the current position)

**API Limitations**

Many APIs impose:

- Maximum offset values
- Maximum page size values
- Rate limits on the number of requests

## Best Practices

- Use reasonable page sizes that balance between minimizing API calls and processing efficiency
- Implement retry logic with exponential backoff for failed requests
- Store pagination state to resume interrupted processes
- Track progress metrics to identify performance issues
