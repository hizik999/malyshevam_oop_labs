from random import randint


class Soldier:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def set_name(self, name):
        self.name = name

    def attack(self, other):
        """Атака на другого солдата, уменьшение его здоровья."""
        damage = randint(10, 30)
        other.health -= damage
        print(f"{self.name} атаковал {other.name} и нанес {damage} урона.")
        if other.health < 0:
            other.health = 0
        print(f"Здоровье {other.name}: {other.health}\n")


class Battle:
    def __init__(self, soldier1, soldier2):
        self.soldier1 = soldier1
        self.soldier2 = soldier2
        self.result = None

    def battle(self):
        """Моделирование сражения между двумя солдатами."""
        while self.soldier1.health > 0 and self.soldier2.health > 0:
            attacker = randint(1, 2)
            if attacker == 1:
                self.soldier1.attack(self.soldier2)
            else:
                self.soldier2.attack(self.soldier1)

        # Определение победителя
        if self.soldier1.health > 0:
            self.result = self.soldier1.name
        else:
            self.result = self.soldier2.name

    def who_win(self):
        """Вывод победителя сражения."""
        if self.result:
            print(f"Победитель: {self.result}")
        else:
            print("Сражение не было проведено.")


def main():
    # Создание двух солдат
    soldier1 = Soldier("Алексей")
    soldier2 = Soldier("Борис")

    # Создание сражения
    battle = Battle(soldier1, soldier2)

    # Моделирование сражения
    battle.battle()

    # Вывод победителя
    battle.who_win()


if __name__ == "__main__":
    main()
