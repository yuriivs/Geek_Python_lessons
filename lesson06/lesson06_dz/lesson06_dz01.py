# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.


# from time import sleep as light_sleep
# import os
#
# class TrafficLight:
#     __color = str
#
#     def run(self, color):
#         self.__color = color
#
#         # os.system('clear')
#         print(color["name"])
#         light_sleep((color["time"]))
#
#
# colors = [{
#     "name": "red",
#     "time": 7
# }, {
#     "name": "yellow",
#     "time": 2
# }, {
#     "name": "green",
#     "time": 4
# }]
#
# traffic = TrafficLight()
#
# i = 0
# while True:
#     traffic.run(colors[i])
#     i += 1
#     if i >= len(colors):
#         i = 0

from time import sleep as light_sleep
# import os //на MacOs почему-то не работает метод clear - поэтому комментирую импорт os


class TrafficLight:
    __color = str

    def running(self, colors):
        i = 0
        while True:
            self.__color = colors[i]
            self.run_color()
            i = (i + 1) if i < len(colors) - 1 else 0

    def run_color(self):
        # os.system('clear') на MacOs почему-то не работает
        print(self.__color["name"])
        light_sleep(self.__color["time"])


colors = [{
    "name": "red",
    "time": 7
}, {
    "name": "yellow",
    "time": 2
}, {
    "name": "green",
    "time": 4
}]

traffic = TrafficLight()
traffic.running(colors)