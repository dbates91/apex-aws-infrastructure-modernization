# Apex — Cloud Support / Junior CloudOps Readiness Scorecard

**Role target:** Cloud Support Associate and Junior CloudOps Engineer. **Assessment:** independent practical ability. This is an *internal rigorous apprenticeship standard*, not an AWS hiring standard or certification exam.

## Weighted competency rubric (100 points)

| Domain | Weight | Mandatory evidence |
| --- | ---: | --- |
| Networking and connectivity diagnosis | **20** | Trace VPC/subnet/routes/SG/NACL/DNS/HTTP traffic; diagnose unfamiliar failure with command evidence |
| Linux/EC2/SSM troubleshooting | **15** | OS/service/logs/disk/permissions, private instance access, recovery verification |
| IAM/security and safe operations | **15** | Role/trust/policy analysis, least privilege, security risks, scoped action and safe cleanup |
| Terraform and change control | **15** | Read/write HCL, root/module boundaries, state, fmt/validate/plan, safe approved apply/rollback, drift |
| Monitoring, incident response, reliability | **15** | Alerts/logs/metrics, prioritization, root-cause process, failure/rollback, evidence |
| Docker and automation | **10** | Local container debug + personally written/tested Bash and Python scripts |
| Customer communication, documentation, escalation | **10** | Accurate updates, scoped escalation, runbook, evidence and technical explanation |
| **Total** | **100** | |

## Graduation conditions (all required)

1. **>= 85/100 overall** on the independent final assessment and **>= 80% of possible points in each competency domain**. Scores are based on performed tasks, not self-report.
2. **Three consecutive uncoached mock shifts** with **9–12 unseen cases total**, no more than ordinary documentation/tool references. Grading assesses evidence, efficient isolation, safe actions, verification, written updates, and judgment to escalate.
3. **No critical safety errors:** no exposed secrets, unauthorized public management ports, irreversible/unreviewed destructive changes, unexpected billable deployment, mishandled Terraform state, or claiming evidence that does not exist. Any such event is a fail requiring remediation and re-test.
4. **One real scoped AWS lab end-to-end**, approved and cost-gated: provision network/EC2, verify identity/SSM/app reachability where applicable, observe failure, recover, and verify cleanup. A static CI run or theory-only mock cannot satisfy this.
5. **One actual bounded Terraform lifecycle** in approved lab: authored resource/module changes, fmt/validate/plan review, actual controlled apply/state inspection/change/teardown or rollback, with sanitized evidence.
6. **At least 12 documented technical incident investigations** across Linux, network, IAM, app, AWS observability, Terraform and container categories, of which **at least 8** are solved independently with minimal or no hints; repeated identical failures don't count.
7. **At least 6 reviewed change requests**, **4 support/customer communications**, **2 scripts (Bash and Python)** personally implemented and tested, and **2 recovery/rollback demonstrations**.
8. Explain an unknown architecture and present Apex's security, cost, failure and design tradeoffs in a mock interview without reading a prepared script.

## Assessment method

- Ticket facts disclosed initially: symptom, time, impact, environment and available logs. Root cause hidden.
- Engineer chooses first investigation; instructor reveals outputs only for legitimate diagnostic commands or asks for user-provided genuine CLI output.
- Real cloud changes require explicit prior approval and cost/teardown plan. Simulated failures are labeled and isolated.
- Use the diagnosis pattern **Verify → Scope → Inspect → Isolate → Resolve → Validate → Document → Prevent**.
- Where an incident legitimately requires access you don't have, correct outcome can be triage + escalation, not unauthorized change.
- Keep a dated log of ticket ID, category, independent/hinted, time spent, severity, evidence path, score, reviewer feedback and remediation.

## Performance score on each case (10 points)

- Clarify symptom/business impact/priority and choose appropriate next step: 1
- Evidence collection and hypothesis-driven isolation: 3
- Root-cause analysis and correct scoped remediation/escalation: 2
- Validation plus rollback/security/cost awareness: 2
- Clear customer/team update and documentation: 2

Multiply/scaffold case and capstone scores as needed for the domain-weighted final rubric. A diagnosis with an invented command result scores zero for evidence and triggers an integrity review.

## Evidence ledger (to complete during training)

| Date | Ticket | Domain | Independence | Actual evidence | Score | Next remediation |
| --- | --- | --- | --- | --- | --- | --- |
| — | — | — | — | None verified | — | — |

## Readiness decisions

- **Not assessed:** required evidence missing.
- **Developing:** guided execution; does not independently meet all gates.
- **Interview-ready for scoped cloud-support roles:** can pass support-case gates and communicate/escalate; CloudOps/Terraform gate may still be pending.
- **Apprenticeship graduated — Cloud Support + Junior CloudOps practical target:** all criteria above met.
- **Not guaranteed:** ATS filters, experience requirements, clearance requirements, interviews and hiring remain independent. Never describe simulation as paid professional experience.

The first gate can be attained before Week 16 if evidence supports it; re-test weak areas without arbitrarily extending the rest of the curriculum.