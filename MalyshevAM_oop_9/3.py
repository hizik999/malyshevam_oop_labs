class Sedan:
    def __init__(self, doors, engine_type):
        self._doors = doors
        self._engine_type = engine_type

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
    def __init__(self, doors, engine_type, cargo_space):
        self._doors = doors
        self._engine_type = engine_type
        self._cargo_space = cargo_space

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
    def __init__(self, doors, engine_type, cargo_space, transmission):
        self._doors = doors
        self._engine_type = engine_type
        self._cargo_space = cargo_space
        self._transmission = transmission

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

    @property
    def cargo_space(self):
        return self._cargo_space

    @cargo_space.setter
    def cargo_space(self, value):
        self._cargo_space = value

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
        Sedan.__init__(self, doors, engine_type)
        SUV.__init__(self, doors, engine_type, cargo_space)
        Hatchback.__init__(self, doors, engine_type, cargo_space, transmission)
        print("Car initialized")

    def drive(self):
        print("Driving the car:")
        self.start_engine()
        self.start_transmission()
        self.accelerate()
        self.brake()



car = Car(4, "Petrol", "Large", "Automatic")
car.drive()
print("Doors:", car.doors)
print("Engine Type:", car.engine_type)
print("Cargo Space:", car.cargo_space)
print("Transmission:", car.transmission)
