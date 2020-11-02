# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    day: int
    month: int
    year: int

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def date_int(self, day, month, year):
      return float(day, month, year)


a = Date()

print(a.date_int(3, 12, 1980))
