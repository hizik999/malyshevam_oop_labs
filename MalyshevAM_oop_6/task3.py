from accessify import private

class Bus:
    @private
    def __max_speed(self):
        return 120

    @private
    def __capacity(self):
        return 75

    @private
    def __fuel_tank(self):
        return 100

    @private
    def __kartet_tank(self):
        return 6

    @private
    def __luggage_spaces(self):
        return 150

    def __init__(self, speed, distance):
        if speed > self.__max_speed():
            self.__speed = self.__max_speed()
            print(f'Нельзя поставить скорость больше максимальной ({self.__max_speed()}), поэтому ставим скорость, равной максимальной')
        else:
            self.__speed = speed
        self.__distance = distance
        self.__passengers = []
        self.__empty_seats = self.__capacity()
        self.__seats_occupied = 0
        self.__toplivo = None
        self.__maslo = None
        self.__luggage = 0

    # Методы-геттеры
    def get_speed(self):
        return self.__speed

    def get_distance(self):
        return self.__distance

    def get_passengers(self):
        return self.__passengers

    def get_empty_seats(self):
        return self.__empty_seats

    def get_luggage(self):
        return self.__luggage

    # Методы-сеттеры
    def set_speed(self, speed):
        if speed <= self.__max_speed():
            self.__speed = speed
        else:
            raise ValueError(f'Скорость превышает максимальную, надо ввести число меньше {self.__max_speed()}')

    def set_distance(self, distance):
        self.__distance = distance

    def set_passengers(self, passengers):
        if len(passengers) > self.__capacity():
            raise ValueError(f"Количество пассажиров не может превышать {self.__capacity()}.")
        self.__passengers = passengers
        self.__seats_occupied = len(passengers)
        self.__empty_seats = self.__capacity() - len(passengers)

    def set_luggage(self, luggage):
        if luggage <= self.__luggage_spaces():
            self.__luggage = luggage
        else:
            raise ValueError(f'Багаж превышает вместительность, надо ввести число меньше {self.__luggage_spaces()}')

    def show_values(self):
        print(f"Скорость: {self.get_speed()}")
        print(f"Расстояние: {self.get_distance()}")
        print(f"Пассажиры: {self.get_passengers()}")
        print(f"Свободные места: {self.get_empty_seats()}")
        print(f"Занятые места: {self.__seats_occupied}")
        print(f"Топливо: {self.__toplivo}")
        print(f"Масло: {self.__maslo}")
        print(f"Багаж: {self.get_luggage()}")

# Пример использования класса
mybus1 = Bus(150, 300)
mybus1.set_speed(80)
mybus1.set_passengers(['Пассажир 1', 'Пассажир 2'])
mybus1.set_luggage(50)

print(Bus.__max_speed())

mybus2 = Bus(90, 200)
mybus2.set_speed(70)
mybus2.set_passengers(['Пассажир 3'])
mybus2.set_luggage(20)

mybus3 = Bus(110, 500)
mybus3.set_speed(100)
mybus3.set_passengers(["Пассажир 4", "Пассажир 5"])
mybus3.set_luggage(30)

# Выводим значения для каждого автобуса
print("Информация об автобусе 1:")
mybus1.show_values()
print('---' * 20)
print("Информация об автобусе 2:")
mybus2.show_values()
print('---' * 20)
print("Информация об автобусе 3:")
mybus3.show_values()
print('--' * 100)

print(mybus1.get_distance())
print(mybus1.__max_speed)
try:
    print("Скорость автобуса 3:", mybus3.get_speed())  # Это должно работать
except Exception as e:
    print("Ошибка при вызове геттера:", e)

try:
    mybus3.set_speed(130)  # Это вызовет ValueError
except ValueError as e:
    print("Ошибка при установке скорости:", e)
