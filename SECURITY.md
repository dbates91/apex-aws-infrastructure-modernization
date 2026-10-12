# Security and Responsible Disclosure Policy

Apex is an educational portfolio project; **no production customer service is operating**.

## Secrets and identity

Never commit AWS access keys, session credentials, Terraform state, tfvars containing secrets, private keys, passwords, tokens, connection strings, credentials from terminal history, or account numbers. Use short-lived AWS authentication with MFA, least-privilege IAM roles, EC2 instance profiles, and GitHub Actions OIDC **only if approved in a future phase**. Avoid long-lived IAM user keys. If credentials are exposed, revoke or rotate them immediately, review CloudTrail activity where available, and remove exposure from Git history as needed. A .gitignore does not protect secrets already committed.

## Network and data controls

Default private application and DB tiers; deny public SSH; allow only scoped security-group-to-security-group communications. Enforce IMDSv2 and encrypted EBS and RDS if deployed. Never put private data in logs or screenshots. Use synthetic records. Redact account IDs, identifiers, IPs, emails, domain ownership details and secrets from published evidence.

## Change safety

Require plan and cost review before deployment. Do not run Terraform apply in repository initialization. Avoid unsafe automatic applies in CI. Re-check policy on every architecture change; no public write access to storage or unrestricted IAM policies.

## Reporting

If you find an actual secret in this repository, do **not** open a public issue containing it. Revoke it immediately and contact the maintainer using a private GitHub channel.

