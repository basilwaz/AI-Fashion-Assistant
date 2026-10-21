import json
import threading
import unittest
from urllib.error import HTTPError
from urllib.request import urlopen

from src.server import make_server


class ServerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = make_server(0)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def get(self, path):
        with urlopen(self.base + path, timeout=3) as response:
            return response.read()

    def test_page_and_assets_are_served(self):
        self.assertIn(b'id="preferences"', self.get("/"))
        self.assertIn(b"outfitCard", self.get("/app.js"))
        self.assertIn(b"@media", self.get("/style.css"))

    def test_form_query_returns_expected_outfit(self):
        data = json.loads(self.get("/api/recommend?budget=70&style=casual&occasion=everyday"))
        self.assertEqual([row["name"] for row in data["outfits"]], ["Budget casual"])

    def test_invalid_and_missing_budget_return_400(self):
        for path in ("/api/recommend", "/api/recommend?budget=NaN"):
            with self.subTest(path=path), self.assertRaises(HTTPError) as caught:
                self.get(path)
            self.assertEqual(caught.exception.code, 400)
            self.assertIn("error", json.loads(caught.exception.read()))

    def test_empty_results_are_successful(self):
        self.assertEqual(json.loads(self.get("/api/recommend?budget=1")), {"outfits": []})

    def test_source_files_are_not_exposed(self):
        with self.assertRaises(HTTPError) as caught:
            self.get("/src/server.py")
        self.assertEqual(caught.exception.code, 404)
