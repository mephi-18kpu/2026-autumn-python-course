from vector_and_trajectory import Vector2D
from vector_and_trajectory import Trajectory
from vector_and_trajectory import TrajectoryFactory

class LinearTrajectory(Trajectory):
    def __init__(self, start_pos: Vector2D, direction: Vector2D):
        if not isinstance(start_pos, Vector2D) or not isinstance(direction, Vector2D):
            raise TypeError("not Vector2D")

        self._start_pos = start_pos
        self._direction = direction

    def __call__(self, t:float|int):
        return self._start_pos + t * self._direction


class LinearTrajectoryFactory(TrajectoryFactory):

    @classmethod
    def from_console(cls) -> Trajectory:
        start_pos_x = float(input("Введите координату Х начала траектории"))
        start_pos_y = float(input("Введите координату Y начала траектории"))

        direction_x = float(input("Введите координату Х вектора перемещения"))
        direction_y = float(input("Введите координату Y вектора перемещения"))

        return LinearTrajectory(
            Vector2D(start_pos_x, start_pos_y),
            Vector2D(direction_x,  direction_y)
        )
