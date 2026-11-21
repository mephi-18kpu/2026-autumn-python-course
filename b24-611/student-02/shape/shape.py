import numpy as np

class Shape:
    def __init__(self):
        raise TypeError("нельзя напрямую создавтать экземпляры класса shape")

    def __str__(self) -> str:
        return type(self).__name__

    def area(self) -> float|int:
        pass

    def perimeter(self) -> float|int:
        pass


class Rectangle(Shape):
    def __init__(self, width: float|int, height: float|int):
        if width < 0 or height < 0:
            raise ValueError("нельзя отрицательные параметры прямоугольника")

        self._width = width
        self._height = height

    def __str__(self) -> str:
        return (f"{super().__str__()}\n"
                f"| width = {self._width}\n"
                f"| height = {self._height}")

    def area(self) -> float|int:
        return self._width * self._height

    def perimeter(self) -> float|int:
        return 2 * self._width + 2 * self._height


shape = Rectangle(width=5, height=3)
print(shape)
print(shape.area())
print(shape.perimeter())


class Circle(Shape):
    def __init__(self, radius: float | int):
        if radius < 0:
            raise ValueError("нельзя задать отрицательные параметры окружности")

        self._radius = radius

    def __str__(self) -> str:
        return (f"{super().__str__()}\n"
                f"| radius = {self._radius}\n")

    def area(self) -> float | int:
        return self._radius**2 * np.pi

    def perimeter(self) -> float|int:
        return self._radius * 2 * np.pi

shape = Circle(radius = 9)
print(shape)
print(shape.area())
print(shape.perimeter())
