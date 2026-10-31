import numpy as np
from numpy.typing import NDArray
from .type_aliases import Integrand

def integrate_left_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    h = x[1] - x[0]

    return float(h * sum(f(x[i]) for i in range(len(x) - 1)))

def integrate_right_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    h = x[1] - x[0]
    return float(h * sum(f(x[i]) for i in range(1, len(x))))


def integrate_midpoint_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    h = x[1] - x[0]

    return float(h * sum(f((x[i] + x[i + 1]) / 2.0) for i in range(len(x) - 1)))
