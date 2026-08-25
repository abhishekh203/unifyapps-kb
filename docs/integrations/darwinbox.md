# Darwinbox connector

Source: https://www.unifyapps.com/docs/unify-integrations/darwinbox
Section: integrations

---

Darwinbox enables businesses to manage human resources, employee lifecycle operations, payroll, attendance, and workforce automation through a unified HRMS platform. By integrating the Darwinbox connector, applications can automate HR workflows, synchronize employee data, and streamline organizational processes across systems.

## Authentication

Integrating your application with Darwinbox enables secure access to employee and HR-related data. Before starting, ensure you have the following information ready:

`Connection name` **:** Choose a descriptive name for your connection. This helps you easily identify the connection within your application or integration settings, such as "MyAppDarwinboxIntegration".

`Authentication type`**:** Darwinbox supports the following authentication method:

- Basic Authentication

## Basic authentication

To configure the Darwinbox connector, collect the following credentials from your Darwinbox administrator or account settings:

`Username` **:**The username used to authenticate with your Darwinbox account.

`Password` **:**The password corresponding to the provided username.

`API Key` **:**The secure API key generated within the Darwinbox admin settings for programmatic access.

1. Log in to your Darwinbox admin account.
2. Navigate to the Admin or Developer/API Settings section.
3. Locate the API Key or Access Token section.
4. Generate or copy the API key for integration use.

`Subdomain`**:**The unique prefix of your Darwinbox URL (e.g., 'companyname' in https://companyname.darwinbox.com).

## **Actions :**

| **Action Name** | **Description** |
|---|---|
| `Activate pending employees` | Activates pending employees in Darwinbox using the import API |
| `Add activity` | Adds one or more activities in Darwinbox |
| `Add attendance punches` | Adds attendance punches in Darwinbox |
| `Add backdated attendance` | Adds backdated attendance in Darwinbox |
| `Add project team` | Adds employees to a project team in Darwinbox |
| `Add standard document` | Adds standard documents (like PAN, Aadhar, Resume, etc.) for an employee in Darwinbox |
| `Add tags to candidate profile` | Adds tags to candidate profile in Darwinbox |
| `Add or update business unit master` | Adds or updates business unit masters in Darwinbox |
| `Add or update project` | Adds or updates projects in Darwinbox |
| `Archive requisition` | Archives requisition in Darwinbox |
| `Assign permissions` | Assigns a configured permission group to users and employees in Darwinbox |
| `Download form attachments` | Downloads form attachments from Darwinbox |
| `Fetch candidate details` | Gets candidate details assigned to a background verification vendor from Darwinbox |
| `Fetch candidate list` | Lists candidates assigned to a background verification vendor in Darwinbo |
| `Submit verification report` | Submit verification report in Darwinbox |
| `Create cost center master` | Creates a cost center master in Darwinbox |
| `Create designation` | Creates designation masters in Darwinbox |
| `Create location masters` | Creates one or more location masters in Darwinbox |
| `Create requisition` | Creates requisition in Darwinbox |
| `Create or update designation name` | Creates or updates designation names in Darwinbox |
| `Create or update position master` | Creates or updates position masters in Darwinbox |
| `Get CTC breakup computation` | Gets the CTC breakup for an employee in Darwinbox |
| `Deactivate active employee` | Deactivates active employees in Darwinbox |
| `Delete pending employee` | Deletes pending employees in Darwinbox using the import API |
| `Import extra payments` | Imports extra payments for an employee in Darwinbox |
| `Fetch advance travel` | Fetches advance travel from Darwinbox |
| `Fetch approved travel requests` | Fetches approved travel requests from Darwinbox |
| `Fetch cancelled travel requests` | Fetches cancelled travel requests from Darwinbox |
| `Fetch candidate CTC data` | Fetches candidate CTC data from Darwinbox |
| `Fetch employee CTC data` | Fetches employee CTC data from Darwinbox |
| `Fetch employee global CTC data` | Fetches employee CTC data from Darwinbox |
| `Fetch expense details` | Fetches expense details from Darwinbox |
| `Fetch global extra deductions` | Fetches global extra deductions from Darwinbox |
| `Fetch global extra payments` | Fetches global extra payments from Darwinbox |
