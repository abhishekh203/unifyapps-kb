# Amazon SES connector

Source: https://www.unifyapps.com/docs/unify-integrations/amazon-ses
Section: integrations

---

Amazon Simple Email Service (SES) is a cloud-based email-sending service designed for marketing, transactional, and notification emails. It provides reliable, scalable, and cost-effective email delivery with built-in analytics and compliance features.

Integrating Amazon SES ensures reliable, scalable, and cost-effective email delivery with analytics and compliance built in.

## Authentication

Ensure you have the following information ready for a seamless integration process:

- `Connection Name`**:** Choose a meaningful name for your connection. This name helps you identify the connection within your application or integration settings. It could be something descriptive like "MyAppAmazonSESIntegration".
- `Authentication Type`**:** Select the type of authentication for connecting to your Amazon SES account:
  - IAM Role
  - Access Key

### Access Key Based

1. Login into Amazon AWS Console and search for "`Users`" in the search bar present at the top of the console's home page.
2. Click on "`Create user`" at the top right corner.
3. Sign in to the AWS Management Console by going to the AWS Management Console ([https://console.aws.amazon.com/](https://console.aws.amazon.com/)).
4. Navigate to the IAM (Identity and Access Management) dashboard by searching in the "`IAM`" search bar.
5. Provide the username and select permissions (AmazonSESFullAccess) policies by selecting "`Attach policies directly`" and click on the create user button.
6. Once the user is created, click on the username of the user created and under the summary section click on create access key.
7. Select "`Command Line Interface`" as the use case and provide the description tag to the key and click on "`create access key`".
8. Treat the access key and secret access key with high confidentiality, as it allows access to your Amazon SES account.

  ![Frame 47 (2).png](_img/9314800bfdc83a7f.webp)

### IAM Role Based

1. Sign in to AWS Management Console ([https://console.aws.amazon.com/](https://console.aws.amazon.com/)) and select security credentials.
2. Navigate to the IAM dashboard and click "`Roles`" > "`Create role`". ([https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html))
3. Under "`Trusted entity type`," choose the AWS account option.
4. Select "`Another AWS account`" and input the UnifyApps AWS account ID (contact support to obtain this).
5. Check the "`Require external ID`" box and enter the External ID provided by UnifyApps.

  ![Frame 48 (1).png](_img/fe995c4f9e1bd954.webp)

6. Assign the necessary permissions for UnifyApps to operate automated workflows within your account.
7. Give the IAM role a name and description.
8. Click the "`Select trusted entities`" Edit button to modify trusted entity policies if needed. (Optional)
9. Click the "`Add permissions`" Edit button to adjust permissions. (Optional)
10. If using object tags, select an appropriate tag for the IAM role. (Optional)
11. Click on Create Role to finalize the process.

### Create an IAM Permissions Policy

1. Go to the `AWS Console` and open the `IAM console` ([https://console.aws.amazon.com/iam](https://console.aws.amazon.com/iam)).
2. Navigate to `Access management` and select `Policies`.
3. Choose `Create Policy.`
4. Locate and choose the AWS service that UnifyApps will access.
5. Select the required permissions under the Actions field.
6. Define the resources that the role will have access to.
7. Continue clicking Next until you reach the Review policy page.
8. Provide a Name for the policy.
9. Click Create policy once done.

### Retrieve IAM Role ARN

1. Open the AWS Console and go to My Security Credentials > Roles.
2. Search for the IAM role you need for the connection.

  ![Frame 49 (1).png](_img/6fd86fda2e9693c8.webp)

3. Select the role to view its details.
4. Copy the Role ARN for use in the UnifyApps connection setup.

## Actions

| Actions | Description |
|---|---|
| `Create contact list` | Creates a new contact list in Amazon SES. |
| `Create template` | Creates an email template in Amazon SES for reusable email content. |
| `Delete contact` | Deletes a contact from a specified contact list in Amazon SES. |
| `Delete contact list` | Deletes a contact list from Amazon SES. |
| `Delete template` | Deletes an email template in Amazon SES. |
| `Get contact` | Retrieves information about a specific contact in Amazon SES. |
| `Get contact list` | Retrieves details of a specific contact list in Amazon SES. |
| `Get template` | Retrieves details of a specific email template in Amazon SES. |
| `List contact lists` | Lists all contact lists available in Amazon SES. |
| `List contacts` | Lists all contacts in a specific contact list in Amazon SES. |
| `List templates` | Lists all email templates available in Amazon SES. |
| `Send bulk email` | Sends bulk emails using a specified email template in Amazon SES. |
| `Send email` | Sends an individual email using Amazon SES. |
| `Update contact` | Updates details of a specific contact in Amazon SES. |
| `Update contact list` | Updates details of a specific contact list in Amazon SES. |
| `Update template` | Updates an existing email template in Amazon SES. |

## Triggers

| Triggers | Description |
|---|---|
| `New email via webhook` | Triggers when an email is received in Amazon SES |
