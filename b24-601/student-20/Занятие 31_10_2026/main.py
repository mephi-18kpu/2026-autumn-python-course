"""."""

# System imports

# External imports
import matplotlib.pyplot as plt
import numpy as np

# User imports
import integration_methods as im

#############################################

given_function: im.Integrand = lambda x: np.exp(x)


def generate_nets(h: int = 10) -> list:
    """Создает наборы разбиений. Только на количество интервалов кратных 10.

    Args:
        h: первое количество разбиений

    Returns:
        Массив с наборами узлов с шагом от 10 до 1000

    """

    sets = []
    steps = []

    while h <= 1000:
        steps.append(h)
        sets.append(np.linspace(0, 1, h + 1))
        h += 10

    return sets, steps


def error_calculation(pre_result: list) -> list:
    """ Расчет погрешностей измерений.

        Args:
            pre_result: Список полученных значений определенного интеграла.

        Returns:
            Список рассчитанных погрешностей.

    """

    for index in range(len(pre_result)):
        pre_result[index] = abs(pre_result[index] - np.exp(1) + 1)

    return pre_result


def create_plot(h: list, results: dict) -> None:
    """ Построение графика E(h) для оценки погрешности.

    Args:
        h: Величина откладываемая по оси x - разбиение отрезка.
        results: Результаты расчета погрешностей.

    Returns:
        Построенный график.
    """

    fig, ax = plt.subplots(figsize=(8, 4))
    for method in results:
        plt.loglog(h, results[method], label=method)
    ax.set_xlabel("h")
    ax.set_ylabel("E(h)")
    ax.set_title("Сравнение погрешностей на графике.")
    ax.grid(True)
    plt.legend()
    plt.show()

    return None


def print_results() -> None:
    """Выводит численные значения, посчитанные разными способами, для исходного интеграла"""

    print("Результат вычисления для одного разбиения (h = 100000) с помощью метода:")
    h = np.linspace(0, 1, 100000 + 1)
    print(f"Методом левых прямоугольников: {im.integrate_left_rectangles(h, given_function):.5f}")
    print(f"Методом правых прямоугольников: {im.integrate_right_rectangles(h, given_function):.5f}")
    print(f"Методом средних прямоугольников: {im.integrate_midpoint_rectangles(h, given_function):.5f}")
    print(f"Методом трапеций: {im.integrate_trapezoid(h, given_function):.5f}")
    print(f"Методом Симпсона: {im.integrate_simpson(h, given_function):.5f}")
    print(f"Истинное значение: {(np.exp(1) - 1):.5f}")

    return None


if __name__ == "__main__":
    h_values, h_steps = generate_nets()
    results_errors = {
        "Метод левых прямоугольников": error_calculation(
            [im.integrate_left_rectangles(h_values[index], given_function)
             for index in range(len(h_values))]),
        "Метод правых прямоугольников": error_calculation(
            [im.integrate_right_rectangles(h_values[index], given_function)
             for index in range(len(h_values))]),
        "Метод средних прямоугольников": error_calculation(
            [im.integrate_midpoint_rectangles(h_values[index], given_function)
             for index in range(len(h_values))]),
        "Метод трапеций": error_calculation(
            [im.integrate_trapezoid(h_values[index], given_function) for index in range(len(h_values))]),
        "Метод Симпсона": error_calculation(
            [im.integrate_simpson(h_values[index], given_function) for index in range(len(h_values))]),
    }
    print_results()
    create_plot(h_steps, results_errors)
