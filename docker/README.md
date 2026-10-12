# Docker learning track

**Status:** a Dockerfile is committed, but no successful container build, ECR push or AWS deployment is claimed.

The local container runs the synthetic Python sample as an unprivileged Linux user. From repository root:

```bash
docker build -f docker/Dockerfile -t apex-local:dev .
docker run --rm -p 127.0.0.1:8080:8080 apex-local:dev
# In another terminal:
curl -i http://127.0.0.1:8080/health
```

A second exercise should intentionally break `PORT` or the health route and inspect container logs and exit behavior. Pin the image digest, scan it, and enforce immutable tags before any real deployment. ECR and ECS/Fargate stay optional advanced phases gated by the AWS budget.
