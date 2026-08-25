# LDAP connector

Source: https://www.unifyapps.com/docs/unify-integrations/ldap
Section: integrations

---

LDAP (Lightweight Directory Access Protocol) is a protocol used for accessing and managing directory services, typically for storing user credentials and other network resources. It provides a standardized method for querying and modifying directory data across networks.

Integrating LDAP streamlines user authentication, centralizes access control, and enhances security by providing a unified directory service for managing user credentials and permissions.

## Authentication

Before integrating LDAP, ensure you have the following information:

- `Connection Name`**:** Choose a descriptive name for your LDAP connection to help you identify it within your application or integration settings. A meaningful name, like "MyAppLDAPIntegration," helps maintain organization, especially when managing multiple integrations.
- `LDAP Host`**:** Enter the hostname or IP address of the LDAP server (e.g., ldap.example.com). This is the network address required to connect to the directory service.
- `LDAP Port`**:** Provide the port number of the LDAP server. Commonly used port numbers are 389 for non-secure connections and 636 for SSL-secured connections.
- `SSL Enabled`**:** Select this option if the LDAP server requires SSL (Secure Sockets Layer) for secure communication. This ensures encrypted data transfer between your system and the LDAP server.
- `Base DN`**:** Specify the base Distinguished Name (DN) for all LDAP requests (e.g., dc=example,dc=com). This sets the starting point for directory searches and ensures requests are directed to the correct branch of the directory tree.
- `Admin DN`**:** Enter the Distinguished Name of the admin user used to authenticate with the LDAP server (e.g., cn=admin,dc=example,dc=com). This account should have sufficient permissions for the required operations.
- `Admin Password`**:** Provide the password for the admin user to securely authenticate with the LDAP server. Ensure this password is kept confidential and aligns with the admin DN credentials.

## Actions

| **Action** | **Description** |
|---|---|
| `LDAP Request` | Make LDAP request to Active Directory server |
