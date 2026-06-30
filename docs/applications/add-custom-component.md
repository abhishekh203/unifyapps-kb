# Add Custom Component

Source: https://www.unifyapps.com/docs/unify-applications/add-custom-component
Section: applications

---

Unify lets you extend your app experience with **Custom Components**. This guide walks you through building a Component using the **Custom Component CLI**.

## Step-by-Step: Build Your First Component

### Step 1: Initialize a New Component

Start by scaffolding a new Component using the CLI. This creates a ready-to-edit project with a sample React component.

```
pnpx @unifyapps/custom-component-cli init <ComponentName>
```

This creates a folder `<ComponentName>/` with:

- `package.json` – project metadata
- `manifest.json` – config for Unify
- `src/index.jsx` – the main React component
- `src/style.css` – component styles

Navigate into the component directory:

```
cd <ComponentName>
```

**Example manifest format generated after initialization:**

```
{
  "name": "SuperButton",
  "type": "SuperButton",
  "entry": "./src/index.jsx",
  "keywords": "SuperButton",
  "style": "./src/style.css",
  "icon": "https://assets.unifyapps.com/user-uploads/theme/unify.svg"
}
```

- **keywords** – used for block search in the block picker
- **icon** – URL of the icon to display in the block picker (optional)

You can add icon and modify the keywords before using the manifest in Unify.

### Step 2: Run in Development Mode

To preview your Component as you build, run in development mode.

**Note:** The development server will only be accessible on your local machine.

```
pnpm run dev
```

Or

```
pnpx @unifyapps/custom-component-cli dev
```

Once started, the CLI hosts the manifest at a local URL like:

```
http://localhost:5001/super-button.json
```

You’ll use this in the next step.

### Step 3: Add the Component in Unify

To make your component available inside Unify:

1. Go to Custom Components Manager
2. Click `Add Component`and fill in:
  - `Component Name` – e.g., SuperButton
  - `Deployment Mode` – Select development mode for testing
  - `Manifest URL` – The local URL from dev mode

On Clicking `Add`**,** Your Component will be added in the Application Builder `block picker`.

### Step 4: Instant Reload

While running in `dev` mode, any changes to your React component are instantly reflected. Just refresh the Application Builder to see updates.

### Step 5 : Build for Production

After finalizing and testing your component, generate a production-ready build to prepare it for deployment :

```
pnpm run build
```

Or

```
pnpx @unifyapps/custom-component-cli build
```

This creates a `<ComponentName>.zip` containing:

- Compiled assets
- A production out.json manifest

### Step 6: Adding Component to Production

Open the `Component Detail` panel and click the three-dot menu next to the manifest URL .

1. From the dropdown, select `Move to Production` to promote the version.
2. Upload the zip file

Your Component is now live and ready to use across your Unify interfaces.

### Step 7 : Removing a Component

To remove a Component from your app:

1. Remove the component from all apps where it is used (make sure it is not referenced or configured anywhere).
2. After all usages are removed, go to the Custom Components Manager and delete the component from the list.

**Note:** If you skip step 1 and delete the component from the list, any apps still referencing it may break or show errors.

**You’re All Set!**

With these steps, you can **build, test, and ship** custom Components in Unify with full flexibility. Components empower your team to reuse UI logic and deliver richer, more tailored app experiences.
