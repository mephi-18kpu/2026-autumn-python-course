from base_trajectory import Trajectory, TrajectoryFactory
from vector2d import Vector2D

class LinearTrajectory(Trajectory):
    def __init__(self, start_pos: Vector2D, direction: Vector2D):
        if not isinstance(start_pos, Vector2D) or not isinstance(direction, Vector2D):
            raise TypeError("Not Vector2D")

        self._start_pos = start_pos
        self._direction = direction

    def __call__(self, t: float|int):
        return self._start_pos + t * self._direction


class LinearTrajectoryFactory(TrajectoryFactory):

    @classmethod
    def from_console(cls) -> Trajectory:
        start_pos_x = float(input("введите Х начала траектории: "))
        start_pos_y = float(input("введите У начала траектории: "))

        return LinearTrajectory(
            Vector2D.from_points((0,0), (start_pos_x, start_pos_y)),
            Vector2D(direction_x, direction_y)
        )
