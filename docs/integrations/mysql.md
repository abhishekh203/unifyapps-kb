# MySQL connector

Source: https://www.unifyapps.com/docs/unify-integrations/mysql
Section: integrations

---

MySQL is an open-source relational database management system used for storing and managing structured data.

Integrating MySQL enables reliable data storage, efficient queries, and scalability for data-driven applications.

## Authentication

Before you begin, make sure you have the following information:

1. `Connection Name` - Choose a meaningful name for your connection. This name helps you identify the connection within your application or integration settings. It could be something descriptive like "MyAppMySQLIntegration".
2. `Host Address` - The MySQL database’s host’s IP address or DNS.
3. `Port Number` - The port on which your MySQL server listens for connections. Default value: 3306.
4. `User` - The authenticated user who has the permissions to read tables in your database.
5. `Password` - The password for the database user.
6. `Database Name` - Specify the database you want to load data from.
7. `Connect through SSH` - Enable this option to connect to Unifyapps using an SSH tunnel, instead of directly connecting to your Oracle database host. This provides an additional level of security to your database by not exposing your Oracle setup to the public.
8. `SSH Host` - Enter the hostname or IP address of the SSH server that acts as the gateway to your database. Example: ssh.example.com or 203.0.113.1
9. `SSH Port` - Specify the port number on which the SSH server is listening. Default is usually 22, but it may be different for security reasons.
10. `SSH User` - Provide the username for authenticating with the SSH server. This is typically the user account on the remote server with necessary permissions.
11. `RSA Private Key` - Provide the RSA private key corresponding to the public key stored on the SSH server.
12. `Client Certificate` - Obtain a valid client certificate issued by a trusted Certificate Authority (CA).This certificate authenticates your client to the database server.
13. `SSL Certificate Key` - This is the private key corresponding to your client certificate.
14. `Server Certificate` - Obtain the database server's SSL certificate. This certificate verifies the server's identity to your client. Often provided by your database administrator or hosting service.

## Actions

| Actions | Description |
|---|---|
| `Create snapshot of a table` | Creates snapshot of a table in MySQL |
| `Delete rows (Batch)` | Deletes rows in a table in MySQL |
| `Export table (File)` | Exports table as a CSV file in MySQL |
| `Get table schema` | Gets the schema of a table in MySQL |
| `Insert row` | Inserts a row in a table in MySQL |
| `Insert rows (Batch)` | Inserts batch of rows in a table in MySQL |
| `Execute SQL statement` | Executes a SQL query in MySQL |
| `Run long query using custom SQL` | Run long query using custom SQL in MySQL |
| `List all databases` | Lists all databases in MySQL |
| `List all tables` | Lists all tables in MySQL |
| `Select rows (Batch)` | Selects rows in a table in MySQL |
| `Update rows` | Updates rows in a table in MySQL |
| `Update batch of rows (Batch)` | Updates batch of rows in a table in MySQL |
| `Upsert row` | Upserts a row in a table in MySQL |
| `Upsert rows (Batch)` | Upserts batch of rows in a table in MySQL |

## Triggers

| Trigger | Description |
|---|---|
| `Delete Row` | Triggers when a row is deleted in a MySQL table |
| `New event` | Triggers when a new event occurs in a MySQL table |
| `New Row` | Triggers when a row is inserted in a MySQL table |
| `New/Update row` | Triggers when a row is inserted or updated in a MySQL table |
| `Update row` | Triggers when a row is updated in a MySQL table |
