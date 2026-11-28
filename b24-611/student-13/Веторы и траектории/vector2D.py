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

class Trajectory(ABC):

    @abstractmethod
    def __call__(self, t: float) -> Vector2D:
        ...


class LinearTrajectory(Trajectory):

    def __init__(self, start: Vector2D, direction: Vector2D) -> None:
        self._start: Vector2D = start
        self._direction: Vector2D = direction

    def __call__(self, t: float) -> Vector2D:
        return self._start + t * self._direction


class TrajectoryFactory(ABC):
    @classmethod
    def from_console(cls) -> Trajectory:
        pass

class LinearTrajectoryFactory(TrajectoryFactory):
    @classmethod
    def from_console(cls) -> Trajectory:
        start_pos_x = float(input("ведите координату Х начала траектории:"))
        start_pos_y = float(input("ведите координату У начала траектории:"))

        direction_x = float(input("ведите координату Х вектора перемещения:"))
        direction_y = float(input("ведите координату У вектора перемещения:"))

        return LinearTrajectory(
            Vector2D.from_points((0,0), (start_pos_x, start_pos_y)),
            Vector2D(direction_x, direction_y),
        )


def main() -> None:
    """Вычислить положение при равномерном движении и построить две кривые."""
    start = (1.0, 2.0)
    end = (4.0, 6.0)
    elapsed_time = 2.0

    displacement = Vector2D.from_points(start, end)
    velocity = displacement * (1.0 / elapsed_time)
    line = LinearTrajectory(Vector2D(*start), velocity)
    position = line(3.0)

    print(abs(displacement))       # 5.0
    print(position.x, position.y)  # 5.5 8.0
