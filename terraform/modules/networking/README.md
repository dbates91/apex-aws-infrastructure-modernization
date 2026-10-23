# Draft Terraform networking module — source code only

**Important:** This is an **unattached, untested draft module** and is **NOT** the Terraform configuration used to provision the real Apex VPC/subnets. The working HCL and local state are on the user's Mac, awaiting a safe Git push. **Do not connect this module to `terraform/environments/dev` or apply it as a substitute for the working local resources:** doing so can create a second VPC and overlapping/different subnet tiers. Reuse would require an intentional refactor with resource address/state migration and a reviewed Terraform plan.

## Draft components

- VPC `10.0.0.0/16` (configurable), DNS support and hostnames
- Public `10.0.0.0/24` / `10.0.1.0/24`, private app `10.0.10.0/24` / `10.0.11.0/24`, private DB `10.0.20.0/24` / `10.0.21.0/24`
- Two explicitly supplied AZ names (different letters may map to different physical AZs across accounts)
- IGW and public default route; one private app and DB route table per AZ with **no default route**
- Two example security groups: future internet-facing ALB port 443; app port reachable only from the ALB SG, with **no app egress initially**.
- No NAT Gateways, SSM endpoints, ALB, instances, EBS volumes, RDS or public IPv4. Private instances won't reach Systems Manager until a separately reviewed egress design is implemented.

**Migration warning:** This draft uses public `10.0.0.0/24` and `10.0.1.0/24`, app `10.0.10.0/24` and `10.0.11.0/24`, and DB `10.0.20.0/24` and `10.0.21.0/24`. **The live network design instead uses** public `10.0.1.0/24` and `10.0.2.0/24`, and private `10.0.10.0/24` and `10.0.20.0/24`; optional DB subnets have not been allocated. Do not migrate/import or run an apply until the draft is reconciled, the local Terraform state is backed up/protected and any resource-address moves have been reviewed.

Static validation instructions:

```bash
terraform fmt -check -recursive terraform
cd terraform/modules/networking
terraform init -backend=false
terraform validate
```

This validates syntax/schema only. It does not demonstrate that an AWS environment has been created, is secure, or is highly available. An application and endpoint egress plan must be added in later phases.
