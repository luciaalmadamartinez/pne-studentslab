score = float(input("Enter a score from 1 - 10:"))
if 9.0 < score < 10.0:
    letter = "A"
elif 7.0 < score < 8.9:
    letter = "B"
elif 5.0 < score < 6.9:
    letter = "C"
elif 3.0 < score < 4.9:
    letter = "D"
elif 0.0 < score < 2.9:
    letter = "F"
else:
    print("Wrong score, you must introduce a number from 1 - 10.")

print("Score", score, "->", letter)