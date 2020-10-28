# from time import sleep as pause
#
# def out_red(text):
#     print("\033[31m {}" .format(text), pause(2), "\033[37m {}" .format(text))
#
# def out_yellow(text):
#     print("\033[33m {}" .format(text))
#
# def out_green(text):
#     print("\033[32m {}" .format(text))
#
# out_red("red")
# pause(2)
# out_yellow("yellow")
# pause(2)
# out_green("green")
class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки ручки: {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандаша: {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки маркера: {self.title}')


staff1 = Pen('Шариковая ручка')
staff1.draw()

staff1 = Pencil('Цветной карандаш')
staff1.draw()

staff1 = Handle('Цветовыделитель')
staff1.draw()
