import numpy as np
import matplotlib.pyplot as plt
from integration_methods import (
    Integrand,
    IntegrationMethod,
    integrate_left_rectangles,
    integrate_midpoint_rectangles,
    integrate_right_rectangles,
    integrate_trapezoid,
    integrate_simpson,
)

function: Integrand = lambda x: np.exp(x)
exact_value = np.e - 1
a = 0
b = 1

N_array = [11, 101, 1001, 10001, 100001]

methods = {
    "Левые прямоугольники": integrate_left_rectangles,
    "Правые прямоугольники": integrate_right_rectangles,
    "Средние прямоугольники": integrate_midpoint_rectangles,
    "Трапеции": integrate_trapezoid,
    "Симпсон": integrate_simpson,
}

errors_by_method = {name: [] for name in methods.keys()}

for N in N_array:
    nodes = np.linspace(a, b, N)

    for name, method in methods.items():
        error = abs(exact_value - method(nodes, function))
        errors_by_method[name].append(error)


fig, ax = plt.subplots(figsize=(10, 6))

for name in methods.keys():
    ax.loglog(N_array, errors_by_method[name], marker='o', label=name)

ax.set_xlabel("Количество узлов N (логарифмический масштаб)")
ax.set_ylabel("Абсолютная погрешность (логарифмический масштаб)")
ax.set_title("Зависимость абсолютной погрешности от количества узлов N")
ax.grid(True, which="both", linestyle="--", alpha=0.7)




# Шапка
header = f"{'Метод':<25} | "
for N in N_array:
    header += f"N={N:<8} | "
print(header)
print("-" * len(header))

# Строки
for name in methods.keys():
    row = f"{name:<25} | "
    for error in errors_by_method[name]:
        row += f"{error:<10.2e} | "
    print(row)

ax.legend()
plt.show()

"""
Как мы видим, методы левых и правых прямоугольников дают практически одинаковый результат.
Стоит отметить, что метод Симпсона, как и предполагалось, оказывается самым точным,
и чем больше сетку мы ему даем, тем точнее он аппроксимирует исходную функцию.
"""
