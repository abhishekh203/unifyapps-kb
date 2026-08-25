# IMAP connector

Source: https://www.unifyapps.com/docs/unify-integrations/imap
Section: integrations

---

The IMAP connector seamlessly integrates with email servers, enabling efficient mailbox access. It provides robust capabilities for managing, retrieving, and organising emails securely.

Integrate your IMAP server with UnifyApps to seamlessly access your emails in workflows and process them via many other applications.

## Authentication

Ensure you have the following information ready for a better integration experience:

- `Connection Name`**:** Choose a meaningful name for your connection. This name helps you identify the connection within your application or integration settings.
- `Host`**:** The host domain name of your IMAP server. For example, if you are using gmails's IMAP server, the host is imap.gmail.com
- `Port`**:** The port at which the IMAP server is listening. By default, IMAP servers run on 143 unencrypted or 993 with SSL/TLS.
- `Allow Multiple Clients`**:** By default, IMAP supports only a single client since it deletes any mail fetched for the first time from the server. However, support for multiple clients can be enabled explicitly if required. Enable this flag to ensure multiple clients can access the same mail.
- `SSL`**:** Enable this option to use SSL (Secure Sockets Layer) for a secure connection. SSL establishes a secure, encrypted link between your client and the server. This is commonly used for email protocols and ensures your data is protected during transmission.
- `Start-TLS`**:** Enable this option to use STARTTLS to secure your connection. STARTTLS upgrades an existing insecure connection to a secure one using TLS (Transport Layer Security). This is often used for email protocols like SMTP, IMAP, and POP3.
- `Trusted Mail Servers`**:** List trusted servers in case SSL or Start-TLS is enabled. Takes a comma-separated list as input.
- `Authentication Type`**:** Select the type of authentication for connecting to your IMAP Server. Currently, only BASIC is supported.

### Basic Auth

The basic authentication method uses a username and password to authenticate to the server.

- `Username`**:** The username is the email address associated with your IMAP server.
- `Password`**:** Password is the password associated with your email address. Some email domains like Gmail do not allow using your email password but require you to use an application password for authentication. Email with MFA or 2FA also requires this.

## Actions

| Actions | Description |
|---|---|
| `Get email` | Get email using IMAP |
| `List emails from a specific folder` | List emails from a specific folder using IMAP |
| `Move email from one folder to another` | Move email from one folder to another using IMAP |
