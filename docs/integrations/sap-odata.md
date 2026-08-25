# SAP OData connector

Source: https://www.unifyapps.com/docs/unify-integrations/sap-odata
Section: integrations

---

# SAP OData

SAP OData integration enables businesses and developers to securely connect applications with SAP systems using OData services. It allows seamless data exchange for enterprise objects such as purchase orders, purchase requisitions, attachments, and other business entities. Through standardized RESTful APIs, SAP OData helps automate workflows, synchronize enterprise data, and build scalable integrations.

### Authentication :

Integrating your application with SAP OData requires proper authentication and endpoint configuration. Before starting, ensure you have the following information:

- `Connection Name`**:** Choose a meaningful name for your connection. Example: *MyAppSAPODataIntegration*.
- `SAP Base URL`**:** Your SAP OData service root URL (e.g., https://your-sap-system.com/sap/opu/odata/sap/SERVICE_NAME/).
- `Authentication Type`**:**
- `Required Credentials`**:** SAP username and password or OAuth access token.

### Basic Authentication Setup :

1. Log in to your SAP system.
2. Ensure OData services are activated in SAP Gateway (/IWFND/MAINT_SERVICE).
3. Obtain the service URL.
4. Use your SAP username and password for API authentication.

## ACTIONS :

| **Action Name** | **Description** |
|---|---|
| `Create Object` | Create a new business object (e.g., Purchase Order, Purchase Requisition) in SAP via OData service. |
| `Download Attachment` | Download attachment files associated with a specific SAP business object. |
| `Get Purchase Order By ID` | Retrieve detailed information of a specific Purchase Order using its unique identifier. |
| `List Attachments` | Retrieve a list of attachments linked to a specific SAP object. |
| `List Purchase Orders` | Fetch a list of purchase orders from SAP based on filters or query parameters. |
| `List Purchase Requisitions` | Fetch a list of purchase requisitions from SAP based on defined criteria. |
| `On New Object` | Trigger-based action that detects and processes newly created objects in SAP. |
| `Search Objects` | Search for SAP business objects using dynamic query parameters and filters. |
