# Automation and Operational Utilities

**Phase 7 — Not Started.** Bootstrap scripts are examples, not evidence of a completed automation phase.

- [bash](bash/README.md): local tool preflight and future AWS CLI operational checks.
- [python](python/README.md): local documentation integrity checks and future AWS API diagnostics.

Safety rule: scripts should default to read-only or dry-run, support explicit scope, return nonzero on errors, avoid raw credentials in arguments or logs, and never silently provision or delete cloud resources.

