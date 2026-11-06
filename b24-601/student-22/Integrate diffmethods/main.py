import matplotlib.pyplot as plt
import numpy as np
from integration_methods import (
    Integrand,
    integrate_left_rectangles,
    integrate_midpoint_rectangles,
    integrate_right_rectangles,
    integrate_simpson,
    integrate_trapezoid,
)

def main() -> None:
    func: Integrand = lambda x: np.float64(np.exp(x))
    exact_integral: float = np.e - 1.0
    n_values = [4, 8, 16, 32, 64, 128, 256]
    methods = {
        "Левые прямоугольники": integrate_left_rectangles,
        "Правые прямоугольники": integrate_right_rectangles,
        "Средние прямоугольники": integrate_midpoint_rectangles,
        "Трапеции": integrate_trapezoid,
        "Симпсон": integrate_simpson,
    }

    steps = []
    errors = {name: [] for name in methods}
    print(f"{'n':<6} | {'Шаг h':<10} | " + " | ".join([f"{name[:18]:<18}" for name in methods]))
    print("-" * 125)
    for n in n_values:
        nodes = np.linspace(0.0, 1.0, n + 1, dtype=np.float64)
        h = nodes[1] - nodes[0]
        steps.append(h)
        row_str = f"{n:<6} | {h:<10.5f} | "
        row_results = []
        for name, method in methods.items():
            val = method(nodes, func)
            err = abs(val - exact_integral)
            errors[name].append(err)
            row_results.append(f"{err:<18.2e}")
        print(row_str + " | ".join(row_results))

    fig, ax = plt.subplots(figsize=(10, 6))
    for name, err_list in errors.items():
        ax.loglog(steps, err_list, marker="o", label=name)
    ax.set_xlabel("Шаг сетки h")
    ax.set_ylabel("Абсолютная погрешность E")
    ax.set_title("Сравнение погрешностей методов численного интегрирования для f(x) = e^x")
    ax.grid(True, which="both", ls="--")
    ax.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()