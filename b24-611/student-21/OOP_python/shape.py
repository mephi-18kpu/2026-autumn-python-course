import math
from math import *
class Shape:
    def __init__(self, width: float|int, hight = float|int):
        raise TypeError("Нельзя напрямую создавать экземпляры  класса Shape")

    def __str__(self):
        return type(self).__name__

    def area(self) -> float|int:
        pass

    def perimetr(self) -> float|int:
        pass

class Rectangle(Shape):
    def __init__(self, width: float|int, hight: float|int):
        if width < 0 or hight < 0:
            raise ValueError("Нельзя задавать отрицательные знчения")
        self._width = width
        self._hight = hight

    def __str__(self) -> str:
        return (f"{(super).__str__()}\n"
                f"| width = {self._width}\n"
                f"| height = {self._hight}")

    def area(self) -> float|int:
        return  self._width * self._hight

    def perimetr(self) -> float|int:
        return self._width + self._hight + self._width + self._hight

class Circle(Shape):
    def __init__(self, radius: float|int):
        raise ValueError("Нельзя задавать отрицательные знчения")
        self._radius = radius

    def __str__(self) -> str:
        return (f"{(super).__str__()}\n"
                f"| radius = {self._radius}")

    def area(self) -> float | int:
        return self._radius * self._radius * math.pi

    def perimetr(self) -> float|int:
        return 2 * math.pi * self._radius


def sump(shapes: list[Shape]) -> float|int:
    total = 0
    for shape in shapes:
        total += shape.perimetr()
    return total

def sum_area(shapes: list[Shape]) -> float|int:
    total = 0
    for shape in shapes:
        total += shape.area()
    return total


if __name__ == "__main__":
    try:
        rect1 = Rectangle(2, 5)
        rect2 = Rectangle(228, 228)
        circ1 = Circle(8)
        shapes = [rect1, rect2, circ1]

        totalp = sump(shapes)
        totals = sum_area(shapes)

        print(f"суммарный периметр {totalp}\n")
        print(f"суммарный периметр {totalp}\n")
    except ValueError as e:
        print(f"Ошибка при создании фигуры - {e}")

