# Automation Interfaces

Source: https://www.unifyapps.com/docs/unify-automations/automation-interfaces
Section: automations

---

## Introduction

In callable automation, we have to **configure** the schema for each callable automation and we might need to define the **same schema** for **multiple callable** automation.

To **reduce manual effort** and ensure **scalability**, define a schema once using an automation interface and reuse it across automations.

![Frame 427319209 (21).png](_img/7c3d477a44de0cdc.webp)

![Automation Interface .mp4](https://assets.contentstack.io/v3/assets/blt55a41789e979ba65/blta6fc4b7416c61cc6/691dc3596cdace512e7b258b/Automation_Interface_.mp4)

## Create Automation Interface

- To **create** a New Automation Interface go to the automation interface in the left navigation pane.
- Click on create “`New Automation Interface`” button to create a new Interface
- Provide the **name** and **description** for the Automation interface.
- You can create **setup** and **result schema** by uploading JSON schema or manually configuring the setup and result schema fields.
- The `Setup schema` of the interface will serve as the setup schema for callable automation.
- The `Result schema` will serve as the result schema for the callable automation.

![Frame 427319210 (14).png](_img/86aad14f8ea953b9.webp)

## Use Automation Interface as Trigger in Automation

- Set up **trigger** as a callable interface.
- Select the **interface** in the Setup tab which you want to use, from the available interfaces in the dropdown.
- Once the interface is selected, the **setup** and **result** **schema** of the interface are populated in the automation trigger.
- The `Setup schema` of the interface defines the parameters the parent automation will pass to the child.
- The `Output schema` of the interface defines the parameters that will be returned to the parent automation.

![Frame 427319211 (15).png](_img/fe910dc809650091.webp)

## Call an Automation Interface

Users can call an automation interface by using the call an interface action within callable Node.

- Users can select which callable Interface you want to refer.

  ![Frame 427319212 (13).png](_img/af23bc59370d7cfe.webp)

- Now users have the capability to call different automation using the same interface based on conditional criteria as shown in the example below.
- Using this you can call **multiple different automations** using same interfaces which helps in achieving scalability.
- You can also select one **Default/ fallback automation** when none of the criteria above it matches. This automation will be called when the rest of them don’t match.
- You can map the input for the automation to be called below in the same node.

  ![Frame 427319213 (10).png](_img/2e6a4eba650f7349.webp)
