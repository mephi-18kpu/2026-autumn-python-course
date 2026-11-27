"""Двумерный вектор и примеры операций с ним."""

# System imports
import operator
from math import hypot
from types import NotImplementedType

# External imports

# User imports

#############################################


class Vector2D:
    """Двумерный вектор с доступом к компонентам по имени и по индексу."""

    DIMENSION = 2

    def __init__(self, x: float | int, y: float | int) -> None:
        """Сохранить компоненты вектора.

        Args:
            x: Компонента по оси X.
            y: Компонента по оси Y.
        """
        self._x: float | int = x
        self._y: float | int = y

    @classmethod
    def from_points(
        cls,
        start: tuple[float | int, float | int],
        end: tuple[float | int, float | int],
    ) -> "Vector2D":
        """Создать вектор перемещения между двумя точками.

        Args:
            start: Координаты начальной точки.
            end: Координаты конечной точки.

        Returns:
            Вектор перемещения от начальной точки к конечной.
        """
        start_x, start_y = start
        end_x, end_y = end
        return cls(end_x - start_x, end_y - start_y)

    @property
    def x(self) -> float | int:
        """Вернуть компоненту по оси X."""
        return self._x

    @property
    def y(self) -> float | int:
        """Вернуть компоненту по оси Y."""
        return self._y

    def __getitem__(self, key: int | str) -> float | int:
        """Вернуть компоненту по индексу или имени."""
        index = self._normalize_index(key, Vector2D.DIMENSION)
        if index == 0:
            return self._x
        return self._y

    def __setitem__(self, key: int | str, value: float | int) -> None:
        """Изменить компоненту по индексу или имени."""
        index = self._normalize_index(key, Vector2D.DIMENSION)
        if index == 0:
            self._x = value
        else:
            self._y = value

    def __repr__(self) -> str:
        """Вернуть представление с именем класса и компонентами."""
        return f"Vector2D({self._x!r}, {self._y!r})"

    def __add__(self, other: "Vector2D") -> "Vector2D | NotImplementedType":
        """Вернуть сумму двух векторов."""
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self._x + other._x, self._y + other._y)

    def __mul__(self, scalar: float | int) -> "Vector2D | NotImplementedType":
        """Вернуть вектор, умноженный на число справа."""
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Vector2D(self._x * scalar, self._y * scalar)

    def __rmul__(self, scalar: float | int) -> "Vector2D | NotImplementedType":
        """Вернуть вектор, умноженный на число слева."""
        return self.__mul__(scalar)

    def __abs__(self) -> float:
        """Вернуть модуль вектора."""
        return hypot(self._x, self._y)

    def dot(self, other: "Vector2D") -> float | int:
        """Вернуть скалярное произведение двух векторов."""
        return self._x * other._x + self._y * other._y

    def __matmul__(self, other: "Vector2D") -> float | int | NotImplementedType:
        """Вернуть скалярное произведение для оператора @."""
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.dot(other)

    @staticmethod
    def _normalize_index(key: int | str, size: int) -> int:
        """Преобразовать индекс или имя компоненты в неотрицательный индекс."""
        if isinstance(key, str):
            if key == "x":
                index = 0
            elif key == "y":
                index = 1
            else:
                raise KeyError(f"У вектора есть только компоненты x и y. Получен ключ {key!r}")
        else:
            index = operator.index(key)
        if index < 0:
            index += size
        if not 0 <= index < size:
            raise IndexError("Индекс компоненты вне диапазона")
        return index


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

    v["x"] = 2
    print(v["x"])    # 2


if __name__ == "__main__":
    main()
