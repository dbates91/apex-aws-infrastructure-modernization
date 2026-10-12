#!/usr/bin/env python3
"""Small synthetic HTTP app for Apex local/Linux/Docker health-check exercises."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from os import getenv

MAX_PORT = 65535
DEFAULT_PORT = 8080


class ApexHandler(BaseHTTPRequestHandler):
    server_version = "ApexSample/0.1"

    def do_GET(self):
        if self.path == "/health":
            code, payload, mime = 200, b'{"status":"ok"}\n', "application/json"
        elif self.path == "/":
            code, payload, mime = 200, b"Apex sample web application\n", "text/plain"
        else:
            code, payload, mime = 404, b"Not found\n", "text/plain"

        self.send_response(code)
        self.send_header("Content-Type", mime + "; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(payload)


def get_port() -> int:
    raw = getenv("PORT", str(DEFAULT_PORT))
    try:
        port = int(raw)
    except ValueError as exc:
        raise ValueError("PORT must be an integer") from exc
    if not 1 <= port <= MAX_PORT:
        raise ValueError("PORT must be between 1 and 65535")
    return port


def main() -> None:
    bind_host = getenv("HOST", "127.0.0.1")
    server = ThreadingHTTPServer((bind_host, get_port()), ApexHandler)
    print(f"Apex sample listening on http://{bind_host}:{server.server_port}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
