"""Главный исполняемый модуль для численного эксперимента и визуализации."""

# System imports

# External imports
import matplotlib.pyplot as plt
import numpy as np

# User imports
from integration_methods import (
    Integrand,
    IntegrationMethod,
    integrate_left_rectangles,
    integrate_midpoint_rectangles,
    integrate_right_rectangles,
    integrate_simpson,
    integrate_trapezoid,
)

#############################################

# Определение подынтегральной функции через lambda-выражение
integrand_function: Integrand = lambda x: np.exp(x)

# Задание границ интервала и аналитического точного значения интеграла
lower_bound = 0.0
upper_bound = 1.0
true_integral_value = np.e - 1.0

# Набор числе узлов сетки (для метода Симпсона используются только нечётные значения)
grid_nodes_counts = [5, 9, 17, 33, 65]

# Коллекции для сохранения шагов и погрешностей методов
steps_collection = []
errors_left = []
errors_right = []
errors_midpoint = []
errors_trapezoid = []
errors_simpson = []

# Привязка методов к аннотированным переменным типа IntegrationMethod
method_left_ref: IntegrationMethod = integrate_left_rectangles
method_right_ref: IntegrationMethod = integrate_right_rectangles
method_mid_ref: IntegrationMethod = integrate_midpoint_rectangles
method_trapezoid_ref: IntegrationMethod = integrate_trapezoid
method_simpson_ref: IntegrationMethod = integrate_simpson

# Основной вычислительный цикл по различным размерам сеток
for count in grid_nodes_counts:
    nodes_grid = np.linspace(lower_bound, upper_bound, count, dtype=np.float64)
    current_step = nodes_grid[1] - nodes_grid[0]
    steps_collection.append(current_step)
    
    # Расчёт значений интегралов
    res_left = method_left_ref(nodes_grid, integrand_function)
    res_right = method_right_ref(nodes_grid, integrand_function)
    res_mid = method_mid_ref(nodes_grid, integrand_function)
    res_trap = method_trapezoid_ref(nodes_grid, integrand_function)
    res_simp = method_simpson_ref(nodes_grid, integrand_function)
    
    # Расчёт абсолютных погрешностей
    errors_left.append(abs(res_left - true_integral_value))
    errors_right.append(abs(res_right - true_integral_value))
    errors_midpoint.append(abs(res_mid - true_integral_value))
    errors_trapezoid.append(abs(res_trap - true_integral_value))
    errors_simpson.append(abs(res_simp - true_integral_value))

# Форматированный вывод результатов в виде таблицы
print(f"{'Метод интегрирования':<26} | {'N = 5':<10} | {'N = 9':<10} | {'N = 17':<10} | {'N = 33':<10} | {'N = 65':<10}")
print("-" * 90)
print(f"{'Левые прямоугольники':<26} | {errors_left[0]:<10.2e} | {errors_left[1]:<10.2e} | {errors_left[2]:<10.2e} | {errors_left[3]:<10.2e} | {errors_left[4]:<10.2e}")
print(f"{'Правые прямоугольники':<26} | {errors_right[0]:<10.2e} | {errors_right[1]:<10.2e} | {errors_right[2]:<10.2e} | {errors_right[3]:<10.2e} | {errors_right[4]:<10.2e}")
print(f"{'Средние прямоугольники':<26} | {errors_midpoint[0]:<10.2e} | {errors_midpoint[1]:<10.2e} | {errors_midpoint[2]:<10.2e} | {errors_midpoint[3]:<10.2e} | {errors_midpoint[4]:<10.2e}")
print(f"{'Метод трапеций':<26} | {errors_trapezoid[0]:<10.2e} | {errors_trapezoid[1]:<10.2e} | {errors_trapezoid[2]:<10.2e} | {errors_trapezoid[3]:<10.2e} | {errors_trapezoid[4]:<10.2e}")
print(f"{'Метод Симпсона':<26} | {errors_simpson[0]:<10.2e} | {errors_simpson[1]:<10.2e} | {errors_simpson[2]:<10.2e} | {errors_simpson[3]:<10.2e} | {errors_simpson[4]:<10.2e}")
print("\n")

# Построение графиков сходимости в логарифмическом масштабе
fig, ax = plt.subplots(figsize=(10, 6))

ax.loglog(steps_collection, errors_left, marker='o', label='Левые прямоугольники')
ax.loglog(steps_collection, errors_right, marker='s', label='Правые прямоугольники')
ax.loglog(steps_collection, errors_midpoint, marker='^', label='Средние прямоугольники')
ax.loglog(steps_collection, errors_trapezoid, marker='v', label='Трапеции')
ax.loglog(steps_collection, errors_simpson, marker='d', label='Симпсон')

ax.set_xlabel("Шаг сетки (h)")
ax.set_ylabel("Абсолютная погрешность E(h)")
ax.set_title("Исследование погрешности методов численного интегрирования")

ax.grid(True, which="major", linestyle="-", linewidth=0.8, alpha=0.7)
ax.grid(True, which="minor", linestyle=":", linewidth=0.5, alpha=0.5)

ax.legend()
plt.tight_layout()
plt.show()