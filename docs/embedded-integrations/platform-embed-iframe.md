# Platform iFrame embed

Source: https://www.unifyapps.com/docs/embedded-integrations/platform-embed-iframe
Section: embedded-integrations

---

## Overview

The iFrame embedding method allows you to integrate your UnifyApps application into any external website by inserting an `<iframe>` tag.

## Step-by-Step Instructions

### Step 1: Get Required Parameters

1. **HOST_NAME** The host name is the URL where the platform application is hosted. Example: If the platform is hosted at `https://platform.unifyapps.com`, then the host is: `https://platform.unifyapps.com`
2. **Generate ACCESS_TOKEN (Session ID)** Make an authentication request using Node.js:`// API endpoint and authentication token const URL = '<HOST_NAME>/auth/createUserExternalLoginSession'; const AUTH_TOKEN = '<AUTH_TOKEN>'; // Payload to be sent in the request body const data = { identityProviderId: '<IDP_ID>', formData: { username: '<USER_NAME>', name: '<NAME>', email: '<USER_EMAIL>', }, }; // Function to make the authentication request async function makeRequest() { try { const response = await fetch(URL, { method: 'POST', headers: { Authorization: `Bearer ${AUTH_TOKEN}`, 'Content-Type': 'application/json', }, body: JSON.stringify(data), }); // Handle non-successful responses if (!response.ok) { throw new Error(`HTTP error! Status: ${response.status}`); } // Parse and return the response const responseData = await response.json(); console.log('✅ Success:', responseData); return responseData; } catch (error) { console.error('❌ Error:', error.message); } } // Use an IIFE to handle top-level await safely (async () => { const result = await makeRequest(); if (result?.sessionId) { const { sessionId } = result; console.log('Session ID:', sessionId); } else { console.error('Failed to retrieve session ID.'); } })();`

### Step 2: Obtain Credentials

To obtain the required credentials, contact **support@unifyapps.com** for:

- `HOST_NAME`
- `AUTH_TOKEN`
- `IDP_ID`

### Step 3: Copy the iFrame Snippet

Copy the following iFrame snippet and paste it into your HTML file:

```
<iframe
  id="unifyapps-embed"
  src="URL"
  width="100%"
  height="1000"
  scrolling="no"
  frameborder="0"
  style="border: none; display: block; width: 100%; height: 1000px;"
></iframe>
```

### Step 4: Embed in Your Website

Paste the modified iFrame code into any webpage where you want to embed the UnifyApps application.

### Step 5: Verify the Integration

1. Open the webpage and check if the embedded page loads correctly.
2. Inspect the browser console for any errors if issues arise.
