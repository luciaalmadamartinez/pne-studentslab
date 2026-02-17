from pathlib import Path

FILENAME = "sequences/U5.txt"

file_contents = Path(FILENAME).read_text()

separated_lines = file_contents.split("\n")
body = separated_lines[1:]
body_result = "\n".join(body)

print("Body of the U5.txt file:", body_result)