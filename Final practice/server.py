import http.server
import socketserver
import jinja2 as j
import urllib.parse import parse_qs, urlparse
from pathlib import Path
import termcolor
import http.client
PORT = 8080

socketserver.TCPServer.allow_reuse_address = True
class TestHandler(http.server.BaseHTTPRequestHandler):

    def read_html_file(self, filename):
        contents = Path("html/" + filename).read_text(encoding="utf-8")
        content = j.Template(contents)
        return content

    def do_GET(self):
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        print(arguments)

        file = self.path.strip("/")
        if file == "" or file == "index.html":
            filename = "html/index.hrml"
            with open(filename, "r", encoding="utf-8") as f:
                body = f.read()
            self.send_response(200)

        elif path == "/listSpecies":
            limit = arguments["limit"][0]

            i = 0
            dictionary = {}
            while i < limit:
                for specie in species:
                    if "common_name" in specie:
                        i += 1
                        dictionary += specie["common_name"]


