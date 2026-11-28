from line_trajectory import LinearTrajectoryFactory

trajectory: Trajectory
trajectory_index_type = input("ведите тип траектории (1-линейная)")

if trajectory_index_type =="":
    trajectory = LinearTrajectoryFactory.from_console()
else:
    raise ValueError()

print(trajectory(5))
