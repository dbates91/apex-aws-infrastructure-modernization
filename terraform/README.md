# Terraform — non-deploying environment and draft modules

- [environments/dev](environments/dev/README.md): provider-only root; **no module calls, resources or state backend**.
- [modules/networking](modules/networking/README.md): draft resource definitions for a two-AZ VPC, route tables and scoped example security groups; **unattached to the dev root**.
- [modules/compute](modules/compute/README.md) and [modules/observability](modules/observability/README.md): design placeholders for later phases.

**Terraform begins as a learning tool in Week 1**; Phase 4 is the integration and repeatability gate. The project requires budgeting, approved AWS Region/AZs, endpoint/egress design, state management and teardown approval **before any apply**.

## Static validation commands (not yet claimed as run)

```bash
terraform fmt -check -recursive terraform
cd terraform/environments/dev
terraform init -backend=false -input=false
terraform validate
cd ../../modules/networking
terraform init -backend=false -input=false
terraform validate
```

CI will run equivalent static commands after workflow publication. The root intentionally declares zero AWS resources so accidental root-level `terraform apply` will not deploy Apex resources; **never use apply at setup**.

Use short-lived credentials when actually working with AWS. State files and variable-value files are ignored; commit `.terraform.lock.hcl` when dependency locks are produced in a reviewed local environment. Later select an encrypted, versioned S3 backend with locking, restricted IAM, change approvals and drift-review practice. Do not commit plans or state; never run unreviewed CI applies.
