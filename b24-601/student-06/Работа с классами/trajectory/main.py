from line_trajectory import Linear_trajectory, LinearTrajectoryFactory
from base_trajectrory import Trajectory, TrajectoryFactory

factory_t: type(TrajectoryFactory)

factory_index = 1

if factory_index == 1:
    factory_t = LinearTrajectoryFactory

trajectory = factory_t.from_console()
print(trajectory(0))
