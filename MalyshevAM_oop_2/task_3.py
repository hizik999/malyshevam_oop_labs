from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")

    def calculate_age(self, current_date):
        age = current_date.year - self.date_of_birth.year
        if (current_date.month, current_date.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age


person1 = Person("Иван", "Россия", "1990-05-12")
person2 = Person("Мария", "США", "1995-08-25")
person3 = Person("Петр", "Канада", "1980-02-15")

current_date = datetime.now()

print("Имя:", person1.name)
print("Страна:", person1.country)
print("Дата рождения:", person1.date_of_birth.strftime("%Y-%m-%d"))
print("Возраст:", person1.calculate_age(current_date))
print()

print("Имя:", person2.name)
print("Страна:", person2.country)
print("Дата рождения:", person2.date_of_birth.strftime("%Y-%m-%d"))
print("Возраст:", person2.calculate_age(current_date))
print()

print("Имя:", person3.name)
print("Страна:", person3.country)
print("Дата рождения:", person3.date_of_birth.strftime("%Y-%m-%d"))
print("Возраст:", person3.calculate_age(current_date))
