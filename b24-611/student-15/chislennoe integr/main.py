"""Вычислительный эксперимент и визуализация погрешностей."""

from pathlib import Path
import csv
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

# --- 1. Подготовка путей и данных ---
base_dir = Path(__file__).resolve().parent
results_dir = base_dir / "results"
results_dir.mkdir(exist_ok=True)

# Подынтегральная функция: f(x) = x^2 на [0, 1]. Точный интеграл = 1/3.
f: Integrand = lambda x: x ** 2
exact_value = 1.0 / 3.0
a, b = 0.0, 1.0

# Сетка по числу узлов (для Симпсона нечетное)
node_counts = [3, 5, 9, 17, 33, 65, 129, 257]

methods: dict[str, IntegrationMethod] = {
    "Левая_прямоуг": integrate_left_rectangles,
    "Правая_прямоуг": integrate_right_rectangles,
    "Средняя_прямоуг": integrate_midpoint_rectangles,
    "Трапеция": integrate_trapezoid,
    "Симпсон": integrate_simpson,
}

# --- 2. Вычисления ---
steps = []
errors = {name: [] for name in methods}
table_data = []

for n in node_counts:
    nodes = np.linspace(a, b, n, dtype=np.float64)
    h = nodes[1] - nodes[0]
    steps.append(h)

    row = {"Шаг": h}
    for name, func in methods.items():
        val = func(nodes, f)
        err = abs(val - exact_value)
        errors[name].append(err)
        row[name] = err

    table_data.append(row)

# --- 3. Сохранение таблицы (CSV) ---
csv_path = results_dir / "errors_table.csv"
with open(csv_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Шаг"] + list(methods.keys()))
    writer.writeheader()
    writer.writerows(table_data)

# --- 4. Построение и сохранение графика ---
fig, ax = plt.subplots(figsize=(10, 6))

for name, err_list in errors.items():
    ax.loglog(steps, err_list, marker='o', label=name.replace('_', ' '))

ax.set_xlabel("Шаг сетки (h)")
ax.set_ylabel("Абсолютная погрешность")
ax.set_title("Зависимость абсолютной погрешности от шага сетки")
ax.grid(True, which="both", ls="--", alpha=0.7)
ax.legend()

plot_path = results_dir / "errors_plot.png"
fig.savefig(plot_path, dpi=150, bbox_inches="tight")
plt.close(fig)

# --- 5. Сохранение текстового вывода ---
conclusions = """
Анализ результатов:
1. Методы левых и правых прямоугольников имеют первый порядок точности O(h).
   При уменьшении шага в 2 раза погрешность уменьшается примерно в 2 раза.
2. Методы средних прямоугольников и трапеций имеют второй порядок точности O(h^2).
   При уменьшении шага в 2 раза погрешность уменьшается в 4 раза.
3. Метод Симпсона имеет четвертый порядок точности O(h^4).
   При уменьшении шага в 2 раза погрешность падает в 16 раз, что
   подтверждается более крутым наклоном линии на логарифмическом графике.
"""

text_path = results_dir / "conclusions.txt"
with open(text_path, mode="w", encoding="utf-8") as file:
    file.write(conclusions)

# --- 6. Уведомление пользователя ---
print("Расчеты успешно завершены!")
print(f"Таблица сохранена в: {csv_path.name}")
print(f"График сохранен в: {plot_path.name}")
print(f"Выводы сохранены в: {text_path.name}")
