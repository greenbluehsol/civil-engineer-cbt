import http.server
import socketserver
import os
import sys

PORT = 8080
WEB_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public")

class DualStackServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True
    daemon_threads = True

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WEB_DIR, **kwargs)

    def log_message(self, format, *args):
        sys.stderr.write(f"[{self.log_date_time_string()}] {format % args}\n")

if __name__ == "__main__":
    os.chdir(WEB_DIR)
    with DualStackServer(("", PORT), Handler) as httpd:
        sys.stderr.write(f"Serving at http://localhost:{PORT} (dir: {WEB_DIR})\n")
        sys.stderr.flush()
        httpd.serve_forever()
