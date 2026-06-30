# Setup Triggers

Source: https://www.unifyapps.com/docs/unify-automations/setup-triggers
Section: automations

---

## What is a Trigger?

A trigger is the **starting point** of an automation; it's what kicks off the automation process. It happens when certain **conditions** or **events** occur, such as receiving an email, updating a database record, or even at scheduled times.

## Types of Triggers

There are several types of triggers you can use depending on your needs:

### Connector-Based Triggers

These triggers work by **detecting events** within other applications.

For **example**, if you're using [Gmail](/docs/unify-automations/setup-triggers), [Zendesk](/docs/unify-automations/setup-triggers), [ServiceNow](/docs/unify-automations/setup-triggers), [Salesforce](/docs/unify-automations/salesforce), or similar platforms, connector-based triggers can initiate an automation whenever something specific happens in those apps, like getting a new email or a ticket update.

### API-Based Triggers

API-based triggers react to API calls. They come in two flavors:

- `Callable Triggers`: These can be triggered from within another automation or via API calls. Think of it as a way to **manually start** an automation process whenever needed.
- `Webhook Triggers`: Similar to callable triggers, webhook triggers respond to **HTTP requests** sent to a specific URL. They're great for integrating with external services that can send webhooks.

> **Note:** Use callable trigger if you want to send a response back to the api, webhook triggers send a 204 response by default for all successful runs.

### Scheduler Triggers

Scheduler triggers are perfect for automating tasks at regular intervals. You can set them up to run daily, weekly, monthly, or even at custom intervals. This is useful for **routine tasks** like sending out reports or cleaning up databases.
