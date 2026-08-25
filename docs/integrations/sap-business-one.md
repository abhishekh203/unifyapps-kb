# SAP Business One integration | connect with UnifyApps

Source: https://www.unifyapps.com/docs/unify-integrations/sap-business-one
Section: integrations

---

SAP Business One is an integrated enterprise resource planning (ERP) solution designed for small and medium-sized businesses. It streamlines core business functions like finance, sales, inventory, and operations in a single platform.

Integrating SAP Business One improves operational efficiency by centralizing business processes, providing real-time insights, and automating tasks.

## Authentication

Before integrating SAP Business One, ensure you have the following information:

- `Connection Name`**:** Choose a descriptive name for your SAP Business One connection to help you identify it within your application or integration settings. A meaningful name, like "MyAppSAPBusinessOneIntegration," helps maintain organization, especially when managing multiple integrations.
- `Project`**:** Select the project associated with this SAP Business One connection. Ensure that the project matches the specific workflow or application requiring this connection to maintain proper organization.
- `Server Name`**:** Enter the server name where SAP Business One is hosted. This is the network address or hostname required to establish the connection.
- `Username`**:** Provide the username used to log into SAP Business One. This should belong to an authorized user with the necessary permissions for integration.
- `Company DB`**:** Input the name of the company database in SAP Business One. This ensures the connection interacts with the correct database for your organization's data.
- `Port`**:** Specify the port number required for connecting to the SAP Business One server. Confirm the port number with your IT administrator to ensure proper configuration.
- `Password`**:** Enter the password for the provided username to securely authenticate with SAP Business One. Ensure this password is accurate and confidential.
- `DB Instance`**:** Input the name of the database instance if applicable. This is essential in environments where multiple database instances are in use to identify the correct instance.

## Actions

| **Action** | **Description** |
|---|---|
| `Create record in batches` | Creates new business partners in batches in SAP Business One, enabling efficient bulk data entry. |
| `Delete record` | Deletes a business partner in SAP Business One, removing unwanted or outdated partner information. |
| `Get record details` | Retrieves detailed information about a business partner in SAP Business One for review or updates. |
| `Search records` | Searches for records of a business partner in SAP Business One, aiding in quick data lookup. |
| `Update record` | Updates specific details of a business partner's record in SAP Business One. |
| `Update records in batches` | Updates records of multiple business partners in SAP Business One to streamline mass modifications. |
