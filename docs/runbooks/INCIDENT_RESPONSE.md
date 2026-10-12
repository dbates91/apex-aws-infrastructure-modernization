# Runbook — CloudOps Incident Response

**Status:** Draft; not exercised against Apex resources.

1. **Verify:** check if the reported symptom is real and whether test, staging or production-like lab is in use.
2. **Scope:** note affected service, Region, AZ, path, time window and expected behavior; avoid public secrets in notes.
3. **Inspect:** check CloudWatch evidence where configured, ELB target health, EC2 status, SSM reachability, `systemctl` and logs, VPC routes/SGs.
4. **Isolate:** compare healthy/unhealthy components and recent changes before changing anything.
5. **Resolve:** use the smallest reviewed change. Never blindly broaden ingress or IAM.
6. **Validate:** rerun health checks and confirm logs/alarms; record exact actual results.
7. **Rollback/escalate:** if unsuccessful, revert the scoped change and request appropriate operational help.
8. **Document and prevent:** fill incident template; create a preventive guardrail and interview summary.

Never assume a CloudWatch alarm, Trail event or VPC Flow Log exists until actually configured.

