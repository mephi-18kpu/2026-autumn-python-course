import math
from typing import Union, List

class Shape:
    def __init__(self):
        raise TypeError("Нельзя напрямую создавать экземпляры класса Shape")

    def __str__(self) -> str:
        return type(self).__name__

    def area(self) -> Union[float, int]:
        pass

    def perimetr(self) -> Union[float, int]:
        pass


class Rectangle(Shape):
    def __init__(self, width: Union[float, int], height: Union[float, int]):
        if width < 0 or height < 0:
            raise ValueError("Нельзя задавать отрицательные значения")
        self._width = width
        self._height = height

    def width(self) -> Union[float, int]:
        return self._width

    def height(self) -> Union[float, int]:
        return self._height

    def __str__(self) -> str:
        return (f"{super().__str__()}\n"
                f"| width = {self._width}\n"
                f"| height = {self._height}")

    def area(self) -> Union[float, int]:
        return self._width * self._height

    def perimetr(self) -> Union[float, int]:
        return self._width + self._height + self._width + self._height


class Circle(Shape):
    def __init__(self, radius: Union[float, int]):
        if radius < 0:
            raise ValueError("Нельзя задавать отрицательные значения")
        self._radius = radius

    def radius(self) -> Union[float, int]:
        return self._radius

    def __str__(self) -> str:
        return (f"{super().__str__()}\n"
                f"| Radius = {self._radius}")

    def area(self) -> Union[float, int]:
        return self._radius * self._radius * math.pi

    def perimetr(self) -> Union[float, int]:
        return 2 * math.pi * self._radius


def sum_p(shapes: List[Shape]) -> Union[float, int]:
    return sum(shape.perimetr() for shape in shapes)

def sum_s(shapes: List[Shape]) -> Union[float, int]:
    return sum(shape.area() for shape in shapes)

if __name__ == "__main__":
    try:
        rect1 = Rectangle(10, 5)
        rect2 = Rectangle(3, 7)
        circle1 = Circle(4.5)
        my_shapes = [rect1, rect2, circle1]
        total = sum_p(my_shapes)

        print(f"Суммарный периметр всех фигур: {total:.2f}")
        total = sum_s(my_shapes)
        print(f"Суммарный сумма всех фигур: {total:.2f}")

    except ValueError as e:
        print(f"Ошибка при создании фигуры: {e}")
