old_dict = dict(name="John", age=10)

new_dict = {"name": "John", "age": 10}

print(old_dict.keys())
print(old_dict.values())

print(new_dict["age"])
print(new_dict.get("age"))

print(new_dict.get("surname"))

if new_dict.get("surname") == None:
    print("No surname")
