# React based Embed

Source: https://www.unifyapps.com/docs/embedded-integrations/platform-embed-react-sdk
Section: embedded-integrations

---

## Introduction

The UnifyApps Platform React Package is designed to integrate specialized platform components. This provides the most seamless and idiomatic experience for React developers.

The `@unifyapps/platform-react` package (proposed name) provides a suite of components for embedding core platform UIs. This guide can be used to embed components like **ConnectionManager** and **AutomationManager**

## Step-by-Step Instructions

### Step 1: Install the Package

```
npm install @unifyapps/platform-react
```

### Step 2: Get Required Parameters

1. **HOST_NAME** The host name is the URL where the platform application is hosted. Example: If the platform is hosted at `https://platform.unifyapps.com`, then the host is:`https://platform.unifyapps.com`
2. **Obtain Credentials**To obtain the required credentials, contact **support@unifyapps.com** for:
  - `HOST_NAME`
  - `AUTH_TOKEN`
  - `IDP_ID`
  - `NPM Access Details` - A token will be provided to enable you to download the NPM package.
    - Create a `.npmrc` file and add this code, and replace `<TOKEN>` with given token from unifyapps team `@unifyapps:registry=https://registry.npmjs.org/ //registry.npmjs.org/:_authToken=<TOKEN>`

### Step 3: Generate `ACCESS_TOKEN` (Session ID)

```
const fetch = require('node-fetch'); // Ensure node-fetch is available if using in Node.js
const URL = '<HOST_NAME>/auth/createUserExternalLoginSession';
const AUTH_TOKEN = '<AUTH_TOKEN>';
const data = {
  identityProviderId: '<IDP_ID>',
  formData: {
    username: '<USER_NAME>',
    name: '<NAME>',
    email: '<USER_EMAIL>',
  },
};
async function makeRequest() {
  try {
    const response = await fetch(URL, {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${AUTH_TOKEN}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    const responseData = await response.json();
    console.log('Success:', responseData);
    return responseData;
  } catch (error) {
    console.error('Error during authentication request:', error.message);
  }
}
// Fetch session ID
(async () => {
  const result = await makeRequest();
  if (result?.sessionId) {
    const { sessionId } = result;
    console.log('Session ID:', sessionId);
  }
})();
```

### Step 4: Import Required Modules

In your React project, import the necessary components from the package:

```
import React from 'react';
import ReactDOM from 'react-dom';
import { UAProvider, ConnectionManager } from '@unifyapps/platform-react';
```

### Step 5: Configure Provider Options

Define the `options` object with the required properties:

```
// Configuration options for API access
const options = {
  host: '<HOST_NAME>',     // Example: 'https://platform.unifyapps.com'
  token: '<SESSION_ID>',   // Example: '123456789/123456789'
};
```

Example:

```
const options = {
  host: 'https://platform.unifyapps.com',
  token: '123456789/123456789',
};
```

### Step 6: Define Styles and Render the Application

Define styles to ensure the embedded module fits within the container and render the ConnectionManager inside `UAProvider`. Finally, mount the App component in your entry file (`index.js` or `index.tsx`):

```
const FULL_SIZE = {
  width: '100%',
  height: '100%',
};

const App = () => (
  <UAProvider options={options}>
    <ConnectionManager style={FULL_SIZE} />
  </UAProvider>
);

ReactDOM.render(<App />, document.getElementById('root'));
```

### Props

- **UAProvider**
  - `host` (string, required) – Base URL of the host application.
  - `token` (string, required) – Authentication token in the format `<IDP_ID>/<SESSION_ID>`.
- **UI Components** Available components:
  - `ConnectionManager` – Manages platform connections.
  - `AutomationManager` – Handles automation workflows.
  - `Connectors` – Manages third-party integrations.
- **UI Component Props**
  - `id (optional)` – Loads a specific entity.
  - `style (optional)` – Defines inline styles for the container.
  - `className (optional)` – Adds a CSS class name for the container.
