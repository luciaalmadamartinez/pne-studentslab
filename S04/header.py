from pathlib import Path

FILENAME = "sequences/RNU6_269P.txt"

file_contents = Path(FILENAME).read_text()

separated_lines = file_contents.split("\n")
print("First line of the RNU6_269P.txt file:", separated_lines[0])
