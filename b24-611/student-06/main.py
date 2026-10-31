from typing import Callable

import numpy as np
import matplotlib.pyplot as plt
from integration_methods import *

f: Integrand = lambda x: np.exp(x)

methods: dict[str, IntegrationMethod] = {
    "Левые": integrate_left_rectangles,
    "Правые": integrate_right_rectangles,
    "Средние": integrate_midpoint_rectangles,
    "Трапеции": integrate_trapezoid,
    "Симпсон": integrate_simpson,
}

intervals = [100, 200, 500, 750, 1000]
a, b = 0.0, 1.0
exact = np.e - 1

errors = {name: [] for name in methods}
steps = []
for n in intervals:
    nodes = np.linspace(a, b, n + 1, dtype=np.float64)
    steps.append((b - a) / n)
    for name, method in methods.items():
        errors[name].append(abs(method(nodes, f) - exact))

print(f"{'n':>6} {'h':>10}", end="")

for name in methods:
    print(f" {name:>12}", end="")
print()

for n in intervals:
    nodes = np.linspace(a, b, n + 1, dtype=np.float64)
    h = (b - a) / n
    print(f"{n:>6} {h:>10.5f}", end="")
    for method in methods.values():
        error = abs(method(nodes, f) - exact)
        print(f" {error:>12.3e}", end="")
    print()

fig, ax = plt.subplots()
for name, errs in errors.items():
    ax.loglog(steps, errs, marker="o", label=name)

ax.set_xlabel("Шаг сетки h")
ax.set_ylabel("Абсолютная погрешность")
ax.set_title("Погрешность методов интегрирования")
ax.grid(True, which="both", alpha=0.3)
ax.legend()
plt.show()
