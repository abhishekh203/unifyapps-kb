# 6sense connector

Source: https://www.unifyapps.com/docs/unify-integrations/6sense
Section: integrations

---

6sense is an account-based marketing and sales intelligence platform that helps organizations identify anonymous website visitors, enrich company and contact data, score leads, and gain predictive insights using AI. 
 By integrating 6sense APIs, you can enrich leads, identify companies, retrieve intent data, and automate sales and marketing workflows.

## Authentication

Before you begin, make sure you have the following information:

`Connection Name`: Choose a descriptive name for your connection, like “6sense connection”. This helps you easily identify the connection within your integration settings.

`Authentication Type`: 6sense supports **API token-based authentication**.

### API Token Based:

1. Log in to your 6sense account.
2. Go to **Settings** from the top navigation menu.
3. Navigate to **API Token Management**.
4. Click **Generate New API Token**.
5. Select the API group and name your token.
6. Select the Integrations.
7. Add Allowed domains, if you want to restrict the usage of API on selected domains. This option is only available for Company Identification API.

## ACTIONS **:**

| **Action Name** | **Description** |
|---|---|
| `Company firmographics` | Provides firmographics data for a company using 6sense |
| `Company identification` | Identifies anonymous website visitors by taking an IP address and matching it to an account using 6sense |
| `Lead scoring` | Scores a lead using 6sense |
| `Lead scoring and firmographics` | Scores a lead and provides firmographics data for the lead using 6sense |
| `People enrichment` | Enrich people (or lead or contact) level data using 6sense |
| Search people | Searches for people in an organisation using 6sense |
