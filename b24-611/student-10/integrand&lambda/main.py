import numpy as np
import matplotlib.pyplot as plt

from integration_methods import (
    Integrand,
    integrate_mid_rectangles,
    integrate_left_rectangles,
    integrate_right_rectangles,
)

def run():
    integrand: Integrand = Lambda x: float(np.exp(x))
    true_value = float(np.exp(1.0) - 1.0)
    n_intervals = [10, 20, 40, 80, 160, 320]

    steps = []
    errors_left = []
    errors_right = []
    errors_mid = []

    print("-"*67)
    print(f"{"N":>6} | {"шаг h":>10} | {"погр левые":>14} | {"погр правые":>14} | {"погр средние":>14}")
    print("-"*67)

    for n in n_intervals:
        nodes = np.linspace(0.0, 1.0, n+1, dtype=np.float64)

        h = float(nodes[1] - nodes[0])
        steps.append(h)

        err_left = abs(integrate_left_rectangles(nodes, integrand) - true_value)
        err_right = abs(integrate_right_rectangles(nodes, integrand) - true_value)
        err_mid = abs(integrate_mid_rectangles(nodes, integrand) - true_value)

        print(f"{n:6d} | {h:10.5f} | {err_left:14.2e} | {err_right:14.2e} | {err_mid:14.2e}")

    print("-"*67)
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.loglog(steps, errors_left, "o-", label="левые прямоугольники (0(h))")
    ax.loglog(steps, errors_right, "s-", label="правые прямоугольники (0(h))")
    ax.loglog(steps, errors_mid, "^--", label="средние прямоугольники (0(h^2))")

