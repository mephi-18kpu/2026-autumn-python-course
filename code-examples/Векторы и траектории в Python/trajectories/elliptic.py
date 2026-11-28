"""Эллиптическая траектория и её консольная фабрика."""

# System imports
from math import cos, isfinite, sin

# External imports
import numpy as np

# User imports
from vector2d import Vector2D
from .base import Trajectory, TrajectoryFactory

#############################################


class EllipticTrajectory(Trajectory):
    """Эллипс с заданными полуосями и центром."""

    def __init__(
        self,
        a: float,
        b: float,
        *,
        center: Vector2D | None = None,
        t_values: np.ndarray | None = None,
    ) -> None:
        """Задать полуоси и центр эллипса.

        Args:
            a: Полуось вдоль X.
            b: Полуось вдоль Y.
            center: Вектор от начала координат до центра эллипса.
                По умолчанию центр находится в точке (0, 0).
            t_values: Шкала обхода траектории.

        Raises:
            ValueError: Одна из полуосей не положительна или шкала не одномерна.
        """
        if not (a > 0 and b > 0):
            raise ValueError("Полуоси должны быть положительными")
        super().__init__(t_values=t_values)
        self._a: float = a
        self._b: float = b
        self._center: Vector2D = Vector2D(0.0, 0.0) if center is None else center

    def __call__(self, t: float) -> Vector2D:
        """Вернуть точку эллипса для параметра t в радианах."""
        displacement = Vector2D(self._a * cos(t), self._b * sin(t))
        return self._center + displacement


class EllipticTrajectoryFactory(TrajectoryFactory):
    """Создать эллипс по центру и полуосям."""

    def _create_trajectory(self) -> EllipticTrajectory:
        """Прочитать центр и полуоси эллипса."""
        center = self._read_vector("Центр эллипса")
        a = float(input("Полуось a = "))
        b = float(input("Полуось b = "))
        if not (isfinite(a) and isfinite(b)):
            raise ValueError("Полуоси должны быть конечными числами.")
        return EllipticTrajectory(a, b, center=center)
