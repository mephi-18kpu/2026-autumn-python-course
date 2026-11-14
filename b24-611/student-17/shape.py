import numpy as np

class Shape:
    def __init__(self):
        raise TypeError("Нельзя создавать напрямую экземпляры класса Shape")

    def __str__(self) -> str:
        return type(self).__name__

    def area(self) -> float|int:
        pass

    def perimetr(self) -> float|int:
        pass

class Rectangle(Shape):
    def __init__(self, width: float|int, height: float|int):
        if width < 0 or height < 0:
            raise ValueError("Нельзя задавать отрицательные параметры прямоугольника")

        self._width = width
        self._height = height

    def __str__(self) -> str:
        return(f"{super().__str__()}\n"
               f"| width = {self._width}\n"
               f"| height = {self._height}")

    def area(self) -> float|int:
        return self._width * self._height

class  Circle:
    def __init__(self, radius: float|int):
        if radius < 0:
            raise ValueError("Нельзя задать отрицательный радиус")

        self._radius = radius

    def __str__(self) -> str:
        return(f"{super().__str__()}\n"
               f"| radius = {self._radius}\n")

    def area(self) -> float|int:
        return np.pi * self._radius ** 2

    def perimetr(self) -> float|int:
        return 2 * (np.pi * self._radius ** 2)

shape = Circle(6)
print(shape)


