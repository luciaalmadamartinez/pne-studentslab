from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
from Seq1 import Seq

PORT = 8080


class TestHandler(BaseHTTPRequestHandler):

    sequences = ["ACGT", "AUTCGT", "TGCGTA", "ATCGTTTA", "GATTACA"]

    def do_GET(self):

        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path
        params = urllib.parse.parse_qs(parsed_path.query)

        try:

            # ---------------- PING ----------------
            if path == "/ping":
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()

                with open("html/index.html") as f:
                    content = f.read()

                response = content.replace("{{content}}", "OK! Server is alive")

            # ---------------- GET ----------------
            elif path == "/get":
                n = int(params["n"][0])
                seq = self.sequences[n]

                with open("html/get.html") as f:
                    content = f.read()

                response = content.replace("{{sequence}}", seq)

                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()

            # ---------------- GENE ----------------
            elif path == "/gene":
                gene = params["name"][0]

                s = Seq()
                s.read_fasta(f"sequences/{gene}.txt")

                with open("html/gene.html") as f:
                    content = f.read()

                response = content.replace("{{gene}}", s.strbases)

                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()

            # ---------------- OPERATION ----------------
            elif path == "/operation":

                seq = params["seq"][0]
                op = params["op"][0]

                s = Seq(seq)

                if op == "info":
                    base_count = s.count()
                    total = sum(base_count.values())

                    result = f"Sequence: {seq}<br>"
                    result += f"Total length: {s.len()}<br>"

                    for base, value in base_count.items():
                        perc = (value / total) * 100 if total > 0 else 0
                        result += f"{base}: {value} ({round(perc,2)}%)<br>"

                elif op == "comp":
                    result = s.complement()

                elif op == "rev":
                    result = s.reverse()

                else:
                    result = "ERROR"

                with open("html/operation.html") as f:
                    content = f.read()

                response = content.replace("{{result}}", result)

                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()

            # ---------------- INDEX ----------------
            elif path == "/":
                with open("html/index.html") as f:
                    response = f.read()

                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()

            # ---------------- ERROR ----------------
            else:
                with open("html/error.html") as f:
                    response = f.read()

                self.send_response(404)
                self.send_header("Content-type", "text/html")
                self.end_headers()

            self.wfile.write(response.encode())

        except Exception as e:
            print("ERROR:", e)
            with open("html/error.html") as f:
                response = f.read()

            self.send_response(500)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(response.encode())


def run():
    server = HTTPServer(("", PORT), TestHandler)
    print(f"Server running on port {PORT}...")
    server.serve_forever()


run()