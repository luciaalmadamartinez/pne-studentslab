from Seq1 import Seq

s1 = Seq()
s2 = Seq("TATAC")
s3 = Seq("AGCXTW")

print(f"Sequence: (Length: {s1.len()}) {s1}")
print(s1.count())
print(f"Sequence: (Length: {s2.len()}) {s2}")
print(s2.count())
print(f"Sequence: (Length: {s3.len()}) {s3}")
print(s3.count())