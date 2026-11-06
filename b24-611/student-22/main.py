"""Основной скрипт вычислительного эксперимента."""

import math
from typing import Dict, List
import numpy as np
import matplotlib.pyplot as plt

from integration_methods import (
    Integrand,
    IntegrationMethod,
    integrate_left_rectangles,
    integrate_midpoint_rectangles,
    integrate_right_rectangles,
    integrate_simpson,
    integrate_trapezoid,
)


def run_experiment() -> None:
    f: Integrand = lambda x: math.exp(x)
    exact_val: float = math.exp(1.0) - 1.0

    methods: Dict[str, IntegrationMethod] = {
        "Левые прямоугольники": integrate_left_rectangles,
        "Правые прямоугольники": integrate_right_rectangles,
        "Средние прямоугольники": integrate_midpoint_rectangles,
        "Трапеции": integrate_trapezoid,
        "Симпсон": integrate_simpson,
    }

    n_intervals: List[int] = [2**k for k in range(1, 11)]  # n = 2, 4, ..., 1024

    errors: Dict[str, List[float]] = {name: [] for name in methods}
    h_values: List[float] = []

    a, b = 0.0, 1.0

    for n in n_intervals:
        N = n + 1
        nodes = np.linspace(a, b, num=N, dtype=np.float64)
        h = float((b - a) / n)
        h_values.append(h)

        for name, method in methods.items():
            val = method(nodes, f)
            err = abs(val - exact_val)
            errors[name].append(err)

    header = f"{'n':<6} | {'h':<10} | " + " | ".join([f"{name:<22}" for name in methods])
    print(header)
    print("-" * len(header))
    for idx, n in enumerate(n_intervals):
        h_str = f"{h_values[idx]:.6f}"
        row_str = f"{n:<6} | {h_str:<10} | " + " | ".join([f"{errors[name][idx]:.4e}" for name in methods])
        print(row_str)

    print("\nОтношение уменьшения погрешности E(h) / E(h/2):")
    print(f"{'n -> 2n':<10} | " + " | ".join([f"{name:<22}" for name in methods]))
    print("-" * (12 + 25 * len(methods)))
    for i in range(len(n_intervals) - 1):
        pair_label = f"{n_intervals[i]}->{n_intervals[i+1]}"
        ratios = [f"{errors[name][i] / errors[name][i+1]:.4f}" for name in methods]
        print(f"{pair_label:<10} | " + " | ".join(ratios))

    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    markers = ['o', 's', '^', 'v', 'd']
    lines = ['-', '--', '-.', ':', '-']

    for (name, err_list), marker, line in zip(errors.items(), markers, lines):
        ax.loglog(h_values, err_list, label=name, marker=marker, linestyle=line, linewidth=1.5, markersize=5)

    ax.set_xlabel("Шаг сетки $h$", fontsize=12)
    ax.set_ylabel("Абсолютная погрешность $E(h) = |I_h - I|$", fontsize=12)
    ax.set_title("Зависимость погрешности численного интегрирования $\\int_0^1 e^x dx$ от шага $h$", fontsize=13)
    ax.grid(True, which="both", linestyle="--", alpha=0.6)
    ax.legend(fontsize=10)
    fig.tight_layout()
    fig.savefig("error_analysis.png")
    plt.close(fig)


if __name__ == "__main__":
    run_experiment()
