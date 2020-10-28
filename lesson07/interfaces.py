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


john = Person()
artur = User()

john.show_name()
artur.show_name()