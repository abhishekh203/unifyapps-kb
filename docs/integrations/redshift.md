# Redshift connector

Source: https://www.unifyapps.com/docs/unify-integrations/redshift
Section: integrations

---

# Redshift

Using Amazon Redshift enables fast and scalable data warehousing for large-scale analytics. It allows you to run complex SQL queries across structured datasets using columnar storage and massively parallel processing (MPP) for high performance. Redshift ensures secure and reliable data management with encryption at rest and in transit, fine-grained access controls, automated backups, and integration with AWS security services.

### Authentication

Integrating your application to Amazon Redshift provides a high-performance environment for large-scale data analysis and reporting. Before you begin, make sure you have the following information:

`Connection Name` **:** Choose a meaningful name for your connection. This name helps you identify the connection within your application or integration settings. It could be something descriptive like "MyAppAmazonRedshiftIntegration".

`Host address` :  The IP address or DNS name of the database server.

`Port number` : The port on which the Amazon Redshift database is listening. The default is 5439.

`User` : Enter the username who can read objects in your database.

`Password` : Enter the password for the database user.

`Database name` : Specify the database you want to load data from.

`Schema name` : Specify the schema you want to use.

**Connection** **:** Choose the method of connection to your Amazon Redshift Server server.

- `Direct` : Connecting directly to the Amazon Redshift Server server without any intermediary. It's the simplest and most common method of connecting.
- `SSH` : Connecting to the Amazon Redshift Server through a secure SSH tunnel via an intermediary host. It's an effective method for adding network-level security when direct access is restricted.
1. `SSH Host` : Enter the hostname or IP address of the SSH server that acts as the gateway to your database.
2. `SSH Port` : Specify the port number on which the SSH server is listening.
3. `SSH User` : Provide the username for authenticating with the SSH server. This is typically the user account on the remote server with necessary permissions.
4. `RSA Private Key` : Provide the RSA private key corresponding to the public key stored on the SSH server.

**SSL Secure** :  This option enables SSL encryption for the Amazon Redshift Server connection, adding an extra layer of security to your data transfer.

1. `Client Certificate` : Obtain a valid client certificate issued by a trusted Certificate Authority (CA).This certificate authenticates your client to the database server.
2. `SSL Certificate Key` : This is the private key corresponding to your client certificate.
3. `Server Certificate` : Obtain the database server's SSL certificate. This certificate verifies the server's identity to your client. Often provided by your database administrator or hosting service.

### ACTIONS :

| **Action Name** | **Description** |
|---|---|
| `Create snapshot of table` | Creates a snapshot of a table from Redshift and stores it in S3 |
| `Delete rows` | Delete rows in a table in Redshift |
| `Execute sql statements` | Executes sql statements in Redshift |
| `Export query result` | Exports query result as a CSV file in Redshift |
| `Get table schema` | Get schema of a table in Redshift |
| `Insert row` | Inserts a row in a table in Redshift |
| `Insert rows` | Inserts a batch of rows in a table in Redshift |
| `List all databases` | Lists all databases in Redshift |
| `List all schemas` | Lists all schemas present in a database in Redshift |
| `List all tables` | Lists all tables present in a schema in Redshift |
| `Run long query using custom SQL` | Runs long query using custom SQL in Redshift |
| `Select rows` | Selects rows in a table in Redshift |
| `Select rows using custom SQL` | Selects rows using custom SQL in Redshift |
| `Update rows` | Updates rows in a table in Redshift |
| `Update rows` | Updates a batch of rows in a table in Redshift |
| `Upsert row` | Upserts a row in a table in Redshift |
| `Upsert rows` | Upserts a batch of rows in a table in Redshift |
| `Upsert rows via file` | Upserts a batch of rows in a table in Redshift by uploading a file and merging on unique keys (if provided). If no unique keys are provided, rows are inserted. |

### TRIGGERS :

| **Trigger Name** | **Description** |
|---|---|
| New row | New row in table in Redshift |
| New/Update row | New/updated row in table in Redshift |
| Triggers For all Rows of a Table | Triggers for all rows of a table in after Particular Time |
