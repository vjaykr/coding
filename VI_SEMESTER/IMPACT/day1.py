a = '2+3/2+4-8+3*45/32-25+3'
print(a)
print(eval(a))



# print('enter the month number')
# month = int(input())
# print('enter the year')
# year = int(input())

# def leap_chek(year):
#     if year % 4 ==0 & year % 100 != 0 or year %400 != 0:
#         return True
#     return False
# print(leap_chek(year))    

# def days_in_month(month,year):
#     if month == 2:
#         if leap_chek(year):
#             return 29
#         else:
#             return 28
        
    
    
    
# month=int(input("Enter the month:
# if
# year=int (input ( "Year :
# if and or year
# print( 'Days: 29')
# else:
# print( 'Days: 28')
# elif month in (1 3 S 7 8 12):
# print( 'Days: 31')
# elif month in (4,6,9,11):
# print( 'Days: 39')
# else:
# print( invalid inpu • )



# Function to reverse a given number 
# def reverse_number(num):
#     reversed_num = 0
#     while num > 0:
#         remainder = num % 10
#         reversed_num = (reversed_num * 10) + remainder
#         num = num // 10
#     return reversed_num

# # Input from user
# number = int(input("Enter a number to reverse: "))
# print("Reversed number:", reverse_number(number))


# Function to calculate the sum of digits of a given number
# def sum_of_digits(num):
#     total = 0
#     while num > 0:
#         total += num % 10
#         num = num // 10
#     return total

# # Input from user
# number = int(input("Enter a number to find the sum of its digits: "))
# print("Sum of digits:", sum_of_digits(number))




# class Solution:
#     def reverse(self, x: int) -> int:
#         sign = -1 if x < 0 else 1
#         x *= sign
#         reversed_x = 0
        
#         while x != 0:
#             reversed_x = reversed_x * 10 + x % 10
#             x //= 10
        
#         reversed_x *= sign
        
#         if reversed_x < -2**31 or reversed_x > 2**31 - 1:
#             return 0
        
#         return reversed_x

# # Test cases
# solution = Solution()
# print(solution.reverse(123))   # Output: 321
# print(solution.reverse(-123))  # Output: -321
# print(solution.reverse(120))   # Output: 21




def combined_function(name="Vijay", age=25, *subjects, city="Patna", **extra_info):
    # 1. Positional Arguments
    print(f"Hello {name}, you are {age} years old.")
    
    # 2. Default Arguments
    print(f"Hi {name}, you are {age} years old.")
    
    # 3. Keyword Arguments
    print(f"City: {city}")
    
    # 4. Variable Length Arguments (*args) - Subjects
    print("Subjects are:")
    for subject in subjects:
        print(subject)
    
    # 5. Keyword Variable Length Arguments (**kwargs)
    print("Extra Information:")
    for key, value in extra_info.items():
        print(f"{key}: {value}")
    
    # 6. Combining Positional and Default Arguments
    print(f"{name} is from {city}.")
    
    # 7. Combining Positional and Keyword Arguments
    print(f"Name: {name}, Age: {age}, City: {city}")
    
    # 8. Using *args and **kwargs together
    print("Subjects and Details:")
    for subject in subjects:
        print(f"Subject: {subject}")
    for key, value in extra_info.items():
        print(f"{key}: {value}")
    
    # 9. Function with *args and Default Arguments
    print(f"Name: {name}, Total Score: {sum(extra_info.values()) if extra_info else 0}")
    
    # 10. Complex Function Using All Types of Arguments
    print(f"Name: {name}, Age: {age}, City: {city}")
    print(f"Hobbies: {', '.join(subjects)}")
    for key, value in extra_info.items():
        print(f"{key}: {value}")
    
# Example usage:

combined_function("Vijay", 30, "Math", "Science", "History", city="Patna", job="Engineer", country="india")

print("\n")

combined_function("Vijay", 25, "Physics", "Chemistry", country="india")
