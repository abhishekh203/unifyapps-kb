# Maven by Glaucus integration | connect with UnifyApps

Source: https://www.unifyapps.com/docs/unify-integrations/maven-by-glaucus
Section: integrations

---

Maven by Glaucus is a supply chain collaboration and logistics management platform that enables organizations to manage procurement, inventory, orders, shipments, and supplier communications in a centralized system. 
 By integrating Maven APIs, you can automate operational workflows, retrieve business data, synchronize order and shipment information, and connect Maven with other enterprise applications.

## Authentication:

Before you begin, make sure you have the following information:

`Connection name`: Choose a descriptive name for your connection, such as **“Maven by Glaucus Connection”**. This helps you easily identify the connection within your integration settings.

`Authentication Type`: Maven by Glaucus uses **login-based token authentication**.

## Token Based:

1. Log in to your **Maven by Glaucus** tenant using your organization credentials.
2. Identify your organization’s Maven domain (for example: imaginetest.gscmaven.com).
3. Enter the email address associated with your account. This is typically the address you used when signing up for the service. Make sure to enter it accurately to ensure successful login and account access.
4. Enter your account password. Passwords are case-sensitive, so ensure that you enter uppercase and lowercase characters correctly. Your password should be kept confidential and not shared with anyone.

## Actions**:**

| **Action Name** | **Description** |
|---|---|
| `Cancel a sale order` | Cancels a sale order in Maven |
| `Check inventory` | Checks inventory in Maven |
| `Check sale order status` | Gets status of a sale order from Maven |
| `Create a sale order` | Creates a sale order in Maven |
| `Create reverse order` | Creates a reverse order for a given order in Maven |
| `Get GRN details` | Gets GRN details for the given order numbers from Maven |
| `Get USN details for packed items` | Gets USN details for a list of orders from Maven |
| `Get USN details on Grade Change` | Gets USN details on grade change in Maven |
| `Get inventory snapshot` | Gets snapshot of inventory (excel) from Maven |
