# FTP/FTPS connector

Source: https://www.unifyapps.com/docs/unify-integrations/ftp-ftps
Section: integrations

---

Integrating your application with FTP/FTPS (File Transfer Protocol / File Transfer Protocol Secure) provides a standard method for transferring files between systems. While FTP offers basic file transfer capabilities, FTPS adds an encryption layer, enhancing security. Users can upload, download, and manage files on remote servers using command-line tools and graphical interfaces.

## Authentication

Before you begin, make sure you have the following information:

- `Connection Name`**:** Choose a descriptive name for your connection. This helps you easily identify the connection within your application or integration settings, such as "MyAppFTPIntegration".
- `Authentication Type`**:** Select the type of authentication for connecting to your FTP/FTPS server:
  - Basic (Username and Password)
  - SSL/TLS Certificates (for FTPS only)

### Basic Authentication

1. Set Up FTP/FTPS User:
  - Log into your server or hosting platform.
  - Navigate to the FTP/FTPS settings or user management area.
  - Create a new user account specifically for FTP/FTPS access.
  - Assign necessary permissions and specify the home directory.
  - Obtain the FTP/FTPS credentials (username and password).
2. Connecting with an FTP/FTPS Client:
  - Open an FTP client like FileZilla, Cyberduck, or WinSCP.
  - Create a new connection profile and enter the following details:
    - `Host`: The FTP/FTPS server address.
    - `Port`: Use 21 for FTP or FTPS (explicit) and 990 for FTPS (implicit).
    - `Username` and `Password`: Enter the credentials obtained in the previous step.
  - For FTPS: Ensure SSL/TLS is enabled in the connection settings to secure the transfer.
  - Connect to the server and start transferring files.

### **SSL/TLS Certificates (FTPS Only)**

For secure FTPS connections using SSL/TLS, follow these additional steps:

1. FTPS Type:
  - Select the type of FTPS connection:
    - `Explicit FTPS`: The connection starts as unencrypted FTP and upgrades to TLS/SSL upon an explicit request from the client.
    - `Implicit FTPS`: The connection is encrypted from the beginning.
2. Certificate Verification:
  - Verify Certificate: Choose whether to verify the server’s SSL/TLS certificate.
  - If required, enable trustAll to accept all certificates without verification (useful for testing environments or self-signed certificates).

## Actions

| Actions | Description |
|---|---|
| `Delete file` | Deletes a file from the FTP/FTPS server |
| `Delete folder` | Deletes a folder from the FTP/FTPS server |
| `Download file` | Downloads a file from the FTP/FTPS server |
| `Get file information` | Gets information about a file from the FTP/FTPS server |
| `List files and directories` | Lists files and directories from the FTP/FTPS server |
| `Rename a file` | Renames a file on the FTP/FTPS server |
| `Search folder` | Searches for files and folders in a folder on the FTP/FTPS server |
| `Upload file` | Uploads a file to the FTP/FTPS server |
