# Apex GitHub Actions

- [quality.yml](quality.yml): **blocking** offline unit tests, Bash syntax, documentation, Terraform formatting/validation, and Gitleaks secret scanning; **advisory** Checkov Terraform security scan until its findings are reviewed and fixed.
- [tflint.yml](tflint.yml): TFLint language rules over the Terraform source tree, no account access.
- [Dependabot configuration](../dependabot.yml): proposes dependency/action updates as PRs; it does not automatically deploy infrastructure.

The workflows use read-only repository permissions. There are no AWS credentials, OIDC deployment permissions, Terraform applies/destroys, or cloud changes. CI can validate syntax and catch some policy errors; it does not prove the planned two-AZ infrastructure exists or works.

Use [GitHub Actions](../../actions) to see **actual** job outcomes. Promote Checkov to a hard gate after reviewing security findings and exceptions; additional AWS rules and image scans belong in later stages.
