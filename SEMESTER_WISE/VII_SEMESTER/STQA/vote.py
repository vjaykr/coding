# # x = int(input("Enter age: "))

# # if x>0:
# #     if x >= 18 and x <=60:
# #         print("You can vote")
# #     else:
# #         print("You cannot vote")    
# # else:
# #     print("Invalid age")          


# # marks = int(input("Enter marks: "))

# # if marks <30:
# #     print("fail")
# # elif marks >= 30 and marks < 50:
# #     print("P")
# # elif marks >= 50 and marks < 75:
# #     print("B")
# # elif marks >= 75 and marks < 90:
# #     print("A")  
# # elif marks >= 90 and marks <= 95:
# #     print("A+")
# # elif marks > 95 and marks <= 100:
# #     print("O+")            


# arr = [2, 0, 3, 1, 5]


# max_num = arr[0]
# for i in range(1, len(arr)):
#     if arr[i] > max_num:
#         max_num = arr[i]

# for i in range(len(arr)):
#     if arr[i] == max_num:
#         print("Max number is:", arr[i])

#         second_max = 0
#         for num in arr:
#             if num != max_num and num > second_max:
#                 second_max = num
 
#         if second_max != 0:
#             print("Second max number is:", second_max)
#         else:
#             print("No second max found")

def generate_pattern(rows):
    n = 1
    for i in range(rows):
        row_elements = []
        for j in range(i + 1):
            row_elements.append(n)
            n += 1
        print(*row_elements) # Prints the list elements separated by spaces

# Generate the pattern with 4 rows
generate_pattern(4)


