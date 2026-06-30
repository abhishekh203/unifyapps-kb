# Create an AI Agent

Source: https://www.unifyapps.com/docs/unify-agentic-ai/create-an-ai-agent
Section: agentic-ai

---

UnifyApp’s AI agents use a **Chain of Thought (COT)** process, where they break down complex tasks into manageable steps.

To function effectively, they require access to `knowledge`, use `prompts` to understand tasks and follow predefined `guardrails` to ensure safe and accurate actions.

Additionally, they handle `prerequisite tasks` to set up automations and ensure smooth execution of actions.

To effectively utilise AI agents by UnifyApps, Let's understand its basic building blocks.

## Knowledge

Knowledge refers to the **data**, **rules**, and **information** an AI agent uses to understand and respond to various tasks.

Within UnifyApps, this knowledge can be **pre-loaded** or **dynamically** gathered in **real time** from sources such as databases, APIs, or user inputs. This may include an organization’s internal knowledge articles, external data, CRM data, websites, and more.

**Insurance AI Agent** can be fed with policy details, premiums, and coverage options, enabling it to provide **quick**, **accurate** answers and **improve** customer support.

The broader and more precise the knowledge, the more effectively the AI agent can perform. In many cases, AI agents can also **learn continuously** and **improve** their responses through user interactions.

In addition, UnifyApps supports **Role-Based Access Control (RBAC)** filters within its knowledge structure. By integrating RBAC filters, AI agents can dynamically filter out restricted information, ensuring that the knowledge provided is relevant and appropriate based on the **user’s role**.

> **Note:** To explore more about how to add your organization’s Knowledge base to your AI Agents, refer to [this](https://www.unifyapps.com/docs/unify-ai/knowledge) article.

## Topics

Topics in UnifyApps’ AI Agents are **groups of actions** that focus on specific areas the agent is trained to handle.

Each topic is designed to execute particular tasks, gather necessary information, and easily complete processes. Users can define these **tasks**, providing detailed **instructions** for the AI agent.

Topics are essentially collections of multiple automations ( refer to [Unify Automation](https://www.unifyapps.com/docs/unify-automations/build-your-first-automation) Documentation for details) triggered by user actions or prompts. Once activated, the AI agent fills in the required information and executes the task smoothly.

> **Note:** Refer to [this](https://www.unifyapps.com/docs/unify-ai/topics) article to know more about Topics and how to configure it.

## Prompts

Prompts in AI Agents are set of **instructions** or **commands** provided to the agent to trigger a specific task or query. They guide the agent in understanding what action needs to be performed.

The accuracy and clarity of the prompts are essential, as they directly influence the agent’s ability to deliver precise and relevant results.

By using **well-crafted prompts** in AI Agent, users can give clear instructions that ensure smooth task execution. High-quality prompts enable the AI agent to produce precise outcomes, enhancing the performance of business processes.

> **Note:** Discover more about how to add a prompt and the best practices to write instructions to your agent in [this](https://www.unifyapps.com/docs/unify-ai/prompts) article.

## Guardrails

Guardrails are a feature in UnifyApps’ AI Agent that are predefined **rules** and **boundaries** that ensure AI agents operate within **safe**, **ethical**, and business-aligned guidelines.

These guardrails are important for maintaining the **reliability** and **integrity** of AI agents by preventing unintended actions, blocking inappropriate content, and ensuring compliance with company policies and regulations.

By setting up guardrails, businesses using AI Agents can ensure that their agents consistently deliver accurate and responsible outcomes, safeguarding **operational** **performance** and **ethical** **standards**.

**Why Are Guardrails Important?**

Guardrails are essential for ensuring that AI agents:

- Provide accurate and reliable responses.
- Avoid harmful or inappropriate actions.
- Respect privacy and data security regulations.
- Stay aligned with company policies and ethical standards.

By implementing these guardrails, businesses can ensure that AI agents operate while maintaining **safety**, **accuracy**, and **compliance**.

> **Note:** Learn more about how UnifyApps supports the Guardrail feature in [this](https://www.unifyapps.com/docs/unify-ai/guardrails) article.

## Prerequisite Tasks

Prerequisite tasks for AI agents are simple steps needed before the agent can start. These tasks include collecting necessary information, like **user data** or **access** **permissions**, to ensure the agent is ready to work.

Fetching customer details or configuring system settings ensures the AI agent runs smoothly, delivering accurate and reliable results from the start.

> **Note:** Refer to [this](https://www.unifyapps.com/docs/unify-ai/prerequisite-tasks) article for configuring Prerequisite Tasks for your AI Agents.
