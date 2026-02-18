from Seq0 import seq_read_fasta
folder = "sequences/"
file = "U5.txt"
full_file = folder + file
result = seq_read_fasta(full_file)

print("DNA file:", file)
print("The first 20 bases are:", result[0:21])