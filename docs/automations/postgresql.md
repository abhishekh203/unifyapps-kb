# PostgreSQL

Source: https://www.unifyapps.com/docs/unify-automations/postgresql
Section: automations

---

PostgreSQL is an open-source relational database management system that supports advanced data storage and retrieval.

Integrating it with your application enhances data management by providing powerful database functionalities and reliable performance.

## Authentication

Before you begin, make sure you have the following information:

- `Connection Name`**:** Choose a meaningful name for your connection. This name helps you identify the connection within your application or integration settings. It could be something descriptive like "My App PostgreSQL".
- `Database Host`**:** The PostgreSQL database host's IP address or DNS.Note: For URL-based hostnames, exclude the http:// or https:// part. For example, if the hostname URL is https://postgresql-qa.xxxx.ap-south-1.rds.amazonaws.com, enter postgresql-qa.xxxx.ap-south-1.rds.amazonaws.com.
- `Database Port`**:** The port on which your PostgreSQL server listens for connections. Default value: 5432.
- `Database User`**:** The authenticated user who has the permissions to read tables in your database.
- `Database Password`**:** The password for the database user.
- `Schema Name`**:** This represents the schema or user namespace within the PostgreSQL database that contains tables, views, and other database objects.
- `Connect through SSH`**:** Enable this option to connect to Unifyapps using an SSH tunnel, instead of directly connecting to your PostgreSQL database host. This provides an additional level of security to your database by not exposing your PostgreSQL setup to the public.
- `SSH Host`**:** Enter the hostname or IP address of the SSH server that acts as the gateway to your database. Example: ssh.example.com or 203.0.113.1
- `SSH Port`**:** Specify the port number on which the SSH server is listening. Default is usually 22, but it may be different for security reasons.
- `SSH User`**:** Provide the username for authenticating with the SSH server. This is typically the user account on the remote server with necessary permissions.
- `RSA Private Key`**:** Provide the RSA private key corresponding to the public key stored on the SSH server.
- `Client Certificate`**:** Obtain a valid client certificate issued by a trusted Certificate Authority (CA). This certificate authenticates your client to the database server.
- `SSL Certificate Key`**:** This is the private key corresponding to your client certificate.
- `Server Certificate`**:** Obtain the database server's SSL certificate. This certificate verifies the server's identity to your client. Often provided by your database administrator or hosting service.

## Actions

The following actions are available to create custom automations on the Unifyapps platform:

| **Action** | **Description** |
|---|---|
| `Create Snapshot of Table` | Creates a snapshot of a table and stores it in S3. |
| `Create a Table and Insert Record` | Creates a new table and inserts a record into it. |
| `Delete Rows` | Deletes rows from a table in PostgreSQL. |
| `Execute a SQL Statement` | Executes a SQL statement in a PostgreSQL database. |
| `Export Query Result as CSV` | Exports the result of a query as a CSV file. |
| `Export Table as CSV` | Exports an entire table as a CSV file. |
| `Get customer by ID` | Retrieves the details of a customer by ID in Stripe |
| `Get invoice by ID` | Retrieves the details of an invoice by ID in Stripe |
| `Search invoice item` | Retrieves the details of the invoice item in Stripe |
| `Search invoice item` | Retrieves the details of an invoice item in Stripe |
| `Cancel a subscription` | Cancels a subscription in Stripe |
| `Get Table Schema` | Retrieves the schema (column definitions) of a PostgreSQL table. |
| `Insert Record` | Inserts a new record into a PostgreSQL table. |
| `Insert Row` | Inserts a new row into a PostgreSQL table. |
| `List All Databases` | Lists all databases in a PostgreSQL instance. |
| `List Tables for a Schema` | Lists all tables within a specified schema in PostgreSQL. |
| `Select Rows` | Selects rows from a PostgreSQL table based on specified criteria. |
| `Update Rows` | Updates existing rows in a PostgreSQL table. |

## Triggers

The following actions are available to create custom automations on the Unifyapps platform:

| **Trigger** | **Description** |
|---|---|
| `New/updated row` | Triggers when a record/batch of records is inserted/updated in a table in PostgreSQL |
| `New row` | Triggers when new rows/batch of rows is created in a table in PostgreSQL |
