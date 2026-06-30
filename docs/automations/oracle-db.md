# Oracle DB

Source: https://www.unifyapps.com/docs/unify-automations/oracle-db
Section: automations

---

Using Oracle Database (OracleDB) with your work helps your organization manage and analyze data more effectively. With OracleDB, you can store large amounts of structured information, run complex queries to gain insights and ensure data consistency across your systems.

Integrating your application to an Oracle database enables integration for data storage, retrieval, and various database functionalities.

## Authentication

Before you begin, make sure you have the following information:

- `Connection Name`**:** Choose a meaningful name for your connection. This name helps you identify the connection within your application or integration settings. It could be something descriptive like "My App Oracle DB".
- `Database Host`: The Oracle database host’s IP address or DNS. **Note:** For URL-based hostnames, exclude the http:// or https:// part. For example, if the hostname URL is https://oracledb-qa.xxxx.ap-south-1.rds.amazonaws.com, enter oracledb-qa.xxxx.ap-south-1.rds.amazonaws.com.
- `Database Port`: The port on which your Oracle server listens for connections. Default value: 1521.
- `Database User`**:** The authenticated user who has the permissions to read tables in your database.
- `Database Password`**:** The password for the database user.
- `SID or Service Name`**:** The unique name identifying your specific database instance on the server. To retrieve the Service Name, open your Oracle server in any SQL client tool as a database user with SYSDBA privilege and enter the following command: `select name from v$database;`
- `PDB Name`**:** A unique identifier for a Pluggable Database within Oracle's multitenant architecture applies only if you're working with a Container Database (CDB) and need to connect to a specific Pluggable Database (PDB).
- `Schema Name`**:** This represents the schema or user namespace within the Oracle database that contains tables, views, and other database objects.
- `Connect through SSH`: Enable this option to connect to Unifyapps using an SSH tunnel, instead of directly connecting to your Oracle database host. This provides an additional level of security to your database by not exposing your Oracle setup to the public.
- `SSH Host`: Enter the hostname or IP address of the SSH server that acts as the gateway to your database. Example: ssh.example.com or 203.0.113.1
- `SSH Port`: Specify the port number on which the SSH server is listening. Default is usually 22, but it may be different for security reasons.
- `SSH User`: Provide the username for authenticating with the SSH server. This is typically the user account on the remote server with necessary permissions.
- `RSA Private Key`: Provide the RSA private key corresponding to the public key stored on the SSH server.
- `Client Certificate`: Obtain a valid client certificate issued by a trusted Certificate Authority (CA).This certificate authenticates your client to the database server.
- `SSL Certificate Key`:This is the private key corresponding to your client certificate.
- `Server Certificate`: Obtain the database server's SSL certificate. This certificate verifies the server's identity to your client. Often provided by your database administrator or hosting service.

### Actions

| Action | Description |
|---|---|
| `Execute a SQL statement` | Executes a SQL statement in Oracle DB |
| `Insert row` | Inserts a row in a table in Oracle DB |
| `List all schemas` | Lists schemas in Oracle DB |
| `List tables for a schema` | Lists tables for a schema in Oracle DB |
| `Create snapshot of table` | Create snapshot of table and stores it in S3 |
| `Insert rows(Batch)` | Insert batch of rows in a table in Oracle DB |
| `Select rows using custom SQL (Batch)` | Select rows using custom SQL in Oracle DB |
| `Export query result (File)` | Export query result in CSV file |
| `Select rows` | Select batch of rows in a table in Oracle DB |
| `Update rows (Batch)` | Update batch of rows in a table in Oracle DB |
| `Update rows` | Update rows in a table in Oracle DB |
| `Upsert row` | Upsert row in a table in Oracle DB |
| `Upsert rows (Batch)` | Upsert batch of rows in a table in Oracle DB |
| `Delete rows (Batch)` | Delete rows in a table in Oracle DB |
| `Execute stored procedure` | Execute stored procedure in Oracle DB |
| `Run long query using custom SQL` | Run long query using custom SQL in Oracle DB |

## Triggers

The following triggers are available to create custom automations on the Unifyapps platform:

| Trigger | Description |
|---|---|
| `New event` | Triggers when a new event occurs in Oracle DB |
| `New row` | Triggers when a row is inserted in Oracle DB |
| `New/Update row` | Triggers when a row is inserted or updated in Oracle DB |
| `Update row` | Triggers when a row is updated in Oracle DB |
| `Delete row` | Triggers when a row is deleted in Oracle DB |
