# Apex — Interview walkthrough notes

**Status:** outline for real project evidence, not a claim of deployed resources.

## 30-second intro
Apex is my personal AWS Cloud Engineering modernization lab for a fictional Linux service. I am progressively designing private compute behind a public load balancer across two AZs, with Terraform, IAM, SSM, CloudWatch and explicit cost controls. I document each decision, failure mode and verified result in GitHub.

## Technical deep-dive prompts
1. Explain the VPC `10.0.0.0/16` and public/app/DB CIDR allocation.
2. What routes allow the ALB to reach a private instance? Why can the app tier not accept internet-initiated SSH?
3. How can a private EC2 instance reach Systems Manager with NAT vs VPC endpoints, and what would each cost?
4. How would you debug an ALB unhealthy target and distinguish service failure from SG/route problems?
5. How do Terraform plans, modules, state, locks and drift review reduce configuration error?
6. Which checks verify IMDSv2, encryption, logging and least-privilege permissions?
7. What did you actually deploy, how did you verify it, and how did you tear it down?

## Evidence fields (complete only when verified)
- Live network/compute evidence: **Not yet available**
- Incident record: **Not yet available**
- Cost comparison: **Not yet measured**
- Measured recovery/availability: **Not yet tested**

Update this document to use *past tense only for work actually performed*.
