# Apex — Engineering Case Study

**Status:** First AWS network foundation applied 2026-10-22: VPC and four subnets through Terraform; post-remediation AWS CLI/no-drift verification and GitHub sync of the actual local HCL are pending. Application, NAT, ALB, ASG, RDS, monitoring and production operations remain unimplemented.

## Problem

A fictional small Linux web application has manual configuration, unclear recovery behavior, limited telemetry and unpredictable cloud spend. Design a modern architecture and prove operational practices without assuming access to real production users.

## Proposed approach

Two-AZ private app architecture behind a public HTTPS ALB, SSM management instead of public SSH, Terraform modules, cost-gated infrastructure and CloudWatch/SNS incident response. The DB tier, NAT topology, private endpoints and container platform are deliberately decision-driven.

## Engineering decision register

| Topic | Options under review | Decision evidence |
| --- | --- | --- |
| Outbound access | One NAT, NAT per AZ, selected interface endpoints | [Architecture ADRs](../architecture-decisions/README.md); not selected |
| IaC management | Terraform-first local engineering and AWS CLI verification | VPC and subnet apply completed via local `terraform/environments/dev` config; default-branch source has **not yet** been synced with the deployed HCL |
| Container runtime | Local Docker then ECR; optional ECS/Fargate | No deployed artifacts |
| Persistence | Synthetic/no DB vs RDS, optional Multi-AZ | Optional based on cost and goals |

## Verified evidence

| Milestone | Verified result | Evidence URL |
| --- | --- | --- |
| GitHub project initialization | Files published to main | [Initial foundation commit](https://github.com/dbates91/apex-aws-infrastructure-modernization/commit/ce7108714c0ce172eb73721c4f0056368030e9ef) |
| AWS networking (VPC, four subnets) | Terraform applies succeeded; Local Zone selection remediated (4 replaced). Final AWS CLI/no-drift verification pending; actual Terraform code is local, not yet pushed. | [INC-001](../troubleshooting/INC-001-local-zone-subnet-placement.md) | 
| EC2 instances | Not deployed | — |
| CI checks | Four GitHub jobs completed successfully; Checkov scan is **advisory**, not a blocking security pass | [First run](https://github.com/dbates91/apex-aws-infrastructure-modernization/actions/runs/38218409414) |
| Linux / containers | No deployment test yet | — |
| Recovery tests | Not performed | — |
| Spend and teardown | No Apex AWS usage measured | — |

## Incidents and learning

**INC-001 — unintended Local Zone placement:** Actual lab misconfiguration detected through AWS CLI: subnet data-source selection included Local Zones. Added a `zone-type=availability-zone` filter, reviewed a plan replacing all four subnets without changing the VPC, and applied successfully. [Read incident report](../troubleshooting/INC-001-local-zone-subnet-placement.md). Post-fix CLI inspection is still pending. Controlled failure drills remain future work.

## Interview walkthrough outline

**Problem → Architecture → Security and cost constraints → What I actually built → What broke → Evidence of fixing it → Tradeoffs and what I'd change.**

Do not claim production adoption, measured availability, certification completion, or live customer impact.
