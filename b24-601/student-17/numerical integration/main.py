import math
import matplotlib.pyplot as plt
import numpy as np

from integration_methods import (
    integrate_left_rectangles,
    integrate_right_rectangles,
    integrate_midpoint_rectangles,
    integrate_trapezoid,
    integrate_simpson,
)

def main():
    f = lambda x: math.exp(x)
    exact = math.e - 1.0
    
    a, b = 0.0, 1.0
    intervals = (4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048)
    
    methods = [
        ("Левые прямоугольники", integrate_left_rectangles),
        ("Правые прямоугольники", integrate_right_rectangles),
        ("Средние прямоугольники", integrate_midpoint_rectangles),
        ("Трапеции", integrate_trapezoid),
        ("Симпсон", integrate_simpson),
    ]

    print(f"Точный интеграл: {exact:.12f}\n")
    
    steps_dict, errors_dict = {}, {}

    for name, method in methods:
        steps, errors = [], []
        print(f"--- {name} ---")
        for n in intervals:
            nodes = np.linspace(a, b, n + 1, dtype=np.float64)
            h = float(nodes[1] - nodes[0])
            approx = method(nodes, f)
            err = abs(approx - exact)
            
            steps.append(h)
            errors.append(err)
            print(f"n={n:4d} | h={h:.5f} | err={err:.2e}")
        
        steps_dict[name] = steps
        errors_dict[name] = errors
        print()

    # График
    fig, ax = plt.subplots(figsize=(8, 5))
    for name in steps_dict:
        ax.loglog(steps_dict[name], errors_dict[name], marker="o", label=name)
        
    ax.set_xlabel("Шаг h (log)")
    ax.set_ylabel("Погрешность E(h) (log)")
    ax.set_title("Сравнение погрешностей методов интегрирования")
    ax.grid(True, which="both")
    ax.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()