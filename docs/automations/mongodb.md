# MongoDB

Source: https://www.unifyapps.com/docs/unify-automations/mongodb
Section: automations

---

MongoDB is a flexible, document-based NoSQL database designed for handling and scaling large volumes of diverse data.

Integrating MongoDB enables efficient data retrieval, horizontal scalability, high availability, and supports dynamic schema, making it ideal for applications requiring flexibility and rapid iteration.

## Authentication

To connect your application to MongoDB, ensure you have the following information ready:

- `Connection Name`: Choose a name to identify this MongoDB connection within your application or integration settings. Use a descriptive name like "MyAppMongoDBIntegration".
- `Database Host`: Provide the MongoDB database host's IP address or DNS. *Note*: For URL-based hostnames, omit the http:// or https:// prefix. For example, if the hostname URL is https://mongodb-qa.xxxx.ap-south-1.docdb.amazonaws.com, enter mongodb-qa.xxxx.ap-south-1.docdb.amazonaws.com.
- `Database Port`: Specify the port on which your MongoDB server listens for connections. Default value: 27017.
- `Database User`: Enter the username that has the permissions to read or modify collections in your MongoDB database.
- `Database Password`: The password for the database user.
- `Schema Name`: (Optional) If needed, specify the schema or database within MongoDB that contains collections, views, and other objects.
- `Connect through SSH`: Enable this option if you want to connect using an SSH tunnel instead of directly connecting to your MongoDB database host. This provides additional security by not exposing MongoDB to the public internet.
  - **SSH Host**: Enter the hostname or IP address of the SSH server acting as a gateway to your database, e.g., ssh.example.com or 203.0.113.1.
  - **SSH Port**: Specify the port on which the SSH server is listening, typically 22.
  - **SSH User**: Provide the username for authentication on the SSH server.
  - **RSA Private Key**: The RSA private key corresponding to the public key stored on the SSH server.
  - **Client Certificate**: Obtain a valid client certificate issued by a trusted Certificate Authority (CA) to authenticate your client with the MongoDB server.
  - **SSL Certificate Key**: The private key that corresponds to your client certificate.
  - **Server Certificate**: Obtain the MongoDB server’s SSL certificate to verify the server’s identity.

## Actions

| **Action** | **Description** |
|---|---|
| `Count Records` | Counts records in a collection from a MongoDB database. |
| `Create Snapshot of Collection` | Creates a snapshot of a collection in MongoDB. |
| `Create Document` | Creates a document in an existing MongoDB collection. |
| `Delete Documents` | Deletes documents in an existing MongoDB collection. |
| `Fetch Collection Metadata` | Fetches collection metadata from a MongoDB database. |
| `Fetch Database Metadata` | Finds documents from a MongoDB collection. |
| `Find Documents` | Finds documents from a MongoDB collection. |
| `Insert Document` | Inserts a document in an existing MongoDB collection. |
| `List Collections` | Lists collections in a MongoDB database. |
| `Replicate Documents` | Replicates documents in a MongoDB collection. |
| `Update Documents` | Updates documents in a MongoDB collection. |

## Triggers

| **Trigger** | **Description** |
|---|---|
| `Triggers an event on changes to collection's records` | Triggers when a record is inserted or updated in a MongoDB database |
