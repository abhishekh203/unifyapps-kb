# Decision Table

Source: https://www.unifyapps.com/docs/platform-tools/decision-table
Section: platform-tools

---

## Overview

A **Decision Table** is a powerful **mapping tool** within our platform that allows you to define rules for determining output values based on specific input conditions. It functions as a structured lookup mechanism where users can define condition variables with specific operators (like "equals," "starts with," etc.) and corresponding result variables.Decision Tables help you implement complex business logic without coding by creating clear relationships between input conditions and desired outcomes.

## Configuring a decision table

1. **Access the Decision Table**
  - Navigate to the platform tools>Decision tables
  - Click on the new table button to create a new decision table.

    ![Frame 427319349 (1).png](_img/ce90f2a0f2b83f8a.webp)

2. **Define condition,result variables**
  - Add Condition variables that will determine your results.
  - For each condition variable, specify Field name,Data type (text, number, date, etc.), Condition operator (equals, starts with, contains, greater than, etc.)
  - Add the output fields your table will return
  - Specify the data type for each result variable

    ![Frame 427319350 (3).png](_img/97bece468c7e09cc.webp)

3. **Add records in decision table**
  - We can either add records in the decision table by manually creating them from table layout, or use one of the actions defined below to create, update and delete records.

## Actions in a decision table

1. **Create a Decision Table:**
  - Provide a name and description for the decision table.
  - Add Condition variables that will determine your results.
  - For each condition variable, specify Field name,Data type (text, number, date, etc.), Condition operator (equals, starts with, contains, greater than, etc.)
  - Add the output fields your table will return
  - Specify the data type for each result variable

    ![Frame 427319351 (1).png](_img/dc7721ce15f8829d.webp)

2. **Add row to existing decision table:**
  - The action allows users to create a new record in an existing decision table.
  - Users can provide the value of each condition variable along with the operator to match when the decision table is executed.
  - For each defined condition variable, users should define the relevant output as the result variable.

    ![Frame 427319352 (2).png](_img/c8b475cfd779538d.webp)

3. **Delete rows from existing decision table:**
  - The action allows users to delete a record from an existing decision table.
  - Users can provide the filter conditions to match the records to be deleted.
  - Using this action will delete the matched record from the decision table.
  - Users are allowed to filter the records via condition variables as well as result variables.

    ![Frame 427319353 (2).png](_img/e8b751f76fcc05c5.webp)

4. **Update rows in an existing decision table:**
  - The action allows the user to update an existing record in a decision table.
  - In order to update a record users should provide filter conditions to identify the record to be updated.
  - The filter conditions can be defined on the basis of existing condition variables or the result variables.
  - Finally users should provide the updated value of the condition and result variables which will override the existing value for the filtered record.

    ![Frame 427319354 (2).png](_img/3b323dba2a4a5b30.webp)

5. **Execute a custom decision table**
  - Within actions in unify apps search for a decision table by unify apps, an action to execute a decision table is present.

    ![Frame 427319355 (1).png](_img/391b841786b1541e.webp)

  - Choose the decision table you want to execute from the available dropdown, choose from one of the available response types:
    - **Final matched result** : Based on the inputs passed corresponding to condition variables defined in your decision table, this action returns the final matched result from the records present in the decision table
    - **All matched result :** Based on the inputs passed corresponding to condition variables defined in your decision table, this action returns all the matched result from the records present in the decision table
    - **First matched result :** Based on the inputs passed corresponding to condition variables defined in your decision table, this action returns the first matched result from the records present in the decision table

      ![Frame 427319356 (2).png](_img/debdb8efdf1dee9a.webp)
