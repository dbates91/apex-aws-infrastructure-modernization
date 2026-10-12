# Containerization — Docker, ECR, Optional ECS/Fargate

**Phase 5 — Not Started.** No image is built, pushed, scanned or deployed.

## Proposed workflow

- Create a minimal reproducible Dockerfile for the synthetic web app.
- Use an appropriate image user and avoid embedding credentials.
- Build, tag and run locally first; validate the HTTP `/health` endpoint.
- Inspect container logs, process exit codes, image layers and published port mapping.
- Scan images and pin base image versions/digests as appropriate.
- When budget approved: ECR repository, short-lived authenticated image push, retention/cleanup, optional ECS/Fargate deployment.
- Update deployment docs with observed evidence and command output after testing.

**Troubleshooting topics:** port mismatch, wrong health-check path, missing environment variable, bind address `127.0.0.1` vs `0.0.0.0`, container exit or incompatible architecture.

No container services will be provisioned during initial repo setup.

