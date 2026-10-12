# Local Docker learning sample; no image build or ECR push is claimed.
FROM python:3.12-slim

WORKDIR /app
RUN groupadd --system apex && useradd --system --gid apex --home-dir /app apex
COPY application/server.py /app/server.py
ENV HOST=0.0.0.0 PORT=8080 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
USER apex
EXPOSE 8080
CMD ["python", "server.py"]
