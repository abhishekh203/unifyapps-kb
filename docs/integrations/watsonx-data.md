# Watsonx data integration

Source: https://www.unifyapps.com/docs/unify-integrations/watsonx-data
Section: integrations

---

## **Watsonx Data**

IBM watsonx.data enables teams to run interactive analytics directly on their data lake using the high-performance Presto engine. It provides scalable, open, and governed access to data across multiple sources, helping organizations derive insights faster while maintaining enterprise-grade security and flexibility. With seamless integration and cloud-native architecture, watsonx.data supports advanced analytics and AI-driven workloads efficiently.

### **Authentication**

Integrating your application with IBM watsonx.data allows secure access to your data lake through the Presto engine. Before starting, ensure you have the following information:

`Connection Name` : Choose a meaningful name for your connection. This helps you identify it within your application or integration settings.It could be something descriptive like "MyAppWatsonxDataIntegration" .

`Database Host` : Enter the hostname or IP address of the Presto engine .

`Database Port` : Enter the port on which the Presto engine listens. 
`Default` : 31760

`Database User` : Use ibmlhapikey as the database username.

`Database Password` : Use your IBM Cloud API key as the database password.

`Catalog Name` : Enter the unique identifier of the catalog you want to connect to .

`Schema Name` : Enter the schema within the selected catalog .

### **Getting Presto Engine Hostname and Port**

1. Log in to the watsonx.data web console.
2. Navigate to **Infrastructure Manager** and switch to **List view**.
3. Open the **Engines** tab.
4. Click the engine name to view its details.
5. Copy the **Hostname** and **Port** using the copy-to-clipboard icon.

### **Getting IBM Cloud API Key**

1. Log in to the **IBM Cloud console**.
2. Navigate to **Manage → Access (IAM)**.
3. Click **API keys** from the left navigation panel.
4. Click **Create +**.
5. Enter a name and description, then click **Create**.
6. Download and securely store the generated API key.

### **Optional: SSH Authentication**

If your setup requires SSH tunneling, provide the following details:

- `SSH Host`: Hostname or IP address of the SSH gateway (for example, ssh.example.com)
- `SSH Port`: SSH port number (default: 22)
- `SSH User`: SSH login username
- `RSA Private Key`: RSA private key used for SSH authentication

### **Optional: SSL Authentication**

If SSL authentication is required, provide the following certificates:

- `Client Certificate`: Certificate issued by a trusted Certificate Authority.
- `SSL Certificate Key`: Private key associated with the client certificate.
- `Server Certificate`: SSL certificate of the Presto server (typically provided by the administrator).

### **Actions**

| **Actions** | **Descriptions** |
|---|---|
| `Execute a SQL statement` | Executes a SQL statement in IBM Watsonx Data |
