import math
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

def main() -> None:
    function: Integrand = lambda x: math.exp(x)
    etalon = math.e - 1

    methods: dict[str, IntegrationMethod] = {
        "Левые прямоугольники": integrate_left_rectangles,
        "Правые прямоугольники": integrate_right_rectangles,
        "Средние прямоугольники": integrate_midpoint_rectangles,
        "Трапеции": integrate_trapezoid,
        "Симпсон": integrate_simpson,
    }

    n_values = [4, 8, 16, 32, 64, 128, 256]
    results: dict[str, list[float]] = {name: [] for name in methods}
    step_h: list[float] = []

    for n in n_values:
        nodes = np.linspace(0, 1, n+1, dtype=np.float64)
        h = nodes[1] - nodes[0]
        step_h.append(h)

        for name, method in methods.items():
            znachenie = method(nodes, function)
            error = abs(znachenie-etalon)
            results[name].append(error)

    plt.figure(figsize=(10,6))

    markers = ['o', 's', '^', 'v', 'D']

    for (name, errors), marker in zip(results.items(), markers):
        plt.loglog(step_h, errors, marker=marker, label=name)


    plt.title("Зависимость абсолютной погрешности от шага сетки")
    plt.xlabel("Шаг сетки (h)")
    plt.ylabel("Абсолютная погрешность")
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
