# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Worker:
    name = str
    surname = str
    position = str
    _income = int

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = int(income["wage"]) + (income["bonus"])


class Position(Worker):

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income


position = Position("Ivan", "Ivanov", "Developer", {"wage": 3000, "bonus": 1000})

print(position.name)
print(position.surname)
print(position.position)

print(position.get_full_name())
print(position.get_total_income())