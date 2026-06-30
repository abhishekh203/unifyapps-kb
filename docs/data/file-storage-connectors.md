# File Storage Connectors

Source: https://www.unifyapps.com/docs/unify-data/file-storage-connectors
Section: data

---

File storage connectors in UnifyApps provide essential capabilities for integrating with diverse file repositories across your infrastructure. These connectors enable your organization to efficiently access, process, and distribute file-based data whether stored in cloud services, on-premises systems, or hybrid environments.

## What Are File Storage Connectors?

File storage connectors are pre-built integration components that establish secure, reliable connections between UnifyApps and your file storage systems. They handle the complexities of file protocols, authentication mechanisms, directory structures, and file format conversions.

## Connection Methods

UnifyApps file storage connectors support multiple authentication methods to ensure secure and flexible connectivity:

1. **API Key/Token Authentication**
  - Service account credentials for cloud storage services
  - Programmatic access with limited permissions
  - Commonly used with S3, Google Cloud Storage, Azure Blob Storage
2. **Username/Password Authentication**
  - Traditional credentials for FTP, SFTP systems
  - Directory and access restrictions
3. **Key Pair Authentication**
  - Public/private key cryptography for secure access
  - Enhanced security for SFTP connections
  - Support for various key formats and passphrases
4. **IAM Role-Based Authentication**
  - Especially for AWS S3 and similar cloud services
  - Temporary, automatically rotated credentials
  - Granular permission controls

## Schema Discovery

UnifyApps automatically scans source files to generate a tabular schema structure, providing:

- Field names detection
- Automatic handling of headers
- Schema consistency validation across files

## Supported File Storage Connectors

UnifyApps offers native connectivity to file storage systems visible in the platform interface:

| **File Storage Connector** | **Description** | **Common Use Cases** |
|---|---|---|
| `Amazon S3` | Cloud object storage | Data lakes, archive storage, log files |
| `SFTP` | Secure File Transfer Protocol | Secure file exchange, EDI transfers |

## Destination Support

UnifyApps supports writing data to file storage systems with these specific formats:

- Destinations: CSV, JSONL, Parquet

The following systems are supported as destinations:

- Amazon S3
- SFTP

## Key Features of File Storage Connectors

All UnifyApps file storage connectors share common capabilities that enable efficient and secure data integration:

1. **Flexible File Format Support**
  - Source formats: CSV, JSON, JSONL, XML, XLS, XLSX, TSV
  - Destination formats: CSV, JSONL, Parquet
  - Automatic schema generation from file scanning
  - Custom delimiters and quote characters
  - Conversion between formats
2. **Directory Organization**
  - Hierarchical folder navigation
  - Wildcard pattern matching
  - Date-based folder structures
  - Dynamic path resolution
3. **File Operation Modes**
  - Read and process operations
  - Write and append capabilities
  - File movement and archiving
4. **Performance Optimizations**
  - Parallel file processing
  - Chunked file handling for large files
  - Streaming capabilities
  - Data buffer management
5. **Security Controls**
  - Encryption in transit
  - Integration with key management systems
  - Secure credential storage
  - Audit logging of file operations

## Business Benefits

File storage connectors deliver significant value to your organization by:

- **Simplifying File-Based Integration**: Eliminating custom scripts and manual file handling
- **Improving Data Accessibility**: Making file-based data available for analytical and operational processes
- **Enhancing Security**: Providing secure, audited access to file repositories
- **Reducing Operational Overhead**: Automating file transfer, processing, and monitoring
- **Supporting Hybrid Architectures**: Bridging on-premises and cloud storage environments
