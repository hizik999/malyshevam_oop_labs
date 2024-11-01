class Vehicle:
    def __init__(self, name, color, price, speed):
        self.name = name
        self.color = color
        self.price = price
        self.speed = speed

    def show(self):
        print(f"Vehicle: {self.name}, Color: {self.color}, Price: {self.price}")

    def max_speed(self):
        pass

    def change_gear(self, gear):
        pass

    def raschet(self, distance, time):
        speed = distance / time
        print(f"{self.name} будет ехать со скоростью {speed} км/ч расстояние {distance} км за {time} час")


class Car:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
        self.speed = 150

    def max_speed(self):
        print(f"Max speed of the car {self.name}: {self.speed} km/h")

    def change_gear(self, gear):
        print(f"Car {self.name} changed to gear {gear}")

    def raschet(self, time):
        distance = self.speed * time
        print(f"Car {self.name} will cover {distance} km in {time} hours")


class Bike:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
        self.speed = 100

    def max_speed(self):
        print(f"Max speed of the bike {self.name}: {self.speed} km/h")

    def change_gear(self, gear):
        print(f"Bike {self.name} changed to gear {gear}")

    def raschet(self, distance):
        time_taken = distance / self.speed
        print(f"Bike {self.name} will take {time_taken} hours to cover {distance} km")


def process_vehicles(vehicles):
    for vehicle in vehicles:
        vehicle.max_speed()
        vehicle.change_gear(3)
        vehicle.raschet(200)

car = Car("Toyota", "Red", 20000)
bike = Bike("Yamaha", "Blue", 15000)

vehicles = (car, bike)

process_vehicles(vehicles)

v = Vehicle("Vehicle", "Black", 10000, 100)
v.raschet(100, 1)