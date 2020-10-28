class Person:
    def __init__(self, attrs: dict):
        self._attributes = attrs

    def __del__(self):
        print("Person removed")

    def __str__(self):
        return f'Person: {self._attributes["first_name"]} {self._attributes["last_name"]}'

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, item):
        if item != "age":
            return self._attributes[item]
        else:
            return None

    def __setattr__(self, key, value):
        if "_attributes" in self.__dict__:
            self._attributes[key] = value
        else:
            super().__setattr__(key, value)


john = Person({"first_name": "John", "last_name": "Doe", "age": 30})
artur = Person({"first_name": "Artut", "last_name": "Doe", "age": 30})

# del john
users = [john, artur]
# print(john.attributes["first_name"])
#
# print(john)
# print(users)

# print(john["first_name"])
# print(john["age"])
# print(artur["first_name"])

john.job = "Developer"
# print(john.job)
print(john["job"])
