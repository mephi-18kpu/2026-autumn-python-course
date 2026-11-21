import math

import numpy as np



class Vector2D:
    DIMENSION = 2

    def __init__(self, x: float, y: float) -> None:
        self._x = float(x)
        self._y = float(y)

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @classmethod
    def from_points(cls, p1: tuple, p2: tuple) -> "Vector2D":
        return cls(p2[0] - p1[0], p2[1] - p1[1])

    def __repr__(self) -> str:
        return f"Vector2D({self._x}, {self._y})"

    def __str__(self) -> str:
        return repr(self)

    def __add__(self, other: "Vector2D") -> "Vector2D":
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self._x + other._x, self._y + other._y)

    def __mul__(self, scalar: float) -> "Vector2D":
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Vector2D(self._x * scalar, self._y * scalar)

    def __rmul__(self, scalar: float) -> "Vector2D":
        return self.__mul__(scalar)

    def __abs__(self) -> float:
        return math.hypot(self._x, self._y)

    def dot(self, other: "Vector2D") -> float:
        return self._x * other._x + self._y * other._y

    def __matmul__(self, other: "Vector2D") -> float:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.dot(other)

    def _normalize_index(self, index: int) -> int:
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть целым числом")
        if index not in (0, 1, -1, -2):
            raise IndexError("Индекс вне диапазона для Vector2D")
        return index

    def __getitem__(self, index: int) -> float:
        idx = self._normalize_index(index)
        return self._x if idx in (0, -2) else self._y

    def __setitem__(self, index: int, value: float) -> None:
        idx = self._normalize_index(index)
        if idx in (0, -2):
            self._x = float(value)
        else:
            self._y = float(value)

