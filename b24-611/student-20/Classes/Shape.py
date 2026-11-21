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


#shape = Rectangle (2, 3)
#print(shape)


