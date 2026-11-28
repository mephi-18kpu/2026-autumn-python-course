"""Базовые классы траектории и фабрики для консольного ввода."""

# System imports
from abc import ABC, abstractmethod
from collections.abc import Iterator
from math import isfinite

# External imports
import numpy as np

# User imports
from vector2d import Vector2D

#############################################


class Trajectory(ABC):
    """Параметрическая кривая на плоскости со шкалой обхода."""

    def __init__(self, *, t_values: np.ndarray | None = None) -> None:
        """Инициализировать шкалу обхода.

        Args:
            t_values: Одномерный массив значений параметра. По умолчанию шкала пуста.

        Raises:
            ValueError: Шкала не одномерна.
        """
        self._t_values: np.ndarray = np.empty(0, dtype=float)
        if t_values is not None:
            self.set_time_values(t_values)

    def set_time_values(self, t_values: np.ndarray) -> None:
        """Заменить шкалу обхода.

        Args:
            t_values: Одномерный массив значений параметра в порядке обхода.

        Raises:
            ValueError: Шкала не одномерна.
        """
        if t_values.ndim != 1:
            raise ValueError("Шкала обхода должна быть одномерным массивом")
        self._t_values = t_values.copy()

    @abstractmethod
    def __call__(self, t: float) -> Vector2D:
        """Вернуть положение на кривой для параметра t."""
        ...

    def __iter__(self) -> Iterator[Vector2D]:
        """Вычислять точки по заданной шкале.

        Yields:
            Следующая точка траектории.
        """
        for t in self._t_values:
            yield self(float(t))


class TrajectoryFactory(ABC):
    """Создать траекторию по параметрам из консоли."""

    def from_console(self) -> Trajectory:
        """Запросить параметры кривой и шкалу обхода.

        Returns:
            Траектория с заданными значениями параметра.
        """
        while True:
            try:
                trajectory = self._create_trajectory()
                trajectory.set_time_values(self._read_time_values())
            except ValueError as error:
                print(f"Введите параметры траектории заново. {error}")
            else:
                return trajectory

    @abstractmethod
    def _create_trajectory(self) -> Trajectory:
        """Запросить параметры конкретной кривой и создать её."""
        ...

    def _read_vector(self, label: str) -> Vector2D:
        """Прочитать координаты двумерного вектора."""
        x = float(input(f"{label}, x = "))
        y = float(input(f"{label}, y = "))
        if not (isfinite(x) and isfinite(y)):
            raise ValueError("Координаты должны быть конечными числами.")
        return Vector2D(x, y)

    def _read_time_values(self) -> np.ndarray:
        """Построить шкалу по границам и числу точек."""
        start = float(input("Начальное значение t = "))
        stop = float(input("Конечное значение t = "))
        if not (isfinite(start) and isfinite(stop)):
            raise ValueError("Границы шкалы должны быть конечными числами.")
        while True:
            try:
                count = int(input("Число точек (не менее двух) = "))
            except ValueError:
                print("Введите целое число.")
                continue
            if count >= 2:
                return np.linspace(start, stop, count)
            print("Введите число не меньше двух.")
