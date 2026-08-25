# SMTP connector

Source: https://www.unifyapps.com/docs/unify-integrations/smtp
Section: integrations

---

SMTP (Simple Mail Transfer Protocol) is a protocol used for sending and relaying email messages between servers. It defines the rules for email transmission, ensuring reliable delivery across networks.

Integrating SMTP allows seamless and reliable email delivery, automating communication processes while ensuring efficient message routing and reducing the risk of email delivery failures.

## Authentication

Before integrating SMTP, ensure you have the following information:

- `Connection Name`**:** Choose a descriptive name for your SMTP connection to help you identify it within your application or integration settings. A meaningful name, like "MyAppSMTPIntegration," helps maintain organization, especially when managing multiple integrations.
- `SMTP Host`: Enter the hostname or IP address of the SMTP server you wish to connect to. Examples include smtp.gmail.com for Gmail or your custom server’s address.
- `TLS`: Select this option if your SMTP server requires a TLS (Transport Layer Security) connection for encrypted communication. This is common for secure email services. If SSL is not enabled, you can secure the connection using STARTTLS, which upgrades an insecure connection to a secure one using TLS (Transport Layer Security).
- `Port`: Provide the port number used to connect to the SMTP server. Common port numbers include **587** for TLS, **465** for SSL, and **25** for non-secure connections. Verify this with your email provider's SMTP settings.
- `Authentication Type`**:** Currently, the only supported authentication method is BASIC, which uses a username and password for authentication.

### BASIC Authentication

The BASIC authentication method requires a username and password to authenticate with the server.

- `Username`**:** The username for your SMTP server.
- `Password`**:** The password for your SMTP server.

## Actions

| **Action** | **Description** |
|---|---|
| `Send email` | Sends a email from a specific SMTP server |
