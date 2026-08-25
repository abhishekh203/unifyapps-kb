# Gainsight connector

Source: https://www.unifyapps.com/docs/unify-integrations/gainsight
Section: integrations

---

Gainsight is a customer success platform that helps businesses drive retention, reduce churn, and maximize customer growth through data-driven insights and automation. It offers tools for customer health monitoring, engagement, and lifecycle management.

Integrating Gainsight enhances customer retention, reduces churn, and drives growth through data-driven insights and automation.

## Authentication

Before you begin, make sure you have the following information:

- `Connection Name`: Choose a descriptive name for your connection (e.g. "MyAppGainsightIntegration") to easily identify it within your integration settings.
- `Authentication Type`: Gainsight API uses **OAuth 2.0** for secure authentication and authorization.

### OAuth 2.0 Based Authentication

- Log in to your Control environment and navigate to `Integrations`
- Navigate to `API` to create or manage your API credentials.
- For more details on available scopes, endpoint-specific parameters, and additional functionalities such as managing community content, users, and webhooks, please refer to the full [Gainsight Customer Communities API Documentation](https://www.gainsight.com/customer-communities/)

## Actions

| Actions | Description |
|---|---|
| `Create company records` | Create a single or multiple company records in Gainsight NXT |
| `Create company team record` | Creates a company team record in Gainsight NXT |
| `Delete records` | Delete a specific record in the company object in Gainsight NXT |
| `Get team record details` | Retrieve the details of a team record in Gainsight NXT |
| `Search records` | Retrieve the details of records in Gainsight NXT |
| `Update company records` | Update company records in Gainsight NXT |
| `Update company team record` | Updates a company team record in Gainsight NXT |
| `Upsert person` | Upsert a single person in Gainsight NXT |
| `Upsert persons in bulk` | Upsert persons in bulk in Gainsight NXT |
