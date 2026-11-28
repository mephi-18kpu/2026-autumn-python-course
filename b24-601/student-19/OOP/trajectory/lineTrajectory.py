from baseTrajectory import Trajectory, TrajectoryFactory
from vector2d import  Vector2D


class LinearTrajectory(Trajectory):

    def __init__(self, start_pos: Vector2D, direction: Vector2D):
        self._start_pos: Vector2D = start_pos
        self._direction: Vector2D = direction

    def __call__(self, t: float|int):
        return self._start_pos+ t * self._direction


class LinearTrajectoryFactory(TrajectoryFactory):
    @classmethod
    def from_console(cls) -> Trajectory:
        start_point_x = float(input("Pass starting x value: "))
        start_point_y = float(input("Pass starting y value: "))

        start_pos = Vector2D.from_points(
            (0,0),(start_point_x, start_point_y)
        )

        direction_x = float(input("Pass displacement vector x value: "))
        direction_y = float(input("Pass displacement vector y value: "))

        direction = Vector2D(direction_x, direction_y)

        return LinearTrajectory(start_pos, direction)
