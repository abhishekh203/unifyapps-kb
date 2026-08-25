# SugarCRM connector

Source: https://www.unifyapps.com/docs/unify-integrations/sugarcrm
Section: integrations

---

# SugarCRM

Sugar CRM helps teams efficiently manage customer relationships by centralizing sales, marketing, and customer data in one platform. It offers flexible customization and automation to align with unique business processes and improve productivity. With real-time insights, strong security, and seamless integrations, Sugar CRM enables better collaboration and smarter decision-making across teams.

### Authentication:

Integrating your application with Sugar CRM enables seamless customer data synchronization, streamlined sales processes, and improved relationship management. Before starting, ensure you have this information:

1. `Connection Name`: Choose a meaningful name for your connection. This name helps you identify the connection within your application or integration settings. It could be something descriptive like "MyAppSugarCRMIntegration".
2. `Authentication type`**:** Select the type of authentication for connecting to your SugarCRM account.
3. `Instance URL`: Enter your instance url. This can be found in your SugarCRM account url.
4. `API version`: Select the REST API version your SugarCRM instance supports. The default is v11.

### OAuth 2.0 Based :

1. `Client ID`: Enter your client ID. To know more about this, follow the [SugarCRM](https://support.sugarcrm.com/documentation/sugar_developer/sugar_developer_guide_14.2/integration/web_services/rest_api/#Overview) official documentation.
2. `Client secret`: Enter your client secret.

### Password grant Based :

1. `Client ID`: Enter your client ID. To know more about this, follow the [SugarCRM](https://support.sugarcrm.com/documentation/sugar_developer/sugar_developer_guide_14.2/integration/web_services/rest_api/#Overview) official documentation.
2. `Client secret`: Enter your client secret.
3. `Username`: Enter the username of your SugarCRM account.
4. `Password`: Enter the password of your SugarCRM account.
5. `Platform identifier`: Enter the unique platform identifier.

### **ACTIONS :**

| **Action Name** | **Description** |
|---|---|
| `Create an outbound email` | Creates an outbound email in SugarCRM |
| `Create new record` | Creates a new record in SugarCRM |
| `Duplicate check` | Duplicates check in SugarCRM |
| `Global search` | Global search in SugarCRM |
| `List staged packages` | Lists staged packages in SugarCRM |
| `Move after target` | Move after target in SugarCRM |
| `Set case as requested for close` | Set case as requested for close in SugarCRM |
| `Update email address` | Update email address in SugarCRM |
| `Count emails` | Count all emails in SugarCRM |
| `Count filtered emails` | Count filtered emails in SugarCRM |
| `Update admin configuration by category` | Sets configuration values for a given configuration category |
| `Enable Elasticsearch refresh` | Enable refresh_interval for all indices managed by SugarCRM |
| `Trigger Elasticsearch refresh` | Triggers an explicit Elasticsearch index refresh for all indices managed by SugarCRM |
| `Create email address` | Creates a new email address in SugarCRM |
| `Create KB configuration` | Creates and/or updates the config settings for the KBContents module in SugarCRM |
| `Create KB content link` | Creates relationships to pre-existing records for a KBContents record in SugarCRM |
| `Count filtered emails` | Count filtered emails in SugarCRM |
| `Get AWS configs` | Gets Amazon Web Services configs from Sugar Serve |
| `Get admin configuration by category` | Gets configuration values for a given category from SugarCRM |
| `Get Elasticsearch indices` | Returns the index statistics for the Elasticsearch backend |
| `Get Elasticsearch mapping` | Returns the mapping for every available Elasticsearch index |
| `Get Elasticsearch queue status` | Returns queue statistics for the Elasticsearch backend in SugarCRM |
| `Get Elasticsearch refresh status` | Returns the current refresh_interval for every index managed by SugarCRM |
| `Get email` | Get email record from SugarCRM |
| `Get knowledge base contents` | Lists filtered KBContents records in SugarCRM |
| `Filter KB contents` | Lists filtered KBContents records in SugarCRM |
| `Get lead free busy` | Get free busy information for a lead |
| `Mark KB content as useful` | Votes for a Knowledge Base article as useful in SugarCRM |
| `List emails` | List emails from SugarCRM |
| `Register lead` | Register a new lead in SugarCRM |
| `Send email` | Sends an email using SugarCRM |
| `Update KB configuration` | Creates and/or updates the config settings for the KBContents module in SugarCRM |
| `Update AWS configs` | Set Amazon Web Services configs in Sugar Serve |
| `Delete package file` | Deletes package file in SugarCRM |
| `Disable IDM mode` | Disable IDM mode in SugarCRM |
| `Enable IDM mode` | Enable IDM mode in SugarCRM |
| `List authentication settings` | Lists authentication settings in SugarCRM |
| `Get installed packages` | Gets installed packages in SugarCRM |
| `Get portal modules` | Gets portal modules in SugarCRM |
| `Get search index status` | Gets search index status in SugarCRM |
| `Get searchable fields` | Gets searchable fields in SugarCRM |
| `Get staged packages` | Gets staged packages in SugarCRM |
| `Reindex search` | Reindex search in SugarCRM |
| `Delete package file` | Deletes package file in SugarCRM |
| `Disable IDM mode` | Disable IDM mode in SugarCRM |
| `Enable IDM mode` | Enable IDM mode in SugarCRM |
| `List authentication settings` | Lists authentication settings in SugarCRM |
| `Get installed packages` | Gets installed packages in SugarCRM |
| `Get portal modules` | Gets portal modules in SugarCRM |
| `Get search index status` | Gets search index status in SugarCRM |
| `Get searchable fields` | Gets searchable fields in SugarCRM |
| `Get staged packages` | Gets staged packages in SugarCRM |
| `Reindex search` | Reindex search in SugarCRM |
