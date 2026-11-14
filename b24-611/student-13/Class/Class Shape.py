import numpy as np

class Shape:
    def __init__(self):
        raise TypeError("нельзя напрямую создавать экземпляры")

    def __str__(self) -> str:
        return type(self).__name__

    def area(self) -> float|int:
        pass

    def perimetr(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, widht: float|int, height: float|int):
        if widht < 0 or height < 0:
            raise ValueError("отрицательная длина")
        self._widht = widht
        self._height = height

    def __str__(self) -> str:
        return (f"{super().__str__()}\n"
                f"| wight = {self.widht}\n"
                f"| height = {self.height}\n")

    def area(self) -> float|int:
        return (self._widht * self._height)

    def perimetr(self) -> float:
        return 2 * (self._widht + self._height)


class Circle(Shape):
    def __init__(self, radius: float|int):
        if radius < 0:
            raise ValueError("отрицательная длина")
        self._radius = radius


    def __str__(self) -> str:
        return (f"{super().__str__()}\n"
                f"| radius = {self.radius}\n")

    def area(self) -> float|int:
        return np.pi * self._radius ** 2

    def perimetr(self) -> float:
        return 2 * np.pi * self._radius


def summ_perimetr(l: list) -> float|int:
    total = 0
    for i in l:
        total += i.perimetr()
    return total

def summ_area(l: list) -> float|int:
    total = 0
    for i in l:
        total += i.area()
    return total


rectangle = Rectangle(3, 5)
circle = Circle(5)

l = []
l.append(rectangle)
l.append(circle)

print(summ_area(l))
print(summ_perimetr(l))
