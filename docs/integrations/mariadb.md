# MariaDB connector

Source: https://www.unifyapps.com/docs/unify-integrations/mariadb
Section: integrations

---

Integrating your application with MariaDB enables efficient data storage, high-performance querying, and reliable database management. As a MySQL-compatible relational database, MariaDB supports scalable applications, transactional operations, and robust data handling for modern systems .

## Authentication:

Connecting your application with MariaDB ensures secure and consistent database operations. Before you begin, ensure you have the following information:

- `Connection Name`**:** Choose a meaningful and unique name for your connection. This helps you identify it within your application or integration settings *(e.g., "MyAppMariaDBConnection").*
- `Host Address` **:** Provide the IP address or DNS name of your MariaDB server *(e.g., "127.0.0.1", "mariadb.example.com")*
- `Port Number` **:** Specify the port on which the database server is listening. The default MariaDB port is : 3306.
- `User` **:** Enter the username used to authenticate with the database.
- `Password` **:** Provide the password associated with the database user.
- `Database Name` **:** Specify the name of the existing database you want to connect to.

### **Connection Type :** Choose how your application connects to the database:

`Directly` **:** Connect directly to the MariaDB server using the provided host, port, and credentials. Suitable for secure and internal environments.

`Via SSH` **:** Connect securely through an SSH tunnel. Recommended when the database server is not publicly accessible. You may need:

- **SSH Host**
- **SSH Port**
- **SSH Username**
- **SSH Password or Private Key**

`SSL Secure` **:** Enable SSL encryption to secure communication between your application and the MariaDB server.

`Client Certificate`**:** Upload the X509 client certificate (.pem format)

- **SSL Certificate Key:** Upload the RSA client key (.pem format)
- **Server Certificate:** Upload the X509 server certificate (.pem format)

## Actions:

| **Action Name** | **Descriptions** |
|---|---|
| `Delete rows` | Deletes rows in a table in MariaDB |
| `Execute SQL statement` | Executes a SQL query in MariaDB |
| `Insert row` | Inserts a row in a table in MariaDB |
| `Select rows` | Selects rows in a table in MariaDB |
| `Update rows` | Updates rows in a table in MariaDB |
