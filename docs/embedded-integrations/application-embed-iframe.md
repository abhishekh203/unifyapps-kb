# App iFrame embed

Source: https://www.unifyapps.com/docs/embedded-integrations/application-embed-iframe
Section: embedded-integrations

---

### **1.Standard Iframe Integration (via** **postMessage****)**

- If you are using a standard Iframe instead of the SDK, you will need to implement a custom route-sync solution using the postMessage API.
- **Event Emission:** The Unify app emits an event to the parent window ( window.parent.postMessage() ) whenever internal navigation happens.
- **URL Updating:** The host application (parent) listens for this message and updates the parent URL to reflect the Unify app's state.
- **Source Update:** To complete the sync, the host app must update the src URL of the Iframe so that browser history is maintained.

### **2. Passing Page Inputs to the Iframe**

- If you need to pass specific page inputs or context to the embedded Unify app within an Iframe, you can do so by appending them as query parameters to the Iframe's source URL.
- For example, to pass a specific Query ID, append &queryId=1342 to your URL: <iframe src="https://app.unifyapps.com/embed/sample?queryId=1342"></iframe>
