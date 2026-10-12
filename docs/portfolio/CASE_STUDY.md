# Apex — Engineering Case Study

**Status:** Planned project, no cloud infrastructure deployed or measured.

## Problem

A fictional small Linux web application has manual configuration, unclear recovery behavior, limited telemetry and unpredictable cloud spend. Design a modern architecture and prove operational practices without assuming access to real production users.

## Proposed approach

Two-AZ private app architecture behind a public HTTPS ALB, SSM management instead of public SSH, Terraform modules, cost-gated infrastructure and CloudWatch/SNS incident response. The DB tier, NAT topology, private endpoints and container platform are deliberately decision-driven.

## Engineering decision register

| Topic | Options under review | Decision evidence |
| --- | --- | --- |
| Outbound access | One NAT, NAT per AZ, selected interface endpoints | [Architecture ADRs](../architecture-decisions/README.md); not selected |
| IaC management | Console exploration then reviewed Terraform | Root does not wire network module; no apply |
| Container runtime | Local Docker then ECR; optional ECS/Fargate | No deployed artifacts |
| Persistence | Synthetic/no DB vs RDS, optional Multi-AZ | Optional based on cost and goals |

## Verified evidence

| Milestone | Verified result | Evidence URL |
| --- | --- | --- |
| GitHub project initialization | Files published to main | [Initial foundation commit](https://github.com/dbates91/apex-aws-infrastructure-modernization/commit/ce7108714c0ce172eb73721c4f0056368030e9ef) |
| AWS network and instances | Not deployed | — |
| CI checks | Four GitHub jobs completed successfully; Checkov scan is **advisory**, not a blocking security pass | [First run](https://github.com/dbates91/apex-aws-infrastructure-modernization/actions/runs/38218409414) |
| Linux / containers | No deployment test yet | — |
| Recovery tests | Not performed | — |
| Spend and teardown | No Apex AWS usage measured | — |

## Incidents and learning

To be completed with real local or approved-cloud failure drills: symptom, hypotheses, logs, root cause, safe remediation, post-fix check and prevention.

## Interview walkthrough outline

**Problem → Architecture → Security and cost constraints → What I actually built → What broke → Evidence of fixing it → Tradeoffs and what I'd change.**

Do not claim production adoption, measured availability, certification completion, or live customer impact.
