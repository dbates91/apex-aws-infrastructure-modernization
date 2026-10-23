# Apex — Project Progress Tracker

**Tracking rule:** A live VPC and four subnets have been applied, but no phase is complete until implementation, independent verification, risk/cost review and evidence are recorded. Do not infer progress from file presence. [Network verification checklist](docs/deployment/NETWORK_VERIFICATION.md) · [Resume evidence](docs/portfolio/RESUME_EVIDENCE.md).

## Allowed statuses

- **Not Started:** implementation hasn't begun (default).
- **In Progress:** work is actively underway with a dated activity log.
- **Needs Review:** implementation is finished but verification, security, cost, or evidence review remains.
- **Completed:** all acceptance gates passed with dated proof.

| Phase | Scope | Status | Actual evidence / PR | Verified date |
| --- | --- | --- | --- | --- |
| [0](https://github.com/dbates91/apex-aws-infrastructure-modernization/issues/1) | Repository, architecture, account audit, budget | Not Started | — | — |
| [1](https://github.com/dbates91/apex-aws-infrastructure-modernization/issues/2) | VPC, subnets, routes, IGW, SGs | **In Progress** | VPC + four subnets: Terraform apply logs; [INC-001 remediation](docs/troubleshooting/INC-001-local-zone-subnet-placement.md). [CLI verification](docs/deployment/NETWORK_VERIFICATION.md), source push, IGW/routes/SG work still pending. | 2026-10-22 (apply observed; final CLI verification pending) |
| [2](https://github.com/dbates91/apex-aws-infrastructure-modernization/issues/3) | EC2, AL2023, IAM, SSM, Linux | Not Started | — | — |
| [3](https://github.com/dbates91/apex-aws-infrastructure-modernization/issues/4) | Web app, ALB, ASG | Not Started | — | — |
| [4](https://github.com/dbates91/apex-aws-infrastructure-modernization/issues/5) | Terraform and repeatable deployment | Not Started | — | — |
| [5](https://github.com/dbates91/apex-aws-infrastructure-modernization/issues/6) | Docker, ECR, optional ECS | Not Started | — | — |
| [6](https://github.com/dbates91/apex-aws-infrastructure-modernization/issues/7) | CloudWatch, CloudTrail, logs, alarms | Not Started | — | — |
| [7](https://github.com/dbates91/apex-aws-infrastructure-modernization/issues/8) | Bash/Python operational automation | Not Started | — | — |
| [8](https://github.com/dbates91/apex-aws-infrastructure-modernization/issues/9) | CloudOps incident simulations | Not Started | — | — |
| [9](https://github.com/dbates91/apex-aws-infrastructure-modernization/issues/10) | Recovery, failure tests, cost review | Not Started | — | — |
| [10](https://github.com/dbates91/apex-aws-infrastructure-modernization/issues/11) | Portfolio docs and interview presentations | Not Started | — | — |

## Phase evidence template

**Date / phase / status:** TBD  
**What was built and changed:** TBD  
**Architecture reasoning and alternatives:** TBD  
**Security decisions:** TBD  
**Expected / observed cost and teardown:** TBD  
**Symptom, investigation and remediation:** TBD  
**Verification command and truthful result:** TBD  
**Docs, sanitized screenshots, commit or PR:** TBD  
**60–90 second interview explanation:** TBD  
**Remaining risks / next action:** TBD

## Current immediate acceptance gates

- [ ] Capture read-only AWS subnet results after Local Zone remediation.
- [ ] Capture a no-drift Terraform plan against the original local state.
- [ ] Commit and push the actual local Terraform source; confirm state and credentials remain excluded.
- [ ] Validate custom IGW/public/private route tables only **after** deployment.
- [ ] Reconcile cost/security review and scope with Phase 1 requirements.

## Change log

| Date | Phase | What changed | Evidence | Outcome |
| --- | --- | --- | --- | --- |
| 2026-10-22 | 1 | Created VPC 10.0.0.0/16 and four /24 subnets via Terraform. Discovered unintended LAX Local Zone placement using AWS CLI; filtered standard AZs and replaced all four subnets. | [INC-001](docs/troubleshooting/INC-001-local-zone-subnet-placement.md), [GitHub incident #13](https://github.com/dbates91/apex-aws-infrastructure-modernization/issues/13) | Terraform apply succeeded; post-remediation CLI/no-drift check and actual Terraform code push pending |


## Repo-wide foundation verification (not phase completion)

- 2026-10-12: [First CI run](https://github.com/dbates91/apex-aws-infrastructure-modernization/actions/runs/38218409414) completed successfully across four jobs: Python offline unit tests/documentation/Bash syntax, Terraform formatting and validation, Gitleaks secret scanning, and an **advisory** Checkov run. Passing the advisory job does **not** mean every IaC policy check passed.
- The **2026-10-12 CI run** did not provision AWS resources. Separately, actual VPC and subnet provisioning and one configuration incident/remediation occurred **2026-10-22**, documented above. NAT/ALB/RDS, containers, endpoints, and full failure drills remain pending.
- Phase 1 is **In Progress**, not complete. Other phases have not met completion criteria; Phase 0's full AWS account audit and budget gate still need documented review.
