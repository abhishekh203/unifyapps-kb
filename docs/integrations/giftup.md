# GiftUp connector

Source: https://www.unifyapps.com/docs/unify-integrations/giftup
Section: integrations

---

GiftUp is a digital platform that allows businesses to sell, manage, and redeem gift cards online. It integrates seamlessly with websites and apps to streamline gift card transactions and promotions.

Integrating GiftUp enables effortless gift card sales, redemptions, and tracking directly within your existing platform.

## Authentication

Before you begin, make sure you have the following information:

- `Connection Name`: Select a descriptive name for your connection, like "MyAppGiftUpIntegration". This helps in easily identifying the connection within your application or integration settings.
- `Authentication Type`**:** GiftUp supports API Key authentication.

## API Key Based Authentication

- Log into your GiftUp account and navigate to the "`Settings`" section from the menu.
- Click on View "`Gift Up! Integrations`"
- Navigate to the bottom of the page and click on "`Get an API Key`"
- In the "`API Keys`" tab, you will find your unique API Key.
- If an API Key is not yet generated, click on "`Create a New API Key`" to create one.
- Copy the API Key and keep it secure, as it grants access to your GiftUp account.

  ![Frame 226.png](_img/206f533ddfd252fe.webp)

## Actions

| Actions | Description |
|---|---|
| `Create item` | Creates a new item in GiftUp |
| `Create order` | Creates an order in GiftUp |
| `Delete item` | Deletes an item in GiftUp |
| `Find gift card` | Finds a gift card in GiftUp |
| `Find report transaction` | Finds a report transaction in GiftUp |
| `List all items` | Lists all items in GiftUp |
| `List all promotions` | Lists all promotions in GiftUp |
| `List report transactions` | Lists a report transactions in GiftUp |
| `Redeem gift card` | Redeems a gift card in GiftUp |
| `Update item` | Updates an item in GiftUp |
| `Update order` | Updates an order in GiftUp |

## Triggers

| Triggers | Description |
|---|---|
| `Gift card redeemed` | Triggers when a gift card is redeemed in GiftUp |
| `Gift card updated` | Triggers on any changes to a gift card, including redemptions in GiftUp |
| `New gift card` | Triggers when a new gift card is created in GiftUp |
| `New order` | Triggers when a new order is placed in GiftUp |
