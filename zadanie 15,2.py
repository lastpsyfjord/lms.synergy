class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"

class Autobus(Transport):
    def seating_capacity(self, capacity=50):
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"

# Создаем объект Autobus
autobus = Autobus("Renaul Logan", 180, 12)

# Выводим результат работы метода
print(autobus.seating_capacity())