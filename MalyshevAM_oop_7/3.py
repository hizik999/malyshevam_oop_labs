class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def giveRaise(self, percent):
        self.salary += self.salary * percent / 100

    def work(self):
        print(f"{self.name} работает.")

    def __repr__(self):
        return f"Employee: {self.name}, Salary: {self.salary}"


class Chef(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def work(self):
        print(f"{self.name} готовит еду.")


class Server(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def work(self):
        print(f"{self.name} обслуживает клиентов.")


class PizzaRobot(Chef):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def work(self):
        print(f"{self.name} готовит пиццу.")


bob = PizzaRobot("Bob", 50000)
bob.work()
bob.giveRaise(10)
print(bob)

employees = [
    Employee("Alice", 40000),
    Chef("Charlie", 60000),
    Server("Dave", 30000),
    PizzaRobot("Bob", 50000)
]

for employee in employees:
    employee.work()
    print(employee)
