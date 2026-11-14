from math import *
class Shape:
    #def __init__(self):
        #raise TypeError("Нельзя напрямую создавать экземпляры класса Shape")

    def __str__(self) -> str:
        return type(self).__name__

    def area(self) -> float|int:
        pass

    def perimeter(self) ->float|int:
        pass

class Circle(Shape):
    def __init__ (self, radius: float):
        if radius < 0:
            raise ValueError("Радиус не может быть отрицательным")
        self.radius=radius
    def __str__(self) -> str:
         return(f"{super().__str__()}\n"
                f"|radius = {self.radius}\n")
    def area(self) -> float:
         return self.radius**2*pi
    def perimeter(self) -> float:
         return self.radius*2*pi
    #def

shape = Circle(5)

print(shape.area(), shape.perimeter())
