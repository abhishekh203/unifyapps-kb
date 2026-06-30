# Application Connectors

Source: https://www.unifyapps.com/docs/unify-data/application-connectors
Section: data

---

Application connectors in UnifyApps serve as the backbone for seamless SaaS integration solutions. These connectors enable your organization to extract data from various cloud applications, transform it according to your business requirements, and load it into your destination platforms without complex coding or maintenance overhead.

## What Are Application Connectors?

Application connectors are pre-built integration components that establish secure, reliable connections between UnifyApps and your SaaS applications. They handle the complexities of API communication, authentication mechanisms, rate limiting, and data schema transformations.

## Connection Methods

UnifyApps application connectors support multiple authentication methods to ensure secure and flexible connectivity:

1. **OAuth 2.0**
  - Industry-standard authorization framework
  - Secure delegated access without sharing credentials
  - Automatic token refresh capabilities
  - Supported by most modern SaaS platforms (Salesforce, Google Apps, Microsoft 365)
2. **API Token/Key Authentication**
  - Simple authentication using application-generated tokens
  - Long-lived access credentials
  - Commonly used for service-to-service integrations
  - Supported by platforms like Jira, HubSpot, Zendesk
3. **Basic Authentication**
  - Username/password-based authentication
  - Typically used for legacy systems
  - Secure transmission via HTTPS
4. **JWT (JSON Web Tokens)**
  - Self-contained authentication method
  - Digitally signed tokens with claims
  - Used by platforms like ServiceNow and some custom implementations

## Polling Methods

UnifyApps implements various polling strategies to efficiently retrieve data from source applications:

1. **Forward Polling**
  - Retrieval starting from most recent records backward
  - Example: Getting latest Zendesk tickets first
  - Optimal for prioritizing recent data in time-sensitive scenarios
2. **Reverse Polling**
  - Sequential data retrieval based on timestamp or ID
  - Example: Fetching Salesforce records created after last sync time
  - Efficient for applications with chronological data creation
3. **Cursor-Based Polling**
  - Uses application-provided pagination cursors
  - Example: Facebook Ads' cursor pagination
  - Highly efficient for large datasets
  - Resilient to data changes during polling
4. **Webhook-Based Ingestion**
  - Real-time data capture via push notifications
  - Example: Shopify order webhooks
  - Minimizes latency and reduces API load
  - Complementary to polling strategies

## Supported Application Connectors

UnifyApps offers native connectivity to a comprehensive range of SaaS platforms:

| **Application Connector** | **Description** | **Common Use Cases** |
|---|---|---|
| `Airtable` | Collaborative spreadsheet-database | Project management, content calendars |
| `Facebook Ads` | Social media advertising platform | Marketing analytics, ad performance |
| `Google Ads` | Online advertising platform | Campaign tracking, conversion analysis |
| `Google Analytics` | Web analytics service | Website performance, user behavior |
| `Google Sheets` | Cloud-based spreadsheet | Collaborative data management, reporting |
| `HubSpot` | CRM and marketing platform | Lead management, marketing automation |
| `Jira` | Project management tool | Development tracking, issue management |
| `Klaviyo` | Marketing automation platform | Email campaigns, customer segmentation |
| `LinkedIn Marketing` | B2B marketing platform | Professional audience targeting, ads |
| `Mailchimp` | Email marketing platform | Newsletter campaigns, subscriber analytics |
| `Microsoft Dynamics 365 CRM` | Business applications suite | Customer relationship management |
| `Mixpanel` | Product analytics platform | User engagement, feature adoption |
| `Monday` | Project management platform | Team collaboration, workflow management |
| `Omnisend` | E-commerce marketing platform | Customer journey automation |
| `QuickBooks` | Accounting software | Financial data, bookkeeping |
| `Recharge` | Subscription payment management | Recurring billing, subscriber analytics |
| `Salesforce` | CRM platform | Sales pipeline, customer data |
| `ServiceNow` | IT service management | Workflow automation, service desk |
| `Shopify` | E-commerce platform | Order data, product inventory |
| `Workday` | HR management system | Employee data, organizational structure |
| `Workiva` | Financial reporting platform | Compliance reporting, disclosure management |
| `Zendesk` | Customer service platform | Support tickets, customer interactions |

## Destination Support

UnifyApps also supports writing data to several application/SaaS connectors, enabling bi-directional data flows:

- Microsoft Dynamics 365 CRM
- Salesforce
- Tableau
- Zendesk

## Key Features of Application Connectors

All UnifyApps application connectors share common capabilities that enable efficient and secure data integration:

1. **Intelligent Rate Limiting**
  - Automatic API quota management
  - Backoff and retry mechanisms
  - Quota distribution optimization
2. **Schema Discovery**
  - Automatic metadata retrieval
  - Field-level mapping capabilities
  - Custom field support
3. **Comprehensive Object Support**
  - Access to standard and custom objects
  - Relationship traversal capabilities
  - Support for nested data structures
4. **Multiple Ingestion Modes**
  - Historical and Live: Full load plus ongoing changes
  - Live Only: New data from deployment onward
  - Historical Only: One-time full load
5. **Data Transformation**
  - Field mapping and conversion
  - Filtering capabilities
  - Formula-based derived fields

## Business Benefits

Application connectors deliver significant value to your organization by:

- **Accelerating Time-to-Value**: Implement integrations in days instead of months
- **Reducing Maintenance Burden**: Automatic adaptation to API changes
- **Breaking Down Data Silos**: Connect data across your application landscape
- **Enabling Real-Time Operations**: Synchronize data with minimal latency
- **Supporting Business Agility**: Quickly adapt to new applications and requirements
