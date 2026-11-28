from line_trajectory import LinearTrajectoryFactory
from vector_and_trajectory import Trajectory

trajectory: Trajectory
trajectory_index_type = input("Введите тип траектории (1- линейная)")

if trajectory_index_type == "1":
    trajectory = LinearTrajectoryFactory.from_console()
else:
    raise ValueError("Неизвестный тип траектории")

print(trajectory(5))
