class Person:
    _first_name: str
    _last_name: str

    def __init__(self, first_name: str, last_name: str):
        self._first_name = first_name
        self._last_name = last_name

    def fullname(self):
        return f"{self._first_name} {self._last_name}"


class User(Person):
    login: str
    password: str

    def __init__(self, first_name: str, last_name: str, login: str):
        super().__init__(first_name, last_name)
        self.login = login

    def log_in(self):
        print(f"Welcome, {self.fullname()}")


class InfoPrinter:
    def info(self, class_object):
        if isinstance(class_object, User):
            print("It's a Person")
        elif isinstance(class_object, Person):
            print("It's a User")
        else:
            print("Unknown class/type")

artur = Person("John", "Doe")
john = User("John", "Doe", "john_doe")
john.log_in

john.log_in()

printer = InfoPrinter()

printer.info(artur)
printer.info(john)
printer.info([])


