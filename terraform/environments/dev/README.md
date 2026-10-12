# Dev — Safe starter root

This root configures only the AWS provider and a status output. **It has no resources, data sources, module calls, backend or deployed infrastructure.**

`terraform/modules/networking` contains proposed resource definitions but is **not invoked here**. Terraform validation of the module is separate and does not create infrastructure.

Do not wire the module into the root until the Phase 0 account audit, regional estimates, IAM/security review, egress/SSM design and resource teardown checklist are approved. Consult [roadmap](../../../PROJECT_ROADMAP.md).

Local static commands (examples, not observed results):

```bash
terraform fmt -check
terraform init -backend=false -input=false
terraform validate
```
