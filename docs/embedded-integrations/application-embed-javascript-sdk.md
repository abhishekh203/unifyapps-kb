# JavaScript SDK

Source: https://www.unifyapps.com/docs/embedded-integrations/application-embed-javascript-sdk
Section: embedded-integrations

---

## Overview

This guide provides step-by-step instructions to embed your application using a JavaScript snippet. Follow the steps below to integrate the UnifyApps SDK into your webpage.

## Step-by-Step Instructions

### Step 1 : Get Required Parameters

- **HOST_NAME** The host name is the URL where the platform application is hosted. Example: If the platform is hosted at https://platform.unifyapps.com, then the host is:`https://platform.unifyapps.com`
- **Generate ACCESS_TOKEN (Session ID)** Make an authentication request using Node.js:`const SESSION_ENDPOINT = '<HOST_NAME>/auth/createUserExternalLoginSession'; const AUTH_TOKEN = '<AUTH_TOKEN>'; const data = { identityProviderId: '<IDP_ID>', formData: { username: '<USER_NAME>', name: '<NAME>', email: '<USER_EMAIL>', }, }; // Example data: {identityProviderId: '123456789', formData: {username: 'user', name: 'Full name', email: 'user@domain.com'}} // Make a POST request to create a user session async function makeRequest(applicationId: string) { try { const response = await fetch(SESSION_ENDPOINT, { method: 'POST', headers: { Authorization: `Bearer ${AUTH_TOKEN}`, 'Content-Type': 'application/json', 'x-ua-app': applicationId, }, body: JSON.stringify(data), }); if (!response.ok) { throw new Error(`HTTP error! status: ${response.status}`); } const responseData = await response.json(); // Example responseData: {"sessionId":"<SESSION_ID>"} console.log('Success:', responseData); return responseData; } catch (error) { console.error('Error:', error); } } // Pass this sessionId to the UAProvider options in the token field const { sessionId: SESSION_ID } = await makeRequest(applicationId);`

### Step 2: Obtain Credentials

To obtain the required credentials, contact [support@unifyapps.com](mailto:support@unifyapps.com) for:

- `HOST_NAME`
- `AUTH_TOKEN`
- `IDP_ID`

### Step 3: Copy the JavaScript Snippet

Copy the following JavaScript snippet and paste it into your HTML file:

```
<script>
    window.unifyAppsSettings = {
        host: '<HOST_NAME>',
        token: '<SESSION_ID>',
        identityProviderId: '<IDP_ID>',
        applicationId: '<APPLICATION_ID>',
        pageId: '<PAGE_ID>',
        pageInputs: '<PAGE_INPUTS>',
        theme: '<THEME>',
        containerEl: '<CONTAINER_ELEMENT>',
        onPageEvent: async ({
            eventType,
            eventPayload
        }) => {
            return Promise.resolve()
        },
    };
(function() {
    var w = window,
        ua = w.UnifyApps;
    if (typeof ua === 'function') {
        ua('update', w.unifyAppsSettings);
    } else {
        var d = document,
            u = function() {
                u.c(arguments);
            };
        u.q = [];
        u.c = function(args) {
            u.q.push(args);
        };
        w.UnifyApps = u;
        w.UnifyApps('init');
        var l = function() {
            var s = d.createElement('script');
            s.type = 'text/javascript';
            s.async = true;
            s.src = `${window.unifyAppsSettings.host}/lib/delta-matrix/ua-web-sdk.js`;
            var x = d.getElementsByTagName('script')[0];
            x.parentNode.insertBefore(s, x);
        };
        if (document.readyState === 'complete') {
            l();
        } else if (w.attachEvent) {
            w.attachEvent('onload', l);
        } else {
            w.addEventListener('load', l, false);
        }
    }
})(); 
</script>
```

### Step 4: Configure the Required Parameters

Replace the placeholders in the script with the actual values.

- **Required Parameters:**
  - `host` – The base URL of the host application.
  - `token` – The temporary session id to authenticate the user.
  - `identityProviderId` – Identity provider, required for authentication.
  - `applicationId` – Application ID: The unique identifier of the application. Retrieve this from the application's overview page in UnifyApps platform.
