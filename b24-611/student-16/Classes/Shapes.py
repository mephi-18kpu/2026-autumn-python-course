import numpy as np
from math import pi

class Shape:
    def __init__(self):
        raise TypeError("не тот тип, нужен конкретный наследник")

    def __str__(self) -> str:
        return type(self).__name__

    def area(self) -> float:
        pass

    def perimetr(self)->float:
        pass


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        if width < 0 or height<0:
            raise ValueError("Отрицательные значения")
        self._width = width
        self._height = height

    def __str__(self) -> str:
        return (f"{super().__str__()}\n"
                f"| width = {self._width}\n"
                f"| height = {self._height}\n")

    def area(self) -> float:
        return (self._width * self._height)

    def perimetr(self)->float:
        return (self._width + self._height)

    def scale(self, factor: float) -> None:
        if factor <= 0:
            raise ValueError("Фактор строго положителен!")

        self._width = self._width * factor
        self._height = self._height * factor

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        if radius < 0:
            raise ValueError("Радиус меньше нуля")
        self._radius = radius

    def __str__(self) -> str:
        return (f"{super().__str__()}\n"
                f" radius = {self._radius}\n")

    def area(self) -> float:
        return pi * self._radius**2


r1 = Rectangle(2, 6)
r2 = Rectangle(4, 5)

print(r1)
print("Площадь: ", r1.area())
print("периметр: ", r1.perimetr())

print("\n***\n")

print(r2)
print("Площадь: ", r2.area())
print("периметр: ", r2.perimetr())

r3 = Rectangle(3, 4)
r3.scale(2)
print("\n")
print(r3)
print("Площадь: ", r3.area())
print("периметр: ", r3.perimetr())

try:
    r3.scale(0)
except ValueError as e:
    print("Ошибка ", e)
    print("Площадь: ", r3.area())
    print("периметр: ", r3.perimetr())
