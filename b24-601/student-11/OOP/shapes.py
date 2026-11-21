import math
from abc import ABC, abstractmethod

''' ФИГУРА '''
class Shape(ABC):
    def __str__(self) -> str:
        return type(self).__name__

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def multiply_scale(self, a):
        if a <= 0:
            raise ValueError("НОЛЬ НЕЛЬЗЯ")
        self._apply_scale(a)

    @abstractmethod
    def _apply_scale(self, a):
        pass


''' ПРЯМОУГОЛЬНИК НАСЛЕДНИК ФИГУРЫ '''
class Rectangle(Shape):
    def __init__(self, width: float | int, height: float | int):
        if width <= 0 or height <= 0:
            raise ValueError("ПОЛОЖИТЕЛЬНО должно быть")
        self._h = height
        self._w = width

    def __str__(self):
        shape_name = super().__str__()
        return f"{shape_name} ({self._w} × {self._h})"

    def area(self):
        return self._w * self._h

    def perimeter(self):
        return 2 * (self._w + self._h)

    def _apply_scale(self, a):
        self._h *= a
        self._w *= a


''' КРУГ НАСЛЕДНИК ФИГУРЫ '''
class Circle(Shape):
    def __init__(self, r: float | int):
        if r <= 0:
            raise ValueError("ПОЛОЖИТЕЛЬНО должно быть")
        self._r = r

    def __str__(self):
        shape_name = super().__str__()
        return f"{shape_name} ({self._r})"

    def area(self):
        return math.pi * (self._r ** 2)

    def perimeter(self):
        return 2 * math.pi * self._r

    def _apply_scale(self, a):
        self._r *= a


''' Треугольник НАСЛЕДНИК ФИГУРЫ '''
class Triangle(Shape):
    def __init__(self, height: float | int, base: float | int):
        if height <= 0 or base <= 0:
            raise ValueError("ПОЛОЖИТЕЛЬНО должно быть")
        self._base = base
        self._height = height

    def __str__(self):
        shape_name = super().__str__()
        return f"{shape_name} ({self._height} × {self._base})"

    def area(self):
        return float(self._base * self._height) / 2

    def _apply_scale(self, a):
        self._height *= a
        self._base *= a

    def perimeter(self):
        return "Нет возможности считать периметр треугольника из-за недостатка данных"




def all_areas(l):
    for i in l:
        print(f"{i}: {i.area()}")
        print(f"{i}: {i.area()}")
