from line_trajectory import LinearTrajectoryFactory, EllipticTrajectory
from base_trajectory import Trajectory, TrajectoryFactory

factory_t: type[TrajectoryFactory]

factory_index = 1 #...

if factory_index == 1:
    factory_t = LinearTrajectoryFactory
else:
    factory_t = LinearTrajectoryFactory

trajectory = factory_t.from_console()
print(trajectory(5))
