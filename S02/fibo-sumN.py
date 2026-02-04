def fibosum(n):
    a = 0
    b = 1
    total = a + b
    if n == 1:
        return total
    count = 1
    while count < n:
        c = a + b
        a = b
        b = c
        count += 1
        total += b
    return total

# Main program
print("Sum of first 5 Fibonacci terms:", fibosum(5))
print("Sum of first 10 Fibonacci terms:", fibosum(10))
