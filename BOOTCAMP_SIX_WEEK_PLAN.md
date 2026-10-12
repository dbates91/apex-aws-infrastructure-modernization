# Apex — Six-Week Bootcamp Execution Plan

Apex is structured around **Learn → Build → Troubleshoot → Explain → Repeat**, targeting AWS Cloud Support and Junior CloudOps practical competency alongside AWS SAA-C03 study.

| Week | Core activities | Deliverable / evidence to produce |
| --- | --- | --- |
| 1 | Phase 0–1: account/budget audit, CIDR/VPC routes/SGs, Terraform fundamentals | Reviewed architecture; budget gate; a *verified* minimal networking lab or an accurately labeled design-only exercise |
| 2 | Phase 2: private AL2023, IAM roles, SSM, Linux service diagnostics | Sanitized SSM connection evidence, network inspection, systemd incident |
| 3 | Phases 3–4: web service, ALB, target health, ASG, Terraform module orchestration | Reproducible deployment, scoped plan, real health and scaling checks |
| 4 | Phase 5: Docker, image inspection, local health tests, optional approved ECR/ECS | Rebuilt container and traceable image test |
| 5 | Phases 6–7: CloudWatch/SNS, CloudTrail/Flow Logs design, automation, CI | Actual alert test results and read-only operational tools |
| 6 | Phases 8–10: incidents, recovery, cost reduction, case study and interview walkthrough | Incident records, measured costs (if deployed), sanitized evidence, finished engineering narrative |

## Scope controls

- Preserve the 11 phases in [PROJECT_ROADMAP.md](PROJECT_ROADMAP.md).
- **Move Terraform into Week 1** as a learning and source-control practice; Phase 4 remains the gate for full repeatable IaC.
- Production-inspired does not mean production traffic or a paid always-on environment.
- Multi-AZ RDS and ECS/Fargate are optional extensions.
- Phase status changes only after real evidence of tests or deployments, security/cost review and documented teardown.
- Start with the smallest affordable lab; don't provision NAT or ALB until clearly justified.

## Exit questions for every week

1. What problem did this design solve and why this service?
2. What alternatives did you reject and why?
3. What IAM, SG, encryption or data risks did you address?
4. What would it cost if left running, and how did you verify cleanup?
5. What failed, how did you isolate it and what validated the correction?
6. What exact commit, evidence and ticket prove the work?
7. Can you explain the outcome to an interviewer without reading your notes?
