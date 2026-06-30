# Use Operators

Source: https://www.unifyapps.com/docs/unify-automations/use-operators
Section: automations

---

## Introduction

Operators like condition, branch, loop, and delay are required to implement logic and control flow within automations. These tools help set up complex scenarios.

Here's an overview of key operators and their applications:

### Condition

- **Definition:** A decision-making operator that executes different actions based on whether a specified condition is true or false.
- **Usage:** Allows automations to make choices, such as differentiating between high and low priority tickets in a support system.
- **Example:** If a new email arrives with "URGENT" in the subject, flag it for immediate attention.

### Branch

- **Definition:** An extension of conditional logic allowing multiple execution paths based on different possible values or states.
- **Usage:** Enables more complex decision trees within automations, handling various scenarios simultaneously.
- **Example:** Routing customer inquiries to different departments based on the nature of the request (billing, technical support, sales).

### For Loop

- **Definition:** A control flow statement that allows code to be executed repeatedly for a predetermined number of iterations.
- **Usage:** Useful for processing lists or performing actions a specific number of times.
- **Example:** Sending a follow-up email to each attendee on a list after an event.

### While Loop

- **Definition:** A control flow statement that repeats a block of code as long as a specified condition remains true.
- **Usage:** Ideal for situations where the number of iterations is not known in advance.
- **Example:** Continuously monitoring a system's status until a specific condition is met.

### Continue in Loop

- **Definition:** A statement used within loops to skip the rest of the current iteration and move to the next one.
- **Usage:** Allows for skipping certain items or conditions within a loop without terminating the entire loop.
- **Example:** In a data processing loop, skip entries that don't meet specific criteria without stopping the overall process.

### Break in Loop

- **Definition:** A statement that exits a loop prematurely when a specific condition is met.
- **Usage:** Useful for terminating a loop when a specific state or condition is achieved, improving efficiency.
- **Example:** Stopping a search loop once the desired item is found rather than continuing through the entire dataset.

### Delay

- **Definition:** An operator that pauses the execution of an automation for a specified period.
- **Usage:** Introduces timed intervals between actions, allowing for paced execution or synchronisation with external systems.
- **Example:** Waiting 5 minutes after sending an email before initiating a follow-up action.

By leveraging these operators, automation designers can create sophisticated automations that handle complex scenarios, make decisions based on varied inputs, process data efficiently, and coordinate timing-sensitive operations.
