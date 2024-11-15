class Vehicle:
    def __init__(self, **kwargs):
        print("Инициализация транспорта")
        super().__init__(**kwargs)


class Radio:
    def __init__(self, **kwargs):
        self.is_on = False
        self.station = 0
        super().__init__(**kwargs)

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            self.station = 0
            print("Радио включено. Станция 0.")
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
            print(f"Переключено на {station_number}.")
        else:
            print("Не может переключиться. Радио выключено.")


class SplitSystem:
    def __init__(self, **kwargs):
        self.is_on = False
        self.mode = None
        self.temperature = None
        super().__init__(**kwargs)

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            self.mode = "охлаждение"
            self.temperature = 22
            print("Сплит-система включена. Режим: охлаждение, Температура: 22°C")
        else:
            print("Сплит-система уже включена.")

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print("Сплит-система выключена.")
        else:
            print("Сплит-система уже выключена.")

    def set_cooling_temperature(self, temperature):
        if self.is_on and self.mode == "охлаждение":
            self.temperature = temperature
            print(f"Температура охлаждения установлена на {temperature}°C.")
        else:
            print("Невозможно установить температуру охлаждения. Сплит-система либо выключена, либо не в режиме охлаждения.")

    def turn_on_cooling(self):
        if not self.is_on:
            self.turn_on()
        elif self.mode != "охлаждение":
            self.mode = "охлаждение"
            print("Режим переключен на охлаждение.")
        else:
            print("Система уже в режиме охлаждения.")

    def turn_off_cooling(self):
        if self.is_on and self.mode == "охлаждение":
            self.turn_off()
            print("Режим охлаждения выключен.")
        else:
            print("Невозможно выключить режим охлаждения. Сплит-система либо выключена, либо не в режиме охлаждения.")

    def turn_on_heating(self):
        if not self.is_on:
            self.is_on = True
            self.mode = "обогрев"
            self.temperature = 25
            print("Сплит-система включена. Режим: обогрев, Температура: 25°C")
        elif self.mode != "обогрев":
            self.mode = "обогрев"
            print("Режим переключен на обогрев.")
        else:
            print("Система уже в режиме обогрева.")

    def turn_off_heating(self):
        if self.is_on and self.mode == "обогрев":
            self.turn_off()
            print("Режим обогрева выключен.")
        else:
            print("Невозможно выключить режим обогрева. Сплит-система либо выключена, либо не в режиме обогрева.")


class Sedan(Vehicle):
    def __init__(self, **kwargs):
        self._doors = kwargs.pop('doors', None)
        self._engine_type = kwargs.pop('engine_type', None)
        print("Инициализация седана")
        super().__init__(**kwargs)

    @property
    def doors(self):
        return self._doors

    @doors.setter
    def doors(self, value):
        self._doors = value

    @property
    def engine_type(self):
        return self._engine_type

    @engine_type.setter
    def engine_type(self, value):
        self._engine_type = value

    def start_engine(self):
        print("Запуск двигателя")

    def accelerate(self):
        print("Ускорение")


class SUV(Vehicle):
    def __init__(self, **kwargs):
        self._cargo_space = kwargs.pop('cargo_space', None)
        print("Инициализация внедорожника")
        super().__init__(**kwargs)

    @property
    def cargo_space(self):
        return self._cargo_space

    @cargo_space.setter
    def cargo_space(self, value):
        self._cargo_space = value

    def brake(self):
        print("Торможение")


class Hatchback(Sedan, Radio):
    def __init__(self, **kwargs):
        self._transmission = kwargs.pop('transmission', None)
        print("Инициализация хэтчбека")
        super().__init__(**kwargs)

    @property
    def transmission(self):
        return self._transmission

    @transmission.setter
    def transmission(self, value):
        self._transmission = value

    def start_transmission(self):
        print("Переключение трансмиссии")


class Car(SUV, Hatchback, SplitSystem):
    def __init__(self, doors, engine_type, cargo_space, transmission):
        print("Инициализация автомобиля...")
        super().__init__(doors=doors, engine_type=engine_type, cargo_space=cargo_space, transmission=transmission)
        print("Автомобиль инициализирован")

    def drive(self):
        self.start_engine()
        self.start_transmission()
        self.accelerate()
        self.turn_on()  # Включаем сплит-систему
        self.set_cooling_temperature(22)
        self.turn_off_cooling()
        self.turn_on_heating()
        self.turn_on()  # Включаем радио
        self.tune_to_station(101.5)
        self.turn_off_heating()
        self.turn_off()  # Выключаем радио
        self.brake()

    def display_info(self):
        print(f"Doors: {self.doors}, Engine Type: {self.engine_type}, Cargo Space: {self.cargo_space}, Transmission: {self.transmission}")


# Тестирование работы классов

car = Car(4, "567-ВАП-02", 5, "АВТОМАТ")
car.drive()
car.display_info()
