# Ozonetel connector

Source: https://www.unifyapps.com/docs/unify-integrations/ozonetel
Section: integrations

---

Ozonetel helps organizations manage customer communication by providing cloud-based telephony and CPaaS capabilities. It enables teams to handle inbound and outbound calls, monitor call activity, and access detailed communication reports through scalable and secure APIs. With seamless integrations and automation support, Ozonetel helps improve customer engagement and operational efficiency.

### Authentication :

Integrating your application with Ozonetel enables secure access to telephony workflows, call management, and reporting data through Ozonetel CPaaS APIs. Before starting, ensure you have the following information:

- `Connection Name`: Choose a meaningful name for your connection. This name helps you identify the connection within your application or integration settings, such as "MyAppOzonetelIntegration".
- `Domain`: Enter the domain of your Ozonetel CPaaS environment.
- `API Token`: Enter the API token generated for your Ozonetel account. This token is used to authenticate all API requests.

### API Token Based Authentication

1. Log in to the Ozonetel Admin (CloudAgent) portal using your administrator credentials.
2. Navigate to your Profile or Account Settings section.
3. Locate the API or Integration settings.
4. In the API / Integration section, retrieve the API Token associated with your Ozonetel account.
5. Paste the copied API token into the API Token field while creating the connection in UnifyApps.

### ACTIONS :

| **Action Name** | **Description** |
|---|---|
| `Collect DTMF` | Collect DTMF |
| `Make a new Outbound Call` | Makes a new outbound call to the recipient in Ozonetel |
| `Send message with HSM template` | Sends a new message with HSM template in Ozonetel |
| `Send card template` | Sends a card message to a recipient in Ozonetel |
| `Send Flow` | Sends a flow message to a recipient in Ozonetel |
| `Send list picker` | Sends an interactive list message in Ozonetel |
| `Send` `simple text message` | Sends a simple text message in Ozonetel |

### TRIGGERS :

| **Trigger Name** | **Description** |
|---|---|
| `New message` | Triggers when a new message is created in Ozonetel |
| `On New Voice Event` | This trigger will be invoked when a new voice event comes from Ozonetel |
| `Redirect to Voicebot` | Redirect to Voicebot |
| `Respond with Instructions` | Respond with Instructions |
