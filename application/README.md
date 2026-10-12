# Apex synthetic web application

**Implemented as source code; cloud deployment and runtime verification remain pending.**

`server.py` is a minimal standard-library Python HTTP service (not production-hardened) for Linux, ALB health-check and container exercises.

| Request | Expected result |
| --- | --- |
| `GET /` | 200, plain-text identification |
| `GET /health` | 200, JSON `{"status":"ok"}` |
| Other paths | 404 |

Start locally: `python3 application/server.py` (default `127.0.0.1:8080`). Test locally: `python3 -m unittest discover -s tests -p 'test_*.py' -v`. Configure `PORT` and `HOST` with explicit values; Docker uses `HOST=0.0.0.0` inside its isolated container.

**Note:** This process-level health endpoint verifies the HTTP handler responds; it does **not** prove database readiness, upstream availability, TLS correctness or production SLOs. TLS will later terminate at an ALB if deployed.
