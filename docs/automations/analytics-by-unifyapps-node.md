# Analytics by UnifyApps

Source: https://www.unifyapps.com/docs/unify-automations/analytics-by-unifyapps-node
Section: automations

---

## Overview

**Analytics by UnifyApps** enables comprehensive data analysis and reporting capabilities. This means you can aggregate metadata, run SQL queries, and export reports in various formats (CSV, XLS or XLSX), making it perfect for generating insights, performance monitoring, and data-driven decision-making.

![Frame 427319210 (17).png](_img/4a42bd67fa790f61.webp)

## Use Cases

1. **Customer Segmentation Analysis** Run an **Analytics Query** to group customers by location or purchase history using projections like count or distinct count. This can help identify key demographics and tailor marketing efforts accordingly.
2. **Multi-Source Data Integration** Aggregate data from various sources (e.g., user activity, transaction logs, product reviews) using SQL queries by using **Execute Analytics SQL Query**. Join tables across multiple platforms to identify patterns and correlations, such as understanding how customer behavior correlates with product sales over time.
3. **Automated Quarterly Budget Reports** A finance team automates the generation of quarterly budget reports using the **Export Reports** action. By setting time ranges and defining projections, they export summarized financial data (like revenue and expenses) in XLSX format. The reports are then shared with stakeholders for review, ensuring timely, accurate data for decision-making, and saving manual report-generation time.
4. **Retrieving Metadata for Specific Fields**A user working within the Platform group wants to gather detailed metadata for fields such as Customer_Name, Customer_Age, and Customer_Location. They utilize the **Aggregate Metadata** action and specify these fields in the Add ID section.

## Aggregate Metadata

![Frame 427319209 (23).png](_img/c58a8a4d7ae76d74.webp)

The **Aggregate Metadata** action in Analytics by UnifyApps enables users to retrieve and explore detailed metadata for data fields within a specific object. It provides crucial insights into field properties such as whether they are sortable, filterable, searchable, or updatable, helping users better understand their dataset structure and enabling more efficient data handling.

**Input Fields:**

![Frame 427319213 (15).png](_img/3c9c2e96771e0523.webp)

- `Group`**:** Select between *Storage* or *Platform* to determine the data context.
- `Base Report`**:** Choose the object to query for metadata.
- `Add ID`**:** Specify the field name for metadata extraction.
- `Query`**:** Enter a partial field name to retrieve related metadata. For example, entering "Cus" returns fields like *Customers_Profile*.
- `Page`**:** Configure pagination with Offset and Limit.
- `Sortable`**:** Enable if you want to retrieve fields that are sortable.
- `Filterable`**:** Enable if you want to retrieve fields that are filterable.

**Output:**

The action returns detailed metadata for each field, including:

- **Aggregation Field Type**
- **Display Name**
- **Entity Type**
- **Field Type**
- **Sortable, Filterable and Searchable**
- **Updatable**
- **Name Field**

This action simplifies data exploration, particularly for large datasets, by allowing users to understand field properties quickly without needing to manually search through the data.

## Analytics Query

![Frame 427319212 (20).png](_img/ae97193dfe1544c8.webp)

The **Analytics Query** action in Analytics by UnifyApps enables users to fetch, process, and analyze data from a selected base report. This action provides powerful querying capabilities, including grouping, filtering, and projecting data, along with aggregation and percentage-based calculations.

**Input Requirements:**

1. `Select Group`**:** Choose between Platform or Storage to define the data grouping.
2. `Select Base Report`**:** Choose the base report object.
3. **Select Projections:**
  - Choose fields and apply aggregation functions like Count, Sum, Min/Max, Percentage Contribution, or even custom operations.
  - Assign aliases to projections for clarity.
  - Optionally, calculate percentage changes.
4. `Select Additional Projections`**:** Add supplementary projections with similar options for fields, aggregation, and percentage change inclusion.

  ![Frame 4748 1.png](_img/701ed95aba25c2e1.webp)

5. `Time Range`**:**
  - Define a time field for the query.
  - Specify start and end times, including previous periods for comparison.

    ![Frame 427319211 (19).png](_img/ed7b8d2422642929.webp)

