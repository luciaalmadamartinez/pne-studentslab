text = "  Hello, World! Welcome to Python Programming.  "

#Get stripped text:
stripped_text = text.strip()
#Get number of words:
split_text = stripped_text.split()
#Capitalize string:
capitalized_string = stripped_text.title()
#String joined by -:
final_string = "-".join(split_text)


print("Leading and Trailing spaces removed:", stripped_text)
print("The number of words is:", len(split_text))
print("Capitalized text:", capitalized_string)
print("The string starts with Hello:", stripped_text.startswith("Hello"))
print("The string ends with ing:", stripped_text.endswith("ing."))
print("The position of the word 'Python' is:", stripped_text.find("Python"))
print("The string joined by - is:", final_string)