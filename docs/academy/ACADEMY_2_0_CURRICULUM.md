# Apex — AWS Cloud Engineering Academy 2.0

**Effective:** 2026-10-21 · **Status:** Curriculum reference, not proof of proficiency · **Cadence:** mastery-based, not calendar-based

## Purpose and operating model

Become capable of independently designing, operating, automating, securing, troubleshooting and explaining production-inspired AWS infrastructure through Apex. Target Cloud Support / Junior CloudOps; deeper engineering competency follows. Keep **Personal Cloud** (software engineering) and the **Active Directory employment lab** separate.

**Every engineering ticket:** Requirements → Design → Explain → Implement → Verify → Troubleshoot → Document → Rebuild.

**Assessment gate:** User independently explains the architecture and failure modes; applies a bounded change; supplies real verification; diagnoses one break/fix; provides a sanitized runbook and rebuild. Reading instructions, a GitHub commit, a passing static check, and a Terraform plan alone do **not** demonstrate a deployed system.

## Verified baseline, 2026-10-21

- Repo contains architecture documents, cost safeguards, a draft **unattached** Terraform networking module, a dev root **without resource/module calls**, sample Python HTTP application, Dockerfile, tests and static CI workflows.
- No Apex AWS deployment has been verified. Phase 0 AWS billing/security inventory is unverified. All implementation phases remain as recorded in PROJECT_TRACKER.md.
- Prior hands-on familiarity with VPC/EC2/AWS CLI and RHEL 10 exists, but independent troubleshooting, IaC, IAM operations and deployment mastery need direct assessment.
- Do **not** invoke the draft networking module or run Terraform apply/destroy before account audit, cost estimate, security review and explicit approval.

## Dependency and competency map

1. **CLI and evidence:** shell, Git, AWS identity/Region, safe CLI flags, redaction → inspect systems without changing them.
2. **Linux and packets:** files, permissions, processes, systemd, logs, TCP/IP, CIDR, DNS and routes → diagnose Linux service vs network failures.
3. **AWS foundational control plane:** VPC/subnets, IGW/routes, SG/NACL, EC2/EBS, IAM instance profiles and SSM → design a reachable, securely administered server.
4. **Terraform adoption early:** HCL/provider/module/root separation, fmt/validate/plan, state discipline → make bounded, reviewable changes before broad IaC rollout.
5. **Applications and availability:** HTTP/health, ALB/targets, ASG, two AZs → troubleshoot 502/unhealthy-target and replacement scenarios.
6. **Storage and observability:** S3/EBS/RDS design, encryption, backups, CloudWatch/CloudTrail and alarms → detect, investigate and recover.
7. **Automation and packaging:** Bash/Python, Docker, ECR and optional ECS/CI with OIDC → repeat builds and operational checks.
8. **Operations:** security, DR, cost, incident tickets, drift, runbooks, rebuild → independent Cloud Support / Junior CloudOps defense.

A local RHEL 10 VMware lab is the default for affordable Linux exercises. Amazon Linux 2023 on EC2 is used for cloud-specific administration. ARM64 vs x86_64 image compatibility must be checked.

## Reference 16-week progression (not a deadline)

A learning week is a *unit of work*; adjust the start/end dates and advance only after practical evidence. Early weeks are light for Security+ / A+; work shifts after Nov 10 remain unknown. Estimated hands-on cloud time: **~90–140 hours across a 16-week reference** assuming ~2–4 hours/week initially and ~6–10 hours/week when capacity permits. Full mastery of every advanced objective may take **160–240+ hours** and a longer calendar; extend to 20–28 weeks if necessary.

