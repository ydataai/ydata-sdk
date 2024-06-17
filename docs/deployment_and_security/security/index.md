# Security

This section describes YData’s security measures to provide a best-in-class experience for its customers, ensuring not only a good product and
service but also risk management and compliance.

Visit ^^[YData's Trust page](https://trust.ydata.ai)^^ to check all the Policies, Controls and Monitoring in place.

## Hosting security
**YData** is not a cloud service provider, however, we use providers which are hosted on their data centers, such as *Google*, *Microsoft* and *Amazon Web Services*,
when the setup is not made on the customer premises. They are leading cloud infrastructure providers with top-class safety standards.
They are able to respond quickly to both operational and security, including well-defined change management policies and procedures to determine when and how
change occurs.

### Clouds compliance standards

=== "Google"

    - CSA
    - ISO 27018
    - SOC 3
    - ISO 27001
    - SOC 1
    - ISO 27017
    - SOC 2

=== "AWS"

    - CSA
    - ISO 27017
    - SOC 2
    - ISO 9001
    - ISO 27018
    - SOC 3
    - ISO 27001
    - SOC 1

=== "Microsoft Azure"

    - CSA
    - ISO 27017
    - ISO 22301
    - SOC
    - ISO 9001
    - ISO 27018
    - ISO 20000-1
    - ISO 27001
    - ISO 27701
    - WCAG

Both physical access perimeters and entry points are strictly controlled by professional security personnel. Authorized personnel must pass a minimum of two-step verification
to gain access to the authorized center floors.

## Corporate security

**YData** has applied internal security policies that are in line with the industry's ISO 27001 and SOC 2. We are regularly training our employees in safety
and privacy awareness, which protects technical and non-technical roles. Training materials are developed for individual roles so that employees can fulfill
their responsibilities appropriately.

- Two-step verification for all services is enforced
- Encrypted hard drives of our devices is enforced
- Hard password requirements and rotation is enforced

## Verification and Access Management

Users can log in via a secured Authentication provider, such as Security Assurance Markup Language, Microsoft Active Directory, Google Sign In or OpenID services.
All requests to any of YData’s APIs must be approved. Data writing requests require at least reporting access as well as an API key. Data reading requests
require full user access as well as application keys. These keys act as carrier tokens to allow access to the YData service functionality. We also use Auth0
in user identification. Auth0 can never save a password because the password is encrypted when the user logs in, and compares with AuthO's encrypted password
to see if they are using the correct password.

The user can change and save the password as they wish. The user can use all types of characters to strengthen his password.

## Certificate Management & Communications
All certificates are generated and used inside the Kubernetes cluster, using cert-manager. Exceptions for cloud providers for specific certificates
and described below.
Every component inside the cluster uses its own certificate, sharing the same issuer so all the components exchange encrypted communication between them.

=== "AWS"

    "During the deployment, a certificate is requested and provisioned by *Let’s Encrypt* to the specified domain."

=== "Microsoft Azure"

    "The public certificate is generated using the AWS Certificate Manager service."

## Protection of Customer Data

User uploaded information or data will be considered confidential, which is stored in encrypted form, separate from other networks, including the public network
if available. Data for a limited time without user request, not allowed to come out.
All data transmitted layer protection (TSL) and HTTP sent by users protected using Strike Transport Security (HSTS). The application is usable if encrypted
communication is compromised.
User uploaded data is not transferred from one data center to another. Encryption is used in many places to protect customer information, such as:
IS-266 with encryption at rest, incomplete encryption (PGP) for system backups, KMS-based protection for privacy protection, and GPG encryption.
Users can use the data stored for business or administrative purposes, but they have to go through many security levels, including multifactor authentication
(MFA).

## Secure Build Materials (SBOM)
To enhance transparency and facilitate security assessments, we provide access to Secure Build Materials (SBOM) for our products and services.
SBOM files offer detailed insights into the components, dependencies, and associated vulnerabilities within our software stack. These files enable stakeholders,
including customers, auditors, and security researchers, to evaluate the security posture of our offerings comprehensively.
For access to SBOM files and additional security-related information, please visit our Security Resources page at:
[Find more information here.](security_building_materials.md)

## Certification, Attestation and Framework
YData uses a frontend framework React (originally maintained by Facebook) which combines the use of unique user tokens to protect your users against
common threats such as cross-site scripting (CSS / XSS) and cross-site request fraud (CSRF / XSRF). This makes it impossible for the user to access data
from another user's account.

## Laws and Regulations
The cloud service providers used by YData are compatible with the General Data Protection Resolution (GDPR).
GDPR is working to expand its products, methods and processes to fulfill its responsibilities as a data processor.
YData's security and privacy teams have established a vendor management program that determines the need for YData to be approved when it involves third parties
or external vendors. Our security team recognizes that the company’s information resources and vendor reliance are critical to our continued activities
and service delivery. These spaces are designed to evaluate technical, physical and administrative controls and ensure that it meets the expectations of it and
its customers.
It is a monitoring service for infrastructure and applications. Our CCPA compliance process may provide additions so that our customers can fulfill their
obligations under the CCPA if there is access to personal data, while we make no plans to transfer, process, use or store personal information.

## Data Security
- No data ever leaves the costumer client cloud.
- All the data is stored using cloud specific services to ensure security, privacy and compliance with YData’s customers requirements.

## Data Encryption
The way YData’s customers communicate with the servers is through SSL / TLS connections, which are encrypted.
YData protects the servers where YData Fabric is deployed from DDOS, SQL injection and other fraudulent activities.
If one wants to interrupt the data transfer, one can only see a mixture of some characters, which is not possible to decrypt.
All data in databases is encrypted with industry standard AES-256.

## API Security
To use the API the user needs to have a *JWT* *token* that is automatically generated by Fabric for a specific user. The *token* is signed and encrypted
using a random key created during the deployment and only known by the service responsible for its provisioning.

## Availability and disaster recovery
When using one of the cloud providers, the data stored in the bucket and database is distributed and copied to different servers.
If a bucket or database fails, it is usually recovered from a different server without targeting other users.Databases are backed up on a daily basis and
can be restored if the software or server fails significantly. Backups are stored in various European and North American data centers (depending on the customer
location) for extra protection.
It is not possible for YData to recover individual customer information - if you delete something in your account, it will be permanently deleted, and we will
not be able to recover it.

## Monitoring
The functionality of our applications and databases is monitored 24/7 through in-built monitoring tools provided by Google, Azure and Amazon Web Services. Internal errors or failures of our various integrations trigger logins and notifications. This usually helps us to identify the problem very quickly and remedy the situation.

## Full disclosure policy
If something serious happens and your data is damaged as required by GDPR, we will disclose in full (such as a data breach).
Transparency is important to us and we will provide you with all the necessary information to properly assess the situation and potential impact.
So far no customer data has been compromised and we aim to keep it that way.
