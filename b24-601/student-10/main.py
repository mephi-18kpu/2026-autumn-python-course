import math


class Shape:
    pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def scale(self, factor: float | int) -> None:
        """Масштабирует окружность в factor раз."""
        if factor <= 0:
            raise ValueError("Коэффициент масштабирования должен быть положительным!")
        self.radius *= factor


# Запрашиваем радиус у пользователя
while True:
    try:
        r = float(input("Введите радиус окружности: "))
        if r <= 0:
            print("Радиус должен быть положительным числом!")
            continue
        break
    except ValueError:
        print("Ошибка! Введите число.")

# Создаём окружность
c = Circle(r)
print(f"\nИсходная окружность:")
print(f"Радиус: {c.radius}")
print(f"Площадь: {c.area():.2f}")
print(f"Периметр: {c.perimeter():.2f}")

# Запрашиваем коэффициент масштабирования
while True:
    try:
        factor = float(input("\nВведите коэффициент масштабирования: "))
        if factor <= 0:
            print("Коэффициент должен быть положительным!")
            continue
        break
    except ValueError:
        print("Ошибка! Введите число.")

# Масштабируем и выводим результат
c.scale(factor)
print(f"\nПосле масштабирования (x{factor}):")
print(f"Радиус: {c.radius}")
print(f"Площадь: {c.area():.2f}")
print(f"Периметр: {c.perimeter():.2f}")
