import math
class Shape:


    def __init__(self):
        raise TypeError("Нельзя создавать объект Shape напрямую")
    def __str__(self) -> str:
        return type(self).__name__
    def area(self) -> float:
        pass
    def perimeter(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self,width: float, height: float):
        if width < 0 or height < 0:
            raise ValueError("Ширина и высота должны быть выше 0")


        self._width = width
        self._height = height

    def __str__(self) -> str:
        return (f"{super().__str__()}\n"
                f"width: {self._width}\n"
                f"height: {self._height}\n")

    def area(self) -> float:
        return self._width * self._height

    def perimeter(self) -> float:
        return self._width * self._height

    def scale(self, factor: float):
        for size_factor in self.__size_factor:
            size_factor *=
shape = Rectangle(2,3)
print(shape)

class Circle(Shape):
    def __init__(self,radius: float):
        if radius < 0:
            raise ValueError("Радиус не может быть отрицательным")

        self._radius = radius

    def __str__(self) -> str:
        return (f"{super().__str__()}\n"
                f"radius: {self._radius}\n"
                f"center: {self._radius}\n")

    def area(self) -> float:
        return self._radius * 2 * math.pi

    def scale(self, factor: float):
        pass

shape = Circle(2)
print(shape)

