# Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position,  передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).

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

print(position.position)
print(position.get_full_name())
print(position.get_total_income())