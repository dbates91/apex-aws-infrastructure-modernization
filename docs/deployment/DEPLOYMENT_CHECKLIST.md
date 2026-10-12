# Deployment / Teardown Checklist

**Template only — no checks are recorded as completed.**

## Before approval
- [ ] Identify exact approved AWS account/Region privately; confirm permissions and MFA.
- [ ] Review proposed resources, architecture, hourly/per-GB cost estimate, budget notifications, lifecycle/teardown time and owner.
- [ ] Inspect Terraform changes and/or exact console actions; confirm least privilege, encryption, private subnet/SSM connectivity, logging scope.
- [ ] Determine how to verify deployment without fabricated metrics.

## During deployment (future)
- [ ] Record timestamp, resource set and Git commit ID.
- [ ] Verify routes, security boundaries, SSM access, target health and app response with real evidence.
- [ ] Investigate any surprise billable resources or security warnings before proceeding.

## Cleanup and verification (future)
- [ ] Shut down/destroy only explicitly scoped, authorized Apex resources.
- [ ] Recheck ALBs, NAT, interfaces, public IPs, EC2, EBS, RDS, ASG, endpoint resources and dependent logs/storage/snapshots.
- [ ] Confirm no remaining project-related charges/resources across relevant Regions (billing reports can lag).
- [ ] Record actual costs/cleanup evidence and update tracker.

