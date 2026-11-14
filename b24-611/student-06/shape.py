import numpy as np


class Shape:
    def __init__(self):
       raise TypeError("Нельзя напрямую создавать экземпляры класса Shape")

    def __str__(self) -> str:
        return type(self).__name__

    def area(self) -> float:
        pass

    def perimeter(self) -> float:
        pass

    def scale(self, factor: float):
        pass

class Rechtangle(Shape):
    def __init__(self, width: float, height: float):
        if width<0 or height<0:
            raise ValueError("Нельзя задавать отрицательные параметры прямоугольника")
        self._width=width
        self._height=height

    def __str__(self) -> str:
        return (f"{super().__str__()}\n"
                f"| width = {self._width}\n"
                f"| height = {self._height}\n")

    def area(self) -> float:
        return self._width * self._height

    def perimeter(self) -> float:
        return 2*self._width + 2* self._height

class Circle(Shape):
    def __init__(self, radius: float):
        if radius<0:
            raise ValueError("Нельзя задавать отрицательный радиус")
        self._radius=radius

    def __str__(self) -> str:
        return (f"{super().__str__()}\n"
                f"| radius = {self._radius}\n")

    def area(self) -> float:
        return np.pi*self._radius**2

    def perimeter(self) -> float:
        return 2*np.pi*self._radius


def calc_sum_perimeter(shapes: list[Shape]) -> float:
    for shape in Shape:

    return rech_perimeter + cir_perimeter

shape_list = [
    Rechtangle(2,5),
    Circle(3)
]
print(calc_sum_perimeter(shape_list))
