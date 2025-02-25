from typing import List

# def find_divisors(n):
#     divisors = []
#     for i in range(1, n):  # Check numbers from 1 to n-1
#         if n % i == 0:
#             divisors.append(i)
#     return divisors

# # Example usage
# num = 20
# print(find_divisors(num))  




#roman to integer

def roman_to_int(s: str) -> int:
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    prev_value = 0
    
    for char in reversed(s):
        value = roman_values[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    
    return total

# Example usage
print(roman_to_int("III"))      # Output: 3
print(roman_to_int("LVIII"))    # Output: 58
print(roman_to_int("MCMXCIV"))  # Output: 1994