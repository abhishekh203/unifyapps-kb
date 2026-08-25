# AI agent overview integration | connect with UnifyApps

Source: https://www.unifyapps.com/docs/unify-agentic-ai/ai-agent-overview
Section: agentic-ai

---

## What are AI Agents?

AI agents utilize large language models (LLMs) to autonomously process information, make decisions, and perform tasks to achieve specific goals. These handle complex operations across various industries, from sales and customer service to research and data analysis. AI agents understand context, learn from interactions, and provide tailored solutions.

## How AI Agents Work?

At the core of an AI agent's functionality is its capacity to process input data, make informed decisions, and execute appropriate actions. This continuous cycle of data analysis, decision-making, and task execution forms the fundamental basis of how AI agents operate.

To help illustrate this process, imagine an employee needs to submit an expense report for a business trip. Instead of manually handling the entire process, they task an AI Agent with processing their expenses. Since the LLM model at the core of the agent doesn't have direct access to company policies or systems, the agent:

- Reviews the company's expense policy from SharePoint
- Scans email inbox for relevant receipts
- Checks corporate card transactions for the travel dates
- Verifies expense limits for meals and hotels

The AI Agent then:

- Matches receipts with transactions
- Flags any items that exceed policy limits
- Creates the expense report in the system
- Manages approval flow with stakeholder notifications

What typically takes an employee 30-45 minutes of manual work is completed in minutes with higher accuracy and in a proper structured manner.

## Understanding AI Agent Capabilities

1. **Knowledge Acquisition**: AI agents gather information through various input methods. For example, a virtual assistant might integrate with external applications like Slack, Google Drive, SharePoint APIs to collect relevant data. AI agents employ Retrieval-Augmented Generation (RAG) that enables LLMs to retrieve relevant external information before generating responses, ensuring more accurate and up-to-date answers compared to using fixed training data alone. This approach enables the agent to provide accurate and up-to-date responses based on enterprise data.
2. **Decision-Making**: The agent processes information based on custom business logic and decides the best course of action. This can range from simple rule-based logic to complex logics simulating human-like reasoning.
3. **Responsive Actions:** Based on the decision, the AI agent performs an action to achieve its goals or respond to inputs. This could involve sending messages on Slack, updating a record on ServiceNow , or applying for leave on Workday.
4. **Feedback and Learning**: AI agents are designed to learn from their experiences over time. The AI Agents also support episodic memory and long term memory, which are available by default without any custom configuration. For example, a sales AI agent might learn from successful and unsuccessful interactions to refine its approach in future customer engagements.
