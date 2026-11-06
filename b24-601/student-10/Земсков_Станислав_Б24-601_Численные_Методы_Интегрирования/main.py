"""Интегрирование exp(x) на [0, 1] пятью методами."""

from math import exp

import matplotlib.pyplot as plt
import numpy as np

from integration_methods import (
    Integrand,
    IntegrationMethod,
    integrate_left_rectangles,
    integrate_right_rectangles,
    integrate_midpoint_rectangles,
    integrate_trapezoid,
    integrate_simpson,
)


function: Integrand = lambda x: exp(x)
exact = exp(1.0) - 1.0
interval_counts = [2, 4, 8, 16, 32, 64, 128, 256]

methods: list[IntegrationMethod] = [
    integrate_left_rectangles,
    integrate_right_rectangles,
    integrate_midpoint_rectangles,
    integrate_trapezoid,
    integrate_simpson,
]
names = [
    "Левые прямоугольники", "Правые прямоугольники",
    "Средние прямоугольники", "Трапеции", "Симпсон",
]
markers = ["o", "x", "s", "^", "D"]

print(f"Точное значение интеграла: {exact:.15f}", flush=True)
print("q показывает, во сколько раз уменьшилась ошибка при делении шага пополам.")
fig, ax = plt.subplots(figsize=(10, 6))

for i in range(len(methods)):
    method: IntegrationMethod = methods[i]
    steps = []
    errors = []
    previous_error = None

    print("\n" + names[i])
    print(f"{'n':>4} {'h':>10} {'Интеграл':>20} {'Ошибка':>14} {'q':>10}")

    for n in interval_counts:
        # n интервалов означают n + 1 узлов.
        nodes = np.linspace(0.0, 1.0, num=n + 1, dtype=np.float64)
        h = float(nodes[1] - nodes[0])
        value = method(nodes, function)
        error = abs(value - exact)

        ratio = "-"
        if previous_error is not None and error > 0:
            ratio = f"{previous_error / error:.4f}"
        print(f"{n:4d} {h:10.7f} {value:20.15f} {error:14.6e} {ratio:>10}")
        previous_error = error

        # Нулевую ошибку нельзя откладывать на логарифмической оси.
        if error > 0:
            steps.append(h)
            errors.append(error)

    ax.loglog(steps, errors, marker=markers[i], label=names[i])

print("\nВывод: ошибка левых и правых прямоугольников уменьшается примерно в 2 раза.")
print("У средних прямоугольников и трапеций - в 4 раза, у Симпсона - в 16 раз.")
print("Это соответствует порядкам O(h), O(h^2) и O(h^4).", flush=True)

ax.set_title("Интеграл exp(x) на [0, 1]")
ax.set_xlabel("Шаг сетки h")
ax.set_ylabel("Абсолютная погрешность")
ax.legend()
ax.grid(True, which="both", alpha=0.3)
fig.tight_layout()
fig.savefig("error_plot.png", dpi=150)
plt.show()
