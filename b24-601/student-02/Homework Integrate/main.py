import numpy as np
import matplotlib.pyplot as plt
import math
from integration_methods import (
    Integrand,
    IntegrationMethod,
    integrate_left_rectangles,
    integrate_midpoint_rectangles,
    integrate_right_rectangles,
    integrate_trapezoid,
    integrate_simpson,
)

# Подынтегральная функция f(x) = e^x
f: Integrand = lambda x: math.exp(x)
# Точное значение интеграла на [0, 1]
EXACT_VALUE: float = math.e - 1.0
METHODS: dict[str, IntegrationMethod] = {
    "Левые прямоуг.": integrate_left_rectangles,
    "Правые прямоуг.": integrate_right_rectangles,
    "Средние прямоуг.": integrate_midpoint_rectangles,
    "Трапеции": integrate_trapezoid,
    "Симпсон": integrate_simpson,
}
def run_experiment() -> None:
    # Списки для накопления результатов
    steps: list[float] = []
    errors: dict[str, list[float]] = {name: [] for name in METHODS}

    num_nodes_list = [2**k + 1 for k in range(2, 8)]
    header = f"{'N':>5} | {'h':>10} | " + " | ".join(f"{name:>14}" for name in METHODS)
    print(header)
    print("-" * len(header))

    for num_nodes in num_nodes_list:
        # Равномерная сетка на [0, 1]
        nodes = np.linspace(0.0, 1.0, num=num_nodes, dtype=np.float64)
        h = float(nodes[1] - nodes[0])
        steps.append(h)

        row = f"{num_nodes:>5} | {h:>10.6f} | "
        for name, method in METHODS.items():
            approx = method(nodes, f)
            error = abs(approx - EXACT_VALUE)
            errors[name].append(error)
            row += f"{error:>14.2e} | "
        print(row)

    # Построение графика
    fig, ax = plt.subplots(figsize=(10, 6))

    for name in METHODS:
        ax.loglog(steps, errors[name], marker="o", label=name)

    ax.set_title("Зависимость погрешности от шага сетки")
    ax.set_xlabel("Шаг сетки h")
    ax.set_ylabel("Абсолютная погрешность E(h)")
    ax.legend()
    ax.grid(True, which="both", linestyle="--", alpha=0.6)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_experiment()
