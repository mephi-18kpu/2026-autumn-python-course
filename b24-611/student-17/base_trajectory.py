from abc import ABC, abstractmethod, abstractclassmethod

class Trajectory(ABC):

    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass

class TrajectoryFactory(ABC):

    @abstractclassmethod
    def from_console(cls) -> Trajectory:
        start_pos_x = float(input("Введите координату х начала траектории: "))
        start_pos_y = float(input("Введите координату y начала траектории: "))

        direction_x = float(input("Введите координату x вектора перемещения: "))
        direction_y = float(input("Введите координату y вектора перемещения: "))

        return LinearTrajectory(
          Vector2D.from_points((0, 0), (start_pos_x, start_pos_y))
        )

