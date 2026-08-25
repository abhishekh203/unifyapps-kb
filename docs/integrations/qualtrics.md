# Qualtrics connector

Source: https://www.unifyapps.com/docs/unify-integrations/qualtrics
Section: integrations

---

Qualtrics is an experience management platform that helps organizations collect, analyze, and act on customer, employee, product, and brand feedback. It provides AI-driven insights and automation to improve decision-making and user experiences.

Integrating your application with Qualtrics allows you to automate survey management processes, synchronize data, and enhance user experiences through API-based authentication.

## Authentication

Before you begin, make sure you have the following information:

- `Connection Name`: Select a descriptive name for your connection, like "MyAppQualtricsIntegration". This helps in easily identifying the connection within your application or integration settings.
- `Authentication Type`**:** Qualtrics supports API tokens for authentication.

### API Token based Authentication

- Log in to Qualtrics.
- Go to `Account Settings` in the user dropdown.
- Go to `Qualtrics IDs`.
- Click `Generate` if you haven't generated your token yet.

> **Note:** If you already have a valid API token, "`Generate Token`" will replace it with a new one (the old one will expire immediately). Any existing API calls will not work until they are updated to use the new token.

## Key Rotation

We highly recommend you rotate your API-token regularly (once a year) to help prevent theft. Note that rotating X-API-TOKEN will expire the current token and likely cause downtime.

## Actions

| Actions | Description |
|---|---|
| `Create contact` | Creates a contact in Qualtrics |
| `Create mailing list` | Creates a mailing list in Qualtrics |
| `Create reminder distribution` | Creates a reminder distribution in Qualtrics |
| `Distribute survey via email` | Distributes a survey via email in Qualtrics |
| `Get mailing list` | Retrieve the details of a mailing list via its ID |
| `Update contact` | Updates an existing contact in Qualtrics |
