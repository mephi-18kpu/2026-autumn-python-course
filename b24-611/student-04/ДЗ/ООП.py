from math import pi


class Shape:
    def area(self) -> float:
        raise NotImplementedError("Подкласс должен определить метод area()")

    def __str__(self) -> str:
        return type(self).__name__


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        if not (width > 0 and height > 0):
            raise ValueError("Ширина и высота должны быть положительными")
        self._width = width
        self._height = height

    def area(self) -> float:
        return self._width * self._height

    def perimeter(self) -> float:
        return 2 * (self._width + self._height)

    def scale(self, factor: float) -> None:
        if not factor > 0:
            raise ValueError("Коэффициент должен быть положительным")
        self._width *= factor
        self._height *= factor

    def __str__(self) -> str:
        return f"{super().__str__()} ({self._width} × {self._height})"


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        if not radius > 0:
            raise ValueError("Радиус должен быть положительным")
        self._radius = radius

    def area(self) -> float:
        return pi * self._radius ** 2

    def __str__(self) -> str:
        return f"{super().__str__()} (радиус {self._radius})"


class Triangle(Shape):
    def __init__(self, base: float, height: float) -> None:
        if not (base > 0 and height > 0):
            raise ValueError("Основание и высота должны быть положительными")
        self._base = base
        self._height = height

    def area(self) -> float:
        return self._base * self._height / 2

    def __str__(self) -> str:
        return f"{super().__str__()} (основание {self._base}, высота {self._height})"


def print_all_areas(shapes: list[Shape]) -> None:
    for shape in shapes:
        print(f"{shape} — площадь {shape.area()}")


if __name__ == "__main__":
    # 1. Для прямоугольника нужны ширина и высота, для круга — радиус.
    # area() использует эти размеры для вычисления площади по формуле фигуры.
    # str() использует имя класса и те же размеры для текстового описания.
    rectangle = Rectangle(3, 4)
    circle = Circle(1)
    print("1. Площади прямоугольника и круга")
    print(rectangle.area(), circle.area())

    print("\n2. Площади и периметры")
    first = Rectangle(2, 6)
    second = Rectangle(4, 5)
    print(first, first.area(), first.perimeter())     # self — объект first
    print(second, second.area(), second.perimeter())  # self — объект second

    print("\n3. Масштабирование")
    scaled = Rectangle(3, 4)
    scaled.scale(2)
    print("После scale(2):", scaled.area(), scaled.perimeter())
    try:
        scaled.scale(0)
    except ValueError as error:
        print(error)
    print("После scale(0):", scaled.area(), scaled.perimeter())

    print("\n4. Треугольник")
    triangle = Triangle(6, 4)
    print(triangle)
    print(triangle.area())

    print("\n5. Площади двух фигур")
    shapes = [rectangle, circle]
    print_all_areas(shapes)
    print("\nПосле добавления треугольника")
    shapes.append(triangle)
    print_all_areas(shapes)
