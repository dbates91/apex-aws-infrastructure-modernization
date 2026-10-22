# Apex — 16-Week Cloud Support + Junior CloudOps Job Simulation

**Status:** 2026-10-21 proposed replacement for the topic-driven 16-week sequence. **Scope:** training blueprint; no cloud resources created. **Graduation target:** entry-level Cloud Support and Junior CloudOps *practical readiness*, not a guarantee of hiring or years of production experience. This document supplements, and does not misrepresent completed work in, PROJECT_TRACKER.md.

## The fictional workplace

**Apex Cloud Operations** is a fictional internal infrastructure team operating the Apex application. The student is a junior engineer handling a queue of work assigned by a simulated senior engineer (ChatGPT). There are two overlapping rotations:

- **Cloud Support Desk:** issue intake, reproduction, logs and metrics, Linux/network/IAM diagnosis, customer impact, updates, workarounds, escalation and ticket closure.
- **Junior CloudOps:** infrastructure health checks, approved Terraform changes, deployment, Linux administration, monitoring, automation, backup/recovery, cost checks, documentation and change handoff.

Simulated cases may represent different fictional customers/tenants, but actual AWS resources remain confined to approved, affordable sandbox deployments. Do not fabricate real customers, SLAs, outage numbers or production experience.

## The non-negotiable daily shift

One full training shift is approximately **2–2.5 hours** and can be split around work or exams:

1. **Shift handoff (10–15 min):** read the previous report; identify system condition, open incidents, cost exposure and queued requests.
2. **Operational checks (15–20 min):** inspect health, recent changes, alarms/logs, AWS cost/running assets using read-only evidence. When cloud resources are off, use cached sanitized artifacts or local simulations and label them.
3. **Assigned ticket (60–90 min):** clarify impact and scope; explain component WHY/HOW; investigate; propose change; receive approval before cost/destructive actions; implement; test.
4. **Validation and rollback (15–20 min):** prove actual service/system state, document tests, verify costs, remove temporary resources.
5. **Closure and communication (15–20 min):** concise customer/team update, incident/change record, Git commit or runbook entry as warranted, one-minute oral explanation.

On a tight day perform a **45–60-minute mini-shift** (handoff, 1 scoped task, verification, closure); schedule longer infrastructure builds on off days. Recurring activities are essential; don't treat each calendar day as introducing a brand-new technology.

## Hours and sequencing

**16 active apprenticeship weeks × 12–16 cloud hours/week = 192–256 cloud practice hours.** This is an instructional design target, not a published hiring threshold. The sequence requires sufficient practice; if only 2–4 hours are available during Security+ or A+ exam weeks, those are **onboarding/maintenance** and do not consume a full apprenticeship week. After November 10 shifts are unknown: update realistic weekly capacity without cutting Software Engineering to zero. If time cannot support the workload, extend the calendar rather than award mastery without evidence.

Each workweek has **five distinct ticket assignments**, plus an optional 2–4-hour off-day build/repair. The first assignment of each week is deliberately scoped; by the end the ticket descriptions provide symptoms and outcomes rather than commands. Terraform is introduced in Week 1 as source inspection, not deferred until after all AWS has been manually built.

## Work queue: 16 weekly rotations, 80 daily assignments

| Week | Monday — Inspect/plan | Tuesday — Configure/diagnose | Wednesday — Change/operate | Thursday — Break/fix | Friday — Validate/handoff |
| --- | --- | --- | --- | --- | --- |
| **1: Onboarding and audit** | APX-001 Repo/historical progress audit | Map dev root, module and state boundaries | AWS identity/Region read-only preflight, no secrets | Investigate “Terraform file = deployed resource?” false report | Write risk, budget and evidence handoff; oral review |
| **2: Linux support foundation** | Inspect RHEL filesystem/permissions | Triage bad directory ownership | Inspect processes and systemd services | Diagnose a failed local service via journald | Blind Linux permissions/service ticket and handoff |
| **3: Networking desk** | Draw packet path and subnet CIDRs | Investigate public vs private routes | Evaluate SG vs NACL vs host firewall | Fix simulated DNS/HTTP/port failure | Explain VPC isolation and evidence, no hints |
| **4: EC2/IAM/SSM** | Review EC2/EBS/instance profiles | Explain least-privilege role and trust | Establish approved AL2023 access using SSM | Diagnose “instance up but session fails” | Close EC2 access incident, verify no public admin ingress |
| **5: Terraform change window** | Read HCL/root/module and dependencies | Review terraform fmt/validate/plan locally | Apply minimal approved VPC change in disposable lab or conduct paper review | Diagnose wrong route/SG or plan surprise | Document resource state, costs, rollback/teardown |
| **6: Linux application operations** | Deploy local Python /health web service | Make a controlled systemd service | Inspect bind/port/logs and Linux networking | Stop service; diagnose HTTP failure with logs | Rebuild app service independently and document |
| **7: Load balancing and scaling** | Design ALB, targets, SG chain and cost | Review/listener/target-group health | Approved short-lived ALB/ASG demo or static simulation | Diagnose 502/unhealthy target (live or labeled local artifacts) | Explain replacement, AZ failure, cleanup |
| **8: Terraform ownership** | Review plan and state safety | Parameterize reusable network configuration | Controlled reviewed IaC change / state design | Identify config drift and safe reconciliation | Independently review a Terraform PR and rollback plan |
| **9: Monitoring desk** | Define actionable health/latency/error signals | Configure log collection and retention (local/live as approved) | Design/test alarm and notification | Triage symptom from CloudWatch-like metrics and logs | Produce incident timeline and dashboard handoff |
| **10: Storage and databases** | Analyze S3/EBS/RDS use cases and costs | Diagnose storage pressure/perms | Validate snapshot/backup restore in an approved small lab | Investigate DB reachability or credential/SG problem | Recover data/test restore and explain RPO/RTO assumptions |
| **11: Automation shift** | Specify Bash health-check requirements | Implement exit codes and error handling | Build Python read-only inventory with dry-run/tests | Debug broken automation and idempotence | Peer-review, test and document scripts |
| **12: Container support** | Build Docker image locally | Run env/ports/volumes/logs checks | Review ECR push permission/cost (deploy if approved) | Investigate crash-loop/port mismatch | Rebuild and explain container support runbook |
| **13: Security operations** | Audit IAM, logging, public exposure | Investigate an AccessDenied case | Patch/review a bounded IAM or OS change | Diagnose over-permissive SG/role scenario safely | Security/customer incident communication and follow-up |
| **14: Resilience and cost** | Compare single-AZ vs two-AZ failure impact | Review recovery/rollback and cost choices | Execute controlled failure or validated simulation | Diagnose multi-symptom application outage | Record real evidence, cost cleanup, after-action review |
| **15: Independent desk rotation** | Unhinted customer case: network | Unhinted incident: EC2/SSM/Linux | Unhinted change request: Terraform | Unhinted case: monitoring/application | Two-ticket mixed shift; handoff and escalation decision |
| **16: Final assessment week** | Cold-start design and bounded rebuild | Execute approved change and prove observability | Blind multi-layer incident shift 1 | Blind incident shift 2 plus customer updates | Blind incident shift 3, portfolio defense, readiness score |