6. `Filter`**:**
  - Create conditions using fields and values to filter data efficiently.
  - Add multiple conditions or condition groups for complex queries.
7. `Search Object`**:**
  - Specify fields and their values to narrow down search results further.
8. `Pagination`**:**
  - Use Offset and Limit to manage the number of records retrieved.
9. `Sorting`**:**
  - Add fields to sort the results by specific attributes.
10. `Include Total Count`**:**
  - Set this option to true for retrieving the total count of records matching the query.

This action allows robust customization to extract insights effectively from large datasets while offering precision in data manipulation.

## Node Level Reporting

1. **Id** : Unique identifier for the node execution instance.

![node_2.jpg](_img/f4a2dc4a4547220d.webp)

2. **Execution Instance Id :** Identifier for the specific execution instance of the workflow.

![node_3.jpg](_img/656baf92039a946f.webp)

3. **Root Execution Instance Id :** Identifier for the root execution instance of the workflow, useful for tracking nested executions.

![node_4.jpg](_img/8b8a1647be3ba80b.webp)

4. **Parent Execution Instance Id :** Identifier for the parent execution instance, if applicable.

![node_5.jpg](_img/aa4ee91223946fb6.webp)

5. **Trigger Instance Id :** Identifier for the trigger instance that initiated the workflow execution.

![node_6.jpg](_img/fbaff03ab7efa5b6.webp)

6. **Workflow :** Name or identifier of the workflow being executed.

![node_7.2.jpg](_img/9b46adc739847945.webp)

7. **Workflow Version :** Version of the workflow being executed.

![node_8.jpg](_img/a517a75223059fef.webp)

8. **Deployed Workflow :** Identifier for the deployed version of the workflow.

![node_9.jpg](_img/ac61ff216866fce6.webp)

9. **Concurrent Execution :** Indicates whether the node execution is part of a concurrent execution path.

![node_11.jpg](_img/9ea078cd1175bc02.webp)

10. **Current Node :** Name or identifier of the current node being executed.

![node_7.jpg](_img/8dd5974fabe56b66.webp)

11. **Current Node App Name :** Name of the application associated with the current node.

![node_13.jpg](_img/dd2b04cad7befc91.webp)

12. **Current Node Resource Name :** Name of the resource associated with the current node.

![node_14.jpg](_img/11234ffa87df581c.webp)

13. **Current Node Connection Id :** Identifier for the connection being executed for the current node.

![node_16.jpg](_img/a47a1cdffd0d56ce.webp)

14. **Next Node :** Name or identifier of the next node to be executed.

![node_17.jpg](_img/687373a75d0ee0eb.webp)

15. **Previous Node :** Name or identifier of the previous node that was executed.

![node_18.jpg](_img/51c55b86b9dd5566.webp)

16. **Entry Time :** Timestamp when the node execution started.

![node_19.jpg](_img/25e2861043cfeca7.webp)

17. **Resume Time :** Timestamp when the node execution resumed after being paused or waiting.

![node_20.jpg](_img/2ff257dc3ca652b9.webp)

18. **Exit Time :** Timestamp when the node execution completed or exited.

![node_21.jpg](_img/558821e91c327f54.webp)

19. **Status :** Current status of the node execution (e.g., RUNNING, COMPLETED, FAILED).

![node_22.jpg](_img/1a4f39877a6a8489.webp)

20. **Execution Time Hour of Day :** Hour of the day when the node execution started, useful for time-based analysis.

![node_24.jpg](_img/f0992f1b4db69dd7.webp)

21. **Execution Time Day of Week :** Day of the week when the node execution started, useful for identifying patterns based on days.

![node_25.jpg](_img/2170cd7a1b7ee67d.webp)

22. **Wait Time :** Total time the node execution spent waiting (e.g., for resources, external calls).

![node_26.jpg](_img/71574364836caf93.webp)

23. **Retry Count :** Number of times the node execution was retried due to failures or errors.

![node_27.jpg](_img/246ba768fd162212.webp)

