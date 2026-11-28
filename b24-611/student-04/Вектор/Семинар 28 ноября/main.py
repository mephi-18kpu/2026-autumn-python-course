from line_trajectory import LinearTrajectoryFactory
from line_trajectory import Trajectory

trajectory: Trajectory
trajectory_index_type = input("Put type of trajectory")

if trajectory_index_type == "1":
    trajectory = LinearTrajectoryFactory.from_console()

else:
    raise ValueError()

trajectory = LinearTrajectoryFactory.from_console()
print(trajectory(5))
