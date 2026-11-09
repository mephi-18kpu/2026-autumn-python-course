"""
Ошибся с абсолютными импортами подмодулей,
поэтому при запуске из корня репозитория (как
и надо работать ошибка:

D:\Tuition\2026-autumn-python-course\.venv\Scripts\python.exe D:\Tuition\2026-autumn-python-course\b24-601\student-01\homeworks\hw5\main.py
Traceback (most recent call last):
  File "D:\Tuition\2026-autumn-python-course\b24-601\student-01\homeworks\hw5\main.py", line 10, in <module>
    from integration_methods import (
    ...<7 lines>...
    )
  File "D:\Tuition\2026-autumn-python-course\b24-601\student-01\homeworks\hw5\integration_methods\__init__.py", line 9, in <module>
    from homeworks.hw5.integration_methods.simpson import integrate_simpson
ModuleNotFoundError: No module named 'homeworks'


Если разобрал, что нейронка сделала, то норм

"""

import math
from typing import Dict, List


import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import NDArray


from integration_methods import (
    Integrand,
    IntegrationMethod,
    integrate_left_rectangles,
    integrate_midpoint_rectangles,
    integrate_right_rectangles,
    integrate_simpson,
    integrate_trapezoid,
)



A: float = 0.0
B: float = 1.0
EXACT: float = math.e - 1.0  # I = e - 1

GRID_POWERS = (1, 2, 3)
HALVING_N: List[int] = [10 * 2**k for k in range(6)]


def make_nodes(n_intervals: int) -> NDArray[np.float64]:
    return np.linspace(A, B, num=n_intervals + 1, dtype=np.float64)


def compute_errors(
    methods: Dict[str, IntegrationMethod],
    function: Integrand,
    n_list: List[int],
) -> Dict[str, List[float]]:
    errors: Dict[str, List[float]] = {name: [] for name in methods}
    for n in n_list:
        nodes = make_nodes(n)
        for name, method in methods.items():
            errors[name].append(abs(method(nodes, function) - EXACT))
    return errors


def main() -> None:
    f: Integrand = lambda x: math.exp(x)

    methods: Dict[str, IntegrationMethod] = {
        "Левые прямоугольники": integrate_left_rectangles,
        "Правые прямоугольники": integrate_right_rectangles,
        "Средние прямоугольники": integrate_midpoint_rectangles,
        "Трапеции": integrate_trapezoid,
        "Симпсон": integrate_simpson,
    }

    # ---------- 1. Три сетки: таблица и график ----------
    n_list = [10**k for k in GRID_POWERS]
    steps = [(B - A) / n for n in n_list]
    errors = compute_errors(methods, f, n_list)

    print(f"Точное значение: e - 1 = {EXACT:.15f}\n")
    for i, n in enumerate(n_list):
        nodes = make_nodes(n)
        print(f"Сетка: n = {n}, узлов {nodes.size}, h = {steps[i]:g}")
        print(f"  {'Метод':<24}{'I_h':>20}{'|I_h - I|':>14}")
        for name, method in methods.items():
            value = method(nodes, f)
            print(f"  {name:<24}{value:>20.15f}{errors[name][i]:>14.3e}")
        print()

    print("Наблюдаемый порядок p = ln(E1/E2) / ln(h1/h2) между соседними сетками:")
    for name in methods:
        orders = [
            math.log(errors[name][i] / errors[name][i + 1])
            / math.log(steps[i] / steps[i + 1])
            for i in range(len(n_list) - 1)
        ]
        print(f"  {name:<24}" + "  ".join(f"{p:6.2f}" for p in orders))

    fig, ax = plt.subplots(figsize=(8, 5.5))
    for name in methods:
        # Нулевую погрешность на логарифмической оси показать нельзя.
        pts = [(h, e) for h, e in zip(steps, errors[name]) if e > 0]
        if pts:
            hs, es = zip(*pts)
            ax.loglog(hs, es, marker="o", label=name, linestyle="--")
    ax.set_xlabel("Шаг сетки h")
    ax.set_ylabel("Абсолютная погрешность")
    ax.set_title("Интеграл от экспоненты с 30г белка на [0, 1]")
    ax.grid(True, which="both", alpha=0.4)
    ax.legend()
    fig.tight_layout()

    # ---------- 2. Деление шага пополам: во сколько раз падает погрешность ----------
    half_errors = compute_errors(methods, f, HALVING_N)
    print("\nОтношение E(h) / E(h/2) при делении шага пополам:")
    print(f"  {'Метод':<24}" + "".join(f"{f'{n}->{2*n}':>10}" for n in HALVING_N[:-1]))
    for name in methods:
        ratios = [
            half_errors[name][i] / half_errors[name][i + 1]
            for i in range(len(HALVING_N) - 1)
        ]
        print(f"  {name:<24}" + "".join(f"{r:>10.2f}" for r in ratios))

    plt.show()


if __name__ == "__main__":
    main()
