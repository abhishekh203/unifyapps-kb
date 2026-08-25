# OpsGenie connector

Source: https://www.unifyapps.com/docs/unify-integrations/opsgenie
Section: integrations

---

Opsgenie is a modern incident management and alerting platform that helps teams monitor systems, respond to incidents, and ensure service reliability. It enables real-time alerting, on-call scheduling, escalation policies, and integrations with various monitoring tools. By integrating the OpsGenie connector, applications can automate alert creation, manage incidents, and streamline operational workflows.

## Authentication

Integrating your application with OpsGenie enables seamless incident and alert management. Before starting, ensure you have the following information ready:

`Connection Name`**:** Choose a descriptive name for your connection. This helps you easily identify it within your application or integration settings, such as *"MyAppOpsGenieIntegration"*.

`Authentication Type`**:**   OpsGenie supports the following authentication method:

### **API Key Authentication:**

1. Log in to your OpsGenie account.
2. Click on your profile icon (top-right corner).
3. Navigate to Settings.
4. Go to API Key Management.
5. Click Create API Key.
6. Assign the required permissions (e.g., Read, Create, Update, Delete alerts).
7. Copy the generated API Key.
8. Paste the API Key into the connector configuration field.

## Actions :

| **Action Name** | **Description** |
|---|---|
| `Acknowledge alert` | Acknowledges an alert in Opsgenie |
| `Assign alert` | Assigns an alert in Opsgenie |
| `Close alert` | Closes an alert in Opsgenie |
| `Create alert` | Creates an alert in Opsgenie |
| `Update alert` | Updates an alert in Opsgenie |
| `Update alert description` | Updates alert description in Opsgenie |
| `Update alert priority` | Updates alert priority in Opsgenie |

## Triggers :

| **Trigger Name** | **Description** |
|---|---|
| `New / updated alert` | Triggers when an alert is created or updated in Opsgenie |
