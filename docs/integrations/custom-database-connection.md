# Custom Database Connection

Source: https://www.unifyapps.com/docs/unify-integrations/custom-database-connection
Section: integrations

---

The Custom Database connector allows seamless integration with any database that supports JDBC drivers. It provides functionalities for efficient interaction with your database, including connecting, querying, and managing data.

## Authentication

Before integrating your custom database, ensure you have the following information:

- `Connection Name`: Choose a descriptive name for your database connection to help identify it within your application or integration settings.
- `Connection URL`: The JDBC connection string for the database, which typically includes the hostname, port, database name, and additional parameters (e.g., jdbc:postgresql://<endpoint>:<database_port>/<database_name>).
- `Username`: The username required to authenticate with the database.
- `Password`: The password required for authentication.

## Actions

| Actions | Description |
|---|---|
| `Execute SQL statement` | Execute a SQL query |
