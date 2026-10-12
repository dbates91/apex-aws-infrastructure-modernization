# Apex — Terraform Infrastructure as Code

**Current state:** starter configuration only; it declares **zero AWS resources**. No Terraform apply has been run as part of creating this repository.

## Layout

- [environments/dev/](environments/dev/README.md): non-provisioning development root, provider constraints, variables, outputs.
- [modules/](modules/README.md): documentation placeholders for future networking, compute and observability modules.
- Later modules may be composed into environments once the phase specifications and budget are approved.

## Local static workflow (future, on your workstation)

```bash
cd terraform/environments/dev
terraform fmt -check -recursive
terraform init -backend=false
terraform validate
terraform plan
```

**These commands are examples, not execution claims.** Terraform init downloads provider plugins; a plan can access AWS or evaluate data sources after resources are added, so inspect the code and use a securely configured identity. **Do not run `terraform apply` or `destroy` without an approved cost and teardown plan.** Keep Terraform state and plans out of Git; commit the provider lock file when created.

## State and provider security

A versioned, encrypted S3 backend with tightly scoped bucket permissions and native S3 state locking is a *future* design task; remote state, backend credentials, and locking are **not configured** here. Design for serialized changes and manual plan review. Do not commit `.tfstate`, plan files, private `.tfvars`, provider caches, private keys or credentials. Authenticate using short-lived identity and IAM least privilege, not access keys hardcoded in `provider` blocks.

## Drift practice

When AWS resources exist, compare configuration and real infrastructure using controlled `terraform plan -refresh-only` for observation and an ordinary plan for desired-state differences. Never uncritically apply drift fixes: investigate the manual change and business impact first.

