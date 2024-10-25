import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_circle_area(self):
        return math.pi * (self.radius ** 2)
    
    def calculate_circle_perimetr(self):
        return 2 * math.pi * self.radius
    

for i in range(10):
    x = int(input("Введите радиус: "))
    circle = Circle(x)
    print("Площадь окружности равна:", circle.calculate_circle_area())
    print("Периметр окружности равен:", circle.calculate_circle_perimetr())