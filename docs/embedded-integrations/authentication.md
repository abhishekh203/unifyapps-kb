# Authentication

Source: https://www.unifyapps.com/docs/embedded-integrations/authentication
Section: embedded-integrations

---

## Overview

This document provides a crucial overview of the security and authentication model required to embed either UnifyApps any platform component or any custom application built in UnifyApps into your own website or product.

## Universal Authentication and Configuration Parameters

| Parameter | Description | Scope | Data Type | How to Obtain |
|---|---|---|---|---|
| `HOST_NAME` | The base URL of your UnifyApps platform instance. | Universal | String | Provided in your platform's "Developer Settings" page. |
| `IDP_ID` | The unique identifier for your identity provider configuration. | Universal | String | Provided in your platform's "Developer Settings" page. |
| `AUTH_TOKEN` | A long-lived, secret API key used for server-to-server authentication. | Server-Side | String | Generate from your platform's "Developer Settings" page. |
| `SESSION_ID` | A short-lived, temporary token generated for a specific end-user session. This is the token passed to the frontend SDKs. | Client-Side | String | Generated via a server-side call to the /auth/createUserExternalLoginSession endpoint. |
| `applicationId` | The unique identifier for the specific UnifyApps application you wish to embed. | App Embed | String | Found on the "Overview" page of your application in the UnifyApps platform. |
| `pageId` | (Optional) The unique identifier (or "slug") of a specific page within your application to load by default. | App Embed | String | Found in the page settings of your application builder (e.g., "Page Slug"). |
| `pageInputs` | (Optional) A JSON object containing key-value pairs to pass as initial inputs to the embedded application's page. | App Embed | Object/String | Defined by the needs of your specific application page. |
| `containerEl` | (Optional) The DOM element in your host page where the UnifyApps application should be rendered. (JS SDK only). | App Embed | DOM Element | A reference to an element, e.g., document.getElementById('unify-container'). |

## The Two-Token Security Model

UnifyApps uses a two-token model to ensure all embedded content is secure. Understanding each token's role is critical.

- `AUTH_TOKEN` **(Server-Side Secret Key)**
  - This is your permanent, secret API key. It must only be used for secure server-to-server communication. **Note:** Never expose your `AUTH_TOKEN` in any client-side code like JavaScript or a mobile app. Treat it like a password.
- `SESSION_ID` **(Client-Side Temporary Token)**
  - This is a temporary, short-lived token generated for a single end-user.
  - It is safely passed to the user's browser to initialize the embedded application. In our SDKs, this is referred to as the token parameter.

## Authentication Flow

The authentication process follows a secure, server-side flow to generate the temporary `SESSION_ID`.

1. **User Authenticates:** A user logs into your application using your existing authentication system.
2. **Server Requests Session ID:** Your backend server makes a POST request to the UnifyApps `/auth/createUserExternalLoginSession` endpoint. This request must be authenticated using your secret `AUTH_TOKEN`.
3. **UnifyApps Returns Session ID:** UnifyApps validates the request and returns a temporary `SESSION_ID` to your server.
4. **Server Passes Session ID to Client:** Your server sends the temporary `SESSION_ID` to the user's browser.
5. **SDK Initializes:** The UnifyApps SDK (JavaScript/React) or iFrame uses this `SESSION_ID` to securely load the embedded content for the authenticated user.
