# Guardrails overview

Source: https://www.unifyapps.com/docs/unify-agentic-ai/guardrails-overview
Section: agentic-ai

---

## What are Guardrails?

Guardrails act as the governance framework in enterprise risk management to establish clear boundaries, enforce compliance protocols, and ensure operational integrity. This ensures that every interaction and response aligns with organizational policies, ethical standards, and compliance requirements. This systematic approach to AI safety and compliance helps organizations leverage AI capabilities confidently while minimizing risks and maintaining high standards of interaction quality.

For example, let's look at sample guardrails implemented for a Financial Services AI Agent:

1. **Content Filters**
  - Blocks requests for unauthorized financial advice
  - Filters out requests for insider trading information
2. **Redact Sensitive Information**
  - Automatically masks credit card numbers (XXXX-XXXX-XXXX-1234)
  - Redacts SSN and tax ID numbers

## Key Components of UnifyApps Guardrails

1. **Hallucination Control**
  - Ensures your AI stays grounded in facts and responses are relevant to the user query
  - Ensures that the final response is grounded in reference to the knowledge source and relevant to the user query. For detailed configuration, refer to Hallucination Control [documentation](https://www.unifyapps.com/docs/unify-ai/hallucination-control).
2. **Content Filters**
  - Customizable filter levels for different content categories
  - Real-time screening of both inputs and outputs
  - Smart detection of problematic content like hate speech or harassment. For detailed configuration, refer to Content Filter [documentation](https://www.unifyapps.com/docs/unify-ai/content-filters).
3. **Custom Word Filter**
  - Blocks specific words or phrases in both user inputs and AI responses
  - Includes built-in profanity filtering and custom word/phrase blocking capabilities. For detailed configuration, refer to Custom Word Filter [documentation](https://www.unifyapps.com/docs/unify-ai/custom-word-filter).
4. **Denied Topics**
  - Prevents engagement with restricted or sensitive subjects
  - Allows configuration of specific topics to be blocked in both inputs and responses. For detailed configuration, refer to Denied Topics [documentation](https://www.unifyapps.com/docs/unify-ai/denied-topics).
5. **PII Masking**
  - Filters out sensitive data based on defined patterns
  - Offers options to block or mask confidential information like SSNs or phone numbers. For detailed configuration, refer to PII Masking [documentation](https://www.unifyapps.com/docs/unify-ai/pii-masking).

## Why Guardrails are important?

1. **Enhanced Safety**
  - Protect against inappropriate content
  - Maintain professional interactions
  - Ensure user safety
2. **Compliance Assurance**
  - Meet regulatory requirements
  - Adhere to industry standards
  - Maintain organizational policies
3. **Quality Control**
  - Ensure consistent responses
  - Maintain high-quality interactions
  - Control output standards
4. **Risk Mitigation**
  - Prevent unauthorized actions
  - Protect sensitive information
  - Reduce liability risks