| Week | Primary module(s) and supporting Linux | Apex milestone / assessment |
| --- | --- | --- |
| 1 (Oct 21–27) | M0 baseline; Git, filesystem, Terraform provider/root/module concepts | APX-001 read-only repo/source audit; no AWS spending |
| 2 (Oct 28–Nov 3) | M0 account and cost safety, M2 CIDR/subnet traffic flow; Linux ip/ss/dig review | Sanitized account-resource inventory; sketch private/public packet flow |
| 3 (Nov 4–10) | M1 Linux files/users/processes; M4 Terraform fmt/validate concepts | Local command evidence, safe Terraform inspection; exam-first |
| 4 (Nov 11–17) | M2 CIDR, SG/NACL/routes, VPC DNS; architecture decisions | Independently defend subnets/routes, review Terraform networking source |
| 5 (Nov 18–24) | M2 + M4: approved, bounded VPC IaC lab | Plan review, actual cost gate, evidence and teardown only if authorized |
| 6 (Nov 25–Dec 1) | M3 IAM role/instance profile/SSM/EC2/EBS | Trace SSM prerequisites and diagnose connection failure |
| 7 (Dec 2–8) | M1 + M3 systemd, journalctl, dnf, permissions, logs | Repeat local web-service admin and OS incident on AL2023 when approved |
| 8 (Dec 9–15) | M4 state, inputs/outputs, modules, drift | Explain safe Terraform lifecycle; distinguish existing/manual resources |
| 9 (Dec 16–22) | M5 HTTP, health endpoint, logs, secure application service | Operate Python app behind least-privilege Linux service |
| 10 (Dec 23–29) | M6 ALB target groups, ASG, launch templates, Multi-AZ | Time-bounded HA demo only if estimated and approved; 502 ticket |
| 11 (Dec 30–Jan 5) | M7 S3, EBS, RDS design, backups and encryption | Compare storage/recovery architectures; RDS optional and cost-gated |
| 12 (Jan 6–12) | M8 CloudWatch, log retention, CloudTrail, alerts | Validate one alert and incident timeline with evidence |
| 13 (Jan 13–19) | M9 Bash and introductory Python; command exit codes | Write/test health-check or safe inventory script independently |
| 14 (Jan 20–26) | M10 Docker, ECR, CI security fundamentals | Build and debug local container; ECR push optional and cost-approved |
| 15 (Jan 27–Feb 2) | M11 security, Well-Architected, resilience, costs, drift | Controlled failure test, recovery/runbook and bill review |
| 16 (Feb 3–9) | M12 capstone, mock support tickets and interview defense | Blind incident, IaC explanation, app/architecture demo and verified portfolio |

**Key design change:** Terraform appears in Week 1 as *reading/validating* existing source, not as a long prerequisite nor as unauthorized provisioning. Linux runs concurrently and transfers to EC2. AWS SAA scenarios map to each module, but exam preparation remains a separate parallel track. High-cost ALB, NAT, RDS Multi-AZ and ECS/Fargate features are optional/time-bounded, not minimum graduation requirements.

## Time allocation by period

### A. Oct 21–29: Security+ priority

- Security+: **3.5–4 hours on study weekdays**; exam appointment Oct 28/29 requires confirmation.
- A+ Core 1: **1–1.5 hours**; Personal Cloud / JS: **1–2 hours**; job search/interviews: **30–45 minutes**.
- Apex: **two 25–40 minute sessions across this exam-focused period**, for no-cost audit, explanations, local Linux/Terraform inspection only.
- These blocks amount to a heavy study day; on fatigue/obligation days, protect Security+ and do a 15–20 minute JavaScript continuity session, reducing other blocks. Include at least one lighter/recovery period.

### B. Oct 30–Nov 9: A+ intensive

- A+ Core 1: **3–4 hours/day**, adjusted to diagnostic performance.
- Software Engineering: **1–2 hours/day**.
- IT job applications / interview / AD lab: **~1 hour/day**.
- Apex: **three 45–60 minute sessions/week**, no major paid infrastructure. Keep November certification milestones and any already-booked A+ exam in view.

### C. Nov 10 onward: flexible work-compatible schedule

**Workday template:** 30–45 minutes Personal Cloud/JS minimum (60–90 if realistic); 30–45 minutes exam/targeted remediation; cloud work 30–60 minutes on **2–3 chosen weekdays**, not all workdays; job tasks 15–30 minutes only when required. Keep sleep and recovery.

**Off-day template:** 90–150 minutes concentrated Apex lab and verification, 60–120 minutes Personal Cloud, 45–90 minutes A+/SAA preparation if imminent, 30–45 minutes applications/AD as relevant; one recovery or lighter block.

