# Application — Planned Linux Web Workload

**Phase 3 — Not Started.** This directory will hold a small synthetic-data application supporting Linux/ALB/Docker labs.

## Application contract

- HTTP response for `/` identifying the sample application.
- `GET /health` returns `200` only when application process is ready.
- Configurable bind host and port, no committed secrets.
- Predictable process lifecycle suitable for `systemd`, EC2 user data (nonsecret), and later a container.
- Structured/sanitized logs with meaningful exit codes.

## Verification plan

Use localhost `curl`, then ALB target-health inspection when deployed; test controlled service stop/restart and alert behavior. Add tests as code is written; record actual results in the tracker. HTTPS is planned at ALB, not present yet.

