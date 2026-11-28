from base_trajectory import Trajectory, TrajectoryFactory
from vector2d import Vector2D

class LinearTrajectory(Trajectory):

    def __init__(self, start_pos: Vector2D, direction: Vector2D):
        self._start_pos: Vector2D = start_pos
        self._direction: Vector2D = direction

    def __call__(self, t: float|int, *args, **kwargs):
        return self._start_pos + t * self._direction


class LinearTrajectoryFactory(TrajectoryFactory):
    @classmethod
    def from_console(cls) -> Trajectory:
        start_point_x = float(input('Введите координату X начала: '))
        start_point_y = float(input('Введите координату Y начала: '))

        start_pos = Vector2D.from_points((0,0), (start_point_x, start_point_y))

        direction_x = float(input("Введите координату X перемещения: "))
        direction_y = float(input("Введите координату Y перемещения: "))

        direction = Vector2D(direction_x, direction_y)

        return LinearTrajectory(start_pos, direction)
