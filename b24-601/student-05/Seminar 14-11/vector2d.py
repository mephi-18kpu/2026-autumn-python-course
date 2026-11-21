import math

import numpy as np
class Vector2D:
    """Класс для описания двумерного вектора"""
    DIMENSION = 2

    def __init__(self, x: float|int, y: float|int):
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
    def x(self) -> float|int:
        return self._x

    @property
    def y(self) -> float | int:
        return self._y

    def __getitem__(self, key) -> float|int:
        if isinstance(key, str):
            if key == "x":
                return self._x
            if key == "y":
                return self._y
            raise KeyError("У типа Vector2D есть только поля x и y\n"
                           f"Попытка получить значение поля {key}")
        if isinstance(key, int):
            index = self._normalize_index(key, Vector2D.DIMENSION)
            if index == 0:
                return self._x
            if index == 1:
                return self._y
        raise TypeError(f"Непоодерживаемый тип type(key = {type(key)}!")

    def __setitem__(self, key, value):
        index = self._normalize_index(key, Vector2D.DIMENSION)
        if index == 0:
            return self._x
        if index == 1:
            return self._y

    @staticmethod
    def _normalize_index(index: int, size: int):
        if index < 0:
            index += 2
        if index < 0 or index >= size:
            raise IndexError("Индекс компоненты вне диапазона!")
        return index

    def __repr__(self) -> str:
        return f"Vector2D (id == {id(self)}) with ._x = {self.x}, ._y = {self.y}"

    def __add__(self, other: "Vector2D") -> Vector2D:
        if not isinstance(other, Vector2D):
            raise TypeError("Сложение Vector2D возможно только с другим Vector2D! "
                            f"Получен {type(other)}")
        return Vector2D(self.x + other.x, self.y+other.y)

    def __mul__(self, scalar: float|int) -> "Vector2D":
        if not isinstance(scalar, (int, float)):
            raise TypeError("Умножение Vector2D возможно только на int или float!")
        return Vector2D(self._x * scalar, self._y * scalar)

    def __rmul__(self, scalar: float|int) -> "Vector2D":
        return self.__mul__(scalar)

    def __abs__(self) -> float|int:
        return np.sqrt(self._x**2, self._y**2)

    def __matmul__(self, other: "Vector2D") -> float|int:
        if not isinstance(other, Vector2D):
            raise TypeError(f"Математическое умножение Vector2D невозможно!")
        return self.x * other.x + self.y * other.y
    
    def dot(self, other: "Vector2D") -> float|int:
        return self.__matmul__(other)
