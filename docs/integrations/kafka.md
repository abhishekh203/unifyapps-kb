# Kafka connector

Source: https://www.unifyapps.com/docs/unify-integrations/kafka
Section: integrations

---

The Kafka connector integrates seamlessly with Apache Kafka, enabling efficient data streaming and event processing. It offers robust capabilities for secure, scalable, and real-time data exchange.

## Authentication

Before you begin integration, ensure you have the following information:

- `Connection Name`**:** Choose a meaningful name for your connection. This name helps you identify the connection within your application or integration settings. It could be something descriptive like "MyAppKafkaIntegration".
- `Bootstrap Server URLs`**:** Broker server URLs separated by a comma (","). Eg: kafka-broker-001:9092,kafka-broker-002:9092
- `Endpoint`**(Deprecated)**: The Kafka brokers' IP address or DNS name.
- `Port Number`**(Depracated)**: The port on which your Kafka server listens for connections. Default value: 9094.
- `Database Username`**:** The authenticated user with the permissions to read tables in your database.
- `Database Password`**:** The password for the database user.
- `Topic Prefix`**:** The prefix to filter topics by. Leave blank to fetch all topics.
- `Properties`**:** Kafka connections often require advanced configurations through key-value pairs to tailor the connection to specific security protocols and operational needs. These properties can be set here.
  - `Key`**:** The property key. Kafka-specific configuration options can be set here. Example: “sasl.mechanism”.
  - `Value`**:** The value for the specified property key. Example: “PLAIN”.
- `SSL Secure`**:** Enable this option to Connect over an SSL-encrypted connection.
- `Client Certificate`: Obtain a valid client certificate from a trusted Certificate Authority (CA). This certificate authenticates your client to the database server.
- `SSL Certificate Key`: This private key corresponds to your client certificate.
- `Server Certificate`**:** Obtain the database server's SSL certificate. This certificate verifies the server's identity to your client. Often provided by your database administrator or hosting service.

## Actions

| Actions | Description |
|---|---|
| `Bulk create records in Kafka` | Bulk Create records in Kafka |
| `Commit offsets in Kafka` | Commit offsets in Kafka |
| `Create record in Kafka` | Create a record in Kafka |
| `Create topic in Kafka` | Creates a topic in Kafka |
| `Get consumer groups metadata` | Gets group metadata from Kafka |
| `Get topics metadata` | Gets topic metadata from Kafka |
| `Polls for new records from Kafka topic` | Polls for new records from Kafka topic |

## Triggers

| Triggers | Description |
|---|---|
| `Trigger from event in a topic in Kafka` | Triggers on record in Kafka |
