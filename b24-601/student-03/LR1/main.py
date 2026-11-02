import numpy as np
import matplotlib.pyplot as plt
from integration_methods import (   #Импорты
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
b = 1               ##Параметры сетки
N_array = [10, 10 ** 2, 10 ** 3]

methods = {
    "Левые прямоугольники": integrate_left_rectangles,
    "Правые прямоугольники": integrate_right_rectangles,
    "Средние прямоугольники": integrate_midpoint_rectangles,
    "Трапеции": integrate_trapezoid,
    "Симпсон": integrate_simpson,
}               #Словарь: Названия - методы

errors_by_method = {name: [] for name in methods.keys()}  #Словарь ошибок соответ. методу

for N in N_array:
    nodes = np.linspace(a, b, N)
    if N % 2 == 0:
        nodes = np.linspace(a, b, N + 1)

    for name, method in methods.items():            #Считаем ошибку для каждого метода
        error = {name: abs(exact_value - method(nodes, function))}


        errors_by_method[name].append(error[name]) #Добавялем в словарь по названию метода ошибку для него



plt.figure(figsize=(10, 6))

for name in methods.keys():
    plt.loglog(N_array, errors_by_method[name], marker='o', label=name)

plt.xlabel("Количество узлов N (логарифмический масштаб)")
plt.ylabel("Абсолютная погрешность (логарифмический масштаб)")
plt.title("Зависимость абсолютной погрешности от количества узлов N")
plt.grid(True, which="both", linestyle="--", alpha=0.7)
plt.legend()
plt.show()

