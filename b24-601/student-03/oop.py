from numpy.ma.core import shape


class Shape:
    def __str__(self) -> str:
        return type(self).__name__



    def area(self) -> float:
        pass



    def perimetr(self) -> float:
        pass

class rectangle(Shape):
    def __init__(self,height,width):
        if width <0 or height < 0:
            raise ValueError("Неправильно надо больше")
        self.width = width
        self.height = height



    def __str__(self) -> str:
        return (f"{super().__str__()}\n"
                f"width = {self.width}\n"
                f"height = {self.height}\n")


    def area(self) -> float:
        return self.width*self.height



    def perimetr(self) -> float:
        return  self.width+self.height




class Circle(Shape):
    def __init__(self,radius):
        if radius < 0:
            raise ValueError("радиус должен быть больше 0")
        self.radius = radius

    def __str__(self) -> str:
        return (f"{super().__str__()}\n"
                f"radius = {self.radius}\n")
    def area(self) -> float:
            return self.radius*3.14*self.radius

Akruznost = Circle(5)
print(Akruznost.area())

