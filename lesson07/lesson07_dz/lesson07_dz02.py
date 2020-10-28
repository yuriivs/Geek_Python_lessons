# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные
# на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractclassmethod

class color:
   BOLD = '\033[1m'
   END = '\033[0m'

class Clothes:
    @abstractclassmethod
    def cut_clothes(self):
        pass


def print_decorator(func):
    def wrapper(*args, **kwargs):
        print (color.BOLD + "Расчет количества ткани:" + color.END)
        func(*args, **kwargs)
        # print("End")

    return wrapper


class Coat(Clothes):
    @print_decorator
    def cut_clothes(self, size = int):
        self.size = size

        print(f"Для пальто ", size, "размера - необходимо: ", size/6.5 + 0.5, "метров ткани.")


class Suit(Clothes):
    @print_decorator
    def cut_clothes(self, height = int):
        self.height = height
        print(f"Для костюма ", height, "роста - необходимо: ", 2 * height + 0.3, "метров ткани.")


a = Coat()
b = Suit()

a.cut_clothes(5)
b.cut_clothes(2)
