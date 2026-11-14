# External imports
import matplotlib.pyplot as plt
import numpy as np

# User imports
from integration_methods import (
    Integrand,
    integrate_left_rectangles,
    integrate_midpoint_rectangles,
    integrate_right_rectangles,
    integrate_simpson,
    integrate_trapezoid,
)

#############################################

function: Integrand = lambda x: np.exp(x)
I_exact = np.e - 1
node_counts = [5, 11, 23, 47, 95, 191]

h_values = []
errors_left = []
errors_right = []
errors_mid = []
errors_trap = []
errors_simp = []

print(f"{'N':<6} | {'Шаг h':<10} | {'Левые':<12} | {'Средние':<12} | {'Трапеции':<12} | {'Симпсон':<12}")
print("-" * 75)

for n_nodes in node_counts:
    nodes = np.linspace(0.0, 1.0, n_nodes)
    h = nodes[1] - nodes[0]
    h_values.append(h)

    res_left = integrate_left_rectangles(nodes, function)
    res_right = integrate_right_rectangles(nodes, function)
    res_mid = integrate_midpoint_rectangles(nodes, function)
    res_trap = integrate_trapezoid(nodes, function)
    res_simp = integrate_simpson(nodes, function)

    err_left = abs(res_left - I_exact)
    err_right = abs(res_right - I_exact)
    err_mid = abs(res_mid - I_exact)
    err_trap = abs(res_trap - I_exact)
    err_simp = abs(res_simp - I_exact)

    errors_left.append(err_left)
    errors_right.append(err_right)
    errors_mid.append(err_mid)
    errors_trap.append(err_trap)
    errors_simp.append(err_simp)

    print(f"{n_nodes:<6} | {h:<10.5f} | {err_left:<12.2e} | {err_mid:<12.2e} | {err_trap:<12.2e} | {err_simp:<12.2e}")

fig, ax = plt.subplots(figsize=(12, 6))

ax.loglog(h_values, errors_left, 'o-', label='Левые прямоугольники (O(h))')
ax.loglog(h_values, errors_right, 'o-', label='Правые прямоугольники (O(h))')
ax.loglog(h_values, errors_mid, 'o-', label='Средние прямоугольники (O(h^2))')
ax.loglog(h_values, errors_trap, 'o-', label='Трапеции (O(h^2))')
ax.loglog(h_values, errors_simp, 'o-', label='Симпсон (O(h^4))')

ax.set_xlabel('Шаг сетки h')
ax.set_ylabel('Абсолютная погрешность E(h)')
ax.set_title('Сравнение погрешностей методов численного интегрирования')
ax.grid(True, which="both")
ax.legend()

plt.show()
