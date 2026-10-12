# Apex — Project Progress Tracker

**Tracking rule:** The repository and draft documents exist, but no phase is complete until its implementation, real verification, risk/cost review, and evidence have been recorded. Do not infer progress from file presence.

## Allowed statuses

- **Not Started:** implementation hasn't begun (default).
- **In Progress:** work is actively underway with a dated activity log.
- **Needs Review:** implementation is finished but verification, security, cost, or evidence review remains.
- **Completed:** all acceptance gates passed with dated proof.

| Phase | Scope | Status | Actual evidence / PR | Verified date |
| --- | --- | --- | --- | --- |
| [0](https://github.com/dbates91/apex-aws-infrastructure-modernization/issues/1) | Repository, architecture, account audit, budget | Not Started | — | — |
| [1](https://github.com/dbates91/apex-aws-infrastructure-modernization/issues/2) | VPC, subnets, routes, IGW, SGs | Not Started | — | — |
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

## Change log

| Date | Phase | What changed | Evidence | Outcome |
| --- | --- | --- | --- | --- |
| — | — | — | — | No verified implementation yet |


## Repo-wide foundation verification (not phase completion)

- 2026-10-12: [First CI run](https://github.com/dbates91/apex-aws-infrastructure-modernization/actions/runs/38218409414) completed successfully across four jobs: Python offline unit tests/documentation/Bash syntax, Terraform formatting and validation, Gitleaks secret scanning, and an **advisory** Checkov run. Passing the advisory job does **not** mean every IaC policy check passed.
- No AWS provisioning, NAT/ALB/RDS deployment, Docker image build, endpoint connection, GitHub Project board, or actual failure drill was verified in this CI run.
- All implementation phases remain **Not Started**; Phase 0's AWS account audit and budget gate are still pending.
