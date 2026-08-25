# AS2 connector

Source: https://www.unifyapps.com/docs/unify-integrations/as2
Section: integrations

---

AS2 (Applicability Statement 2) is a protocol that securely transmits business data over the internet using HTTP/S. It ensures confidentiality, integrity, and authenticity through encryption, digital signatures, and message receipts.

Integrating AS2 ensures secure, reliable, and cost-effective data exchange, enhancing compliance and interoperability with business partners.

## Authentication

Before integrating AS2, ensure you have the following information:

- `Connection Name`**:** Choose a descriptive name for your AS2 connection to help you identify it within your application or integration settings. A meaningful name, like "MyAppAS2Integration," helps maintain organization, especially when managing multiple integrations.
- `Sender AS2 ID`**:** The AS2 ID of the sender. A unique identifier used to establish the identity of the sender.
- `Sender Email`**:** The email address associated with the sender. This is typically used for communication or notifications related to AS2 transmissions.
- `Private key`**:** RSA client key in .pem format. Needed if you want to send encrypted messages.
- `Client certificate`**:** X509 client certification in .pem format. Needed if you want to send signed messages.

## Actions

| Actions | Description |
|---|---|
| `Send AS2 message` | Send AS2 message to receiver and get MDN response |

## Triggers

| Triggers | Description |
|---|---|
| `On new message` | AS2 server for receiving messages |
