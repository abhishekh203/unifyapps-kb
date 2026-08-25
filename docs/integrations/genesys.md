# Genesys connector

Source: https://www.unifyapps.com/docs/unify-integrations/genesys
Section: integrations

---

Genesys empowers advanced customer experience orchestration by unifying voice, chat, messaging, and digital channels within a single cloud contact center platform. It provides intelligent routing, real-time analytics, workforce engagement tools, and AI-driven automation to help organizations deliver personalized, scalable, and seamless customer interactions across every touchpoint.

## Authentication:

Integrating your application with Genesys enables unified customer engagement, intelligent routing, and real-time interaction management to optimize contact center performance and elevate customer experience. Before you begin, ensure you have the following information:

- `Connection Name` : Choose a meaningful name for your connection. This name helps you identify the connection within your application or integration settings. It could be something descriptive like "MyAppGenesysIntegration".
- `Region`: Select the region matching your Genesys Cloud account.

### Client Credentials Based:

1. Log into your Genesys Cloud account.
2. From the main menu, go to Admin -> Integrations -> OAuth.
3. Click the + Add Client button and provide app name and then select grant type as Client credentials.
4. Click Next, then toggle on the specific roles your app needs and then click Next.
5. Adjust the token duration if needed and click on save.
6. Copy the generated client ID and client secret and use it for further authentication purposes.

## Actions :

