def is_even_number(number):
    if number % 2 == 0:
        answer = "True"
    else:
        answer = "False"
    return answer

user_number = int(input("Enter a number:"))
print("The number you entered is even:", is_even_number(user_number))