import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = client["acer"]

mycollection = mydb["student"]

data =[
    {"name": "Parul", "age": 21},
    {"name": "Rahul", "age": 22},
    {"name": "Rohit", "age": 23},
    {"name": "Raj", "age": 24}
]

result = mycollection.insert_many(data)

print("inserted ids:", result.inserted_ids)

all_users = mycollection.find()

for user in all_users:
    print(user)

query = {"name": "Parul"}
new_values = {"$set": {"address": "Canyon 123"}}

mycollection.update_one(query, new_values)

delete_query = {"name": "Raj"}
mycollection.delete_one(delete_query)
print("document deleted")

delete_query = {"name": "Rahul"}
mycollection.delete_one(delete_query)
print("document deleted")
