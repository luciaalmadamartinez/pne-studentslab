import socket
from Seq1 import Seq

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


PORT = 8080
IP = "212.128.255.104"


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))

ls.listen()

print("The server is configured!")

while True:
    print("Waiting for Clients...")

    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    else:
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()
        msg_final = msg.strip().split(" ")


        sequences = ["ACGT", "AUTCGT", "TGCGTA", "ATCGTTTA"]

        if msg_final[0] == "PING":
            print("PING command!")
            response = "OK!"
        elif msg_final[0] == "GET":
            print("GET command")
            number = int(msg_final[1])
            response = sequences[number]
        elif msg_final[0] == "INFO":
            print("INFO command")
            msg_seq = msg_final[1]
            s = Seq(msg_seq)
            base_count = s.count()
            response = f"Sequence: {msg_seq} "
            response += f"Length: {s.len()} "

            num_total = 0
            for base, value in base_count.items():
                num_total = sum(base_count.values())
                percentage = round((value / num_total) * 100, 3)
                response += f"{base} : {num_total} ({percentage} %) "
        elif msg_final[0] == "COMP":
            print("COMP command")
            msg_seq = msg_final[1]
            s = Seq(msg_seq)
            response = s.complement()
        elif msg_final[0] == "REV":
            print("REV command")
            msg_seq = msg_final[1]
            s = Seq(msg_seq)
            response = s.reverse()
        elif msg_final[0] == "GENE":
            print("GENE command")
            gene_name = msg_final[1]
            s = Seq()
            s.read_fasta(f"../sequences/{gene_name}.txt")
            response = f"{s.strbases}\n"
        else:
            response = ""
        print(response)

        cs.send(response.encode())

        cs.close()
