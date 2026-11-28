from base_trajectory import Trajectory, TranjectoryFactory
from trajectories import Vector2D


class LinearTrajectory(Trajectory):

    def __init__(self, start_pos: Vector2D, direction: Vector2D):
        self._start_pos: Vector2D = start_pos
        self._direction: Vector2D = direction

    def __call__(self, t: float):
        return self._start_pos + self._direction * t


class LineTrajectoryFactory(TranjectoryFactory):

    @classmethod
    def from_console(self) -> Trajectory:
        start_point_x = float(input('Введите начльную координату Х'))
        start_point_y = float(input('Введите начльную координату Y'))

        start_pos = Vector2D.from_points(
            (0, 0) , (start_point_x, start_point_y)
        )

        direction_x = float(input('Введите координату вектора X'))
        direction_y = float(input('Введите координату вектора Y'))

        direction = Vector2D(direction_x, direction_y)

        return LinearTrajectory(start_pos, direction)
