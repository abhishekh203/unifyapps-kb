# Zoho Catalyst integration | connect with UnifyApps

Source: https://www.unifyapps.com/docs/unify-integrations/zoho-catalyst
Section: integrations

---

Zoho Catalyst is a serverless full-stack development platform that enables developers to build, deploy, and scale applications with minimal infrastructure management. It offers backend services, AI, and automation tools to streamline app development.

Integrating your application with Zoho Catalyst enhances functionality by leveraging its powerful APIs for file storage, email services, and AI-driven capabilities. This integration allows you to efficiently manage files, send emails, and utilize Zoho's Zia services for OCR and object recognition.

## Authentication

Before you begin, make sure you have the following information:

- `Connection Name`: Choose a meaningful name for your connection. This name helps you identify the connection within your application or integration settings. It could be something descriptive like "MyAppZohoCatalystIntegration".
- `Authentication Type`: Zoho Catalyst supports OAuth for authentication.

### OAuth Based Authentication

1. Register your application with Zoho's Developer Console to get your `Client ID` and `Client Secret`.
2. Visit Zoho Developer Console and click on `Add Client ID`.
3. Select `Server-based applications`.
4. Fill in the required details to complete the registration.
5. Upon successful registration, you'll receive your OAuth 2.0 credentials: Client ID and Client Secret.
6. Keep these credentials secure and do not share them as they provide access to your zoho catalyst account.

## Actions

| Actions | Description |
|---|---|
| `Delete file` | Deletes a file in Zoho Catalyst |
| `Download file` | Downloads a file from Zoho Catalyst |
| `Get file` | Retrieves a file from Zoho Catalyst |
| `Send mail` | Sends mail to users in Zoho Catalyst |
| `Upload file` | Uploads a file in Zoho Catalyst |
| `Zia services OCR` | Performs OCR on documents in Zoho Catalyst |
| `Zia services object recognition` | Performs object recognition in Zoho Catalyst |
