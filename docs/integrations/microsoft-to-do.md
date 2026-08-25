# Microsoft to Do integration | connect with UnifyApps

Source: https://www.unifyapps.com/docs/unify-integrations/microsoft-to-do
Section: integrations

---

Microsoft To Do is a cloud-based task management application that helps users organize their daily activities, tasks, and goals. It allows for creating task lists, setting reminders, and collaborating across devices.

Its intuitive interface and cross-device sync make it easy to stay organized and productive from anywhere.

## Authentication

Before you begin, make sure you have the following information:

- `Connection Name`: Select a descriptive name for your connection, like "MyMicrosoftToDo". This helps in easily identifying the connection within your application or integration settings.
- `Authentication Type`**:** Select the type of authentication for connecting to your “Microsoft To Do” account. Microsoft To Do supports
  - OAuth with client credentials
  - OAuth 2.0 Authentication for authentication.

> **Note:** In the Redirect URL section paste the following link [https://webhooks-global.ext-alb.qa.unifyapps.com/api/connector-auth-callback/oauth](https://webhooks-global.ext-alb.qa.unifyapps.com/api/connector-auth-callback/oauth).

### OAuth Based Authentication

- Enter your Tenant ID (Directory tenant ID).
- Select the scopes required.
- Click on Authorize.
- After you are redirected, login to your Microsoft account and approve the scopes needed.

### OAuth with Client Credentials

To authenticate using the Client Credentials flow, you need a Client ID and Client Secret. This flow is used when accessing user data (like mailboxes) without direct user login. It requires admin consent to access organizational resources.

- Login into the Microsoft Azure Portal by clicking [here](https://portal.azure.com/).
- In the search Bar, search for `App Registration` and then Click on `new Registration`.
- Provide the Name and supported account types and register your app.
- The Client ID refers to the Application(client) ID.
- Click on **“**`Add a credential or scope`**”** to generate the client secret.
- Copy and store these securely to prevent unauthorised access.
- Enter your Tenant ID (Directory tenant ID).
- Select the scopes required.
- You need user consent to access the mailbox

  ![Frame 280 (1).png](_img/0d884d4fc57ec485.webp)

## Permissions

| **Scope Code** | **Description** |
|---|---|
| `Group.ReadWrite.All` | Read/write all groups data |
| `offline_access` | Have full access to all files user can access |
| `Tasks.ReadWrite` | Manage user's tasks and lists |
| `Group.Read.All` | Read all groups' basic info |

## Sensitive Permissions

| **Scope Code** | **Description** |
|---|---|
| `Group.Read.All` | Read all groups' basic info |
| `Group.ReadWrite.All` | Read/write all groups data |

## Actions

| **Actions** | **Description** |
|---|---|
| `Create linkedResource` | Create a linkedResource in Microsoft To Do |
| `Create task` | Create a task in Microsoft To Do |
| `Create task list` | Create a task list in Microsoft To Do |
| `Delete linkedResource` | Delete a linkedResource in Microsoft To Do |
| `Delete task` | Delete a task in Microsoft To Do |
| `Delete task list` | Delete a task list in Microsoft To Do |
| `Get linkedResource` | Get a linkedResource in Microsoft To Do |
| `Get task` | Get a task in Microsoft To Do |
| `Get task list` | Get a task list in Microsoft To Do |
| `List linkedResource` | List a linkedResource in Microsoft To Do |
| `List Task List` | List all task list in Microsoft To do |
| `Update Linked Resource` | Update a linked resource in microsoft to do |
| `Update Task` | Update a task in microsoft to do |
| `Update task list` | Update a list of tasks in microsoft to do |
