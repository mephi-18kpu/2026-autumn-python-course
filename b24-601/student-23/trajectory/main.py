from line_trajectory import LineTrajectory, LinearTrajectoryFactory

trajectory = LinearTrajectoryFactory.from_console()
print(trajectory(5))
