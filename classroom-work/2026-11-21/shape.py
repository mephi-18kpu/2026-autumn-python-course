from abc import ABC, abstractmethod

class Shape(ABC):
    def __str__(self) -> str:
        return type(self).__name__

    @abstractmethod
    @property
    def area(self) -> float|int:
        pass

    @abstractmethod
    @property
    def perimeter(self) -> float|int:
        pass

    # @abstractmethod
    # def scale(self, factor: float|int):
    #     pass


class Rectangle(Shape):
    def __init__(self, width: float|int, height: float|int):
        if width < 0 or height < 0:
            raise ValueError("Нельзя задавать отрицательные параметры прямоугольника")

        self._width = width
        self._height = height

    def __str__(self) -> str:
        return (f"{super().__str__()}\n"
                f"| width  = {self._width}\n"
                f"| height = {self._height}")

    @property
    def area(self) -> float|int:
        return self._width * self._height

    @property
    def perimeter(self) -> float|int:
        return 2 * (self._width + self._height)


shape = Rectangle(2, 3)
print(shape.area)
