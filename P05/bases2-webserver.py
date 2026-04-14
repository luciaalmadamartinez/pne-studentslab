from http.server import BaseHTTPRequestHandler, HTTPServer
import os

PORT = 8080


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        print("Request received:", self.path)

        if self.path == "/" or self.path == "/index.html":
            filename = "html/index.html"

        else:
            requested_file = self.path.lstrip("/")

            filename = os.path.join("html", requested_file)

            if not os.path.exists(filename):
                filename = "html/error.html"


        try:
            with open(filename, "r") as f:
                content = f.read()

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(content.encode())

        except:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"Internal Server Error")



server = HTTPServer(("localhost", PORT), MyHandler)

print(f"Server running on http://localhost:{PORT}")

server.serve_forever()