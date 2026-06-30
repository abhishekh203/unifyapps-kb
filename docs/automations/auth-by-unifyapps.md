# Auth by UnifyApps

Source: https://www.unifyapps.com/docs/unify-automations/auth-by-unifyapps
Section: automations

---

Auth by UnifyApps provides comprehensive authentication and identity management capabilities for your automation workflows. This enables you to handle user authentication, manage identity providers, configure multi-factor authentication, and control password management processes, making it essential for secure workflow automation and user access management.

## Biometric Registered

This action checks the registration status of biometric authentication for users within the system. Add the Auth by UnifyApps node, select "`Biometric Registered`" option and provide below mentioned inputs.

**Inputs:** No specific input fields are required for this action.

**Output:** Returns information about biometric registration status, allowing you to verify whether users have biometric authentication configured and can proceed with biometric-based workflows.

## Login to UnifyApps

This action handles user authentication processes within the UnifyApps platform. Add the Auth by UnifyApps node, select "`Login to UnifyApps`" option and provide below mentioned inputs.

**Inputs:** No specific input fields are required for this action.

**Output:** Returns authentication status and session information, providing confirmation of successful login and session tokens for subsequent workflow steps.

## Create Identity Provider

This action establishes new identity providers for authentication workflows, enabling integration with external authentication systems. Add the Auth by UnifyApps node, select "`Create Identity Provider`" option and provide below mentioned inputs.

**Inputs:**

1. **Name:** Specify the name for the identity provider that will be used to identify this authentication source
2. **Application ID:** Provide the application identifier to associate with the identity provider, linking it to specific applications in your workflow

**Output:** Returns the created identity provider details and configuration information, including the provider ID and settings that can be used in subsequent authentication workflows.

## Update Identity Provider

This action modifies existing identity provider configurations to update settings or change authentication parameters. Add the Auth by UnifyApps node, select "`Update Identity Provider`" option and provide below mentioned inputs.

**Inputs:** Input fields are available but specific parameters depend on the provider being updated. Common fields include provider configuration settings and authentication parameters.

**Output:** Returns updated identity provider information, confirming the changes made and providing the current configuration state.

## Delete Identity Provider

This action removes identity providers from the system when they are no longer needed. Add the Auth by UnifyApps node, select "`Delete Identity Provider`" option and provide below mentioned inputs.

**Inputs:**

1. **Identity Provider ID:** Specify the ID of the identity provider to delete, ensuring the correct provider is targeted for removal

**Output:** Returns confirmation of deletion status, indicating whether the identity provider was successfully removed from the system.

## Fetch Identity Providers

This action retrieves a list of configured identity providers, allowing you to view all available authentication sources. Add the Auth by UnifyApps node, select "`Fetch Identity Providers`" option and provide below mentioned inputs.

**Inputs:** No specific input fields are required for this action.

**Output:** Returns a list of available identity providers and their configurations, including provider names, IDs, and current status information that can be used for management and workflow planning.

## Reset Password

This action completes the password reset process for users after validation steps have been completed. Add the Auth by UnifyApps node, select "`Reset Password`" option and provide below mentioned inputs.

**Inputs:** No specific input fields are required for this action.

**Output:** Returns password reset completion status, confirming whether the password change was successful and providing any relevant status information.

## Trigger Reset Password

This action initiates the password reset workflow for users, starting the process of changing user credentials. Add the Auth by UnifyApps node, select "`Trigger Reset Password`" option and provide below mentioned inputs.

**Inputs:** No specific input fields are required for this action.

**Output:** Returns information about the triggered reset process, including reset tokens or session identifiers needed for subsequent steps in the password reset workflow.

## Validate Reset Password Session

This action verifies the validity of password reset sessions to ensure security and prevent unauthorized access. Add the Auth by UnifyApps node, select "`Validate Reset Password Session`" option and provide below mentioned inputs.

**Inputs:** No specific input fields are required for this action.

**Output:** Returns session validation status and details, confirming whether the reset session is valid and providing timing or security information.

## Verify MFA

This action validates multi-factor authentication attempts to ensure additional security layers are properly enforced. Add the Auth by UnifyApps node, select "`Verify MFA`" option and provide below mentioned inputs.

**Inputs:** No specific input fields are required for this action.

**Output:** Returns MFA verification results, indicating whether the multi-factor authentication was successful and providing any additional security tokens or status information.

## Re Trigger MFA

This action initiates a new multi-factor authentication request when the previous attempt has failed or expired. Add the Auth by UnifyApps node, select "`Re Trigger MFA`" option and provide below mentioned inputs.

**Inputs:** No specific input fields are required for this action.

**Output:** Returns information about the re-triggered MFA process, including new authentication codes or session identifiers for the fresh MFA attempt.

## Create User External Session

This action establishes external user sessions for third-party integrations, enabling secure connections with external applications. Add the Auth by UnifyApps node, select "`Create User External Session`" option and provide below mentioned inputs.

**Inputs:**

1. **Application ID:** Specify the application identifier for which the external session should be created
2. **Identity Provider ID:** Provide the identity provider identifier for session creation, linking the session to the appropriate authentication source

**Output:** Returns external session details and authentication tokens, providing the necessary credentials and session information for third-party application integration.

## Update Max Login Failures

This action configures the maximum number of allowed login attempts before account lockout, enhancing security by preventing brute force attacks. Add the Auth by UnifyApps node, select "`Update Max Login Failures`" option and provide below mentioned inputs.

**Inputs:** No specific input fields are required for this action.

**Output:** Returns updated login failure threshold settings, confirming the new security configuration and providing details about the lockout policy.

## Generate SAML Response

This action creates SAML authentication responses for single sign-on workflows, enabling integration with SAML-compatible applications. Add the Auth by UnifyApps node, select "`Generate SAML Response`" option and provide below mentioned inputs.

**Inputs:** No specific input fields are required for this action.

**Output:** Returns generated SAML response data, providing the XML response and authentication assertions needed for SAML-based single sign-on integration.

## Use Cases

**Enterprise Single Sign-On Management:** Organizations can automate the creation and management of identity providers across multiple applications, streamlining user access management and maintaining consistent authentication policies. For example, a company can use the Create Identity Provider action to automatically set up authentication for new SaaS applications, then use Fetch Identity Providers to monitor all configured authentication sources from a central dashboard.

**Automated Password Reset Workflows:** Support teams can implement automated password reset processes that trigger notifications, validate sessions, and complete password changes without manual intervention. The workflow would use Trigger Reset Password to initiate the process, Validate Reset Password Session to ensure security, and Reset Password to complete the change, all while sending automated notifications to users.

**Multi-Factor Authentication Integration:** Security teams can integrate MFA verification into existing workflows, ensuring additional security layers are enforced across automated processes. For instance, when users access sensitive data workflows, the system can automatically trigger Verify MFA, and if verification fails, use Re Trigger MFA to provide another authentication opportunity before denying access.
