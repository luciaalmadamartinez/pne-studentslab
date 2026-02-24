class Seq:

    def __init__(self, strbases):
        self.strbases = strbases

    def __str__(self):
        return self.strbases

    def __len__(self):
        return len(self.strbases)


def print_seqs(seq_list):
    index = 0
    for sequence in seq_list:
        print(f"Sequence {index}: (Length: {len(sequence)}) {sequence}")
        index += 1


seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_list)