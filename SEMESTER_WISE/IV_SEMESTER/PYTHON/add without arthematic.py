def add_without_arithmetic(x, y):
    while(y):
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x
print(add_without_arithmetic(input("Enter first number: "), input("Enter second number: ")))

