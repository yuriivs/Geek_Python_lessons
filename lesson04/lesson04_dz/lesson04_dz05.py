# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
#
# Подсказка: использовать функцию reduce().

from itertools import count
from functools import reduce

for x in count(100, 2):
    if x > 1000:
        break

print(reduce(lambda res, x: res * x, count, 2))

# from functools import reduce
#
# print(x * (x + 1))
