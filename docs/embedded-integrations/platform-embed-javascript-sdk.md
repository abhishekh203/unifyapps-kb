# Platform JavaScript SDK

Source: https://www.unifyapps.com/docs/embedded-integrations/platform-embed-javascript-sdk
Section: embedded-integrations

---

## Overview

A JavaScript SDK for Platform Embed would allow integration into any web application. While no specific documentation for this exists, a logical implementation would extend the global UnifyApps function to mount specific platform components.

The UnifyApps JavaScript SDK allows seamless embedding of platform modules like **AutomationManager, ConnectionManager and Connectors** into web applications. This guide provides an overview of how to integrate it using JavaScript.

## Step-by-Step Instructions

### Step 1: Get Required Parameters

1. **HOST_NAME** The host name is the URL where the platform application is hosted. Example: If the platform is hosted at `https://platform.unifyapps.com`, then the host is: `https://platform.unifyapps.com`
2. **Obtain Credentials**To obtain the required credentials, contact **support@unifyapps.com** for:
  - `HOST_NAME`
  - `AUTH_TOKEN`
  - `IDP_ID`

### Step 2: Generate `ACCESS_TOKEN` (Session ID)

Make an authentication request using Node.js:

```
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
    console.log('✅ Success:', responseData);
    return responseData;
  } catch (error) {
    console.error('❌ Error during authentication request:', error.message);
  }
}
// Fetch session ID using an IIFE to allow top-level await
(async () => {
  const result = await makeRequest();
  if (result?.sessionId) {
    const { sessionId } = result;
    console.log('Session ID:', sessionId);
  } else {
    console.error('Failed to retrieve session ID.');
  }
})();
```

### Step 3: Integrate the UnifyApps JavaScript SDK

```
<script>
  // Platform configuration
  window.uaPlatformSettings = {
    host: '<HOST_NAME>',          // e.g., 'https://platform.unifyapps.com'
    token: '<SESSION_ID>',        // e.g., '123456789/abcdef'
    module: 'AutomationManager',  // Options: AutomationManager | ConnectionManager | Connectors
    // containerEl: document.getElementById('containerId') // Optional: Specify a container element
  };
  (function () {
    const w = window;
    const ua = w.uaPlatform;
    if (typeof ua === 'function') {
      // If the SDK is already loaded, update the settings
      ua('update', w.uaPlatformSettings);
    } else {
      // SDK not yet loaded: queue the settings
      const d = document;
      const u = function () {
        u.c(arguments);
      };
      u.q = [];
      u.c = function (args) {
        u.q.push(args);
      };
      w.uaPlatform = u;
      w.uaPlatform('init');
      // Load the SDK script
      const loadSdk = function () {
        const s = d.createElement('script');
        s.type = 'text/javascript';
        s.async = true;
        s.src = 'https://cdn.unifyapps.com/lib/delta-platform/sdk-loader.js';
        const firstScript = d.getElementsByTagName('script')[0];
        firstScript.parentNode.insertBefore(s, firstScript);
      };
      // Attach script loader based on browser readiness
      if (document.readyState === 'complete') {
        loadSdk();
      } else if (w.attachEvent) {
        w.attachEvent('onload', loadSdk);
      } else {
        w.addEventListener('load', loadSdk, false);
      }
    }
  })();
</script>
```
