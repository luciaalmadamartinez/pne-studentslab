from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")


IP = "212.128.255.37"
PORT1 = 8080
PORT2 = 8081


c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)

print(c1.__str__())
print(c2.__str__())


s = Seq()
s.read_fasta("sequences/FRAT1.txt")


gene = str(s).replace(" ", "").replace("\n", "").upper()
s.strbases = gene

print(f"Gene FRAT1: {gene[:60]}...")


for i in range(10):
    start = i * 10
    end = start + 10
    fragment = gene[start:end]

    print(f"Fragment {i+1}: {fragment}")


    if i % 2 == 0:
        response = c1.talk(fragment)
    else:
        response = c2.talk(fragment)

