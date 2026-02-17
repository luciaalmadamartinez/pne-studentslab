from pathlib import Path

FILENAME = "sequences/ADA.txt"

file_contents = Path(FILENAME).read_text()

separated_lines = file_contents.split("\n")
remove_header = separated_lines[1:]
result = "".join(remove_header)

print("Number of bases:", len(result))