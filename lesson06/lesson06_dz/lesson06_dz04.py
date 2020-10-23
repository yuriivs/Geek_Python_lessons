# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.


class Car:
    speed = str
    color = str
    name = str
    is_police = bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Car go")

    def stop(self):
        print("Car stop")

    def turn(self, direction):
        print("Car turn on " + direction)

    def show_speed(self):
        print("Car's speed: " + self.speed)


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print("WARNING car speeding")
        else:
            print("Car's speed: " + str(self.speed))


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print("WARNING car speeding!!!")
        else:
            print("Car's speed: " + str(self.speed))


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


town_car = TownCar(61, "red", "audi", False)
town_car.go()
town_car.stop()
town_car.turn("left")
town_car.show_speed()