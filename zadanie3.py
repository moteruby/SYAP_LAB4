# Задание 3
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина движется")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print("Машина повернула", direction)

    def show_speed(self):
        print("Текущая скорость автомобиля", self.speed, "км/ч")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости на towncar")
        else:
            print("Текущая скорость автомобиля", self.speed, "км/ч")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости на workcar")
        else:
            print("Текущая скорость автомобиля", self.speed, "км/ч")


class PoliceCar(Car):
    pass

# Example usage
town_car = TownCar(70, 'red', 'Toyota', False)
town_car.go()
town_car.show_speed()
town_car.turn('налево')
town_car.stop()
print("")

work_car = WorkCar(80, 'green', 'Skoda', False)
work_car.go()
work_car.show_speed()
work_car.turn('направо')
work_car.stop()
print("")

police_car = PoliceCar(80, 'black', 'Jeep', True)
police_car.go()
police_car.show_speed()
police_car.turn('направо')
police_car.stop()