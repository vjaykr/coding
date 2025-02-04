import random
import string
def generate_password(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) 
                   for i in range(length))

print(generate_password(10))