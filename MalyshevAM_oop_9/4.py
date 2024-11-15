class Sedan:
    def __init__(self, **kwargs):
        self._doors = kwargs.pop('doors', None)
        self._engine_type = kwargs.pop('engine_type', None)
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
        print("Engine started in Sedan")

    def accelerate(self):
        print("Sedan is accelerating")


class SUV:
    def __init__(self, **kwargs):
        self._cargo_space = kwargs.pop('cargo_space', None)
        super().__init__(**kwargs)

    @property
    def cargo_space(self):
        return self._cargo_space

    @cargo_space.setter
    def cargo_space(self, value):
        self._cargo_space = value

    def start_engine(self):
        print("Engine started in SUV")

    def accelerate(self):
        print("SUV is accelerating")

    def brake(self):
        print("SUV is braking")


class Hatchback:
    def __init__(self, **kwargs):
        self._transmission = kwargs.pop('transmission', None)
        super().__init__(**kwargs)

    @property
    def transmission(self):
        return self._transmission

    @transmission.setter
    def transmission(self, value):
        self._transmission = value

    def start_engine(self):
        print("Engine started in Hatchback")

    def accelerate(self):
        print("Hatchback is accelerating")

    def start_transmission(self):
        print("Transmission started in Hatchback")


class Car(Sedan, SUV, Hatchback):
    def __init__(self, doors, engine_type, cargo_space, transmission):
        print("Initializing Car...")
        super().__init__(doors=doors, engine_type=engine_type, cargo_space=cargo_space, transmission=transmission)
        print("Car initialized")

    def drive(self):
        print("Driving the car:")
        self.start_engine()
        self.start_transmission()
        self.accelerate()
        self.brake()


# Тестирование работы классов
if __name__ == "__main__":
    car = Car(4, "Petrol", "Large", "Automatic")
    car.drive()
    print("Doors:", car.doors)
    print("Engine Type:", car.engine_type)
    print("Cargo Space:", car.cargo_space)
    print("Transmission:", car.transmission)
