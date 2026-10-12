# Bash Operations

`preflight.sh` is a **local-only** tool-availability check; it does not access AWS or create resources.

Example future invocation from repository root: `bash scripts/bash/preflight.sh`.

Future lab scripts may inspect services, route tables or SSM agent status, but require scope, approvals and sanitized output.

