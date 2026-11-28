from base_trajectory import Trajectory
from line_trajectory import LinearTrajectoryFactory

trajectory: Trajectory
trajectory_index_type = input("Введите тип траектории (1 - линейная)")

if trajectory_index_type == "1":
    trajectory = LinearTrajectoryFactory.from_console()
else:
    raise ValueError()
