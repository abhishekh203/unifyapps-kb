# Workflow debugger

Source: https://www.unifyapps.com/docs/unify-automations/workflow-debugger
Section: automations

---

## Overview

**Breakpoints** are intentional pause points in a program’s execution that let you stop the code while it’s running so you can inspect what’s going on under the hood.

They’re most commonly used in debugging.

Breakpoints help you:

- Find bugs faster than printing logs everywhere.
- Understand program flow, especially in complex logic.
- Debug edge cases that only happen in certain conditions.

![image14.png](_img/5bde855742991e0b.webp)

## Actions in breakpoints

- **Continue**: This action moves the flow to the next breakpoint while executing the immediate nodes.
- **Step over**: This action executes the current node and moves to the following node.
- **Step into:** This action enables running of the child automation first, and then the parent automation is executed (used in case of callable automation).
- **Stop:** This action stops the workflow and the remaining nodes go into the disabled state.

## Feature

1. Breakpoints can simply be ***ADDED*** or ***REMOVED*** by hovering over the breakpoint icon.

![image16.png](_img/ef9c43dad10083d6.webp)

2. The ***Debug icon*** appears or disappears with the breakpoints.

![image12.png](_img/bb1e3ab5c96dff13.webp)

![image7.png](_img/accaf11989b1067b.webp)

3. Clicking the RUN Button enables the ***STEP OVER****,* ***STEP INTO****,* ***CONTINUE*** actions.

![image2.png](_img/dcdba060c9eb32e1.webp)

4. Clicking *CONTINUE* after a breakpoint moves execution to the next breakpoint and executes immediate nodes.

![image4.png](_img/3c6841043fd6f01f.webp)

![image10.png](_img/cfa70f9c17ae3c6e.webp)

5. After adding a new breakpoint and running the test, the previously added breakpoints reappear with clicking on the *NEW TEST.*

![image11.png](_img/8229c262c3983177.webp)

6. The test status is shown *“IN PROGRESS”* after adding the breakpoints and running the tests.

![image15.png](_img/34202677cc71bd31.webp)

7. When the new test is run, the test parameters are asked in the form.

![image9.png](_img/31c8d8c8e1670b25.webp)

8. The breakpoints and the debug icon are not visible after the successful execution of the test and when clicking the *Repeat Test.*

![image1.png](_img/40994f962a6d8e93.webp)

9. When Step over or Continue is clicked, “*This step is still processing”* message is displayed.

![image17.png](_img/917d28765e240aee.webp)

10. When callable automation is used, STEP INTO executes the child automation while the parent automation displays the loading indicator.

![image13.png](_img/b4258690501faaad.webp)

![image9.png](_img/370144d6395cf2bd.webp)

The child automation can be viewed and run in a new window. By clicking the CONTINUE DEBUGGING button, we can view the child automation.

![image6.png](_img/9afda54c5908fbbe.webp)

![image5.png](_img/a917f808d4cea5a9.webp)

11. When the *STOP* button is clicked, the workflow is cancelled and the nodes go into the disabled state. The “CANCELLED” text appears in the history.

![image19.png](_img/24bc7ba143ffd867.webp)

![image3.png](_img/a2c6481d2a2a0fd7.webp)

12. When the execution is successful, the *“SUCCESSFUL”* message is displayed in the history.

![image7.png](_img/accaf11989b1067b.webp)

![Screen Recording 2026-02-27 at 12.58.47 PM.mov](https://assets.contentstack.io/v3/assets/blt55a41789e979ba65/bltae5f164882c571d2/69a32be2c10aada75dc82f95/Screen_Recording_2026-02-27_at_12.58.47_PM.mov)

## Use Cases

**Finding bugs**

- Stop execution where the output goes wrong
- Inspect variables to see where values change unexpectedly
- Catch off-by-one errors, null values, or incorrect logic.

**Understanding code behaviour**

- Learn how unfamiliar or legacy code works
- Trace execution flow step by step
- See which functions are actually called (vs. which you *think* are)

**Debugging loops and iterations**

- Pause inside loops to:
- Track iteration counts
- Inspect how variables evolve
- Detect infinite or skipped loops

**Verifying function calls and parameters**

- Check whether a function is called
- Confirm arguments passed are correct
- Validate return values

##
