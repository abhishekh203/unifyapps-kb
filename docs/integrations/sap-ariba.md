# SAP Ariba connector

Source: https://www.unifyapps.com/docs/unify-integrations/sap-ariba
Section: integrations

---

SAP Ariba empowers organizations to streamline and transform their core business operations through intelligent ERP, finance, supply chain, procurement, and HR solutions tailored for the regional market. By combining cloud-based innovation with industry-specific best practices, SAP Ariba enables businesses to automate complex workflows, ensure regulatory compliance, and gain real-time visibility across operations.

## Authentication:

Integrating your application with SAP Ariba allows businesses to extend their SAP ecosystem with reliable data synchronization, intelligent process orchestration, and secure system interoperability. Before starting, ensure you have the following information:

1. `Connection Name`**:** Choose a meaningful name for your connection. This name helps you identify the connection within your application or integration settings. It could be something descriptive like "MyAppSAPAribaIntegration".
2. `Applications`**:** Select the Ariba applications you wish to integrate.
3. `Datacenter`: Select the datacenter you would like to connect to.
4. `Client ID`**:** Enter the OAuth Client ID of your application which will be generated when the application was approved for production.To retrieve your Client ID click[here](https://help.sap.com/docs/ariba-apis/help-for-sap-ariba-developer-portal/finding-your-application-s-application-key-and-oauth-client-id?locale=en-US).
5. `Client secret`: Enter the client secret generated with your client ID when you first registered your application in SAP Ariba.
6. `Application key`**:** The application key was generated when the application was first created. To retrieve your application key click[here.](https://help.sap.com/docs/ariba-apis/help-for-sap-ariba-developer-portal/finding-your-application-s-application-key-and-oauth-client-id?locale=en-US)

## Actions  :

| **Action Name** | **Description** |
|---|---|
| `Get data from view template` | Gets data from a view template using Procurement Reporting API in SAP Ariba |
| `Get entity metadata` | Gets entity meta data using Master Data Retrieval API for Procurement in SAP Ariba |
| `Get entity metadata` | Gets entity meta data using Master Data Retrieval API for Sourcing in SAP Ariba |
| `List entities` | Lists entities using Master Data Retrieval API for Procurement in SAP Ariba |
| `List entities` | Lists entities using Master Data Retrieval API for Sourcing in SAP Ariba |
| `List objects` | Retrieves a list of objects in SAP Ariba |
| `Search entities` | Searches entities using Master Data Retrieval API for Procurement in SAP Ariba |
| `Search entities` | Searches entities using Master Data Retrieval API for Sourcing in SAP Ariba |
| `Search objects` | Retrieves a list of records in SAP Ariba |
