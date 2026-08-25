# Khoros connector

Source: https://www.unifyapps.com/docs/unify-integrations/khoros
Section: integrations

---

Khoros is a customer engagement platform that helps brands manage social media, community forums, and messaging interactions to enhance customer experience. It offers AI-powered analytics, automation, and collaboration tools for marketing, support, and engagement teams.

Connecting your application to a Khoros account enables seamless integration with its suite of customer engagement and social media management tools, enhancing collaboration, automating workflows, and simplifying digital interactions across your organization.

## Authentication

Before you begin, make sure you have the following information:

- `Connection Name`**:** Choose a descriptive name for your connection. This will help you easily identify it within your application or integration settings. For example "MyAppKhorosIntegration".
- `Authentication Type`**:** Khoros supports OAuth authentication for integrations.

## OAuth Based Authentication

1. To obtain credentials, contact your company admin-contact Khoros [support](https://uat.unifyapps.com/%22https://community.khoros.com/t5/Case-Portal/bd-p/caseportal/%22) to request a client ID and client Secret for Khoros Marketing.
2. Enter the `Client ID` and `Client Secret` in the Khoros connection setup and click "`Authorize`".
3. You will be redirected to the permissions page; review the permissions and click "`Allow`".
4. Once authorized, a new Khoros connection will be successfully created.

## Actions

| Actions | Description |
|---|---|
| `Delete message` | Delete message by ID in Khoros |
| `List streams` | List all available streams for a company in Khoros |
| `List survey data` | List all survey data for a set of streams in Khoros |
| `Post message` | Publish a new marketing message for the target initiative in Khoros |
| `Update message` | Update marketing messages for the target initiative in Khoros |
