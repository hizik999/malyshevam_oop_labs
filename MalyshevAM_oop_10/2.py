class Radio:
    def __init__(self):
        self.is_on = False
        self.station = 0

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
            print(f"Переключено {station_number}.")
        else:
            print("Не может переключиться. Радио выключено.")


# Пример использования класса Radio
# Создаем экземпляр радио
radio = Radio()

# Включаем радио
radio.turn_on()

# Настраиваем на станцию 101.5
radio.tune_to_station(101.5)

# Выключаем радио
radio.turn_off()
