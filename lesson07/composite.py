from abc import ABC, abstractclassmethod


class AbstractUser:
    @abstractclassmethod
    def show_name(self):
        pass

class Person(AbstractUser):

    def show_name(self):
        print(f"It's a Person")


class User(AbstractUser):

    def show_name(self):
        print(f"It's a User")

class CompositeUser(AbstractUser):
    def __init__(self, children: list):
        self.children = children

    def show_name(self):
        for item in self.children:
            item.show_name()


a = Person()
b = User()

compositer = CompositeUser([a, b])

compositer.show_name()