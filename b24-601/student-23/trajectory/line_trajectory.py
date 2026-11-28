from base_trajectory import Trajectory, TrajectoryFactory
from b24-601
from vector import Vector2D

class LineTrajectory(Trajectory):

    def __init__(self, start_pos: Vector2D, direction: Vector2D):
        self._strat_pos: Vector2D = start_pos
        self._direction: Vector2D = direction

    def __call__(self, t: float|int, *args, **kwargs):
        return self._strat_pos + t * self._direction

class LinearTrajectoryFactory(TrajectoryFactory):

    @classmethod
    def from_console(cls) -> Trajectory:
        start_point_x = float(input("Введите координату x для начала: "))
        start_point_y = float(input("Введите координату y для начала: "))

        start_pos = Vector2D.from_point(
            (0, 0), (start_point_x, start_point_y)
        )

        direction_x = float(input("Введите координату x вектора перемещения: "))
        direction_y = float(input("Введите координату y вектора перемещения: "))

        direction = Vector2D(direction_x, direction_y)

        return LineTrajectory(start_pos, direction)
