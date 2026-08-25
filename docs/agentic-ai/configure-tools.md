# Configure tools

Source: https://www.unifyapps.com/docs/unify-agentic-ai/configure-tools
Section: agentic-ai

---

![Frame 427319441.png](_img/a749ed570a1eb005.webp)

UnifyApps comes equipped with an extensive library of default tools that seamlessly integrate with your AI Agents, enabling them to perform complex operations across multiple platforms without writing a single line of code. These pre-built integrations empower your agents to pull data directly from various sources, trigger workflows, and execute actions across your entire tech stack. Let's explore how to leverage these powerful default tools to create sophisticated AI-driven automations.

## Understanding Default Tools

Default tools in UnifyApps are pre-configured integrations that provide your AI Agents with immediate access to popular business applications and services. These tools serve as building blocks that enable your agents to:

- **Pull Real-time Data**: Access information from various platforms to provide accurate, up-to-date responses
- **Trigger Workflows**: Initiate complex multi-step processes based on user interactions or specific conditions
- **Execute Actions**: Perform operations like creating records, updating information, or sending notifications
- **Connect Systems**: Bridge different applications to create unified workflows across your organization

## How to Leverage Default Tools

1. **Direct Data Access**: Configure your AI Agent to pull information directly from integrated tools. For instance, use Azure CosmosDB to retrieve customer data or Bitrix24 to access CRM records during conversations.
2. **Pre-existing Connection Utilization**: Leverage established connections to trigger specific workflows. Your AI Agent can use these connections to execute complex operations without requiring users to authenticate repeatedly.
3. **Multi-tool Orchestration**: Combine multiple default tools to create sophisticated workflows. For example, configure your AI Agent to pull customer data from Airtable, send personalized emails through Gmail, and then log the interaction in Slack, all triggered by a single user request.
4. **Conditional Logic Implementation**: Apply branching and conditional processing to determine which tools to use based on user input or data conditions.

## Implementation Best Practices

1. **Tool Selection Strategy**: Choose tools that align with your existing tech stack to maximize efficiency and minimize integration complexity.
2. **Authentication Management**: Set up secure connections once and reuse them across multiple AI Agent tasks, ensuring seamless user experiences.
3. **Data Flow Optimization**: Design your tool usage to minimize API calls and optimize performance, especially when dealing with high-volume operations.
4. **Error Handling**: Implement robust error handling for tool interactions to ensure your AI Agent can gracefully manage connection issues or API limitations.
5. **Testing Workflows**: Thoroughly test each tool integration in isolation before combining them into complex workflows.

## Real-World Use Cases

1. **Customer Support Enhancement**: Combine Azure Service Bus for message queuing, Bitrix24 for CRM data access, and Benchmark Email for automated follow-ups to create a comprehensive support system.
2. **Sales Automation**: Use Better Proposals for document generation, BigCommerce for order processing, and Billetto for event registration, all orchestrated by your AI Agent based on customer interactions.
3. **Project Management**: Integrate Awork for task tracking, Backlog for issue management, and Azure DevOps for development workflows, allowing your AI Agent to provide comprehensive project updates and automate routine tasks.

By leveraging UnifyApps' extensive library of default tools, you can transform your AI Agents from simple conversational interfaces into powerful automation engines that seamlessly integrate with your entire business ecosystem. These pre-built integrations eliminate the complexity of API development while providing the flexibility to create sophisticated, enterprise-grade solutions.
