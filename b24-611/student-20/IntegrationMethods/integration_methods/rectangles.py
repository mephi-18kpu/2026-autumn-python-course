import numpy as np
from numpy.typing import NDArray

from .type_aliases import Integrand

def integrate_left_rectangles(
    nodes: NDArray[np.float64],
    func: Integrand,
) -> float:

    if len(nodes) < 2:
        raise ValueError("Нужно хотя бы два узла")

    total = 0.0
    for index in range(len(nodes) - 1):
        width = nodes[index + 1] - nodes[index]
        total += width * func(nodes[index])
    return total


def integrate_right_rectangles(
    nodes: NDArray[np.float64],
    func: Integrand,
) -> float:

    if len(nodes) < 2:
        raise ValueError("Нужно хотя бы два узла")

    total = 0.0
    for index in range(len(nodes) - 1):
        width = nodes[index + 1] - nodes[index]
        total += width * func(nodes[index + 1])
    return total


def integrate_midpoint_rectangles(
    nodes: NDArray[np.float64],
    func: Integrand,
) -> float:

    if len(nodes) < 2:
        raise ValueError("Нужно хотя бы два узла")

    total = 0.0
    for index in range(len(nodes) - 1):
        width = nodes[index + 1] - nodes[index]
        middle = (nodes[index] + nodes[index + 1]) / 2
        total += width * func(middle)
    return total
