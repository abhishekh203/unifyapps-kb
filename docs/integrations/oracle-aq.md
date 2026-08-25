# Oracle AQ connector

Source: https://www.unifyapps.com/docs/unify-integrations/oracle-aq
Section: integrations

---

Using Oracle Advanced Queuing (Oracle AQ) enables your organization to build robust, event-driven applications. Oracle AQ allows you to integrate messaging and queuing functionalities directly into your Oracle database, providing reliable message delivery, guaranteed message ordering.

Integrating your application with Oracle AQ helps manage asynchronous communication, event notifications, and workflow automation seamlessly.

## Authentication

Before you begin, make sure you have the following information:

- `Connection Name`: Choose a meaningful name for your connection. This name helps you identify the connection within your application or integration settings. It could be something descriptive like "MyAppOracleAQ".
- `Database Host`: The Oracle database host’s IP address or DNS. **Note:** For URL-based hostnames, exclude the http:// or https:// part. For example, if the hostname URL is https://oracledb-qa.xxxx.ap-south-1.rds.amazonaws.com, enter oracledb-qa.xxxx.ap-south-1.rds.amazonaws.com.
- `Database Port`: The port on which your Oracle server listens for connections. Default value: 1521.
- `Database User`: The authenticated user who has the permissions to read tables in your database.
- `Database Password`: The password for the database user.
- `SID` or `Service Name` : The unique name identifying your specific database instance on the server. To retrieve the Service Name, open your Oracle server in any SQL client tool as a database user with SYSDBA privilege and enter the following command: `select name from v$database;`
- `PDB Name`: A unique identifier for a Pluggable Database within Oracle's multitenant architecture applies only if you're working with a Container Database (CDB) and need to connect to a specific Pluggable Database (PDB).
- `Schema Name`: This represents the schema or user namespace within the Oracle database that contains tables, views, and other database objects.
- `Connect through SSH`: Enable this option to connect to Unifyapps using an SSH tunnel, instead of directly connecting to your Oracle database host. This provides an additional level of security to your database by not exposing your Oracle setup to the public.
- `SSH Host`: Enter the hostname or IP address of the SSH server that acts as the gateway to your database. Example: ssh.example.com or 203.0.113.1
- `SSH Port`: Specify the port number on which the SSH server is listening. Default is usually 22, but it may be different for security reasons.
- `SSH User`: Provide the username for authenticating with the SSH server. This is typically the user account on the remote server with necessary permissions.
- `RSA Private Key`: Provide the RSA private key corresponding to the public key stored on the SSH server.
- `Client Certificate`: Obtain a valid client certificate issued by a trusted Certificate Authority (CA).This certificate authenticates your client to the database server.
- `SSL Certificate Key`:This is the private key corresponding to your client certificate.
- `Server Certificate`: Obtain the database server's SSL certificate. This certificate verifies the server's identity to your client. Often provided by your database administrator or hosting service.

## Actions

| **Action Name** | **Description** |
|---|---|
| `Create queue table` | Creates a queue table in Oracle AQ. |
| `Alter queue table` | Alters a queue table in Oracle AQ. |
| `Drop queue table` | Drops a queue table in Oracle AQ. |
| `Purge queue table` | Purges a queue table in Oracle AQ. |
| `Migrate queue table` | Migrates a queue table in Oracle AQ. |
| `Publish message` | Publishes a message in Oracle AQ. |
| `Publish messages` | Publishes a batch of messages in Oracle AQ. |
| `Subscribe message` | Subscribes to a message from Oracle AQ. |
