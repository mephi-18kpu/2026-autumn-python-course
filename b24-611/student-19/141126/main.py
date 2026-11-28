class Shape:
    def __init__(self):
        raise TypeError("ельзя напрям создавать экземпляры класса Shape")

    def __str__(self) -> str:
        return type(self).__name__

    def area(self) -> float|int:
        pass

    def perimeter(self) -> float:
        pass

    def scale(self, factor: float|int):
        pass

class Rectangle(Shape):
    def __init__(self, width: float|int, height: float|int):
        if width <0 or height < 0:
            raise ValueError("no")

        self._width = width
        self._height = height

    def __str__(self) -> str:
        return (f"{super().__str__()}\n"
                f"| width = {self._width}\n"
                f"| height = {self._height}")

    def area(self) -> float|int:
        return self._width * self._height

    def scale(self, factor) -> float|int:
        return (f"{super().__str__()}scaled \n"
                f"| width scaled = {self._width * factor}\n"
                f"| height scaled = {self._height * factor}")

    def perimeter(self) -> float|int:
        return 2 * (self._width + self._height)

class Circle(Shape):
    def __init__(self, radius: float|int):
        if radius <0 :
            raise ValueError("no")

        self._radius = radius

    def scale(self, factor) -> float|int:
        return (f"{super().__str__()}scaled \n"
                f"| radius scaled = {self._radius * factor}")



    def __str__(self) -> str:
        return (f"{super().__str__()}\n"

                f"| radius = {self._radius}")

    def area(self) -> float|int:
        return self._radius * self._radius * 3.141

    def perimeter(self) -> float|int:
        return 2 * self._radius * 3.141


def calc_sum_perimetr(shapes: list[Shape]) -> float | int:
    total = 0
    for shape in shapes:
        total += shape.perimeter()
    return total

def calc_sum_area(shapes: list[Shape]) -> float | int:
    total = 0
    for shape in shapes:
        total += shape.area()
    return total


shapes = []
shape = Rectangle(2, 3)
shapes.append(shape)

shapec = Circle(2)
shapes.append(shapec)

print(shape)
print("площадь: ", shape.area())
print("периметр: ", shape.perimeter())
print(shapec)
print("площадь: ", shapec.area())
print("периметр: ", shapec.perimeter())
print(shape.scale(2))
print(shapec.scale(2))
print("сумма периметров", calc_sum_perimetr(shapes))
print("сумма площадей", calc_sum_area(shapes))


