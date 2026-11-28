from  line_trajectory import LinearTrajectory, LinearTrajectoryFactory
from base_trajectory import Trajectory, TrajectoryFactory

factory_t: type[TrajectoryFactory]

factoy_index = 1

if factoy_index == 1:
    factory_t = LinearTrajectoryFactory
# if factoy_index == 2:
    # factoy_t = EllipseTrajectoryFactory
trajectory = factory_t.from_console()
print(trajectory(5))

