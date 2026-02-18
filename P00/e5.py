from Seq0 import seq_count
from Seq0 import seq_read_fasta

genes = ["ADA", "FXN", "FRAT1", "U5"]
for gene in genes:
    filename = "sequences/"+gene+".txt"
    seq = seq_read_fasta(filename)
    print(gene, ":")
    print(seq_count(seq))
