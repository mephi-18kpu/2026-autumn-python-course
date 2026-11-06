"""Сравнение пяти методов численного интегрирования"""

import math

import matplotlib.pyplot as plt
import numpy as np

from integration_methods import (
    Integrand,
    IntegrationMethod,
    integrate_left_rectangles,
    integrate_midpoint_rectangles,
    integrate_right_rectangles,
    integrate_simpson,
    integrate_trapezoid,
)


def main() -> None:
    # f(x) = e^x.
    function: Integrand = lambda x: math.exp(x)

    a = 0.0
    b = 1.0
    exact_value = math.e - 1.0

    # Методы в словарь
    methods: dict[str, IntegrationMethod] = {
        "Левые прямоугольники": integrate_left_rectangles,
        "Правые прямоугольники": integrate_right_rectangles,
        "Средние прямоугольники": integrate_midpoint_rectangles,
        "Трапеции": integrate_trapezoid,
        "Симпсона": integrate_simpson,
    }

    # В сетках нечётное число узлов, (чтобы работал метод симпсона)
    node_counts = [3, 5, 9, 17, 33, 65, 129]

    steps: list[float] = []
    errors: dict[str, list[float]] = {}

    for method_name in methods:
        errors[method_name] = []

    print(f"Значение интеграла: {exact_value:.15f}")
    print()
    print(
        f"{'Узлов':>5}  {'Шаг h':>12}  {'Метод':<25}  "
        f"{'Результат':>18}  {'Абс. погрешность':>18}"
    )
    print("-" * 91)

    # Расчет ин-ла каждым методом
    for node_count in node_counts:
        nodes = np.linspace(a, b, node_count, dtype=np.float64)
        step = float(nodes[1] - nodes[0])
        steps.append(step)

        for method_name, method in methods.items():
            result = method(nodes, function)
            error = abs(exact_value - result)
            errors[method_name].append(error)

            print(
                f"{node_count:>5}  {step:>12.6e}  {method_name:<25}  "
                f"{result:>18.12f}  {error:>18.6e}"
            )

        print("-" * 91)

    # Сравнение шагов сетки
    print("\nУменьшение погрешности при делении шага пополам:")
    for method_name in methods:
        print(f"\n{method_name}:")
        method_errors = errors[method_name]

        for i in range(1, len(method_errors)):
            ratio = method_errors[i - 1] / method_errors[i]
            print(f"  {node_counts[i - 1]:>3} -> {node_counts[i]:>3} узлов: {ratio:.3f} раза")

    # Графики погрещностей
    figure, axes = plt.subplots()

    for method_name, method_errors in errors.items():
        axes.loglog(
            steps[::-1],
            method_errors[::-1],
            marker="o",
            label=method_name,
        )

    axes.set_title("Абсолютная погрешность методов интегрирования")
    axes.set_xlabel("Шаг сетки h")
    axes.set_ylabel("Абсолютная погрешность")
    axes.grid(True, which="both")
    axes.legend()

    plt.tight_layout()
    plt.savefig("integration_errors.png", dpi=150)
    print("\nГрафик сохранён в файл integration_errors.png")
    plt.show()


if __name__ == "__main__":
    main()
