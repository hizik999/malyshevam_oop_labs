class Radio:
    def __init__(self):
        self.is_on = False
        self.station = 0

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            self.station = 0
            print("Radio turned on. Station set to 0.")
        else:
            print("Radio is already on.")

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print("Radio turned off.")
        else:
            print("Radio is already off.")

    def tune_to_station(self, station_number):
        if self.is_on:
            self.station = station_number
            print(f"Tuned to station {station_number}.")
        else:
            print("Cannot tune to station. The radio is off.")


# Пример использования класса Radio
if __name__ == "__main__":
    # Создаем экземпляр радио
    radio = Radio()

    # Включаем радио
    radio.turn_on()

    # Настраиваем на станцию 101.5
    radio.tune_to_station(101.5)

    # Выключаем радио
    radio.turn_off()
