# Apex — Architecture Overview

**Target design only.** No Apex AWS network or application exists yet.

## Goal

Modernize a hypothetical Linux web application with secure tier separation, two Availability Zones, repeatable deployments, visibility, and explicit cost controls. The target VPC is `10.0.0.0/16`. The actual AWS Region, account, AZ identifiers, and final IP layout will be chosen at the Phase 0 design gate.

## Candidate network design

| Tier | AZ A | AZ B | Routing concept |
| --- | --- | --- | --- |
| Public | `10.0.0.0/24` | `10.0.1.0/24` | IGW for ALB; NAT gateways only if approved |
| Application | `10.0.10.0/24` | `10.0.11.0/24` | No direct inbound from internet; outbound via scoped NAT or endpoints |
| Database | `10.0.20.0/24` | `10.0.21.0/24` | No route to Internet gateway; private RDS subnet group |
 
CIDRs are non-overlapping **proposals**, not verified deployments. Route-table association, NACL defaults, IPv6 scope, endpoint DNS and AZ capacity are future validation tasks.

## Intended traffic paths

- Internet clients → Route 53 → HTTPS (443) ALB listener with ACM certificate → healthy targets on a private application port.
- ALB security group: narrow inbound HTTP redirect (optional) and HTTPS from the internet; outbound only to application target port.
- Application instance security group: inbound application port **from ALB SG**, not from `0.0.0.0/0`; outbound restricted to necessary destinations.
- DB SG (optional): inbound database port from **application SG** only; no publicly accessible RDS instance.
- Systems Manager: instance IAM role and SSM Agent with outbound network path. With no NAT, design interface endpoints for `ssm`, `ssmmessages`, and other services required by the chosen setup, including logging/KMS when applicable. Endpoint costs must be estimated.
- HTTPS requires a valid owned domain and certificate; these are future optional costs.
- ALB spanning two AZs and an ASG across AZs are an *availability design*, not demonstrated resilience.

## NAT tradeoff

Single NAT can be cheaper in small labs but creates single-AZ egress dependency and may incur cross-AZ transfer. NAT per AZ improves fault isolation but increases fixed hourly expense. Private subnets also can use suitable VPC endpoints, with service-specific hourly and per-GB charges. Determine the practical cost and security tradeoff before provisioning.

## Optional advanced services

RDS with private subnet group and encryption, possibly Multi-AZ; ECR and ECS/Fargate after local Docker evidence; CloudWatch metrics/logging, CloudTrail, VPC Flow Logs and SNS.

See [subnet and dependency checklist](networking-plan.md), [cost policy](../COST_MANAGEMENT.md), and [roadmap](../PROJECT_ROADMAP.md).

