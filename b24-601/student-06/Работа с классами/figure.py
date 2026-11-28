import math
class Shape:
    def __init__(self,*, size_factors: list):
        self.__size_factors = size_factors

    def __str__(self)-> str:
        return type(self).__name__

    def area(self)->float:
        pass

    def perimeter(self)->float:
        pass

    def scale(self, factor):
        for i in  range(self.__size_factors):
            size_factor *= factor


class Rectangle(Shape):
    def __init__(self, width,height):
        if width <= 0 or height <= 0:
            raise ValueError("Длина и высота должны быть больше нуля")

        self.width = width
        self.height = height
        super().__init__(size_factors=[self.width, self.height])



    def __str__(self) -> str:
        return f"{super().__str__()}\n" + f"высота = {self.height}\n" + f"ширина = {self.width}"

    def perimeter(self) ->float:
        return (self.width+self.height)*2

    def area(self) ->float:
        return self.height*self.width

class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Радиус окружности больше 0")
        self.radius = radius

    def __str__(self) -> str:
        return f"{super().__str__()}\n" + f"Радиус окружности = {self.radius}"

    def area(self) ->float:
        return math.pi*(self.radius)**2

    def perimeter(self) ->float:
        return 2*math.pi*self.radius

