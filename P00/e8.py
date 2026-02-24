from Seq0 import seq_count
from Seq0 import seq_read_fasta
from Seq0 import most_bases

genes = ["ADA", "FXN", "FRAT1", "U5"]
for gene in genes:
    filename = "sequences/"+gene+".txt"
    seq = seq_read_fasta(filename)
    n = seq_count(seq)
    print("Base that appears most in", gene, "is:", most_bases(n))