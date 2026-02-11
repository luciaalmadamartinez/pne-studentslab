dna = "ATGCGATCGATCGATCGATCGA"

#How many times "ATC" appears:
i = 0
count = 0
while i < len(dna):
    if dna[i:i+3] == "ATC":
        count += 1
        i += 1
    else:
        i += 1

#RNA transcription:
transcribed_chain = dna.replace("T", "U")

#Final result:
print("The length of the string is:", len(dna))
print("The first five characters are:", dna[0:6])
print("The last three characters are:", dna[-3:])
print("Sequence in lower case:", dna.lower())
print("The substring 'ATC' appears", count, "times")
print("The RNA chain is:", transcribed_chain)