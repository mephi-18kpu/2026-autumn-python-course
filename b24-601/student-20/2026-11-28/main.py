from line_trajectory import LinearTrajectory, LinearTrajectoryFactory
from base_trajectory import Trajectory, TrajectoryFactory

factory_t:type[TrajectoryFactory]

factory_index = 1

if factory_index == 1:
    factory_t = LinearTrajectoryFactory
#if factory_index ==2:
#   factory_t = ...

trajectory = LinearTrajectoryFactory.from_console()
print(trajectory(5))
