# 2. Реализуйте абстрактный базовый класс Shape (фигура), а от него унаследуйте
# классы Rectangle (прямоугольник) и Circle (круг). Класс Shape должен иметь
# абстрактный метод area, который должен быть реализован в каждом дочернем классе.
# Классы Rectangle и Circle также должны иметь метод perimeter для расчета
# периметра. Выведите площадь и периметр прямоугольника и круга на экран.


# Пример использования:


# rectangle = Rectangle(5, 3)

# circle = Circle(2)

# # Вывод: Rectangle area: 15
# print(f"Rectangle area: {rectangle.area()}")

# # Вывод: Rectangle perimeter: 16
# print(f"Rectangle perimeter: {rectangle.perimeter()}")

# # Вывод: Circle area: 12.566370614359172
# print(f"Circle area: {circle.area()}")

# # Вывод: Circle perimeter: 12.566370614359172
# print(f"Circle perimeter: {circle.perimeter()}")

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


class Circle(Shape):
    def __init__(self, diameter):
        self.diameter = diameter

    def area(self):
        radius = self.diameter / 2
        return 3.14 * radius ** 2

    def perimeter(self):
        return 3.14 * self.diameter


# Пример использования
shapes = [Rectangle(7, 4), Circle(6)]

for shape in shapes:
    print(f"Площадь: {shape.area()}, Периметр: {shape.perimeter()}")
