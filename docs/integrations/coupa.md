# Coupa connector

Source: https://www.unifyapps.com/docs/unify-integrations/coupa
Section: integrations

---

Coupa is a cloud-based platform for Business Spend Management (BSM) that helps organizations streamline procurement, invoicing, expense management, and supply chain operations. It enables businesses to optimize costs, improve efficiency, and gain real-time visibility into spending across departments.

Integrating your application with Coupa brings a range of transformative capabilities to your organization’s spend management.

## Authentication

Before integrating Coupa, ensure you have the following information

- `Connection Name`**:** Choose a meaningful name for your connection. This name helps you identify the connection within your application or integration settings. It could be something descriptive like “MyAppCoupaIntegration”.
- `Authentication Type`**:** Coupa supports OAuth 2.0 authentication for integrations. This allows admins to take actions within Coupa without any user interference.

### OAuth Authentication

Using OAuth to connect your application with Coupa enhances security and enables controlled access to Coupa's APIs. Follow these steps to generate and configure OAuth credentials within Coupa:

1. Login to Coupa: Access your Coupa instance at [https://[your-instance-name].coupacloud.com/oauth2/clients](about:blank).
2. Navigate to OAuth Setup: Go to `Setup` then `Integrations` and then OAuth2/OpenID Connect Clients in the menu.
3. Create a New OAuth Client: Select “`Create`” to configure a new OAuth client and fill in the necessary details:
4. Select all the scopes that you plan to provide to Unify Apps. Example: core.common.read
5. After adding all selections, click `Save`.
6. Coupa displays the OAuth connection details, including the Secret. Copy and store the Identifier and the Secret for use in Unify Apps.

## Scopes

| **Scope Code** | **Description** |
|---|---|
| `core.common.read` | Basic read access for Coupa data |
| `core.common.write` | Basic edit access for Coupa data |
| `core.account_type.read` | Access to view account types |
| `core.account_type.write` | Access to create and update account types |
| `core.budget_line.read` | Access to view budget lines |
| `core.budget_line.write` | Access to create and update budget lines |
| `core.item.read` | Access to view items |
| `core.item.write` | Access to create and update items |
| `core.task.read` | Access to view tasks |
| `core.task.write` | Access to create and update tasks |
| `core.supplier.read` | Access to view suppliers |
| `core.supplier.write` | Access to create and update suppliers |
| `core.supplier_information_site.read` | Access to view supplier information sites |
| `core.supplier_information_site.write` | Access to create and update supplier information sites |
| `core.approval.read` | Access to view approvals |
| `core.approval.write` | Access to create and update approvals |
| `core.purchase_order.read` | Access to view purchase orders |
| `core.purchase_order.write` | Access to create and update purchase orders |

## Actions

| Actions | Description |
|---|---|
| `Cancel purchase order` | Cancels purchase order in Coupa |
| `Clone account type` | Clones a chart of accounts in Coupa |
| `Close purchase order` | Closes purchase order in Coupa |
| `Create account type` | Creates a chart of accounts in Coupa |
| `Create budget line` | Creates a budget line in Coupa |
| `Create item` | Creates an item in Coupa |
| `Create supplier` | Creates a supplier in Coupa |
| `Create task` | Creates a task in Coupa |
| `Delete task` | Deletes a task in Coupa |
| `Get account type by id` | Retrieves a chart of accounts by ID in Coupa |
| `Get budget line by id` | Retrieves a budget line by ID in Coupa |
| `Get item by id` | Retrieves an item by ID in Coupa |
| `Get supplier information site` | Retrieves supplier information sites by supplier ID in Coupa |
| `Get task by id` | Retrieves task by ID in Coupa |
| `Grant approval` | Perform approve action on an approval in Coupa |
| `Reject approval` | Perform reject action on an approval in Coupa |
| `Update budget line` | Updates a budget line record in Coupa |
| `Update item` | Updates an item in Coupa |
| `Update task` | Updates a task in Coupa |

## Triggers

| Triggers | Description |
|---|---|
| `New/Update account_type` | Polls periodically for new or updated account_type in Coupa |
| `New/Update budget_line` | Polls periodically for new or updated budget_line in Coupa |
| `New/Update item` | Polls periodically for new or updated item in Coupa |
| `New/Update supplier` | Polls periodically for new or updated supplier in Coupa |
| `New/Update task` | Polls periodically for new or updated task in Coupa |
