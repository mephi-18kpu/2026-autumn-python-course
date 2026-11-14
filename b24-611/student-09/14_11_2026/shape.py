#System imports

#User imports

#External imports

#########################

class Shape:
    def __init__ (self):
        raise TypeError('Нельзя напрямую создавать объекты данного класса')

    def __str__(self) -> str:
        return type(self).__name__

    def area(self) ->float|int:
        pass

    def perimeter(self) -> float:
        pass

    def scale(self):
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        if width<0 or height<0:
            raise ValueError ('Ширина и высота должны быть неотрицательными')

        self.width=width
        self.height=height

    def __str__(self) -> str:
        return (f'{super().__str__()}'
                f'width={self.width}'
                f'height={self.height}')
    def area(self)-> float:
        return self.width*self.height

    def perimeter(self) -> float:
        return 2*(self.height*self.width)

    def scale(self, factor):
        self.width=self.width*factor
        self.height=self.height*factor
        return

class Circle(Shape):
    def __init__(self, rad: float):
        if rad<0:
            raise ValueError ('Радиус должен быть неотрицательным')

        self.rad=rad

    def __str__(self) -> str:
        return (f'{super().__str__()}'
                f'radius={self.rad}')

    def area(self) ->float:
        return (3.1415926*self.rad**2)

    def perimeter(self) -> float:
        return (2*3.1415926*self.rad)

    def scale(self, factor):
        self.rad=self.rad*factor
        return

def calc_sum_perimeter (shapes: list[Shape])->float:
    sum=0
    for i in range(0, len(shapes)):
        sum=sum+shapes[i].perimeter()
    return sum

if __name__== '__main__':

    shapes = [Rectangle(1, 1), Rectangle(2, 2)]
    shapes[1].scale(2)
    print(f'Sum of perimeters {calc_sum_perimeter(shapes)}')