24. **Is Child Execution Instance :** Indicates whether the node execution instance is a child execution of another instance.

![node_29.jpg](_img/acdf99a7a0f18bad.webp)

25. **Successful Runs Count :** Count of successful node executions, useful for performance and reliability analysis.

![node_32.jpg](_img/535fe1eac6143913.webp)

26. **Failed Runs Count :** Count of failed node executions, useful for identifying issues and improving workflow design.

![node_33.jpg](_img/1409b908a1f64e85.webp)

27. **Total Runs Count :** Total count of node executions, useful for overall execution analysis and reporting.

![node_34.jpg](_img/d54d86ff58efe744.webp)

28. **Application Id :** Identifier for the application associated with the node execution, if applicable.

![node_36.jpg](_img/4802644ce5b565cb.webp)

29. **Skipped :** Indicates whether the node execution was skipped, which can occur due to conditional logic in the workflow.

![node_37.jpg](_img/9206f0b0c7d61a7c.webp)

30. **Cache Hit :** Indicates whether the node execution resulted in a cache hit, which can impact performance analysis.

![node_38.jpg](_img/a0d2c40152b86793.webp)

31. **Input :** JSON representation of the input data for the node execution, used for debugging and analysis (PII).

![node_39.jpg](_img/a86953734f7a966c.webp)

32. **Output :** JSON representation of the output data from the node execution, used for debugging and analysis (PII).

![node_40.jpg](_img/adb50a0159d84262.webp)

33. **State :** JSON representation of the state of the node execution, providing insights into execution context.

![node_41.jpg](_img/2a4d4dfe13422e91.webp)

34. **Node Execution Count :** Total count of node executions for a specific node, useful for identifying frequently executed nodes.

![node_43.jpg](_img/f5ddc0954ceb541e.webp)

35. **Debugged :** Indicates whether the node execution was debugged.

![node_45.jpg](_img/143481af5af7a019.webp)

## Execute Analytics SQL Query

![Frame 427319216 (12).png](_img/758d71b4a219f12a.webp)

The **Execute Analytics SQL Query** action in Analytics by UnifyApps allows users to directly execute custom SQL queries against their data, providing granular control and flexibility for advanced analysis. This action supports dynamic schema definition and integration with custom workflows.

**Input Fields Requirements:**

1. `SQL Query`**:**
  - Enter the SQL query to execute.
  - Prefix every table name with ENTITY_ and every column name with _pr_ to comply with the query format. Example: Select _pr_columnName from ENTITY_TableName
2. `Select Group`**:**
  - Choose between Storage or Platform to define the data context.
3. `Define Result Schema`**:**
  - Specify the structure of each row in the query response. This is essential for defining alias column names and ensuring accurate mapping.
    - Add Field: Manually add fields by specifying:
      - Key: Identifier for the field.
      - Display Label: Displayed label for the field.
      - Type: Data type (e.g., string, number).
      - Optional: Mark the field as optional.
      - Default Value: Set a fallback value.
      - Nest Under: Place the field within a hierarchical structure, if needed.
    - Use Code Snippet: Define the schema using a JSON, XML or XSD snippet.
      - Create a new snippet or select an existing one from saved options.
    - Map from Step: Map the schema directly from another automation step.

This action is ideal for advanced users who need to execute SQL queries for custom reporting, filtering, or complex data transformations while dynamically shaping the output schema.

## Export Reports

![Frame 427319217 (10).png](_img/171f5b381ff094bf.webp)

The **Export Reports** action provides users with the ability to generate and export customized reports based on specified parameters. This action enables users to select data projections, filters, sorting options, and define the desired time range, along with the option to include the total record count. Users can also choose between different file formats (CSV, XLS, or XLSX) for the exported report, ensuring flexibility and compatibility with various tools. The generated report is available for download via a preview link.

**Input Fields:**

![Frame 427319214 (17).png](_img/21cc39519b038b7e.webp)

