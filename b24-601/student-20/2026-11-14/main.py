import math as m

class Shape:
    def __init__(self, *, size_factors:list):
        #raise TypeError("Нельзя создавать объект shape на прямую.")
        self.__size_factors = size_factors

    def __str__(self) -> str:
        return type(self).__name__

    def area(self) -> float|int:
        pass

    def perimeter(self) -> float|int:
        pass

    def scale(self, factor: float|int) -> list:
        for index in range (len(self.__size_factors)):
            self.__size_factors *= factor
        return self.__size_factors

class Rectangle(Shape):
    def __init__(self, width,  height, ) -> None:
        if width < 0 or height < 0:
            raise ValueError("Ширина и высота должны быть больше 0!")

        self._width = width
        self._height = height

        super().__init__(size_factors=[self._width, self._height])

    def __str__(self) -> str:
        return (f"{super().__str__()}\n"
                f"width = {self._width}\n"
                f"height = {self._height}\n")

    def area(self) -> float|int:
        return self._width * self._height

    def perimeter(self) -> float|int:
        return 2 * (self._width + self._height)

    #def scale(self, factor: float|int) -> None:
        self._width += factor
        self._height += factor
        return None

class Circle(Shape):
    def __init__(self, radius) -> None:
        if radius < 0:
            raise ValueError("Радиус должен быть больше 0!")

        self._radius = radius

        super().__init__(size_factors=[self._radius])

    def __str__(self) -> str:
        return (f"{super().__str__()}\n"
                f"radius = {self._radius}\n")

    def area(self) -> float|int:
        return m.pi * self._radius **2

    def perimeter(self) -> float|int:
        return 2 * m.pi * self._radius

    #def scale(self, factor: float|int) -> None:
        self._radius += factor
        return None


shape_1 = Rectangle(2,14)
print(shape_1)
print(shape_1.area())
print(shape_1.perimeter())
print()

shape_2 = Circle(2)
print(shape_2)
print(shape_2.area())
print(shape_2.perimeter())
print()

print(shape_1.scale(2))

