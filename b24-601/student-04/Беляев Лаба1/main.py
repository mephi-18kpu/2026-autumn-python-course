import numpy as np
import matplotlib.pyplot as plt
from integration_methods import (
    Integrand,
    integrate_left_rectangles,
    integrate_midpoint_rectangles,
    integrate_right_rectangles,
    integrate_trapezoid,
    integrate_simpson,
)


def main():
    f: Integrand = lambda x: float(np.exp(x))
    # Границы интегрирования
    a, b = 0.0, 1.0

    exact_value = float(np.exp(1.0) - np.exp(0.0))

    #
    # Обычно задают количество элементов, а не количество узлов.
    # Так что в следующих работах задавай именно количество элементов
    #

    # Список количества интервалов
    intervals_counts = [4, 8, 16, 32, 64, 128, 256]
    # Словари для каждого из методов
    steps = []
    errors = {
        "Левые прям.": [],
        "Правые прям.": [],
        "Средние прям.": [],
        "Трапеции": [],
        "Симпсон": []
    }

    # Шапка таблицы
    print(
        f"{'Интервалов':<12} | {'Шаг h':<10} | {'Погр Левые':<11} | {'Погр Правые':<11} | {'Погр Средние':<11} | {'Погр Трап':<11} | {'Погр Симпс':<11}")
    print("-" * 90)

    #
    # У тебя уже есть словарь методов, так что лучше тоже в цикле проходить по
    # всем методам, чтобы при изменении количества элементов не надо было
    # править сам цикл для всех интервалов
    #

    for n in intervals_counts:
        num_nodes = n + 1  # Узлов на 1 больше интервалов

        # Равномерная сетка узлов
        nodes = np.linspace(a, b, num_nodes, dtype=np.float64)
        h = (b - a) / n
        steps.append(h)

        # Интегралы каждым методом
        i_left = integrate_left_rectangles(nodes, f)
        i_right = integrate_right_rectangles(nodes, f)
        i_mid = integrate_midpoint_rectangles(nodes, f)
        i_trap = integrate_trapezoid(nodes, f)
        i_simp = integrate_simpson(nodes, f)

        # Абсолютная погрешность каждого метода
        err_left = abs(i_left - exact_value)
        err_right = abs(i_right - exact_value)
        err_mid = abs(i_mid - exact_value)
        err_trap = abs(i_trap - exact_value)
        err_simp = abs(i_simp - exact_value)

        errors["Левые прям."].append(err_left)
        errors["Правые прям."].append(err_right)
        errors["Средние прям."].append(err_mid)
        errors["Трапеции"].append(err_trap)
        errors["Симпсон"].append(err_simp)

        print(
            f"{n:<12} | {h:<10.4f} | {err_left:<11.2e} | {err_right:<11.2e} | {err_mid:<11.2e} | {err_trap:<11.2e} | {err_simp:<11.2e}")

    # ПОСТРОЕНИЕ ГРАФИКА    // Так нейронка пишет, хех
    fig, ax = plt.subplots(figsize=(10, 6))

    # ax.loglog тоже в цикле можно сделать, у тебя для этого вроде даже всё есть
    # Логарифмические линии
    ax.loglog(steps, errors["Левые прям."], 'o-', label="Левые прямоугольники (O(h))")
    ax.loglog(steps, errors["Правые прям."], 's-', label="Правые прямоугольники (O(h))")
    ax.loglog(steps, errors["Средние прям."], '^-', label="Средние прямоугольники (O(h²))")
    ax.loglog(steps, errors["Трапеции"], 'd-', label="Трапеции (O(h²))")
    ax.loglog(steps, errors["Симпсон"], '*-', label="Симпсон (O(h⁴))")

    # НВнешний вид графика
    ax.set_title("Зависимость абсолютной погрешности от шага сетки h (Log-Log)")
    ax.set_xlabel("Шаг сетки h (меньше шагов — левее)")
    ax.set_ylabel("Абсолютная погрешность E(h)")
    ax.grid(True, which="both", linestyle="--", alpha=0.7)
    ax.legend()  # Включаем легенду методов

    # Показываем график
    plt.show()


if __name__ == "__main__":
    main()
