from abc import abstractclassmethod

from base_trajectory import Trajectory, TrajectoryFactory
from vector2d import Vector2D
from math import cos, sin

class LinearTrajectory(Trajectory):
    def __init__(self, start_pos: Vector2D, direction: Vector2D) -> None:
        self._start_pos: Vector2D = start_pos
        self._direction: Vector2D = direction

    def __call__(self, t: float):
        return self._start_pos + t * self._direction

class LinearTrajectoryFactory(TrajectoryFactory):
    @classmethod
    def from_console(cls) -> Trajectory:
        start_point_x = float(input("Введите координату начала x: "))
        start_point_y = float(input("Введите координату начала y: "))

        start_pos = Vector2D.from_points(
            (0, 0), (start_point_x, start_point_y)
        )

        direction_x = float(input("Введите координаты x вектора перемещения: "))
        direction_y = float(input("Введите координаты y вектора перемещения: "))

        direction = Vector2D(direction_x, direction_y)

        return LinearTrajectory(start_pos, direction)

class EllipticTrajectory(Trajectory):
    def __init__(self, a: float, b: float) -> None:
        if not (a > 0 and b > 0):
            raise ValueError("Полуоси должны быть положительными")
        self._a: float = a
        self._b: float = b

    def __call__(self, t: float) -> Vector2D:
        return Vector2D(self._a * cos(t), self._b * sin(t))
