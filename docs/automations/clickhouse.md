# ClickHouse

Source: https://www.unifyapps.com/docs/unify-automations/clickhouse
Section: automations

---

Using ClickHouse makes managing and analyzing large datasets faster and more efficient. It allows you to set up optimized queries, handle real-time data, and process millions of rows per second. ClickHouse ensures your data is stored and processed securely with robust encryption and security features.

Integrating your application to a ClickHouse database enables fast data storage, retrieval, and various analytical functionalities.

## Authentication

Before you begin, make sure you have the following information:

- `Connection Name` **:** Choose a meaningful name for your connection. This name helps you identify the connection within your application or integration settings. It could be something descriptive like "MyAppClickhouse".
- `Database Host` **:** The ClickHouse database host’s IP address or DNS. **Note:** For URL-based hostnames, exclude the jdbc:clickhouse:// part. For example, if the JDBC URL is , jdbc:clickhouse://host:8443?user=default&password=<password>&ssl=true , enter the host url as host.
- `Database Port` **:** The port on which your Clickhouse server listens for connections. Default value: 8443.
- `Database User` **:** The authenticated user who has the permissions to read tables in your database.
- `Database Password` **:** The password for the database user.
- `Database name` **:** Specify the database you want to load data from.
- `Connect through SSH` **:** Enable this option to connect to Unifyapps using an SSH tunnel, instead of directly connecting to your Clickhouse database host. This provides an additional level of security to your database by not exposing your Clickhouse setup to the public.
- `SSH Host` **:** Enter the hostname or IP address of the SSH server that acts as the gateway to your database.
- `SSH Port` **:** Specify the port number on which the SSH server is listening. Default is usually 22, but it may be different for security reasons.
- `SSH User` **:** Provide the username for authenticating with the SSH server. This is typically the user account on the remote server with necessary permissions.
- `RSA Private Key` **:** Provide the RSA private key corresponding to the public key stored on the SSH server.
- `Client Certificate` **:** Obtain a valid client certificate issued by a trusted Certificate Authority (CA).This certificate authenticates your client to the database server.
- `SSL Certificate Key` **:** This is the private key corresponding to your client certificate.
- `Server Certificate` **:** Obtain the database server's SSL certificate. This certificate verifies the server's identity to your client. Often provided by your database administrator or hosting service.

## Actions

| **Action** | **Description** |
|---|---|
| `List Databases` | List all databases in ClickHouse |
| `List Tables` | List ClickHouse tables |
| `Execute SQL` | Executes a SQL statement in ClickHouse |
| `Insert record` | Inserts a record in a table in ClickHouse |
