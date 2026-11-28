"""Построить параметрические кривые на плоскости."""

# System imports
import operator
from abc import ABC, abstractmethod
from math import cos, hypot, pi, sin
from types import NotImplementedType

# External imports
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes

# User imports

#############################################


class Vector2D:
    """Двумерный вектор с доступом к компонентам по имени и по индексу."""

    DIMENSION = 2

    def __init__(self, x: float, y: float) -> None:
        """Сохранить компоненты вектора.

        Args:
            x: Компонента по оси X.
            y: Компонента по оси Y.
        """
        self._x: float = x
        self._y: float = y

    @classmethod
    def from_points(cls, start: tuple[float, float], end: tuple[float, float]) -> "Vector2D":
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
    def x(self) -> float:
        """Вернуть компоненту по оси X."""
        return self._x

    @property
    def y(self) -> float:
        """Вернуть компоненту по оси Y."""
        return self._y

    def __getitem__(self, index: int) -> float:
        """Вернуть компоненту по индексу."""
        index = self._normalize_index(index, Vector2D.DIMENSION)
        if index == 0:
            return self._x
        return self._y

    def __setitem__(self, index: int, value: float) -> None:
        """Изменить компоненту по индексу."""
        index = self._normalize_index(index, Vector2D.DIMENSION)
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

    def __mul__(self, scalar: float) -> "Vector2D | NotImplementedType":
        """Вернуть вектор, умноженный на число справа."""
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Vector2D(self._x * scalar, self._y * scalar)

    def __rmul__(self, scalar: float) -> "Vector2D | NotImplementedType":
        """Вернуть вектор, умноженный на число слева."""
        return self.__mul__(scalar)

    def __abs__(self) -> float:
        """Вернуть модуль вектора."""
        return hypot(self._x, self._y)

    def dot(self, other: "Vector2D") -> float:
        """Вернуть скалярное произведение двух векторов."""
        return self._x * other._x + self._y * other._y

    def __matmul__(self, other: "Vector2D") -> float | NotImplementedType:
        """Вернуть скалярное произведение для оператора @."""
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.dot(other)

    @staticmethod
    def _normalize_index(index: int, size: int) -> int:
        """Вернуть неотрицательный индекс компоненты."""
        index = operator.index(index)
        if index < 0:
            index += size
        if not 0 <= index < size:
            raise IndexError("Индекс компоненты вне диапазона")
        return index
