# iFrame

Source: https://www.unifyapps.com/docs/embedded-integrations/application-embed-iframe
Section: embedded-integrations

---

## Overview

The iFrame embedding method allows you to integrate your UnifyApps application into any external website by inserting an `<iframe>` tag.

## Step-by-Step Instructions

### Step 1: Get Required Parameters

- **HOST_NAME** The host name is the URL where the platform application is hosted. Example: If the platform is hosted at https://platform.unifyapps.com, then the host is:`https://platform.unifyapps.com`
- **Generate ACCESS_TOKEN (Session ID)**Make an authentication request using Node.js:

### Step 2: Obtain Credentials

To obtain the required credentials, contact [support@unifyapps.com](mailto:support@unifyapps.com) for:

- `HOST_NAME`
- `AUTH_TOKEN`
- `IDP_ID`

### Step 3: Copy the iFrame Snippet

Copy the following iFrame snippet and paste it into your HTML file:

```
<
iframe
 id="unifyapps-embed" src="URL" 
width="100%" height="1000" scrolling="no" frameborder="0" style="border:none;"></
iframe
>
```

### Step 4: Embed in Your Website

Paste the modified iFrame code into any webpage where you want to embed the UnifyApps application.

### Step 5: Verify the Integration

- Open the webpage and check if the embedded page loads correctly.
- Inspect the browser console for any errors if issues arise.

### **Standard Iframe Integration (via** **postMessage****)**

- If you are using a standard Iframe instead of the SDK, you will need to implement a custom route-sync solution using the postMessage API.
- **Event Emission:** The Unify app emits an event to the parent window ( window.parent.postMessage() ) whenever internal navigation happens.
- **URL Updating:** The host application (parent) listens for this message and updates the parent URL to reflect the Unify app's state.
- **Source Update:** To complete the sync, the host app must update the src URL of the Iframe so that browser history is maintained.

### **Passing Page Inputs to the Iframe**

- If you need to pass specific page inputs or context to the embedded Unify app within an Iframe, you can do so by appending them as query parameters to the Iframe's source URL.
- For example, to pass a specific Query ID, append &queryId=1342 to your URL: `<iframe src="https://app.unifyapps.com/embed/sample?queryId=1342"></iframe>`
