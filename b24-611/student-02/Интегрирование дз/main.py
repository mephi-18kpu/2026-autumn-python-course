import numpy as np
import matplotlib.pyplot as plt
from integration_methods import (
Integrand, IntegrationMethod, integrate_left_rectangles,
integrate_right_rectangles, integrate_midpoint_rectangles,
integrate_simpson, integrate_trapezoid
)

def main():
    f: Integrand = lambda x: np.exp(x)
    a, b = 0.0, 1.0
    exact_value = np.e - 1
    intervals = [2, 4, 8, 16, 32, 64]         #для симпсона надо соблюсти чётность
    errors = {
        "left": [], "right": [], "midpoint": [],
        "trapezoid": [], "simpson": []
    }
    steps = []
    print(f"{'Шаг (h)':<10} | {'Левые':<10} | {'Правые':<10} | {'Средние':<10} | {'Трапеции':<10} | {'Симпсон':<10}")
    print("-" * 75)

    for n in intervals:
        nodes = np.linspace(a, b, n + 1, dtype=np.float64)
        h = nodes[1] - nodes[0]
        steps.append(h)

        errors["left"].append(abs(integrate_left_rectangles(nodes, f) - exact_value))
        errors["right"].append(abs(integrate_right_rectangles(nodes, f) - exact_value))
        errors["midpoint"].append(abs(integrate_midpoint_rectangles(nodes, f) - exact_value))
        errors["trapezoid"].append(abs(integrate_trapezoid(nodes, f) - exact_value))
        errors["simpson"].append(abs(integrate_simpson(nodes, f) - exact_value))

        print(
            f"{h:<10.5f} | {errors['left'][-1]:<10.5e} | {errors['right'][-1]:<10.5e} | {errors['midpoint'][-1]:<10.5e} | {errors['trapezoid'][-1]:<10.5e} | {errors['simpson'][-1]:<10.5e}")

    plt.figure(figsize=(10, 8))

    plt.loglog(steps, errors["left"], 'o-', label="левые_прямоугольники")
    plt.loglog(steps, errors["right"], 's-', label="правые_прямоугольники")
    plt.loglog(steps, errors["midpoint"], '^-', label="средние_прямоугольники")
    plt.loglog(steps, errors["trapezoid"], 'd-', label="трапеции")
    plt.loglog(steps, errors["simpson"], '*-', label="параболы")

    plt.xlabel("шаг сетки h")
    plt.ylabel("абсолютная погрешность")
    plt.title("зависимость погрешности от шага сетки")
    plt.grid(True, which="both", ls="--")
    plt.legend()
    plt.savefig("график_погрешностей.png", dpi=150)
    plt.show()

if __name__ == "__main__":
 main()