1. `File Name`**:** Prefix for the exported file name.
2. `Select Group`**:** Choose between Storage or Platform for the data context.
3. `Select Base Report`: Choose the base report object.
4. `Select Projections`**:** Choose fields to aggregate and customize based on required operations like sum, count, etc.
5. `Time Range`**:** Define the start and end time for the data included.
6. `Filter`**:** Add conditions for filtering data.
7. `Search Object`**:** Specify fields and their values to filter results.

  ![Frame 427319215 (15).png](_img/fb352e727b94fad2.webp)

8. `Page`**:** Set offset and limit for paginated data.
9. `Sorts`**:** Define how the data should be sorted.
10. `Include Total Count`**:** Toggle to include the total count of records.
11. `File Format`**:** Choose between CSV, XLS, or XLSX.

This action is ideal for users who need to export formatted reports, whether for internal analysis, sharing, or integration with other systems.

## Converts Filter to SQL Condition

The **Converts Filter to SQL Condition** action in **Analytics by UnifyApps** enables users to transform visual filter inputs into a SQL-compatible condition string. This allows for seamless integration of UI-based filter logic into backend SQL queries, ensuring data consistency and query efficiency.

![Frame 427319318 (2).png](_img/49f21018ee7bc42e.webp)

**Input Fields:**

- `Group`: Choose between Storage or Platform for the data context.
- `Base Report`:Choose the base report object. **Filter**: Set conditions to define what subset of data you want to filter. You can specify:
  - **Where**: Enter the field name you want to apply the condition to.
  - **Condition**: Define condition operators such as Equals to, Start with, In etc.
  - Enter values for each condition.
  - Additional options include:
    - **Add Condition**: Add a new condition within the same group.
    - **Add Condition Group**: Create logical groups using AND/OR conditions.
    - **Add Filter**: Combine multiple filters for complex logic.

**Output:** The action returns a SQL-compatible condition string in JSON format.

![Frame 427319319 (1).png](_img/cb01176d5dcaa086.webp)

The output condition string can be directly appended to SQL queries, such as when using the **Execute Analytics SQL Query** action. This enables users to dynamically inject filter conditions into custom queries, enhancing automation, flexibility, and scalability of data-driven operations.

## Export SQL Query Result

The Export SQL Query Result action in **Analytics by UnifyApps** allows users to execute a custom SQL query on a selected group (Storage or Platform) and export the result as a downloadable file. This is useful for automating data extraction, reporting, and sharing datasets across teams or systems.

**Input Fields:**

- `File Name`**:** Provide a prefix for the exported file name. The full file name will include this prefix along with a timestamp and appropriate file extension.
- `SQL Query`**:** Write your SQL query to retrieve the desired data. You can query any available object or entity.

  ![Frame 427319320 (1).png](_img/1bf93d3dffc3a92f.webp)

- `Select Group`**:** Choose between Storage or Platform for the data context.
- `Define the Result Schema` **(Optional):** Define the expected structure of each row in the query result. This helps in downstream automation where you may want to access specific fields. You can use:
  - **Add Field** to manually specify field names
  - **Use Code Snippet** to write custom parsing logic
  - **Map from Step** to auto-map schema from previous step

**Output:** On successful execution, the action returns the following details:

- **File Type:** The format of the exported file
- **File Name:** The system-generated full filename
- **Source:** Path within cloud storage
- **Source Type:** Indicates storage type
- **Link:** A secure URL to download the exported file
- **ua:type:** Always returns "FILE" to indicate file object

## Execute Analytics SQL Update Query

The **Execute Analytics SQL Update Query** action in **Analytics by UnifyApps** is used to **modify existing records** in a dataset using SQL UPDATE statements. This action is ideal for automation scenarios where dynamic updates to datasets are required based on business logic.

**Input Fields:**

![Frame 427319322 (1).png](_img/24b88bc88f28dc30.webp)

- `SQL Query`**:** Provide a valid UPDATE SQL statement to modify data in the selected group
- `Select Group`**:** Choose between Storage or Platform for the data context.

**Output:**

![Frame 427319323 (1).png](_img/9814209af8c79b84.webp)

On successful execution, the action returns the count of records that were updated.
