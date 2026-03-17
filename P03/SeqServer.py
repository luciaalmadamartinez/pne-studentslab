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
        try:
            msg_raw = cs.recv(2048)
            msg = msg_raw.decode()
            msg_final = msg.strip().split(" ")

            sequences = ["ACGT", "AUTCGT", "TGCGTA", "ATCGTTTA"]

            if msg_final[0] == "PING":
                response = "OK!"

            elif msg_final[0] == "GET":
                number = int(msg_final[1])
                response = sequences[number]

            elif msg_final[0] == "INFO":
                msg_seq = msg_final[1]
                s = Seq(msg_seq)
                base_count = s.count()

                response = f"Sequence: {msg_seq}\n"
                response += f"Length: {s.len()}\n"

                num_total = sum(base_count.values())

                for base, value in base_count.items():
                    if num_total > 0:
                        percentage = round((value / num_total) * 100, 3)
                    else:
                        percentage = 0
                    response += f"{base}: {value} ({percentage}%)\n"

            elif msg_final[0] == "COMP":
                s = Seq(msg_final[1])
                response = s.complement()

            elif msg_final[0] == "REV":
                s = Seq(msg_final[1])
                response = s.reverse()

            elif msg_final[0] == "GENE":
                gene_name = msg_final[1]
                s = Seq()
                s.read_fasta(f"../sequences/{gene_name}.txt")
                response = f"{s.strbases}\n"

            else:
                response = "ERROR"

        except Exception as e:
            print("ERROR:", e)
            response = "ERROR"

        cs.send(response.encode())
        cs.close()