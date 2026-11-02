import math
from pathlib import Path

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

graph = Path("graph_output")
graph.mkdir(parents=True, exist_ok=True)

fun: Integrand = lambda x: np.exp(x)
spaces = [
    np.linspace(0, 1, 51, dtype=np.float64),
    np.linspace(0, 1, 10**2+1, dtype=np.float64),
    np.linspace(0, 1, 10**3+1, dtype=np.float64),
    np.linspace(0, 1, 10**4+1, dtype=np.float64),
    np.linspace(0, 1, 10**5+1, dtype=np.float64)
]

results = np.zeros((5, 5), dtype=np.float64)
names = ["Левые прямоугольники", "Правые прямоугольники",
         "Средние прямоугольники", "Трапеции", "Метод Симпсона"]
real = math.e - 1
space_volume = [len(x) for x in spaces]

for i in range(5):
    results[0][i] = integrate_left_rectangles(spaces[i], fun)
    results[1][i] = integrate_right_rectangles(spaces[i], fun)
    results[2][i] = integrate_midpoint_rectangles(spaces[i], fun)
    results[3][i] = integrate_trapezoid(spaces[i], fun)
    results[4][i] = integrate_simpson(spaces[i], fun)

print(f"{names[0]}:   {results[0]}\n"
      f"{names[1]}:  {results[1]}\n"
      f"{names[2]}: {results[2]}\n"
      f"{names[3]}:               {results[3]}\n"
      f"{names[4]}:        {results[4]}\n")

errors = np.abs(results - real)

plt.figure(figsize=(16, 9))

for j, name in enumerate(names):
    plt.loglog(space_volume, errors[j], marker="o", label=name)

plt.xlabel("n")
plt.ylabel("Погрешность")
plt.legend()
plt.grid(alpha=0.7)
plt.savefig(graph / "errors.png", dpi=150, bbox_inches="tight")
plt.show()
