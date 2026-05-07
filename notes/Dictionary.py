user = {
    "name": "Atanu",
    "age": 25
}

print(user["name"]) # print value of key
print(user.items()) # print all items
print(user.keys()) # print all keys
print(user.values()) # print all values
print(user.get("name")) # print value of key
print(user.get("address", "Not Found")) # print value of key or default value
user.update({"name": "Atanu"}) # update value of key
