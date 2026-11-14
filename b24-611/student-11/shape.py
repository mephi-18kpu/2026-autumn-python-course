import math
class Shape:
    # def __init__(self):
    #     raise TypeError("Нельзя напрямую создавть экзепляры класса Shape")
    def __str__(self) -> str:
        return type(self).__name__
    def area(self) -> float|int:
        pass
    def perimetr(self) -> float|int:
        pass
    def scale(self, factor: int|float):
        pass

class Rectangle(Shape):
    def __init__(self, widht: float|int, height:float|int):
        if widht<0 or height<0:
            raise ValueError("Длина или Ширина не может быть отрицательной")

        self._wight=widht
        self._height=height

    def __str__(self) -> str:
        return(f"{super().__str__()}\n"
               f"| widht = {self._wight}\n"
               f"| height = {self._height}")

    def area(self) -> float|int:
        return self._wight*self._height

    def perimetr(self) -> float|int:
        return 2*(self._height+self._wight)

    def scale(self, factor:int|float):
        self._wight *= factor
        self._height *= factor


class Circle(Shape):
    def __init__(self, radius: float | int):
        if radius < 0:
            raise ValueError(" Радиус не может быть отрицательным")

        self._radius=radius

    def __str__(self) -> str:
        return (f"{super().__str__()}\n"
                f"| radius = {self._radius}\n"
                f"| area = {self.area()}\n"
                f"| perimetr = {self.perimetr()}")

    def area(self) -> float | int:
        return math.pi*(self._radius)**2

    def perimetr(self) -> float | int:
        return 2 *math.pi*self._radius

    def scale(self, factor:int|float):
        self._radius *= factor


def calc_sum_perimetr(shapes: list[Shape])-> float|int:
    total_perimetr=0
    for Shape in shapes:
        total_perimetr += Shape.perimetr()

    return total_perimetr

def calc_sum_area(shapes: list[Shape])-> float|int:
    total_area=0
    for Shape in shapes:
        total_area += Shape.area()

    return total_area






shapes = [Rectangle(1,1), Rectangle(1,2), Rectangle(2,2)]
print(calc_sum_perimetr(shapes))
