# SAP Concur Integration

Source: https://www.unifyapps.com/docs/unify-integrations/sap-concur
Section: integrations

---

SAP Concur is a cloud-based solution for managing travel, expenses, and invoices, streamlining processes to improve efficiency and compliance. It provides real-time insights and automation for expense tracking, approvals, and reporting.

Integrating SAP Concur simplifies expense management, automates workflows, and ensures compliance, while providing real-time visibility into spending and reducing manual errors.

## Authentication

Before integrating SAP Concur, ensure you have the following information:

- `Connection Name`**:** Choose a descriptive name for your SAP Concur connection to help you identify it within your application or integration settings. A meaningful name, like "MyAppSAPConcurIntegration," helps maintain organization, especially when managing multiple integrations.
- `Client ID`**:** Enter the Client ID provided by SAP Concur. This is a unique identifier associated with your SAP Concur account and is required for API authentication.
- `Client secret`**:** Input the Client Secret associated with the SAP Concur Client ID. This is used in combination with the Client ID to securely authenticate and access SAP Concur APIs. Ensure this information is kept confidential.
- `Username`**:** Provide the username of the SAP Concur account. This is typically the email or username used to log in to your SAP Concur instance.
- `Password`**:** Enter the password for the provided SAP Concur username. This password should match the credentials used for logging into SAP Concur. Keep this secure.
- `Data Center URI`**:** Input the Data Center URI for your SAP Concur account. This URI specifies the endpoint associated with your SAP Concur datacenter. For example, it could be https://us.api.concursolutions.com. Verify the URI with your SAP Concur documentation or support.

## Actions

| Action | Description |
|---|---|
| `Create list item` | Creates a new list item in SAP Concur for structured data organization and management. |
| `Create users (batch)` | Adds multiple users in a single batch operation to SAP Concur, streamlining user onboarding. |
| `Create vendors` | Adds new vendors to SAP Concur for managing vendor-related transactions and details. |
| `Delete list item` | Deletes a specific list item from SAP Concur to remove outdated or irrelevant entries. |
| `Get attendee types (batch)` | Retrieves all attendee types in batch from SAP Concur for efficient event or meeting management. |
| `Get expense group configurations (batch)` | Fetches all expense group configurations in batch from SAP Concur for streamlined expense setup. |
| `Get expense report` | Retrieves an individual expense report from SAP Concur for review or processing. |
| `Get invoice details` | Fetches detailed invoice data from SAP Concur for billing and payment reconciliation. |
| `Get lists` | Retrieves all lists available in SAP Concur for data tracking and management. |
| `Retrieve entry image` | Retrieves the URL of an entry image from SAP Concur for reference or audit purposes. |
| `Retrieve user profile data` | Fetches profile data of a user from SAP Concur for managing account information. |
| `Retrieve vendors (batch)` | Retrieves a batch of vendor details from SAP Concur for bulk vendor management. |
| `Search expense reports (batch)` | Searches and retrieves multiple expense reports in a single batch operation from SAP  Concur. |
| `Search users (batch)` | Searches for users in batch from SAP Concur for efficient account lookup and management. |
| `Submit expense report through workflow` | Submits a new expense report through the defined workflow in SAP Concur for approval processing. |
| `Update user` | Updates the information of a specific user in SAP Concur for maintaining up-to-date records. |
| `Update users (batch)` | Updates multiple user records in batch within SAP Concur for efficient data management. |
| `Update vendors (batch)` | Updates multiple vendor details in SAP Concur to ensure accurate and updated vendor information. |
