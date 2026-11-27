"""Запросить параметры траекторий и построить их графики."""

# System imports

# External imports
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

# User imports
from trajectories import (
    EllipticTrajectoryFactory,
    LinearTrajectoryFactory,
    Trajectory,
    TrajectoryFactory,
)

#############################################


def plot_trajectory(ax: Axes, trajectory: Trajectory, label: str) -> None:
    """Построить траекторию по её шкале обхода.

    Args:
        ax: Область построения.
        trajectory: Траектория с заданной шкалой обхода.
        label: Подпись кривой в легенде.
    """
    points = list(trajectory)
    x_values = [point.x for point in points]
    y_values = [point.y for point in points]
    ax.plot(x_values, y_values, label=label)


def main() -> None:
    """Создать прямую и эллипс из консольного ввода и построить их."""
    factories: list[tuple[TrajectoryFactory, str]] = [
        (LinearTrajectoryFactory(), "Прямая"),
        (EllipticTrajectoryFactory(), "Эллипс"),
    ]
    trajectories: list[tuple[Trajectory, str]] = []
    for factory, label in factories:
        print(f"\nПараметры траектории «{label}»")
        trajectories.append((factory.from_console(), label))

    _, ax = plt.subplots()
    for trajectory, label in trajectories:
        plot_trajectory(ax, trajectory, label)

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True)
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
