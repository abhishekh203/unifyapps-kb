# LlamaParse Integration

Source: https://www.unifyapps.com/docs/unify-integrations/llamaparse
Section: integrations

---

Using LlamaParse enables you to extract, structure, and transform data from documents such as PDFs and images. It provides intelligent document parsing capabilities including text extraction, OCR processing, layout-aware parsing, and structured JSON output generation. LlamaParse allows you to upload files, monitor parsing jobs, retrieve structured results, and manage document processing workflows with high performance and reliability. Integrating your application with LlamaParse enables secure document processing, automated data extraction, and seamless integration into downstream systems and analytics platforms.

### Authentication

Before you begin, make sure you have the following information:

`Connection Name`: This is a user-defined name for your Connection to the API. Choose a descriptive name that will help you easily recognize the connection later.

`Base URL`: The base URL of the LlamaParse API (for example: https://api.llamaparse.com).

`Authentication Type`: API Key Authentication.

`API Key`: Enter your LlamaParse API Key for authentication.

`Connection`: Choose the method of connection to the LlamaParse API.

`Direct`: Connecting directly to the LlamaParse API without any intermediary. It's the simplest and most common method of connecting.

`Proxy`: Connect via an HTTP proxy, which requires additional configuration including Proxy Host and Port.

`SSL Configuration`: SSL is enabled by default for secure data transfer. You can configure certificates, trust settings, and host verification as needed.

### ACTIONS **:**

| **Action Name** | **Description** |
|---|---|
| `Upload File` | Uploads a document (PDF or image) for parsing and creates a parsing job. |
| `Check Status of Parsing Job` | Checks the current status of a submitted parsing job. |
| `Get Job Details` | Retrieves metadata and configuration details of a specific parsing job. |
| `Get Job Result` | Fetches the structured parsed output (JSON) of a completed job. |
| `Get Image Result` | Retrieves parsed image or OCR-specific results. |
| `On New Parsing Job Polling` | Polls for newly created or completed parsing jobs. |
