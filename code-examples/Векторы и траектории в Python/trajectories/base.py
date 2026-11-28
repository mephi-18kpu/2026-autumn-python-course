"""Базовые классы траектории и фабрики для консольного ввода."""

# System imports
from abc import ABC, abstractmethod

# External imports

# User imports
from vector2d import Vector2D

#############################################


class Trajectory(ABC):
    """Параметрическая кривая на плоскости."""

    @abstractmethod
    def __call__(self, t: float) -> Vector2D:
        """Вернуть положение на кривой для параметра t."""
        ...


class TrajectoryFactory(ABC):
    """Создать траекторию по параметрам из консоли."""

    @abstractmethod
    def from_console(self) -> Trajectory:
        """Прочитать параметры кривой и вернуть траекторию."""
        ...
