# SAP HANA connector

Source: https://www.unifyapps.com/docs/unify-integrations/sap-hana
Section: integrations

---

SAP HANA is a widely used in-memory database platform by SAP, allowing you to store, process, and analyze large volumes of data effortlessly. It offers robust features like real-time data processing, advanced analytics, and integration with various SAP applications such as SAP S/4HANA and SAP BW. With strong performance and security, SAP HANA is ideal for efficient, high-speed data management and advanced business intelligence.

Integrating SAP HANA with your application enables seamless data communication, real-time analytics, and efficient data management, empowering smarter decision-making and streamlined operations.

## Authentication

Before integrating SAP HANA, ensure you have the following information:

- `Connection Name`: Choose a descriptive name for your SAP HANA connection to help you identify it within your application or integration settings. A meaningful name, like "MyAppSAPHANAIntegration," helps maintain organization, especially when managing multiple integrations.
- `Domain`: Specify the domain name of the SAP HANA server (e.g., sap.hana.domain.com). This identifies the network location where your SAP HANA instance is hosted.
- `Host`**:** Enter the hostname or IP address of the SAP HANA server:
  - Example hostname: sap-hana-server1.company.com
  - Example IP address: 192.168.xx.xx
- `Email`**:** Provide the email address associated with this connection for authentication.
- `Password`**:** Enter the password for the user or service account associated with the SAP HANA connection.
- `Port`**:** Specify the port number for connecting to the SAP HANA server (default: 30015 for tenant databases, 30013 for the system database).

## Actions

| **Action** | **Description** |
|---|---|
| `Add purchase order` | Add purchase order in SAP HANA |
| `Create directory` | Create directory in SAP HANA |
| `Create file` | Create file in SAP HANA |
| `Delete file or folder` | Delete file or folder in SAP HANA |
| `Get directory contents` | Get directory contents in SAP HANA |
| `Get file metadata` | Get file metadata in SAP HANA |
| `Get folder metadata` | Get folder metadata in SAP HANA |
| `Set file contents` | Set file contents in SAP HANA |
