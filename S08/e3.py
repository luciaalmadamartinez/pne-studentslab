import socket

PORT = 8081
IP = "212.128.255.64"


while True:
    client_message = input("Enter your message:")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    s.send(str.encode(client_message))
    s.close()

    if client_message == "ADIOS":
        break
