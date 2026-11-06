import numpy as np
import matplotlib.pyplot as plt
from numpy.typing import NDArray

from integration_methods import (
    Integrand,
    IntegrationMethod,
    integrate_left_rectangles,
    integrate_midpoint_rectangles,
    integrate_right_rectangles,
    integrate_trapezoid,
    integrate_simpson


)



def main() -> None:
    function: Integrand = lambda x: np.exp(x)
    trueres = float(np.e - 1)
    a, b = 0.0, 1.0
    ns = [3, 5, 9, 17, 33, 65, 129]
    methods: dict[str, IntegrationMethod] = {
        "Левые": integrate_left_rectangles,
        "Правые": integrate_right_rectangles,
        "Средние": integrate_midpoint_rectangles,
        "Трапеции": integrate_trapezoid,
        "Симпсон": integrate_simpson,
    }

    hs = np.array([(b - a) / (n - 1) for n in ns])
    errs: dict[str, np.ndarray] = {}

    for name, method in methods.items():
        errs[name] = np.array([
            abs(method(np.linspace(a, b, n), function) - trueres)
            for n in ns
        ])


    fig, ax = plt.subplots()
    for name in methods:
        ax.loglog(hs, errs[name], "o-", label=name)
    ax.set_xlabel("Шаг h")
    ax.set_ylabel("Погрешность")
    ax.grid(True, which="both")
    ax.legend()
    plt.show()






if __name__ == "__main__":
    main()
