# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


with open("data4.txt", "w") as digit_list:
    digit_list = int(input("Введите числа, разделенные пробелами >>>").split())
    for x in digit_list:
        print(x, file="data4.txt")

    print(sum(digit_list))
