# def print_numbers(n):
#     if n <= 10:
#         print(n)
#         print_numbers(n + 1)

# print_numbers(1)

# n = 2

# if n == 2 or n == 3:
#     print("n is 2")
#     if n == 3:
#         print("n  3")
#     else:
#         print("n issss 2")
# else:
#     print("n is neither 2 nor 3")


# def check_condition(x):
#     if x > 5:
#         print("x is greater than 5")
#     else:
#         print("x is not greater than 5")

# check_condition(10) 
# check_condition(3) 


def print_numbers(n):
    if n <= 10:
        print(n)
        print_numbers(n + 1)

def check_condition(x):
    if x > 5:
        print("x is greater than 5")
    else:
        print("x is not greater than 5")

print_numbers(1)
check_condition(10)
check_condition(3)x