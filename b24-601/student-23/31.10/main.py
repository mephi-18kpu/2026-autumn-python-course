
import math
import numpy as np
import matplotlib.pyplot as plt
from numpy.typing import NDArray

from integration_methods import (
    Integrand,
    IntegrationMethod,
    integrate_left_rectangles,
    integrate_right_rectangles,
    integrate_midpoint_rectangles,
    integrate_trapezoid,
    integrate_simpson,
)


def main():

    f: Integrand = lambda x: math.exp(x)
    exact_integral = math.e - 1.0
    a, b = 0.0, 1.0

    methods: list[tuple[str, IntegrationMethod]] = [
        ("Левые прямоуг.", integrate_left_rectangles),
        ("Правые прямоуг.", integrate_right_rectangles),
        ("Средние прямоуг.", integrate_midpoint_rectangles),
        ("Трапеции", integrate_trapezoid),
        ("Симпсон", integrate_simpson),
    ]


    interval_counts = [10 ** 1, 10 ** 2, 10 ** 3]

    results = {name: [] for name, _ in methods}

    header = f"{'n (инт.)':<8} | {'h':<8} | " + " | ".join(f"{name:<16}" for name, _ in methods)
    print(header)
    print("-" * len(header))

    for n in interval_counts:

        if n % 2 != 0:
            n += 1

        num_nodes = n + 1

        nodes: NDArray[np.float64] = np.linspace(a, b, num_nodes, dtype=np.float64)

        h = nodes[1] - nodes[0]

        row = f"{n:<8} | {h:<8.5f} |"
        for name, method in methods:
            approx = method(nodes, f)
            error = abs(approx - exact_integral)
            results[name].append((h, error))
            row += f" {error:<16.4e} |"
        print(row)

    plt.figure(figsize=(10, 6))

    for name, _ in methods:

        sorted_data = sorted(results[name], key=lambda x: x[0])
        h_values = [item[0] for item in sorted_data]
        error_values = [item[1] for item in sorted_data]

        plt.loglog(h_values, error_values, marker='o', label=name)

    plt.title("Абсолютная погрешность методов численного интегрирования")
    plt.xlabel("Шаг сетки h (логарифмический масштаб)")
    plt.ylabel("Абсолютная погрешность E(h) (логарифмический масштаб)")
    plt.grid(True, which="both", ls="--", alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
