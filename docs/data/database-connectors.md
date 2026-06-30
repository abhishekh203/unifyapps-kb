# Database connectors

Source: https://www.unifyapps.com/docs/unify-data/database-connectors
Section: data

---

Database connectors in UnifyApps provide the foundation for building robust data integration solutions. These connectors enable your organization to extract data from various database systems, transform it according to your business requirements, and load it into your destination platforms.

## What Are Database Connectors?

Database connectors are pre-built integration components that establish secure, reliable connections between UnifyApps and your database systems. They handle the complexities of database communication protocols, authentication mechanisms, and data type conversions.

## Supported Database Systems

UnifyApps offers native connectivity to a comprehensive range of database platforms:

| **Database Connector** | **Description** | **Common Use Cases** |
|---|---|---|
| `PostgreSQL` | Open-source relational database | Application backends, analytics systems |
| `OracleDB Server` | Enterprise relational database | ERP systems, financial applications |
| `MySQL` | Open-source relational database | Web applications, content management |
| `Microsoft SQL Server` | Microsoft's enterprise database | Business applications, data warehousing |
| `MongoDB` | Document-oriented NoSQL database | Content repositories, real-time analytics |
| `Snowflake` | Cloud data warehouse | Analytics, reporting, data sharing |
| `ClickHouse` | Column-oriented OLAP database | High-performance analytics, real-time reporting |
| `Databricks` | Unified analytics platform | Data engineering, machine learning |
| `Amazon DynamoDB` | NoSQL database service | High-scale applications, serverless architectures |
| `Starrocks` | High-performance analytical database | Real-time analytics, complex queries |

## Managed Database Services

UnifyApps integrates seamlessly with major cloud-managed database platforms, providing enterprise-grade connectivity without infrastructure complexity.

## Supported Managed Services

| **Service** | **Provider** | **Description** |
|---|---|---|
| `Amazon RDS` | AWS | Easy-to-manage relational database service optimized for total cost of ownership[GCP DB: BigQuery, Spanner, Atlas, Alloy, Cloud SQL, Firebase](https://vastedge.com/gcp-databases) |
| `Google Cloud SQL` | Google Cloud | Fully managed MySQL, PostgreSQL, SQL Server |
| `Azure SQL Database` | Microsoft Azure | Intelligent, scalable database service built for the cloud[Amazon RDS for SQL Server Supports Minor Versions in November 2024 - AWS](https://aws.amazon.com/about-aws/whats-new/2024/11/amazon-rds-sql-server-versions-november-2024/) |
| `Oracle Database@Azure` | Oracle + Microsoft | Enterprise Oracle databases in Azure infrastructure |

**Key Integration Benefits:**

- **Simplified Setup**: Native authentication and network connectivity
- **Auto-Scaling**: Leverage cloud-native scaling capabilities
- **Enhanced Security**: Built-in encryption and compliance features
- **Cost Efficiency**: Pay-as-you-scale with no infrastructure overhead

These managed services enable organizations to focus on data integration while the cloud provider handles database operations, maintenance, and scaling.

## Key Features of Database Connectors

All UnifyApps database connectors share common capabilities that enable efficient and secure data integration:

1. **Flexible Authentication Options**
  - Direct database authentication
  - SSH tunneling for secure connectivity
  - SSL/TLS encryption support
  - Certificate-based authentication
2. **Timezone Intelligence**
  - Server timezone configuration
  - Automatic datetime normalization
  - Consistent UTC conversion
3. **Comprehensive Data Type Support**
  - Native handling of database-specific data types
  - Automatic type conversion and mapping
  - Support for complex types (JSON, arrays, etc.)
4. **Multiple Ingestion Modes**
  - Historical and Live: Full load plus ongoing changes
  - Live Only: New data from deployment onward
  - Historical Only: One-time full load
5. **Change Data Capture (CDC)**
  - Real-time change tracking
  - Minimal impact on source systems
  - Complete CRUD operation visibility

## Business Benefits

Database connectors deliver significant value to your organization by:

- **Reducing Development Time**: Eliminating the need to build and maintain custom database integrations
- **Improving Data Currency**: Enabling real-time or near-real-time data synchronization
- **Enhancing Security**: Providing secure connectivity options for sensitive data
- **Supporting Compliance**: Maintaining comprehensive audit logs of data movement
- **Enabling Analytics**: Making data available across your organization for insights
