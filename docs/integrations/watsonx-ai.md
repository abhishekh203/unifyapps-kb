# Watsonx AI connector

Source: https://www.unifyapps.com/docs/unify-integrations/watsonx-ai
Section: integrations

---

Watsonx AI empowers businesses and developers to build, train, and deploy enterprise-grade AI solutions with confidence and scalability. Through a unified platform for foundation models, machine learning, and generative AI, Watsonx AI enables organizations to create intelligent applications, automate workflows, and extract deeper insights from their data.

## Authentication

Integrating your application with Watsonx AI unlock AI-powered capabilities including advanced language understanding, machine learning, and analytics. Before starting, ensure you have the following information:

- `Connection Name`: Choose a meaningful name for your connection. This name helps you identify the connection within your application or integration settings. It could be something descriptive like “MyAppWatsonxAIIntegration”.

### API Token Based:

1. Go to IBM watsonx.ai and log in.
2. In the Developer access section, select your Project or Space to reveal the Project ID and watsonx.ai URL.
3. Click on Create API Key.
4. Enter a name for your API key, optionally add a description.
5. Choose an action in case the key is leaked (Disable, Delete, or Nothing).
6. Click Create and then Copy the API Key value securely.
7. The domain URL is visible under the watsonx.ai URL field in the Developer access section.
8. Copy the URL (e.g., https://us-south.ml.cloud.ibm.com) as it will be required to make authenticated API calls to watsonx.ai.

## ACTIONS :

| **Action Name** | **Descriptions** |
|---|---|
| `Generate embeddings` | Generate embeddings from text input in Watsonx AI |
| `Chat completions (streaming)` | Generated conversational text using foundation models with streaming chat response in Watsonx AI |
| `Generate text` | Generates text using foundation models in Watsonx AI |
| `Generate text(streaming)` | Generates text using foundation models in Watsonx AI with streaming response |
| `Tool calling` | Generates text by sending a structured list of messages, together with a list of tools in Watsonx AI |
