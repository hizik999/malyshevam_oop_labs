class SplitSystem:
    def __init__(self):
        self.is_on = False
        self.mode = None
        self.temperature = None

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            self.mode = "cooling"
            self.temperature = 22
            print("Сплит-система включена.")
            print("Температура охлаждения установлена на 22°C.")
        else:
            print("Сплит-система уже включена.")

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print("Сплит-система выключена.")
        else:
            print("Сплит-система уже выключена.")

    def set_cooling_temperature(self, temperature):
        if self.is_on and self.mode == "cooling":
            self.temperature = temperature
            print(f"Температура охлаждения установлена на {temperature}°C.")
        else:
            print("Невозможно установить температуру охлаждения. Сплит-система выключена или не в режиме охлаждения.")

    def turn_on_cooling(self):
        if not self.is_on:
            self.turn_on()
        elif self.mode != "cooling":
            self.mode = "cooling"
            print("Режим охлаждения включен.")
        else:
            print("Сплит-система уже в режиме охлаждения.")

    def turn_off_cooling(self):
        if self.is_on and self.mode == "cooling":
            self.turn_off()
        else:
            print("Невозможно выключить режим охлаждения. Сплит-система выключена или не в режиме охлаждения.")

    def turn_on_heating(self):
        if not self.is_on:
            self.is_on = True
            self.mode = "heating"
            self.temperature = 25
            print("Сплит-система включена.")
            print("Режим обогрева включен.")
        elif self.mode != "heating":
            self.mode = "heating"
            print("Режим обогрева включен.")
        else:
            print("Сплит-система уже в режиме обогрева.")

    def turn_off_heating(self):
        if self.is_on and self.mode == "heating":
            self.turn_off()
            print("Режим обогрева выключен.")
        else:
            print("Невозможно выключить режим обогрева. Сплит-система выключена или не в режиме обогрева.")


class Radio:
    def __init__(self):
        self.is_on = False
        self.station = 0

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            self.station = 0
            print("Радио включено.")
        else:
            print("Радио уже включено.")

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print("Радио выключено.")
        else:
            print("Радио уже выключено.")

    def tune_to_station(self, station_number):
        if self.is_on:
            self.station = station_number
            print(f"Настроено на радиостанцию {station_number}.")
        else:
            print("Невозможно настроить радиостанцию. Радио выключено.")


class Sedan:
    def __init__(self, doors, engine_type):
        self.doors = doors
        self.engine_type = engine_type


class Hatchback(Sedan, Radio):
    def __init__(self, doors, engine_type, transmission):
        Sedan.__init__(self, doors, engine_type)
        Radio.__init__(self)
        self.transmission = transmission

    def start_engine(self):
        print("Запуск двигателя")

    def start_transmission(self):
        print("Переключение трансмиссии")

    def accelerate(self):
        print("Ускорение")

    def brake(self):
        print("Торможение")


class SUV:
    def __init__(self, cargo_space):
        self.cargo_space = cargo_space


class Car(SUV, Hatchback, SplitSystem):
    def __init__(self, doors, engine_type, cargo_space, transmission):
        SUV.__init__(self, cargo_space)
        Hatchback.__init__(self, doors, engine_type, transmission)
        SplitSystem.__init__(self)

    def drive(self):
        self.start_engine()
        self.start_transmission()
        self.accelerate()
        self.turn_on()
        self.set_cooling_temperature(22)
        self.turn_off_cooling()
        self.turn_on_heating()
        self.turn_on()
        self.tune_to_station(101.5)
        self.turn_off_heating()
        self.turn_off()
        self.brake()

    def display_info(self):
        print(f"Doors: {self.doors}, Engine type: {self.engine_type}, Cargo space: {self.cargo_space}, Transmission: {self.transmission}")


# Пример использования класса Car
if __name__ == "__main__":
    car = Car(4, "567-ВАП-02", 5, "АВТОМАТ")
    car.drive()
    car.display_info()
