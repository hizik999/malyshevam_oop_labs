import random


class Vagon:
    # Общие атрибуты
    NumList = [f"Вагон_{i + 1}" for i in range(14)]
    MasList = ["Станки", "Автозапчасти", "Бумага", "Керамическая плитка"]

    def __init__(self, num, cargo):
        self.num = num
        self.cargo = cargo

    def __str__(self):
        return f"{self.num} - {self.cargo}"


class TrainsOfVagon:
    def __init__(self):
        self.train = [Vagon(random.choice(Vagon.NumList), random.choice(Vagon.MasList)) for _ in range(56)]

    def shuffle(self):
        random.shuffle(self.train)

    def get(self, i):
        if 0 <= i < len(self.train):
            return self.train[i]
        else:
            raise IndexError("Номер вагона вне допустимых значений")


def main():
    train = TrainsOfVagon()
    train.shuffle()
    used_vagons = set()

    while len(used_vagons) < len(train.train):
        try:
            user_input = input("Введите номер вагона (0-55) или 'exit' для завершения: ")
            if user_input.lower() == 'exit':
                break

            vagon_number = int(user_input)
            if vagon_number in used_vagons:
                print("Этот вагон уже был выбран.")
                continue

            vagon = train.get(vagon_number)
            print(vagon)
            used_vagons.add(vagon_number)
        except ValueError:
            print("Пожалуйста, вводите корректный номер вагона.")
        except IndexError as e:
            print(e)

    print("Выбор вагонов завершен.")


if __name__ == "__main__":
    main()
