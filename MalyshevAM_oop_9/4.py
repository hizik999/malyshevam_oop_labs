class Vehicle:
    def __init__(self, **kwargs):
        print("Инициализация транспорта")
        super().__init__(**kwargs)


class Sedan(Vehicle):
    def __init__(self, doors, engine_type, **kwargs):
        print("Инициализация седана")
        self._doors = doors
        self._engine_type = engine_type
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
        print("Двигатель седана запущен.")

    def accelerate(self):
        print("Седан ускоряется.")


class SUV(Vehicle):
    def __init__(self, cargo_space, **kwargs):
        print("Инициализация внедорожника")
        self._cargo_space = cargo_space
        super().__init__(**kwargs)

    @property
    def cargo_space(self):
        return self._cargo_space

    @cargo_space.setter
    def cargo_space(self, value):
        self._cargo_space = value

    def start_engine(self):
        print("Двигатель внедорожника запущен.")

    def accelerate(self):
        print("Внедорожник ускоряется.")

    def brake(self):
        print("Внедорожник тормозит.")


class Hatchback(Vehicle):
    def __init__(self, transmission, **kwargs):
        print("Инициализация хэтчбека")
        self._transmission = transmission
        super().__init__(**kwargs)

    @property
    def transmission(self):
        return self._transmission

    @transmission.setter
    def transmission(self, value):
        self._transmission = value

    def start_engine(self):
        print("Двигатель хэтчбека запущен.")

    def accelerate(self):
        print("Хэтчбек ускоряется.")

    def start_transmission(self):
        print("Трансмиссия хэтчбека включена.")


class Car(Sedan, SUV, Hatchback):
    def __init__(self, doors, engine_type, cargo_space, transmission):
        print("Инициализация автомобиля...")
        super().__init__(doors=doors, engine_type=engine_type, cargo_space=cargo_space, transmission=transmission)
        print("Автомобиль инициализирован.")

    def drive(self):
        self.start_engine()
        self.start_transmission()
        self.accelerate()
        self.brake()

    def display_info(self):
        print(f"Двери: {self.doors}, Тип двигателя: {self.engine_type}, Багажное пространство: {self.cargo_space}, Трансмиссия: {self.transmission}")


# Тестирование
if __name__ == "__main__":
    car = Car(doors=4, engine_type="Бензиновый", cargo_space="Большой", transmission="Автомат")
    car.drive()
    car.display_info()
