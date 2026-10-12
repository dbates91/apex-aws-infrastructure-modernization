# Draft Terraform networking module — source code only

**Important:** This module now contains Terraform *resource definitions*, but **is NOT called by `terraform/environments/dev`**. It has not been applied, the infrastructure doesn't exist, and all network tests and costs are unverified.

## Draft components

- VPC `10.0.0.0/16` (configurable), DNS support and hostnames
- Public `10.0.0.0/24` / `10.0.1.0/24`, private app `10.0.10.0/24` / `10.0.11.0/24`, private DB `10.0.20.0/24` / `10.0.21.0/24`
- Two explicitly supplied AZ names (different letters may map to different physical AZs across accounts)
- IGW and public default route; one private app and DB route table per AZ with **no default route**
- Two example security groups: future internet-facing ALB port 443; app port reachable only from the ALB SG, with **no app egress initially**.
- No NAT Gateways, SSM endpoints, ALB, instances, EBS volumes, RDS or public IPv4. Private instances won't reach Systems Manager until a separately reviewed egress design is implemented.

Do not connect this module to an environment until Phase 0 audit, selected Region/AZs, IAM permissions, actual price evaluation, and teardown steps are approved.

Static validation instructions:

```bash
terraform fmt -check -recursive terraform
cd terraform/modules/networking
terraform init -backend=false
terraform validate
```

This validates syntax/schema only. It does not demonstrate that an AWS environment has been created, is secure, or is highly available. An application and endpoint egress plan must be added in later phases.
