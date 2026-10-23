# Troubleshooting and CloudOps Incident Lab

**Phase 8 — Controlled drills not started.** This directory contains an actual Phase 1 provisioning/configuration incident as well as templates for future controlled CloudOps drills.

- **[INC-001 — Unintended Local Zone subnet placement](INC-001-local-zone-subnet-placement.md):** AWS CLI discovery, Terraform filtering and replacement; actual Terraform apply succeeded; final AWS CLI/no-drift check pending. Also tracked in [GitHub issue #13](https://github.com/dbates91/apex-aws-infrastructure-modernization/issues/13).

Use **Verify → Scope → Inspect → Isolate → Resolve → Validate → Document → Prevent**.

Planned scenarios: ALB 5xx/unhealthy targets, SSM connection failures, VPC route mistakes, SG block, private DNS failure, `systemd` failure, failed image start, CloudWatch alarm, and Terraform drift. Record simulated versus actually reproduced incidents accurately; never present an invented outage as a live production incident.

Start from [the incident evidence template](INCIDENT_TEMPLATE.md).

