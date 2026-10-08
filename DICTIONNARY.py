# Dictionary = a collection of {key : value} pairs
# Ordered, changeable (mutable), and no duplicate keys

capitals = {
    "USA": "Washington D.C",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}

# print(dir(capitals))
# print(help(capitals))

# .get() → gets the value of a key
print(capitals.get("India"))

# Checking if a key exists
if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

# .update() → adds a new key-value pair
capitals.update({"Germany": "Berlin"})

# .update() can also change an existing value
capitals.update({"USA": "New York"})

# .pop() → removes a specific key-value pair
capitals.pop("China")

# .popitem() → removes the last inserted key-value pair
capitals.popitem()

# .keys() → returns all keys
for key in capitals.keys():
    print(key)

# .values() → returns all values
for value in capitals.values():
    print(value)

# .items() → returns both keys and values
for key, value in capitals.items():
    print(f"{key} : {value}")