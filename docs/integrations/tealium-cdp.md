# Tealium CDP connector

Source: https://www.unifyapps.com/docs/unify-integrations/tealium-cdp
Section: integrations

---

Tealium CDP  helps businesses unify, manage, and activate customer data in real-time across multiple channels. It enables personalized experiences, data governance, and seamless integration with marketing and analytics tools.

Integrating your application with Tealium CDP enables real-time customer data collection, unification, and activation across multiple platforms. Tealium's API allows you to manage visitor profiles, track user interactions, and optimize audience segmentation programmatically.

## Authentication

Before starting, make sure you have the following information:

- `Connection Name`**:** Choose a meaningful name for your connection. This name helps you identify the connection within your application or integration settings. It could be something descriptive like "MyAppTealiumCDPIntegration".
- `Account`**:** Enter the name of your account.
- `Profile`**:** Log in to your Tealium account, navigate to the Admin menu, select Manage Profiles to view profile name.
- `Username`**:** Log in to your Tealium account, navigate to the Admin menu, and click Manage Users to view the users. Click on user to view username.
- `Authentication Type`**:** Tealium CDP provides JWT authentication.

### JWT Based Authentication

1. Log in to your Tealium CDP account.
2. Navigate to the `Admin Menu` and select Edit/View user settings.
3. Click on `API key`.
4. Click `Generate Key` to create a new API key.
5. Use this API Token for authentication purposes.

## Actions

| Actions | Description |
|---|---|
| `Delete visitor` | Deletes a visitor in Tealium CDP |
| `Get historical visitor` | Retrieves historical visitor record in Tealium CDP |
| `Get transaction` | Retrieves information about transaction status in Tealium CDP |
| `Get visitor` | Retrieves information about visitor record in Tealium CDP |
| `Get visitor ID attributes` | Retrieves list of visitor ID attributes available in Tealium CDP account |
| `Get visitor record` | Retrieves visitor records with the option to prioritize live or historical data in Tealium CDP |
