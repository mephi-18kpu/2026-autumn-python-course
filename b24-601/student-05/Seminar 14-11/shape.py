# from curses.textpad import rectangle

from numpy import pi
from abc import ABC, abstractmethod
class Shape(ABC):
    # def __init__(self, *, size_factors: list):
    #     self.__size_factors = size_factors
    def __str__(self) -> str:
        return type(self).__name__

    @abstractmethod
    def area(self) -> float|int:
        pass

    @abstractmethod
    def perimeter(self) -> float|int:
        pass

    @abstractmethod
    def scale(self, factor: float | int) -> None:
        if factor <= 0:
            raise ValueError(f'Масштаб должен быть положительным! Введено {factor}!')
        pass
class Rectange(Shape):
    def __init__(self, width, height):
        self._height = 0
        self._width = 0
        if width < 0 or height < 0:
            raise ValueError("Ширина и высота должны быть больше нуля")
        self._width = width
        self._height = height
        super().__init__()

    def __str__(self) -> str:
        return(f"{super().__str__()}\n"
               f"Ширина = {self._width}\n"
               f"Высота = {self._height}")

    @property
    def area(self) -> float|int:
        return self._width * self._height

    @property
    def perimeter(self) -> float|int:
        return 2 * (self._width + self._height)
    def scale(self, factor: float | int) -> None:
        super().scale(factor)
        self._width*=factor
        self._height*=factor


class Cirlcle(Shape):
    def __init__(self, radius):
        self._radius = 0
        if radius < 0:
            raise ValueError("Радиус должен быть больше нуля")
        self._radius = radius

    def __str__(self) -> str:
        return (f"{super().__str__()}\n"
                f"Радиус = {self._radius}")
    @property
    def area(self) -> float|int:
        return pi*self._radius**2
    @property
    def perimeter(self) -> float|int:
        return 2*pi*self._radius

    def scale(self, shape: Shape, factor: float | int) -> None:
        super().scale(factor)
        self._radius*=factor


class Triangle(Shape):
    def __init__(self, foundation, height):
        self._foundation = foundation
        self._height = height
        if foundation < 0:
            raise ValueError("Основание должно быть больше нуля")
        if height < 0:
            raise ValueError("Высота должна быть больше нуля")

    def __str__(self) -> str:
        return (f"{super().__str__()}\n"
                f"Основание = {self._foundation}\n"
                f"Высота = {self._height}")
    @property
    def area(self) -> float|int:
        return self._foundation*self._height/2

    def perimeter(self) -> float|int:
        super().perimeter()

    def scale(self, shape: Shape, factor: float | int) -> None:
        super().scale(factor)
        self._foundation*=factor
        self._height*=factor

def print_all_areas(shapes: list[Shape]) -> None:
    for shape in shapes:
        print(f'{shape.area}')


if __name__ == '__main__':
    rec = Rectange(3, 4)
    cir = Cirlcle(1)
    tri = Triangle(6, 4)
    print_all_areas([rec, cir, tri])