A 6–10-hour weekly cloud workload after Nov 10 is **provisional** until actual shifts are known. Do not promise all modules in 16 weeks if available hours drop.

## Next 14 days: executable plan (Oct 21–Nov 3)

| Date | Primary priority | Secondary / Apex |
| --- | --- | --- |
| Wed Oct 21 | Security+ domain diagnostics + remediation; A+ Core 1; JS; job applications | Review Academy baseline; no cloud deployment |
| Thu Oct 22 | Security+ practice and error log; A+; JS; jobs | **Apex session 1 (25–40m): APX-001 repo/HCL inspection** |
| Fri Oct 23 | Security+ timed weak-domain questions; A+; JS; jobs | No Apex |
| Sat Oct 24 | Security+ practical/PBQ remediation; shorter A+; JS | Optional recovery; no Apex requirement |
| Sun Oct 25 | Security+ full readiness checkpoint; JS; targeted A+ | Recovery block; no Apex |
| Mon Oct 26 | Security+ weak-domain corrections; A+; JS; jobs | **Apex session 2 (25–40m): explain safe Terraform root and network module** |
| Tue Oct 27 | Security+ final review, PBQs, rest | No Apex |
| Wed Oct 28 | Security+ exam **if confirmed**; otherwise focused review | Short JS or rest |
| Thu Oct 29 | Security+ exam **if confirmed**; otherwise review transition | Exam/recovery; no Apex |
| Fri Oct 30 | Shift to A+ Core 1 diagnostic/weak domains; JS; jobs | **Apex session (45–60m): local Linux CLI and repo layout** |
| Sat Oct 31 | A+ hardware/networking practice; JS | Recovery / off-day; no Apex required |
| Sun Nov 1 | A+ timed scenario practice; JS | **Apex session (45–60m): CIDR/VPC diagram, no deployment** |
| Mon Nov 2 | A+ Core 1 remediation; JS; applications / AD | No Apex |
| Tue Nov 3 | A+ performance-based practice and error log; JS | **Apex session (45–60m): account-cost inventory planning** |

Move Security+ exam work according to actual appointment. November 10 is the stated orientation, not a verified work-shift pattern. Preserve A+ Core 1 readiness target around Nov 10 and actual booked exam date separately; don't assume an exam is taken merely because a target date arrives.

## Recurring weekly checkpoint

- **Explain:** articulate the design, packet/permission behavior and service alternatives from memory.
- **Build:** user performs one scoped ticket, not a copied end-to-end solution.
- **Verify:** real CLI/Console evidence, correct AWS Region/account, clean status/HTTP/test output where relevant.
- **Troubleshoot:** one controlled failure and a concise root-cause note.
- **Assess:** 1–3 interview/SAA scenarios asked one at a time.
- **Document:** sanitize outputs; update repository notes; *never* treat documentation or CI as proof of deployment.
- **Cost/security:** budget checked before any resource creation, no public administrative ingress, least privilege and explicit teardown.
- **Track:** skills independently demonstrated, unverified areas and next corrective assignment.

## Practical job-readiness exit rubric

An outcome must be **independently demonstrated** rather than inferred from certification, commits or repeated guided labs.

- Explain VPC traffic paths, SG vs NACL, DNS and instance role/SSM without notes.
- Use Linux shell, systemd, journald and networking commands to isolate an application incident.
- Inspect/author Terraform HCL, validate/plan, explain state and reconcile drift safely.
- Deploy a small application and verify health, logs, reachability and least privilege in an approved lab.
- Produce one working operational script with exit-code/error behavior and tests.
- Diagnose at least **five mixed, progressively less-hinted** incidents (e.g. instance access, HTTP 502, SG, Linux service failure, Terraform drift), with evidence and rollback.
- Explain cost, alternatives, security and operating tradeoffs of each major component.
- Rebuild a scoped environment and walk through it in a mock interview.
- Maintain truthful evidence and a public-safe portfolio narrative.

**Initial ticket:** [APX-001 — Read-only repository and Terraform safety audit](TICKET_APX_001.md).