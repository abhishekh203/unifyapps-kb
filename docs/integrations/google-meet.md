# Google Meet connector

Source: https://www.unifyapps.com/docs/unify-integrations/google-meet
Section: integrations

---

Integrating your application with Google Meet transforms your communication strategy by enabling seamless video conferencing for global teams, leveraging real-time collaboration features, and driving instant connection—all while maintaining enterprise-grade security and reliable performance.

## Authentication:

Before you begin, ensure you have the following information:

- `Connection Name:` Choose a descriptive name for your Google meet connection to help you identify it within your application or integration settings. A meaningful name, like "MyAppGoogleMeetIntegration," helps maintain organization, especially when managing multiple integrations.
- `Authentication Type:` Google meet supports following type of authentication. **1. Service Account Authentication** **2. OAuth**

### Service Account Based Authentication

Create a service account by following these steps. 
 1) Go to [Google console](https://console.developers.google.com/) and sign in with your google account

2) Create a project under **IAM & Admin**->**Manage Resources** under menu section

3) Enter the project name and click on **Create**

4) To Turn on the API services  for the service account go to APIs & Services -> Library  as shown below

5) Enable Google meet API  services here for your service account

6) Set up oAuth consent screen to configure OAuth consent for your application,Go to APIs & Services → OAuth consent screen    
 7) Select the userType and details like Appname, User support email and developer contact information and click on save as shown below

8) Create a service account By clicking on APIs & Services → Credentials  on menu

9) Click on create credentials → Service Account and enter the service account name and description and press save and continue

10) To create a new key for your service account click on Keys → Add Key, then select Create new key with JSON type, and save the downloaded private key JSON file as shown below

After you are done with creating the service account add domain-level access to the service account (based on client ID) by following these [**steps**](https://developers.google.com/cloud-search/docs/guides/delegation#delegate_domain-wide_authority_to_your_service_account). (either by logging in as super administrator or giving your service account details to super administrator)

Use the service account email, private key, and a sample user email to authenticate the connection.

### OAuth Based Authentication

The OAuth  method involves signing in with your Google account credentials on Google's Single Sign-On page, and granting the necessary permissions to UnifyWorkflows, For **OAuth**-based authentication, you'll need to perform the following steps to generate access credentials:

Create an Oauth Credentials by following these steps. 
 1) Go to [Google console](https://console.developers.google.com/) and sign in with your google account.

2) Create a project under **IAM & Admin**->**Manage Resources** under the Menu section.

3) Enter the project name and click on **Create**

4) To Turn on the API services  for the OAuth Client ID go to APIs & Services -> Library  as shown below

5) Turn on Google meet API  services here for your OAuth Client ID authentication.

6) Set up oAuth consent screen to configure OAuth consent for your application,Go to APIs & Services -> OAuth consent screen

7) Select the userType and details like Appname, User support email and developer contact information and click on save as shown below

8) Create a OAuth client ID By clicking on APIs & Services -> Credentials  on menu

9) Click on create credentials -> OAuth client ID.

10) Create a new **web client** by Name in OAuth 2.0 Client IDs.

11) Collect the Client ID and Client secret and store it.

12) The Redirect url of Unify Apps ([Redirect URL for Unify apps](https://webhooks-global.ext-alb.qa.unifyapps.com/api/connector-auth-callback/oauthflowName=GeneralOAuthFlow)) , use this url and register this in  Authorization redirect URls

13) Using the Client ID and Client secret ,press the Authorize button. You’ll be redirected to a Google sign-in page.

14) If you're not already logged into Google, enter your Google account credentials and Sign in.

15) Google will display a permissions request screen, showing the app name and the specific Google services we are requesting access to (e.g., Google meet).

16) Carefully review the permissions being requested. If you’re comfortable with them, click the "Allow" or "Grant Access" button.

17) After granting access, you will be automatically redirected back to our platform, where you should see a confirmation message indicating that your Google account is now connected and authorized.

**Ensure that the following permissions are granted for OAuth authentication and provide public access to your data in Google meet.**

| **Scope Code** | **Description** |
|---|---|
| [https://www.googleapis.com/auth/meetings.space.created](https://www.googleapis.com/auth/meetings.space.created) | Allows the application to create new meeting spaces. |
| [https://www.googleapis.com/auth/meetings.space.readonly](https://www.googleapis.com/auth/meetings.space.readonly) | Allows read-only access to meeting space information. |
| [https://www.googleapis.com/auth/meetings.space.settings](https://www.googleapis.com/auth/meetings.space.settings) | Allows the application to manage meeting space settings. |
| [https://www.googleapis.com/auth/meetings.media.readonly](https://www.googleapis.com/auth/meetings.media.readonly) | Allows read-only access to general meeting media. |
| [https://www.googleapis.com/auth/meetings.media.audio.readonly](https://www.googleapis.com/auth/meetings.media.audio.readonly) | Allows read-only access to meeting audio media. |
| [https://www.googleapis.com/auth/meetings.media.video.readonly](https://www.googleapis.com/auth/meetings.media.video.readonly) | Allows read-only access to meeting video media. |
| [https://www.googleapis.com/auth/meetings.conference.media.readonly](https://www.googleapis.com/auth/meetings.conference.media.readonly) | Allows read-only access to conference media. |
| [https://www.googleapis.com/auth/meetings.conference.media.audio.readonly](https://www.googleapis.com/auth/meetings.conference.media.audio.readonly) | Allows read-only access to conference audio media. |
| [https://www.googleapis.com/auth/meetings.conference.media.video.readonly](https://www.googleapis.com/auth/meetings.conference.media.video.readonly) | Allows read-only access to conference video media. |
| [https://www.googleapis.com/auth/userinfo.email](https://www.googleapis.com/auth/userinfo.email) | Allows the application to view the user's primary email address. |
| [https://www.googleapis.com/auth/userinfo.profile](https://www.googleapis.com/auth/userinfo.profile) | Allows the application to view basic profile information (name, photo, etc.). |

## Actions

| **Action Name** | **Description** |
|---|---|
| Create pub/sub subscription | Creates a pub/sub subscription in Google Meet |
| Delete pub/sub subscription | Deletes pub/sub subscription in Google Meet |
| Export file | Export a file in Google Meet File |
| Get conference record | Gets conference record by ID from Google Meet |
| Get conference record participant | Gets conference record participant from Google Meet |
| Get conference record transcript | Gets conference record transcripts from Google Meet |
| Get file | Gets a file in Google Meet File |
| Get file details | Get file details in Google Meet |
| Get meeting space by ID | Gets meeting space by ID from Google Meet |
| List conference record participants | Lists conference record participants from Google Meet |
| List conference record transcript entries | Lists conference record transcript entries from Google Meet |
| List conference record transcripts | Lists conference record transcripts from Google meet |
| List conference records | Lists conference records from Google Meet |
| List file permissions | Lists the permissions for a file in Google Meet |
| List meetings | Lists meetings in Google Meet |
| List subscriptions | Lists pub/sub subscription in Google Meet |
| Schedule meeting | Schedules a meeting in Google Meet |
| Update meeting | Updates a meeting in Google Meet |
| Update pub/sub subscription | Updates a pub/sub subscription in Google Meet |
