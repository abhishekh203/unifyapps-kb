# Marketo

Source: https://www.unifyapps.com/docs/unify-integrations/marketo
Section: integrations

---

Integrating your application with Marketo enables seamless marketing automation by allowing you to manage leads, custom activities, campaigns, and marketing assets through REST APIs. Automate lead synchronization, track customer interactions, and integrate marketing workflows with your business applications to improve operational efficiency and customer engagement.

## Authentication:

Connect your application to Marketo Engage to securely automate lead management, synchronize marketing data, and integrate customer engagement workflows using Marketo REST APIs. Before you begin, ensure you have the following information:

`Connection Name` : Choose a meaningful name for your connection. This name helps you identify the connection within your application or integration settings. It could be something descriptive like "MyAppMarketoIntegration".

`Authentication type` **:** Select the authentication type you would like to proceed with.

- `Client Credentials`
- `Access Token`

`Marketo domain` : If your Marketo REST API base URL is https://example.mktorest.com/rest, then your domain will be example. Follow the [Marketo official](https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/rest/base-url)documentation to find your domain.

### Client Credentials Based:

**1. Create API Role:**

- Log in to[Adobe Marketo Engage](https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/rest/rest-api).
- Navigate to Admin → Users & Roles → Roles.
- Click `New Role`.
- Enter a Role Name and, optionally, a Description.
- Grant the required API permissions.
- Click `create`.

**2. Create API User:**

- Navigate to Admin → Users & Roles → Users.
- Click`Invite New User`.
- Enter the required user details (First Name, Last Name, and Email Address).
- Click `Next`.
- Check the API Only box and assign the API role you created.
- Click `Next`, then `Send` to create the API user.
3. **Create a LaunchPoint Custom Service**:
- Navigate to Admin → Integration → LaunchPoint.
- Click `New` and select `New Service`.
- Enter a Display Name for the service.
- Select Custom from the Service dropdown.
- Select the API user created and click `Create`.
- Click `View details` and copy the generated `client ID` and `client secret` and store them securely for further authentication purposes.

### Access Token Based:

1. Log in to your `Marketo account`.
2. Navigate to `Admin`.
3. In the left navigation panel, select `API` `Token`.
4. Open the newly created application and go to the `Credentials section`.
5. Enter the required details and select scopes.
6. Click `Generate Token`.
7. Copy the generated token and use it for further authentication purposes.

## Actions :

| **Action Name** | **Description** |
|---|---|
| `Add Custom Activity` | Adds custom activities in Marketo |
| `Add Lead to List` | Adds a lead to a list in Marketo |
| `Change Lead Program Status` | Changes a lead's program status in Marketo |
| `Create or Update Lead` | Creates or updates a lead in Marketo |
| `Get Campaigns (Cursor-based Pagination)` | Fetches all campaigns from Marketo using cursor-based pagination |
| `Get Campaigns` | Lists all campaigns in Marketo |
| `Get Emails` | Lists all emails in Marketo |
| `Get Lead By ID` | Retrieves a single Marketo lead record by its ID |
| `Get Program By ID` | Retrieves a Marketo program asset by its ID |
| `Get Program Members` | Retrieves members of a Marketo program with optional filtering |
| `Get Programs` | Lists all programs in Marketo |
| `Remove Lead from List` | Removes leads from a list in Marketo |
| `Schedule Smart Campaign` | Schedules a smart campaign in Marketo |
| `Send Simple Email` | Sends a sample email to the specified email address in Marketo |
| `Submit Form` | Submits a form in Marketo |
| `Upsert Token` | Creates or updates a token in Marketo |
| `Upsert Custom Objects` | Creates or updates custom objects in Marketo |
