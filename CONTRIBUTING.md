# Contributing to Apex

Apex is a personal educational cloud-engineering portfolio. Changes should be small, auditable and reversible. Open an issue describing the phase, expected outcome, estimated costs and acceptance tests before substantial resource changes.

1. Create a topic branch from `main`, and avoid committing secrets, Terraform state, personal AWS identifiers, or unsanitized screenshots.
2. Use the phase acceptance criteria in [PROJECT_ROADMAP.md](PROJECT_ROADMAP.md).
3. Run applicable local lint and format checks; write down actual results, not presumed passes.
4. Review security boundaries, least-privilege changes, and cost/teardown plan.
5. Open a PR with architecture reasoning, actual verification, risks and rollback steps.
6. Update [PROJECT_TRACKER.md](PROJECT_TRACKER.md) only with observed evidence. Unverified implementation belongs in **Needs Review**, not **Completed**.

Automatic deployments are intentionally not set up during repository initialization.

