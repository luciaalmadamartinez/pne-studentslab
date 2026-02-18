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
