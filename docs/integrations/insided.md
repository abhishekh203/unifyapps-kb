# Insided connector

Source: https://www.unifyapps.com/docs/unify-integrations/insided
Section: integrations

---

Insided is a customer community platform that helps businesses engage users, foster discussions, and provide peer-to-peer support. It integrates with CRMs and support tools to enhance customer experience and self-service.

Integrating your application with Insided (Gainsight’s Customer Communities) API enhances your community management capabilities by enabling advanced user management, content creation, and workflow automation.

## Authentication

Before you begin, make sure you have the following information:

- `Connection Name`: Choose a descriptive name for your connection (e.g. "MyAppInsidedIntegration") to easily identify it within your integration settings.
- `Authentication Type`: Insided API uses **OAuth 2.0** for secure authentication and authorization.

### OAuth 2.0 Based Authentication

- Log in to your Control environment and navigate to `Integrations`
- Navigate to `API` to create or manage your API credentials.
- For more details on available scopes, endpoint-specific parameters, and additional functionalities such as managing community content, users, and webhooks, please refer to the full [Gainsight Customer Communities API Documentation](https://www.gainsight.com/customer-communities/).

## Actions

| Actions | Description |
|---|---|
| `Search content` | Searches content in Insided |
| `Index content for search` | Indexes content for search in Insided |
| `Delete specific URLs` | Delete specific URLs from search in Insided |
| `Delete all content` | Delete all content from search in Insided |
