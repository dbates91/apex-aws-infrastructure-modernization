# ADR-001 — Explicit Regional Availability Zone Selection

- **Date:** 2026-10-22
- **Status:** Accepted for the Apex networking lab; remediation Terraform apply completed, **final AWS CLI/no-drift verification pending**
- **Scope:** `us-west-2`, VPC `10.0.0.0/16`, four public/private `/24` subnets
- **Related:** [INC-001](../troubleshooting/INC-001-local-zone-subnet-placement.md), [network specification](../../architecture/networking-plan.md)

## Context

The original Terraform `aws_availability_zones` data source used only `state = "available"`. Selecting `names[0]` and `names[1]` unexpectedly returned `us-west-2-lax-1a` and `us-west-2-lax-1b` (Los Angeles Local Zones) instead of two standard regional AZs.

The lab needs ordinary regional AZ placement to exercise a consistent two-AZ application architecture and facilitate later AWS services. A successful Terraform apply alone was insufficient proof of this requirement.

## Decision

Constrain the data-source result to standard availability zones:

```hcl
data "aws_availability_zones" "available" {
  state = "available"
  filter {
    name   = "zone-type"
    values = ["availability-zone"]
  }
}
```

The subnet resource definitions continue referencing `names[0]` and `names[1]`; explicit review of the resulting AZ names and zone IDs remains mandatory.

## Alternatives considered

1. **Use the first two available entries without filtering:** Rejected; selected unintended Local Zones.
2. **Hard-code AZ names:** More predictable for one account but less adaptable across accounts and AZ-name mappings. May be useful if pinned placement and auditability become necessary.
3. **Filtered discovery with verified results:** Chosen for the guided development lab, accompanied by post-apply inspection.

## Consequences and evidence

The corrected Terraform plan showed **4 to add, 0 to change, 4 to destroy** (AZ changes force subnet replacement). The `apply` finished with the same counts and preserved the VPC. This was acceptable **only** because the affected subnets did not host application workloads.

**Not yet proven:** Final CLI `describe-subnets` showing regional placements and a fresh zero-diff Terraform plan. See [verification checklist](../deployment/NETWORK_VERIFICATION.md).

## Prevention

- Check AZ *type* and returned AZ identifiers before deployment.
- Review `terraform plan` for replacements and destructive blast radius.
- Independently query actual AWS resources after deployment.
- Avoid relying on incidental ordering in cloud API discovery without verification.
