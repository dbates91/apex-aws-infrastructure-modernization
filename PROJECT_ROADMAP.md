# Apex — Official Development Roadmap

**Status (2026-10-22):** Phase 1 networking is **In Progress**: the VPC/four subnet Terraform deployments and INC-001 remediation have completed, but post-fix read-only verification, code push and routing remain pending. Other phases have not met their acceptance gates. **The [project tracker](PROJECT_TRACKER.md) is the authoritative implementation-status record.** Phases can span multiple study weeks; higher-cost services remain discretionary.

| Phase | Topic | Bootcamp week | Current status |
| --- | --- | --- | --- |
| 0 | Foundation / cost audit | 1 | Not Started |
| 1 | AWS networking | 1 | **In Progress — VPC/subnets deployed; routing pending** |
| 2 | EC2 / Linux / IAM / SSM | 2 | Not Started |
| 3 | Application / ALB / ASG | 3 | Not Started |
| 4 | Terraform IaC | 3 | Not Started as a full repeatability milestone; **basic Terraform deployments performed in Phase 1** |
| 5 | Docker / ECR | 4 | Not Started |
| 6 | CloudWatch / CloudTrail / logging | 5 | Not Started |
| 7 | Bash / Python automation | 5 | Not Started |
| 8 | CloudOps incident simulation | 6 | Not Started as a dedicated simulation phase; **actual configuration incident INC-001 completed at Phase 1** |
| 9 | Failure testing / recovery / cost | 6 | Not Started |
| 10 | Portfolio / interviews | 6 | Not Started |

## Phase 0 — Setup and guardrails

**Build:** finish repository initialization, document the business scenario and subnet topology, review AWS account root MFA/IAM billing protections, audit existing resources across Regions, record the planned Region and budget, estimate service costs, and define a test/teardown window. The AWS account audit is not performed by creating this repo.

**Verify:** review the account console and pricing; document actual regional estimates, alert settings, and approvals **privately**. Record a sanitized design review and risk assessment before anything billable starts.

## Phase 1 — VPC and networking

**Built so far:** `10.0.0.0/16` VPC and four subnets (`10.0.1.0/24`, `10.0.2.0/24`, `10.0.10.0/24`, `10.0.20.0/24`) via Terraform. Local Zone placement was corrected with a reviewed four-subnet replacement. **Remaining:** independently verify AZ placement/no drift, publish the local HCL, deploy IGW/public/private routes, review NAT/endpoints, and later security-group rules and optional DB subnet CIDRs.

**Verify:** start with [post-remediation network CLI checks](docs/deployment/NETWORK_VERIFICATION.md); then inspect routes, subnet associations, internet path and SG boundaries with real outputs **after those resources are deployed**, and assess isolation, cost, and teardown. [First incident](docs/troubleshooting/INC-001-local-zone-subnet-placement.md).

## Phase 2 — EC2, AL2023, IAM, SSM and Linux

**Build:** private Amazon Linux 2023 instance, least-privilege instance profile, SSM Agent/network path, encrypted EBS, IMDSv2, OS updates and users/groups permissions; systemd and log drills.

**Verify:** successful authenticated SSM session **without opening SSH**, instance role trust/policies, private IP placement, user/permission/process checks, and documented failure diagnosis.

## Phase 3 — Application, load balancing and scaling

**Build:** synthetic-data HTTP service with /health, ALB listener/target group, launch template, two-AZ Auto Scaling group and health checks; add ACM TLS and Route 53 only when domain/hosted-zone costs are approved.

**Verify:** real target health, app response, AZ placement, scale event, failure response, TLS when configured, and cleaned-up lab resources. Do not claim uptime percentages without measurements.

## Phase 4 — Terraform and reproducible infrastructure

**Build:** version-pinned AWS provider, variables and outputs, networking/compute/security modules, per-environment conventions, safeguarded state backend design and change review. Migrate deliberately from manually built learning resources when appropriate.

**Verify:** terraform fmt, init/validate/plan with an approved backend setup, plan review, actual repeatable provisioning and teardown only when authorized, and documented drift detection. State and secrets remain out of Git.

## Phase 5 — Docker and ECR

**Build:** minimal Dockerfile, locally built/tagged Linux web image, health behavior, minimal image privileges and scan/rebuild workflow; ECR push in a bounded AWS lab. ECS/Fargate is optional advanced deployment.

**Verify:** local run and /health, image inspect/scan, digest/tag traceability, ECR configuration when deployed, and cost cleanup.

## Phase 6 — Monitoring and auditability

**Build:** bounded CloudWatch metrics/log groups/alarms, SNS notification path, scoped CloudTrail configuration, and VPC Flow Logs as justified. Define log retention, encryption/access and expected alert conditions.

**Verify:** trigger real controlled signals, verify notification delivery, check log retention and scope. Record costs from actual use rather than inventing measurements.

## Phase 7 — Operations automation

**Build:** Bash preflight, Python config validation, AWS CLI read-only inventory or health scripts, idempotence checks and safe error handling; later consider GitHub Actions with OIDC and restricted permissions.

**Verify:** run scripts against known inputs; demonstrate nonzero failures, dry-run behavior, and no secret leakage.

## Phase 8 — CloudOps incident exercises

**Break / fix:** recreate misrouted private traffic, incorrect SG rules, failed SSM connectivity, stopped Linux service, unhealthy ALB target, unexpected instance replacement, and Terraform drift where safe.

**Verify:** for each ticket, capture symptom, scope, evidence, hypothesis, root cause, fix, post-fix check and preventative action in [docs/troubleshooting](docs/troubleshooting/README.md).

## Phase 9 — Recovery, resilience and optimization

**Test:** AZ/instance failure scenarios within lab limits, app service recovery, restore/rollback, optional database HA design, and measured billing comparison of NAT, interface endpoints, public IPs, idle EBS and RDS alternatives.

**Verify:** record dated outcomes, observed recovery intervals (if measured), rollback evidence, teardown and actual charges. Avoid fictitious SLOs.

## Phase 10 — Engineering portfolio and interview defense

**Deliver:** accurate architecture diagram, README, sanitized deployment evidence, module guide, ADRs, security/cost tradeoff matrix, runbooks, incident postmortems, technical interview summaries, and portfolio presentation.

**Verify:** links point to real artifacts, claims match deployment logs, no secrets, and can explain architecture, troubleshooting and cost choices from memory.

## Definition of done for every phase

- [ ] Document actual implementation and timestamp
- [ ] Explain design alternatives and decisions
- [ ] Review least-privilege permissions and attack surface
- [ ] Estimate and, when deployed, record actual spend and teardown
- [ ] Reproduce a scenario or document a realistic failure mode
- [ ] Supply repeatable checks with truthful results
- [ ] Update diagrams, tracker and supporting docs
- [ ] Write a 60–90 second interview-ready walkthrough

