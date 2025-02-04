def square(x):
    return x*x

def sum_of_squares(x, y):
    return square(x) + square(y)

print(sum_of_squares(3, 4))

x = 1
def f():
    x = 2
    return x
print(x)
print(f())
print(x)


x = "hello world"
print(x.format())

print(2<3 and not 3>2)

x = 43
if x %2 ==0:
    print("even")
else:
    print("odd")

x = 42

if x < 10:
    print("one digit number")
elif x < 100:
    print("two digit number")
else:
    print("big number")

x = 2
if x ==2:
    print(x)
else:
    print(x+


x = [1, 2, 3, 4, 5]
# print('this is numbers list', x)
# x = ["hello", "world"]  
# print(x)

import sys
x = ("cadbsjkdba","sadfkbasdf   ")
# x = sys.argv[1]
# print("\n\n",x)


print(len(x))

import csv

def calculate_average(csv_file, column_name):
    total = 0
    count = 0
    
    with open('csv_file', 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            if column_name in row:
                try:
                    total += float(row[column_name])
                    count += 1
                except ValueError:
                    print(f"Invalid value '{row[column_name]}' in column '{column_name}'")
                    
    if count > 0:
        average = total / count
        return average
    else:
        return None
    
csv_file = "data.csv"
column_name = "value"

average = calculate_average('csv_file', column_name)
print(f"The average of column '{column_name}' is {average}")  



import mysql.connector

db = mysql.connector.connect(
    host =
    user =
    password =
    database=
)


cursor = db.cursor()
def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS userss (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))")
    

    
def insert_data(name, email):
    sql = 






import pymongo

client = pymongo.Mongoclient("mongodb://localhost:27017/")

my db = client["ParulDatabase"]

mycollection = mydb["Students"]

data = [{"name": "Parul", "age": 21}
        {"name": "Rahul", "age": 22}
        {"name": "Rohit", "age": 23}
        {"name": "Raj", "age": 24}]
        
        
result = mycollection.insert_many(data)

print("inserted ids", result.inserted_ids)


all_users = mycollection.find()

for user in all_users:
    print(user)
    
query = {"address": "Park Lane 38"}
new_values = {"$set": {"address": "Canyon 123"}}

mycollection.update_one(query, new_values)


delete_query = {"name": "Raj"}
mycollection.delete_one(delete_query)

print("document deleted")


delete_query = {"name": "Rahul"}
mycollection.delete_one(delete_query)
print("document deleted")







import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gobi123@",
    database="gobi1"
)

cursor = db.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)")

def insert_data(name, age):
    sql = "INSERT INTO students (name, age) VALUES (%s, %s)"
    values = (name, age)
    cursor.execute(sql, values)
    db.commit()

create_table()
insert_data("John", 20)
insert_data("Jane", 22)
insert_data("Mike", 19)


