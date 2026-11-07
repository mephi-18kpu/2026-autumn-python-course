import numpy as np
import matplotlib.pyplot as plt
from integration_methods import (
    Integrand,
    IntegrationMethod,
    integrate_left_rectangles,
    integrate_right_rectangles,
    integrate_midpoint_rectangles,
    integrate_trapezoid,
    integrate_simpson,
)

def main():
    function: Integrand = lambda x: float(np.exp(x))
    exact = np.e - 1

    methods: list[tuple[str, IntegrationMethod]] = [
        ("Левые прямоугольники", integrate_left_rectangles),
        ("Правые прямоугольники", integrate_right_rectangles),
        ("Средние прямоугольники", integrate_midpoint_rectangles),
        ("Трапеции", integrate_trapezoid),
        ("Симпсон", integrate_simpson), ]

    fig, ax = plt.subplots()
    print("Метод | Интервал | Шаг | Интеграл | Ошибка | Разница (во сколько меньше)")

    for name, method in methods:
        steps = []
        errors = []
        previous_error = None

        for n in [4, 8, 16, 32, 64]:
            nodes = np.linspace(0, 1, n + 1, dtype=np.float64)
            h = nodes[1] - nodes[0]

            result = method(nodes, function)
            error = abs(result - exact)

            ratio = "—"
            if previous_error is not None and error != 0:
                ratio = f"{previous_error / error:.2f}"

            print(f"{name} | {n} | {h:.5f} | {result:.8f} | {error:.3e} | {ratio}")

            steps.append(h)
            errors.append(error)
            previous_error = error
        ax.loglog(steps, errors, marker="o", label=name)

    ax.set_xlabel("Шаг h")
    ax.set_ylabel("Абсолютная погрешность")
    ax.set_title("Сравнение методов")
    ax.grid(True)
    ax.legend()
    fig.tight_layout()
    plt.show()
if __name__ == "__main__":
    main()
