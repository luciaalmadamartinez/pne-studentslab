from Seq0 import seq_reverse
from Seq0 import seq_read_fasta

folder = "sequences/"
file = "U5.txt"
full_file = folder + file
result = seq_read_fasta(full_file)
sequence_to_reverse = result[0:21]

print("the reverse sequence is:", seq_reverse(sequence_to_reverse, 20))