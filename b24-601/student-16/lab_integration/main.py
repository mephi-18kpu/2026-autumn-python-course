"""Вычислительный эксперимент по численному интегрированию."""
import math
import numpy as np
import matplotlib.pyplot as plt
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
    exact_value = math.e - 1.0

    methods: list[tuple[str, IntegrationMethod]] = [
        ("Левые прямоугольники", integrate_left_rectangles),
        ("Правые прямоугольники", integrate_right_rectangles),
        ("Средние прямоугольники", integrate_midpoint_rectangles),
        ("Трапеции", integrate_trapezoid),
        ("Симпсон", integrate_simpson),
    ]


    powers = range(2, 10)
    N_values = [2 ** k + 1 for k in powers]


    errors_data = {name: [] for name, _ in methods}
    h_values = []

    print(f"{'N узлов':<10} | {'Шаг h':<10} | Точное значение: {exact_value:.8f}")
    print("-" * 70)


    for N in N_values:

        nodes = np.linspace(0.0, 1.0, N, dtype=np.float64)
        h = nodes[1] - nodes[0]
        h_values.append(h)
        print(f"N = {N:<6} | h = {h:.6f}")
        for name, method in methods:
            approx_value = method(nodes, f)
            error = abs(approx_value - exact_value)
            errors_data[name].append(error)
            print(f"  -> {name:<25}: {approx_value:.10f} (ошибка: {error:.2e})")

    plt.figure(figsize=(10, 6))
    for name, _ in methods:

        plt.loglog(h_values, errors_data[name], marker='o', label=name)
    plt.title("Сходимость методов численного интегрирования")
    plt.xlabel("Шаг сетки (h)")
    plt.ylabel("Абсолютная погрешность (E)")
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.legend()
    plt.gca().invert_xaxis()
    plt.savefig("integration_errors.png", dpi=300)
    plt.show()
if __name__ == "__main__":
    main()