# StarRocks connector

Source: https://www.unifyapps.com/docs/unify-integrations/starrocks
Section: integrations

---

StarRocks is a high-performance distributed SQL data warehouse designed for real-time analytics. It enables fast querying of large-scale datasets with support for OLAP workloads, real-time ingestion, and seamless integration with data lakes and streaming systems. StarRocks is optimized for low-latency queries, high concurrency, and scalable storage, making it suitable for business intelligence, reporting, and interactive analytics use cases.

## Authentication:

Integrating your application with StarRocks allows you to execute SQL queries, manage databases and tables, load data, and export query results. Before starting, ensure you have the following information:

- `Connection Name`**:** Choose a meaningful name for your connection. Example: "MyAppStarRocksIntegration".
- `Host`**:** Enter the StarRocks FE (Frontend) host URL or IP address.
- `Port`**:** Enter the query port (default MySQL-compatible port is usually 9030).
- `Database`**:** Provide the default database name you want to connect to.
- `Username`**:** Enter the StarRocks username.
- `Password`**:** Enter the password associated with the user.

## ACTIONS **:**

| **Action Name** | **Description** |
|---|---|
| `Check Load Status` | Checks the status of a data load job in StarRocks. |
| `Create Database` | Creates a new database in StarRocks. |
| `Create Table` | Creates a new table in a specified database. |
| `Create Table From File` | Creates a table based on schema inferred from an uploaded file. |
| `Describe Table` | Retrieves the structure and column definitions of a table. |
| `Drop Table` | Deletes a table from the database. |
| `Execute Prepared Statement` | Executes a parameterized SQL statement securely. |
| `Execute Select Query` | Executes a SELECT query to retrieve records from a table. |
| `Execute SQL` | Executes a custom SQL command on the connected database. |
| `Execute SQL Metadata` | Retrieves metadata information from executed SQL queries. |
| `Export Records To File` | Exports query results to a downloadable file. |
| `Extract Columns Info` | Extracts column details from a query or table. |
| `Fetch Columns Information` | Fetches detailed column metadata from a specified table. |
| `Fetch Table Schema` | Retrieves the complete schema definition of a table. |
| `List Tables` | Lists all tables available in a specified database. |
| Load Data From File | Loads structured data into a table from a file source. |
| Load Data From File Using Broker Load | Loads data into StarRocks using the broker load mechanism. |
