# Sprout Social integration | connect with UnifyApps

Source: https://www.unifyapps.com/docs/unify-integrations/sprout-social
Section: integrations

---

Sprout Social is a social media management platform that helps businesses streamline publishing, engagement, and analytics across multiple social networks. It offers powerful tools for scheduling posts, monitoring brand mentions, and analyzing performance.

Integrating your application with Sprout Social enables you to access social media analytics, automate workflows, and enhance engagement with your audience.

## Authentication

Ensure you have the following information ready for a seamless integration process:

- `Connection Name`: Select a descriptive name for your connection, like 'MyAppSproutIntegration'. This helps in easily identifying the connection within your application or integration settings.
- `Authentication Type`: Sprout Social uses API Tokens for authentication. This method ensures secure access to Sprout Social functionalities and data.

### API Token Based Authentication

- Log into your Sprout Social account and navigate to the account settings.
- Go to the '`API Tokens`' section under '`Reporting and Listening`'.
- Click on the “`Generate New Token`” button.
- Provide a name for the token and select the required scopes based on your use case.
- Click on “`Create Token`” and copy the generated token.

## Actions

| Actions | Description |
|---|---|
| `Get a publishing post` | Gets a publishing post by its ID in Sprout Social |
| `List customer groups` | Lists customer groups you created in Sprout Social |
| `List customer profiles` | Lists customer profiles by customer ID in Sprout Social |
| `List customer topics` | Lists the topics associated with your customer ID in Sprout Social |
| `List customer users` | Lists users that are active for your customer in Sprout Social |
| `List message tags` | Lists message tags (active and archived) created in Sprout Social |
| `List messages` | Lists detailed data and metadata about your Sprout messages in Sprout Social |
| `List messages within a topic` | Lists messages within a topic in Sprout Social |
| `List metrics within a topic` | Lists metrics within a topic in Sprout Social |
| `Query posts` | Queries for individual sent posts based on a filter criteria in Sprout Social |
| `Query profile level metrics` | Queries profile level metrics in Sprout Social |
