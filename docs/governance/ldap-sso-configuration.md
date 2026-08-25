# LDAP SSO Configuration

Source: https://www.unifyapps.com/docs/governance/ldap-sso-configuration
Section: governance

---

# **LDAP SSO Configuration Guide**

UnifyApps · Identity Provider Configuration & Automation

## **1. Open Directory Settings in UnifyApps**

Follow the steps below to establish a secure directory integration using Lightweight Directory Access Protocol (LDAP).

### **STEP 1 · Open Directory Settings**

Navigate to your environment in UnifyApps and go to: **Settings** → **Security** → **Identity Providers**.

### **STEP 2 · Select LDAP**

Select **LDAP** from the provider dropdown menu to reveal the configuration forms.

## **2. Configure Directory Connection & Select Auth Type**

### **STEP 3 · Provide Server Connection Details**

Fill out the network path to your directory server:

- **LDAP Host / URL:** Enter the server address (e.g., ldap://company.com or ldaps://company.com ).
- **Port:** Enter 389 for standard LDAP or 636 for secure LDAPS.

### **STEP 4 · Choose Your Authentication Type**

Select your preferred workflow based on your directory architecture and complete the respective fields:

#### **Option A: Search and Bind**

*Use this option if users are scattered across different organizational units (OUs), requiring a system account to look up user paths first.*

- **Admin Distinguished Name*:** Enter the full DN path of your service/admin account (e.g., cn=unify_svc,ou=ServiceAccounts,dc=company,dc=com ).
- **Admin Password*:** Enter the password for the service/admin account.
- **Search Filter*:** Set the lookup filter used to find the user entry (e.g., (sAMAccountName={0}) or (uid={0}) ).
- **Search Base*:** Define the specific node in the tree where the user search should be performed (e.g., ou=Employees,dc=company,dc=com ).
- **Search Scope:** Select the depth of the search within the tree (e.g., *Base*, *One Level*, or *Subtree*).
- **Base Distinguished Name*:** Enter the root DN of your directory tree (e.g., dc=company,dc=com ).
- **User Identifier Attribute:** Specify the attribute that holds the user login name (e.g., sAMAccountName or uid ).

#### **Option B: Direct Bind**

*Use this option if you want UnifyApps to authenticate users immediately against a uniform, flat directory structure without a service account lookup.*

- **Base Distinguished Name*:** Enter the root directory node where your user accounts reside (e.g., ou=Users,dc=company,dc=com ).
- **User Identifier Attribute*:** Specify the attribute that serves as the unique login username (e.g., uid or userPrincipalName ).

## **3. Configure Fallback Auth & Finalize**

### **STEP 5 · Set Alternative Authentication**

Configure the fallback setting at the bottom of the form:

- **Do you wish to use UnifyApps password store as an alternative authentication?:** Check this box or toggle to **Yes** if you want users to be able to log in using their locally managed UnifyApps password if the LDAP server is unreachable or if a user profile does not exist in the directory.

### **STEP 6 · Test and Save**

Click **Test Connection** to validate the configuration against your server. Once successful, click **Save** and toggle the LDAP identity provider to **Active**.
