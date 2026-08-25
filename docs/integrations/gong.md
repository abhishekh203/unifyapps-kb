# Gong Integration

Source: https://www.unifyapps.com/docs/unify-integrations/gong
Section: integrations

---

Integrating your application with Gong enables you to capture, analyze, and gain insights from customer interactions such as sales calls, meetings, and emails. It provides a revenue intelligence platform that automatically records and transcribes conversations, analyzes engagement and sentiment, identifies key topics and trends, and delivers actionable insights to improve sales performance, coaching, and decision-making across teams.

## Authentication

Connecting your application with Gong enables secure access to call data, transcripts, and analytics. Before you begin, ensure you have the following information:

`Connection Name:` Choose a meaningful name for your connection. This helps you identify it within your application.*(e.g., "MyAppGongIntegration")*

`Authentication Type:` Gong supports the following authentication types in UnifyApps:

1. `Basic Authentication`
2. `OAuth Authentication`

### Basic Authentication

1. Log in to your Gong account
2. Go to Company Settings / API Settings
3. If API access is not enabled:
4. Navigate to the API / Developer section
5. Click on Create API Key
6. Copy the following credentials:

### OAuth Authentication

1. Oauth is not enabled by default in Gong . Requires: Special enablement from Gong or App registration via Gong Team
2. Register your application with Gong
3. Provide the Callback URL
4. After registration, you will receive:
5. Use these credentials in UnifyApps OAuth configuration
6. Complete the authorization flow to generate:

## Actions :

| **Action Name** | **Description** |
|---|---|
| `Add New Call` | Adds a new call record in Gong. |
| `Get User` | Retrieves details of a specific user. |
| `List Users` | Fetch list of users. |
| `List Workspaces` | Fetch list of workspaces. |
| `List Coaching Metrics` | Fetch coaching metrics data. |
| `Retrieve Call Data by Date Range` | Retrieves call data within a specified date range. |
| `Retrieve Detailed Call Data Using Filters` | Retrieves detailed call data based on applied filters. |
| `Retrieve Transcript of Calls` | Retrieves transcripts of calls. |
| `Retrieve Aggregated Activity for Users by Date` | Retrieves aggregated activity for users for a specific date. |
| `Retrieve Aggregated Activity for Users by Date Range with Time Period` | Retrieves aggregated activity for users within a date range grouped by time period. |
| `Retrieve Daily Activity for Date Range` | Retrieves daily activity metrics within a specified date range. |
| `Retrieve All References for Email` | Retrieves all activity references associated with an email. |
| `Retrieve Data for Call` | Retrieves complete data for a specific call. |

### Triggers :

| **Trigger Name** | **Description** |
|---|---|
| `New Call` | This trigger is invoked when a new call is created in Gong. |

###
