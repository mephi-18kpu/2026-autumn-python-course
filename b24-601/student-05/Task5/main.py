from typing import Callable

import numpy as np
import matplotlib.pyplot as plt
from integration_methods import *
value = np.e - 1
f: Integrand = lambda x: np.exp(x)
nodes = [np.linspace(0,1, 10**i + 1) for i in range(1,6)]
methods = {'Левые прямоугольники': integrate_left_rectangles,
           'Правые прямоугольники': integrate_right_rectangles,
           'Средние прямоугольники': integrate_midpoint_rectangles,
           'Трапеции': integrate_trapezoid,
           'Симпсон': integrate_simpson}
errors = {name: np.array([abs(method(i, f) - value) for i in nodes])
    for name, method in methods.items()}
print(f"{'Порядок числа разбиений':>7}" + "".join(f"{name:>24}" for name in methods))
for k, grid in enumerate(nodes):
    print(f"        {grid.size-1:>7}" + "   ".join(f"{errors[n][k]:>24.3e}" for n in methods))
fig, ax = plt.subplots()
for name in methods:
    ax.loglog([len(n)-1 for n in nodes], errors[name], marker='o', label=name)
ax.set_title('Погрешность методов численного интегрирования')
ax.grid(True, which='both'); ax.legend()
ax.set_xlabel("Порядок числа разбиений")
ax.set_ylabel("Абсолютная погрешность")
ax.grid(True, which="both")
ax.legend()
plt.show()
