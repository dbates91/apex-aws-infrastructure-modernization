# Apex Terraform — Development Environment

**Repository state:** As of 2026-10-22, the **GitHub `main` version** of this folder is still a provider-only scaffold, containing `versions.tf`, `variables.tf`, `outputs.tf` and this README. **It is not the working configuration used for the AWS deployment.**

**Real lab state:** The user authored `main.tf` on a local `feature/apex-network-foundation` branch, successfully applied a `10.0.0.0/16` VPC and four `/24` subnet resources, and then replaced all four subnets to switch from unintended LAX Local Zones to regional AZs. Terraform apply succeeded; final AWS CLI and `terraform plan` verification has not been supplied. [Incident record](../../../docs/troubleshooting/INC-001-local-zone-subnet-placement.md).

## Current configured networking (local only)

| Resource | CIDR |
| --- | --- |
| VPC | `10.0.0.0/16` |
| Public A | `10.0.1.0/24` |
| Public B | `10.0.2.0/24` |
| Private A | `10.0.10.0/24` |
| Private B | `10.0.20.0/24` |

The `outputs.tf` on `main` still says scaffold-only and is **outdated** for the local deployed environment. It must be replaced with actual resource outputs in a reviewed code change.

## Safe next actions (run on the original Mac)

1. Use VS Code with the current local repo and inspect Git status and `git diff` before committing.
2. Confirm the AWS CLI/Terraform identity is a **non-root** identity in `us-west-2`.
3. Run [read-only network checks](../../../docs/deployment/NETWORK_VERIFICATION.md) and inspect a post-change `terraform plan`.
4. Commit and push the reviewed local resource configuration, provider lockfile and suitable documentation on the feature branch.
5. Bring the documentation updates on GitHub `main` into the feature branch **without overwriting local Terraform state or source**; open a PR and validate CI.
6. Add routing through an intentional, reviewed Terraform change only after source and state consistency are confirmed.

**Do not** wire in `terraform/modules/networking` yet: that draft defines a separate VPC and a different subnet layout and is not an import of existing resources. Never run `terraform destroy` to “reset” a state mismatch without an explicit and reviewed teardown plan.

The goal is a reproducible implementation with working evidence—not just a clean-looking repository.
