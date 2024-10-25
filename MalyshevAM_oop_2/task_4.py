import math

class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3


circle = Circle(7)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4, 5, 6, 7)

print("Окружность:")
print("Площадь:", circle.calculate_area())
print("Периметр:", circle.calculate_perimeter())

print("\nПрямоугольник:")
print("Площадь:", rectangle.calculate_area())
print("Периметр:", rectangle.calculate_perimeter())

print("\nТреугольник:")
print("Площадь:", triangle.calculate_area())
print("Периметр:", triangle.calculate_perimeter())