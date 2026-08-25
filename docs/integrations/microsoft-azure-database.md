# Microsoft Azure database

Source: https://www.unifyapps.com/docs/unify-integrations/microsoft-azure-database
Section: integrations

---

The Microsoft Azure Database connector integrates seamlessly with Azure SQL, enabling efficient management and interaction with your database. By integrating Azure databases with your application, you can leverage the power of cloud-hosted database services for real-time processing and efficient data management.

## Authentication

Before integrating your Azure database, ensure you have the following information:

- `Connection Name`**:** Assign a descriptive name to your Azure database connection for easy identification, such as "MyAzureDBConnection."
- `Server Name`**:** Your Azure SQL server's fully qualified domain name (e.g., <name>.database.windows.net).
- `Port Number`**:** The port number for Azure SQL databases. Default: 1433.
- `Username`**:** The username used to authenticate with the Azure SQL database.
- `Password`**:** The password associated with your Azure SQL database user account.
- `Database Name`**:** The Azure SQL database you want to connect to.
- `Connection Type`**:** Specify the connection type as *Direct*.
- `Schema Name`**:** This represents the schema or user namespace within the database containing tables, views, and other objects.
- `Connect through SSH`**:** Enable this option to connect to Unifyapps using an SSH tunnel instead of directly connecting to your Azure database host. This provides additional security to your database by not exposing your Azure database setup to the public.
- `SSH Host`**:** Enter the hostname or IP address of the SSH server that acts as the gateway to your database. Example: ssh.example.com or 203.0.113.1.
- `SSH Port`**:** Specify the port number on which the SSH server listens. The default is usually 22, but it may differ for security reasons.
- `SSH User`**:** Provide the username for authenticating with the SSH server. This is typically the user account on the remote server with the necessary permissions.
- `RSA Private Key`**:** Provide the RSA private key corresponding to the public key stored on the SSH server.
- `Client Certificate`**:** Obtain a valid client certificate from a trusted Certificate Authority (CA). This certificate authenticates your client to the database server.
- `SSL Certificate Key`**:** This private key corresponds to your client's certificate.
- `Server Certificate`**:** Obtain the database server's SSL certificate. This certificate verifies the server's identity to your client. Often provided by your database administrator or hosting service.

## Actions

| Actions | Description |
|---|---|
| `Insert row` | Insert a row into a table in Microsoft Azure Database |
| `Update rows` | Update rows in a table in Microsoft Azure Database |
| `Upsert rows` | Upsert rows in a table in Microsoft Azure Database |
| `Delete rows` | Delete rows in a table in Microsoft Azure Database |
| `Execute a SQL statement` | Executes a SQL statement in Microsoft Azure Database |
