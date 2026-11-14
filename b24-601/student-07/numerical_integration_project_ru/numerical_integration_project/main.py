"""Запуск эксперимента по численному интегрированию и построение графика."""

import numpy as np
import matplotlib.pyplot as plt

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
    """Сравнивает пять методов для интеграла экспоненты на отрезке [0, 1]."""

    # Подынтегральная функция: f(x) = e в степени x.
    function: Integrand = lambda x: float(np.exp(x))

    # Точное значение интеграла от e в степени x на [0, 1]: e - 1.
    exact_value = float(np.e - 1.0)

    # Словарь связывает название метода с соответствующей функцией.
    methods: dict[str, IntegrationMethod] = {
        "Левые прямоугольники": integrate_left_rectangles,
        "Правые прямоугольники": integrate_right_rectangles,
        "Средние прямоугольники": integrate_midpoint_rectangles,
        "Трапеции": integrate_trapezoid,
        "Симпсон": integrate_simpson,
    }

    # Число интервалов удваивается на каждом следующем шаге.
    # Для метода Симпсона число интервалов должно быть чётным.
    interval_counts = [4, 8, 16, 32, 64, 128, 256, 512]

    # Для каждого метода создаём отдельный список погрешностей.
    errors: dict[str, list[float]] = {
        name: [] for name in methods
    }
    steps: list[float] = []

    print(f"Точное значение интеграла: {exact_value:.15f}\n")

    header = f"{'Интервалы':>10} {'Шаг сетки':>14}"
    for name in methods:
        header += f" {name:>24}"
    print(header)
    print("-" * len(header))

    # Проводим вычисления для каждого количества интервалов.
    for intervals in interval_counts:
        # Число узлов на единицу больше числа интервалов.
        nodes = np.linspace(
            0.0,
            1.0,
            intervals + 1,
            dtype=np.float64,
        )

        # Находим расстояние между соседними узлами.
        step = float(nodes[1] - nodes[0])
        steps.append(step)

        row_errors = []

        # Последовательно запускаем все пять методов.
        for name, method in methods.items():
            approximation = method(nodes, function)

            # Абсолютная погрешность — модуль разности
            # приближённого и точного значений интеграла.
            error = abs(approximation - exact_value)

            errors[name].append(error)
            row_errors.append(error)

        # Выводим строку таблицы для текущей сетки.
        row = f"{intervals:10d} {step:14.6g}"
        for error in row_errors:
            row += f" {error:24.8e}"
        print(row)

    # Создаём фигуру и область для построения графика.
    fig, ax = plt.subplots(figsize=(10, 6))

    # Для каждого метода строим зависимость погрешности от шага.
    for name, method_errors in errors.items():
        # На логарифмической оси нельзя отображать нулевые значения.
        valid = [
            (h, error)
            for h, error in zip(steps, method_errors)
            if error > 0.0
        ]

        if valid:
            plot_steps, plot_errors = zip(*valid)

            ax.loglog(
                plot_steps,
                plot_errors,
                marker="o",
                label=name,
            )

    # Подписываем оси, добавляем заголовок, сетку и легенду.
    ax.set_xlabel("Шаг сетки h")
    ax.set_ylabel("Абсолютная погрешность")
    ax.set_title("Погрешность методов численного интегрирования")
    ax.grid(True, which="both", linestyle="--", alpha=0.6)
    ax.legend()

    fig.tight_layout()
    plt.show()

    # Выводим ожидаемые теоретические порядки точности.
    print("\nОжидаемые порядки суммарной погрешности:")
    print("- Левые и правые прямоугольники: O(h). При делении шага пополам ошибка примерно в 2 раза меньше.")
    print("- Средние прямоугольники и трапеции: O(h^2). Ошибка примерно в 4 раза меньше.")
    print("- Метод Симпсона: O(h^4). Ошибка примерно в 16 раз меньше.")


if __name__ == "__main__":
    main()
