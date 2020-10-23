class Human:
    age: int
    first_name: str
    last_name: str
    weight: int
    _password: str
    __bank_account: str

    counter: int = 0

    def __init__(self, first_name, last_name, age, weight=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.weight = weight
        self._init_password()
        self.__bank_account = "10000004"

        Human.counter += 1

    def info(self):
        print(f"I'm {self.first_name}, age: {self.age}, weight: {self.weight}")


    def _init_password(self):
        self._password = "1024328923"


    def show_bank_account(self):
        print(f"Account: {self.__bank_account[:3]}*****")


john = Human("John", "Doe", 30)
artur = Human("Artur", "Doe", 40)


john.info()  # Human.info(john)
artur.info()

print(john._password)
john._init_password()
print(john._password)


print(john.counter)
print(artur.counter)
print(Human.counter)

print(john._Human__bank_account)
print(john.show_bank_account())

# print(john, artur)

# john.age = 30
# john.first_name = "John"
# john.last_name = 'Doe'
#
# artur.age = 40
# artur.first_name = "Artur"
# artur.last_name = 'Doe'

