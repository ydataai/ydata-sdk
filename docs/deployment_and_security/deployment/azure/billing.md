# Billing
After the installation, the client will be billed for all the infrastructure costs plus the usage metrics describe in the offer.

Using a usage-based pricing model you will only pay for what you use. 

The following metrics are calculated and sent to Azure in order to charge you at the current offer pricing:

- CPU / Hour
- Memory / Hour
- GPU / Hour

The following *Azure services* are mandatory for the platform to work and will be billed:

- Virtual networks
- IP Address
- Private DNS Zones
- Container Registry
- Storage Account
- MySQL Server
- Deployment Scripts
- Kubernetes Services
- Key Vault
- Container Instances

To check the infrastructure costs of the platform, you can use the Azure Cost analysis (under the Cost Management + Billing service) and filter by the
created resource groups during the deployment. This will aggregate all the resources deployed by the platform.

## Cost Estimations

**YData Fabric** final cost can be estimated following the logic of a usage-based plan since it depends on your users and data. The following table provides
a guideline of how to compute the total cost for different usage scenarios based on the deployed infrastructure. 

| AKS Nodes | Instance Type | vCPUs | Memory (GBi) | GPUs | Number of instances | % Usage/ CPU/Hour | % Usage/ Memory/Hour | % Usage/ GPU/Hour | Cost Azure/Hour | Cost Azure/Day | Cost YData/Hour | Cost YData/Day |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| System | Standard_D8s_v3 | 8 | 32 | 0 | 2 | 30 | 30 | 0 | 0.4800 | 23.04 | 0.288 | 6.912 |
| CPU Micro (labs) | Standard_D2s_v3 | 2 | 8 | 0 | 1 | 50 | 50 | 0 | 0.1200 | 2.88 | 0.06 | 1.44 |
| CPU Small (labs) | Standard_D4s_v3 | 4 | 16 | 0 | 1 | 50 | 50 | 0 | 0.2400 | 5.76 | 0.12 | 2.88 |
| CPU Medium (labs) | Standard_D8s_v3 | 8 | 32 | 0 | 0 | 0 | 0 | 0 | 0.4800 | 0 | 0 | 0 |
| CPU Large (labs) | Standard_D16s_v3 | 16 | 64 | 0 | 0 | 0 | 0 | 0 | 0.9600 | 0 | 0 | 0 |
| CPU Compute Micro (computing) | Standard_D32s_v3 | 32 | 128 | 0 | 1 | 80 | 80 | 0 | 1.9200 | 46.08 | 1.536 | 36.864 |
| GPU Micro (labs) | Standard_NC6s_v3 | 6 | 112 | 1 | 0 | 0 | 0 | 0 | 3.8230 | 0 | 0 | 0 |
| GPU Compute Micro (computing) | Standard_NC6s_v3 | 6 | 112 | 1 | 0 | 0 | 0 | 0 | 3.8230 | 0 | 0 | 0 |

The example above illustrates a scenario where the Micro and Small instances are used. 
It is also illustrated that despite the Nodes being available, they're not necessarily being used, hence billed - only when the infrastructure is required and actually used,
it is measured and billed accordingly.
