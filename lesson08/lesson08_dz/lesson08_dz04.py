# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
#
# class Warehouse:
#     pass
#
# class OfficeEquipment:
#     pass
#
# class Printer:
#     pass
#
# class Scanner:
#     pass
#
# class Copier:
#     pass


class StoreMashines:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Device model': self.name, 'Price per one': self.price, 'Quantity': self.quantity}

    def __str__(self):
        return f'{self.name} price {self.price} quantity {self.quantity}'


    def reception(self):

        try:
            unit = input(f'Enter the name ')
            unit_p = int(input(f'Enter the price per one '))
            unit_q = int(input(f'Enter the quantity '))
            unique = {'Device model': unit, 'Price per one': unit_p, 'Quantity': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Current list -\n {self.my_store}')
        except:
            return f'Data entry error'

        print(f'Press "Q" to exit, or "Enter" to continue')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Whole warehouse -\n {self.my_store_full}')
            return f'Quit'
        else:
            return StoreMashines.reception(self)


class Printer(StoreMashines):
    def to_print(self):
        return f'to print smth. {self.numb} times'


class Scanner(StoreMashines):
    def to_scan(self):
        return f'to scan smth. {self.numb} times'


class Copier(StoreMashines):
    def to_copier(self):
        return f'to copier smth.  {self.numb} times'


unit_1 = Printer('Kyocera', 44000, 20, 10)
unit_2 = Scanner('HP', 34500, 15, 10)
unit_3 = Copier('Xerox', 51250, 4, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())