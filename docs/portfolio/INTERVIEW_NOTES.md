# Apex — Interview Walkthrough

**Project:** Independent AWS Cloud Infrastructure & Operations Engineering lab. This is **project experience**, not paid production work.

## 30-second introduction (what has been completed)

> Apex is my AWS infrastructure and CloudOps portfolio project, focused on provisioning and operating a future Linux web application through Terraform. So far I've provisioned a custom VPC and four /24 subnet resources and used the AWS CLI to inspect their placement. The initial subnets landed in Los Angeles Local Zones instead of the regional Availability Zones I wanted. I corrected the Terraform zone discovery filter, reviewed the replacement plan and successfully applied all four subnet replacements while keeping the VPC. I'm now building routing and will follow with private Linux compute, secure administration and monitoring.

**Evidence limitation:** Post-remediation AWS CLI and Terraform no-drift checks have not yet been supplied, and the applied local Terraform HCL has not yet been pushed to GitHub. Do not claim those checks as complete.

## 60-second incident narrative

**Requirement:** A `10.0.0.0/16` AWS VPC with four non-overlapping `/24` subnet resources, targeted across two standard regional AZs.

**Symptom:** A read-only `describe-subnets` response showed `us-west-2-lax-1a/b`, meaning Local Zone placement.

**Root cause:** The Terraform `aws_availability_zones` data source allowed all available zone types and selected the first two.

**Fix:** Restrict the filter to `zone-type=availability-zone`. Terraform correctly flagged subnet `availability_zone` as an immutable, replacement-forcing attribute. Plan: **4 create, 0 update, 4 destroy**, VPC unchanged. Apply: **4 added, 0 changed, 4 destroyed**.

**Lesson:** Do not equate a successful API deployment with architectural correctness. Verify infrastructure independently, then scope and review potential destructive changes before applying.

[Incident report](../troubleshooting/INC-001-local-zone-subnet-placement.md) · [Resume evidence](RESUME_EVIDENCE.md)

## Questions I should be able to answer

1. Why use `10.0.0.0/16` for the VPC? How many IPv4 addresses does a `/24` contain, and how many does AWS reserve?
2. What's the difference between an AWS Region, a regional Availability Zone and a Local Zone?
3. Why didn't `terraform validate` catch my Local Zone selection as an architecture error?
4. What do `+ create`, `-/+ replace` and `known after apply` mean in a Terraform plan?
5. How does `vpc_id = aws_vpc.apex.id` establish a resource reference and dependency?
6. What is Terraform state and why can't I delete, copy or publish it carelessly?
7. What makes a subnet functionally public instead of private?
8. How would I verify subnet placement, routes and effective associations using AWS CLI?
9. How will private EC2 instances reach Systems Manager without exposed SSH?
10. What must be tested before claiming load-balancer health, availability or recovery?

## Evidence gates

| Claim | Status |
| --- | --- |
| VPC and subnet Terraform apply completed | **Observed** |
| Unexpected Local Zone selection investigated and four subnets replaced | **Observed** |
| Corrected subnets independently verified through AWS CLI | **Pending** |
| Fresh Terraform no-drift plan | **Pending** |
| Applied HCL committed and pushed | **Pending** |
| Routed network, EC2/SSM, ALB, monitoring, CI/CD deployment | **Not deployed** |
| Real costs, measured uptime, production users | **Not measured** |

Only describe completed work in past tense. Scope other services explicitly as targets.
