"""Построить параметрические кривые на плоскости."""

# System imports
import operator
from abc import ABC, abstractmethod, abstractclassmethod
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
    """Параметрическая кривая на плоскости."""

    @abstractmethod
    def __call__(self, t: float) -> Vector2D:
        pass
        """Вернуть положение на кривой для параметра t."""
        ...


class LinearTrajectory(Trajectory):
    """Прямая, заданная точкой и направлением."""

    def __init__(self, start: Vector2D, direction: Vector2D) -> None:
        """Задать параметры прямой.

        Args:
            start: Положение при t = 0.
            direction: Изменение положения при увеличении t на единицу.
        """
        self._start: Vector2D = start
        self._direction: Vector2D = direction

    def __call__(self, t: float) -> Vector2D:
        """Вернуть положение на прямой для параметра t."""
        return self._start + t * self._direction


class EllipticTrajectory(Trajectory):
    """Эллипс с центром в начале координат."""

    def __init__(self, a: float, b: float) -> None:
        """Задать полуоси эллипса.

        Args:
            a: Полуось вдоль X.
            b: Полуось вдоль Y.

        Raises:
            ValueError: Одна из полуосей не положительна.
        """
        if not (a > 0 and b > 0):
            raise ValueError("Полуоси должны быть положительными")
        self._a: float = a
        self._b: float = b

    def __call__(self, t: float) -> Vector2D:
        """Вернуть точку эллипса для параметра t в радианах."""
        return Vector2D(self._a * cos(t), self._b * sin(t))


def plot_trajectory(ax: Axes, trajectory: Trajectory, t_values: np.ndarray, label: str) -> None:
    """Построить траекторию по заданным значениям параметра.

    Args:
        ax: Область построения.
        trajectory: Траектория, возвращающая точки на плоскости.
        t_values: Одномерный массив значений параметра.
        label: Подпись кривой в легенде.
    """
    points = [trajectory(float(t)) for t in t_values]
    x_values = [point.x for point in points]
    y_values = [point.y for point in points]
    ax.plot(x_values, y_values, label=label)


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

    ellipse = EllipticTrajectory(a=3.0, b=2.0)
    _, ax = plt.subplots()

    plot_trajectory(ax, line, np.linspace(0.0, 3.0, 100), "Прямая")
    plot_trajectory(ax, ellipse, np.linspace(0.0, 2.0 * pi, 200), "Эллипс")

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True)
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
