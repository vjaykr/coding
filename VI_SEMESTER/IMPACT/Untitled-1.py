# Program to demonstrate tuple operations

# Input a space-separated string and convert it to a tuple
user_input = input("Enter space-separated values: ")
tuple_data = tuple(user_input.split())

# Accessing the first element
print(tuple_data[0])

# Accessing the last element
print(tuple_data[-1])

# Slicing the tuple (all elements except the first) and joining with a comma
sliced_data = ','.join(tuple_data[1:])
print(sliced_data)

# Joining the entire tuple into a space-separated string
joined_data = ' '.join(tuple_data)
print(joined_data)


