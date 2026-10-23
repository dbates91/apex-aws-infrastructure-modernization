# Apex — Resume and Interview Evidence Ledger

**Status as of 2026-10-22:** The independent project has **real AWS VPC/subnet Terraform apply evidence** and one actual configuration incident. The final AWS CLI verification of subnet replacement and a post-remediation no-drift plan are **pending**; the working Terraform configuration is **local and not yet synchronized to GitHub**.

## Current accurate project positioning

**Apex — AWS Cloud Infrastructure & Operations Engineering**  
*Independent technical project, not paid professional employment.*

**Technologies exercised:** AWS VPC, AWS EC2 networking APIs, AWS CLI, Terraform, HCL, IPv4/CIDR, subnetting, regional Availability Zones, Git/GitHub incident documentation.

### Resume bullets — usable with appropriate project label

- **Provisioned** an AWS VPC (`10.0.0.0/16`) and four non-overlapping `/24` subnet resources using Terraform Infrastructure as Code as the foundation for a two-AZ application network.
- **Diagnosed** unintended AWS Local Zone placement with the AWS CLI, corrected the Terraform availability-zone discovery filter, reviewed an infrastructure replacement plan and **successfully applied** four subnet replacements while preserving the VPC.
- **Used** Terraform `fmt`, `validate`, `plan` and `apply` to manage incremental AWS network configuration, and documented the configuration incident with evidence, root cause, remediation and remaining verification steps.

**Be precise:** Four subnet replacements were applied, but **the final AWS CLI inspection of their new AZ placements is not yet supplied**. Do not claim completion of independent network verification until it is performed and recorded. Do not say the Terraform code is publicly reproducible until it has been committed and pushed.

## Interview story — actual troubleshooting

> In my independent AWS infrastructure lab, I defined a VPC and four subnet resources with Terraform. A read-only AWS CLI check revealed they had landed in Los Angeles Local Zones instead of the standard Oregon AZs I intended. I inspected the Terraform availability-zone data source, added a zone-type filter, reviewed a plan that replaced four subnets without changing the VPC, and successfully applied the update. The incident reinforced that a successful provisioning command doesn't guarantee the deployed architecture matches the design.

[Full INC-001 report](../troubleshooting/INC-001-local-zone-subnet-placement.md) · [issue #13](https://github.com/dbates91/apex-aws-infrastructure-modernization/issues/13)

## Missing evidence to earn stronger claims

- [ ] Post-remediation `aws ec2 describe-subnets` confirms intended CIDRs and `us-west-2a/b` placements.
- [ ] `terraform plan` reports no changes after remediation.
- [ ] Terraform `main.tf`, lock file and other relevant code are pushed and reviewed; no state or secrets committed.
- [ ] IGW and custom route tables deployed with proven associations and connectivity.
- [ ] A private Linux EC2 instance is deployed and accessible via a verified secure management path.
- [ ] A live application health endpoint is tested through the intended network and load balancer.
- [ ] Documented security controls, monitoring and failure-recovery tests.
- [ ] Demonstrated independent rebuild, peer/mentor code review and operational runbooks.

## Claims not supported yet

Do **not** claim: production or enterprise cloud experience; professional years of Terraform experience; a deployed NAT Gateway, ALB, ASG, RDS, SSM-accessible EC2 host, Docker/ECR, CloudWatch alarm, or CI/CD infrastructure deployment; production-grade security; tested high availability; cost savings; or measured uptime.

## Evidence links

- [Repository README](../../README.md)
- [Phase 1 project tracker](../../PROJECT_TRACKER.md)
- [Architecture and addressing](../../architecture/README.md)
- [Network verification procedure](../deployment/NETWORK_VERIFICATION.md)
- [Incident record](../troubleshooting/INC-001-local-zone-subnet-placement.md)
- [Engineering case study](CASE_STUDY.md)

Update this ledger only when completed work has **observed results**, source code and credible proof. Actual lab work can qualify for a resume **Projects** section, but never mislabel it as professional employment.
