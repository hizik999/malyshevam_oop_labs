class Vehicle:
    def __init__(self, name, color, price, time, distance, speed):
        self.name = name
        self.color = color
        self.price = price
        self.time = time
        self.distance = distance
        self.speed = speed

    def show(self):
        print(f"Vehicle: {self.name}, Color: {self.color}, Price: {self.price}")

    def max_speed(self):
        print(f"Max speed of {self.name}: {self.speed} km/h")

    def change_gear(self, gear):
        print(f"{self.name} is in gear {gear}")

    def raschet(self):
        time_taken = self.distance / self.speed
        print(f"{self.name} will take {time_taken} hours to cover {self.distance} km")


class Car(Vehicle):
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


class Bike(Vehicle):
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


car = Car("Toyota", "Red", 20000)
bike = Bike("Yamaha", "Blue", 15000)

car.show()
car.max_speed()
car.change_gear(3)
car.raschet(2)

bike.show()
bike.max_speed()
bike.change_gear(2)
bike.raschet(200)
