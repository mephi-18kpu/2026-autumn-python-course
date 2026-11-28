"""Прямолинейная траектория и её консольная фабрика."""

# System imports
from math import isfinite

# External imports

# User imports
from vector2d import Vector2D
from .base import Trajectory, TrajectoryFactory

#############################################


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


class LinearTrajectoryFactory(TrajectoryFactory):
    """Создать прямую по начальной точке и направлению."""

    def from_console(self) -> LinearTrajectory:
        """Прочитать начальную точку и направление.

        Returns:
            Прямолинейная траектория.
        """
        while True:
            try:
                start = Vector2D(
                    float(input("Начальная точка, x = ")),
                    float(input("Начальная точка, y = ")),
                )
                if not (isfinite(start.x) and isfinite(start.y)):
                    raise ValueError("Координаты начальной точки должны быть конечными числами.")

                direction = Vector2D(
                    float(input("Направление, x = ")),
                    float(input("Направление, y = ")),
                )
                if not (isfinite(direction.x) and isfinite(direction.y)):
                    raise ValueError("Компоненты направления должны быть конечными числами.")
            except ValueError as error:
                print(f"Введите параметры траектории заново. {error}")
            else:
                return LinearTrajectory(start, direction)
