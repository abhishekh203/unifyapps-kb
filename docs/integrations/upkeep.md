# UpKeep connector

Source: https://www.unifyapps.com/docs/unify-integrations/upkeep
Section: integrations

---

UpKeep is a cloud-based maintenance and asset management software built for operational teams to streamline work orders, manage assets, and track inventory. It improves equipment reliability and maintenance efficiency.

Integrating UpKeep automates maintenance workflows and provides real-time visibility into operations across teams.

## Authentication

Before you begin, make sure you have the following information:

- `Connection Name`: Select a descriptive name for your connection, like "MyAppUpKeepIntegration". This helps in easily identifying the connection within your application or integration settings.
- `Authentication Type`**:** UpKeep uses a session token for authentication.

### Session token Based Authentication

- You can generate this token by sending a POST request to UpKeep's authentication API with your email and password.
- The session token must be included in all API requests.
- Keep this token confidential, as it grants access to your UpKeep account and services.

## Actions

| Actions | Description |
|---|---|
| `Create purchase order` | Creates a purchase order in UpKeep |
| `Create request` | Creates a request in UpKeep |
| `Create work order` | Creates a work order in UpKeep |
| `Find asset` | Find one or more assets in UpKeep |
| `Find location` | Find one or more locations in UpKeep |
| `Find part` | Find one or more parts in UpKeep |
| `Find user` | Find one or more users in the user's company in UpKeep |
| `Find vendor` | Find one or more vendors in UpKeep |
| `Update purchase order` | Updates a purchase order in UpKeep |

## Triggers

| Triggers | Description |
|---|---|
| `On new purchase order creation` | Triggers when a new purchase order is created in UpKeep |
| `On new request creation` | Triggers when a new request is created in UpKeep |
| `On new work order creation` | Triggers when a new work order is created in UpKeep |
| `On purchase order status change` | Triggers when a purchase order status changes in UpKeep |
| `On request approve` | Triggers when a request is approved in UpKeep |
| `On work order category change` | Triggers when a work order category changes in UpKeep |
| `On work order status change` | Triggers when a work order status changes in UpKeep |