An unapproved expensive lab is never mandatory. For ALB/NAT/RDS, a **genuinely executed** short-lived test is stronger evidence than a simulation; label design-only work and do not claim real operational verification. Graduation requires at least one actual approved AWS EC2/network deployment and troubleshooting cycle and actual Terraform provisioning/rollback or approved equivalent with real state; if these cannot be done safely, practical graduation is pending.

## Weekly score and deliverables

Every week closes with **one support case, one operations/change artifact, one incident or diagnostic investigation, one written handoff, and one verbal interview defense** (some tasks can satisfy multiple categories). Dated, sanitized GitHub evidence matters; commit count does not.

Ticket template: number; fictional customer/impact/severity; reported symptoms; known facts and access; requirements; expected cost/risk; hypotheses; commands/evidence; scope/isolation; approved change; validation; rollback; customer update; escalation rationale; root cause; preventative improvement; Git references.

Senior engineer support: Weeks 1–4 guided; 5–8 prompts and hints; 9–12 minimal hints; 13–16 incident intake only. One question/checkpoint at a time; require student-produced commands and reasoning. Review and grade actual output; no fictional successful runs.

## Depth contract

**Required:**
- Linux RHEL 10 to AL2023: files/permissions, packages, user/service/SSH-SSM workflows, journalctl, ss/ip/dig/curl, disk/log investigations, Bash.
- Networking: packet flow, CIDR/subnets, routes, IGW/NAT/endpoints decisions, SG/NACL, HTTP/TLS/DNS, security troubleshooting.
- AWS operations: EC2/EBS/IAM roles, SSM, VPC, S3 and RDS practical connectivity/design, ALB/ASG health and resilience, CloudWatch logs/alarms, CloudTrail basics, cost/cleanup.
- Terraform: HCL, root vs module, variables/outputs, init/fmt/validate/plan/apply/destroy guarded by approval, state security/locking basics, drift, safe change/rollback, at least one actual bounded deployment cycle.
- Docker: Dockerfile, local build/run/inspect/logs, ports/environment, troubleshooting; ECR basics.
- Automation: personally written and tested Bash health-check and Python read-only diagnostics with realistic failures.
- Professional behavior: prioritization, escalation, clear customer updates, change control, incident notes, security/cost accountability and architecture defense.

**Not required for this entry-level gate:** Kubernetes, advanced RHEL/RHCSA administration, complex Ansible or multi-account enterprise landing-zone implementation, deep RDS DBA, large-scale production traffic, full-scale disaster recovery, production-grade platform SRE, or perpetual paid HA infrastructure.

## Final operational examination

Three consecutive **uncoached** mock shifts with a total of **9–12 mixed cases** drawn from an unseen incident bank, plus a separate approved infrastructure change/rebuild, client-facing update and oral architecture defense. Scoring is in [ROLE_READINESS_SCORECARD.md](ROLE_READINESS_SCORECARD.md). Critical safety mistakes (secrets exposed, unapproved spending/destructive operations, dangerous public admin access, Terraform state damage) block passing regardless of score. Graduation decisions cannot be based on having an SAA/Terraform certificate, finishing weeks, or copied AI-generated solutions.

## Start here

Current first assignment remains [APX-001](TICKET_APX_001.md). It is read-only and requires **zero AWS spending**. Begin by inspecting the local Terraform version and the existing dev root; don't assume Terraform is installed on the RHEL machine.