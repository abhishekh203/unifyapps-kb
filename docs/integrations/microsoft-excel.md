# Microsoft Excel integration | connect with UnifyApps

Source: https://www.unifyapps.com/docs/unify-integrations/microsoft-excel
Section: integrations

---

**Microsoft Excel** is a powerful spreadsheet software by Microsoft used for data organization, analysis, visualization, and automation through formulas and macros. It supports a wide range of functions, from basic calculations to advanced data modeling.

Integrating Excel helps seamlessly manage, analyze and visualize structured data in real-time across systems or workflows.

## Authentication

Before you begin, make sure you have the following information:

- `Connection Name`: Select a descriptive name for your connection, like "`MyAppExcelIntegration`". This helps in easily identifying the connection within your application or integration settings.
- `Authentication Type`**:** Select the type of authentication for connecting to your Slack account.
  - OAuth
  - OAuth with Client Credentials

### OAuth Based Authentication

- Select OAuth as the provide the appropriate scopes.
- A pop-up screen opens, sign in to your Microsoft account.
- Login into the Microsoft Azure Portal by clicking [here](https://portal.azure.com/).
- In the search Bar, search for App Registration and then Click on new Registration.
- Provide the Name and supported account types and register your app.
- The Client ID refers to the Application(client) ID.
- Click on **“**`Add a credential or scope`**”** to generate the client secret.
- Copy and store these securely to prevent unauthorised access.

## Permissions

| **Scope Code** | Description |
|---|---|
| `Files.ReadWrite.All` | Have full access to all files user can access |
| `offline_access` | Maintain access to data you have given it access to |
| `Sites.ReadWrite.All` | Edit or delete items in all site collections |
| `User.Read` | Sign in and read user profile |
| `TeamSettings.ReadWrite.All` | Create, read, update, and delete all teams and channels, including private channels and sensitive settings. |

## Sensitive Permissions

| **Scope Code** | Description |
|---|---|
| `User.Read.All` | Read all users' full profiles |

## Actions

| **Actions** | Description |
|---|---|
| `Add rows in table` | Add rows in batches in Microsoft Excel |
| `Add table` | Add table in Microsoft Excel |
| `Add worksheet` | Add worksheet in Microsoft Excel |
| `Delete row` | Delete a row in Microsoft Excel |
| `Download file` | Downloads the contents of a file in Microsoft Excel |
| `Fetch permissions` | Fetch permissions for files and folders in Microsoft Excel |
| `Get file metadata` | Get file metadata in Microsoft Excel |
| `Get onedrive drive id` | Get OneDrive drive ID in Microsoft Excel |
| `Get organization` | Get organizations in Microsoft Excel |
| `Get rows` | Get rows from table in Microsoft Excel |
| `Get teams of a user` | Get teams of a user by user ID in Microsoft Excel |
| `Get user details from email` | Get details of a user by user email in Microsoft Excel |
| `List sharepoint sites` | List SharePoint sites in Microsoft Excel |
| `List tables` | List table objects in Microsoft Excel |
| `List worksheets` | List worksheet objects in Microsoft Excel |
| `Search workbooks` | Search workbook items in Microsoft Excel |
| `Update row` | Update a row in Microsoft Excel |
