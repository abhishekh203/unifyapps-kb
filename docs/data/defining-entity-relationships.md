# Defining Entity Relationships

Source: https://www.unifyapps.com/docs/unify-data/defining-entity-relationships
Section: data

---

## **Overview**

Defining an entity relationship is the process of structurally linking two separate data objects to enable cross-entity intelligence.

By creating these definitions, you move beyond simple data storage to creating a "Knowledge Graph," where the UnifyApps platform understands exactly how a record in one table (like a Customer) relates to records in another table (like Orders or Support Tickets).

This configuration is performed via the New Relationship modal, which provides a visual interface for mapping keys and defining cardinality.

## **The Configuration Process**

To establish a new link, navigate to the Relationships tab and click the + Add Relationship button. This opens the configuration window, which is divided into three logical steps:

1. **Identity** Relationship Name: Give the connection a unique, descriptive identifier (e.g., Customer_Orders or Parent_Child_Account). This name is used internally by the system for graph traversals and API queries.
2. **Source Configuration** The "Source" represents the starting point or the "Parent" in the relationship hierarchy.
- **Source Entity:** Select the entity that initiates the relationship (e.g., Entity 2 ).
- **Cardinality:** Choose whether a single record in this source entity relates to **One** or **Many** records in the target.
- **Primary Key:** Select the unique identifier field from the source entity (e.g., CUSTOMER_ID ) that will act as the anchor for this connection.
1. **Target Configuration** The "Target" represents the destination or the "Child" entity that connects back to the source.
- **Target Entity:** Select the related entity to complete the relationship (e.g., Entity 1 ).
- **Cardinality:** Define the volume of the relationship on this side. Selecting **Many** here while the source is **One** creates a standard "One-to-Many" relationship.
- **Foreign Key:** Select the field in the target entity (e.g., accountUuid ) that contains the matching value to the source's Primary Key.

## **Understanding Cardinality**

The Cardinality controls in the modal allow you to define complex logic simply by toggling One or Many on either side of the equation:

- **One-to-One (1:1):** Select "One" for Source and "One" for Target. (Example: One Employee has one Social Security Number ).
- **One-to-Many (1:N):** Select "One" for Source and "Many" for Target. (Example: One Customer places Many Orders).
- **Many-to-Many (N:N):** Select "Many" for Source and "Many" for Target. (Example: Many Students attend Many Classes).

## **Visual Verification**

Once created, the relationship is immediately visualized in the Graph View.

The connector line between the entities will reflect your configuration, using specific markers (like 1 or *) to denote the cardinality you selected, allowing for instant architectural validation.
