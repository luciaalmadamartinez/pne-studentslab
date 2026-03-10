from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "192.168.1.45"
PORT = 8081

c = Client(IP, PORT)

print(c.__str__())


s = Seq()
s.read_fasta("sequences/FRAT1.txt")


gene = str(s).replace(" ", "").replace("\n", "").upper()
s.strbases = gene

print(f"Gene FRAT1: {gene[:60]}...")

for i in range(5):
    start = i * 10
    end = start + 10
    fragment = gene[start:end]

    print(f"Fragment {i+1}: {fragment}")

    # Send fragment to server
    response = c.talk(fragment)