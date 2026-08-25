# POP3 connector

Source: https://www.unifyapps.com/docs/unify-integrations/pop3
Section: integrations

---

Post Office Protocol version 3 (POP3) is an email protocol clients use to retrieve messages from a mail server. It downloads emails to the local device and typically deletes them from the server, promoting offline access.

Integrating Post Office Protocol (POP) enables efficient email retrieval, offline access, and centralized email management for users.

## Authentication

Before you begin, make sure you have the following information:

- `Connection Name`**:** Choose a descriptive name for your POP connection to help you identify it within your application or integration settings. A meaningful name, like "MyAppPOPIntegration," helps maintain organization, especially when managing multiple integrations.
- `Host`**:** The host domain name of your POP server. For example, if you are using Gmail's POP server, the host is pop.gmail.com
- `Port`**:** The port at which the POP server is listening. By default, POP servers run on 110 unencrypted or 995 with SSL/TLS.
- `Allow Multiple Clients`**:** By default, POP3 supports only a single client since it deletes any mail fetched for the first time from the server. However, support for multiple clients can be enabled explicitly if required. Enable this flag to ensure multiple clients can access the same mail.
- `SSL`**:** Enable this option to use SSL (Secure Sockets Layer) for a secure connection. SSL establishes a secure, encrypted link between your client and the server. This is commonly used for email protocols and ensures your data is protected during transmission.
- `Start-TLS`**:** Enable this option to use STARTTLS to secure your connection. STARTTLS upgrades an existing insecure connection to a secure one using TLS (Transport Layer Security). This is often used for email protocols like SMTP, IMAP, and POP3.
- `Trusted Mail Servers`**:** List trusted servers in case SSL or Start-TLS is enabled. Takes a comma-separated list as input.
- `Authentication Type`**:** Select the type of authentication for connecting to your POP Server. Currently, only BASIC is supported.

### BASIC Auth

The basic authentication method uses a username and password to authenticate to the server.

- `Username`**:** The username is the email address associated with your POP server.
- `Password`**:** Password is the password associated with your email address. Some email domains like Gmail do not allow using your email password but require you to use an application password for authentication. Email with MFA or 2FA also requires this.

## Actions

| Actions | Description |
|---|---|
| `Get Email By ID` | Fetch a particular email by its ID via POP3 |
| `List Emails` | List emails from the INBOX folder using POP3 |
