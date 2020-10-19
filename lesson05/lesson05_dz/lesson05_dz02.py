# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
lines = 0

my_file = open("data1.txt", "r")

for line in my_file:
    lines += 1

my_file.seek(0)
content = my_file.readlines()
# print(content)

print("Количество строк в файле:", lines, "\nКоличество слов в файле:", len(content))

my_file.close()
