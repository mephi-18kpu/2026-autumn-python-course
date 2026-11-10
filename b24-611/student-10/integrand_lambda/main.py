import numpy as np
import matplotlib.pyplot as plt
from integration_methods import (
    Integrand,
    integrate_left_rectangles,
    integrate_right_rectangles,
    integrate_midpoint_rectangles,
    integrate_trapezoid,
    integrate_simpson,
)


def main() -> None:
    # подынтегральная функция: e^x
    f: Integrand = lambda x: float(np.exp(x))

    # точное значение
    exact = float(np.e - 1.0)

    # число интервалов (для Симпсона чётное => n+1 нечётно)
    n_intervals = [10, 20, 40, 80, 160, 320]

    # методы: имя -> функция
    methods = {
        "левые":    integrate_left_rectangles,
        "правые":   integrate_right_rectangles,
        "средние":  integrate_midpoint_rectangles,
        "трапеции": integrate_trapezoid,
        "Симпсон":  integrate_simpson,
    }

   
    errors = {name: [] for name in methods}
    steps = []  # шаги h

   
    header = f'{"N":>6} | {"h":>10} | ' + ' | '.join(f'{name:>12}' for name in methods)
    line = '-' * len(header)
    print(line)
    print(header)
    print(line)

    for n in n_intervals:
        nodes = np.linspace(0.0, 1.0, n + 1, dtype=np.float64)
        h = float(nodes[1] - nodes[0])
        steps.append(h)

        row = [f'{n:6d}', f'{h:10.5f}']
        for name, method in methods.items():
            approx = method(nodes, f)
            err = abs(approx - exact)
            errors[name].append(err)
            row.append(f'{err:12.2e}')
        print(' | '.join(row))

    print(line)

    for name, errs in errors.items():
        plt.loglog(steps, errs, marker="o", label=name)
    plt.xlabel("Шаг сетки h")
    plt.ylabel("Абсолютная погрешность")
    plt.title("Сходимость методов интегрирования")
    plt.legend()
    plt.grid(True, which="both")
    plt.show()


if __name__ == "__main__":
    main()
