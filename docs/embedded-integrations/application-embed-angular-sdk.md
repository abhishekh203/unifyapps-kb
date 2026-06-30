# Angular SDK

Source: https://www.unifyapps.com/docs/embedded-integrations/application-embed-angular-sdk
Section: embedded-integrations

---

## Overview

Angular library for integrating UnifyApps SDK into Angular applications.

## Step-by-Step Instructions

### Step 1: Installation

Install the package using npm or your preferred package manager:

```
npm install @unifyapps/sdk-angular
```

### Step 2: Obtain Credentials

- To get the required credentials, Contact [support@unifyapps.com](mailto:support@unifyapps.com)
- Required values:
- Replace these values in your component configuration.

### Step 3: Setting Up

**Basic Setup**

Import the `UnifyAppsComponent` in your Angular module or standalone component:

```
import { Component } from '@angular/core';
import { UnifyAppsComponent, UnifyAppsSettings } from '@unifyapps/sdk-angular';
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [UnifyAppsComponent],
  template: `
    <unifyapps [unifyAppsSettings]="settings"></unifyapps>
  `,
})
export class AppComponent {
  settings: UnifyAppsSettings = {
    host: '<HOST_NAME>',
    token: '<SESSION_ID>',
    identityProviderId: '<IDP_ID>',
    applicationId: '<APPLICATION_ID>',
    pageId: '<PAGE_ID>',
    pageInputs: '<PAGE_INPUTS>',
    theme: '<THEME>',
  };
}
```

**Using with Template Reference**

You can access component methods using a template reference variable:

```
import { Component, ViewChild } from '@angular/core';
import { UnifyAppsComponent, UnifyAppsSettings } from '@unifyapps/sdk-angular';
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [UnifyAppsComponent],
  template: `
    <unifyapps 
      #unifyapps 
      [unifyAppsSettings]="settings">
    </unifyapps>
  `,
})
export class AppComponent {
  @ViewChild('unifyapps') unifyappsComponent!: UnifyAppsComponent;
  settings: UnifyAppsSettings = {
    host: '<HOST_NAME>',
    token: '<SESSION_ID>',
    identityProviderId: '<IDP_ID>',
    applicationId: '<APPLICATION_ID>',
  };
}
```

## Step 4: Configure Required Parameters

`unifyAppsSettings (required)`

Configuration object for UnifyApps SDK:

- `host`(required) - The base URL of the host application
- `token`(optional) - The temporary session id to authenticate the user
- `identityProviderId`(required) - Identity provider, required for authentication
- `applicationId`(required) - Application ID: The unique identifier of the application . Retrieve this from the application's overview page in the UnifyApps platform
- `isApplicationPublic` (optional) - Whether the application is public
- `pageId`(optional) - Page ID: If a specific page needs to be opened . Retrieve this from inside application's page settings (Page Slug)
- `pageInputs`(optional) - Page inputs required to render the application's page
- `theme` (optional) - Theme to be set for the application. Available themes: `light`, `dark`, `system`. Default is `light`
- `onPageEvent`(optional) - Callback function for page events
- `appConfig` (optional) - Application configuration
- `locale` (optional) - Locale to override the locale selection logic
- `client` (optional) - Client type: ( '`unifyapps`' | '`external`' )
- `deployedVersion` (optional) - Deployed version
- `renderInShadowDom` (optional) - Use ShadowDom to wrap the SDK container element
- `networkHeaders` (optional) - An object containing any custom headers to be sent with each request to the host application

`containerEl (optional)`

The element where the application will be rendered. Can be:

- A string selector (e.g., '`#my-container`' or '`.container`')
- An HTMLElement reference

If not provided, it defaults to the component’s host element.

# Component Methods

`update(updatedSettings: Partial<UnifyAppsSettings>)`

- Update any of the UnifyApps global settings.
- `this.unifyappsComponent.update({ theme: 'dark', pageId: 'new-page-id', });`

`goToPage(options)`

- Navigate to a specific page.
- `this.unifyappsComponent.goToPage({ pageId: 'target-page-id', pageInputs: { key: 'value' }, mergeWithExistingPageInputs: true, // optional });`

`setTheme(theme: 'light' | 'dark' | 'system')`

- Set the theme of the application.
- `this.unifyappsComponent.setTheme('dark');`
