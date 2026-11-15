import numpy as np

class Shape:
    def __init__(self):
        raise TypeError("Нельзя напрямцю создавть эксзмпляры класса Shape")

    def __str__(self) -> str:
        return type(self).__name__

    def area(self) -> float|int:
        pass

    def perimetr(self) -> float|int:
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        if width < 0 or height < 0:
            raise ValueError("Нельзя задавать отрицательные значения для высоты и ширины")

        self._width = width
        self._height = height

    def __str__(self) -> str:
        return (f"{super().__str__()}\n"
                f"| width = {self._width}\n"
                f"| height = {self._height}")

    def area(self) -> float|int:
        return self._width * self._height

    def perimetr(self) -> float|int:
        return 2 * (self._width + self._height)

class Round(Shape):
    def __init__(self, radius: float):
        if radius < 0:
            raise ValueError("Нельзя задавать отрицательные значения для радиуса")

        self._radius = radius


    def __str__(self) -> str:
        return (f"{super().__str__()}\n"
                f"| radius = {self._width}\n")

    def area(self) -> float|int:
        return self._radius * 3.14 * 2

    def perimetr(self) -> float|int:
        return 3.14 * self._radius ** 2

def caluclate_sum_perimetr(l: list[Shape]) -> float|int:
    values = []
    for i in l:
        values.append(i.perimetr())

    print(sum(values))
    return sum(values)



shape = Rectangle(2,5)
list1 = [Rectangle(2,3),Round(9),Rectangle(2,4)]
print(shape)
print(shape.area())
print(shape.perimetr())
caluclate_sum_perimetr(list1)
