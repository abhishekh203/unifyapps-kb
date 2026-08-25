# Shiprocket connector

Source: https://www.unifyapps.com/docs/unify-integrations/shiprocket
Section: integrations

---

Shiprocket integration enables businesses and developers to automate shipping, order fulfillment, courier allocation, tracking, and returns management through Shiprocket’s REST APIs. It helps streamline logistics workflows, generate shipping labels, create AWBs, track shipments in real-time, and manage delivery operations efficiently.

## Authentication

Integrating your application with Shiprocket requires API authentication and proper account configuration. Before starting, ensure you have the following information:

- `Connection Name`**:** Choose a meaningful name for your connection. Example: *MyAppShiprocketIntegration*.
- `API Base URL`**:** https://apiv2.shiprocket.in
- `Authentication Type`**:** Token-Based Authentication
- `Required Credentials`**:** Registered Shiprocket Email ID and Password

### Authentication Setup

1. Log in to your Shiprocket seller panel.
2. Go to API settings or generate an authentication token via login API.
3. Use the login API to generate a Bearer Token.
4. Pass the Bearer Token in the Authorization header for subsequent API requests.

## ACTIONS :

| **Action Name** | **Description** |
|---|---|
| `Cancel Orders` | Cancel one or multiple orders created in Shiprocket. |
| `Cancel Shipment` | Cancel an already created shipment before dispatch. |
| `Check Courier Serviceability` | Check available courier partners and serviceability for pickup and delivery pincodes. |
| `Create Channel Order` | Create a new order linked to a sales channel integrated with Shiprocket. |
| `Create Custom Order` | Create a direct custom order in Shiprocket without a sales channel. |
| `Create Return Shipment` | Initiate a return shipment for delivered orders. |
| `Generate AWB for Shipment` | Generate an Air Waybill (AWB) number for a shipment. |
| `Generate Label` | Generate and download shipping label for a shipment. |
| `Get Order Details` | Retrieve detailed information of a specific order. |
| `Get Order Details (Client)` | Retrieve order details using client-based authentication context. |
| `Get Shipment Details` | Retrieve shipment status and tracking details. |
| `Get Statement Details` | Fetch account statement and transaction details. |
| `Get Tracking Data for Multiple AWBs` | Retrieve tracking information for multiple AWB numbers in a single request. |
| `Get Tracking Through AWB` | Track shipment using a single AWB number. |
| `On Delivery` | Trigger-based action executed when shipment is marked as delivered. |
| `Update Order Delivery Address` | Update the delivery address of an existing order. |
| `Update Order Pickup Location` | Update the pickup location details for an order. |
