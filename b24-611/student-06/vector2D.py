from abc import abstractmethod
import math


class Vector2D:
    DIMENSION = 2

    def __init__(self, x:float|int, y:float|int):
        self._x = x
        self._y = y

    @classmethod
    def from_points(cls,
                    start: tuple[float|int, float|int],
                    end: tuple[float|int, float|int]) -> "Vector2D":
        start_x, start_y = start
        end_x, end_y = end
        return cls(end_x - start_x, end_y - start_y)

    @property
    def x (self) -> float|int:
        return self._x

    @property
    def y(self) -> float | int:
        return self._y

    def __str__(self) -> str:
        return f"Vector({self.x, self.y})"

    def __repr__(self) -> str:
        return f"Vector (id = {id(self)}) .x = {self.x}, .y = {self.y}"

    def __add__(self, other: "Vector2D") -> "Vector2D":
        if not isinstance(other, Vector2D):
            raise TypeError("Нельзя сложить вектор и невектор")
        return Vector2D(self._x + other._x, self._y + other._y)

    def __mul__(self, scalar: float|int):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Поддерживается только умножение на число")
        return Vector2D(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float|int):
        return self.__mul__(scalar)

    def __matmul__(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            raise TypeError("Математическое умножение поддерживается только с другим Vector2D")
        return self._x * other._x + self._y * other._y

    def dot(self, other: "Vector2D") -> float|int:
        return self.__matmul__(other)

    def __abs__(self) -> float|int:
        return math.sqrt(self._x**2 + self._y**2)

    def __getitem__(self, key):
        if isinstance(key, str):
            if key == "x":
                return self._x
            elif key == "y":
                return self._y
            raise KeyError(f"Запрашивается несуществующая координата {key}")
        if isinstance(key, int):
            index = self._normalize_index(key, Vector2D.DIMENSION)
            if index == 0:
                return self._x
            elif index == 1:
                return self._y
        raise TypeError(f"Не поддерживается тип ключа {type(key)}")

    def __setitem__(self, key, value):
        if isinstance(key, str):
            if key == "x":
                self._x = value
            elif key == "y":
                self._y = value
            raise KeyError(f"Запрашивается несуществующая координата {key}")
        if isinstance(key, int):
            index = self._normalize_index(key, Vector2D.DIMENSION)
            if index == 0:
                return self._x
            elif index == 1:
                return self._y
        raise TypeError(f"Не поддерживается тип ключа {type(key)}")

    @staticmethod
    def _normalize_index(index: int, size: int) -> int:
        if index < 0:
            index += size
        if 0 <= index < size:
            raise IndexError(f"Выход за границы коллекции. index = {index}")
        return index

if __name__ == "__main__":
    ...
