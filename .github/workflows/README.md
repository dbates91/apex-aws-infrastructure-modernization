# Apex CI controls

`quality.yml` runs on `main`, pull requests and manual dispatch.

- **Blocking:** local Python unit tests, documentation-path checks, Bash syntax, Terraform formatting and validation of the unattached module, Gitleaks secret scanning.
- **Advisory initially:** Checkov static findings for Terraform source. Review findings before promoting this job to a hard security gate. This is not a guarantee that AWS resources are secure.
- **No deployment:** workflow has `contents: read` permissions, no AWS credentials, no cloud CLI and **no terraform apply/destroy**.

**Security caveat:** The networking module has draft IAM/network dependencies, no SSM egress, no VPC Flow Logs, and no resources actually deployed. Treat Checkov findings as work items, not as a passing security review.

Future CI extensions after verified development: Docker build/test, TFLint, policy-as-code exception workflow, deterministic provider lock files, SARIF reports, protected branches, reviewed OIDC read-only plans (not automatic apply).

Check actual [GitHub Actions runs](../../actions) before reporting tests as passed.
