# Zendesk

Source: https://www.unifyapps.com/docs/unify-automations/zendesk
Section: automations

---

Zendesk is a customer service platform that helps businesses manage support, sales, and customer engagement through email, chat, social media, and other channels. It provides tools to improve customer experiences, automate workflows, and analyze performance.

Integrating Zendesk streamlines customer support, enhances communication, and boosts team efficiency through centralized workflows and automation.

## Authentication

Before you begin, make sure you have the following information:

- `Connection Name`: Select a descriptive name for your connection, like "MyAppZendeskIntegration". This helps in easily identifying the connection within your application or integration settings.
- `Subdomain`**:** Your Zendesk subdomain is part of your Zendesk URL. For instance, if your Zendesk URL is https://cname.zendesk.com, your subdomain would be cname.
- `Authentication Type`**:** Zendesk supports the following types of authentications
  - Basic
  - Auth Token
  - OAuth

### Basic Authentication

- Log in to your Zendesk account as an administrator.
- Navigate to "`Admin Cente`r" and then "`People`" and then "`Team Members`".
- Create a new agent or select an existing one.
- Ensure that the agent has the necessary permissions for your integration.
- Securely store the email address and password of the agent as they provide access to your Zendesk account.

### Auth Token Based Authentication

- Log in to your Zendesk account as an administrator.
- Navigate to "`Admin Center`" and then "`Apps and Integrations`" and then "`Zendesk API`".
- Allow access to Tokens and click to "`Activate`".
- Now click on `Add API token`.
- Click "`Copy`" and save the token securely as it provides access to your Zendesk account.

### OAuth Based Authentication

- Log in to your Zendesk account as an administrator.
- Navigate to `Admin Center` and then `Apps and Integrations`.
- Navigate to `Zendesk API` and then `OAuth Clients`.
- Click the plus icon to add a new OAuth client.
- Fill in the required information:
  - `Client Name`: A descriptive name for your application.
  - `Description`: Brief description of your integration.
  - `Redirect URLs`: The URL(s) where users will be redirected after authorization.
  - `Scopes`: Select the permissions your application needs.
- Click `Save`.
- Securely store the `Client ID` and Secret as they provide access to your Zendesk account.

## Actions

| Actions | Description |
|---|---|
| `Bulk update tickets` | Update multiple tickets identified by their Zendesk IDs |
| `Create article` | Creates a new article record in Zendesk |
| `Create custom object record` | Creates a new custom object record in Zendesk |
| `Create organization` | Creates an organization in Zendesk |
| `Create organization membership` | Add a user to an organization in Zendesk |
| `Create side conversation` | Creates a side conversation in Zendesk |
| `Create ticket` | Creates a ticket in Zendesk |
| `Create user` | Creates a new user record in Zendesk |
| `Delete custom object record by ID` | Delete a custom object record by ID in Zendesk |
| `Delete ticket` | Deletes a ticket in Zendesk |
| `Get agent status` | Gets the status of an agent in Zendesk |
| `Get comments by ticket ID` | Retrieves list of comments by ticket ID from Zendesk |
| `Get custom object record` | Get details of a custom object record by ID in Zendesk |
| `Get custom object records by external ID` | Get custom object records by external ID |
| `Get custom record object by external ID` | Gets custom object records by external ID in Zendesk |
| `Get group by name` | Gets group by name in Zendesk |
| `Get list of organizations by external ID` | Gets list of organizations by external ID |
| `Get list of tickets by external ID` | Get list of tickets by external ID |
| `Get organization details by ID` | Retrieves organization details via its ID from Zendesk |
| `Get ticket details by ID` | Gets ticket details by its ID from Zendesk |
| `Get user details by ID` | Gets user details by its ID from Zendesk |
| `List identities of user` | Lists identities of users by ID in Zendesk |
| `List ticket incidents` | Lists ticket incidents in Zendesk |
| `Merge tickets` | Merges tickets into target ticket in Zendesk |
| `Search Organization` | Searches organizations matching the criteria in Zendesk |
| `Search tickets` | Searches tickets using query in Zendesk |
| `Search user in an organization` | Searches user in an organization |
| `Search users` | Searches users in Zendesk |
| `Solve ticket` | Updates the status of a ticket to solved via its ID in Zendesk |
| `Update article` | Updates an article record in Zendesk |
| `Update custom object record` | Updates a custom object record in Zendesk |
| `Update organization` | Updates an organization in Zendesk |
| `Update ticket` | Updates a ticket in Zendesk |
| `Update user` | Updates a user record in Zendesk |
| `Uploads attachment` | Uploads a file to a ticket in Zendesk |

## Triggers

| Triggers | Description |
|---|---|
| `Change of agent status` | Triggers when an agent status is changed in Zendesk |
| `New or update user` | Triggers when a user is created or updated in Zendesk |
| `New or updated organization` | Triggers when an organization is created or updated in Zendesk |
| `New or updated records` | Triggers when records are created or updated in Zendesk |
| `New or updated ticket` | Triggers when a ticket is created or updated in Zendesk |
| `New organization` | Triggers when a new organization is created in Zendesk |
| `New ticket` | Triggers when a new ticket is created in Zendesk |
| `New user` | Triggers when a new user is created in Zendesk |
