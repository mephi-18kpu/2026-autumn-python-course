from typing import Callable
import numpy as np
import matplotlib.pyplot as plt
from integration_methods import *

value = np.e - 1    # "Эталонное" значение
f: Integrand = lambda x: np.exp(x)

nodes = [np.linspace(0,1, 10**i + 1) for i in range(1,6)] # Массив с разбиениями, 10**i + 1 для нечётного числа узлов, чтобы метод Симпсона работал корректно
methods = {'Левые прямоугольники': integrate_left_rectangles,           # Словарь, где ключами выступают названия методов, а значения-соответствующие функции
           'Правые прямоугольники': integrate_right_rectangles,
           'Средние прямоугольники': integrate_midpoint_rectangles,
           'Трапеции': integrate_trapezoid,
           'Симпсон': integrate_simpson}
errors = {name: np.array([abs(method(i, f) - value) for i in nodes])    # Рассчёт абсолюной ошибки. В качестве ключей-названия методов
    for name, method in methods.items()}                                # в качестве значений - массивы разницы полученного значения и "эталона" для 11, 101, ... узлов

print(f"{'Порядок числа разбиений':>7}" + "".join(f"{name:>24}" for name in methods))
for k, grid in enumerate(nodes):
    print(f"        {grid.size-1:>7}" + "   ".join(f"{errors[n][k]:>24.3e}" for n in methods)) # Вывод таблицы

fig, ax = plt.subplots()
for name in methods:
    ax.loglog([len(n)-1 for n in nodes], errors[name], marker='o', label=name)  # Вывод графиков. В качестве значений по оси x порядок числа узлов
ax.set_title('Погрешность методов численного интегрирования')                         # значения по оси y-соответствующая величина ошибки. Для каждого метода производится вызов
ax.grid(True, which='both'); ax.legend()                                       # нужного массива ошибок путём подставления ключа из словаря методов
ax.set_xlabel("Порядок числа разбиений")
ax.set_ylabel("Абсолютная погрешность")
ax.grid(True, which="both")
ax.legend()
plt.show()
