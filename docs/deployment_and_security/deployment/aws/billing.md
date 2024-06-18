# Billing

After the installation, the client will be billed for all the infrastructure costs plus the usage metrics describe in the offer.
Using a usage-based pricing model you will only pay for what you use.
The following metrics are calculated and sent to AWS in order to charge you at the current offer pricing:

- CPU / Hour
- Memory / Hour
- GPU / Hour

The following AWS services are mandatory for the platform to work and will be billed:

- VPC
- ACM
- Secrets Manager
- CloudWatch
- EKS
- EC2
- EFS
- RDS
- Cognito
- ECS
- Lambda

To check the infrastructure costs of the platform, you can use the AWS Cost Explorer and filter by the tag Environment = YData.
This will aggregate all the resources deployed by the platform.

## Cost Estimations

**YData Fabric** final cost can be estimated following the logic of a usage-based plan since it depends on your users and data. The following table provides
a guideline of how to compute the total cost for different usage scenarios based on the deployed infrastructure.

| EKS Nodes | Instance Type | vCPUs | Memory (GBi) | GPUs | Number of instances | % Usage/ CPU/Hour | % Usage/ Memory/Hour | % Usage/ GPU/Hour | Cost AWS/Hour | Cost AWS/Day | Cost YData/Hour | Cost YData/Day |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| System | t3a.2xlarge | 8 | 32 | 0 | 2 | 20 | 20 | 0 | $0.30 | $14.44 | $0.38 | $9.22 |
| CPU Micro (labs) | t3a.large | 2 | 8 | 0 | 1 | 40 | 40 | 0 | $0.08 | $1.80 | $0.10 | $2.30 |
| CPU Small (labs) | t3a.xlarge | 4 | 16 | 0 | 1 | 20 | 20 | 0 | $0.15 | $3.61 | $0.10 | $2.30 |
| CPU Medium (labs) | t3a.2xlarge | 8 | 32 | 0 | 0 | 0 | 0 | 0 | $0.30 | $0.00 | $0.00 | $0.00 |
| CPU Large (labs) | m5a.4xlarge | 16 | 64 | 0 | 0 | 0 | 0 | 0 | $0.69 | $0.00 | $0.00 | $0.00 |
| CPU Compute Micro (computing) | r5a.4xlarge | 16 | 128 | 0 | 1 | 20 | 20 | 0 | $0.90 | $21.70 | $0.64 | $15.36 |
| GPU Micro (labs) | g4dn.xlarge | 4 | 16 | 1 | 0 | 0 | 0 | 0 | $0.53 | $0.00 | $0.00 | $0.00 |
| GPU Compute Micro (computing) | g3.4xlarge | 16 | 122 | 1 | 0 | 0 | 0 | 0 | $1.14 | $0.00 | $0.00 | $0.00 |

The example above illustrates a scenario where the Micro and Small instances are used. It is also illustrated that despite the Nodes being available,
they're not necessarily being used, hence billed - only when the infrastructure is required and actually used, it is measured and billed accordingly.
