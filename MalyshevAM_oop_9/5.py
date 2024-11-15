class Vehicle:
    def __init__(self, **kwargs):
        print("Инициализация транспорта")
        super().__init__(**kwargs)


class EngineTypeMixin:
    def __init__(self, engine_type, **kwargs):
        self._engine_type = engine_type
        print("Инициализация типа двигателя")
        super().__init__(**kwargs)

    @property
    def engine_type(self):
        return self._engine_type

    @engine_type.setter
    def engine_type(self, value):
        self._engine_type = value


class Sedan(Vehicle, EngineTypeMixin):
    def __init__(self, doors, engine_type, **kwargs):
        self._doors = doors
        print("Инициализация седана")
        super().__init__(engine_type=engine_type, **kwargs)

    @property
    def doors(self):
        return self._doors

    @doors.setter
    def doors(self, value):
        self._doors = value

    def start_engine(self):
        print("Двигатель седана запущен.")

    def accelerate(self):
        print("Седан ускоряется.")


class SUV(Vehicle, EngineTypeMixin):
    def __init__(self, cargo_space, engine_type, **kwargs):
        self._cargo_space = cargo_space
        print("Инициализация внедорожника")
        super().__init__(engine_type=engine_type, **kwargs)

    @property
    def cargo_space(self):
        return self._cargo_space

    @cargo_space.setter
    def cargo_space(self, value):
        self._cargo_space = value

    def brake(self):
        print("Внедорожник тормозит.")


class Car(Sedan, SUV):
    def __init__(self, doors, cargo_space, engine_type):
        print("Инициализация автомобиля...")
        super().__init__(doors=doors, cargo_space=cargo_space, engine_type=engine_type)
        print("Автомобиль инициализирован.")

    def drive(self):
        self.start_engine()
        self.accelerate()
        self.brake()

    def display_info(self):
        print(f"Двери: {self.doors}, Тип двигателя: {self.engine_type}, Багажное пространство: {self.cargo_space}")
        

# Тестирование
if __name__ == "__main__":
    car = Car(doors=4, cargo_space="Большой", engine_type="Бензиновый")
    car.drive()
    car.display_info()
