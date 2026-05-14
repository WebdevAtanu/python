# dictionary is a collection of key-value pairs. It is unordered, mutable, and indexed. It is defined using curly braces {}.
user = {
    "name": "Mike",
    "age": 25
}

print(user["name"])                     # print value of key
print(user.items())                     # print all items
print(user.keys())                      # print all keys
print(user.values())                    # print all values
print(user.get("name"))                 # print value of key
print(user.get("address", "Not Found")) # print value of key or default value
user.update({"name": "Will"})           # update value of key
print(user["name"])                     # print updated value of key