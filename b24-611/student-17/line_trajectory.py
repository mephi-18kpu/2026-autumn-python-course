from base_trajectory import Trajectory, TrajectoryFactory
from vector2d import Vector2D

class LinearTrajectory(Trajectory):
    def __init__(self, start_pos: Vector2D, direction, Vector2D):
        if not isinstance(start_pos, Vector2D) or not isinstance(direction, Vector2D):
            raise TypeError("Not Vector2D")

        self._start_pos = start_pos
        self._direction = direction

        def __call__(self, t: float) -> Vector2D:
            return self._start_pos + self._direction * t

class LinearTrajectoryFactory(TrajectoryFactory):
    @classmethod
    def from_console(cls):
        x = float(input("Начальная координата х: "))
        y = float(input("Начальная координата y: "))

        dx = float(input("Компонента направления по x: "))
        dy = float(input("Компонента направления по y: "))

        start_pos = Vector2D(x, y)
        direction = Vector2D(dx, dy)

        return LinearTrajectory(start_pos, direction)
