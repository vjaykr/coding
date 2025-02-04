def rectangle(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)

print(rectangle(5, 2))
print(rectangle_perimeter(5, 2))


    
for i in range(1, 9):
    print(" " * (8 - i) + "*" + " " * (2 * i - 3) + "*" * (i != 1))
for i in range(7, 0, -1):
    print(" " * (8 - i) + "*" + " " * (2 * i - 3) + "*" * (i != 1))

    
    