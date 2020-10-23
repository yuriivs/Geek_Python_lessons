# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep as light_sleep
from os import




class TrafficLight:
    __color = str

    def running(self, color):
        TrafficLight.__color = color
        print(color["color_one"])
        light_sleep((color["pause_one"]))
        sp.call('cls', shell=True)
        print(color["color_two"])
        light_sleep((color["pause_two"]))
        print(color["color_three"])


a = TrafficLight()
a.running({"color_one": "red", "pause_one": 1,
               "color_two": "yellow", "pause_two": 1,
               "color_three": "green", "pause_three": 1})
