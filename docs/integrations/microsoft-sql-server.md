# Microsoft SQL Server

Source: https://www.unifyapps.com/docs/unify-integrations/microsoft-sql-server
Section: integrations

---

Microsoft SQL Server is a relational database management system that supports data **storage**, **retrieval**, and **management**.

Integrating it with your application enables seamless access to advanced database functionalities for efficient data handling and operations.

## Authentication

Before you begin, make sure you have the following information:

- `Connection Name`**:** Choose a meaningful name for your connection. This name helps you identify the connection within your application or integration settings. It could be something descriptive like "My App SQLServer".
- `Database Host`**:** The SQLServer database host's IP address or DNS.Note: For URL-based hostnames, exclude the http:// or https:// part. For example, if the hostname URL is https:/sqlserver-qa.xxxx.ap-south-1.rds.amazonaws.com, enter *sqlserver-qa.xxxx.ap-south-1.rds.amazonaws.com.*
- `Database Port`**:** The port on which your SQLServer server listens for connections. Default value: 1433.
- `Database User`**:** The authenticated user with permission to read tables in your database.
- `Database Password`**:** The password for the database user.
- `Schema Name`**:** This represents the schema or user namespace within the PostgreSQL database containing tables, views, and other objects.
- `Connect through SSH`**:** Enable this option to connect to Unifyapps using an SSH tunnel instead of directly connecting to your SQLServer database host. This provides additional security to your database by not exposing your SQLServer setup to the public.
- `SSH Host`**:** Enter the hostname or IP address of the SSH server that acts as the gateway to your database. Example: ssh.example.com or 203.0.113.1
- `SSH Port`**:** Specify the port number on which the SSH server listens. The default is usually 22, but it may differ for security reasons.
- **SSH User:** Provide the username for authenticating with the SSH server. This is typically the user account on the remote server with the necessary permissions.
- `RSA Private Key`**:** Provide the RSA private key corresponding to the public key stored on the SSH server.
- `Client Certificate`**:** Obtain a valid client certificate from a trusted Certificate Authority (CA). This certificate authenticates your client to the database server.
- `SSL Certificate Key`**:** This private key corresponds to your client's certificate.
- `Server Certificate`**:** Obtain the database server's SSL certificate. This certificate verifies the server's identity to your client. Often provided by your database administrator or hosting service.

## Actions

The following actions are available to create custom automations on the Unifyapps platform:

| **Action** | **Description** |
|---|---|
| `Create Snapshot of Table` | Creates a snapshot of a table and stores it in S3. |
| `Execute SQL statement` | Executes a SQL statement in Microsoft SQL server |
| `Insert row` | Inserts row into a table in Microsoft SQL server |
| `List all databases` | Lists all databases in Microsoft SQL server |
| `List tables for a schema` | Lists tables for a schema in Microsoft SQL server |
| `Replicate schema` | Create/alter table schema in SQL Server |
| `Replicate rows (Batch)` | Replicate batch of rows to table in SQL Server |
| `Insert rows(Batch)` | Insert batch of rows in a table in SQL Server |
| `Select rows using custom SQL (Batch)` | Select rows using custom SQL in SQL Server |
| `Export query result (File)` | Export query result as a CSV file |
| `Get table schema` | Get table schema for SQL Server |
| `Bulk load from an on-prem file` | Bulk load rows into a table in SQL server from an on-prem file |
| `Select rows` | Select rows in a table in SQL Server |
| `Update rows (Batch)` | Update batch of rows in a table in SQL Server |
| `Update rows` | Update rows in a table in SQL Server |
| `Upsert rows` | Upsert row in a table in SQL Server |
| `Upsert rows (Batch)` | Upsert batch of rows in a table in SQL Server |
| `Delete rows (Batch)` | Delete rows in a table in SQL Server |
| `Execute stored procedure` | Execute stored procedure in SQL Server |
| `Run long query using custom SQL` | Run long query using custom SQL in SQL Server |

## Triggers

The following actions are available to create custom automations on the Unifyapps platform:

| Trigger | Description |
|---|---|
| `New/updated row` | New/updated row in a table in SQL Server |
| `New row` | New row in a table in SQL Server |
| `New rows via custom SQL(Batch)` | New batch of rows via custom SQL in SQL Server |
| `New/updated rows via custom SQL(Batch)` | New/updated batch of rows via custom SQL in SQL Server |
| `Scheduled query (Batch)` | Scheduled query using custom SQL in SQL Server |
| `New/updated rows (Batch)` | New/updated batch of rows in a table in SQL Server |
| `New rows (Batch)` | New batch of rows in a table in SQL Server |
