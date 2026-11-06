import numpy as np
import matplotlib.pyplot as plt
from integration_methods import (
    Integrand, IntegrationMethod,
    integrate_left_rectangles, integrate_right_rectangles, integrate_midpoint_rectangles,
    integrate_trapezoid, integrate_simpson
)

f: Integrand = lambda x: np.exp(x)
exact_value = np.e - 1


methods = [integrate_left_rectangles,
           integrate_right_rectangles,
           integrate_midpoint_rectangles,
           integrate_trapezoid,
           integrate_simpson]
method_names = ['Левые прямоугольники: ',
                'Правые прямоугольники: ',
                'Средние прямоугольники: ',
                "Трапеции: ",
                "Симпсон: "]


steps = []
n = [10, 20, 50, 100, 250, 500, 1000]
errors = [[] for _ in range(len(methods))]
for j in n:
    nodes = np.linspace(0, 1, j+1)
    h = nodes[1] - nodes[0]
    steps.append(h)


    for i, method in enumerate(methods):
        result = method(nodes,f)
        error = abs(exact_value - result)
        errors[i].append(error)

plt.figure(figsize=(10, 6))

for i in range(5):
    plt.loglog(steps, errors[i], marker='o', label=method_names[i])

plt.title('Зависимость абсолютной погрешности от шага h')
plt.xlabel('Шаг h')
plt.ylabel('Абсолютная погрешность')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.show()

