class Shape:
    def __init__(self):
        raise TypeError("Нельзя создать объект Shape напрямую")

    def __str__(self) -> str:
        return type(self).__name__

    def area(self) -> float:
        pass

    def perimeter(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise  ValueError("Ало они кароче больше нуля должны быть болван")

        self._width = width
        self._height = height

    def __str__(self) -> str:
        return (f"{super().__str__()}\n"
                f"width = {self._width}\n"
                f"height = {self._height}\n")

    def area(self) -> float:
        return self._height*self._width

    def perimeter(self) -> float:
        return 2*(self._width+self._height)


shape = Rectangle(2, 3)
print(shape)

class Circle(Shape):
    def __init__(self, radius):
        if radius < 0:
            raise  ValueError("Ало он кароче больше нуля должен быть болван")

        self._radius = radius

    def __str__(self) -> str:
        return (f"{super().__str__()}\n"
                f"radius = {self._radius}\n")

    def area(self) -> float:
        return 3.14*self._radius*self._radius

    def perimeter(self) -> float:
        return 2*3.14*self._radius

shape = Circle(5)
print(shape.area())