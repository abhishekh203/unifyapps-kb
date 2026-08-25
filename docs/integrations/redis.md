# Redis connector

Source: https://www.unifyapps.com/docs/unify-integrations/redis
Section: integrations

---

The Redis connector enables seamless interaction with your Redis database by offering robust functionalities to manage data efficiently. It supports operations such as getting, setting, and deleting key-value pairs, as well as retrieving all keys, ensuring smooth integration and effective control over your Redis environment.

Integrating Redis with your application provides high-speed data caching and real-time processing, boosting performance and scalability.

## Authentication and Connection Details

Before integrating Redis, ensure you have the following information:

- `Connection Name`: Choose a descriptive name for your Redis connection to help you identify it within your application or integration settings. A meaningful name, like "MyAppRedisIntegration," helps maintain organization, especially when managing multiple integrations.
- `Host Address`: The hostname or IP address of the Redis server (e.g., redis15.localnet.org).
- `Port Number`: The port number on which the Redis server is running (default: 6379).
- `Username`: Username for redis server
- `Password`: Password for redis server
- `Redis Type`: Choose between Cluster or Standalone mode for connecting to your Redis instance.
- `SSL`: Enable or disable SSL for secure communication with the Redis server.

## **Actions**

| Actions | Description |
|---|---|
| `Get Key` | Gets a key from redis |
| `Set Key` | Sets key to hold values in redis |
| `Delete Key` | Deletes a key in redis |
| `Get all keys` | Gets all keys from redis |
