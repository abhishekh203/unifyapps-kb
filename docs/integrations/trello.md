# Trello connector

Source: https://www.unifyapps.com/docs/unify-integrations/trello
Section: integrations

---

Trello is a collaboration and project management platform that helps teams organize tasks using boards, lists, and cards. It provides REST APIs that allow developers to automate workflows, manage boards and cards, collaborate with team members, and integrate task tracking into their applications.

## Authentication

Integrating your application with Trello allows you to execute board and card operations, manage lists, add comments, assign members, and automate workflows. Before starting, ensure you have the following information:

- `Connection Name`: Choose a meaningful name for your connection. Example: "MyAppTrelloIntegration".
- `API Key`: Enter your Trello API key generated from the Trello Developer Portal.
- `API Token`: Enter the API token associated with your Trello account to authorize API requests.

## Actions :

| **Actions** | **Description** |
|---|---|
| `Create Board` | Creates a new board in Trello. |
| `Delete Board` | Deletes an existing board. |
| `List Boards` | Retrieves all boards accessible to the authenticated user. |
| `Create List` | Creates a new list within a board. |
| `List Lists` | Retrieves all lists from a specified board. |
| `Create Card` | Creates a new card in a specified list. |
| `Update Card` | Updates card details such as name, description, due date, or members. |
| `Delete Card` | Deletes a specified card. |
| `Move Card` | Moves a card from one list to another. |
| `Add Comment` | Adds a comment to a card. |
| `Create Checklist` | Creates a checklist within a card. |
| `Add Checklist Item` | Adds an item to an existing checklist. |
| `Create Label` | Creates a label on a board. |
| `Add Label to Card` | Associates a label with a card. |
| `Invite Member to Board` | Invites a member to collaborate on a board. |
| `Create Webhook` | Creates a webhook to receive real-time updates from Trello. |
