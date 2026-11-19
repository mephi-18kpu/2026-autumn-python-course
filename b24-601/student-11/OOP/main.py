import math

''' ФИГУРА '''
class Shape:
    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    def multiply_scale(self, a):
        if a <= 0:
            raise ValueError("НОЛЬ НЕЛЬЗЯ")
        self._apply_scale(a)

    def _apply_scale(self, a):
        raise NotImplementedError

    def __str__(self) -> str:
        return type(self).__name__

''' ПРЯМОУГОЛЬНИК НАСЛЕДНИК ФИГУРЫ '''
class Rectangle(Shape):
    def __init__(self, width: float|int, height: float|int):
        if width <= 0 or height <= 0:
            raise ValueError("ПОЛОЖИТЕЛЬНО должно быть")
        self._h = height
        self._w = width

    def area(self):
        return self._w * self._h

    def perimeter(self):
        return 2 * (self._w  + self._h)

    def _apply_scale(self, a):
        self._h *= a
        self._w *= a

    def __str__(self):
        shape_name = super().__str__()
        return f"{shape_name} ({self._w} × {self._h})"

''' КРУГ НАСЛЕДНИК ФИГУРЫ '''
class Circle(Shape):
    def __init__(self, r: float|int):
        if r <= 0:
            raise ValueError("ПОЛОЖИТЕЛЬНО должно быть")
        self._r = r

    def area(self):
        return math.pi * (self._r**2)

    def perimeter(self):
        return 2 * math.pi * self._r

    def _apply_scale(self, a):
        self._r *= a

    def __str__(self):
        shape_name = super().__str__()
        return f"{shape_name} ({self._r})"

''' Треугольник НАСЛЕДНИК ФИГУРЫ '''
class Triangle(Shape):
    def __init__(self, height: float|int, base: float|int):
        if height <= 0 or base <= 0:
            raise ValueError("ПОЛОЖИТЕЛЬНО должно быть")
        self._base = base
        self._height = height

    def area(self):
        return float(self._base * self._height) / 2

    def _apply_scale(self, a):
        self._height *= a
        self._base *= a

    def __str__(self):
        shape_name = super().__str__()
        return f"{shape_name} ({self._height} × {self._base})"

def all_areas(l):
    for i in l:
        print(f"{i}: {i.area()}")

if __name__ == "__main__":
    my_bed = Rectangle(4, 3)
    my_pizza = Circle(31)
    my_echpochmak = Triangle(5, 10)

    my_things = [my_bed, my_pizza, my_echpochmak]
    all_areas(my_things)

