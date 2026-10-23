# Architecture Decision Records (ADRs)

Record meaningful design choices with an explicit status, alternatives, rejected options, cost/security impact, and evidence.

## Accepted lab decision

- [ADR-001 — Explicit regional Availability Zone selection](ADR-001-regional-availability-zones.md): Terraform's zone-type filter, reviewed subnet replacement and outstanding verification; documented after [INC-001](../troubleshooting/INC-001-local-zone-subnet-placement.md).

## Proposed future decisions

One NAT versus per-AZ NAT; NAT versus SSM VPC endpoints; short-lived RDS lab versus simulated DB dependency; EC2 ASG versus ECS/Fargate; Terraform local state learning versus a secure remote backend.

Use the [ADR template](ADR_TEMPLATE.md). An accepted **configuration decision** does not imply the full architecture is deployed or fully tested.

