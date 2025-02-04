# Create a dictionary with integer keys and string values
hashTable = {}

# Insert key-value pairs
hashTable[1] = "Geeks"
hashTable[12] = "forGeeks"
hashTable[15] = "A computer"
hashTable[3] = "Portal"

# Print the hash table
print(hashTable)

# Retrieve a value using a key
keyToRetrieve = 12
value = hashTable.get(keyToRetrieve)
print("Value for key", keyToRetrieve, ":", value)
