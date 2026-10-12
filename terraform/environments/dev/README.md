# Dev — Non-provisioning Terraform Scaffold

This directory intentionally contains **provider configuration, variables and outputs only**, with **no AWS resource or data blocks**. It is not a deployed network, compute stack or a configured remote-state backend.

## Intended configuration

- `versions.tf`: Terraform and AWS provider constraints; uses ambient credentials.
- `variables.tf`: Region and tags.
- `outputs.tf`: explicit string explaining that no resources are defined.

For future local validation, inspect files first, then use:

```bash
terraform fmt -check
terraform init -backend=false
terraform validate
terraform plan
```

No tests have been executed or verified by merely initializing the GitHub repository. **Do not run terraform apply.** Later add module calls with justified dependencies, price estimates and verified output evidence.

