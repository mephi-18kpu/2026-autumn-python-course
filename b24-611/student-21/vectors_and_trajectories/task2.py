from vector_and_trajectory import ParabolicTrajectory

try:
    ParabolicTrajectory(0, 1, 2)
except ValueError as e:
    print(f"Поймали ошибку: {e}")


traj = ParabolicTrajectory(1, -2, 3)
print("Точка при t=2:", traj(2))
