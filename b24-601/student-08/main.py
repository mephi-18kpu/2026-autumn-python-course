import math

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

f: Integrand = lambda x: math.exp(x)

exact = math.e - 1.0

n_intervals_list = [2, 4, 8, 16, 32, 64, 128, 256]

methods: dict[str, IntegrationMethod] = {
    "Левые прямоугольники": integrate_left_rectangles,
    "Правые прямоугольники": integrate_right_rectangles,
    "Средние прямоугольники": integrate_midpoint_rectangles,
    "Трапеции": integrate_trapezoid,
    "Симпсон": integrate_simpson,
}

results: dict[str, tuple[list[float], list[float]]] = {
    name: ([], []) for name in methods
}

for n in n_intervals_list:
    nodes = np.linspace(0.0, 1.0, n + 1, dtype=np.float64)
    h = 1.0 / n
    for name, method in methods.items():
        approx = method(nodes, f)
        error = abs(approx - exact)
        steps, errors = results[name]
        steps.append(h)
        errors.append(error)

print(f"{'Метод':<28} {'h':>8} {'Погрешность':>16}")
print("-" * 56)
for name in methods:
    steps, errors = results[name]
    for h, err in zip(steps, errors):
        print(f"{name:<28} {h:>8.5f} {err:>16.6e}")
    print()

fig, ax = plt.subplots(figsize=(10, 6))
for name, (steps, errors) in results.items():
    ax.loglog(steps, errors, marker="o", label=name)

ax.set_xlabel("Шаг сетки h")
ax.set_ylabel("Абсолютная погрешность")
ax.set_title("Зависимость погрешности от шага сетки")
ax.legend()
ax.grid(True, which="both", ls="--", alpha=0.6)
plt.tight_layout()
plt.show()

print("Уменьшение погрешности при делении h пополам:")
for name, (steps, errors) in results.items():
    ratios = []
    for i in range(1, len(errors)):
        if errors[i] > 0 and errors[i - 1] > 0:
            ratios.append(errors[i - 1] / errors[i])
    if ratios:
        avg = sum(ratios) / len(ratios)
        print(f"{name:<28}: среднее отношение ≈ {avg:.2f}")
