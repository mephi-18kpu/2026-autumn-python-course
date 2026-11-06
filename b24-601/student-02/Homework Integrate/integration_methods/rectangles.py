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
        x = nodes[i]
        total_sum += function(x)
    return float(h * total_sum)


def integrate_right_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    h = nodes[1] - nodes[0]
    total_sum = 0.0
    for i in range(1, len(nodes)):
        x = nodes[i]
        total_sum += function(x)
    return float(h * total_sum)


def integrate_midpoint_rectangles(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    h = nodes[1] - nodes[0]
    total_sum = 0.0
    for i in range(0, len(nodes) - 1):
        x = (nodes[i]+nodes[i+1])/2
        total_sum += function(x)
    return float(h * total_sum)