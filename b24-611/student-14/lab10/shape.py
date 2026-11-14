from numpy import pi
class Shape:
    def __init__(self):
        raise TypeError("Нельзя напрямую создавать экземпляры класса Shape")


    def __str__(self)->str:
        return type(self).__name__

    def area(self)->float|int:
        pass

    def perimeter(self):
        pass

    def scale(self, factor: float|int):
        pass


class Rectangle(Shape):

    def __init__(self, width: float|int, height: float|int):
        if width < 0 or height < 0:
            raise ValueError("Нельзя создавать отрицательные параметра прямоугольника")
        self._width = width
        self._height = height

    def __str__(self)->str:
        return (f"{super().__str__()}\n"
                f"| width = {self._width}\n"
                f"| height = {self._height}\n")

    def area(self)->float|int:
        return self._width * self._height

    def perimeter(self)->float|int:
        return 2*(self._width+self._height)

    def scale(self, factor: float|int):
        self._width *= factor
        self._height *= factor


class Circle(Shape):

    def __init__(self, radius: float|int):
        if radius < 0:
            raise ValueError("Нельзя создавать отрицательные параметра прямоугольника")
        self._radius = radius

    def __str__(self)->str:
        return (f"{super().__str__()}\n"
                f"| radius = {self._radius}\n")

    def area(self)->float|int:
        return (self._radius)**2*pi

    def perimeter(self)->float|int:
        return self._radius*2*pi

    def scale(self, factor: float|int):
        self._radius *= factor


def calculate_perimeter(shapes: list[Shape])->float|int:
    summ=0
    for i in range(0, len(shapes)):
        summ += shapes[i].perimeter()
    return summ


figures = [
    Rectangle(2, 3),
    Rectangle(4, 5),
    Circle(5),
    Circle(8)

]

result = calculate_perimeter(figures)

print(result)
