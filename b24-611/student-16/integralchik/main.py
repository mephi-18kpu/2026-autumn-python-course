
import math
from typing import List

import matplotlib.pyplot as plt
import numpy as np

from integration_methods import (
    Integrand,
    Integration_Method,
    integrate_left_rectangles,
    integrate_midpoint_rectangles,
    integrate_right_rectangles,
    integrate_simpson,
    integrate_trapezoid,
)

f: Integrand = lambda x: np.exp(x)
EXACT_I: float = np.exp(1.0) - 1.0


def main() -> None:
    
    segments = [4, 8, 16, 32, 64, 128, 256, 512]


    h_list: List[float] = []
    err_left: List[float] = []
    err_right: List[float] = []
    err_mid: List[float] = []
    err_trap: List[float] = []
    err_simp: List[float] = []

    print("Segm | Step (h)  | Left Rect | Right Rect| Midpoint  | Trapezoid | Simpson")
    print("-" * 78)

    for n in segments:
       
        grid = np.linspace(0.0, 1.0, n + 1, dtype=np.float64)
        h = float(grid[1] - grid[0])
        h_list.append(h)

        res_left = integrate_left_rectangles(grid, f)
        res_right = integrate_right_rectangles(grid, f)
        res_mid = integrate_midpoint_rectangles(grid, f)
        res_trap = integrate_trapezoid(grid, f)
        res_simp = integrate_simpson(grid, f)

        e_left = abs(res_left - EXACT_I)
        e_right = abs(res_right - EXACT_I)
        e_mid = abs(res_mid - EXACT_I)
        e_trap = abs(res_trap - EXACT_I)
        e_simp = abs(res_simp - EXACT_I)

        err_left.append(e_left)
        err_right.append(e_right)
        err_mid.append(e_mid)
        err_trap.append(e_trap)
        err_simp.append(e_simp)

        
        print(
            f"{n:<4} | {h:.3e} | {e_left:.3e} | {e_right:.3e} | {e_mid:.3e} | {e_trap:.3e} | {e_simp:.3e}"
        )

    fig, ax = plt.subplots(figsize=(9, 6))

    ax.loglog(h_list, err_left, "o-", label="Left Rectangles")
    ax.loglog(h_list, err_right, "o-", label="Right Rectangles")
    ax.loglog(h_list, err_mid, "o-", label="Midpoint Rectangles")
    ax.loglog(h_list, err_trap, "o-", label="Trapezoid")
    ax.loglog(h_list, err_simp, "o-", label="Simpson")

    ax.set_title("График погрешностей численного интегрирования")
    ax.set_xlabel("Шаг сетки h")
    ax.set_ylabel("Абсолютная погрешность E(h)")
    ax.grid(True, which="both", linestyle=":")
    ax.legend()

    ax.set_xlim(max(h_list) * 1.2, min(h_list) * 0.8)

    plt.show()


if __name__ == "__main__":
    main()

