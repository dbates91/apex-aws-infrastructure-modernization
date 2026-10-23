# Apex Phase 1 — AWS Network Verification

**Status:** Procedure published; **commands have not been independently executed after the subnet-remediation apply**. Do not mark the remaining checkboxes as passed until the actual output has been inspected.

**Goal:** Verify that AWS resources match the intended Terraform configuration and that the correction in [INC-001](../troubleshooting/INC-001-local-zone-subnet-placement.md) actually produced standard regional AZ placements.

## 0. Environment and identity (read-only)

In the **local Apex repository** (not the provider-only root currently published on GitHub `main`):

```bash
cd ~/apex-aws-infrastructure-modernization/terraform/environments/dev
export AWS_PROFILE=apex-dev
export AWS_DEFAULT_REGION=us-west-2
pwd
aws sts get-caller-identity --query Arn --output text
```

Confirm the intended **non-root IAM identity**. Do not post the returned ARN or account ID in public evidence. Stop if it reports `root`, an expired session, or an unexpected profile.

## 1. Resolve the intended VPC and inspect it

```bash
aws ec2 describe-vpcs --region us-west-2 \
  --filters 'Name=tag:Name,Values=apex-dev-vpc' \
  --query 'Vpcs[].{ID:VpcId,CIDR:CidrBlock,State:State,IsDefault:IsDefault}' \
  --output table
```

**Expected:** Exactly one Apex VPC with `10.0.0.0/16` and `available` status. If more than one VPC has that tag, investigate before proceeding.

Set `VPC_ID` **locally** from the actual verified VPC identifier (not a guessed ID):

```bash
VPC_ID="paste-the-VPC-ID-you-just-verified"
```

## 2. Inspect actual subnet placements

```bash
aws ec2 describe-subnets --region us-west-2 \
  --filters "Name=vpc-id,Values=$VPC_ID" \
  --query 'Subnets[].{Name:Tags[?Key==`Name`]|[0].Value,CIDR:CidrBlock,AZ:AvailabilityZone,AZID:AvailabilityZoneId,State:State}' \
  --output table
```

**Expected:** `apex-public-a` → `10.0.1.0/24`, `us-west-2a`; `apex-public-b` → `10.0.2.0/24`, `us-west-2b`; `apex-private-a` → `10.0.10.0/24`, `us-west-2a`; `apex-private-b` → `10.0.20.0/24`, `us-west-2b`; all `available`, no `lax` zone placement.

- [ ] Actual post-remediation subnet output reviewed.
- [ ] All expected CIDRs, names and regional AZs match.
- [ ] No extra unintended subnet found in the Apex VPC.

## 3. Inspect Terraform's view

```bash
terraform fmt -check
terraform validate
terraform plan
```

**Expected:** Validation succeeds and the plan shows **No changes**. Investigate unexpected create, destroy or replace actions instead of approving them. Be aware that `terraform plan` may access AWS and that the actual local Terraform state must be retained; state files are **never** committed.

- [ ] `fmt` and `validate` passed locally.
- [ ] Post-remediation `terraform plan` shows no changes.
- [ ] Actual local `.tf` files and `.terraform.lock.hcl` are staged safely (state/secrets excluded).

## 4. Routing (perform only once routing is actually deployed)

```bash
aws ec2 describe-internet-gateways --region us-west-2 \
  --filters "Name=attachment.vpc-id,Values=$VPC_ID" \
  --output table

aws ec2 describe-route-tables --region us-west-2 \
  --filters "Name=vpc-id,Values=$VPC_ID" \
  --output json
```

Confirm **explicit** public subnet associations and `0.0.0.0/0` pointing to the VPC's IGW. Confirm private subnets have the intended **effective** route tables and no unauthorized default internet route. These are **future checks** until those resources are defined and applied.

- [ ] IGW attached and public route correct.
- [ ] Public A/B explicitly associated with correct route table.
- [ ] Private A/B route associations checked.
- [ ] Actual reachability tested from appropriate resources, once EC2 exists.

## Record an observation responsibly

For each command capture: UTC date/time, local Terraform commit hash (if committed), target AWS Region, expected result, observed result, pass/fail, and a sanitized snippet or text table. Redact account numbers, identifying ARNs, credentials and any sensitive details. Update [PROJECT_TRACKER.md](../../PROJECT_TRACKER.md) and the relevant incident report **only after** reviewing actual output.

**Boundary:** Running this checklist does not prove ALB health, NAT functionality, SSM access, high availability, security controls or uptime. Those require their own deployed systems and tests.
