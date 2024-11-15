class SplitSystem:
    def __init__(self):
        self.is_on = False
        self.mode = None
        self.temperature = None

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            self.mode = "cooling"
            self.temperature = 22  # Начальная температура
            print("Split system turned on. Mode: cooling, Temperature: 22°C")
        else:
            print("Split system is already on.")

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print("Split system turned off.")
        else:
            print("Split system is already off.")

    def set_cooling_temperature(self, temperature):
        if self.is_on and self.mode == "cooling":
            self.temperature = temperature
            print(f"Cooling temperature set to {temperature}°C.")
        else:
            print("Cannot set cooling temperature. The system is either off or not in cooling mode.")

    def turn_on_cooling(self):
        if not self.is_on:
            self.turn_on()
        elif self.mode != "cooling":
            self.mode = "cooling"
            print("Mode switched to cooling.")
        else:
            print("System is already in cooling mode.")

    def turn_off_cooling(self):
        if self.is_on and self.mode == "cooling":
            self.turn_off()
        else:
            print("Cannot turn off cooling. The system is either off or not in cooling mode.")

    def turn_on_heating(self):
        if not self.is_on:
            self.is_on = True
            self.mode = "heating"
            self.temperature = 25  # Начальная температура для обогрева
            print("Split system turned on. Mode: heating, Temperature: 25°C")
        elif self.mode != "heating":
            self.mode = "heating"
            print("Mode switched to heating.")
        else:
            print("System is already in heating mode.")

    def turn_off_heating(self):
        if self.is_on and self.mode == "heating":
            self.turn_off()
        else:
            print("Cannot turn off heating. The system is either off or not in heating mode.")


# Пример использования класса SplitSystem
if __name__ == "__main__":
    split_system = SplitSystem()
    
    # Включение сплит-системы
    split_system.turn_on()
    
    # Установка температуры охлаждения
    split_system.set_cooling_temperature(18)
    
    # Включение режима обогрева
    split_system.turn_on_heating()
    
    # Отключение режима обогрева
    split_system.turn_off_heating()
    
    # Включение режима охлаждения
    split_system.turn_on_cooling()
    
    # Отключение системы
    split_system.turn_off()
