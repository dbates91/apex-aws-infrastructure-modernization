# INC-001 — Subnets placed in unintended AWS Local Zones

**Date:** 2026-10-22  
**Environment:** Apex development, `us-west-2`  
**Classification:** Actual lab configuration error discovered during initial provisioning; **not** a production incident or intentional fault injection  
**Status:** Terraform remediation applied successfully; post-remediation AWS CLI and no-drift verification not yet captured  
**Issue:** [#13](https://github.com/dbates91/apex-aws-infrastructure-modernization/issues/13)  
**Related milestone:** [Phase 1, #2](https://github.com/dbates91/apex-aws-infrastructure-modernization/issues/2)

## Intended infrastructure

A Terraform-managed VPC (`10.0.0.0/16`) in Oregon with four non-overlapping `/24` subnets in **two standard regional Availability Zones**:

| Subnet | CIDR | Target AZ |
| --- | --- | --- |
| apex-public-a | `10.0.1.0/24` | `us-west-2a` |
| apex-public-b | `10.0.2.0/24` | `us-west-2b` |
| apex-private-a | `10.0.10.0/24` | `us-west-2a` |
| apex-private-b | `10.0.20.0/24` | `us-west-2b` |

## Detect and scope

After the first successful Terraform subnet deployment, an independent AWS CLI query showed that the subnets were in **Los Angeles Local Zones** (`us-west-2-lax-1a` and `us-west-2-lax-1b`). This did not satisfy Apex's intended regional two-AZ design.

Command used for discovery (substitute the live VPC ID as appropriate):

```bash
aws ec2 describe-subnets \
  --region us-west-2 \
  --filters "Name=vpc-id,Values=<YOUR_VPC_ID>" \
  --query 'Subnets[].{Name:Tags[?Key==`Name`]|[0].Value,AZ:AvailabilityZone,CIDR:CidrBlock,State:State}' \
  --output table
```

## Root cause

The Terraform data source requested all available zones without constraining their **zone type**. Indexing the first two `names` selected available Local Zones in this environment. Terraform had executed the desired configuration correctly; the configuration did not encode the architectural requirement precisely enough.

## Remediation (Infrastructure as Code)

Changed the data source to restrict results to standard AZs:

```hcl
data "aws_availability_zones" "available" {
  state = "available"

  filter {
    name   = "zone-type"
    values = ["availability-zone"]
  }
}
```

The existing subnet resources continued using `data.aws_availability_zones.available.names[0]` and `names[1]`; subnet CIDRs were unchanged.

## Observed results

1. `terraform fmt` ran successfully and `terraform validate` returned **Success! The configuration is valid.**
2. `terraform plan` proposed **4 to add, 0 to change, 4 to destroy**. For all four subnets, the AZ changed from `us-west-2-lax-1a/b` to `us-west-2a/b` and Terraform marked the change as **forces replacement**.
3. After reviewing the destructive scope, `terraform apply` returned **Apply complete! Resources: 4 added, 0 changed, 4 destroyed.**
4. The existing VPC was not proposed for replacement; no EC2 instances or other application workloads had been deployed in these subnets.
5. The Terraform output `deployment_status` still says scaffold-only. This output is stale and must be replaced with actual resource outputs in a subsequent code update.

**Evidence limitation:** Terminal output for the successful apply has been reviewed in the learning session. No post-remediation `describe-subnets` output or no-drift `terraform plan` result has yet been provided. Do not claim these checks passed.

## Remaining verification

- [ ] Run `aws ec2 describe-subnets` to confirm subnet CIDRs and AZs match the intended architecture.
- [ ] Run `terraform plan` and confirm **No changes**.
- [ ] Commit and push the actual `.tf` changes from the local `feature/apex-network-foundation` branch.
- [ ] Replace the stale Terraform `deployment_status` output with useful VPC/subnet ID outputs.
- [ ] Add IGW, route tables, and explicit associations; independently test effective routing before introducing controlled incidents.

## Lessons learned

- **Verify → Scope → Inspect → Isolate → Resolve → Validate → Document → Prevent.**
- A successful API call or Terraform apply does not prove the resulting network meets requirements.
- Explicitly filter discovered cloud resources by the characteristics the architecture needs.
- A subnet's Availability Zone cannot be altered in place: the required change causes destroy/create replacement.
- Before approving a destructive Terraform plan, confirm dependencies, blast radius, state, and whether workloads are attached.
- Avoid credentials, account identifiers, and unnecessary resource IDs in public documentation.

## 60-second interview explanation

"During my independent AWS Terraform lab, I built a VPC and four subnets, then discovered through the AWS CLI that Terraform had chosen Local Zones instead of standard regional Availability Zones. The available-zone data source was insufficiently constrained. I added a zone-type filter, reviewed the replacement plan for all four subnets, and applied the correction without replacing the VPC. That taught me why independent post-deployment verification and careful review of immutable resource changes are essential."

_This is independently performed lab work, not professional production experience._
