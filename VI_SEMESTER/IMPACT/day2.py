#lamda Function

# def squre(x):
#     return x**2
# print(squre(5))



# squre = lambda x:x**2
# print(squre(10))





# p = 10000  # principle
# r = 5      # rate of interest per year
# n = 7      # number of years the money is invested
# t = 1      # number of times the interest is compounded per year

# compound_interest = lambda p, r, n, t: p * (1 + r / (100 * t)) ** (n * t)
# print(compound_interest(p, r, n, t))

# def calculate_total_interest(p, r, n, t):
#     total_interest = 0
#     for year in range(1, n + 1):
#         interest = compound_interest(p, r, year, t) - p
#         print(f"Year {year}: {interest:.2f}")
#         total_interest += interest
#     return total_interest

# total_interest = calculate_total_interest(p, r, n, t)
# print(f"Total interest over {n} years: {total_interest:.2f}")


# def Calculate_Compound_Interest(p,n,r):
#     print("start bal\t\tinterest\t\tend bal")
#     total = 0
#     x = r/100
#     tot=0
#     for i in range(1,n+1):
#         z_new=p*(1+x)**i-p
#         z_old=p*(1+x)**(i-1)-p
#         tot=tot+(z_new-z_old)
        
#         if(i==1):
#             print('{0:.2f}\t'.format(p),end=" ")
#             print('\t{0:.2f}\t'.format(z_new-z_old),end=" ")
#             print('\t\t{0:.2f}'.format(z_new+p))
#         else:
#             print('{0:.2f}\t'.format(p+z_old),end=" ")
#             print('\t{0:.2f}\t'.format(z_new-z_old),end=" ")
#             print('\t\t{0:.2f}'.format(z_new+p))
            
#     print("Total Interest: Rs {0:.2f}".format(tot))
#     p=int(input("Enter the principal amount: "))
#     n=int(input("Enter the number of years: "))
#     r=float(input("Enter the rate of interest: "))
# Calculate_Compound_Interest(10000,7,5)    


# 1. Find the Largest Palindrome in a List
# Question :
# Write a Python program to find the largest palindromic number in a list of integers.
# A palindrome reads the same forward and backward
# (e.g., 121, 3443).
# Algorithm:
# Input a list of numbers.
# Filter palindromic numbers:
# For each number in the list,
# Find the largest palindrome:
# If there are any palindromes,
# Output the result:
# Print the largest palindrome
# check if it reads the same forward
# find the maximum value.
# or indicate that no palindromes exist.

# def is_palindrome(num):
# 



# def largestpalindromechek(numbers):
#    palindrome = []
#    for i in numbers:
#        if str(i) == str(i)[::-1]:
#               palindrome.append(i)
#    if palindrome:
#        print(max(palindrome))    
#    else:
#        print("No palindromes found.")
           
           
# # largestpalindromechek([121, 8148, 7747, 999, 1441, 167461])  
# largestpalindromechek([98,87])           


# def is_palindrome(num):
#     return str(num) == str(num)[::-1]

# def largest_length_palindromes(nums):
#     palindromes = [num for num in nums if is_palindrome(num)]
#     if not palindromes:
#         return []
#     max_length = max(len(str(num)) for num in palindromes)
#     return [num for num in palindromes if len(str(num)) == max_length]

# nums = [121, 3334, 2443, 3443, 5445, 6666, 666611]
# result = largest_length_palindromes(nums)
# if result:
#     print(f"The largest-length palindrome numbers are: {result}")
# else:
#     print("No palindromes found in the list.")



#chek the armstrong number
# def chek_armstrong_number(num): 
#     num_str = str(num)
#     num_length = len(num_str)
#     sum_of_powers = 0
#     for digit in num_str:
#         print(digit)
#         sum_of_powers += int(digit) ** num_length
#         print(sum_of_powers)
    
#     if sum_of_powers == num:
#         print(f"{num} is an Armstrong number")
#     else:
#         print(f"{num} is not an Armstrong number")

# chek_armstrong_number(153)



def chek2nd_largest(numbers):
    largest=0
    second_largest=0
    for i in numbers:
        # print(i)
        if i>largest:
            
            second_largest=largest
            largest=i
            
        elif i>second_largest and i!=largest:
            second_largest=i
    
    print(f"The second largest number is {second_largest}")    
chek2nd_largest([2,4,5,6])             



