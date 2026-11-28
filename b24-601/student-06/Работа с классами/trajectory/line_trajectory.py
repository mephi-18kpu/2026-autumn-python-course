from base_trajectrory import Trajectory, TrajectoryFactory
from vector_example import Vector2D


class Linear_trajectory(Trajectory):

    def __init__(self, start_pos: Vector2D, direction: Vector2D):
        self.start_pos: Vector2D = start_pos
        self.direction: Vector2D = direction

    def __call__(self, t: float|int):
        return self.start_pos + self.direction * t

class LinearTrajectoryFactory(TrajectoryFactory):

    def from_console(self) -> Trajectory:
        start_point_x = float(input("Введите координату x начала: "))
        start_point_y = float(input("Введите координату y начала: "))
        start_pos = Vector2D.from_points(
            (0,0), (start_point_x, start_point_y)
        )

        direction_x = float(input("Введите координату x вектора перемещения: "))
        direction_y = float(input("Введите координату y вектора перемещения: "))

        direction = Vector2D(direction_x, direction_y)

        return Linear_trajectory(start_pos, direction)
