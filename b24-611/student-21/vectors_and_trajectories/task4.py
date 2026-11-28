import numpy as np
import matplotlib.pyplot as plt
from vector_and_trajectory import Vector2D, ParabolicTrajectory, HyperbolicTrajectory, Trajectory



def plot_trajectory(trajectory: Trajectory, t_values: np.ndarray, ax=None, label=""):
    if ax is None:
        _, ax = plt.subplots(figsize=(8, 6))

    points = [trajectory(t) for t in t_values]
    xs = [p.x for p in points]
    ys = [p.y for p in points]
    ax.plot(xs, ys, label=label)
    ax.set_aspect('equal')
    ax.grid(True)
    ax.legend()
    return ax



t_parab = np.linspace(-2, 3, 100)
parab = ParabolicTrajectory(1, -2, 3)
plot_trajectory(parab, t_parab, label="Парабола (t от -2 до 3)")


t_hyper = np.linspace(-1.5, 1.5, 100)
hyper_right = HyperbolicTrajectory(3, 2, branch=1)
hyper_left = HyperbolicTrajectory(3, 2, branch=-1)
plot_trajectory(hyper_right, t_hyper, label="Гипербола (правая)")
plot_trajectory(hyper_left, t_hyper, label="Гипербола (левая)")

plt.title("Траектории")
plt.show()
