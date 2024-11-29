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


class CarAcceleration:
    def __init__(self, mass, max_power_hp):
        self.mass = mass
        self.max_power_hp = max_power_hp

    def calculate_power(self, mode="100-200", speed_factor=0.66):
        max_power_watts = self.max_power_hp * 735 
        if mode == "0-100":
            power = ((max_power_watts * 0.25 + max_power_watts) / 2) * 0.8
        elif mode == "100-200":
            power = ((max_power_watts * speed_factor + max_power_watts) / 2) * 0.8
        else:
            raise ValueError("Invalid mode. Choose '0-100' or '100-200'.")
        return power

    def calculate_time(self, v_final, v_initial=0, speed_factor=0.66):
        mode = "0-100" if v_initial == 0 else "100-200"
        power = self.calculate_power(mode, speed_factor)
        v_initial_mps = v_initial / 3.6  
        v_final_mps = v_final / 3.6  
        time = self.mass * (v_final_mps**2 - v_initial_mps**2) / (2 * power)
        return time


class Car(SUV, Hatchback, SplitSystem, CarAcceleration):
    def __init__(self, doors, engine_type, cargo_space, transmission, mass, max_power_hp, car_type):
        print("Инициализация автомобиля...")
        super().__init__(doors=doors, engine_type=engine_type, cargo_space=cargo_space, transmission=transmission, mass=mass, max_power_hp=max_power_hp)
        self.car_type = car_type
        print("Автомобиль инициализирован")

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
        print(f"Doors: {self.doors}, Engine Type: {self.engine_type}, Cargo Space: {self.cargo_space}, Transmission: {self.transmission}")

    def display_acceleration_times(self):
        time_0_100 = self.calculate_time(100)
        time_100_200 = self.calculate_time(200, 100)
        print(f"{self.car_type} (массой {self.mass} кг и мощностью {self.max_power_hp} л.с.):")
        print(f"  Время разгона от 0 до 100 км/ч: {time_0_100:.2f} секунд.")
        print(f"  Время разгона от 100 до 200 км/ч: {time_100_200:.2f} секунд.")

    def calculate_acceleration_intervals(self):
        print(f"{self.car_type} (массой {self.mass} кг и мощностью {self.max_power_hp} л.с.):")
        v_initial = 100  
        step = 20  
        speed_factor = 0.66

        for v_final in range(120, 221, step):
            time = self.calculate_time(v_final, v_initial, speed_factor)
            print(f"  Разгон от {v_initial} до {v_final} км/ч: {time:.2f} секунд.")
            v_initial = v_final  
            speed_factor += 0.08 


    
sedan = Car(doors=4, engine_type="Gasoline", cargo_space=500, transmission="Manual", mass=1100, max_power_hp=100, car_type="Sedan")
hatchback = Car(doors=4, engine_type="Gasoline", cargo_space=700, transmission="Automate", mass=1200, max_power_hp=150, car_type="Hatchback")
suv = Car(doors=4, engine_type="Electric", cargo_space=1000, transmission="Automate", mass=1700, max_power_hp=300, car_type="SUV")

sedan.calculate_acceleration_intervals()
hatchback.calculate_acceleration_intervals()
suv.calculate_acceleration_intervals()
