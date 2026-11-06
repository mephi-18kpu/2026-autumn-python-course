"""Главный файл для проведения расчетов и построения графиков."""

# System imports

# External imports
import numpy as np
import matplotlib.pyplot as plt

# User imports
from integration_methods import (
    Integrand,
    IntegrationMethod,
    integrate_left_rectangles,
    integrate_midpoint_rectangles,
    integrate_right_rectangles,
    integrate_trapezoid,
    integrate_simpson,
)

#############################################


# Задаем подынтегральную функцию
function: Integrand = lambda x: np.exp(x)

# Пределы интегрирования и точное значение
a = 0.0
b = 1.0
exact_value = np.e - 1.0

# Количество узлов сетки (берем нечетные значения для метода Симпсона)
N_array = [5, 9, 17, 33, 65]

# Списки для хранения шагов и погрешностей
h_values = []
err_left = []
err_right = []
err_mid = []
err_trap = []
err_simp = []

# Присваиваем методам нужный тип
method_left: IntegrationMethod = integrate_left_rectangles
method_right: IntegrationMethod = integrate_right_rectangles
method_mid: IntegrationMethod = integrate_midpoint_rectangles
method_trap: IntegrationMethod = integrate_trapezoid
method_simp: IntegrationMethod = integrate_simpson

# --- Вычислительный цикл ---
for N in N_array:
    # Создаем равномерную сетку
    nodes = np.linspace(a, b, N, dtype=np.float64)
    h = nodes[1] - nodes[0]
    h_values.append(h)
    
    # Вычисляем интегралы каждым методом
    val_left = method_left(nodes, function)
    val_right = method_right(nodes, function)
    val_mid = method_mid(nodes, function)
    val_trap = method_trap(nodes, function)
    val_simp = method_simp(nodes, function)
    
    # Находим абсолютную погрешность и сохраняем результаты
    err_left.append(abs(val_left - exact_value))
    err_right.append(abs(val_right - exact_value))
    err_mid.append(abs(val_mid - exact_value))
    err_trap.append(abs(val_trap - exact_value))
    err_simp.append(abs(val_simp - exact_value))

# --- Вывод таблицы результатов ---
print(f"{'Метод':<25} | {'N=5':<10} | {'N=9':<10} | {'N=17':<10} | {'N=33':<10} | {'N=65':<10}")
print("-" * 85)

# Выводим строки таблицы (жестко прописываем индексы от 0 до 4, так как у нас 5 значений N)
print(f"{'Левые прямоугольники':<25} | {err_left[0]:<10.2e} | {err_left[1]:<10.2e} | {err_left[2]:<10.2e} | {err_left[3]:<10.2e} | {err_left[4]:<10.2e}")
print(f"{'Правые прямоугольники':<25} | {err_right[0]:<10.2e} | {err_right[1]:<10.2e} | {err_right[2]:<10.2e} | {err_right[3]:<10.2e} | {err_right[4]:<10.2e}")
print(f"{'Средние прямоугольники':<25} | {err_mid[0]:<10.2e} | {err_mid[1]:<10.2e} | {err_mid[2]:<10.2e} | {err_mid[3]:<10.2e} | {err_mid[4]:<10.2e}")
print(f"{'Трапеции':<25} | {err_trap[0]:<10.2e} | {err_trap[1]:<10.2e} | {err_trap[2]:<10.2e} | {err_trap[3]:<10.2e} | {err_trap[4]:<10.2e}")
print(f"{'Симпсон':<25} | {err_simp[0]:<10.2e} | {err_simp[1]:<10.2e} | {err_simp[2]:<10.2e} | {err_simp[3]:<10.2e} | {err_simp[4]:<10.2e}")
print("\n")

# --- Построение графика ---
plt.figure(figsize=(10, 6))

# Строим графики в логарифмическом масштабе
plt.loglog(h_values, err_left, marker='o', label='Левые прямоугольники')
plt.loglog(h_values, err_right, marker='s', label='Правые прямоугольники')
plt.loglog(h_values, err_mid, marker='^', label='Средние прямоугольники')
plt.loglog(h_values, err_trap, marker='v', label='Трапеции')
plt.loglog(h_values, err_simp, marker='d', label='Симпсон')

# Оформление осей и заголовка
plt.xlabel("Шаг сетки h")
plt.ylabel("Абсолютная погрешность")
plt.title("Зависимость абсолютной погрешности от шага сетки")

# Настройка сетки: основные линии сплошные, минорные (промежуточные) - пунктирные и бледные
plt.grid(True, which="major", linestyle="-", linewidth=0.8, alpha=0.7)
plt.grid(True, which="minor", linestyle=":", linewidth=0.5, alpha=0.5)

plt.legend()
plt.tight_layout() 

plt.show()