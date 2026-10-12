# Network Design Review Checklist — Draft

**Do not interpret as an AWS resource inventory.**

| Question | Planned choice | Needs verification |
| --- | --- | --- |
| VPC CIDR | 10.0.0.0/16 | Region/account overlapping VPCs, peering/VPN plans |
| AZ strategy | Two AZs | Region and account AZ labels |
| Public subnet pair | 10.0.0.0/24 and 10.0.1.0/24 | Main/public route table associations |
| Private app pair | 10.0.10.0/24 and 10.0.11.0/24 | Route tables, outbound path |
| Private DB pair | 10.0.20.0/24 and 10.0.21.0/24 | No public routing; subnet group |
| Inbound path | Public ALB HTTPS only | Certificate/domain approval |
| Instance administration | Systems Manager (no open SSH) | SSM Agent, IAM policy, NAT/endpoints |
| Egress model | NAT per AZ vs one NAT vs endpoints | Projected hours, AZ risk, pricing |
| Logs | CloudWatch, CloudTrail, Flow Logs as justified | Retention, encryption, delivery and cost |

## Phase 1 verification plan

1. Confirm CIDRs and exact AWS Region/AZ selection.
2. Inspect VPC DNS support and DNS hostnames settings.
3. Map every route table to its associated subnets and explicitly test relevant outbound reachability.
4. Verify ALB SG → private app SG → DB SG rule references and deny public SSH.
5. Validate SSM connectivity without assigning a public IP to application instances.
6. Record actual evidence when deployed, then tear down according to the [cost checklist](../COST_MANAGEMENT.md).

**Observed results:** Not available; no deployment has occurred.