- **Optional Parameters:**
  - `pageId` – The unique identifier for a specific page within the application, used to designate the overview page. This can be retrieved from the application's page. Example: pageId: 'Homepage'
  - `pageInputs` – An object containing the necessary inputs required to render the application's page. Multiple page inputs can be passed at once. Example: pageInputs: ‘{ inputA: 1, inputB: 2, inputC: "abc" }’
  - `containerEl` – The HTML element where the application should be rendered (defaults to <body> if not provided). Eg. - document.getElementById("container");
  - `theme` - Theme to be set for the application. Available themes are `light`, `dark`, system . Default is `light`
  - `renderInShadowDom` - Use ShadowDom to wrap the sdk containerEl.
  - `networkHeaders` - An object containing any custom headers to be sent with each request to the host application.
  - `onPageEvent`
  - Signature: `async ({eventType, eventPayload}) => { return Promise.resolve() }`
  - Parameters:
  - Return Value: The function should return a Promise
  - `eventType` (string): The name of page event which was emitted
  - `eventPayload` (object): Payload with which this event was triggered

### Step 5: Verify the Integration

- Open the HTML file in a browser.
- Ensure that the application loads correctly inside the specified container.
- If any issues arise, check the browser console for errors.

## Dynamic Control with SDK Methods

Once initialized, you can interact with the embedded application using the global UnifyApps function. 6

- `UnifyApps ('update', updatedUnifyAppsSettings)` - To update any of UnifyApps global settings
- `UnifyApps ('goToPage', {pageId, pageInputs})` - To change pageId or pageInputs use this method. In case of copilot chat, if the chat is closed when the method is called, it will be opened first and then the corresponding navigation updates will be made.
- `UnifyApps('setTheme', { theme: 'light' | 'dark' | 'system' })` - To set the theme of the application
- **Copilot Chat specific methods:**
  - `UnifyApps('show')` - Open the copilot chat
  - `UnifyApps('hide')` - Close the copilot chat, launcher will still be visible
  - `UnifyApps('showCopilotTrigger')` - Show the copilot launcher if not visible
  - `UnifyApps('hideCopilotTrigger')` - Hide the copilot launcher if visible
  - `UnifyApps('addCopilotResponse', { data: a2aResponse, el: htmlElToRenderUnder })`- Render a copilot A2A response, returns {copilotResponseId: string}
  - `UnifyApps('removeCopilotResponse', {copilotResponseId: string})` - Removes given copilot response
  - `UnifyApps('preloadCopilotResponse')` - Preloads copilot response, useful to reduce latency when user clicks on the copilot trigger

### **Javascript SDK Integration (Recommended)**

- The Javascript SDK is the simplest way to integrate and handle routing automatically.
- The Unify app emits a pageChange event on navigation, which the host app can store in its URL.
- **Step 1: Store Navigation State in the Parent URL.** Listen for the pageChange event via onPageEvent . When triggered, update the parent URL with the current page ID and inputs without reloading the page (using history.replaceState ).

```
onPageEvent: ({ eventType, eventPayload }) => {
  if (eventType === 'pageChange') {
    const url = new URL(window.location.href);
    
    // Store the page context as a stringified JSON object in the URL
    url.searchParams.set('uaPageContext', JSON.stringify({ 
      pageId: eventPayload.pageId, 
      pageInputs: eventPayload.pageInputs 
    }));
    
    // Update the browser URL without reloading
    history.replaceState({}, '', url);
  }
}
```

- **Step 2: Read State from URL and Pass to SDK.** When the parent app loads (or when the user navigates using browser history), extract the stored uaPageContext from the URL parameters and pass the pageId into the Unify SDK settings.

```
// Extract URL parameters
const params = new URLSearchParams(window.location.search);

const uaPageContext = params.get('uaPageContext') 
  ? JSON.parse(params.get('uaPageContext')) 
  : {};

// Initialize Unify SDK with the extracted pageId
const unifyAppsSettings = {
  pageId: uaPageContext.pageId,
  // ...rest of your settings
};
```

**SDK Installation on Restricted Networks**
 **SDK Architecture and Updates** **Embedded App Capabilities and Limitations**
