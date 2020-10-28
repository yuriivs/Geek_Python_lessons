# Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()),
# умножение (mul()), деление (truediv()). Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

class Cell:

    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Result: {self.quantity * "*"}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity - other.quantity < 0:
            print('Negative result!')

        return Cell(self.quantity - other.quantity)

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, cell_row):
        row = ''

        for i in range(int(self.quantity / cell_row)):
            row += f'{"*" * cell_row}\\n'
        row += f'{"*" * (self.quantity % cell_row)}'

        return row


cells1 = Cell(12)
cells2 = Cell(4)

print(cells1 + cells2)
print(cells1 - cells2)
print(cells1 * cells2)
print(cells1 / cells2)
print(cells1.make_order(5))