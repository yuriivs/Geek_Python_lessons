# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.

# Подсказка: использовать функцию range() и генератор.

from itertools import count

for x in count(20, 20):
    if x > 240:
        break
    print(list(range(x, 20 + 1 * x, x)))

for x in count(21, 21):
    if x > 240:
        break
    print(list(range(x, 21 + 1 * x, x)))