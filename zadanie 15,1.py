class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Autobus(Transport):
    pass  # Класс наследует всё из Transport без изменений

# Создаем объект Autobus
autobus = Autobus("Renault Logan", 180, 12)

# Выводим информацию в заданном формате
print(f"Название автомобиля: {autobus.name} Скорость: {autobus.max_speed} Пробег: {autobus.mileage}")