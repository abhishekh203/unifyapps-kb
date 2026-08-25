# Razorpay connector

Source: https://www.unifyapps.com/docs/unify-integrations/razorpay
Section: integrations

---

Integrating your application with Razorpay enables seamless online payment processing by supporting multiple payment methods such as cards, UPI, and net banking within a single platform. Razorpay helps automate payment collection, manage transactions, and ensure secure and reliable payment experiences, allowing businesses to streamline their financial operations efficiently.

## Authentication:

Connecting your application with Razorpay enables smooth payment collection, real-time transaction tracking, and automated billing processes across multiple payment channels. Before you begin, ensure you have the following information:

`Connection Name` : Choose a meaningful name for your connection. This name helps you identify the connection within your application or integration settings. It could be something descriptive like "MyAppRazorpayIntegration".

### Basic Based :

1. Log in to your Dashboard using your credentials.
2. Go to Account & Settings.
3. Open API Keys under Website and App Settings.
4. Click on Generate Key to create an API key.
5. Copy the generated key ID, key secret and use it for further authentication purposes.

## **Actions:**

| **Action Name** | **Description** |
|---|---|
| `Create a standard payment link` | Creates a standard payment link in Razorpay |
| `Create order` | Creates a new order in Razorpay |
| `Create payout links using contact details` | Creates a payout link using contact details in Razorpay |
| `Fetch all settlements` | Fetches all settlements from your Razorpay account |
| `Fetch settlement` | Fetches settlement reconciliation details in Razorpay |
| `Get order by ID` | Fetches the details of a specific order by its ID in Razorpay |
| `Get payout link status` | Gets the status of a payout link in Razorpay |
| `Initiate refund` | Initiates a refund for an order in Razorpay |
| `List all orders` | Lists all orders in Razorpay |
| `List payments of order` | Fetches all payments of an order from Razorpay |
| `Update order` | Updates the notes of an existing order in Razorpay |

## Triggers**:**

| **Trigger Name** | **Description** |
|---|---|
| `On payment` | Triggers when a payment is successfully made in Razorpay |
