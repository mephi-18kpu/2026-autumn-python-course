import math


class Shape:
    def area(self) -> float:
        raise NotImplementedError("Подкласс должен реализовать метод area()")

    def __str__(self) -> str:
        return self.__class__.__name__


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота должны быть положительными")
        self.width = float(width)
        self.height = float(height)

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def scale(self, factor: float) -> None:
        if factor <= 0:
            raise ValueError("Коэффициент масштабирования должен быть положительным")
        self.width *= factor
        self.height *= factor

    def __str__(self) -> str:
        return f"{super().__str__()}({self.width} x {self.height})"


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным")
        self.radius = float(radius)

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def scale(self, factor: float) -> None:
        if factor <= 0:
            raise ValueError("Коэффициент масштабирования должен быть положительным")
        self.radius *= factor

    def __str__(self) -> str:
        return f"{super().__str__()}(r={self.radius})"


class Triangle(Shape):
    def __init__(self, base: float, height: float) -> None:
        if base <= 0 or height <= 0:
            raise ValueError("Основание и высота должны быть положительными")
        self.base = float(base)
        self.height = float(height)

    def area(self) -> float:
        return 0.5 * self.base * self.height

    def __str__(self) -> str:
        return f"{super().__str__()}(base={self.base}, height={self.height})"


def print_all_areas(shapes: list[Shape]) -> None:
    for shape in shapes:
        print(f"{shape}: area = {shape.area():.2f}")


if __name__ == "__main__":
    # 1. Демонстрация операции area() для разных фигур
    sample_rect = Rectangle(3, 4)
    sample_circle = Circle(5)
    print(f"1. Площадь прямоугольника: {sample_rect.area()}, круга: {sample_circle.area():.2f}")

    # 2. Класс и экземпляры Rectangle
    r1 = Rectangle(2, 6)
    r2 = Rectangle(4, 5)
    # При r1.perimeter() в self передаётся r1; при r2.perimeter() в self передаётся r2
    print(f"2. r1 -> area: {r1.area()}, perimeter: {r1.perimeter()}")
    print(f"   r2 -> area: {r2.area()}, perimeter: {r2.perimeter()}")

    # 3. Масштабирование прямоугольника
    r3 = Rectangle(3, 4)
    r3.scale(2)
    assert r3.area() == 48.0 and r3.perimeter() == 28.0
    print(f"3. После scale(2) -> area: {r3.area()}, perimeter: {r3.perimeter()}")

    try:
        r3.scale(0)
    except ValueError as err:
        print(f"   Ожидаемая ошибка при scale(0): {err}")

    assert r3.area() == 48.0 and r3.perimeter() == 28.0
    print(f"   После scale(0) -> area: {r3.area()}, perimeter: {r3.perimeter()}")

    # 4. Подкласс Triangle и строковое представление
    triangle = Triangle(6, 4)
    assert triangle.area() == 12.0
    print(f"4. {triangle} -> area: {triangle.area()}")

    # 5. Вывод площадей разных фигур
    shapes: list[Shape] = [Rectangle(3, 4), Circle(5)]
    print("5. Список из 2 фигур:")
    print_all_areas(shapes)

    shapes.append(triangle)
    print("   Список после добавления треугольника:")
    print_all_areas(shapes)
