# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

res = 0


def operation(res):
    try:
        list = input("Введите любое количество чисел через пробел ").split(" ")
        for s in list:
            res += int(s)

        print(res)
        operation(res)
    except ValueError:
        print(res)
        print("Спецсимволы нельзя !!!")

operation(res)