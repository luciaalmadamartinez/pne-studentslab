from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# --- Server configuration
IP = "212.128.255.37"
PORT = 8081

c = Client(IP, PORT)

print(c)

# Genes to send
genes = ["U5", "FRAT1", "ADA"]

for gene in genes:
    print(f"Sending the {gene} Gene to the server...")

    # Create Seq object and load FASTA
    s = Seq()  # NULL sequence created
    s.read_fasta(f"sequences/{gene}.txt")

    sequence = str(s).replace(" ", "").replace("\n", "").upper()
    s.strbases = sequence


    response = c.talk(sequence)

    print(response)