| **Action Name** | **Description** |
|---|---|
| `Add group members` | Adds group member in Genesys |
| `Assign routing language to an existing user` | Assigns routing language to an existing user in Genesys |
| `Assign routing skill to an existing user` | Assigns routing skill to an existing user in Genesys |
| `Change your account password` | Changes your account password in Genesys |
| `Create an agentless email conversation` | Creates an agentless email conversation in Genesys |
| `Create an email conversation` | Creates an email conversation in Genesys |
| `Create a single benefit assessment` | Creates a single benefit assessment in Genesys |
| `Create a call conversation` | Creates a call conversation in Genesys |
| `Create a call conversation on behalf of a user` | Creates a call conversation on behalf of a user in Genesys |
| `Create a new location` | Creates a new location in Genesys |
| `Create an outbounding message conversation` | Creates an outbounding message conversation in Genesys |
| `Create routing language` | Creates routing language in Genesys |
| `Create a routing queue` | Creates a routing queue in Genesys |
| `Create routing skill` | Creates a routing skill in Genesys |
| `Create routing wrapupcode` | Creates a routing wrapupcode in Genesys |
| `Create edge` | Creates edge in Genesys |
| `Create a new didpol` | Creates a new didpol in Genesys |
| `Create a new extension pool` | Creates a new extension pool in Genesys |
| `Create telephony edge poll` | Creates telephony edge poll in Genesys |
| `Create a telephony edge site` | Creates a telephony edge site in Genesys |
| `Create a telephony edge trunk base settings` | Creates a telephony edge trunk base settings in Genesys |
| `Create a new user` | Creates a new user in Genesys |
| `Create a new user group` | Creates a new user group in Genesys |
| `Delete a single benefit by assessment ID` | Deletes a single benefit by assessment ID in Genesys |
| `Delete an existing location` | Deletes an existing location in Genesys |
| `Delete routing language` | Deletes a routing language in Genesys |
| `Delete a routing queue by ID` | Deletes a routing queue by ID in Genesys |
| `Delete routing skill` | Deletes a routing skill in Genesys |
| `Delete routing wrapupcode` | Deletes a routing wrapupcode in Genesys |
| `Delete an existing edge` | Deletes an existing edge in Genesys |
| `Delete didpol by ID` | Deletes a Genesys didpol by ID |
| `Delete extension pools by ID` | Deletes extension pools by ID in Genesys |
| `Delete telephony edge phone by ID` | Deletes telephony edge phone by ID in Genesys |
| `Delete telephony edge sites by ID` | Deletes telephony edge sites by ID in Genesys |
| `Delete telephony edge trunk base settings by ID` | Delete telephony edge trunk base settings by ID in Genesys |
| `Delete an existing user` | Deletes an existing user in Genesys |
| `Delete a new user group` | Deletes a new user group in Genesys |
| `Get active call conversations` | Gets active call conversations in Genesys |
| `Get a active call conversation by ID` | Gets active call conversation by ID in Genesys |
| `Get active mail conversations` | Gets active mail conversations in Genesys |
| `Get a single benefit assessment by ID` | Gets single benefit assessment by ID in Genesys |
| `Retrieves conversation by id` | Retrieves conversation by conversation id in Genesys |
| `Retrieves conversation analytics data` | Retrieves conversation analytics data by conversation ID in Genesys |
| `Get conversation draft reply` | Retrieves the current draft reply for a specific email conversation in Genesys Cloud using its conversation ID |
| `Get conversation message` | Retrieves a specific email message within a Genesys cloud conversation. |
| `List email conversation messages` | Retrieves the history of messages within the conversation |
| `Retrieves conversations call history` | Retrieves conversations call history in Genesys |
| `Get email conversation by ID` | Retrieves the details of a specific email conversation in Genesys Cloud using its Conversation ID |
| `Get group members` | Gets group members in Genesys |
| `Get location by ID` | Gets a location by ID in Genesys |
| `Get a message conversation` | Gets message conversation in Genesys |
| `Get a message conversation by id` | Gets message conversation by id  in Genesys |
| `Get outbound event` | Gets an outbound event in Genesys |
| `Get routing language` | Gets a routing language in Genesys |
| `Get a routing queue by ID` | Gets a routing queue by ID in Genesys |
| `Get routing skill` | Gets a routing skill in Genesys |
| `Get routing wrapupcode` | Gets a routing wrapupcode in Genesys |
| `Get station by ID` | Gets a station by ID in Genesys |
| `Get telephony line` | Gets a telephony line in Genesys |
| `Get an existing edge` | Gets an existing edge in Genesys |
| `Gets listing of unassigned and/or assigned numbers in a set of didpools` | Gets listing of unassigned and/or assigned numbers in a set of didpools in Genesys |
| `Get extensionpool in by ID` | Gets extensionpool in Genesys by ID |
| `Get extension pools` | Gets extension pools in Genesys |
| `Get extension pools in divisionviews` | Get extension pools in divisionviews in Genesys |
| `Get telephony extensions by ID` | Gets telephony extensions in Genesys by ID |
| `Get telephony phone by ID` | Gets telephony phone by ID in Genesys |
| `Get telephony edge sites by site ID` | Gets telephony edge sites by site ID in Genesys |
| `Get telephony edge trunk base settings by site ID` | Gets telephony edge trunk base settings by site ID in Genesys |
| `Get didpool by ID` | Gets a Genesys didpool in Genesys by its ID |
| `Get did by ID` | Gets a Genesys did by ID |
| `Get a user by ID` | Gets a user by ID in Genesys |
| `Get an existing user group` | Gets an existing user group in Genesys |
| `Get queues for a user` | Gets queues for a user in Genesys |
| `Get routing languages assigned to a user` | Gets routing languages assigned to a user in Genesys |
| `Get routing skills assigned to a user` | Gets routing skills assigned to a user in Genesys |
| `Get routing status of a user` | Gets routing status of a user in Genesys |
| `Get skill groups for a user` | Gets skill groups for a user in Genesys |
| `Get state information of a user` | Gets state information of a user in Genesys |
| `Get station information of a user` | Gets station information of a user in Genesys |
| `Lists users` | Lists users in Genesys |
| `Query conversation details` | Query for conversation details in Genesys |
| `Remove group members` | Removes group members in Genesys |
| `Search users` | Search users using query in Genesys |
| `Send an agentless outbound message` | Sends an agentless outbound message in Genesys |
| `Send reply to an existing conversation` | Sends an email reply to an existing conversation in Genesys |
| `Send email to an external conversation` | Sends email to an external conversation in Genesys |
| `Send an inbound open text message` | Sends an inbound open text message in Genesys |
| `Send message on existing conversation and communication` | Sends a message on existing conversation and communication in Genesys |
| `Unassign user assigned to a station` | Unassigns user assigned to a station in Genesys |
| `Update an existing location` | Updates an existing location in Genesys |
| `Update a routing queue by ID` | Updates a routing queue by ID in Genesys |
| `Update an existing edge` | Updates an existing edge in Genesys |
| `Update extensionpool by ID` | Updates extensionpool by ID in Genesys |
| `Update telephone edge phone by ID` | Updates telephone edge phone by ID in Genesys |
| `Update telephony edge sites by site ID` | Updates telephony edge sites by site ID in Genesys |
| `Update telephony edge trunk base settings by ID` | Updates telephony edge trunk base settings by ID in Genesys |
| `Update didpool by ID` | Updates a didpool in Genesys by its ID |
| `Update user’s associated station` | Updates user’s associated station in Genesys |
| `Update user’s default station` | Updates user’s default station in Genesys |
| `Update an existing user group` | Updates an existing user group in Genesys |
| `Change a user’s password` | Changes a user’s password in Genesys |
| `Update user profile skills` | Updates user profile skill in Genesys |
| `Update user’s role` | Updates user’s role in Genesys |
| `Update user routing skill` | Updates user routing skill in Genesys |
| `Update user routing status` | Updates user routing status in Genesys |
| `Update user routing skills in bulk` | Updates user routing skills in bulk in Genesys |
| `Update user state information` | Updates user state information in Genesys |
| `Update user’s verifier` | Updates user’s verifier in Genesys |

## Triggers :

| **Trigger Name** | **Description** |
|---|---|
| `On new event` | Triggers when a new event is occurred in Genesys |
