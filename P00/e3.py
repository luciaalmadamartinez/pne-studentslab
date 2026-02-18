from Seq0 import seq_read_fasta
from Seq0 import seq_len

genes = ["U5", "ADA", "FRAT1", "FXN"]
for gene in genes:
    folder = "sequences/"
    file = gene + ".txt"
    filename = folder + file
    full_file = seq_read_fasta(filename)
    length = seq_len(full_file)
    print(file, ":", length)