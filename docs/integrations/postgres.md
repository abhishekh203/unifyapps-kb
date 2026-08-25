# Postgres connector

Source: https://www.unifyapps.com/docs/unify-integrations/postgres
Section: integrations

---

## **PostgreSQL**

Using PostgreSQL enables reliable, secure, and scalable relational data storage. It supports advanced SQL querying, indexing, transactions, and strong consistency guarantees. PostgreSQL is well-suited for applications requiring complex queries, structured schemas, and ACID-compliant operations. It also provides robust security features such as SSL encryption, role-based access control, and secure authentication mechanisms.

### **Authentication**

Integrating your application to a PostgreSQL database enables seamless integration for data storage, retrieval, and advanced database functionalities. Before you begin, make sure you have the following information:

**Connection Name :**Choose a meaningful name for your connection. This name helps you identify the connection within your application or integration settings.It could be something descriptive like "MyAppPostgreSQLIntegration".

**Host Address:**The IP address or DNS name of the PostgreSQL database server.

**Port Number:** The port on which the PostgreSQL server is listening. 
  Default value: 5432

**User:** The authenticated user who has the permissions to read tables in your database.

**Password:** The password for the database user.

**Database Name:**The name of the PostgreSQL database you want to connect to.

**Schema Name:**The schema or namespace within the PostgreSQL database that contains tables, views, and other database objects.

Default value: public

**Connection:** Choose the method of connection to your PostgreSQL database server.

**Direct:** Connecting directly to the PostgreSQL database server without any intermediary.This is the simplest and most common method of connecting.

**SSH:** Connecting to the PostgreSQL database server through a secure SSH tunnel via an intermediary host. This is an effective method for adding network-level security when direct access to the database is restricted.

**SSH Host:** Enter the hostname or IP address of the SSH server that acts as the gateway to your database. 
**SSH Port:** Specify the port number on which the SSH server is listening. 
 Default is usually 22, but it may differ based on security policies.

**SSH User :** Provide the username for authenticating with the SSH server. 
 This is typically the user account on the remote server with the necessary permissions. 
**RSA Private Key:** Provide the RSA private key corresponding to the public key stored on the SSH server.

**SSL Secure:** Enable this option to establish an SSL-encrypted connection to the PostgreSQL database server. This adds an extra layer of security by encrypting data in transit.

**Client Certificate:**Obtain a valid X.509 client certificate issued by a trusted Certificate Authority (CA). This certificate authenticates your client to the PostgreSQL server. 
 Supported format: .pem

**SSL Certificate Key:** This is the private key corresponding to your client certificate. 
 Supported format: .pem

**Server Certificate:** Obtain the PostgreSQL server’s SSL certificate. 
 This certificate verifies the server’s identity to your client and is often provided by your database administrator or hosting service. 
  Supported format: .pem

### **Actions**

| **Actions** | **Descriptions** |
|---|---|
| **Create snapshot of table** | Create snapshot of a table and store in S3 from PostgreSQL |
| **Delete rows** | Delete rows in a table in PostgreSQL |
| **Execute a SQL statement** | Execute a SQL statementExecutes a SQL statement in a database in PostgreSQL |
| **Export query result** | Export query result as CSV file in PostgreSQL |
| **Get table schema** | Get table schema from PostgreSQL |
| **Insert row** | Insert row into a table in PostgreSQL |
| **List all databases** | Lists all databases in PostgreSQL |
| **List tables for a schema** | Lists tables for a schema in PostgreSQL |
| **Run long query using custom SQL** | Run long query using custom SQL in PostgreSQL |
| **Select rows** | Select rows from a table in PostgreSQL |
| **Select rows using custom sql** | Select rows using custom sql from a table in PostgreSQL |
| **Update row** | Update row in a table in PostgreSQL |
| **Upsert rows** | Upsert rows in a table in PostgreSQL |

### **Triggers**

| **Triggers** | **Description** |
|---|---|
| **Delete row** | Triggers when a row is deleted in PostgreSQL |
| **New event** | Triggers when a new event occurs in PostgreSQL |
| **New row** | Triggers when a row is inserted in PostgreSQL |
| **New/Update row** | Triggers when a row is inserted or updated in PostgreSQL |
| **Scheduled query** | Execute query on specified schedule and return results as list of rows |
| **Update row** | Triggers when a row is updated in PostgreSQL |
