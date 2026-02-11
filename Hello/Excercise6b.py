def classify_triangle(a, b, c):
    if a == b == c:
        triangle = "Equilateral"
    elif a == b or a == c or b == c:
        triangle = "Isosceles"
    elif a != b != c:
        triangle = "Scalene"

    return triangle

side_1 = int(input("Enter side1:"))
side_2 = int(input("Enter side2:"))
side_3 = int(input("Enter side3:"))

print("Your triangle is:", classify_triangle(side_1, side_2, side_3))


