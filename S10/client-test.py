from Client0 import Client
import socket

while connection_count < 5:
    c = Client(IP, PORT)
    c.talk(msg)
    print(f"CLIENT: {connection_count} {client_ip_port}")



