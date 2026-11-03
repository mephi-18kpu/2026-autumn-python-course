from math import e

import matplotlib.pyplot as plt
import numpy as np

from integration_methods import (
    Integrand,
    IntegrationMethod,
    integrate_left_rectangles,
    integrate_midpoint_rectangles,
    integrate_right_rectangles,
    integrate_simpson,
    integrate_trapezoid,
)


def main() -> None:

    function: Integrand = lambda x: e**x
    exact_value = e - 1.0

    methods: list[tuple[str, IntegrationMethod]] = [
        ("Левые прямоугольники", integrate_left_rectangles),
        ("Правые прямоугольники", integrate_right_rectangles),
        ("Средние прямоугольники", integrate_midpoint_rectangles),
        ("Трапеции", integrate_trapezoid),
        ("Симпсон", integrate_simpson),
    ]

    interval_counts = [4, 8, 16, 32, 64, 128, 256, 512, 1024]
    step_sizes: list[float] = []
    errors: dict[str, list[float]] = {name: [] for name, _ in methods}

    print(f"Точное значение интеграла: {exact_value:.15f}\n")
    print(
        f"{'Интервалы':>10} {'Шаг h':>14} "
        + " ".join(f"{name:>25}" for name, _ in methods)
    )
    print("-" * (27 + 26 * len(methods)))

    for interval_count in interval_counts:
        nodes = np.linspace(
            0.0,
            1.0,
            num=interval_count + 1,
            dtype=np.float64,
        )
        h = float(nodes[1] - nodes[0])
        step_sizes.append(h)

        row_errors: list[float] = []
        for name, method in methods:
            approximation = method(nodes, function)
            absolute_error = abs(approximation - exact_value)
            errors[name].append(absolute_error)
            row_errors.append(absolute_error)

        print(
            f"{interval_count:10d} {h:14.6e} "
            + " ".join(f"{error:25.6e}" for error in row_errors)
        )

    figure, axes = plt.subplots()
    step_array = np.asarray(step_sizes, dtype=np.float64)

    for name, _ in methods:
        error_array = np.asarray(errors[name], dtype=np.float64)
        positive = error_array > 0.0
        axes.loglog(
            step_array[positive][::-1],
            error_array[positive][::-1],
            marker="o",
            label=name,
        )

    axes.set_title("Абсолютная погрешность методов интегрирования")
    axes.set_xlabel("Шаг сетки h")
    axes.set_ylabel("Абсолютная погрешность |I_h - I|")
    axes.grid(True, which="both", linestyle="--", alpha=0.6)
    axes.legend()
    figure.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
