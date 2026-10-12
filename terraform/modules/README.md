# Terraform reusable modules — planned

These module directories are **design placeholders**, not deployable modules. Define clear inputs, outputs, version constraints, tagging, and explicit resource ownership when Phase 4 begins.

- [networking](networking/README.md): VPC, subnet tiers, routing, NAT/endpoint decisions.
- [compute](compute/README.md): SGs, IAM instance profiles, AL2023 launch templates, ALB, ASG.
- [observability](observability/README.md): alarms, log retention, SNS, audit integrations.

Do not add billable infrastructure without Phase 0 account audit, costs and teardown approval.

