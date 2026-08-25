# Mongo connector

Source: https://www.unifyapps.com/docs/unify-integrations/mongo
Section: integrations

---

## **MongoDB**

Using MongoDB makes managing and analyzing flexible datasets faster and more scalable. It allows you to store JSON-like documents, handle dynamic schemas, and perform rapid lookups across distributed clusters. MongoDB ensures your data is stored and accessed securely with built-in encryption, role-based access control, and ACID transactions for multi-document operations.

### **Authentication**

Integrating your application to a MongoDB database enables flexible document storage, powerful aggregation pipelines, and real-time data synchronization capabilities.Before you begin, make sure you have the following information:

**Connection Name :** Choose a meaningful name for your connection. This name helps you identify the connection within your application or integration settings. It could be something descriptive like "MyAppMongoDBIntegration".

**Authentication type :** MongoDB supports two types of authentications. They are :

- Basic Authentication
- IAM Role

**Host address :** The IP address or DNS name of the database server.

**Port number :** The port on which the Mongo database is listening.

**Database name :** The name of the Mongo database you want to load data from.

**Authentication database :** Specify your authentication database. Required if it is different from the admin database.

**Connection :** Choose the method of connection to your MongoDB Server server.

- **Direct** : Connecting directly to the MongoDB Server server without any intermediary. It's the simplest and most common method of connecting.
- **SSH** : Connecting to the MongoDB Server through a secure SSH tunnel via an intermediary host. It's an effective method for adding network-level security when direct access is restricted.

**SSL Secure**:  This option enables SSL encryption for the MongoDB Server connection, adding an extra layer of security to your data transfer.

1. **Client Certificate :** Obtain a valid client certificate issued by a trusted Certificate Authority (CA).This certificate authenticates your client to the database server.
2. **SSL Certificate Key :** This is the private key corresponding to your client certificate.
3. **Server Certificate :** Obtain the database server's SSL certificate. This certificate verifies the server's identity to your client. Often provided by your database administrator or hosting service.

**Basic Authentication Based :**
**1. User :** Enter the username of someone who can read objects in your database.

**2. Password** : Enter the password for the database user.

### **IAM Role Based :**

**1. IAM Role :** Enter the IAM role ARN that you want to use for authentication.

**2**. **External Id :** Enter the external ID that you want to use for authentication.

**3**. **Region** **:**  Enter 'us-east-1' as your region, if your AWS account url starts with https://us-east-1.console.aws.amazon.com.

### **ACTIONS :**

| **Action Name** | **Description** |
|---|---|
| **Aggregate documents in MongoDB collection** | Aggregate documents in MongoDB collection |
| **Bulk write documents** | Bulk write documents in MongoDB collection |
| **Create collection** | Creates a collection in MongoDB |
| **Create document** | Creates a document in an existing MongoDB collection |
| **Create snapshot of collection** | Create snapshot of a collection in MongoDB |
| **Get current operations** | Get currently running operations in MongoDB server with filtering options |
| **Delete documents** | Deletes a document in an existing MongoDB collection |
| **Fetch Collection Metadata** | Fetches collection metadata from a MongoDB Database |
| **Fetch Database Metadata** | Fetches database metadata from a MongoDB Database |
| **Find documents** | Finds documents from a MongoDB collection |
| **Get indexes** | Get all indexes from a MongoDB collection |
| **Insert document** | Insert a document in an existing MongoDB collection |
| **List collections** | Lists collections in a MongoDB database |
| **Replicate documents** | Replicate documents in MongoDB collection |
| **Server status** | Get MongoDB server status and statistics |
| **Update documents** | Updates a document in a MongoDB collection |

### **Triggers :**

| **Trigger Name** | **Description** |
|---|---|
| **Delete record** | Triggers when a record is deleted in a MongoDB database |
| **New event** | Triggers when a record is inserted or updated or deleted in a MongoDB database |
| **New record** | Triggers when a record is inserted in a MongoDB database |
| **New/Update record** | Triggers when a record is inserted or updated in a MongoDB database |
| **Update record** | Triggers when a record is updated in a MongoDB database |
