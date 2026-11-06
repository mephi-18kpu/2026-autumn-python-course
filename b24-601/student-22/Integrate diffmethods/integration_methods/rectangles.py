import numpy as np
from numpy.typing import NDArray
from .type_aliases import Integrand

def integrate_left_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    h = nodes[1] - nodes[0]
    total_sum = 0.0
    for i in range(0, len(nodes) - 1):
        total_sum += function(nodes[i])
    return float(h * total_sum)

def integrate_right_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    h = nodes[1] - nodes[0]
    total_sum = 0.0
    for i in range(1, len(nodes)):
        total_sum += function(nodes[i])
    return float(h * total_sum)

def integrate_midpoint_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    h = nodes[1] - nodes[0]
    total_sum = 0.0
    for i in range(0, len(nodes) - 1):
        mid = (nodes[i] + nodes[i + 1]) / 2.0
        total_sum += function(mid)
    return float(h * total_sum)