# Grafana Loki integration

Source: https://www.unifyapps.com/docs/unify-integrations/grafana-loki
Section: integrations

---

**Grafana Loki** is a log aggregation system designed for storing and querying logs from cloud-native applications. Unlike traditional logging tools, it indexes only metadata, making it highly efficient and cost-effective.

Integrating Grafana Loki enables seamless, scalable log monitoring within the Grafana dashboard alongside metrics and traces.

## Authentication

Before you begin, make sure you have the following information:

- `Connection Name`: Select a descriptive name for your connection, like "MyAppGrafanaLokiIntegration". This helps in easily identifying the connection within your application or integration settings.
- `Authentication Type`**:** Grafana Loki supports `Basic` and `No Authorization` for authentication.

### Basic Authentication

- Enter the username for the Grafana Loki instance.
- Enter the password for the Grafana Loki instance.
- Enter the Base URL for the Grafana Loki instance. Example: https://loki.example.com

### No Authorization

- Enter the Base URL for the Grafana Loki instance. Example: https://loki.example.com

## Actions

| Actions | Description |
|---|---|
| `Query logs` | Queries logs in Grafana Loki |
