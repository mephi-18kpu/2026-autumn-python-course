import numpy as np
from numpy.typing import NDArray

from .type_aliases import Integrand

def integrate_left_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    if nodes.ndim != 1 or len(nodes) < 2:
        raise ValueError("Нужна одномерная сетка минимум из двух узлов.")

    h = float(nodes[1] - nodes[0])
    total = 0.0
    for i in range(len(nodes) - 1):
        total += function(float(nodes[i]))
    return float(h * total)


def integrate_right_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    if nodes.ndim != 1 or len(nodes) < 2:
        raise ValueError("Нужна одномерная сетка минимум из двух узлов.")

    h = float(nodes[1] - nodes[0])
    total = 0.0
    for i in range(1, len(nodes)):
        total += function(float(nodes[i]))
    return float(h * total)


def integrate_midpoint_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    if nodes.ndim != 1 or len(nodes) < 2:
        raise ValueError("Нужна одномерная сетка минимум из двух узлов.")

    h = float(nodes[1] - nodes[0])
    total = 0.0
    for i in range(len(nodes) - 1):
        middle = float((nodes[i] + nodes[i + 1]) / 2.0)
        total += function(middle)
    return float(h * total)
