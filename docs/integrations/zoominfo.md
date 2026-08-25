# ZoomInfo

Source: https://www.unifyapps.com/docs/unify-integrations/zoominfo
Section: integrations

---

ZoomInfo is a go-to-market intelligence platform that provides B2B contact and company data for sales, marketing, and recruiting teams. This integration allows you to enrich records, search for contacts and companies, and pull firmographic and intent data into your workflows with up-to-date information.

For a smooth integration process, ensure you have the following information ready:

## Authentication :

Before you begin, make sure you have the following information:

1. `Connection Name`**:** Choose a meaningful name for your connection. This name helps you identify the connection within your application or integration settings. It could be something descriptive like "MyAppZoomInfoIntegration".
2. `Authentication Type`**:** ZoomInfo supports two authentication methods Auth Token and Private Key (JWT).

### Auth Token based Authentication:

1. Log in to your ZoomInfo account at[https://www.zoominfo.com](https://www.zoominfo.com).
2. Use the same `username` (email) and `password` you use to sign in to ZoomInfo.
3. Ensure your account has `API`access enabled .
4. Enter these credentials directly into the connection — the connector exchanges them for a short-lived token automatically.

### Private Key based Authentication:

1. Log in to the `ZoomInfo Admin Portal`.
2. Navigate to the `API` / integrations section.
3. Generate or locate your `Client ID`.
4. Generate a `Private Key` and copy it (store it securely — it is shown only once).
5. Note the `username` associated with the API-enabled account.
6. Enter the username, Client ID, and private key into the connection — the connector signs a JWT and obtains a token automatically.

## Actions :

| **Action Name** | **Description** |
|---|---|
| `Enrich companies` | Enriches company information with data in ZoomInfo |
| `Enrich company location` | Enriches company location using company ID in ZoomInfo |
| `Enrich compliance data` | Enriches compliance data in ZoomInfo |
| `Enrich contacts` | Enriches contact information with data in ZoomInfo |
| `Enrich hashtags` | Enriches hashtags for a company in ZoomInfo |
| `Enrich intent` | Enriches intent for a company in ZoomInfo |
| `Enrich news` | Enriches news for a company in ZoomInfo |
| `Enrich organizational chart` | Enriches organizational chart for given company and department in ZoomInfo |
| `Enrich scoops` | Enriches scoops for a company in ZoomInfo |
| `Enrich technology stack information` | Enriches information about the technology stack of a company in ZoomInfo |
| `Search companies` | Searches companies in ZoomInfo |
| `Search contacts` | Searches contacts in ZoomInfo |
| `Search intent` | Searches intent in ZoomInfo |
| `Search news` | Searches news in ZoomInfo |
| `Search scoops` | Searches scoops in ZoomInfo |
