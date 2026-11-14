class Shape: #5 usages
    def __init__(self, *, size_factors: list):
        self.__size_factors = size_factors

    def __str__(self) -> str:
        return type(self).__name__

    def area(self) -> float|int: #2 usages (2 dynamic)
        pass

    def perimetr(self) -> float|int:
        pass

    def scale(self, factor: float | int) -> None:
        for index in range(len(self.__size_factors)):
            size_factors *= factor



class Rectangle(Shape):
    def __init__(self, width: float|int, height: float|int):
        if width < 0 or height < 0:
            raise ValueError("Ширина и высота должны быть больше 0")

        self._width = width
        self._height = height

        super().__init__(size_factors=[self._width, self._height])

    def __str__(self) -> str:
        return(f"{super().__str__()}\n"
               f"width = {self._width}\n"
               f"height = {self._height}")

    def area(self) -> float|int:
        return self._width * self._height

    def perimetr(self) -> float|int:
        return 2 * (self._width + self._height)


class Circle(Shape):
    def __init__(self, x0: float|int, y0: float|int, radius: float|int):
        if radius < 0:
            raise ValueError("Радиус должен быть больше 0")

        self._x0 = x0
        self._y0 = y0
        self._radius = radius

    def __str__(self) -> str:
        return (f"{super().__str__()}\n"
                f"x0 = {self._x0}\n"
                f"y0 = {self._y0}\n"
                f"radius = {self._radius}")

    def area(self) -> float|int:
        return pi * self._radius ** 2

    def perimetr(self) -> float|int:
        return 2 * pi * self._radius


