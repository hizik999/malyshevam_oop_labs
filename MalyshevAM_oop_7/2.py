class Equipment:
    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year

    def action(self):
        return "Не определено"

    def __str__(self):
        return f"Equipment: {self.name}, Make: {self.make}, Year: {self.year}"


class Printer(Equipment):
    def __init__(self, name, make, year, series):
        super().__init__(name, make, year)
        self.series = series

    def action(self):
        return "Печатает"

    def __str__(self):
        return f"Printer: {self.name} (Series: {self.series}), Make: {self.make}, Year: {self.year}"


class Scaner(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return "Сканирует"


class Xerox(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return "Копирует"


sklad = [
    Printer("HP LaserJet", "HP", 2021, "P1102"),
    Scaner("Canon Scan", "Canon", 2020),
    Xerox("Xerox WorkCentre", "Xerox", 2019)
]

for equipment in sklad:
    print(equipment.action())

sklad = [item for item in sklad if not isinstance(item, Printer)]

print('Вывод оставшихся объектов после удаления Printer:')
for equipment in sklad:
    print(equipment.action())
