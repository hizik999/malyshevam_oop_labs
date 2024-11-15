class SplitSystem:
    def __init__(self):
        self.is_on = False
        self.mode = None
        self.temperature = None

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            self.mode = "cool"
            self.temperature = 22  # Начальная температура
            print("Сплит-система включена. Режим: cool, Температура: 22°C")
        else:
            print("Сплит-система уже включена.")

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print("Сплит-система выключена.")
        else:
            print("Сплит-система уже выключена.")

    def set_cooling_temperature(self, temperature):
        if self.is_on and self.mode == "cool":
            self.temperature = temperature
            print(f"Температура охлаждения установлена на {temperature}°C.")
        else:
            print("Невозможно установить температуру охлаждения. Сплит-система либо выключена, либо не в режиме охлаждения.")

    def turn_on_cooling(self):
        if not self.is_on:
            self.turn_on()
        elif self.mode != "cool":
            self.mode = "cool"
            print("Режим переключен на cool.")
        else:
            print("Система уже в режиме охлаждения.")

    def turn_off_cooling(self):
        if self.is_on and self.mode == "cool":
            self.turn_off()
        else:
            print("Невозможно выключить режим охлаждения. Сплит-система либо выключена, либо не в режиме охлаждения.")

    def turn_on_heating(self):
        if not self.is_on:
            self.is_on = True
            self.mode = "обогрев"
            self.temperature = 25  # Начальная температура для обогрева
            print("Сплит-система включена. Режим: обогрев, Температура: 25°C")
        elif self.mode != "обогрев":
            self.mode = "обогрев"
            print("Режим переключен на обогрев.")
        else:
            print("Система уже в режиме обогрева.")

    def turn_off_heating(self):
        if self.is_on and self.mode == "обогрев":
            self.turn_off()
        else:
            print("Невозможно выключить режим обогрева. Сплит-система либо выключена, либо не в режиме обогрева.")


# Пример использования класса SplitSystem

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
