# Oracle NoSQL integration

Source: https://www.unifyapps.com/docs/unify-integrations/oracle-nosql
Section: integrations

---

Oracle NoSQL Database is a distributed, scalable database designed for handling large volumes of unstructured data with low latency. It supports flexible data models, enabling real-time applications and high-performance transactions.

Integrating Oracle NoSQL Database enables high-speed data processing, scalability, and real-time analytics, while supporting flexible data models to meet diverse application needs.

## Authentication

Before integrating Oracle NoSQL, ensure you have the following information:

- `Connection Name`**:** Choose a descriptive name for your Oracle NoSQL connection to help you identify it within your application or integration settings. A meaningful name, like "MyAppOracleNoSQLCIntegration," helps maintain organization, especially when managing multiple integrations.
- `Host`**:** Provide the hostname of your Oracle NoSQL Database service endpoint. This is the URL or IP address where the Oracle NoSQL Database is hosted. For example, it might look like nosql.[region].oci.oraclecloud.com. Ensure you copy it correctly from your Oracle Cloud Console to avoid connectivity issues.
- `OCI private key`**:** Paste the contents of the private key file you downloaded from the Oracle Cloud Infrastructure Console. This private key file is in PEM format and is used for securely authenticating with the Oracle Cloud Infrastructure API. Ensure you keep this key confidential and do not share it.
- `Tenancy OCID`**:** Enter the OCID (Oracle Cloud Identifier) of your tenancy. This is a unique identifier for your Oracle Cloud account and can be found in the "Tenancy Information" section of your Oracle Cloud Console.
- `User OCID`**:** Provide the OCID of the user who will authenticate with the Oracle Cloud Infrastructure API. This is a unique identifier for the user in your Oracle Cloud account, which you can find in the "User Details" section of the Oracle Cloud Console.
- `API key fingerprint`**:** Input the fingerprint of the public key that you uploaded to the Oracle Cloud Infrastructure Console. This fingerprint is a unique identifier for your public key and is displayed when you upload the public key during API key setup in Oracle Cloud. For more details refer [this](https://apexapps.oracle.com/pls/apex/r/dbpm/livelabs/run-workshop?p210_wid=879).

## Actions

| **Action** | **Description** |
|---|---|
| `Execute a query` | Execute a query |
| `Get a list of tables` | Get a list of tables |
| `Write a single row` | Write a single row |
