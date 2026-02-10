def get_length(dna):
    length = 0
    while length < len(dna):
        length += 1
    return length

def count_bases(dna):
    a_count = 0
    c_count = 0
    g_count = 0
    t_count = 0
    i = 0

    for i in range(len(dna)):
        if dna[i] == "A":
            a_count += 1
        elif dna[i] == "C":
            c_count += 1
        elif dna[i] == "G":
            g_count += 1
        elif dna[i] == "T":
            t_count += 1
        else:
            print("You entered an invalid base, valid DNA bases are: A, C, G, T")

    i += 1
    return "A:", a_count, "C:", c_count, "G:", g_count, "T:", t_count

#MAIN PROGRAM
dna_sequence = input("Enter your DNA sequence:").upper()
print("The total length of the sequence is:", get_length(dna_sequence))
print("The total number of each base is:", count_bases(dna_sequence))