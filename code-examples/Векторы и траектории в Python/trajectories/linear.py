"""Прямолинейная траектория и её консольная фабрика."""

# System imports

# External imports
import numpy as np

# User imports
from vector2d import Vector2D
from .base import Trajectory, TrajectoryFactory

#############################################


class LinearTrajectory(Trajectory):
    """Прямая, заданная точкой и направлением."""

    def __init__(
        self,
        start: Vector2D,
        direction: Vector2D,
        *,
        t_values: np.ndarray | None = None,
    ) -> None:
        """Задать параметры прямой.

        Args:
            start: Положение при t = 0.
            direction: Изменение положения при увеличении t на единицу.
            t_values: Шкала обхода траектории.

        Raises:
            ValueError: Шкала не одномерна.
        """
        super().__init__(t_values=t_values)
        self._start: Vector2D = start
        self._direction: Vector2D = direction

    def __call__(self, t: float) -> Vector2D:
        """Вернуть положение на прямой для параметра t."""
        return self._start + t * self._direction


class LinearTrajectoryFactory(TrajectoryFactory):
    """Создать прямую по начальной точке и направлению."""

    def _create_trajectory(self) -> LinearTrajectory:
        """Прочитать начальную точку и направление."""
        start = self._read_vector("Начальная точка")
        direction = self._read_vector("Направление")
        return LinearTrajectory(start, direction)
