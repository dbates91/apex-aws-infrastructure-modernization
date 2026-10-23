# Apex — Network Specification and Verification

**Version:** 2026-10-22 · **Region:** `us-west-2` · **Status:** VPC/subnets applied; subnet post-fix read-only verification and routing still pending.

## Addressing plan

| Component | CIDR | Intended placement | Status |
| --- | --- | --- | --- |
| VPC | `10.0.0.0/16` | Regional VPC | Terraform-created |
| Public A | `10.0.1.0/24` | Standard regional AZ `us-west-2a` | Subnet replacement apply succeeded |
| Public B | `10.0.2.0/24` | Standard regional AZ `us-west-2b` | Subnet replacement apply succeeded |
| Private app A | `10.0.10.0/24` | `us-west-2a` | Subnet replacement apply succeeded |
| Private app B | `10.0.20.0/24` | `us-west-2b` | Subnet replacement apply succeeded |
| Optional private DB subnets | TBD: reserve new, non-overlapping CIDRs | Standard regional AZs | Not designed/deployed |

Each `/24` block contains 256 IPv4 addresses, with five reserved by AWS. AZ names are account-specific aliases; verify returned physical zone IDs when planning cross-account alignment.

## Routing — still to build

| Route table | Intended association | Required IPv4 destinations |
| --- | --- | --- |
| Public | Public A and B | `10.0.0.0/16 → local`; `0.0.0.0/0 → Internet Gateway` |
| Private app | Private A and B | `10.0.0.0/16 → local`; **no default route initially** |
| Private app with approved outbound access | Private A and B | Add default route to a public NAT gateway (or use selected VPC endpoints for supported services) only after implementation/test |
| Optional DB | Future database subnets | Local VPC routes; no direct IGW route |

Public or private status depends on the subnet's **effective route table** and other addressing/security conditions, not the resource name. No connectivity tests can prove IGW/NAT routing until those resources exist.

## Actual incident: AZ selection

Original `aws_availability_zones` discovery included `us-west-2-lax-1a/b` Local Zones. Restricting `zone-type` to `availability-zone` led Terraform to plan four forced subnet replacements into `us-west-2a/b`. Apply succeeded: **4 added, 0 changed, 4 destroyed**, with no VPC replacement.

[INC-001 investigation and remediation](../docs/troubleshooting/INC-001-local-zone-subnet-placement.md)

## Required verification

- [ ] Inspect all four subnets via AWS CLI **after** replacement; confirm CIDRs, regional AZs, state and no stray Local Zone subnets.
- [ ] Confirm Terraform `plan` reports no drift.
- [ ] Commit and push the actual local Terraform HCL; verify state and sensitive files remain ignored.
- [ ] Review VPC DNS support, default networking resources and tags.
- [ ] After IGW and custom route tables are applied, inspect default routes and **explicit** subnet associations.
- [ ] After compute is configured, test connectivity and security group behavior with real endpoints; do not infer from route tables alone.
- [ ] Document cost/risk decisions for NAT, VPC endpoints and possible database subnets.

Use the exact read-only commands in [Network Verification](../docs/deployment/NETWORK_VERIFICATION.md). The full routing/compute milestones are pending.
