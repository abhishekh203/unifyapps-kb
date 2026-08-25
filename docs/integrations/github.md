# Github connector

Source: https://www.unifyapps.com/docs/unify-integrations/github
Section: integrations

---

GitHub is a web-based platform for version control and collaboration, enabling developers to host, review, and manage code repositories. It simplifies teamwork with tools for branching, pull requests, and integration, fostering seamless software development workflows.

### **Authentication:**

Integrating your application with GitHub revolutionizes development workflows and automation, facilitating efficient, secure, and collaborative software engineering solutions.  Before you begin, ensure you have the following information:

`Connection Name` : Choose a meaningful name for your connection. This name helps you identify the connection within your application or integration settings. It could be something descriptive like "MyAppGitHubIntegration".

`Authentication Type` : GitHub supports three types of authentications. They are :

- Auth Token
- OAuth with Client Credentials
- OAuth
- GitHub App

`Hostname`:  Enter your GitHub Enterprise Server hostname. For example, github.example-organisation.com. Leave this field empty if you are using GitHub.com.

### Auth Token Based:

1. Log in to the GitHub website and click on your profile picture in the top right corner.
2. Select "Settings" from the dropdown menu.
3. In the left sidebar, click on "Developer settings".
4. Click on "Personal access tokens" in the left sidebar.
5. Click on "Generate new token" (for classic tokens) or "Generate new token (fine-grained").
6. Enter a descriptive name for the token and optionally set an expiration date.
7. Select the scopes/permissions you want to grant the token.
8. Click "Generate token" at the bottom of the page.
9. Copy the generated token immediately, as you won't be able to see it again after leaving the page.
10. Treat this token like a password - keep it confidential and secure.

### OAuth with Client Credentials Based:

1. Log in to the GitHub website and click on your profile picture in the top right corner.
2. Select "Settings" from the dropdown menu.
3. In the left sidebar, click on "Developer settings".
4. Click on "OAuth Apps" in the left sidebar.
5. Click on "New OAuth App".
6. Enter a descriptive name, callback URL and all other required fields.
7. Click "Register Application" at the bottom of the page.
8. Copy the client ID next to Client ID in your app.
9. Next to Client secrets, click "Generate a new client secret" to generate a client secret for your app.
10. Copy the generated client secret and use these credentials for further authentication purposes.

### OAuth Based :

1. Click on the "Authorize button".
2. You will be redirected to the permissions request screen.
3. Carefully review the permissions we're asking for. If you're comfortable with the permissions, click "Authorize Integartions-Unifyapps" button.
4. You will be automatically redirected back to our platform, and you should see a confirmation message that your Github account is now connected.

### GitHub App Based :

1. Log in to the GitHub website and click on your profile picture in the top right corner.
2. Select "Settings" from the dropdown menu.
3. In the left sidebar, click on "Developer settings".
4. Click on "GitHub Apps" in the left sidebar.
5. Click on "New GitHub App" and follow the [official GitHub documentation](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/registering-a-github-app) to create an app.
6. After creating the app, open your GitHub App settings and copy the App ID.
7. Navigate to the Private keys section and click Generate a private key.
8. Download or copy the generated private key.
9. Install your app using the [official GitHub documentation.](https://docs.github.com/en/apps/using-github-apps/installing-your-own-github-app)
10. Copy the installation ID in the app settings where the app is installed.

## Actions

| **Action Name** | **Description** |
|---|---|
| `Search for an action event` | Searches for an action event in GitHub. |
| `Compare two commits` | Compares two commits and returns the list of files changed between them. |
| `Create blob` | Creates a blob in GitHub. |
| `Create comment` | Creates a comment on an issue in GitHub. |
| `Create commit` | Creates a new commit in GitHub. |
| `Create file` | Creates a new file in a GitHub repository. |
| `Create issue` | Creates a new issue in GitHub. |
| `Create pull request` | Creates a new pull request in GitHub. |
| `Create pull request review comment` | Creates a review comment on a pull request in GitHub. |
| `Create reference` | Creates a reference in GitHub. |
| `Create repository` | Creates a new repository in a GitHub organization. |
| `Create tree` | Creates a tree in GitHub. |
| `Get User details` | Retrieves GitHub user details. |
| `Get commit` | Retrieves a Git commit object from GitHub. |
| `Get commit diff` | Retrieves the differences for a Git commit from GitHub. |
| `Get directory content` | Retrieves directory content from a GitHub repository. |
| `Get file content` | Retrieves file content from a GitHub repository. |
| `Get issue` | Retrieves an issue from GitHub. |
| `Get pull request (PR)` | Retrieves details of a pull request (PR) in GitHub. |
| `Get raw file content` | Retrieves raw file content from a GitHub repository. |
| `Get reference` | Retrieves a reference from GitHub. |
| `Get workflow run` | Retrieves a workflow run from GitHub. |
| `Iterate on repository files` | Iterates through all files in a GitHub repository. |
| `List branches` | Lists branches in a GitHub repository. |
| `List commits` | Lists commits on a repository branch within an optional time range. |
| `List pull request (PR) commits` | Lists all commits associated with a pull request (PR) in GitHub. |
| `List pull request files` | Lists all files in a pull request. |
| `List statuses for ref` | Lists commit statuses for a reference in GitHub. |
| `List workflow runs` | Lists workflow runs for a repository with optional filtering. |
| `Lists repositories` | Lists repositories in GitHub. |
| `Search issues and pull requests` | Searches issues and pull requests in GitHub. |
| `Trigger workflow` | Triggers a workflow in a GitHub repository. |
| `Update file` | Updates a file in a GitHub repository. |
| `Update issue` | Updates an issue in GitHub. |
| `Update reference` | Updates a reference in GitHub. |

**TRIGGERS**

| **Trigger Name** | **Description** |
|---|---|
| `Search for a trigger event` | Searches for a trigger event in GitHub. |
| `Iterate On All files in a github repo` | Iterates on all files from a GitHub repository. |
| `New issue polling` | Triggers when a new issue is created in GitHub. |
| `On Closed Issue Polling` | Triggers when an issue is closed in GitHub. |
| `On new or updated PR` | Triggers when a new or updated pull request (PR) is made in GitHub. |
| `On new or updated PR review` | Triggers when a pull request (PR) review activity is recorded in GitHub. |
| `On new or updated PR review comment` | Triggers when a pull request (PR) review comment is created or updated in GitHub. |
| `On new or updated PR review thread` | Triggers when a pull request (PR) review thread is created or updated in GitHub. |
| `On new or updated issue` | Triggers when a new or updated issue occurs in GitHub. |
| `On new or updated issue comment` | Triggers when a new or updated issue comment is made in GitHub. |
| `On new or updated milestone` | Triggers when a new or updated milestone occurs in a GitHub repository. |
