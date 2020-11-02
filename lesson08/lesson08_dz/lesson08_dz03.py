# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные
# и заполнять список только числами.
# Класс-исключение должен контролировать типы данных элементов списка.

class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                # count = int(input('Сколько элементов будет в списке? >>> '))
                val = int(input('Введите число для списка: >>> '))
                self.my_list.append(val)
                print(f'Список - {self.my_list} \n ')
            except:
                print(f"Ошибка!")
                y_or_n = input(f'Попробуем еще? Да/Нет ')

                if y_or_n == 'Да' or y_or_n == 'да':
                    print(try_except.my_input())
                elif y_or_n == 'Нет' or y_or_n == 'нет':
                    return f'Ок. Программа завершена!'
                    break
                else:
                    return f'Ок'

try_except = Error(1)
print(try_except.my_input())