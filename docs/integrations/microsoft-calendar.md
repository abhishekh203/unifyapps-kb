# Microsoft Calendar

Source: https://www.unifyapps.com/docs/unify-integrations/microsoft-calendar
Section: integrations

---

**Microsoft Calendar** is a digital scheduling tool that allows users to organize events, set reminders, and manage meetings across time zones. It integrates seamlessly with Outlook and Microsoft 365 for real-time collaboration.

Integrating your application with Microsoft Calendar optimizes scheduling and time management, facilitating efficient coordination of meetings, events, and tasks.

## Authentication

Before you begin, make sure you have the following information:

- `Connection Name`**:** Select a descriptive name for your connection, like "MyAppCalendarIntegration". This helps in easily identifying the connection within your application or integration settings.
- `Authentication Type`**:** Microsoft Calendar supports OAuth authentication for integrations.

### OAuth Based Authentication

- Login into the Microsoft Azure Portal by clicking [here](https://portal.azure.com/).
- In the search Bar, search for `App Registration` and then Click on `new Registration`.
- Provide the Name and supported account types and register your app.
- The Client ID refers to the Application(client) ID
- Click on “`Add a credential or scope`” to generate the client secret.
- Copy this and store it securely to prevent unauthorized access.

![Frame 280.png](_img/a895edbe67db946c.webp)

## Permissions

| **Scope Code** | **Description** |
|---|---|
| `offline_access` | Maintain access to data you have given it access to |
| `Calendars.ReadWrite` | Have full access to user calendars |
| `Calendars.ReadWrite.Shared` | Read and write user and shared calendars |
| `OnlineMeetings.ReadWrite` | Read and create user's online meetings |
| `User.Read` | Sign in and read user profile |

## Sensitive Permissions

Admin permissions are required for the following scopes:

| **Scope Code** | **Description** |
|---|---|
| `OnlineMeetingRecording.Read.All` | Read all recordings of online meetings. |
| `OnlineMeetingTranscript.Read.All` | Read all transcripts of online meetings. |

## Actions

| **Actions** | **Description** |
|---|---|
| `Create a calendar` | Creates a calendar in Microsoft Calendar |
| `Create a calendar event` | Creates an event by calendar ID in Microsoft Calendar |
| `Delete a calendar event` | Deletes a calendar event by calendar and event ID in Microsoft Calendar |
| `Fetch event by ID` | Fetches event by ID from Microsoft Calendar |
| `Get Free/Busy Events` | Gets free/busy events from Microsoft Calendar |
| `Get a calendar` | Gets a calendar by its ID in Microsoft Calendar |
| `Get a calendar event` | Gets a calendar event by calendar ID in Microsoft Calendar |
| `Get attachments` | Gets attachment in Microsoft Calendar |
| `List all instances of an event` | Lists all instances of a recurring event in a specific calendar |
| `List calendars` | Lists calendars in Microsoft Calendar |
| `List events` | Lists events for a specific calendar in Microsoft Calendar |
| `Search calendar events (Batch)` | Searches calendar events in batches in Microsoft Calendar |
| `Search calendar (Batch)` | Searches calendars in batches in Microsoft Calendar |
| `Update a calendar event` | Updates an event by calendar and event ID in Microsoft Calendar |

## Triggers

| **Triggers** | **Description** |
|---|---|
| `Delete calendar event` | Triggers when a calendar event is deleted in Microsoft Calendar |
| `New calendar event` | Triggers when a new calendar event is created in Microsoft Calendar |
| `Updated calendar event` | Triggers when a calendar event is updated in Microsoft Calendar |
