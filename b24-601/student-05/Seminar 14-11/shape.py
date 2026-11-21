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

    # @abstractmethod
    # def scale(self, factor: float | int) -> None:
    #     pass
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
    # def scale(self, factor: float | int) -> None:
    #     self._width*=factor
    #     self._height*=factor


class Cirlcle(Shape):
    def __init__(self, radius):
        self._radius = 0
        if radius < 0:
            raise ValueError("Радиус должен быть больше нуля")
        self._radius = radius
    def __str__(self) -> str:
        return (f"{super().__str__()}\n"
                f"Ширина = {self._radius}")
    def area(self) -> float|int:
        return pi*self._radius**2
    def perimeter(self) -> float|int:
        return 2*pi*self._radius
    # def scale(shape: Shape, factor: float | int) -> None:

if __name__ == '__main__':
    req = Rectange(1,1)
    print(req.area)
    # cir = Cirlcle(2)
    # req.scale(5)
    # print('after scaling')
    # print(req)
