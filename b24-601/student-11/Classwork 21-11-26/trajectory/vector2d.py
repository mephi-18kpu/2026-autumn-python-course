import math

class Vector2D:

    DIMENSION = 2

    def __init__(self, x: int|float, y: int|float):
        self._x = x
        self._y = y

    @classmethod
    def from_points(cls, start: tuple[float|int, float|int],
                    end: tuple[float|int, float|int]) -> "Vector2D":
        start_x, start_y = start
        end_x, end_y = end
        return cls(end_x - start_x, end_y - start_y)

    @staticmethod
    def _normalize_index(index: int, size: int) -> int:
        if index < 0:
            index += size
        if not 0 <= index < size:
            raise IndexError("Индекс компоненты вне диапазона")
        return index

    @property
    def x(self) -> float|int:
        return self._x

    @property
    def y(self) -> float|int:
        return self._y

    def __getitem__(self, key):
        if isinstance(key, str):
            if key == "x":
                return self._x
            elif key == "y":
                return self._y
            raise KeyError("Есть только x и y")

        if isinstance(key, int):
            index = self._normalize_index(key, Vector2D.DIMENSION)
            if index == 0:
                return self._x
            return self._y

        raise TypeError("Не тот тип данных")

    def __setitem__(self, index: int, value: float|int) -> None:
        index = self._normalize_index(index, Vector2D.DIMENSION)
        if index == 0:
            self._x = value
        else:
            self._y = value

    def __repr__(self) -> str:
        return (f"Vector2D(id = {id(self)}, with x = {self._x!r}, "
                f"y = {self._y!r})")

    def __add__(self, other: "Vector2D") -> "Vector2D":
        if not isinstance(other, Vector2D):
            raise TypeError("Сложение возможно только с другим вектором")
        return Vector2D(self._x + other.x, self._y + other.y)

    def __mul__(self, scalar: float|int) -> "Vector2D":
        if not isinstance(scalar, (int, float)):
            raise TypeError("Умножение возможно только сна скаляр")
        return Vector2D(self._x * scalar, self._y * scalar)

    def __rmul__(self, scalar: float|int) -> "Vector2D":
        return self.__mul__(scalar)

    def __abs__(self) -> float|int:
        return math.sqrt(self._x**2 + self._y**2)

    def __matmul__(self, other: "Vector2D") -> float|int:
        if not isinstance(other, Vector2D):
            raise TypeError("Не то умножаешь")
        return self._x * other.x + self._y * other.y

    def dot(self, other: "Vector2D") -> float|int:
        return self.__matmul__(other)

if __name__ == "__main__":
    ras = Vector2D(10, 12)
    dva = Vector2D.from_points((10, 15), (3, 19))

    ras_or_dva = ras + dva
    print(ras_or_dva, ras["x"], ras[-1])

    ras[0] = 42
    ras[1] = 67
    print(ras * 4, ras["y"])

    print(Vector2D.dot(ras, dva))
