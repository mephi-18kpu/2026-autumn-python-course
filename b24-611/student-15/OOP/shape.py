class Shape:
    def __init__(self):
        raise TypeError ("Нельзя напрямую создавать экземпляры класса Shape")

    def __str__(self) -> str:
        return type(self).__name__

    def area(self) ->float:
        pass

    def perimetr(self) ->float:
        pass


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        if width <0 or height<0:
            raise ValueError("Nevernaia visota ili shirina")

        self._width = width
        self._height = height

    def __str__(self) -> str:
        return(f"{super().__str__()}\n"
               f"| width = {self._width}\n"
               f"| height = {self._height}")

    def area(self) ->float:
        return self._width * self._height

    def perimetr(self) ->float:
        return 2*(self._width+self._height)

shape = Rectangle(2, 3)
print(shape)
