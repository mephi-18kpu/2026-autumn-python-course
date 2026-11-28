"""Показать операции двумерного вектора."""

# System imports

# External imports

# User imports
from trajectory import Vector2D

#############################################


def main() -> None:
    """Вывести результаты операций и показать изменение координаты."""
    v = Vector2D.from_points((1, 2), (4, 6))
    w = Vector2D(1, 2)

    print(repr(v))   # Vector2D(3, 4)
    print(v + w)     # Vector2D(4, 6)
    print(v * 2)     # Vector2D(6, 8)
    print(2 * v)     # Vector2D(6, 8)
    print(abs(v))    # 5.0
    print(v.dot(w))  # 11
    print(v @ w)     # 11

    print(v[-1])     # 4
    v[-1] = 7
    print(v.y)       # 7


if __name__ == "__main__":
    main()
