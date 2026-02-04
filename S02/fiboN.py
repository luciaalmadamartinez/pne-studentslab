def fibon(n):
    a = 0
    b = 1
    count = 0
    if n == 1:
        return a
    while count < n-1:
        c = a + b
        a = b
        b = c
        count += 1
    return c

# Main program 
print("5th Fibonacci term:", fibon(5))
print("10th Fibonacci term:", fibon(10))
print("15th Fibonacci term:", fibon(15))
