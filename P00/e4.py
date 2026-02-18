from Seq0 import seq_count_base
from Seq0 import seq_read_fasta
bases = ["A", "C", "G", "T"]


#Gene ADA
gene = "sequences/ADA.txt"
sequence = seq_read_fasta(gene)
print("ADA:")
for base in bases:
    base_count = seq_count_base(sequence, base)
    print(base, ":", base_count)

#Gene FXN
gene = "sequences/FXN.txt"
sequence = seq_read_fasta(gene)
print("FXN:")
for base in bases:
    base_count = seq_count_base(sequence, base)
    print(base, ":", base_count)

#Gene FRAT1
gene = "sequences/FRAT1.txt"
sequence = seq_read_fasta(gene)
print("FRAT1:")
for base in bases:
    base_count = seq_count_base(sequence, base)
    print(base, ":", base_count)

#Gene U5
gene = "sequences/U5.txt"
sequence = seq_read_fasta(gene)
print("U5:")
for base in bases:
    base_count = seq_count_base(sequence, base)
    print(base, ":", base_count)

