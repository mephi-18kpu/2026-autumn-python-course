from base_trajectory import Trajectory, TrajectoryFactory
from vector import Vector2D


class LinearTrajectory(Trajectory):

    def __init__(self, start_pos: Vector2D, direction: Vector2D):
        self._start_pos: Vector2D = start_pos
        self._direction: Vector2D = direction

    def __call__(self, t: float|int):
        return self._start_pos + t * self._direction


class LinearTrajectoryFactory(TrajectoryFactory):

    @classmethod
    def from_console(cls) -> Trajectory:
        start_points_x = float(input("Введите координату x начала: "))
        start_points_y = float(input("Введите координату y начала: "))

        start_pos = Vector2D.from_points(
            (0,0), (start_points_x, start_points_y)
        )

        direction_x = float(input("Введите координату x перемещения: "))
        direction_y = float(input("Введите координату y перемещения: "))

        direction = Vector2D(direction_x, direction_y)

        return LinearTrajectory(start_pos, direction)
