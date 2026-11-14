from pathlib import Path
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

func: Integrand = lambda x: np.exp(x)
lo, hi = 0.0, 1.0
true_value = np.e - 1

rules: dict[str, IntegrationMethod] = {
    "Левые": integrate_left_rectangles,
    "Правые": integrate_right_rectangles,
    "Средние": integrate_midpoint_rectangles,
    "Трапеции": integrate_trapezoid,
    "Симпсон": integrate_simpson,
}

intervals = [4, 8, 16, 32, 64, 128, 256]

hs = []
approx = {name: [] for name in rules}
err = {name: [] for name in rules}
for n in intervals:
    grid = np.linspace(lo, hi, n + 1, dtype=np.float64)
    hs.append((hi - lo) / n)
    for name, rule in rules.items():
        value = rule(grid, func)
        approx[name].append(value)
        err[name].append(abs(value - true_value))

print(f"Точное значение: {true_value:.12f}\n")

print("Приближённые значения")
print(f"{'n':>5} {'h':>9}", end="")
for name in rules:
    print(f" {name:>14}", end="")
print()
for i, n in enumerate(intervals):
    print(f"{n:>5} {hs[i]:>9.5f}", end="")
    for name in rules:
        print(f" {approx[name][i]:>14.10f}", end="")
    print()

print("\nАбсолютные погрешности")
print(f"{'n':>5} {'h':>9}", end="")
for name in rules:
    print(f" {name:>14}", end="")
print()
for i, n in enumerate(intervals):
    print(f"{n:>5} {hs[i]:>9.5f}", end="")
    for name in rules:
        print(f" {err[name][i]:>14.3e}", end="")
    print()

fig, ax = plt.subplots(figsize=(8, 5))
for name in rules:
    ax.loglog(hs, err[name], marker="o", label=name)
ax.set_xlabel("Шаг сетки")
ax.set_ylabel("Абсолютная погрешность")
ax.set_title("Погрешность integral methods")
ax.grid(True, which="both", alpha=0.3)
ax.legend()
plt.show()
