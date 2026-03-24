import socket

IP = "127.0.0.1"
PORT = 8080

def process_client(cs):
    req = cs.recv(2000).decode()
    print(req)

    if "GET /info/A" in req:
        filename = "html/info/A.html"
    elif "GET /info/C" in req:
        filename = "html/info/C.html"
    elif "GET /info/G" in req:
        filename = "html/info/G.html"
    elif "GET /info/T" in req:
        filename = "html/info/T.html"
    else:
        filename = "error.html"

    f = open(filename)
    content = f.read()
    f.close()

    response = "HTTP/1.1 200 OK\r\n"
    response += "Content-Type: text/html\r\n\r\n"
    response += content
    cs.send(response.encode())

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()
print("Server running...")

while True:
    cs, addr = ls.accept()
    process_client(cs)
    cs.close()