# People.AI connector

Source: https://www.unifyapps.com/docs/unify-integrations/people-ai
Section: integrations

---

# **People.AI**

People.ai is an AI-driven revenue intelligence platform that automatically captures every email, call, and meeting, and maps it directly to your deals, accounts, and CRM — eliminating manual data entry and giving sales teams a complete, real-time picture of pipeline health.

Integrating your application with People.ai empowers you to unlock actionable revenue insights, automate go-to-market activity tracking, and enable your sales, marketing, and RevOps teams to make smarter, data-driven decisions that accelerate growth.

### Authentication

Ensure you have the following information ready for a seamless integration process:

- `Connection Name`: Select a descriptive name for your connection, like "MyAppPeopleAIIntegration". This helps in easily identifying the connection within your application or integration settings.
- `Authentication Type`: PeopleAI supports the following type of authentication for connecting to your PeopleAI account:

#### Access Token Based Authentication :

- Go to https://app.people.ai and sign in with your admin credentials.
- Once logged in, click on your profile icon or navigate to the Admin Settings panel, accessible from the top-right menu or the gear icon.
- Within the admin panel, look for a section labeled API Keys or Integrations.
- Click Generate or Create New API Key. The platform will produce:
- Treat this token with high confidentiality, as it allows access to your People AI instance.

### ACTIONS :

| **Action** | **Description** |
|---|---|
| `Bulk push conference activities` | Ingests multiple conference activity records in a single request. |
| `Bulk push email activities` | Submits a batch of email activity records to People.ai in one call. |
| `Bulk push meeting activities` | Pushes multiple meeting activity records to People.ai simultaneously. |
| `Delete call activity` | Permanently removes a specific call activity record by its unique identifier. |
| `Delete chat activity` | Deletes a specific chat activity record by its unique identifier. |
| `Push call activity` | Submits a single call activity record to People.ai. |
| `Push chat activity` | Sends a single chat or messaging activity record to People.ai. |
| `Push conference activity` | Submits a single conference activity record to People.ai. |
| `Push email activity` | Sends a single email activity record to People.ai. |
| `Push meeting activity` | Submits a single meeting activity record to People.ai. |
| `Get activity by CRM ID` | Retrieves a specific activity record using its CRM identifier. |
| `Get activity participants by CRM ID` | Returns all participants associated with a specific activity via its CRM record ID. |
| `List activities` | Retrieves all captured activities across the organization. |
| `List activities of type` | Fetches a paginated list of activities filtered by a specific activity type. |
| `List activity participants` | Returns a paginated list of all participants across activities in the organization. |
| `List participants` | Returns all participants associated with a specific activity. |
| `Get contact` | Retrieves full profile and engagement details for a specific contact. |
| `Get contact by CRM ID` | Looks up a contact record in People.ai using its CRM identifier. |
| `Get contact by email` | Retrieves a contact record from People.ai by the contact's email address. |
| `List contacts` | Returns a paginated list of all contact records in the organization. |
| `List contact engagement insights` | Retrieves AI-generated engagement insights for a specific contact. |
| `Get lead` | Fetches complete details for a specific lead record. |
| `Get lead by CRM ID` | Retrieves a lead record from People.ai using its CRM system identifier. |
| `Get lead by email` | Looks up a lead in People.ai by email address. |
| `List leads` | Returns a paginated list of all lead records in the organization. |
| `List lead engagement insights` | Provides AI-powered engagement insights for a specific lead. |
| `Get opportunity` | Fetches full details for a specific opportunity. |
| `Get opportunity by CRM ID` | Fetches a specific opportunity record using its CRM system identifier. |
| `List opportunities` | Lists all opportunities in the CRM pipeline. |
| `List opportunity engagement insights` | Returns AI-generated engagement insights for a specific opportunity. |
| `Get account` | Retrieves detailed information for a specific account. |
| `List accounts` | Returns a paginated list of all account records in the organization. |
| `List account engagement scores` | Retrieves engagement score data across all accounts in the organization. |
| `List engagement levels` | Returns engagement level definitions and current scores for accounts or contacts. |
| `Get team by CRM ID` | Fetches a specific team record using its CRM system identifier. |
| `Get team by ID` | Retrieves full details for a specific team using the People.ai internal identifier. |
| `List teams` | Returns a paginated list of all teams defined in the organization. |
| `Get team member` | Returns profile and performance data for a specific team member. |
| `Get team member by CRM ID` | Looks up a team member record using their CRM system identifier. |
| `Get team member by email` | Retrieves a team member's profile by their email address. |
| `List team members` | Retrieves the full list of team members in the organization. |
| `List team members by team CRM ID` | Returns all team members belonging to a specific team via its CRM record ID. |
| List team members by team ID | Retrieves all members of a specific team using the People.ai internal identifier. |
