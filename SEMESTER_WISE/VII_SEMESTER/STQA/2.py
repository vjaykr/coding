def is_valid_age(age):
    if 18 <= age <= 60:
        return "Valid"
    else:
        return "Invalid"
    
print(f"Age 30: {is_valid_age(30)}")  # Expected: Valid

print(f"Age 17: {is_valid_age(17)}") 

print(f"Age 10: {is_valid_age(10)}") 

print(f"Age 61: {is_valid_age(61)}") 

print(f"Age 70: {is_valid_age(70)}")