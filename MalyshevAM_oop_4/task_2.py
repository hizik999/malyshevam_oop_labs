class WinDoor:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Room:
    """Класс, представляющий комнату, в которой могут быть окна и двери."""

    def __init__(self, length, width, height):
        self.length = length  # Длина комнаты
        self.width = width  # Ширина комнаты
        self.height = height  # Высота комнаты
        self.wd_list = []  # Список окон и дверей (экземпляры класса WinDoor)

    def add_windoor(self, width, height):
        """Метод для добавления окна или двери в комнату."""
        self.wd_list.append(WinDoor(width, height))

    def total_area(self):
        """Метод для расчета общей площади стен комнаты."""
        # Площадь стен комнаты = 2*(длина + ширина) * высота
        return 2 * (self.length + self.width) * self.height

    def work_surface_area(self):
        """Метод для расчета площади стен под оклейку обоями,
        за вычетом площади окон и дверей."""
        # Общая площадь стен минус площадь всех окон и дверей
        return self.total_area() - sum([wd.square for wd in self.wd_list])

    def wallpaper_rolls_needed(self, roll_width, roll_length):
        """Метод для расчета необходимого количества рулонов обоев с учетом реальной логики."""
        # Периметр комнаты = 2*(длина + ширина)
        perimeter = 2 * (self.length + self.width)

        # Число полос обоев, которые понадобятся для оклейки по периметру
        strips_needed = perimeter // roll_width

        # Количество полос, которое можно получить из одного рулона
        strips_per_roll = roll_length // self.height

        # Общее количество рулонов
        rolls_needed = strips_needed / strips_per_roll

        return round(rolls_needed + 0.5)  # Округляем в большую сторону


# Основная программа для расчета площади под оклейку и необходимого количества рулонов обоев
if __name__ == "__main__":
    # Ввод параметров комнаты
    length = float(input("Введите длину комнаты (в метрах): "))
    width = float(input("Введите ширину комнаты (в метрах): "))
    height = float(input("Введите высоту комнаты (в метрах): "))

    # Создание экземпляра класса Room
    room = Room(length, width, height)

    # Добавление окон и дверей
    while True:
        action = input("Добавить окно или дверь? (да/нет): ").strip().lower()
        if action == 'нет':
            break
        width_wd = float(input("Введите ширину окна/двери (в метрах): "))
        height_wd = float(input("Введите высоту окна/двери (в метрах): "))
        room.add_windoor(width_wd, height_wd)

    # Ввод параметров обоев
    roll_width = float(input("Введите ширину рулона обоев (в метрах): "))
    roll_length = float(input("Введите длину рулона обоев (в метрах): "))

    # Вывод количества необходимых рулонов обоев
    print(f"Необходимое количество рулонов обоев: {room.wallpaper_rolls_needed(roll_width, roll_length)}")
