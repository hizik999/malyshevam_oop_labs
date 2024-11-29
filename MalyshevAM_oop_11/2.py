class CarAcceleration:
    def __init__(self, mass, max_power_hp):
        self.mass = mass
        self.max_power_hp = max_power_hp

    def calculate_power(self, mode="0-100"):
        max_power_watts = self.max_power_hp * 735  # перевод л.с. в ватты
        if mode == "0-100":
            power = ((max_power_watts * 0.25 + max_power_watts) / 2) * 0.8
        elif mode == "100-200":
            power = ((max_power_watts * 0.66 + max_power_watts) / 2) * 0.8
        else:
            raise ValueError("Invalid mode. Choose '0-100' or '100-200'.")
        return power

    def calculate_time(self, v_final, v_initial=0):
        mode = "0-100" if v_initial == 0 else "100-200"
        power = self.calculate_power(mode)
        v_initial_mps = v_initial / 3.6  # перевод скорости из км/ч в м/с
        v_final_mps = v_final / 3.6  # перевод скорости из км/ч в м/с
        time = self.mass * (v_final_mps**2 - v_initial_mps**2) / (2 * power)
        return time


class Car(CarAcceleration):
    def __init__(self, mass, max_power_hp, car_type):
        super().__init__(mass, max_power_hp)
        self.car_type = car_type

    def display_acceleration_times(self):
        time_0_100 = self.calculate_time(100)
        time_100_200 = self.calculate_time(200, 100)
        print(f"{self.car_type} (массой {self.mass} кг и мощностью {self.max_power_hp} л.с.):")
        print(f"  Время разгона от 0 до 100 км/ч: {time_0_100:.2f} секунд.")
        print(f"  Время разгона от 100 до 200 км/ч: {time_100_200:.2f} секунд.")


if __name__ == "__main__":
    # Создаем экземпляры автомобилей
    sedan = Car(1100, 100, "Sedan")
    hatchback = Car(1200, 150, "Hatchback")
    suv = Car(1700, 370, "SUV")

    # Вывод времени разгона
    sedan.display_acceleration_times()
    hatchback.display_acceleration_times()
    suv.display_acceleration_times()
