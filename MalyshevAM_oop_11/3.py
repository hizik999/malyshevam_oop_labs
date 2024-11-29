class CarAcceleration:
    def __init__(self, mass, max_power_hp):
        self.mass = mass
        self.max_power_hp = max_power_hp

    def calculate_power(self, mode="100-200", speed_factor=0.66):
        max_power_watts = self.max_power_hp * 735  # перевод л.с. в ватты
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
        v_initial_mps = v_initial / 3.6  # перевод скорости из км/ч в м/с
        v_final_mps = v_final / 3.6  # перевод скорости из км/ч в м/с
        time = self.mass * (v_final_mps**2 - v_initial_mps**2) / (2 * power)
        return time


class Car(CarAcceleration):
    def __init__(self, mass, max_power_hp, car_type):
        super().__init__(mass, max_power_hp)
        self.car_type = car_type

    def calculate_acceleration_intervals(self):
        print(f"{self.car_type} (массой {self.mass} кг и мощностью {self.max_power_hp} л.с.):")
        v_initial = 100  # начальная скорость в км/ч
        step = 20  # шаг скорости
        speed_factor = 0.66  # начальный коэффициент мощности

        for v_final in range(120, 221, step):  # диапазон скоростей: 120, 140, ..., 200 км/ч
            time = self.calculate_time(v_final, v_initial, speed_factor)
            print(f"  Разгон от {v_initial} до {v_final} км/ч: {time:.2f} секунд.")
            v_initial = v_final  # обновляем начальную скорость
            speed_factor += 0.08  # увеличиваем коэффициент мощности


if __name__ == "__main__":
    # Создаем экземпляры автомобилей
    sedan = Car(1100, 100, "Sedan")
    hatchback = Car(1200, 150, "Hatchback")
    suv = Car(1700, 370, "SUV")

    # Вывод времени разгона через каждые 20 км/ч
    sedan.calculate_acceleration_intervals()
    hatchback.calculate_acceleration_intervals()
    suv.calculate_acceleration_intervals()