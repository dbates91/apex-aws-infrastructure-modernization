# Apex — AWS Cost Management and Teardown Policy

> **Current state:** design only. No AWS resources have been provisioned from this project.

Apex will use a personal AWS account. Billing is Region-, service-, account-, and usage-dependent. **AWS Budgets notifications are alerts, not hard caps**. Do not rely on general free-tier assumptions; verify pricing and any account eligibility before using a service.

## Mandatory Phase 0 budget gate

- [ ] Confirm AWS Region, account free-plan/free-tier eligibility and applicable pricing.
- [ ] Audit existing resources in all relevant AWS Regions; separate Apex costs from other account usage.
- [ ] Check root MFA, least-privilege identity and billing access.
- [ ] Configure and actually verify budget thresholds and notification recipients, without revealing account details publicly.
- [ ] Obtain service-by-service cost estimate including hourly, per-GB, transfer, logs and idle resource charges.
- [ ] Set a limited lab window and a teardown checklist with explicit completion review.
- [ ] Defer NAT, ALB, RDS, ECR, endpoints, DNS and any other billable resources until approved.

## Cost-driver analysis

| Component | Charges to evaluate | Planned mitigation |
| --- | --- | --- |
| NAT Gateway | Hourly provisioned fee and per-GB processing; possible cross-AZ transfer | Prefer short runs; weigh a single-NAT budget lab vs per-AZ resilience or endpoints |
| Application Load Balancer | Hourly and LCU usage | Activate only during bounded tests; delete after |
| Public IPv4 / Elastic IP | Public IPv4 hourly fees including in-use allocations | Keep application/DB instances private; release unused IPs |
| EC2 | Instance runtime and instance type | Right-size and stop or terminate after testing |
| EBS | Volumes, snapshots, throughput/IOPS where applicable | Limit disks; remember stopped EC2 can still incur EBS charges |
| RDS | Compute, storage, snapshots, backups; Multi-AZ increases cost | Optional advanced phase; short tests and verified deletion |
| CloudWatch | Ingestion, retention, custom metrics, alarms, queries | Set retention, avoid verbose logs and dispose of unused alarms |
| Data transfer | Egress, cross-AZ, NAT and service-specific transfer | Evaluate architecture traffic paths and keep synthetic test data small |
| VPC endpoints | Interface endpoint hourly and per-GB fees; gateway endpoints differ | Compare endpoint vs NAT total cost; remove idle interfaces |
| CloudTrail / Flow Logs | Data events, destinations and log ingestion/storage | Scoped telemetry and time-bounded retention |
| Route 53 / ACM | Hosted zones, DNS requests, domains; certificate type costs vary | Defer custom domain and paid features until justified |
| Docker/ECR/ECS | ECR storage/transfer, Fargate runtime, image pulls | Run Docker locally first; explicitly clean up cloud artifacts |
| Terraform state backend | S3 storage/requests/versioning, optional KMS | Encrypt, restrict and review before enabling |

Price references: [AWS VPC pricing](https://aws.amazon.com/vpc/pricing/), [EC2](https://aws.amazon.com/ec2/pricing/), [ELB](https://aws.amazon.com/elasticloadbalancing/pricing/), [RDS](https://aws.amazon.com/rds/pricing/), [CloudWatch](https://aws.amazon.com/cloudwatch/pricing/), [AWS Pricing Calculator](https://calculator.aws/).

## Deployment variants

**Design only (current):** no Apex AWS charges.  
**Minimal lab (future):** limited scope, possibly not highly available; never market it as HA.  
**HA demonstration (future, optional):** two AZ app instances, ALB, optional per-AZ NAT or RDS Multi-AZ; estimate substantially higher costs and set short test windows.

## Teardown verification

1. Retain only sanitized evidence and authorized data.
2. Use reviewed teardown order respecting dependencies and Terraform state; never destroy resources without verifying the plan and scope.
3. Check EC2/ASG, ALB, NAT, endpoints, RDS, EBS, snapshots, public IPv4, ECS/Fargate, ECR, Route 53, CloudWatch, CloudTrail/Flow Logs, SNS and storage resources.
4. Verify relevant Regions show no leftover billable Apex resources; note billing-report delay.
5. Capture actual charge and teardown evidence in the tracker **only once observed**.

## Cost ledger — intentionally empty

| Date | AWS Region | Phase | Planned estimate | Actual charges | Resources removed? | Proof |
| --- | --- | --- | --- | --- | --- | --- |
| — | — | — | — | — | — | — |

