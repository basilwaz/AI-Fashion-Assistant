"""Local prototype server. Run from the repository with python -m src.server."""

import json
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

from src.recommendations import recommend


WEB = Path(__file__).resolve().parents[1] / "web"


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        request = urlsplit(self.path)
        if request.path != "/api/recommend":
            return super().do_GET()
        params = parse_qs(request.query)
        try:
            outfits = recommend(params.get("budget", [""])[0],
                                params.get("style", ["any"])[0],
                                params.get("occasion", ["any"])[0])
        except ValueError as error:
            return self.send_json({"error": str(error)}, 400)
        self.send_json({"outfits": outfits})

    def send_json(self, value, status=200):
        body = json.dumps(value).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def make_server(port=8000):
    return ThreadingHTTPServer(("127.0.0.1", port), partial(Handler, directory=str(WEB)))


if __name__ == "__main__":
    with make_server() as server:
        print("Open http://127.0.0.1:8000. Press Ctrl+C to stop.")
        server.serve_forever()
