# Databricks connector

Source: https://www.unifyapps.com/docs/unify-integrations/databricks
Section: integrations

---

# Databricks

Using Databricks enables you to process large-scale data efficiently with unified analytics. It provides a collaborative environment for data engineering, data science, and analytics using Apache Spark. Databricks allows you to execute queries, manage structured and unstructured data, and perform advanced analytics with high performance and scalability.

Integrating your application with a Databricks cluster enables secure data access, fast query execution, and seamless data management across your data lake and warehouse.

### Authentication

Before you begin, make sure you have the following information:

1. `Connection Name`**:** This is a user-defined name for your Connection to the database / API. Choose a descriptive name that will help you easily recognize the connection later.
2. `Host Address`**:** The server hostname of the databricks cluster.
3. `Port Number`**:** The port number on which the cluster is listening.
4. `Protocol`**:** The protocol to connect to the cluster with.
5. `HTTP Path`**:** The HTTP Path for the databricks cluster.
6. `Catalog Name`**:** The catalog in which your tables belong to in the databricks cluster.
7. `Schema Name`**:** The schema to refer to by default when not specified.
8. `Authentication Type`**:** Currently supports Basic Authentication only.
9. `Username`**:** Enter your Databricks username for authentication.
10. `Password`**:** Enter your Databricks password for secure authentication. If the username is 'token', in that case you have to use the 'access_token' provided for the databricks server.
11. `Connection`**:** Choose the method of connection to your Databricks server.
12. `SSL Configuration`**:** SSL is enabled by default for secure data transfer. You can configure certificates, trust settings, and host verification as needed.

### **ACTIONS :**

| **Action Name** | **Description** |
|---|---|
| `Execute a SQL statement` | Executes a SQL statement via Databricks |
| `Fetch schemas` | Fetch list of schemas |
| `Fetch tables` | Fetch list of tables |
