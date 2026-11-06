import math


import numpy as np
from numpy.typing import NDArray

# User imports
from .type_aliases import Integrand


def _step(nodes: NDArray[np.float64]) -> float:
    if nodes.ndim != 1 or nodes.size < 2:
        raise ValueError("Нужен одномерный массив минимум из двух узлов.")
    return float(nodes[-1] - nodes[0]) / (nodes.size - 1)


def integrate_left_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    h = _step(nodes)
    return h * math.fsum(function(float(x)) for x in nodes[:-1])


def integrate_right_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    h = _step(nodes)
    return h * math.fsum(function(float(x)) for x in nodes[1:])


def integrate_midpoint_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    h = _step(nodes)
    return h * math.fsum(
        function(float(left + right) / 2.0)
        for left, right in zip(nodes[:-1], nodes[1:])
    )
