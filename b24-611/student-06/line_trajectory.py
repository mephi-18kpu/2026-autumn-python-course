from base_trajectory import Trajectory, TrajectoryFactory
from vector2D import Vector2D

class LinearTrajectory(Trajectory):
    def __init__ (self, start_pos: Vector2D, direction: Vector2D):
        if not isinstance(start_pos, Vector2D) or not isinstance(direction, Vector2D):
            raise TypeError("Not Vector2d")

        self._start_pos = start_pos
        self._direction = direction

    def __call__(self, t: float|int):
        return self._start_pos + t * self._direction


class LinearTrajectoryFactory(TrajectoryFactory):

    @classmethod
    def from_console(cls) -> Trajectory:
        start_pos_x = float(input("Введите координату x начала траектории"))
        start_pos_y = float(input("Введите координату y начала траектории"))

        direction_x = float(input("Введите координату x вектора перемещения"))
        direction_y = float(input("Введите координату y вектора перемещения"))

        return LinearTrajectory(
            Vector2D.from_points((0,0),(start_pos_x, start_pos_y)),
            Vector2D(direction_x, direction_y)
        )
