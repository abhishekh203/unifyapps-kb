# Amazon Cloudwatch integration | connect with UnifyApps

Source: https://www.unifyapps.com/docs/unify-integrations/amazon-cloudwatch
Section: integrations

---

Amazon CloudWatch is a monitoring and observability service that provides actionable insights into applications, infrastructure, and services on AWS and on-premises. It enables real-time metrics collection, log analysis, and automated alerts to optimize performance and resolve issues quickly.

Integrating Amazon CloudWatch enables real-time monitoring, automated alerts, and actionable insights to optimize system performance and reliability.

## Authentication

Before you begin, make sure you have the following information:

- `Connection Name`: Select a descriptive name for your connection, like "MyAppAmazonCloudwatchIntegration". This helps in easily identifying the connection within your application or integration settings.
- `Authentication Type`: Select the type of authentication for connecting to your Amazon cloudwatch account:
  - IAM Role
  - Access Key

### Access Key Based

1. Login into Amazon AWS Console and search for "`Users`" in the search bar present at the top of the console's home page.
2. Click on "`Create user`" at the top right corner.
3. Sign in to the AWS Management Console by going to the AWS Management Console ([https://console.aws.amazon.com/](https://console.aws.amazon.com/)).
4. Navigate to the IAM (Identity and Access Management) dashboard by searching in the "`IAM`" search bar.
5. Provide the username and select permissions (AmazonCloudwatchFullAccess) policies by selecting "`Attach policies directly`" and click on the `create user` button.
6. Once the user is created, click on the username of the user created and under the summary section click on `create access key`.
7. Select "`Command Line Interface`" as the use case and provide the description tag to the key and click on "`create access key`".
8. Treat the access key and secret access key with high confidentiality, as it allows access to your Amazon Cloudwatch account.

  ![Frame 47 (3).png](_img/0ef5542d0919b61a.webp)

### **IAM Role Based**

1. Sign in to AWS Management Console ([https://console.aws.amazon.com/](https://console.aws.amazon.com/)) and select security credentials.
2. Navigate to the IAM dashboard and click "`Roles`" > "`Create role`". ([https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html))
3. Under "`Trusted entity type`," choose the AWS account option.
4. Select "`Another AWS account`" and input the UnifyApps AWS account ID (contact support to obtain this).
5. Check the "`Require external ID`" box and enter the External ID provided by UnifyApps.

  ![Frame 48 (2).png](_img/00a34b3128e2c055.webp)

6. Assign the necessary permissions for UnifyApps to operate automated workflows within your account.
7. Give the IAM role a name and description.
8. Click the "`Select trusted entities`" Edit button to modify trusted entity policies if needed. (Optional)
9. Click the "`Add permissions`" Edit button to adjust permissions. **(Optional)**
10. If using object tags, select an appropriate tag for the IAM role. **(Optional)**
11. Click on `Create Role` to finalize the process.

### Create an IAM Permissions Policy

1. Go to the AWS Console and open the IAM console ([https://console.aws.amazon.com/iam](https://console.aws.amazon.com/iam)).
2. Navigate to `Access management` and select `Policies`.
3. Choose `Create Policy`.
4. Locate and choose the AWS service that UnifyApps will access.
5. Select the required permissions under the `Actions` field.
6. Define the resources that the role will have access to.
7. Continue clicking Next until you reach the Review policy page.
8. Provide a Name for the policy.
9. Click `Create policy` once done.

### Retrieve IAM Role ARN

1. Open the AWS Console and go to `My Security Credentials` > `Roles`.
2. Search for the IAM role you need for the connection.

  ![Frame 49 (2).png](_img/646ebe86af3dad88.webp)

3. Select the role to view its details.
4. Copy the Role ARN for use in the UnifyApps connection setup.

## Actions

| Actions | Description |
|---|---|
| `Delete alarms` | Deletes specified alarms in Amazon CloudWatch |
| `Disable alarm actions` | Disables actions for the specified alarms in Amazon CloudWatch |
| `Enable alarm actions` | Enables actions for the specified alarms in Amazon CloudWatch |
| `Set alarm state` | Sets the state of an alarm in Amazon CloudWatch |
