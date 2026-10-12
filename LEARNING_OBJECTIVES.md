# Apex — AWS Cloud Engineering Learning Objectives

**Core learning cycle: Learn → Build → Troubleshoot → Explain → Repeat.** The course prepares for AWS Solutions Architect – Associate concepts and practical CloudOps / Terraform fluency; it does not certify mastery or imply passed exams.

| Week | Build competency | Troubleshooting / architectural explanation |
| --- | --- | --- |
| 1 | VPC 10.0.0.0/16, subnetting, IGW, NAT, route tables, SGs, budget | Trace traffic between public ALB and private compute; isolate a bad route |
| 2 | Amazon Linux 2023, EC2, IAM instance profiles, SSM, CLI, systemd | Diagnose SSM unavailable, permission denied, DNS resolution or stopped service |
| 3 | HTTP /health, ALB, ASG and Terraform states, variables, modules | Identify why a target is unhealthy and assess unsafe plan changes |
| 4 | Dockerfile, image tags, local run, ECR strategy | Isolate health-check failure, container networking or bad image tag |
| 5 | CloudWatch, CloudTrail, Flow Logs, SNS, Bash and Python | Correlate metrics/logs with an alert and write a safe remediation |
| 6 | Failure drills, recovery, spend and teardown, interview pitch | Explain an actual incident and quantified results, if measured |

## Required deliverables for a completed phase

1. **Technical implementation:** actual configuration and repeatable steps.
2. **Architecture reasoning:** why this service and relevant alternatives.
3. **Security review:** IAM, encryption, trust boundaries and secret handling.
4. **Cost review:** approved estimate, actual costs if incurred, cleanup.
5. **Troubleshooting:** symptom, scope, evidence, root cause, corrective action.
6. **Operational verification:** dated output and accurate status.
7. **GitHub documentation:** README, architecture decision, runbook or incident.
8. **Interview readiness:** 60–90 second explanation without exaggeration.

## Practice method

First complete a guided build, then repeat with partial hints, then diagnose a broken state without step-by-step instructions, then rebuild from memory and document the difference. Never include fabricated screenshots, invented costs, claims of active AWS infrastructure, or false certification status.

