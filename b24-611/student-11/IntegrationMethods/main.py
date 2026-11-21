import matplotlib.pyplot as plt
import numpy as np
from integration_methods import (
    Integrand,
    IntegrationMethod,
    integrate_left_rectangles,
    integrate_midpoint_rectangles,
    integrate_right_rectangles,
    integrate_trapezoid,
    integrate_simpson,
)

integrand: Integrand = lambda x: float(np.exp(x))
exact_value: float = float(np.exp(1.0) - 1.0)
errors_left = []
errors_right = []
errors_midpoint = []
errors_trapezoid = []
errors_simpson = []

num_intervals = np.array([8, 16, 32, 64, 128, 256])
steps = 1.0 / num_intervals

print(f"{'Шаг (h)':<12} | {'Левые':<10} | {'Правые':<10} | {'Средние':<10} | {'Трапеции':<10} | {'Симпсон':<10}")
print("-" * 75)

for N in num_intervals:
    h = 1.0 / N

    nodes = np.linspace(0.0, 1.0, num=N + 1, dtype=np.float64)

    approx_left = integrate_left_rectangles(nodes, integrand)
    approx_right = integrate_right_rectangles(nodes, integrand)
    approx_mid = integrate_midpoint_rectangles(nodes, integrand)
    approx_trap = integrate_trapezoid(nodes, integrand)
    approx_simp = integrate_simpson(nodes, integrand)

    err_left = abs(approx_left - exact_value)
    err_right = abs(approx_right - exact_value)
    err_mid = abs(approx_mid - exact_value)
    err_trap = abs(approx_trap - exact_value)
    err_simp = abs(approx_simp - exact_value)

    errors_left.append(err_left)
    errors_right.append(err_right)
    errors_midpoint.append(err_mid)
    errors_trapezoid.append(err_trap)
    errors_simpson.append(err_simp)

    print(f"{h:<12.6f} | {err_left:<10.2e} | {err_right:<10.2e} | {err_mid:<10.2e} | {err_trap:<10.2e} | {err_simp:<10.2e}")



fig, ax = plt.subplots(figsize=(10, 6))

ax.loglog(steps, errors_left, marker='o', label="Левые прямоугольники")
ax.loglog(steps, errors_right, marker='o', label="Правые прямоугольники")
ax.loglog(steps, errors_midpoint, marker='o', label="Средние прямоугольники")
ax.loglog(steps, errors_trapezoid, marker='o', label="Трапеции")
ax.loglog(steps, errors_simpson, marker='o', label="Симпсон")

ax.set_xlabel("Шаг сетки (h)")
ax.set_ylabel("Абсолютная погрешность")
ax.set_title("Зависимость абсолютной погрешности методов от шага сетки")
ax.grid(True, which="both", ls="--")
ax.legend()

plt.show()
