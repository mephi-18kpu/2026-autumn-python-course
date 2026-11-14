class Shape:
    def __init__(self):
        raise TypeError ("Нельзя напрямую создавать экземпляры класса Shape")

    def __str__(self) -> str:
        return type(self).__name__

    def area(self) ->float:
        pass

    def perimetr(self) ->float:
        pass

    def scale(self, factor):
        pass


class Ocruznost(Shape):
    def __init__(self, radius: float):
        if radius<0:
            raise ValueError("Radius<0")

        self._radius = radius

    def __str__(self) -> str:
        return(f"{super().__str__()}\n"
               f"| radius = {self._radius}")

    def scale(self, factor):
        if factor<0:
            raise ValueError("Radius doljen bit bolshe 0")
        self._radius*=factor

    def area(self) ->float:
        return self._radius * self._radius * 3.14 *0.5

    def perimetr(self) ->float:
        return 2*(self._radius * 3.14)


def calc_sum_perimeter(shapes: list[Shape]) ->float:
    return sum(shape.perimetr() for shape in shapes)

def calc_sum_areas(shapes: list[Shape]) ->float:
    return sum(shape.area() for shape in shapes)



shapes_list = [Ocruznost(3), Ocruznost(18)]
factor = 2
test=Ocruznost(2)
test.scale(factor)
print(test)

print(calc_sum_perimeter(shapes_list))
print(calc_sum_areas(shapes_list))
