"""Offline HTTP tests: no external network and no AWS access."""
from http.server import ThreadingHTTPServer
from pathlib import Path
import sys
import threading
import unittest
from urllib.error import HTTPError
from urllib.request import urlopen

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "application"))
from server import ApexHandler, get_port  # noqa: E402


class SampleAppTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), ApexHandler)
        cls.worker = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.worker.start()
        cls.base = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.worker.join(timeout=5)
        cls.server.server_close()

    def test_health_returns_json(self):
        with urlopen(self.base + "/health", timeout=3) as response:
            self.assertEqual(response.status, 200)
            self.assertEqual(response.headers.get_content_type(), "application/json")
            self.assertEqual(response.read(), b'{"status":"ok"}\n')

    def test_root_returns_text(self):
        with urlopen(self.base + "/", timeout=3) as response:
            self.assertEqual(response.status, 200)
            self.assertIn(b"Apex sample", response.read())

    def test_unknown_route_returns_404(self):
        with self.assertRaises(HTTPError) as err:
            urlopen(self.base + "/missing", timeout=3)
        self.assertEqual(err.exception.code, 404)

    def test_default_port_is_valid(self):
        # Cannot assume caller did not override PORT; validate its documented range.
        self.assertGreaterEqual(get_port(), 1)
        self.assertLessEqual(get_port(), 65535)


if __name__ == "__main__":
    unittest.main()
