# Deployment Records

**A VPC and four subnets have been applied through local Terraform for Apex (2026-10-22)**; a Local Zone placement issue was remediated with four subnet replacements. The final read-only AWS verification and Terraform no-drift plan are **not yet recorded**. See [INC-001](../troubleshooting/INC-001-local-zone-subnet-placement.md) and the [Phase 1 verification guide](NETWORK_VERIFICATION.md).

Use [the preflight and teardown checklist](DEPLOYMENT_CHECKLIST.md), then record the exact commands, versions, Region, sanitized outcomes, service charges and cleanup. The deployed Terraform configuration is still local and must be pushed safely. Never publish credentials, state, access tokens or sensitive identifiers.

