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

class Rectangle(Shape):
    def __init__ (self, width: float, height: float):
        if width<0 or height<0:
            raise  ValueError("Нельзя писать отрицательные")
        self.width=width
        self.height=height
    def __str__(self) -> str:
        return(f"{super().__str__()}\n"
               f"|width = {self.width}\n"
               f"|height = {self.height}\n")
    def area(self) -> float:
        return self.width+self.height
    def perimeter(self) -> float:
        return 2*(self.width+ self.height)

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

n=input("Введите колиечство фигур")
def calc_sum_perimeter(shapes: list[Shape]) -> float:
        l=
        for i in range(n):
            t=input(f"Введите тип {n} фигуры")
            d=input("Введите параметры фигуры (длина или радиус)")
            d1=input("Введите параметры фигуры (ширина или 0, если circle)")
            if t== "circle":
                sh = Circle(float(d))
            if t== "rectangle":
                sh= Rectangle(float(d), float(d1))
            l.append(sh.perimeter())
        return (l)

print(f"Периметры фигур по порядку: {calc_sum_perimeter()}")
