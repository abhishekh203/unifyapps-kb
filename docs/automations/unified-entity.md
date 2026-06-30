# Unified Entity

Source: https://www.unifyapps.com/docs/unify-automations/unified-entity
Section: automations

---

## Overview

Unified Entity by UnifyApps provides comprehensive entity and relationship management capabilities for your automation workflows. This enables you to create, manage, and query entities and their relationships using multiple query languages including SQL, Gremlin, and OpenCypher, making it essential for graph database operations, data modelling, and complex relationship management.

## Create Unified Entity

This action establishes new entities within the unified entity system, enabling the creation of structured data objects with configurable properties. Add the Unified Entity by UnifyApps node, select "`Create Unified Entity`" option and provide below mentioned inputs.

**Inputs:**

- **Time Series:** Set to true (enables time-series functionality for the entity, allowing temporal data tracking and historical analysis)
- **Tag IDs:** Set to ["`internal`"] (applies specified tags to the entity for categorization, filtering, and workflow organization purposes)

**Output:** Returns information about the created unified entity, including entity ID, configuration details, timestamp information, and metadata that can be used in subsequent workflow steps for relationship creation and data operations.

## Delete Unified Entity

This action removes entities from the system, supporting data cleanup and entity lifecycle management workflows. Add the Unified Entity by UnifyApps node, select "`Delete Unified Entity`" option and provide below mentioned inputs.

**Inputs:** No specific input fields are defined for this action. The target entity identification and deletion parameters are managed through workflow context.

**Output:** Returns confirmation of entity deletion, providing deletion status, timestamp, and any cascading relationship changes that occurred as a result of the entity removal.

## Create Entity Relationship

This action establishes connections between entities in the system, enabling the creation of complex data graphs and relationship networks. Add the Unified Entity by UnifyApps node, select "`Create Entity Relationship`" option and provide below mentioned inputs.

**Inputs:** No specific input fields are defined for this action. Relationship parameters including source entity, target entity, and relationship type are handled through workflow context.

**Output:** Returns information about the created relationship, including relationship ID, connection details, relationship type, and metadata that can be used for graph traversal and relationship querying operations.

## Find Entity Relationships

This action searches for and retrieves existing relationships between entities, enabling relationship discovery and graph analysis. Add the Unified Entity by UnifyApps node, select "`Find Entity Relationships`" option and provide below mentioned inputs.

**Inputs:** No specific input fields are defined for this action. Search criteria and relationship filters are managed through workflow parameters and query context.

**Output:** Returns a list of entity relationships matching the search criteria, including relationship details, connected entities, relationship types, and metadata that can be used for graph visualization and analysis workflows.

## Delete Entity Relationships

This action removes relationships between entities, supporting relationship lifecycle management and graph restructuring operations. Add the Unified Entity by UnifyApps node, select "`Delete Entity Relationships`" option and provide below mentioned inputs.

**Inputs:** No specific input fields are defined for this action. Target relationship identification and deletion scope are handled through workflow context and automation parameters.

**Output:** Returns confirmation of relationship deletion, providing deletion status, affected entities, and any cascading changes that occurred in the entity graph structure.

## Entity Engine

Entity Engine is a flexible feature in our platform that allows users to define and manage custom schemas, handle data storage, and perform lookup operations within workflows. It enables the creation of structured, reusable data models tailored to your specific business needs. By using Entity Engine, teams can centralize key information, streamline automation, and build more intelligent, data-driven workflows—reducing reliance on external systems and improving overall efficiency.

## Execute Gremlin Query

This action runs Gremlin graph traversal queries against the entity data, enabling complex graph pattern matching and traversal operations. Add the Unified Entity by UnifyApps node, select "`Execute Gremlin Query`" option and provide below mentioned inputs.

**Inputs:** No specific input fields are defined for this action. Gremlin query syntax and parameters are provided through workflow configuration and query context.

**Output:** Returns results from the executed Gremlin query, including matched entities, traversal paths, aggregated data, and graph metrics that can be used for complex relationship analysis and graph-based insights.

## Execute OpenCypher Query

This action runs OpenCypher queries for graph pattern matching and data retrieval, providing declarative graph querying capabilities. Add the Unified Entity by UnifyApps node, select "`Execute OpenCypher Query`" option and provide below mentioned inputs.

**Inputs:** No specific input fields are defined for this action. OpenCypher query syntax and pattern matching criteria are specified through workflow parameters.

**Output:** Returns results from the executed OpenCypher query, including pattern matches, entity collections, relationship data, and query statistics that enable sophisticated graph analytics and pattern discovery.

## Find by SQL

This action executes SQL queries against the unified entity system, providing familiar relational query capabilities for entity data. Add the Unified Entity by UnifyApps node, select "`Find by SQL`" option and provide below mentioned inputs.

**Inputs:** No specific input fields are defined for this action. SQL query syntax and table references are provided through workflow configuration and query parameters.

**Output:** Returns results from the executed SQL query, including selected data, aggregated metrics, filtered results, and query metadata that can be used for traditional relational data analysis and reporting workflows.

## Use Cases

**Graph Database Management:** Organizations can build and maintain complex data relationships using graph database technologies, enabling sophisticated data modeling and traversal operations. For example, a social network platform could use Create Unified Entity to establish user profiles, Create Entity Relationship to connect users as friends or followers, and Execute Gremlin Query to find mutual connections or recommend new connections based on graph proximity and relationship patterns.

**Entity Relationship Modeling:** Development teams can create and manage entity models with defined relationships, supporting complex data architectures and business logic implementations. A supply chain management system might use Create Unified Entity Model to define product, supplier, and warehouse templates, then Create Unified Entity to instantiate specific instances, Create Entity Relationship to model supply chains, and Find Entity Relationships to trace product origins or identify supply chain bottlenecks.

**Multi-Query Language Support:** Data analysts can leverage different query languages (SQL, Gremlin, OpenCypher) depending on their specific use cases and technical requirements. A financial analytics platform could use Find by SQL for traditional reporting and aggregations, Execute OpenCypher Query for fraud pattern detection across transaction networks, and Execute Gremlin Query for complex traversals to identify money laundering paths or unusual transaction patterns across multiple accounts and institutions.
