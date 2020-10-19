# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
#
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


import os
import random

file_path = os.path.join(os.path.dirname(__file__), 'school_lessons.txt')

to_file_numbers = [random.randint(1, 200) for _ in range(random.randint(10, 250))]
print(sum(to_file_numbers))

with open(file_path, 'w', encoding='UTF-8') as file:
    to_file_str = ' '.join(map(str, to_file_numbers))
    file.write(to_file_str)

with open(file_path, 'r', encoding='UTF-8') as file:
    numbers = map(int, file.read().split(' '))

print(sum(numbers))

assert sum(to_file_numbers) == sum(numbers), 'Сработал ASSERT'
