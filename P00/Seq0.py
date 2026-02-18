from pathlib import Path
def seq_ping():
    print("Ok")

def seq_read_fasta(filename):

    file_contents = Path(filename).read_text()
    separated_lines = file_contents.split("\n")
    body = separated_lines[1:]
    body_result = "".join(body)

    return body_result

def seq_len(seq):
    return len(seq)

def seq_count_base(seq, base):
    count = 0
    for i in seq:
        if i == base:
            count += 1
    return count

def seq_count(seq):
    count_dict = {}
    i = 0
    for base in seq:
        if base not in count_dict:
            count_dict[base] = 1
        else:
            count_dict[base] += 1
        i += 1
    return count_dict

def seq_reverse(seq, n):
    new_seq = seq[:n]
    reverse_sequence = new_seq[::-1]
    return reverse_sequence