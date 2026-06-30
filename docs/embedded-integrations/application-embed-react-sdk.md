# React SDK

Source: https://www.unifyapps.com/docs/embedded-integrations/application-embed-react-sdk
Section: embedded-integrations

---

## Overview

Application Embed is used to render specific, custom applications that you have built on the UnifyApps platform. This is ideal for displaying data-driven UIs, forms, or dashboards to your end-users within your product or a third-party platform.

This section provides instructions to embed your application using the UnifyApps SDK React package. This method is ideal for React applications and provides a more modular approach.

## Step-by-Step Instructions

### Step 1: Install the Package

Run the following command to install the UnifyApps React SDK:

```
npm install @unifyapps/sdk-react
```

### Step 2: Get Required Parameters

- **HOST_NAME**The host name is the URL where the platform application is hosted. Example: If the platform is hosted at https://platform.unifyapps.com, then the host is: `https://platform.unifyapps.com`
- **Generate ACCESS_TOKEN (Session ID)** Make an authentication request using Node.js: `const SESSION_ENDPOINT = '<HOST_NAME>/auth/createUserExternalLoginSession'; const AUTH_TOKEN = '<AUTH_TOKEN>'; const data = { identityProviderId: '<IDP_ID>', formData: { username: '<USER_NAME>', name: '<NAME>', email: '<USER_EMAIL>', }, }; // Example data: {identityProviderId: '123456789', formData: {username: 'user', name: 'Full name', email: 'user@domain.com'}} // Make a POST request to create a user session async function makeRequest(applicationId: string) { try { const response = await fetch(SESSION_ENDPOINT, { method: 'POST', headers: { Authorization: `Bearer ${AUTH_TOKEN}`, 'Content-Type': 'application/json', 'x-ua-app': applicationId, }, body: JSON.stringify(data), }); if (!response.ok) { throw new Error(`HTTP error! status: ${response.status}`); } const responseData = await response.json(); // Example responseData: {"sessionId":"<SESSION_ID>"} console.log('Success:', responseData); return responseData; } catch (error) { console.error('Error:', error); } } // Pass this sessionId to the UAProvider options in the token field const { sessionId: SESSION_ID } = await makeRequest(applicationId);`

### Step 3: Obtain Credentials

To obtain the required credentials, contact [support@unifyapps.com](mailto:support@unifyapps.com) for:

- `HOST_NAME`
- `AUTH_TOKEN`
- `IDP_ID`
- `NPM Access Details` - A token will be provided to enable you to download the NPM package.
  - Create a .npmrc file and add this code, and replace <TOKEN> with given token from unifyapps team

```
@unifyapps:registry=https://registry.npmjs.org/
//registry.npmjs.org/:_authToken=<TOKEN>
```

### Step 4: Import and Configure the SDK

Create a React component that renders the application using UAProvider and WebApplication.

```
import React from 'react';
import ReactDOM from 'react-dom';
import { UAProvider, WebApplication } from '@unifyapps/sdk-react';
const options = {
  host: '<HOST_NAME>',
  token: '<SESSION_ID>',
  identityProviderId: '<IDP_ID>',
  isApplicationPublic: '<BOOLEAN>',
  theme: '<THEME>'
};
// Example: {host: 'https://prod.unifyapps.com', token: '123456789', identityProviderId: '123456789'}
const webApplicationProps = {
  applicationId: '<APPLICATION_ID>',
  pageId: '<PAGE_ID>',
  pageInputs: '<PAGE_INPUTS>',
  onPageEvent: async ({eventType, eventPayload}) => { return Promise.resolve() },
};
// Example: {applicationId: 'my_app'}
const App = () => (
  <UAProvider options={options}>
    <WebApplication {...webApplicationProps} />
  </UAProvider>
);
ReactDOM.render(<App />, document.getElementById('root'));
```

### Step 5: Configure Required Parameters

Replace the placeholders with actual values:

- `UAProvider`
  - `options` : An object containing configuration options for the provider.
  - `host` : The base URL of the host application
  - `token`(optional): The temporary session id to authenticate the user
  - `identityProviderId`(optional): Identity provider, required for authentication
  - `isApplicationPublic`(optional): Boolean flag to indicate if the application is public or private. Default is false (private app)
  - `theme`(optional): Theme to be set for the application. Available themes are `light`, `dark`, system. Default is `light`.
- `WebApplication` **-** Renders application made via UnifyApps platform.
  - `applicationId` - Application ID: The unique identifier of the application. Retrieve this from the application's overview page in UnifyApps platform
  - `initialPageId` (optional) - Page ID: If a specific page needs to be opened. Retrieve this from inside application's page settings (Page Slug)
  - `initialPageInputs` (optional) - Page inputs required to render the application's page
  - `ref` (optional) - A React ref object that provides access to the following methods:
  - `goToPage`: A method to programmatically navigate to a different page in the application. It accepts an object with the following properties:
  - `pageId`: The ID of the page to navigate to
  - `pageInputs` (optional): Any page inputs required by the target page
