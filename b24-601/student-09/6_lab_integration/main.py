"""Вычислительный эксперимент по численному интегрированию."""

# System imports
from typing import List, Tuple
import math

# External imports
import matplotlib.pyplot as plt
import numpy as np

# User imports
from integration_methods import (
    IntegrationMethod,
    Integrand,
    integrate_left_rectangles,
    integrate_midpoint_rectangles,
    integrate_right_rectangles,
    integrate_simpson,
    integrate_trapezoid,
)

#############################################


def main() -> None:
    """Сравнить методы интегрирования и построить график погрешностей."""
    lower_bound = 0.0
    upper_bound = 1.0
    exact_integral = math.e - 1.0

    function: Integrand = lambda x: float(np.exp(x))

    methods: List[Tuple[str, IntegrationMethod]] = [
        ("Левые прямоугольники", integrate_left_rectangles),
        ("Правые прямоугольники", integrate_right_rectangles),
        ("Средние прямоугольники", integrate_midpoint_rectangles),
        ("Трапеции", integrate_trapezoid),
        ("Симпсона", integrate_simpson),
    ]

    # Число интервалов всегда чётное, поэтому оно подходит и для Симпсона.
    interval_counts = [4, 8, 16, 32, 64, 128, 256]
    steps = []
    errors = {name: [] for name, _ in methods}
    approximations = {name: [] for name, _ in methods}

    print(f"Точное значение интеграла: {exact_integral:.15f}")
    print()
    print(
        f"{'Интервалы':>10} {'Шаг':>12} "
        + " ".join(f"{name:>25}" for name, _ in methods)
    )
    print("-" * 150)

    for intervals in interval_counts:
        nodes = np.linspace(
            lower_bound,
            upper_bound,
            intervals + 1,
            dtype=np.float64,
        )
        step = float(nodes[1] - nodes[0])
        steps.append(step)

        row_values = []
        for method_name, method in methods:
            approximation = method(nodes, function)
            absolute_error = abs(approximation - exact_integral)
            approximations[method_name].append(approximation)
            errors[method_name].append(absolute_error)
            row_values.append(approximation)

        print(
            f"{intervals:10d} {step:12.6g} "
            + " ".join(f"{value:25.15f}" for value in row_values)
        )

    print()
    print("Абсолютные погрешности:")
    print(f"{'Интервалы':>10} {'Шаг':>12} " +
          " ".join(f"{name:>25}" for name, _ in methods))
    print("-" * 150)

    for row_index, intervals in enumerate(interval_counts):
        print(
            f"{intervals:10d} {steps[row_index]:12.6g} "
            + " ".join(
                f"{errors[name][row_index]:25.8e}"
                for name, _ in methods
            )
        )

    print()
    print("Отношение предыдущей погрешности к следующей при делении шага пополам:")
    for method_name, _ in methods:
        ratios = [
            errors[method_name][index] / errors[method_name][index + 1]
            if errors[method_name][index + 1] != 0.0
            else float("inf")
            for index in range(len(errors[method_name]) - 1)
        ]
        formatted_ratios = ", ".join(f"{ratio:.3g}" for ratio in ratios)
        print(f"{method_name}: {formatted_ratios}")

    figure, axes = plt.subplots()
    for method_name, _ in methods:
        axes.loglog(
            steps,
            errors[method_name],
            marker="o",
            label=method_name,
        )

    axes.set_xlabel("Шаг сетки h")
    axes.set_ylabel("Абсолютная погрешность")
    axes.set_title("Сравнение погрешностей методов численного интегрирования")
    axes.grid(True, which="both")
    axes.legend()
    figure.tight_layout()
    figure.savefig("integration_errors.png", dpi=150)
    plt.show()


if __name__ == "__main__":
    main()
