class Person:
    def __init__(self, name, job, pay):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_rise(self, percent):
        self.pay += self.pay * percent / 100

    def __repr__(self):
        return f"Person: {self.name}, Job: {self.job}, Pay: {self.pay}"


class Manager(Person):
    def __init__(self, name, job, pay):
        super().__init__(name, job, pay)

    def give_rise(self, percent, bonus=5000):
        super().give_rise(percent)
        self.pay += bonus


person = Person("John Doe", "Engineer", 50000)
manager = Manager("Jane Smith", "Manager", 80000)

print(person)
print(manager)

person.give_rise(10)
manager.give_rise(10)

print(person)
print(manager)
