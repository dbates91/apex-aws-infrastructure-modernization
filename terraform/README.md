# Apex — Terraform Infrastructure as Code

**Actual cloud deployment:** A VPC and four subnets have been provisioned using **local** Terraform configuration. **GitHub `main` does not yet contain that applied configuration.** See [network evidence](../docs/troubleshooting/INC-001-local-zone-subnet-placement.md) and [tracker](../PROJECT_TRACKER.md).

## Repository layout

- [`environments/dev/`](environments/dev/README.md): **GitHub `main` currently has provider settings and a stale scaffold output, not the applied VPC/subnet resources.** Actual `main.tf` exists only on the local `feature/apex-network-foundation` branch pending a reviewed push.
- [`modules/networking/`](modules/networking/README.md): **unattached draft**; CIDRs and resources do **not** represent the deployed configuration. **Do not attach or apply** it without a migration strategy: it creates a different VPC and subnet layout.
- [`modules/compute/`](modules/compute/README.md) and [`modules/observability/`](modules/observability/README.md): placeholders for later, not deployed.

## Safe engineering workflow

Use the local directory that actually contains Terraform state, not a fresh clone, when managing existing AWS resources:

```bash
cd ~/apex-aws-infrastructure-modernization/terraform/environments/dev
export AWS_PROFILE=apex-dev
export AWS_DEFAULT_REGION=us-west-2
aws sts get-caller-identity --query Arn --output text
terraform fmt
terraform validate
terraform plan
# terraform apply only after a reviewed and approved plan
```

Never run `terraform apply` against the provider-only dev root currently on GitHub expecting it to manage the already deployed network. Confirm non-root identity, exact AWS Region, existing local state and resource addresses before any changes.

Read-only [network verification guide](../docs/deployment/NETWORK_VERIFICATION.md) documents the evidence needed after the AZ placement correction.

## Versioning and state precautions

- **Never commit:** `terraform.tfstate*`, `.terraform/`, sensitive `.tfvars`, AWS credentials, secret-bearing plans/logs.
- **Commit:** relevant `.tf`, documented configuration, and `.terraform.lock.hcl` after reviewing the contents and staged diff.
- The state currently resides in the user's local Terraform working directory. A new clone **does not automatically know about existing managed resources**.
- When ready, migrate deliberately to protected remote state with locking, access controls and recovery/versioning; do not simply change the backend without migration.
- Separate `.tf` files in the same directory share one Terraform root module, but moving resources into a child module changes their addresses and may require `moved` blocks/state migration.
- CI validation and linting are **static**; GitHub Actions does not deploy AWS infrastructure.

**Current status:** Terraform resource provisioning and forced replacement have been exercised. Reusable modules, remote state, automated plans on live AWS and independent full rebuild are later competency milestones.
