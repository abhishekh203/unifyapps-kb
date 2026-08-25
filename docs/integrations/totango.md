# Totango connector

Source: https://www.unifyapps.com/docs/unify-integrations/totango
Section: integrations

---

Integrating your application with Totango enables access to customer success data and workflows within your automations. Totango helps customer success teams monitor account health, manage customer journeys, track engagement, and identify opportunities to improve retention and growth. By integrating Totango APIs, you can sync customer data, update account and user attributes, log activities, and automate customer success workflows using secure personal access tokens.

## Authentication:

Connecting your application to Totango requires a connection type and a personal access token. Before starting, make sure you have the following information:

- `Connection Name`: Choose a meaningful name for your connection. This name helps you identify the connection within your application or integration settings. It could be something descriptive like MyAppTotangoIntegration.
- `Connection Type`: Select the Totango service type you want to connect.

## Personal Access Token Based Authentication:

1. Log in to your `Totango` account.
2. Click your `profile` icon and select `Edit Profile`.
3. Open the `Integration tab.`
4. Click `Create Token`.
5. Enter a `token name` and choose an `expiration time`.
6. Click `Generate Token`.
7. Copy the generated token and paste it into the `Personal access token` field in your connection configuration.

## Actions :

| **Action Name** | **Description** |
|---|---|
| `Create a task` | Creates a task in Totango |
| `Delete a task` | Deletes a task in Totango |
| `Get account plan summary` | Get account plan summary in Totango |
| `List events` | List events in Totango |
| `Search accounts` | Searches for account in Totango |
| `Search events` | Searches for events in Totango |
| `Search users` | Searches for users in Totango |
| `Update a task` | Updates a task in Totango |
