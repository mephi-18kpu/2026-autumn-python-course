import numpy as np
from numpy.typing import NDArray
import matplotlib.pyplot as plt
from Integration_methods import integrate_trapezoid, integrate_simpson, integrate_left_rectangles, integrate_right_rectangles, integrate_midpoint_rectangles
from Integration_methods.type_aliases import Integrand, IntegrationMethod
def main() -> None:
    f: Integrand = lambda x: np.exp(x)
    a, b, n_1 = 0.0, 1.0, 102
    I = np.e - 1
    x: NDArray[np.float64] = np.linspace(a, b, n_1, dtype=np.float64)

    method_left: IntegrationMethod = integrate_left_rectangles
    method_right: IntegrationMethod = integrate_right_rectangles
    method_mid: IntegrationMethod = integrate_midpoint_rectangles
    method_trap: IntegrationMethod = integrate_trapezoid
    method_simpson: IntegrationMethod = integrate_simpson

    result_left: float = method_left(x, f)
    result_right: float = method_right(x, f)
    result_mid: float = method_mid(x, f)
    result_trap: float = method_trap(x, f)
    result_simpson: float = method_simpson(x, f)
    #Табличка
    print(f"Точное значение интеграла: {I:.8f}\n")
    print(f"{'Метод':<25} | {'Результат':<15} | {'Абс. погрешность':<15}")
    print("-" * 62)
    print(f"{'Левые прямоугольники':<25} | {result_left:<15.8f} | {abs(result_left - I):<15.2e}")
    print(f"{'Правые прямоугольники':<25} | {result_right:<15.8f} | {abs(result_right - I):<15.2e}")
    print(f"{'Средние прямоугольники':<25} | {result_mid:<15.8f} | {abs(result_mid - I):<15.2e}")
    print(f"{'Трапеции':<25} | {result_trap:<15.8f} | {abs(result_trap - I):<15.2e}")
    print(f"{'Симпсон':<25} | {result_simpson:<15.8f} | {abs(result_simpson - I):<15.2e}")
    print()

    n_2 = [7, 25, 101, 301, 601, 901, 1001, 2019]
    h = []
    err_left, err_right, err_mid, err_trap, err_simp = [], [], [], [], []
    for i in n_2:
        m = (b - a) / (i - 1)
        h.append(m)
        x_plot: NDArray[np.float64] = np.linspace(a, b, i, dtype=np.float64)
        #Подсчет значений интеграла
        err_left.append(abs(integrate_left_rectangles(x_plot, f) - I))
        err_right.append(abs(integrate_right_rectangles(x_plot, f) - I))
        err_mid.append(abs(integrate_midpoint_rectangles(x_plot, f) - I))
        err_trap.append(abs(integrate_trapezoid(x_plot, f) - I))
        err_simp.append(abs(integrate_simpson(x_plot, f) - I))

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.loglog(h, err_left, 'o-', label='Левые прямоугольники')
    ax.loglog(h, err_right, 's-', label='Правые прямоугольники')
    ax.loglog(h, err_mid, '^-', label='Средние прямоугольники')
    ax.loglog(h, err_trap, 'd-', label='Трапеции')
    ax.loglog(h, err_simp, '*-', label='Симпсон')

    ax.set_title('Зависимость абсолютной погрешности от шага сетки h')
    ax.set_xlabel('Шаг сетки h')
    ax.set_ylabel('Абсолютная погрешность')
    ax.grid(True, which="both", ls="--", alpha=0.7)
    ax.legend()

    plt.show()


if __name__ == "__main__":
    main()